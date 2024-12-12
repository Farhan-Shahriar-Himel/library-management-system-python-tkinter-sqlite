# import tkinter as tk
# from tkinter import messagebox

# # Demo list to store donated books
# donated_books = [
#     {"Book ID": 1, "Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Published Date": "1925-04-10", 
#      "Genre": "Fiction", "Language": "English", "Read Count": 0, "Available": True, "Copies": 1},
#     {"Book ID": 2, "Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Published Date": "1960-07-11", 
#      "Genre": "Fiction", "Language": "English", "Read Count": 0, "Available": True, "Copies": 1},
# ]

# # Function to open the Edit Book window
# def open_edit_book_window(root):
#     edit_window = tk.Toplevel(root)
#     edit_window.title("Edit Book")
#     edit_window.geometry("400x400")

#     # Label and Entry for Book ID
#     tk.Label(edit_window, text="Enter Book ID").grid(row=0, column=0, padx=10, pady=5)
#     book_id_entry = tk.Entry(edit_window)
#     book_id_entry.grid(row=0, column=1, padx=10, pady=5)

#     # Function to fetch and display book details for editing
#     def fetch_book_details():
#         book_id = int(book_id_entry.get())
#         for book in donated_books:
#             if book["Book ID"] == book_id:
#                 title_entry.delete(0, tk.END)
#                 title_entry.insert(0, book["Title"])
#                 author_entry.delete(0, tk.END)
#                 author_entry.insert(0, book["Author"])
#                 date_entry.delete(0, tk.END)
#                 date_entry.insert(0, book["Published Date"])
#                 genre_entry.delete(0, tk.END)
#                 genre_entry.insert(0, book["Genre"])
#                 language_entry.delete(0, tk.END)
#                 language_entry.insert(0, book["Language"])
#                 copies_entry.delete(0, tk.END)
#                 copies_entry.insert(0, book["Copies"])
#                 return
#         messagebox.showerror("Error", "Book ID not found!")

#     # Button to fetch book details
#     tk.Button(edit_window, text="Fetch Details", command=fetch_book_details).grid(row=1, column=0, columnspan=2, pady=5)

#     # Labels and Entry fields for book details
#     tk.Label(edit_window, text="Title").grid(row=2, column=0, padx=10, pady=5)
#     title_entry = tk.Entry(edit_window)
#     title_entry.grid(row=2, column=1, padx=10, pady=5)

#     tk.Label(edit_window, text="Author").grid(row=3, column=0, padx=10, pady=5)
#     author_entry = tk.Entry(edit_window)
#     author_entry.grid(row=3, column=1, padx=10, pady=5)

#     tk.Label(edit_window, text="Published Date (YYYY-MM-DD)").grid(row=4, column=0, padx=10, pady=5)
#     date_entry = tk.Entry(edit_window)
#     date_entry.grid(row=4, column=1, padx=10, pady=5)

#     tk.Label(edit_window, text="Genre").grid(row=5, column=0, padx=10, pady=5)
#     genre_entry = tk.Entry(edit_window)
#     genre_entry.grid(row=5, column=1, padx=10, pady=5)

#     tk.Label(edit_window, text="Language").grid(row=6, column=0, padx=10, pady=5)
#     language_entry = tk.Entry(edit_window)
#     language_entry.grid(row=6, column=1, padx=10, pady=5)

#     tk.Label(edit_window, text="Number of Copies").grid(row=7, column=0, padx=10, pady=5)
#     copies_entry = tk.Entry(edit_window)
#     copies_entry.grid(row=7, column=1, padx=10, pady=5)

#     # Save function to update book information
#     def save_book():
#         book_id = int(book_id_entry.get())
#         for book in donated_books:
#             if book["Book ID"] == book_id:
#                 book["Title"] = title_entry.get()
#                 book["Author"] = author_entry.get()
#                 book["Published Date"] = date_entry.get()
#                 book["Genre"] = genre_entry.get()
#                 book["Language"] = language_entry.get()
#                 book["Copies"] = int(copies_entry.get())
#                 messagebox.showinfo("Success", "Book details updated successfully!")
#                 edit_window.destroy()  # Close the edit window
#                 return
#         messagebox.showerror("Error", "Book ID not found!")

#     # Submit button to save the book details
#     tk.Button(edit_window, text="Submit Changes", command=save_book).grid(row=8, column=0, columnspan=2, pady=20)

# # Main application window with Edit Book button
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Library Management System")
#     root.geometry("400x300")

#     # Button to open the Edit Book window
#     edit_button = tk.Button(root, text="Edit Book", command=open_edit_book_window)
#     edit_button.pack(pady=20)

#     root.mainloop()





import customtkinter as ctk
from tkinter import messagebox
import data_manage  # Import the data management module

# Configure the appearance mode and color theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class LibraryManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure main window
        self.title("Library Management System")
        self.geometry("500x400")
        self.minsize(400, 300)

        # Create main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title Label
        title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Library Management System", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=20)

        # Edit Book Button
        edit_button = ctk.CTkButton(
            self.main_frame, 
            text="Edit Book", 
            command=lambda: self.open_edit_book_window(),  # Use lambda to delay the call
            corner_radius=6
        )
        edit_button.pack(pady=10)

    def open_edit_book_window(self):
        # Hide main window
        self.withdraw()

        # Create edit book window
        edit_window = ctk.CTkToplevel(self)
        edit_window.title("Edit Book")
        edit_window.geometry("500x700")
        edit_window.minsize(400, 500)

        # Callback to show the main window when edit window is closed
        def on_edit_window_close():
            self.deiconify()
            edit_window.destroy()

        # Bind the callback to the edit window's destroy event
        edit_window.protocol("WM_DELETE_WINDOW", on_edit_window_close)

        # Create main frame for edit window
        edit_frame = ctk.CTkFrame(edit_window, corner_radius=10)
        edit_frame.grid(row=0, column=0, padx=20, pady=20)

        # Center the main frame
        edit_window.grid_rowconfigure(0, weight=1)
        edit_window.grid_columnconfigure(0, weight=1)

        # Book ID Entry
        book_id_label = ctk.CTkLabel(edit_frame, text="Enter Book ID")
        book_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.book_id_entry = ctk.CTkEntry(edit_frame, width=200)
        self.book_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Fetch Details Button
        fetch_button = ctk.CTkButton(
            edit_frame, 
            text="Fetch Details", 
            command=self.fetch_book_details,
            corner_radius=6
        )
        fetch_button.grid(row=0, column=2, padx=10, pady=10)

        # Entry Widgets
        self.entries = {
            "title": {"label": "Title", "widget": None},
            "writer": {"label": "Author", "widget": None},
            "genre": {"label": "Genre", "widget": None},
            "language": {"label": "Language", "widget": None},
            "published_year": {"label": "Published Year", "widget": None},
            "no_of_copies": {"label": "Number of Copies", "widget": None}
        }

        # Create entry widgets
        for i, (key, entry_info) in enumerate(self.entries.items()):
            # Label
            label = ctk.CTkLabel(edit_frame, text=entry_info["label"])
            label.grid(row=i+1, column=0, padx=10, pady=10, sticky="e")
            
            # Entry
            entry_widget = ctk.CTkEntry(edit_frame, width=300)
            entry_widget.grid(row=i+1, column=1, columnspan=2, padx=10, pady=10, sticky="w")
            
            # Store the entry widget
            self.entries[key]["widget"] = entry_widget

        # Save Function
        def save_book():
            try:
                book_id = int(self.book_id_entry.get())
                
                # Prepare updated book details
                updated_book = {}
                for key, entry_info in self.entries.items():
                    updated_book[key] = entry_info["widget"].get()
                
                # Connect to database and update book
                conn = data_manage.sqlite3.connect('library_database.db')
                
                # Construct UPDATE query dynamically
                update_query = '''
                UPDATE books 
                SET title=?, writer=?, genre=?, language=?, published_year=?, no_of_copies=?
                WHERE book_id=?
                '''
                
                # Prepare values for the update query
                update_values = (
                    updated_book['title'], 
                    updated_book['writer'], 
                    updated_book['genre'], 
                    updated_book['language'], 
                    int(updated_book['published_year']), 
                    int(updated_book['no_of_copies']), 
                    book_id
                )
                
                # Execute update
                conn.execute(update_query, update_values)
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Success", "Book details updated successfully!")
                edit_window.destroy()
            
            except (ValueError, Exception) as e:
                messagebox.showerror("Error", f"Failed to update book: {str(e)}")

        # Submit button
        submit_button = ctk.CTkButton(
            edit_frame, 
            text="Submit Changes", 
            command=save_book,
            corner_radius=6,
            fg_color="green"
        )
        submit_button.grid(row=len(self.entries) + 1, columnspan=3, padx=10, pady=20)

    def fetch_book_details(self):
        try:
            book_id = int(self.book_id_entry.get())
                
            # Get all books and find the specific book
            books = data_manage.get_all_books()
            book_to_edit = None
                
            for book in books:
                if book['book_id'] == book_id:
                    book_to_edit = book
                    break
                
            if book_to_edit:
                # Populate entries with book details
                for key, entry_info in self.entries.items():
                    entry_info["widget"].delete(0, 'end')
                    entry_info["widget"].insert(0, str(book_to_edit.get(key, '')))
            else:
                messagebox.showerror("Error", "Book ID not found!")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid Book ID")

def main():
    app = LibraryManagementApp()
    app.mainloop()

if __name__ == "__main__":
    main()
