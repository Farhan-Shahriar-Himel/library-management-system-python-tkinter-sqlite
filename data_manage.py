import sqlite3 
import bcrypt

def make_hashed(password):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode(), salt)
    hashed_pass_str = hashed_pass.decode('utf-8')
    return hashed_pass_str


def register_it(username, email, phone, password, address, university, img):
    conn = sqlite3.connect("library_database.db")
    
    conn.execute(
        ''' 
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(100) PRIMARY KEY,
            email VARCHAR(100),
            phone VARCHAR(11),
            password VARCHAR(100),
            address VARCHAR(100),
            university VARCHAR(50),
            image BLOB
        )
        '''
    )

    password = make_hashed(password)

    conn.execute(
        '''
        INSERT INTO users (username, email, phone, password, address, university, image)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (username, email, phone, password, address, university, img)
    )

    conn.commit()
    conn.close()



def add_genres(username, genres):
    conn = sqlite3.connect("library_database.db")
    
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS fav_genres(
            username VARCHAR(100),
            genre VARCHAR(20)
        )
        '''
    )

    for genre in genres:
        conn.execute(
            '''
            INSERT INTO fav_genres(username, genre)
            VALUES (?, ?)
            ''', (username, genre)
        )
        conn.commit()

    conn.close()


def Authenticate(username, password):
    conn = sqlite3.connect('library_database.db')

    data = conn.execute(
        "SELECT password FROM users WHERE username = ?", (username,)
    )

    data = data.fetchone()

    if data is None:
        return False
    
    data = data[0].encode()
    
    return bcrypt.checkpw(password.encode(), data)


def get_data(username):
    conn = sqlite3.connect('library_database.db')
    data = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
    column = [description[0] for description in data.description]
    data = data.fetchone()
    user_info = dict(zip(column, data))
    conn.close()
    return user_info


def get_genres(username):
    conn = sqlite3.connect('library_database.db')
    data = conn.execute("SELECT genre FROM fav_genres WHERE username = ?", (username,)).fetchall()
    return [genres[0] for genres in data]
    


def store_book(title, writer, username, genre, language, no_of_copies, published_year, img, book_pdf):
    conn = sqlite3.connect('library_database.db')
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS books(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(50),
            writer VARCHAR(50), 
            username VARCHAR(100),
            genre VARCHAR(50),
            language VARCHAR(50),
            published_year INTEGER,
            no_of_copies INTEGER,
            image BLOB,
            book_pdf BLOB
        )
        '''
    )

    conn.execute(
        '''
        INSERT INTO books(title, writer, username, genre, language, no_of_copies, published_year, image, book_pdf)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, writer, username, genre, language, no_of_copies, published_year, img, book_pdf)
    )
    conn.commit()
    conn.close()


def update_book_count(book_id, return_book = False):
    conn = sqlite3.connect("library_database.db")
    data = conn.execute("SELECT no_of_copies FROM books WHERE book_id = ?", (book_id,)).fetchone()[0]

    if return_book:
        data += 1
    else:
        data -= 1

    conn.execute(
        '''
        UPDATE books
        SET no_of_copies = ?
        WHERE book_id = ?
        ''', (data, book_id)
    )
    conn.commit()
    conn.close()


def get_all_books():
    conn = sqlite3.connect("library_database.db")
    data = conn.execute("SELECT * FROM books")
    columns = [description[0] for description in data.description]
    data = data.fetchall()
    books = []
    for el in data:
        d = dict(zip(columns, el))
        books.append(d)

    return books


def register_reviews(book_id, username, review):
    conn = sqlite3.connect("library_database.db")
    conn.execute(
        '''
        CREATE TABLE IF EXISTS book_reviews(
            username VARCHAR(50),
            book_id INTEGER,
            review VARCHAR(200),
        )
        '''
    )

    conn.execute(
        '''
        INSERT INTO book_reviews(username, book_id, review)
        VALUES (?, ?, ?)
        ''', (username, book_id, review)
    )
    conn.commit()
    conn.close()


def register_borrow_return(book_id, username, transaction):
    conn = sqlite3.connect("library_database.db")
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS transaction_info(
            book_id INTEGER,
            username VARCHAR(100),
            transaction_type VARCHAR(10),
            date TEXT DEFAULT (DATE('now'))
        )
        '''
    )

    conn.execute(
        '''
        INSERT INTO transaction_info(book_id, username, transaction_type)
        VALUES(?, ?, ?)
        ''', (book_id, username, transaction)
    )
    conn.commit()
    conn.close()


def register_review(book_id, username, review):
    conn = sqlite3.connect('library_database.db')
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS books_review(
            book_id INTEGER,
            username VARCHAR(100),
            review TEXT
        )
        '''
    )

    # print(book_id, username, review)

    # Fixed the typo from "VALES" to "VALUES"
    conn.execute(
        '''
        INSERT INTO books_review(book_id, username, review)
        VALUES (?, ?, ?)
        ''', (book_id, username, review)
    )
    conn.commit()
    conn.close()


def get_reviews(book_id):
    conn = sqlite3.connect('library_database.db')
    data = conn.execute("SELECT username, review FROM books_review WHERE book_id = ?", (book_id,)).fetchall()
    ret = []
    for el in data:
        ret.append(dict(zip(['username', 'review'], el)))
    return ret


def get_transactions(username):
    conn = sqlite3.connect("library_database.db")
    data = conn.execute("SELECT book_id, transaction_type, date FROM transaction_info WHERE username = ?", (username,)).fetchall()
    return data

