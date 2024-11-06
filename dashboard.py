import tkinter as tk
from tkinter import messagebox
from data_manage import get_data
class DashboardWindow:
    def __init__(self, master, username):
        self.user = get_data(username)
        self.root = tk.Toplevel(master)
        self.root.title("Dashboard")
        self.root.geometry("300x400")

        # Display Username and Email
        user_info_frame = tk.Frame(self.root)
        user_info_frame.pack(pady=10)

        username_label = tk.Label(user_info_frame, text=f"Username: {self.user['username']}", font=("Arial", 12))
        username_label.pack()

        email_label = tk.Label(user_info_frame, text=f"Email: {self.user['email']}", font=("Arial", 12))
        email_label.pack()

        # Buttons
        profile_button = tk.Button(self.root, text="Profile", command=self.show_profile, width=20, height=2)
        profile_button.pack(pady=10)

        books_button = tk.Button(self.root, text="Books", command=self.show_books, width=20, height=2)
        books_button.pack(pady=10)

        donate_book_button = tk.Button(self.root, text="Donate Book", command=self.donate_book, width=20, height=2)
        donate_book_button.pack(pady=10)

        edit_book_button = tk.Button(self.root, text="Edit Book", command=self.edit_book, width=20, height=2)
        edit_book_button.pack(pady=10)

        articles_button = tk.Button(self.root, text="Articles", command=self.show_articles, width=20, height=2)
        articles_button.pack(pady=10)

        logout_button = tk.Button(self.root, text="Log out", command=self.logout, width=20, height=2)
        logout_button.pack(pady=10)

    # Button functions
    def show_profile(self):
        from Profile_window import ProfileWindow
        self.root.iconify()
        ProfileWindow(master=self.root, user=self.user)
        # messagebox.showinfo("Profile", "Profile details would go here.")

    def show_books(self):
        from all_books import BooksWindow
        from demo_data import demo_books
        self.root.iconify
        BooksWindow(self.root, demo_books)
        # messagebox.showinfo("Books", "Books section would go here.")

    def donate_book(self):
        from donate_book import open_donate_book_window
        self.root.iconify()
        open_donate_book_window(self.root)
        # messagebox.showinfo("Donate Book", "Donate book functionality would go here.")

    def edit_book(self):
        from edit_book import open_edit_book_window
        self.root.iconify()
        open_edit_book_window(self.root)
        # messagebox.showinfo("Edit Book", "Edit book functionality would go here.")

    def show_articles(self):
        from articles import open_articles_window
        open_articles_window(self.root)
        # messagebox.showinfo("Articles", "Articles section would go here.")

    def logout(self):
        self.root.destroy()
        messagebox.showinfo("Logout", "You have been logged out.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("300x200")
    
    # Simulating user data
    username = "farhan"
    email = "john_doe@example.com"

    # Button to open dashboard
    open_dashboard_button = tk.Button(root, text="Open Dashboard", command=lambda: DashboardWindow(root, username))
    open_dashboard_button.pack(pady=20)

    root.mainloop()
