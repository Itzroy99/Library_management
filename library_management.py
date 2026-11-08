import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def get_books_by_author(author_name):

    try:

        with create_connection() as con:

            with con.cursor() as cursor:

                query = """
                    SELECT
                        b.title,
                        a.author_name,
                        b.genre

                    FROM books b

                    JOIN book_authors ba
                    ON b.book_id = ba.book_id

                    JOIN authors a
                    ON ba.author_id = a.author_id

                    WHERE a.author_name = %s;
                """

                cursor.execute(query, (author_name,))

                records = cursor.fetchall()

                if records:

                    for record in records:
                        print(record)

                else:
                    print("No books found.")

    except Exception as e:

        print("Database Error:", e)


author = input("Enter author name: ")

get_books_by_author(author)