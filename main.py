import tkinter as tk
from tkinter import messagebox
from Login import LoginWindow

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x300")

        # Creating the Menu bar
        menu_bar = tk.Menu(self.root)
        menu = tk.Menu(menu_bar, tearoff=0)
        menu.add_command(label="Ask Help", command=self.ask_help)
        menu.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

        # Label for title
        title_label = tk.Label(self.root, text="Welcome to the Library Management System", font=("Arial", 12))
        title_label.pack(pady=20)

        # Admin Login button
        admin_button = tk.Button(self.root, text="Admin Login", command=self.admin_login, width=20)
        admin_button.pack(pady=10)

        # User Login button
        user_button = tk.Button(self.root, text="User Login", command=self.user_login, width=20)
        user_button.pack(pady=10)

    def admin_login(self):
        messagebox.showinfo("Admin Login", "Redirecting to Admin Login...")

    def user_login(self):
        # messagebox.showinfo("User Login", "Redirecting to User Login...")
        self.root.iconify()
        LoginWindow(self.root)

    def ask_help(self):
        messagebox.showinfo("Ask Help", "For help, please contact support@example.com.")

    def about(self):
        messagebox.showinfo("About", "Library Management System\nVersion 1.0\nDeveloped by Farhan.")

# Creating main window
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
