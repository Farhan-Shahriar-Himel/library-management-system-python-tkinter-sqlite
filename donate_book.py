# import tkinter as tk
# from tkinter import filedialog, messagebox
# from data_manage import store_book

# class DonateBookWindow:
#     def __init__(self, root, username):
#         self.root = root
#         self.username = username
#         # Initialize the Donate Book window
#         self.donate_window = tk.Toplevel(root)
#         self.donate_window.title("Donate a Book")
#         self.donate_window.geometry("400x600")

#         # Create form fields
#         tk.Label(self.donate_window, text="Book Title").grid(row=0, column=0, padx=10, pady=5)
#         self.title_entry = tk.Entry(self.donate_window)
#         self.title_entry.grid(row=0, column=1, padx=10, pady=5)

#         tk.Label(self.donate_window, text="Author").grid(row=1, column=0, padx=10, pady=5)
#         self.author_entry = tk.Entry(self.donate_window)
#         self.author_entry.grid(row=1, column=1, padx=10, pady=5)

#         tk.Label(self.donate_window, text="Genre").grid(row=2, column=0, padx=10, pady=5)
#         self.genre_entry = tk.Entry(self.donate_window)
#         self.genre_entry.grid(row=2, column=1, padx=10, pady=5)

#         tk.Label(self.donate_window, text="Language").grid(row=3, column=0, padx=10, pady=5)
#         self.language_entry = tk.Entry(self.donate_window)
#         self.language_entry.grid(row=3, column=1, padx=10, pady=5)

#         tk.Label(self.donate_window, text="Publishing Year").grid(row=4, column=0, padx=10, pady=5)
#         self.year_entry = tk.Entry(self.donate_window)
#         self.year_entry.grid(row=4, column=1, padx=10, pady=5)

#         tk.Label(self.donate_window, text="Number of Copies").grid(row=5, column=0, padx=10, pady=5)
#         self.copies_entry = tk.Entry(self.donate_window)
#         self.copies_entry.grid(row=5, column=1, padx=10, pady=5)

#         # File selector for PDF upload
#         tk.Label(self.donate_window, text="Upload PDF").grid(row=6, column=0, padx=10, pady=5)
#         self.pdf_path = tk.StringVar()
#         tk.Button(self.donate_window, text="Choose PDF", command=self.select_pdf).grid(row=6, column=1, padx=10, pady=5)

#         # File selector for Image upload
#         tk.Label(self.donate_window, text="Upload Book Image").grid(row=7, column=0, padx=10, pady=5)
#         self.image_path = tk.StringVar()
#         tk.Button(self.donate_window, text="Choose Image", command=self.select_image).grid(row=7, column=1, padx=10, pady=5)

#         # Submit button
#         tk.Button(self.donate_window, text="Submit", command=self.save_book).grid(row=8, column=0, columnspan=2, pady=20)

#     def select_pdf(self):
#         # Open file dialog to select a PDF file
#         file_path = filedialog.askopenfilename(
#             title="Select PDF file",
#             filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
#         )
#         if file_path:
#             self.pdf_path.set(file_path)
#             messagebox.showinfo("File Selected", "PDF file selected successfully!")

#     def select_image(self):
#         # Open file dialog to select an image file
#         file_path = filedialog.askopenfilename(
#             title="Select Image file",
#             filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
#         )
#         if file_path:
#             self.image_path.set(file_path)
#             messagebox.showinfo("File Selected", "Image file selected successfully!")

#     def save_book(self):
#         # Get values from the form fields
#         title = self.title_entry.get()
#         author = self.author_entry.get()
#         genre = self.genre_entry.get()
#         language = self.language_entry.get()
#         copies = self.copies_entry.get()
#         published_year = self.year_entry.get()

#         # Check for required fields
#         if not (title and author and genre and language and copies and published_year and self.pdf_path.get() and self.image_path.get()):
#             messagebox.showerror("Error", "All fields, PDF, and image are required.")
#             return

#         try:
#             # Read the PDF file as binary
#             with open(self.pdf_path.get(), "rb") as file:
#                 pdf_data = file.read()

#             # Read the image file as binary
#             with open(self.image_path.get(), "rb") as file:
#                 image_data = file.read()

#             # Insert data into database
#             store_book(
#                 title=title,
#                 writer=author,
#                 username=self.username,
#                 genre=genre,
#                 language=language,
#                 published_year=published_year,
#                 no_of_copies=copies,
#                 img=image_data,
#                 book_pdf=pdf_data
#             )

#             messagebox.showinfo("Success", f"{copies} copies of '{title}' donated successfully!")
#             self.donate_window.destroy()  # Close the donate window
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

# # Main application window with a Donate Book button
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Library Management System")
#     root.geometry("400x300")

#     # Button to open the Donate Book window
#     tk.Button(root, text="Donate Book", command=lambda: DonateBookWindow(root, "farhan")).pack(pady=20)

#     root.mainloop()



import customtkinter as ctk
from tkinter import filedialog, messagebox
from data_manage import store_book

class DonateBookWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username

        # Initialize the Donate Book window
        self.donate_window = ctk.CTkToplevel(root)
        self.donate_window.title("Donate a Book")
        self.donate_window.geometry("500x700")
        self.donate_window.transient(self.root)  # Make it appear in front of the main window
        self.donate_window.grab_set()  # Disable interaction with the main window

        # Form header
        header_label = ctk.CTkLabel(self.donate_window, text="Donate a Book", font=("Arial", 20, "bold"))
        header_label.pack(pady=20)

        # Form fields
        self.create_field("Book Title", "title_entry")
        self.create_field("Author", "author_entry")
        self.create_field("Genre", "genre_entry")
        self.create_field("Language", "language_entry")
        self.create_field("Publishing Year", "year_entry")
        self.create_field("Number of Copies", "copies_entry")

        # File selectors
        self.pdf_path = ctk.StringVar()
        self.create_file_selector("Upload PDF", self.select_pdf)

        self.image_path = ctk.StringVar()
        self.create_file_selector("Upload Book Image", self.select_image)

        # Submit button
        submit_button = ctk.CTkButton(self.donate_window, text="Submit", command=self.save_book)
        submit_button.pack(pady=20)

    def create_field(self, label_text, attr_name):
        """Helper method to create a labeled entry field."""
        frame = ctk.CTkFrame(self.donate_window)
        frame.pack(pady=10, padx=20, fill="x")

        label = ctk.CTkLabel(frame, text=label_text, width=150, anchor="w")
        label.pack(side="left", padx=10)

        entry = ctk.CTkEntry(frame, width=300)
        entry.pack(side="right", padx=10)

        setattr(self, attr_name, entry)

    def create_file_selector(self, label_text, command):
        """Helper method to create a labeled file selection button."""
        frame = ctk.CTkFrame(self.donate_window)
        frame.pack(pady=10, padx=20, fill="x")

        label = ctk.CTkLabel(frame, text=label_text, width=150, anchor="w")
        label.pack(side="left", padx=10)

        button = ctk.CTkButton(frame, text="Choose File", command=command, width=120)
        button.pack(side="right", padx=10)

    def select_pdf(self):
        # Open file dialog to select a PDF file
        file_path = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf")],
        )
        if file_path:
            self.pdf_path.set(file_path)
            messagebox.showinfo("File Selected", "PDF file selected successfully!")

    def select_image(self):
        # Open file dialog to select an image file
        file_path = filedialog.askopenfilename(
            title="Select Image file",
            filetypes=[("JPEG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("PNG files", "*.png")],
        )
        if file_path:
            self.image_path.set(file_path)
            messagebox.showinfo("File Selected", "Image file selected successfully!")

    def save_book(self):
        # Get values from the form fields
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        language = self.language_entry.get()
        copies = self.copies_entry.get()
        published_year = self.year_entry.get()

        # Check for required fields
        if not (title and author and genre and language and copies and published_year and self.pdf_path.get() and self.image_path.get()):
            messagebox.showerror("Error", "All fields, PDF, and image are required.")
            return

        try:
            # Read the PDF file as binary
            with open(self.pdf_path.get(), "rb") as file:
                pdf_data = file.read()

            # Read the image file as binary
            with open(self.image_path.get(), "rb") as file:
                image_data = file.read()

            # Insert data into database
            store_book(
                title=title,
                writer=author,
                username=self.username,
                genre=genre,
                language=language,
                published_year=published_year,
                no_of_copies=copies,
                img=image_data,
                book_pdf=pdf_data
            )

            messagebox.showinfo("Success", f"{copies} copies of '{title}' donated successfully!")
            self.donate_window.destroy()  # Close the donate window
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Main application window with a Donate Book button
if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    root = ctk.CTk()
    root.title("Library Management System")
    root.geometry("500x400")

    # Button to open the Donate Book window
    donate_button = ctk.CTkButton(root, text="Donate Book", command=lambda: DonateBookWindow(root, "farhan"),
                                  font=("Arial", 16))
    donate_button.pack(pady=50)

    root.mainloop()