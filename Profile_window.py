import tkinter as tk
from tkinter import messagebox
from data_manage import get_genres, get_data

class ProfileWindow:
    def __init__(self, master, user):
        # Store profile details
        self.username = user["username"]
        self.email = user["email"]
        self.phone = user["phone"]
        self.address = user["address"]
        self.university = user["university"]
        self.fav_genres = get_genres(self.username)
        # self.password = password  # password is stored but not displayed for security

        # Create profile window
        self.root = tk.Toplevel(master)
        self.root.title("User Profile")
        self.root.geometry("400x400")

        # Display user information
        self.create_profile_labels()

        # Edit button
        edit_button = tk.Button(self.root, text="Edit Details", command=self.edit_details, width=15, height=2)
        edit_button.pack(pady=10)

    def create_profile_labels(self):
        # Clear existing labels if any
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()
                
        # Labels for user details
        tk.Label(self.root, text="Username: " + self.username).pack(pady=5)
        tk.Label(self.root, text="Email: " + self.email).pack(pady=5)
        tk.Label(self.root, text="Phone: " + self.phone).pack(pady=5)
        tk.Label(self.root, text="Address: " + self.address).pack(pady=5)
        tk.Label(self.root, text="University: " + self.university).pack(pady=5)
        tk.Label(self.root, text="Favorite Genres: " + ", ".join(self.fav_genres)).pack(pady=5)

    def edit_details(self):
        # Open a new window to edit details
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Profile")
        edit_window.geometry("400x400")

        # Entry fields for each attribute
        tk.Label(edit_window, text="Username").pack()
        username_entry = tk.Entry(edit_window)
        username_entry.insert(0, self.username)
        username_entry.pack(pady=5)

        tk.Label(edit_window, text="Email").pack()
        email_entry = tk.Entry(edit_window)
        email_entry.insert(0, self.email)
        email_entry.pack(pady=5)

        tk.Label(edit_window, text="Phone").pack()
        phone_entry = tk.Entry(edit_window)
        phone_entry.insert(0, self.phone)
        phone_entry.pack(pady=5)

        tk.Label(edit_window, text="Address").pack()
        address_entry = tk.Entry(edit_window)
        address_entry.insert(0, self.address)
        address_entry.pack(pady=5)

        tk.Label(edit_window, text="University").pack()
        university_entry = tk.Entry(edit_window)
        university_entry.insert(0, self.university)
        university_entry.pack(pady=5)

        tk.Label(edit_window, text="Favorite Genres (comma-separated)").pack()
        fav_genres_entry = tk.Entry(edit_window)
        fav_genres_entry.insert(0, ", ".join(self.fav_genres))
        fav_genres_entry.pack(pady=5)

        def save_changes():
            # Update attributes with new data
            self.username = username_entry.get()
            self.email = email_entry.get()
            self.phone = phone_entry.get()
            self.address = address_entry.get()
            self.university = university_entry.get()
            self.fav_genres = [genre.strip() for genre in fav_genres_entry.get().split(",")]

            # Close edit window and refresh profile labels
            root.deiconify()
            edit_window.destroy()
            self.create_profile_labels()
            messagebox.showinfo("Success", "Profile updated successfully.")

        # Save button to apply changes
        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
        save_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("300x200")

    # Button to open profile window
    open_profile_button = tk.Button(
        root, 
        text="Open Profile", 
        command=lambda: ProfileWindow(root, get_data("farhan"))
    )
    open_profile_button.pack(pady=20)

    root.mainloop()
