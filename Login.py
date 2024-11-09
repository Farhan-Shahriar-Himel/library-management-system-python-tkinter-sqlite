import tkinter as tk
from tkinter import messagebox
from Registration import RegistrationWindow
from data_manage import Authenticate


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.title("Login")
        self.root.geometry("400x300")

        # Restore the main window when the login window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

        # Creating the Menu bar
        menu_bar = tk.Menu(self.root)
        menu = tk.Menu(menu_bar, tearoff=0)
        menu.add_command(label="Ask Help", command=self.ask_help)
        menu.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

        # Title Label
        title_label = tk.Label(self.root, text="Login", font=("Arial", 16))
        title_label.pack(pady=20)

        # Username Label and Entry
        username_label = tk.Label(self.root, text="Username")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=5)

        # Password Label and Entry
        password_label = tk.Label(self.root, text="Password")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        login_button = tk.Button(self.root, text="Login", command=self.login)
        login_button.pack(pady=10)

        # Create Account Button
        create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        create_account_button.pack(pady=10)

        # Forgot Password Link
        forgot_password_label = tk.Label(self.root, text="Forgot Password?", fg="blue", cursor="hand2")
        forgot_password_label.pack(pady=5)
        forgot_password_label.bind("<Button-1>", self.forgot_password)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Placeholder login validation
        if Authenticate(username, password):
            from dashboard import DashboardWindow
            self.root.iconify()
            DashboardWindow(self.root, username=username)
            # ProfileWindow(master=self.root, username=username, email=f"{username}@gmail.com", phone="10234", address="Mirpur, Dhaka", university="BUBT", fav_genres=['history', 'programming'], password=password)
            # messagebox.showinfo("Login Success", "Welcome!")
            # self.root.destroy()  # Close the login window on successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def forgot_password(self, event):
        messagebox.showinfo("Forgot Password", "Password recovery instructions sent to your email.")

    def create_account(self):
        self.root.iconify()
        RegistrationWindow(self.root)
        # messagebox.showinfo("Create Account", "Redirecting to account creation page...")

    def close_window(self):
        # Restore the main window and destroy the login window
        self.master.deiconify()
        self.root.destroy()  # Close the login window
        # Optionally, you could also call master.deiconify() here if needed
    
    def ask_help(self):
        pass

    def about(self):
        pass


# Creating main window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200")

    # Function to open the login window and minimize the main window
    def open_login_window():
        root.iconify()  # Minimize the main window
        LoginWindow(root)

    # Button to open the login window
    open_login_button = tk.Button(root, text="Open Login Window", command=open_login_window)
    open_login_button.pack(pady=50)

    root.mainloop()
