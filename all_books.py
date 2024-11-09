import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from data_manage import get_all_books
import webbrowser
from PIL import Image, ImageTk
import io
from data_manage import register_borrow_return, update_book_count, register_review, get_reviews

# Fetch all books from the database


# Dictionary to store reviews for each book
# book_reviews = {book["book_id"]: [] for book in demo_books}

book_reviews = {}

class BookDetailsWindow:
    def __init__(self, master, book, username):
        self.username = username
        self.root = tk.Toplevel(master)
        self.root.title("Book Details")
        self.root.geometry("500x650")

        # Display book details
        tk.Label(self.root, text=f"Title: {book['title']}", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.root, text=f"Writer: {book['writer']}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.root, text=f"Genre: {book['genre']}").pack()
        tk.Label(self.root, text=f"Language: {book['language']}").pack()
        tk.Label(self.root, text=f"Published Year: {book['published_year']}").pack()
        tk.Label(self.root, text=f"Copies Available: {book['no_of_copies']}").pack(pady=5)

        # Display the book's image
        if book['image']:
            image_data = book['image']
            image = Image.open(io.BytesIO(image_data))
            image.thumbnail((200, 300))
            img = ImageTk.PhotoImage(image)
            tk.Label(self.root, image=img).pack(pady=10)
            self.root.image = img

        # Borrow button
        # tk.Button(self.root, text="Borrow Book", command=lambda: self.borrow_book(book)).pack(pady=5)

        # PDF View button
        tk.Button(self.root, text="View Book PDF", command=lambda: self.view_pdf(book)).pack(pady=5)

        # # Review Book button
        # tk.Button(self.root, text="Review Book", command=lambda: self.add_review(book["book_id"])).pack(pady=5)

        # Frame for reviews
        review_frame = tk.Frame(self.root)
        review_frame.pack(pady=10)

        tk.Label(review_frame, text="Reviews:").pack()
        self.review_listbox = tk.Listbox(review_frame, width=60, height=10)
        self.review_listbox.pack(pady=5)
        self.load_reviews(book["book_id"])

    def load_reviews(self, book_id):
        self.review_listbox.delete(0, tk.END)  # Clear previous reviews
        reviews = get_reviews(book_id)
        for review in reviews:
            self.review_listbox.insert(tk.END, f"{review['username']} - {review['review']}")

    def add_review(self, book_id):
        # Prompt user to enter a review
        review_text = simpledialog.askstring("Review Book", "Enter your review:")
        if review_text:
            # Prompt user to enter a rating between 1 and 5
            try:
                rating = int(simpledialog.askstring("Rating", "Enter a rating (1-5):"))
                if 1 <= rating <= 5:
                    book_reviews[book_id].append((review_text, rating))
                    self.review_listbox.insert(tk.END, f"Rating: {rating} - {review_text}")
                    messagebox.showinfo("Success", "Review added successfully!")
                else:
                    messagebox.showwarning("Invalid Rating", "Rating must be between 1 and 5.")
            except (ValueError, TypeError):
                messagebox.showwarning("Invalid Input", "Please enter a valid number for the rating.")

    def borrow_book(self, book):
        if book["no_of_copies"] > 0:
            # register_borrow(book["book_id"], self.username)
            # update_book_count(book['book_id'], True)
            messagebox.showinfo("Success", f"You have borrowed '{book['title']}'!")
        else:
            messagebox.showwarning("Unavailable", "No copies available.")

    def view_pdf(self, book):
        pdf_data = book["book_pdf"]
        if pdf_data:
            with open(f"book_{book['book_id']}.pdf", "wb") as pdf_file:
                pdf_file.write(pdf_data)
            webbrowser.open(f"book_{book['book_id']}.pdf")
        else:
            messagebox.showwarning("No PDF", "No PDF available for this book.")


class BooksWindow:
    def __init__(self, master, username):
        self.username = username
        self.root = tk.Toplevel(master)
        self.root.title("Library Books")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")  # Dark background for a modern dark theme
        
        self.books = get_all_books()
        self.filtered_books = self.books

        # Title of the window
        title_label = tk.Label(self.root, text="Library Book Collection", font=("Helvetica", 16, "bold"), background="#1e1e1e", foreground="#ffffff")
        title_label.pack(pady=10)

        # Search bar frame on the left
        search_frame = tk.Frame(self.root, bg="#1e1e1e")
        search_frame.pack(pady=10, padx=10, side="left", fill="y")

        # Define entry widgets for search criteria
        self.create_search_field(search_frame, "Title", 0, 0)
        self.create_search_field(search_frame, "Writer", 2, 0)
        self.create_search_field(search_frame, "Genre", 4, 0)
        self.create_search_field(search_frame, "Language", 6, 0)
        self.create_search_field(search_frame, "Published Year", 8, 0)

        # Search Button
        search_button = tk.Button(search_frame, text="Search", command=self.search_books, relief="flat", bg="#007ACC", fg="#ffffff", font=("Helvetica", 10, "bold"))
        search_button.grid(row=10, column=0, padx=10, pady=5)

        # Scrollable frame for books
        canvas = tk.Canvas(self.root, bg="#1e1e1e", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        self.scroll_frame = tk.Frame(canvas, bg="#1e1e1e")

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        self.display_books(self.filtered_books)

    def create_search_field(self, frame, label, row, col):
        # Function to create search label and entry field
        label_widget = tk.Label(frame, text=label, font=("Helvetica", 10, "bold"), bg="#1e1e1e", fg="#ffffff")
        label_widget.grid(row=row, column=col, padx=5)
        entry = tk.Entry(frame, width=20, font=("Helvetica", 10), relief="flat", bg="#2b2b2b", fg="#ffffff")
        entry.grid(row=row + 1, column=col, padx=5)
        setattr(self, f"{label.lower().replace(' ', '_')}_search", entry)

    def display_books(self, books):
        # Clear previous book frames
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # Display each book as a button with image, title, and writer in a two-column grid
        for index, book in enumerate(books):
            # Create a frame for each book
            book_frame = tk.Frame(self.scroll_frame, bg="#2b2b2b", padx=5, pady=5, relief="raised", bd=1)
            
            # Position the book frame in a grid with two columns
            row = index // 2
            col = index % 2
            book_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            # Book image
            if book['image']:
                image_data = book['image']
                image = Image.open(io.BytesIO(image_data))
                image.thumbnail((70, 100))
                img = ImageTk.PhotoImage(image)
                img_label = tk.Label(book_frame, image=img, bg="#2b2b2b")
                img_label.image = img
                img_label.pack(side="left", padx=5)

            # Book details
            details_frame = tk.Frame(book_frame, bg="#2b2b2b")
            details_frame.pack(fill="x", padx=5, pady=5)

            # Book Title and Writer
            title_label = tk.Label(details_frame, text=f"{book['title']} by {book['writer']}", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="#ffffff")
            title_label.pack(anchor="w")

            genre_label = tk.Label(details_frame, text=f"Genre: {book['genre']} | Language: {book['language']}", font=("Helvetica", 10), bg="#2b2b2b", fg="#a9a9a9")
            genre_label.pack(anchor="w")

            # Buttons for book actions
            buttons_frame = tk.Frame(details_frame, bg="#2b2b2b")
            buttons_frame.pack(anchor="s", pady=5)

            # Details Button
            details_button = tk.Button(buttons_frame, text="Details", command=lambda b=book: self.open_details(b), relief="flat", bg="#007ACC", fg="#ffffff", font=("Helvetica", 10, "bold"))
            details_button.pack(side="left", padx=2)

            # Open PDF Button
            pdf_button = tk.Button(buttons_frame, text="Open PDF", command=lambda b=book: self.open_pdf(b), relief="flat", bg="#007ACC", fg="#ffffff", font=("Helvetica", 10, "bold"))
            pdf_button.pack(side="left", padx=2)

            # Borrow Button
            borrow_button = tk.Button(buttons_frame, text="Borrow", command=lambda b=book: self.borrow_book(b), relief="flat", bg="#007ACC", fg="#ffffff", font=("Helvetica", 10, "bold"))
            borrow_button.pack(side="left", padx=2)

            # Review Button
            review_button = tk.Button(buttons_frame, text="Review", command=lambda b=book: self.review_book(b), relief="flat", bg="#007ACC", fg="#ffffff", font=("Helvetica", 10, "bold"))
            review_button.pack(side="left", padx=2)

    def search_books(self):
        # Implement search function based on entered criteria
        pass

    def open_details(self, book):
        # Implement book details view
        BookDetailsWindow(self.root, book, self.username)

    def open_pdf(self, book):
        # Open book PDF
        if book["book_pdf"]:
            with open(f"book_{book['book_id']}.pdf", "wb") as pdf_file:
                pdf_file.write(book["book_pdf"])
            webbrowser.open(f"book_{book['book_id']}.pdf")
        else:
            messagebox.showwarning("No PDF", "No PDF available for this book.")

    def borrow_book(self, book):
        if book["no_of_copies"] > 0:
            register_borrow_return(book["book_id"], self.username, "borrowed")
            update_book_count(book['book_id'])
            messagebox.showinfo("Success", f"You have borrowed '{book['title']}'!")
        else:
            messagebox.showwarning("Unavailable", "No copies available.")

    def review_book(self, book):
        # Prompt user to enter a review text
        review_text = simpledialog.askstring("Review Book", "Enter your review:")
        if review_text:
            # Display the review text
            register_review(book['book_id'], self.username, review_text)
            messagebox.showinfo("Review Added", f"Your review: {review_text}")
            # Optionally, you can append the review to a list or database, if needed
            # book_reviews[book_id].append(review_text)  # If you need to store reviews

# Main Application Window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("300x200")

    # Instantiate the BooksWindow directly to view the dark theme with new button color
    BooksWindow(root, "farhan")

    root.mainloop()
