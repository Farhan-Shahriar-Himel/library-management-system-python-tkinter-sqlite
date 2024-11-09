import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import io
from data_manage import get_genres, get_data, get_transactions  # Assuming these functions fetch required data

class ProfileWindow:
    def __init__(self, master, user):
        # Store profile details
        self.username = user["username"]
        self.email = user["email"]
        self.phone = user["phone"]
        self.address = user["address"]
        self.university = user["university"]
        self.fav_genres = get_genres(self.username)
        self.profile_image = user["image"]  # Image data as bytes
        self.transactions = get_transactions(self.username)  # Transaction data
        
        # Create profile window
        self.root = tk.Toplevel(master)
        self.root.title("User Profile")
        self.root.geometry("600x700")
        self.root.configure(bg="#F8F9FA")

        # Styling options
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 10), background="#F8F9FA")
        style.configure("Header.TLabel", font=("Helvetica", 12, "bold"), background="#F8F9FA")
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

        # Display user information
        self.create_profile_labels()

        # Edit button
        edit_button = tk.Button(self.root, text="Edit Details", command=self.edit_details, width=15, height=2, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold"))
        edit_button.pack(pady=10)

    def create_profile_labels(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Frame for user details
        details_frame = tk.Frame(self.root, bg="#F8F9FA")
        details_frame.pack(pady=20)

        # Profile Image
        if self.profile_image:
            image_data = io.BytesIO(self.profile_image)
            image = Image.open(image_data)
            image = image.resize((120, 120), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            img_label = tk.Label(details_frame, image=photo, bg="#F8F9FA")
            img_label.image = photo  # Keep a reference to avoid garbage collection
            img_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

        # User Details
        details = {
            "Username": self.username,
            "Email": self.email,
            "Phone": self.phone,
            "Address": self.address,
            "University": self.university,
            "Favorite Genres": ", ".join(self.fav_genres)
        }

        row = 0
        for label, value in details.items():
            ttk.Label(details_frame, text=label + ":", style="Header.TLabel").grid(row=row, column=1, sticky=tk.W, padx=5)
            ttk.Label(details_frame, text=value, style="TLabel").grid(row=row, column=2, sticky=tk.W, padx=5)
            row += 1

        # Transaction history section
        ttk.Label(self.root, text="Book Transactions", style="Header.TLabel", font=("Helvetica", 12, "bold")).pack(pady=10)

        # Transactions Treeview Table
        transactions_frame = tk.Frame(self.root)
        transactions_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("Book ID", "Transaction Type", "Date")
        tree = ttk.Treeview(transactions_frame, columns=columns, show="headings", height=8, style="Treeview")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        tree.pack(fill="both", expand=True, padx=5, pady=5)

        # Insert transactions into the table
        for transaction in self.transactions:
            tree.insert("", "end", values=transaction)

    def edit_details(self):
        # Open a new window to edit details
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Profile")
        edit_window.geometry("400x400")
        edit_window.configure(bg="#F8F9FA")

        # Entry fields for each attribute
        fields = [
            ("Username", self.username),
            ("Email", self.email),
            ("Phone", self.phone),
            ("Address", self.address),
            ("University", self.university),
            ("Favorite Genres (comma-separated)", ", ".join(self.fav_genres))
        ]
        entries = {}

        for i, (label_text, value) in enumerate(fields):
            tk.Label(edit_window, text=label_text, bg="#F8F9FA", font=("Helvetica", 10, "bold")).pack(anchor="w", padx=20, pady=(10 if i == 0 else 5))
            entry = tk.Entry(edit_window, font=("Helvetica", 10), width=30)
            entry.insert(0, value)
            entry.pack(padx=20, pady=5)
            entries[label_text] = entry

        def save_changes():
            # Save updated values
            self.username = entries["Username"].get()
            self.email = entries["Email"].get()
            self.phone = entries["Phone"].get()
            self.address = entries["Address"].get()
            self.university = entries["University"].get()
            self.fav_genres = [genre.strip() for genre in entries["Favorite Genres (comma-separated)"].get().split(",")]

            # Close edit window and refresh profile labels
            edit_window.destroy()
            self.create_profile_labels()
            messagebox.showinfo("Success", "Profile updated successfully.")

        # Save Button
        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold"))
        save_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("400x300")
    root.configure(bg="#F8F9FA")

    # Button to open profile window
    open_profile_button = tk.Button(
        root, 
        text="Open Profile", 
        command=lambda: ProfileWindow(root, get_data("farhan")),
        width=15, height=2, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold")
    )
    open_profile_button.pack(pady=40)

    root.mainloop()
