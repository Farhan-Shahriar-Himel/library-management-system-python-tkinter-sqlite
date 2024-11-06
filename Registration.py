import tkinter as tk
from tkinter import messagebox, filedialog
from data_manage import register_it, add_genres

class RegistrationWindow:
    def __init__(self, parent):
        # Create the Toplevel registration window
        self.window = tk.Toplevel(parent)
        self.window.title("Registration")
        self.window.geometry("500x650")  # Adjusted size to fit the layout

        # Restore the main window when the registration window is closed
        self.window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(parent))

        # Title Label
        title_label = tk.Label(self.window, text="Create Account", font=("Arial", 16))
        title_label.grid(row=0, columnspan=2, pady=10)

        # Username Label and Entry
        tk.Label(self.window, text="Username:").grid(row=1, column=0, sticky="e", padx=5)
        self.username_entry = tk.Entry(self.window, width=30)
        self.username_entry.grid(row=1, column=1, pady=5)

        # Email Label and Entry
        tk.Label(self.window, text="Email:").grid(row=2, column=0, sticky="e", padx=5)
        self.email_entry = tk.Entry(self.window, width=30)
        self.email_entry.grid(row=2, column=1, pady=5)

        # Phone Number Label and Entry
        tk.Label(self.window, text="Phone Number:").grid(row=3, column=0, sticky="e", padx=5)
        self.phone_entry = tk.Entry(self.window, width=30)
        self.phone_entry.grid(row=3, column=1, pady=5)

        # Password Label and Entry
        tk.Label(self.window, text="Password:").grid(row=4, column=0, sticky="e", padx=5)
        self.password_entry = tk.Entry(self.window, width=30, show="*")
        self.password_entry.grid(row=4, column=1, pady=5)

        # Confirm Password Label and Entry
        tk.Label(self.window, text="Confirm Password:").grid(row=5, column=0, sticky="e", padx=5)
        self.confirm_password_entry = tk.Entry(self.window, width=30, show="*")
        self.confirm_password_entry.grid(row=5, column=1, pady=5)

        # Address Label and Entry
        tk.Label(self.window, text="Address:").grid(row=6, column=0, sticky="e", padx=5)
        self.address_entry = tk.Entry(self.window, width=30)
        self.address_entry.grid(row=6, column=1, pady=5)

        # University Label and Entry
        tk.Label(self.window, text="University:").grid(row=7, column=0, sticky="e", padx=5)
        self.university_entry = tk.Entry(self.window, width=30)
        self.university_entry.grid(row=7, column=1, pady=5)

        # Image Upload Section
        tk.Label(self.window, text="Upload Image:").grid(row=8, column=0, sticky="e", padx=5)
        self.image_path_label = tk.Label(self.window, text="No file chosen", width=25, anchor="w")
        self.image_path_label.grid(row=8, column=1, sticky="w", pady=5)

        # Browse Button for Image Upload
        image_button = tk.Button(self.window, text="Browse", command=self.browse_image)
        image_button.grid(row=8, column=1, sticky="e", padx=5)

        # Favorite Book Genres Label
        tk.Label(self.window, text="Favorite Genres:").grid(row=9, column=0, sticky="e", padx=5)

        # Genre Options with Checkboxes
        self.genres = {
            "Sci-Fi": tk.IntVar(),
            "Horror": tk.IntVar(),
            "History": tk.IntVar(),
            "Comedy": tk.IntVar(),
            "Tragedy": tk.IntVar(),
            "Romantic": tk.IntVar(),
            "Subjective": tk.IntVar(),
            "Physics": tk.IntVar(),
            "Chemistry": tk.IntVar(),
            "Biology": tk.IntVar(),
            "Law": tk.IntVar(),
            "Art": tk.IntVar(),
            "BBA": tk.IntVar(),
            "Accounting": tk.IntVar(),
            "Economics": tk.IntVar(),
            "Textiles": tk.IntVar(),
            "English": tk.IntVar()
        }

        # Arrange checkboxes in a grid
        genre_frame = tk.Frame(self.window)
        genre_frame.grid(row=10, columnspan=2, pady=5)
        row, col = 0, 0
        for genre, var in self.genres.items():
            checkbox = tk.Checkbutton(genre_frame, text=genre, variable=var)
            checkbox.grid(row=row, column=col, sticky="w", padx=5, pady=2)
            col += 1
            if col == 3:  # Adjust this value to set number of checkboxes per row
                col = 0
                row += 1

        # Submit Button
        submit_button = tk.Button(genre_frame, text="Submit", command=lambda: self.register(parent))
        submit_button.grid(row=row + 1, columnspan=3, pady=20)  # Position the button below everything

    def browse_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All Files", "*.*"))
        )
        if file_path:
            self.image_path_label.config(text=file_path)

    def register(self, parent):
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

        image_data = None
        if image_path and image_path != "No file chosen":
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()

        register_it(username, email, phone, password, address, university, image_data)
        add_genres(username, selected_genres)

        # Display user input in a message box
        details = f"Username: {username}\nEmail: {email}\nPhone: {phone}\nPassword: {password}\nAddress: {address}\nUniversity: {university}\nFavorite Genres: {', '.join(selected_genres)}\nImage Path: {image_path}"
        
        messagebox.showinfo("Registration Details", details)

        # Close the registration window and restore the main window
        self.close_window(parent)

    def close_window(self, parent):
        # Restore the main window and destroy the registration window
        parent.deiconify()
        self.window.destroy()

# Main application window
def open_registration():
    root.iconify()  # Minimize the main window
    RegistrationWindow(root)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200")

    # Button to open the registration window
    open_registration_button = tk.Button(root, text="Register", command=open_registration)
    open_registration_button.pack(pady=50)

    root.mainloop()
