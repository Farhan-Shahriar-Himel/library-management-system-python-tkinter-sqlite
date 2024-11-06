import tkinter as tk
from tkinter import ttk, messagebox

# Demo books data (list of dictionaries)
demo_books = [
    {"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publish_date": "1925-04-10", "genre": "Fiction", "pages": 1200, "available": True, "language": "English"},
    {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publish_date": "1960-07-11", "genre": "Fiction", "pages": 1500, "available": True, "language": "English"},
    {"book_id": 3, "title": "1984", "author": "George Orwell", "publish_date": "1949-06-08", "genre": "Dystopian", "pages": 800, "available": False, "language": "English"},
    {"book_id": 4, "title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "publish_date": "1967-06-05", "genre": "Magical Realism", "pages": 600, "available": True, "language": "Spanish"},
    {"book_id": 5, "title": "Pride and Prejudice", "author": "Jane Austen", "publish_date": "1813-01-28", "genre": "Romance", "pages": 2000, "available": True, "language": "English"},
    {"book_id": 6, "title": "Brave New World", "author": "Aldous Huxley", "publish_date": "1932-09-01", "genre": "Dystopian", "pages": 700, "available": True, "language": "English"},
    {"book_id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "publish_date": "1951-07-16", "genre": "Fiction", "pages": 900, "available": False, "language": "English"},
    {"book_id": 8, "title": "The Alchemist", "author": "Paulo Coelho", "publish_date": "1988-01-01", "genre": "Adventure", "pages": 1800, "available": True, "language": "Portuguese"},
    {"book_id": 9, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "publish_date": "1880-11-01", "genre": "Philosophical Fiction", "pages": 500, "available": True, "language": "Russian"},
    {"book_id": 10, "title": "War and Peace", "author": "Leo Tolstoy", "publish_date": "1869-01-01", "genre": "Historical Fiction", "pages": 300, "available": False, "language": "Russian"}
]

# Dictionary to store reviews for each book
book_reviews = {book["book_id"]: [] for book in demo_books}

class BooksWindow:
    def __init__(self, master, books):
        self.root = tk.Toplevel(master)
        self.root.title("Library Books")
        self.root.geometry("800x400")

        # Frame for the Treeview
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        # Treeview for displaying books
        self.tree = ttk.Treeview(frame, columns=("ID", "Title", "Author", "Published", "Genre", "Pages", "Available", "Language"), show="headings", yscrollcommand=scrollbar.set)
        
        # Define headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Published", text="Publish Date")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Pages", text="Pages")
        self.tree.heading("Available", text="Available")
        self.tree.heading("Language", text="Language")

        # Define column widths
        self.tree.column("ID", width=50)
        self.tree.column("Title", width=150)
        self.tree.column("Author", width=120)
        self.tree.column("Published", width=100)
        self.tree.column("Genre", width=120)
        self.tree.column("Pages", width=80)
        self.tree.column("Available", width=80)
        self.tree.column("Language", width=100)

        self.tree.pack(fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)

        # Insert books into Treeview
        self.load_books(books)

        # Borrow Book Button
        borrow_button = tk.Button(self.root, text="Borrow Book", command=self.borrow_book)
        borrow_button.pack(pady=10)

        # Review Book Button
        review_button = tk.Button(self.root, text="Review Book", command=self.review_book)
        review_button.pack(pady=10)

        # Frame for displaying reviews
        self.review_frame = tk.Frame(self.root)
        self.review_frame.pack(pady=10)

        # Label for reviews
        self.review_label = tk.Label(self.review_frame, text="Reviews for the selected book:")
        self.review_label.pack()

        # Listbox to display reviews
        self.review_listbox = tk.Listbox(self.review_frame, width=80, height=10)
        self.review_listbox.pack(pady=5)

        # Bind selection event to update reviews
        self.tree.bind("<<TreeviewSelect>>", self.update_reviews)

    def load_books(self, books):
        for book in books:
            self.tree.insert("", "end", values=(book["book_id"], book["title"], book["author"],
                                                 book["publish_date"], book["genre"], book["pages"],
                                                 "Yes" if book["available"] else "No",
                                                 book["language"]))

    def borrow_book(self):
        # Create a borrow book window
        borrow_window = tk.Toplevel(self.root)
        borrow_window.title("Borrow Book")
        borrow_window.geometry("300x150")

        tk.Label(borrow_window, text="Enter Book ID to Borrow:").pack(pady=10)
        book_id_entry = tk.Entry(borrow_window)
        book_id_entry.pack(pady=5)

        tk.Button(borrow_window, text="Borrow", command=lambda: self.confirm_borrow(book_id_entry.get(), borrow_window)).pack(pady=10)

    def confirm_borrow(self, book_id, borrow_window):
        try:
            book_id = int(book_id)
            for book in demo_books:
                if book["book_id"] == book_id:
                    if book["available"]:
                        book["available"] = False
                        self.refresh_books()
                        messagebox.showinfo("Success", f"You have borrowed '{book['title']}'!")
                        borrow_window.destroy()
                    else:
                        messagebox.showwarning("Unavailable", f"'{book['title']}' is currently not available.")
                    return
            messagebox.showerror("Error", "Book ID not found.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid Book ID.")

    def refresh_books(self):
        # Clear and reload the tree view to reflect updated availability
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.load_books(demo_books)

    def review_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a book to review.")
            return

        book_id = self.tree.item(selected_item)["values"][0]
        review_window = tk.Toplevel(self.root)
        review_window.title("Review Book")
        review_window.geometry("300x250")

        tk.Label(review_window, text="Enter your review:").pack(pady=10)
        review_text = tk.Text(review_window, height=5)
        review_text.pack(pady=5)

        tk.Label(review_window, text="Rate (1-5):").pack(pady=10)
        rating_entry = tk.Entry(review_window)
        rating_entry.pack(pady=5)

        tk.Button(review_window, text="Submit", command=lambda: self.submit_review(book_id, review_text.get("1.0", "end-1c"), rating_entry.get(), review_window)).pack(pady=10)

    def submit_review(self, book_id, review_text, rating, review_window):
        if not review_text.strip() or not rating.strip():
            messagebox.showwarning("Input Error", "Please fill in both fields.")
            return

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError:
            messagebox.showerror("Invalid Rating", "Please enter a valid rating between 1 and 5.")
            return

        # Store the review
        book_reviews[book_id].append((review_text, rating))
        messagebox.showinfo("Success", "Review submitted successfully.")
        review_window.destroy()
        self.update_reviews()  # Update reviews display after submission

    def update_reviews(self, event=None):
        self.review_listbox.delete(0, tk.END)  # Clear existing reviews
        selected_item = self.tree.selection()
        if selected_item:
            book_id = self.tree.item(selected_item)["values"][0]
            reviews = book_reviews[book_id]
            for review, rating in reviews:
                self.review_listbox.insert(tk.END, f"Rating: {rating} - {review}")

# Main Application Window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("300x200")

    # Button to open the Books Window
    open_books_button = tk.Button(root, text="View Books", command=lambda: BooksWindow(root, demo_books))
    open_books_button.pack(pady=20)

    root.mainloop()
