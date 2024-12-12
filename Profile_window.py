# import tkinter as tk
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
# import io
# from data_manage import get_genres, get_data, get_transactions  # Assuming these functions fetch required data

# class ProfileWindow:
#     def __init__(self, master, user):
#         # Store profile details
#         self.username = user["username"]
#         self.email = user["email"]
#         self.phone = user["phone"]
#         self.address = user["address"]
#         self.university = user["university"]
#         self.fav_genres = get_genres(self.username)
#         self.profile_image = user["image"]  # Image data as bytes
#         self.transactions = get_transactions(self.username)  # Transaction data
        
#         # Create profile window
#         self.root = tk.Toplevel(master)
#         self.root.title("User Profile")
#         self.root.geometry("600x700")
#         self.root.configure(bg="#F8F9FA")

#         # Styling options
#         style = ttk.Style()
#         style.configure("TLabel", font=("Helvetica", 10), background="#F8F9FA")
#         style.configure("Header.TLabel", font=("Helvetica", 12, "bold"), background="#F8F9FA")
#         style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

#         # Display user information
#         self.create_profile_labels()

#         # Edit button
#         edit_button = tk.Button(self.root, text="Edit Details", command=self.edit_details, width=15, height=2, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold"))
#         edit_button.pack(pady=10)

#     def create_profile_labels(self):
#         # Clear existing widgets
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Frame for user details
#         details_frame = tk.Frame(self.root, bg="#F8F9FA")
#         details_frame.pack(pady=20)

#         # Profile Image
#         if self.profile_image:
#             image_data = io.BytesIO(self.profile_image)
#             image = Image.open(image_data)
#             image = image.resize((120, 120), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             img_label = tk.Label(details_frame, image=photo, bg="#F8F9FA")
#             img_label.image = photo  # Keep a reference to avoid garbage collection
#             img_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

#         # User Details
#         details = {
#             "Username": self.username,
#             "Email": self.email,
#             "Phone": self.phone,
#             "Address": self.address,
#             "University": self.university,
#             "Favorite Genres": ", ".join(self.fav_genres)
#         }

#         row = 0
#         for label, value in details.items():
#             ttk.Label(details_frame, text=label + ":", style="Header.TLabel").grid(row=row, column=1, sticky=tk.W, padx=5)
#             ttk.Label(details_frame, text=value, style="TLabel").grid(row=row, column=2, sticky=tk.W, padx=5)
#             row += 1

#         # Transaction history section
#         ttk.Label(self.root, text="Book Transactions", style="Header.TLabel", font=("Helvetica", 12, "bold")).pack(pady=10)

#         # Transactions Treeview Table
#         transactions_frame = tk.Frame(self.root)
#         transactions_frame.pack(fill="both", expand=True, padx=20, pady=10)

#         columns = ("Book ID", "Transaction Type", "Date")
#         tree = ttk.Treeview(transactions_frame, columns=columns, show="headings", height=8, style="Treeview")
#         for col in columns:
#             tree.heading(col, text=col)
#             tree.column(col, anchor="center")

#         tree.pack(fill="both", expand=True, padx=5, pady=5)

#         # Insert transactions into the table
#         for transaction in self.transactions:
#             tree.insert("", "end", values=transaction)

#     def edit_details(self):
#         # Open a new window to edit details
#         edit_window = tk.Toplevel(self.root)
#         edit_window.title("Edit Profile")
#         edit_window.geometry("400x400")
#         edit_window.configure(bg="#F8F9FA")

#         # Entry fields for each attribute
#         fields = [
#             ("Username", self.username),
#             ("Email", self.email),
#             ("Phone", self.phone),
#             ("Address", self.address),
#             ("University", self.university),
#             ("Favorite Genres (comma-separated)", ", ".join(self.fav_genres))
#         ]
#         entries = {}

#         for i, (label_text, value) in enumerate(fields):
#             tk.Label(edit_window, text=label_text, bg="#F8F9FA", font=("Helvetica", 10, "bold")).pack(anchor="w", padx=20, pady=(10 if i == 0 else 5))
#             entry = tk.Entry(edit_window, font=("Helvetica", 10), width=30)
#             entry.insert(0, value)
#             entry.pack(padx=20, pady=5)
#             entries[label_text] = entry

#         def save_changes():
#             # Save updated values
#             self.username = entries["Username"].get()
#             self.email = entries["Email"].get()
#             self.phone = entries["Phone"].get()
#             self.address = entries["Address"].get()
#             self.university = entries["University"].get()
#             self.fav_genres = [genre.strip() for genre in entries["Favorite Genres (comma-separated)"].get().split(",")]

#             # Close edit window and refresh profile labels
#             edit_window.destroy()
#             self.create_profile_labels()
#             messagebox.showinfo("Success", "Profile updated successfully.")

#         # Save Button
#         save_button = tk.Button(edit_window, text="Save Changes", command=save_changes, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold"))
#         save_button.pack(pady=20)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Library Management System")
#     root.geometry("400x300")
#     root.configure(bg="#F8F9FA")

#     # Button to open profile window
#     open_profile_button = tk.Button(
#         root, 
#         text="Open Profile", 
#         command=lambda: ProfileWindow(root, get_data("farhan")),
#         width=15, height=2, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold")
#     )
#     open_profile_button.pack(pady=40)

#     root.mainloop()







import customtkinter as ctk
from tkinter import messagebox, ttk  # Importing ttk for Treeview
from PIL import Image, ImageTk, ImageDraw
import io
import sqlite3
from data_manage import get_genres, get_data, get_transactions, add_genres

class ProfileWindow:
    def __init__(self, master, user):
        # Store profile details
        self.user = user
        self.username = user["username"]
        self.email = user["email"]
        self.phone = user["phone"]
        self.address = user["address"]
        self.university = user["university"]
        self.fav_genres = get_genres(self.username)
        self.profile_image = user["image"]  # Image data as bytes
        self.transactions = get_transactions(self.username)  # Transaction data

        # Create profile window
        self.root = ctk.CTkToplevel(master)
        self.root.title("User Profile")
        self.root.geometry("800x600")

        # Callback to show the main window when profile window is closed
        def on_profile_window_close():
            master.deiconify()
            self.root.destroy()

        # Bind the callback to the profile window's destroy event
        self.root.protocol("WM_DELETE_WINDOW", on_profile_window_close)

        # Display user information
        self.create_profile_labels()

    def create_profile_labels(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Frame for user details
        details_frame = ctk.CTkFrame(self.root)
        details_frame.pack(pady=20, padx=20, fill="x")

        # Profile Image
        if self.profile_image:
            image_data = io.BytesIO(self.profile_image)
            image = Image.open(image_data)
            image = image.resize((120, 120), Image.LANCZOS)
            
            # Create a mask to round the corners of the image
            mask = Image.new('L', image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, 120, 120), fill=255)

            rounded_image = Image.new('RGBA', image.size)
            rounded_image.paste(image, (0, 0), mask)

            photo = ImageTk.PhotoImage(rounded_image)
            img_label = ctk.CTkLabel(details_frame, image=photo)
            img_label.image = photo  # Keep a reference to avoid garbage collection
            img_label.grid(row=0, column=0, rowspan=5, padx=20, pady=20)

        # User Details
        details = {
            "Username": self.username,
            "Email": self.email,
            "Phone": self.phone,
            "Address": self.address,
            "University": self.university,
            "Favorite Genres": ", ".join(self.fav_genres)
        }

        self.entries = {}
        row = 0
        for label, value in details.items():
            ctk.CTkLabel(details_frame, text=label + ":", font=ctk.CTkFont(size=14, weight="bold")).grid(row=row, column=1, sticky="w", padx=10)
            entry = ctk.CTkEntry(details_frame, width=300)
            entry.insert(0, value)
            entry.grid(row=row, column=2, sticky="w", padx=10)
            entry.configure(state="readonly")  # Set to readonly by default
            self.entries[label] = entry
            row += 1

        # Transaction history section
        ctk.CTkLabel(self.root, text="Book Transactions", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)

        # Transactions Treeview Table
        transactions_frame = ctk.CTkFrame(self.root)
        transactions_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("Book ID", "Transaction Type", "Date")
        tree = ttk.Treeview(transactions_frame, columns=columns, show="headings", height=10)
        for col in columns:
            tree.heading(col, text=col, anchor="center")
            tree.column(col, anchor="center")

        tree.pack(fill="both", expand=True, padx=5, pady=5)

        # Edit button
        self.edit_button = ctk.CTkButton(self.root, text="Edit Info", command=self.edit_info, width=200)
        self.edit_button.pack(pady=20)

    def edit_info(self):
        for entry in self.entries.values():
            entry.configure(state="normal")
        
        # Remove Edit button and show Save and Cancel buttons
        self.edit_button.pack_forget()
        
        self.save_button = ctk.CTkButton(self.root, text="Save Changes", command=self.save_changes, width=100)
        self.save_button.pack(side="left", padx=20)

        self.cancel_button = ctk.CTkButton(self.root, text="Cancel", command=self.cancel_edit, width=100)
        self.cancel_button.pack(side="left", padx=20)

    def save_changes(self):
        # Save updated values
        self.username = self.entries["Username"].get()
        self.email = self.entries["Email"].get()
        self.phone = self.entries["Phone"].get()
        self.address = self.entries["Address"].get()
        self.university = self.entries["University"].get()
        self.fav_genres = [genre.strip() for genre in self.entries["Favorite Genres"].get().split(",")]

        # Update user data
        self.user.update({
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "university": self.university,
            "image": self.profile_image
        })

        # Save user info
        self.save_user_info()

        # Update genres
        add_genres(self.username, self.fav_genres)

        # Refresh profile labels
        self.create_profile_labels()
        messagebox.showinfo("Success", "Profile updated successfully.")

    def cancel_edit(self):
        self.create_profile_labels()

    def save_user_info(self):
        conn = sqlite3.connect('library_database.db')
        cursor = conn.cursor()
        
        # Update user details in the database
        update_query = """
        UPDATE users
        SET email = ?, phone = ?, address = ?, university = ?, image = ?
        WHERE username = ?
        """
        
        cursor.execute(update_query, (
            self.email,
            self.phone,
            self.address,
            self.university,
            sqlite3.Binary(self.profile_image),  # Ensure profile_image is saved as binary
            self.username
        ))
        
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Library Management System")
    root.geometry("400x300")

    # Button to open profile window
    open_profile_button = ctk.CTkButton(
        root, 
        text="Open Profile", 
        command=lambda: ProfileWindow(root, get_data("farhan")),
        width=200
    )
    open_profile_button.pack(pady=40)

    # Hide main window when profile window opens
    def open_profile():
        root.withdraw()
        ProfileWindow(root, get_data("farhan"))

    open_profile_button.configure(command=open_profile)

    root.mainloop()

