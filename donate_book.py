import tkinter as tk
from tkinter import messagebox

# Demo list to store donated books
donated_books = []

# Function to open the Donate Book window
def open_donate_book_window(root):
    donate_window = tk.Toplevel(root)
    donate_window.title("Donate a Book")
    donate_window.geometry("400x400")

    # Labels and Entry fields for book details
    tk.Label(donate_window, text="Book ID").grid(row=0, column=0, padx=10, pady=5)
    book_id_entry = tk.Entry(donate_window)
    book_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(donate_window, text="Book Title").grid(row=1, column=0, padx=10, pady=5)
    title_entry = tk.Entry(donate_window)
    title_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(donate_window, text="Author").grid(row=2, column=0, padx=10, pady=5)
    author_entry = tk.Entry(donate_window)
    author_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(donate_window, text="Published Date (YYYY-MM-DD)").grid(row=3, column=0, padx=10, pady=5)
    date_entry = tk.Entry(donate_window)
    date_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(donate_window, text="Genre").grid(row=4, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(donate_window)
    genre_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(donate_window, text="Language").grid(row=5, column=0, padx=10, pady=5)
    language_entry = tk.Entry(donate_window)
    language_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(donate_window, text="Number of Copies").grid(row=6, column=0, padx=10, pady=5)
    copies_entry = tk.Entry(donate_window)
    copies_entry.grid(row=6, column=1, padx=10, pady=5)

    # Save function to add book information to the donated_books list
    def save_book():
        try:
            book_id = int(book_id_entry.get())
            title = title_entry.get()
            author = author_entry.get()
            published_date = date_entry.get()
            genre = genre_entry.get()
            language = language_entry.get()
            copies = int(copies_entry.get())

            # Validate that required fields are filled
            if not (title and author and published_date and genre and language):
                raise ValueError("All fields except 'read_count' are required.")

            # Create a new book dictionary entry
            new_book = {
                "Book ID": book_id,
                "Title": title,
                "Author": author,
                "Published Date": published_date,
                "Genre": genre,
                "Language": language,
                "Read Count": 0,  # Automatically generated for a new book
                "Available": True,  # Assuming donated books are available
                "Copies": copies
            }

            donated_books.append(new_book)
            messagebox.showinfo("Success", f"{copies} copies of '{title}' donated successfully!")
            donate_window.destroy()  # Close the donate window
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Submit button to save the book details
    tk.Button(donate_window, text="Submit", command=save_book).grid(row=7, column=0, columnspan=2, pady=20)

# Main application window with a Donate Book button
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("400x300")

    # Button to open the Donate Book window
    donate_button = tk.Button(root, text="Donate Book", command=open_donate_book_window)
    donate_button.pack(pady=20)

    root.mainloop()
