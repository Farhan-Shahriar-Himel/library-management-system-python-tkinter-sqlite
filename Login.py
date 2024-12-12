import tkinter as tk
from tkinter import messagebox
from Registration import RegistrationWindow
from data_manage import Authenticate

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.title("Login Page")
        self.root.geometry("400x500")
        self.root.configure(bg="#F3F4F6")

        # Restore the main window when the login window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

        # Create a frame for the login form
        frame = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=400)

        # Title Label
        title_label = tk.Label(frame, text="Login", font=("Helvetica", 20, "bold"), fg="#1F2937", bg="white")
        title_label.pack(pady=20)

        # Email Label and Entry
        email_label = tk.Label(frame, text="Email", font=("Helvetica", 12), fg="#4B5563", bg="white")
        email_label.pack(anchor="w", padx=20, pady=(10, 0))

        self.email_entry = tk.Entry(frame, font=("Helvetica", 12))
        self.email_entry.pack(fill="x", padx=20, pady=5)

        # Password Label and Entry
        password_label = tk.Label(frame, text="Password", font=("Helvetica", 12), fg="#4B5563", bg="white")
        password_label.pack(anchor="w", padx=20, pady=(10, 0))

        self.password_entry = tk.Entry(frame, font=("Helvetica", 12), show="*")
        self.password_entry.pack(fill="x", padx=20, pady=5)

        # Remember Me Checkbox
        remember_var = tk.IntVar()
        remember_check = tk.Checkbutton(frame, text="Remember me", variable=remember_var, bg="white", font=("Helvetica", 10))
        remember_check.pack(anchor="w", padx=20, pady=10)

        # Login Button
        login_button = tk.Button(frame, text="Log In", font=("Helvetica", 12, "bold"), bg="#3B82F6", fg="white", command=self.login)
        login_button.pack(fill="x", padx=20, pady=10)

        # Divider
        divider_label = tk.Label(frame, text="Don't have an account?", font=("Helvetica", 10), bg="white", fg="#6B7280")
        divider_label.pack(pady=(10, 0))

        # Sign Up Button
        sign_up_button = tk.Button(frame, text="Sign up", font=("Helvetica", 10, "bold"), bg="white", fg="#3B82F6", bd=0, command=self.create_account)
        sign_up_button.pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if Authenticate(email, password):
            from dashboard import DashboardWindow
            self.root.iconify()
            DashboardWindow(self.root, username=email)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    def create_account(self):
        self.root.iconify()
        RegistrationWindow(self.root)

    def close_window(self):
        self.master.deiconify()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200")
    
    def open_login_window():
        root.iconify()  # Minimize the main window
        LoginWindow(root)

    open_login_button = tk.Button(root, text="Open Login Window", command=open_login_window)
    open_login_button.pack(pady=50)

    root.mainloop()
