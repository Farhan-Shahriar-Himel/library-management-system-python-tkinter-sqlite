import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from data_manage import register_it, add_genres

class RegistrationWindow:
    def __init__(self, parent):
        self.parent = parent

        # Create the Toplevel registration window with a modern look
        self.window = tk.Toplevel(parent)
        self.window.title("Create Account")
        self.window.geometry("600x750")  # Adjusted size for better spacing
        self.window.resizable(False, False)
        self.window.config(bg="#f4f4f4")  # Modern background color

        # Title Label with modern font and styling
        title_label = tk.Label(self.window, text="Create Account", font=("Helvetica", 18, "bold"), fg="#2C3E50", bg="#f4f4f4")
        title_label.grid(row=0, columnspan=2, pady=20)

        # Create input fields with labels and modernized entry boxes
        self.create_input_fields()

        # Image Upload Section with modern styling
        self.create_image_upload()

        # Genre Selection with modern checkboxes
        self.create_genre_selection()

        # Submit Button with modern design
        submit_button = tk.Button(self.window, text="Register", command=self.register, width=20, height=2, bg="#27AE60", fg="white", font=("Helvetica", 12, "bold"), relief="flat", bd=0)
        submit_button.grid(row=13, columnspan=2, pady=20)

        # Close the registration window when it is closed
        self.window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(parent))

    def create_input_fields(self):
        # Modernized Entry Fields
        self.username_entry = self.create_entry_field("Username:", 1)
        self.email_entry = self.create_entry_field("Email:", 2)
        self.phone_entry = self.create_entry_field("Phone Number:", 3)
        self.password_entry = self.create_entry_field("Password:", 4, show="*")
        self.confirm_password_entry = self.create_entry_field("Confirm Password:", 5, show="*")
        self.address_entry = self.create_entry_field("Address:", 6)
        self.university_entry = self.create_entry_field("University:", 7)

    def create_entry_field(self, label, row, show=None):
        tk.Label(self.window, text=label, font=("Helvetica", 12), fg="#2C3E50", bg="#f4f4f4").grid(row=row, column=0, sticky="e", padx=20, pady=10)
        entry = tk.Entry(self.window, width=35, font=("Helvetica", 12), relief="solid", bd=1, fg="#2C3E50")
        entry.grid(row=row, column=1, pady=5)
        entry.config(highlightbackground="#BDC3C7", highlightcolor="#27AE60")
        if show:
            entry.config(show="*")
        return entry

    def create_image_upload(self):
        # Modern image upload with padding and modern button
        tk.Label(self.window, text="Upload Profile Image:", font=("Helvetica", 12), fg="#2C3E50", bg="#f4f4f4").grid(row=8, column=0, sticky="e", padx=20, pady=10)
        self.image_path_label = tk.Label(self.window, text="No file chosen", width=35, anchor="w", font=("Helvetica", 12), fg="#BDC3C7", bg="#f4f4f4")
        self.image_path_label.grid(row=8, column=1, sticky="w", pady=5)

        # Browse Button for Image Upload with modern design
        image_button = tk.Button(self.window, text="Browse", command=self.browse_image, width=10, height=1, bg="#3498DB", fg="white", font=("Helvetica", 12, "bold"), relief="flat", bd=0)
        image_button.grid(row=8, column=1, sticky="e", padx=20)

    def create_genre_selection(self):
        # Favorite Genres Label
        tk.Label(self.window, text="Favorite Genres:", font=("Helvetica", 12), fg="#2C3E50", bg="#f4f4f4").grid(row=9, column=0, sticky="e", padx=20, pady=10)

        # Modern Genre Options with Checkboxes
        self.genres = {
            "Sci-Fi": tk.IntVar(),
            "Horror": tk.IntVar(),
            "Comedy": tk.IntVar(),
            "Tragedy": tk.IntVar(),
            "Romantic": tk.IntVar(),
            "Subjective": tk.IntVar(),
        }

        genre_frame = tk.Frame(self.window, bg="#f4f4f4")
        genre_frame.grid(row=10, columnspan=2, pady=10)

        row, col = 0, 0
        for genre, var in self.genres.items():
            checkbox = tk.Checkbutton(genre_frame, text=genre, variable=var, font=("Helvetica", 12), fg="#2C3E50", bg="#f4f4f4", selectcolor="#2ECC71")
            checkbox.grid(row=row, column=col, sticky="w", padx=10, pady=5)
            col += 1
            if col == 3:  # Adjust the number of checkboxes per row
                col = 0
                row += 1

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All Files", "*.*"))
        )
        if file_path:
            self.image_path_label.config(text=file_path)

    def register(self):
        # Get all user inputs
        username = self.username_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        address = self.address_entry.get()
        university = self.university_entry.get()
        image_path = self.image_path_label.cget("text")

        # Validate password confirmation
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Collect selected genres
        selected_genres = [genre for genre, var in self.genres.items() if var.get() == 1]

        # Handle Image Data
        image_data = None
        if image_path and image_path != "No file chosen":
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()

        # Register User and Add Genres to Database
        register_it(username, email, phone, password, address, university, image_data)
        add_genres(username, selected_genres)

        # Confirmation Message
        details = f"Username: {username}\nEmail: {email}\nPhone: {phone}\nUniversity: {university}\nGenres: {', '.join(selected_genres)}"
        messagebox.showinfo("Registration Successful", f"User {username} registered successfully!\n{details}")

        # Close Registration Window
        self.close_window(self.parent)

    def close_window(self, parent):
        parent.deiconify()  # Restore the parent window
        self.window.destroy()  # Close the registration window

# Main window to open registration
def open_registration():
    root.iconify()  # Minimize the main window
    RegistrationWindow(root)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("300x200")

    # Button to open the registration window with modern styling
    open_registration_button = tk.Button(root, text="Register", command=open_registration, width=20, height=2, bg="#3498DB", fg="white", font=("Helvetica", 12, "bold"), relief="flat", bd=0)
    open_registration_button.pack(pady=50)

    root.mainloop()

