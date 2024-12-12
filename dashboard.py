import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_manage import get_data, update_book_count, register_borrow_return
import io

class DashboardWindow:
    def __init__(self, master, username):
        self.user = get_data(username)
        self.root = tk.Toplevel(master)
        self.root.title("Library Management Dashboard")
        self.root.geometry("800x500")  # Adjusted window size
        self.root.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        self.display_user_info()
        self.add_announcements()
        self.create_buttons()
        self.add_middle_content()

    def display_user_info(self):
        user_info_frame = tk.Frame(self.root, bg="#e0e0e0", bd=2, relief="ridge")
        user_info_frame.pack(pady=10, padx=20, fill="x")

        profile_info_frame = tk.Frame(user_info_frame, bg="#e0e0e0")
        profile_info_frame.pack(side="left", padx=10)

        if 'image' in self.user:
            image_data = io.BytesIO(self.user['image'])
            profile_image = Image.open(image_data)
            profile_image = profile_image.resize((50, 50), Image.LANCZOS)
            self.profile_photo = ImageTk.PhotoImage(profile_image)
            profile_label = tk.Label(profile_info_frame, image=self.profile_photo, bg="#e0e0e0", cursor="hand2")
            profile_label.pack(side="left", padx=(0, 10), pady=10)
            profile_label.bind("<Button-1>", lambda e: self.show_profile())

        details_frame = tk.Frame(profile_info_frame, bg="#e0e0e0")
        details_frame.pack(side="left")

        username_label = tk.Label(details_frame, text=f"Username: {self.user['username']}", font=("Arial", 12), bg="#e0e0e0")
        username_label.pack(pady=(10, 0))

        email_label = tk.Label(details_frame, text=f"Email: {self.user['email']}", font=("Arial", 12), bg="#e0e0e0")
        email_label.pack(pady=(5, 10))

        # Log out button at top-right
        logout_icon_image = Image.open("image/log_out.png")
        logout_icon_image = logout_icon_image.resize((20, 20), Image.LANCZOS)
        logout_icon_photo = ImageTk.PhotoImage(logout_icon_image)
        logout_button = tk.Button(user_info_frame, text="Log out", command=self.logout, image=logout_icon_photo, compound="left", bg="#4caf50", fg="white", relief="raised", bd=3)
        logout_button.image = logout_icon_photo
        logout_button.pack(side="right", padx=10, pady=10)

    def add_announcements(self):
        announcements_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="solid")
        announcements_frame.pack(pady=10, padx=20, fill="x")

        announcements_title = tk.Label(announcements_frame, text="Announcements", font=("Arial", 14, "bold"), bg="#ffffff")
        announcements_title.pack(pady=5)

        announcements_info = tk.Label(announcements_frame, text="New books available in the Fiction section! Library closed on public holidays.\nJoin our book club every Saturday.", font=("Arial", 12), bg="#ffffff", justify="center")
        announcements_info.pack(pady=5)

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(side="left", padx=20, pady=20)

        button_specs = [
            ("Books", self.show_books, "image/book_icon1.png"),
            ("Donate Book", self.donate_book, "image/add_book.png"),
            ("Edit Book", self.edit_book, "image/edit_book.png"),
            ("Return Book", self.return_book, "image/return_book1.png"),
            ("Articles", self.show_articles, "image/book_icon2.png")
        ]

        for spec in button_specs:
            text, command = spec[:2]
            icon = spec[2] if len(spec) > 2 else None
            if icon:
                icon_image = Image.open(icon)
                icon_image = icon_image.resize((20, 20), Image.LANCZOS)
                icon_photo = ImageTk.PhotoImage(icon_image)
                button = tk.Button(buttons_frame, text=text, command=command, width=200, height=40, font=("Arial", 12, "bold"), bg="#4caf50", fg="white", relief="raised", bd=3, compound="left", image=icon_photo)
                button.image = icon_photo  # Keep a reference to the image
            else:
                button = tk.Button(buttons_frame, text=text, command=command, width=25, height=2, font=("Arial", 12, "bold"), bg="#4caf50", fg="white", relief="raised", bd=3)
            button.pack(pady=10, anchor="w")

    def add_middle_content(self):
        content_frame = tk.Frame(self.root, bg="#f0f0f0")
        content_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Statistics container frame
        stats_frame = tk.Frame(content_frame, bg="#ffffff", bd=2, relief="solid", height=150)
        stats_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Create a Matplotlib figure and add it to the stats frame
        fig = Figure(figsize=(5, 2), dpi=100)
        ax = fig.add_subplot(111)

        # Sample data for the graph
        labels = ['Total Books', 'Borrowed Books', 'Returned Books', 'Members', 'New Books']
        values = [1500, 300, 200, 350, 50]

        ax.bar(labels, values, color=['#4caf50', '#ff9800', '#f44336', '#2196f3', '#9c27b0'])
        ax.set_title('Library Statistics')
        ax.set_ylabel('Count')

        canvas = FigureCanvasTkAgg(fig, master=stats_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def show_profile(self):
        from Profile_window import ProfileWindow
        self.root.iconify()
        ProfileWindow(master=self.root, user=self.user)

    def show_books(self):
        from all_books import BooksWindow
        self.root.iconify()
        BooksWindow(self.root, self.user['username'])

    def donate_book(self):
        from donate_book import DonateBookWindow
        self.root.iconify()
        DonateBookWindow(self.root, self.user['username'])

    def edit_book(self):
        from edit_book import open_edit_book_window
        self.root.iconify()
        open_edit_book_window(self.root)

    def return_book(self):
        try:
            book_id = int(simpledialog.askstring("Return Book", "Enter the Book ID to return:"))
        except (TypeError, ValueError):
            messagebox.showwarning("Invalid Input", "Please enter a valid numeric Book ID.")
            return

        register_borrow_return(book_id, self.user['username'], "Returned")
        update_book_count(book_id, True)
        messagebox.showinfo("Book Returned", f"Book with ID {book_id} has been returned by {self.user['username']}.")

    def show_articles(self):
        from articles import open_articles_window
        open_articles_window(self.root)

    def logout(self):
        self.root.destroy()
        messagebox.showinfo("Logout", "You have been logged out.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("800x500")
    root.configure(bg="#f0f0f0")

    open_dashboard_button = tk.Button(root, text="Open Dashboard", command=lambda: DashboardWindow(root, "farhan"), width=25, height=2, font=("Arial", 12, "bold"), bg="#4caf50", fg="white", relief="raised", bd=3)
    open_dashboard_button.pack(pady=20)

    root.mainloop()
