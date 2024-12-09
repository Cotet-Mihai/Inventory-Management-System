import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

secret_key = os.getenv('SECRET_KEY')

def create_connection():
    """
    Creeaza o conexiune la baza de date folosind datele din fisierul .env.

    :return: Obiectul conexiunii MySQL, sau None daca conexiunea nu poate fi stabilita.
    """
    try:
        # Stabileste conexiunea la baza de date folosind informatiile din .env
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DB')
        )

        return connection  # Returneaza obiectul conexiunii daca este stabilita cu succes

    except Error as e:
        # Afiseaza eroarea daca conexiunea esueaza
        print(f'MySQL Error: {e}')
