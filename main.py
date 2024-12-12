# import tkinter as tk
# from tkinter import messagebox
# from Login import LoginWindow

# class LibraryManagementSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Library Management System")
#         self.root.geometry("400x300")

#         # Creating the Menu bar
#         menu_bar = tk.Menu(self.root)
#         menu = tk.Menu(menu_bar, tearoff=0)
#         menu.add_command(label="Ask Help", command=self.ask_help)
#         menu.add_command(label="About", command=self.about)
#         menu_bar.add_cascade(label="Menu", menu=menu)
#         self.root.config(menu=menu_bar)

#         # Label for title
#         title_label = tk.Label(self.root, text="Welcome to the Library Management System", font=("Arial", 12))
#         title_label.pack(pady=20)

#         # Admin Login button
#         admin_button = tk.Button(self.root, text="Admin Login", command=self.admin_login, width=20)
#         admin_button.pack(pady=10)

#         # User Login button
#         user_button = tk.Button(self.root, text="User Login", command=self.user_login, width=20)
#         user_button.pack(pady=10)

#     def admin_login(self):
#         messagebox.showinfo("Admin Login", "Redirecting to Admin Login...")

#     def user_login(self):
#         # messagebox.showinfo("User Login", "Redirecting to User Login...")
#         self.root.iconify()
#         LoginWindow(self.root)

#     def ask_help(self):
#         messagebox.showinfo("Ask Help", "For help, please contact support@example.com.")

#     def about(self):
#         messagebox.showinfo("About", "Library Management System\nVersion 1.0\nDeveloped by Farhan.")

# # Creating main window
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LibraryManagementSystem(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk  # Import for handling images
# from Login import LoginWindow

# class LibraryManagementSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Library Management System")
#         self.root.geometry("500x400")

#         # Load background image
#         background_image_path = "image/books2.jpg"
#         background_image = Image.open(background_image_path)
#         background_photo = ImageTk.PhotoImage(background_image)

#         # Create a canvas to hold the background image
#         self.canvas = tk.Canvas(self.root, width=500, height=400)
#         self.canvas.pack(fill="both", expand=True)
        
#         # Display the background image
#         self.canvas.create_image(0, 0, image=background_photo, anchor="nw")
#         self.background_photo = background_photo  # Keep a reference to the image

#         # Creating the Menu bar
#         menu_bar = tk.Menu(self.root)
#         menu = tk.Menu(menu_bar, tearoff=0)
#         menu.add_command(label="Ask Help", command=self.ask_help)
#         menu.add_command(label="About", command=self.about)
#         menu_bar.add_cascade(label="Menu", menu=menu)
#         self.root.config(menu=menu_bar)

#         # Label for title
#         title_label = tk.Label(self.root, text="Welcome to the Library Management System", font=("Arial", 16, "bold"), bg="#f0f0f0")
#         title_label.place(x=50, y=50)

#         # Frame for login buttons
#         login_frame = tk.Frame(self.root, bg="#f0f0f0")
#         login_frame.place(x=100, y=150)

#         # Admin Login button
#         admin_button = tk.Button(login_frame, text="Admin Login", command=self.admin_login, width=20, height=2, font=("Arial", 12, "bold"), bg="#4caf50", fg="white", relief="raised", bd=3)
#         admin_button.grid(row=0, column=0, padx=10, pady=10)

#         # User Login button
#         user_button = tk.Button(login_frame, text="User Login", command=self.user_login, width=20, height=2, font=("Arial", 12, "bold"), bg="#2196f3", fg="white", relief="raised", bd=3)
#         user_button.grid(row=0, column=1, padx=10, pady=10)

#     def admin_login(self):
#         messagebox.showinfo("Admin Login", "Redirecting to Admin Login...")

#     def user_login(self):
#         self.root.iconify()
#         LoginWindow(self.root)

#     def ask_help(self):
#         messagebox.showinfo("Ask Help", "For help, please contact support@example.com.")

#     def about(self):
#         messagebox.showinfo("About", "Library Management System\nVersion 1.0\nDeveloped by Farhan.")

# # Creating main window
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LibraryManagementSystem(root)
#     root.mainloop()



import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import for handling images
from Login import LoginWindow

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x400")

        # Load background image
        background_image_path = "image/books2.jpg"
        background_image = Image.open(background_image_path)
        background_photo = ImageTk.PhotoImage(background_image)

        # Create a canvas to hold the background image
        self.canvas = tk.Canvas(self.root, width=500, height=400)
        self.canvas.pack(fill="both", expand=True)
        
        # Display the background image
        self.canvas.create_image(0, 0, image=background_photo, anchor="nw")
        self.background_photo = background_photo  # Keep a reference to the image

        # Creating the Menu bar
        menu_bar = tk.Menu(self.root)
        menu = tk.Menu(menu_bar, tearoff=0)
        menu.add_command(label="Ask Help", command=self.ask_help)
        menu.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

        # Label for title
        title_label = tk.Label(self.root, text="Welcome to the Library Management System", font=("Arial", 16, "bold"), bg="#f0f0f0")
        title_label.place(relx=0.5, rely=0.3, anchor="center")

        # Frame for login buttons
        login_frame = tk.Frame(self.root, bg="#f0f0f0")
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Admin Login button
        admin_button = tk.Button(login_frame, text="Admin Login", command=self.admin_login, width=20, height=2, font=("Arial", 12, "bold"), bg="#4caf50", fg="white", relief="raised", bd=3)
        admin_button.grid(row=0, column=0, padx=10, pady=10)

        # User Login button
        user_button = tk.Button(login_frame, text="User Login", command=self.user_login, width=20, height=2, font=("Arial", 12, "bold"), bg="#2196f3", fg="white", relief="raised", bd=3)
        user_button.grid(row=0, column=1, padx=10, pady=10)

    def admin_login(self):
        messagebox.showinfo("Admin Login", "Redirecting to Admin Login...")

    def user_login(self):
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
