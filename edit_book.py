import tkinter as tk
from tkinter import messagebox

# Demo list to store donated books
donated_books = [
    {"Book ID": 1, "Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Published Date": "1925-04-10", 
     "Genre": "Fiction", "Language": "English", "Read Count": 0, "Available": True, "Copies": 1},
    {"Book ID": 2, "Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Published Date": "1960-07-11", 
     "Genre": "Fiction", "Language": "English", "Read Count": 0, "Available": True, "Copies": 1},
]

# Function to open the Edit Book window
def open_edit_book_window(root):
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Book")
    edit_window.geometry("400x400")

    # Label and Entry for Book ID
    tk.Label(edit_window, text="Enter Book ID").grid(row=0, column=0, padx=10, pady=5)
    book_id_entry = tk.Entry(edit_window)
    book_id_entry.grid(row=0, column=1, padx=10, pady=5)

    # Function to fetch and display book details for editing
    def fetch_book_details():
        book_id = int(book_id_entry.get())
        for book in donated_books:
            if book["Book ID"] == book_id:
                title_entry.delete(0, tk.END)
                title_entry.insert(0, book["Title"])
                author_entry.delete(0, tk.END)
                author_entry.insert(0, book["Author"])
                date_entry.delete(0, tk.END)
                date_entry.insert(0, book["Published Date"])
                genre_entry.delete(0, tk.END)
                genre_entry.insert(0, book["Genre"])
                language_entry.delete(0, tk.END)
                language_entry.insert(0, book["Language"])
                copies_entry.delete(0, tk.END)
                copies_entry.insert(0, book["Copies"])
                return
        messagebox.showerror("Error", "Book ID not found!")

    # Button to fetch book details
    tk.Button(edit_window, text="Fetch Details", command=fetch_book_details).grid(row=1, column=0, columnspan=2, pady=5)

    # Labels and Entry fields for book details
    tk.Label(edit_window, text="Title").grid(row=2, column=0, padx=10, pady=5)
    title_entry = tk.Entry(edit_window)
    title_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Author").grid(row=3, column=0, padx=10, pady=5)
    author_entry = tk.Entry(edit_window)
    author_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Published Date (YYYY-MM-DD)").grid(row=4, column=0, padx=10, pady=5)
    date_entry = tk.Entry(edit_window)
    date_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Genre").grid(row=5, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(edit_window)
    genre_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Language").grid(row=6, column=0, padx=10, pady=5)
    language_entry = tk.Entry(edit_window)
    language_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Number of Copies").grid(row=7, column=0, padx=10, pady=5)
    copies_entry = tk.Entry(edit_window)
    copies_entry.grid(row=7, column=1, padx=10, pady=5)

    # Save function to update book information
    def save_book():
        book_id = int(book_id_entry.get())
        for book in donated_books:
            if book["Book ID"] == book_id:
                book["Title"] = title_entry.get()
                book["Author"] = author_entry.get()
                book["Published Date"] = date_entry.get()
                book["Genre"] = genre_entry.get()
                book["Language"] = language_entry.get()
                book["Copies"] = int(copies_entry.get())
                messagebox.showinfo("Success", "Book details updated successfully!")
                edit_window.destroy()  # Close the edit window
                return
        messagebox.showerror("Error", "Book ID not found!")

    # Submit button to save the book details
    tk.Button(edit_window, text="Submit Changes", command=save_book).grid(row=8, column=0, columnspan=2, pady=20)

# Main application window with Edit Book button
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("400x300")

    # Button to open the Edit Book window
    edit_button = tk.Button(root, text="Edit Book", command=open_edit_book_window)
    edit_button.pack(pady=20)

    root.mainloop()
