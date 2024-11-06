# Data classes for demo objects (replace these with actual classes if available)
class Book:
    def __init__(self, bookId, name, writer, published_date, genre, read_count, available, language):
        self.bookId = bookId
        self.name = name
        self.writer = writer
        self.published_date = published_date
        self.genre = genre
        self.read_count = read_count
        self.available = available
        self.language = language

class Article:
    def __init__(self, articleId, author, title, description, conclusion, published_date):
        self.articleId = articleId
        self.author = author
        self.title = title
        self.description = description
        self.conclusion = conclusion
        self.published_date = published_date

class Comment:
    def __init__(self, article_id, username, body, published_date):
        self.article_id = article_id
        self.username = username
        self.body = body
        self.published_date = published_date

class User:
    def __init__(self, username, email, phone, address, university, fav_genres, password) -> None:
        self.username = username
        self.email = email
        self.phone = phone
        self.address = address
        self.university = university
        self.fav_genres = fav_genres
        self.password = password
        

# Demo data creation
demo_books = [
    {"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publish_date": "1925-04-10", "genre": "Fiction", "pages": 1200, "available": True, "language": "English"},
    {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publish_date": "1960-07-11", "genre": "Fiction", "pages": 1500, "available": True, "language": "English"},
    {"book_id": 3, "title": "1984", "author": "George Orwell", "publish_date": "1949-06-08", "genre": "Dystopian", "pages": 800, "available": False, "language": "English"},
    {"book_id": 4, "title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "publish_date": "1967-06-05", "genre": "Magical Realism", "pages": 600, "available": True, "language": "Spanish"},
    {"book_id": 5, "title": "Pride and Prejudice", "author": "Jane Austen", "publish_date": "1813-01-28", "genre": "Romance", "pages": 2000, "available": True, "language": "English"},
    {"book_id": 6, "title": "Brave New World", "author": "Aldous Huxley", "publish_date": "1932-09-01", "genre": "Dystopian", "pages": 700, "available": True, "language": "English"},
    {"book_id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "publish_date": "1951-07-16", "genre": "Fiction", "pages": 900, "available": False, "language": "English"},
    {"book_id": 8, "title": "The Alchemist", "author": "Paulo Coelho", "publish_date": "1988-01-01", "genre": "Adventure", "pages": 1800, "available": True, "language": "Portuguese"},
    {"book_id": 9, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "publish_date": "1880-11-01", "genre": "Philosophical Fiction", "pages": 500, "available": True, "language": "Russian"},
    {"book_id": 10, "title": "War and Peace", "author": "Leo Tolstoy", "publish_date": "1869-01-01", "genre": "Historical Fiction", "pages": 300, "available": False, "language": "Russian"}
]


demo_articles = [
    Article(1, "Alice Johnson", "The Future of Artificial Intelligence", "An exploration of AI advancements...", "AI will continue to evolve...", "2024-01-15"),
    Article(2, "Bob Smith", "Climate Change and Its Effects", "A detailed analysis of climate change...", "Urgent action is needed...", "2023-12-05"),
    Article(3, "Carol White", "The Benefits of a Plant-Based Diet", "An overview of the health benefits of plant-based diets...", "Plant-based diets can improve health and help the environment.", "2023-08-21"),
    Article(4, "David Brown", "Blockchain Technology: Beyond Cryptocurrency", "An examination of blockchain uses beyond cryptocurrency...", "Blockchain has transformative potential across industries.", "2023-05-18"),
    Article(5, "Emily Davis", "The Importance of Cybersecurity", "An in-depth look into the need for robust cybersecurity...", "Protecting data is essential in today's digital age.", "2023-09-30"),
    Article(6, "Franklin Green", "Exploring Quantum Computing", "A look at the basics and possibilities of quantum computing...", "Quantum computing may revolutionize data processing.", "2024-02-10"),
    Article(7, "Grace Taylor", "Mental Health Awareness", "An article discussing the importance of mental health...", "Greater mental health awareness is crucial for society.", "2023-10-05"),
    Article(8, "Henry Adams", "Space Exploration: The Next Frontier", "An exploration of humanity's recent advancements in space...", "The future of space exploration is full of potential.", "2024-03-01"),
    Article(9, "Isabel Lee", "Renewable Energy Sources", "An analysis of renewable energy types and benefits...", "Renewables are key to sustainable development.", "2023-11-20"),
    Article(10, "Jack Wilson", "The Evolution of E-commerce", "A discussion on the growth and changes in e-commerce...", "E-commerce will continue to reshape retail.", "2023-07-15")
]


demo_comments = [
    Comment(1, "john_doe", "Great insights into AI technology.", "2024-02-01"),
    Comment(2, "jane_smith", "Climate change is indeed alarming.", "2023-12-10"),
    Comment(3, "alice_jones", "Plant-based diets are definitely worth trying!", "2023-08-25"),
    Comment(4, "john_doe", "Blockchain's potential beyond crypto is huge.", "2023-06-01"),
    Comment(5, "jane_smith", "Cybersecurity is crucial in our digital world.", "2023-10-02"),
    Comment(6, "alice_jones", "AI developments are both exciting and scary.", "2024-01-20"),
    Comment(7, "frank_green", "Quantum computing will change the world.", "2024-02-15"),
    Comment(8, "grace_taylor", "Mental health awareness is so important.", "2023-10-10"),
    Comment(9, "henry_adams", "Space exploration opens endless possibilities.", "2024-03-05"),
    Comment(10, "isabel_lee", "Renewable energy is our best hope for sustainability.", "2023-11-25")
]


# Functions to retrieve data
def get_articles():
    return demo_articles

def get_books():
    return demo_books

def get_comment(article_id):
    return [c for c in demo_comments if c.article_id == article_id]


def authenticate(username, password):
    if username == password:
        return True
    return False