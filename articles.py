import tkinter as tk
from tkinter import messagebox

# Demo article data
demo_articles = [
    {"Article ID": 1, "Author": "Alice Johnson", "Title": "The Future of Artificial Intelligence",
     "Content": "An exploration of AI advancements... AI will continue to evolve...", "Date": "2024-01-15"},
    {"Article ID": 2, "Author": "Bob Smith", "Title": "Climate Change and Its Effects",
     "Content": "A detailed analysis of climate change... Urgent action is needed...", "Date": "2023-12-05"},
    {"Article ID": 3, "Author": "Carol White", "Title": "The Benefits of a Plant-Based Diet",
     "Content": "An overview of the health benefits of plant-based diets... Plant-based diets can improve health and help the environment.", "Date": "2023-08-21"},
    {"Article ID": 4, "Author": "David Brown", "Title": "Blockchain Technology: Beyond Cryptocurrency",
     "Content": "An examination of blockchain uses beyond cryptocurrency... Blockchain has transformative potential across industries.", "Date": "2023-05-18"},
    {"Article ID": 5, "Author": "Emily Davis", "Title": "The Importance of Cybersecurity",
     "Content": "An in-depth look into the need for robust cybersecurity... Protecting data is essential in today's digital age.", "Date": "2023-09-30"},
    {"Article ID": 6, "Author": "Franklin Green", "Title": "Exploring Quantum Computing",
     "Content": "A look at the basics and possibilities of quantum computing... Quantum computing may revolutionize data processing.", "Date": "2024-02-10"},
    {"Article ID": 7, "Author": "Grace Taylor", "Title": "Mental Health Awareness",
     "Content": "An article discussing the importance of mental health... Greater mental health awareness is crucial for society.", "Date": "2023-10-05"},
    {"Article ID": 8, "Author": "Henry Adams", "Title": "Space Exploration: The Next Frontier",
     "Content": "An exploration of humanity's recent advancements in space... The future of space exploration is full of potential.", "Date": "2024-03-01"},
    {"Article ID": 9, "Author": "Isabel Lee", "Title": "Renewable Energy Sources",
     "Content": "An analysis of renewable energy types and benefits... Renewables are key to sustainable development.", "Date": "2023-11-20"},
    {"Article ID": 10, "Author": "Jack Wilson", "Title": "The Evolution of E-commerce",
     "Content": "A discussion on the growth and changes in e-commerce... E-commerce will continue to reshape retail.", "Date": "2023-07-15"}
]

# Dictionary to store comments for each article
comments = {article["Article ID"]: [] for article in demo_articles}

# Function to open the Articles window
def open_articles_window(root):
    articles_window = tk.Toplevel(root)
    articles_window.title("Articles")
    articles_window.geometry("600x600")

    # Function to add a comment
    def add_comment(article_id):
        username = username_entry.get()
        comment_text = comment_entry.get()
        if username and comment_text:
            comments[article_id].append((username, comment_text))
            username_entry.delete(0, tk.END)
            comment_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Comment added successfully!")
            display_comments(article_id)
        else:
            messagebox.showwarning("Input Error", "Please enter both username and comment.")

    # Function to display comments for a specific article
    def display_comments(article_id):
        comment_list.delete(0, tk.END)  # Clear the comment list
        for username, comment in comments[article_id]:
            comment_list.insert(tk.END, f"{username}: {comment}")

    # Create a listbox to display articles
    article_listbox = tk.Listbox(articles_window, width=80, height=15)
    article_listbox.pack(pady=10)

    # Populate the listbox with article titles
    for article in demo_articles:
        article_listbox.insert(tk.END, f"{article['Title']} by {article['Author']} ({article['Date']})")

    # Create a frame for displaying article content and comments
    content_frame = tk.Frame(articles_window)
    content_frame.pack(pady=10)

    # Label for article content
    content_label = tk.Label(content_frame, text="", wraplength=550, justify="left")
    content_label.pack()

    # Label for comments
    comments_label = tk.Label(content_frame, text="Comments:", font=("Arial", 14))
    comments_label.pack()

    # Listbox for displaying comments
    comment_list = tk.Listbox(content_frame, width=80, height=5)
    comment_list.pack()

    # Entry for username and comment
    username_entry = tk.Entry(content_frame, width=60)
    username_entry.pack(pady=5)
    username_entry.insert(0, "Enter your username")

    comment_entry = tk.Entry(content_frame, width=60)
    comment_entry.pack(pady=5)
    comment_entry.insert(0, "Enter your comment")

    # Button to add comment
    comment_button = tk.Button(content_frame, text="Add Comment",
                                command=lambda: add_comment(article_listbox.curselection()[0] + 1) if article_listbox.curselection() else messagebox.showwarning("Selection Error", "Please select an article first."))
    comment_button.pack(pady=5)

    # Function to display article content and comments when an article is selected
    def show_article(event):
        selected_index = article_listbox.curselection()
        if selected_index:
            article_id = selected_index[0] + 1
            selected_article = demo_articles[selected_index[0]]
            content_label.config(text=selected_article["Content"])
            display_comments(article_id)

    # Bind the listbox selection event
    article_listbox.bind("<<ListboxSelect>>", show_article)

# Main application window with Articles button
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("400x300")

    # Button to open the Articles window
    articles_button = tk.Button(root, text="Articles", command=open_articles_window)
    articles_button.pack(pady=20)

    root.mainloop()
