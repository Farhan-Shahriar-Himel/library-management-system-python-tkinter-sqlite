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
    





    