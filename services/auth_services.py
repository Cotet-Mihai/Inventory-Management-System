from services.core_services import create_connection


def verify_auth(username: str, password: str):
    """
    Verifica daca utilizatorul exista in baza de date si daca parola este corecta.

    :param username: Numele de utilizator (str)
    :param password: Parola utilizatorului (str)
    :return: Datele utilizatorului (tuple), sau None daca utilizatorul nu este gasit.
    """
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a verifica utilizatorul
        sql_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(sql_query, (username, password))

        # Verifica daca s-au gasit datele utilizatorului
        result = cursor.fetchone()

        if result:
            return result  # Returneaza datele utilizatorului daca au fost gasite

        else:
            return None  # Returneaza None daca nu exista utilizatorul

    except Exception as e:
        # Prinde orice eroare si o afiseaza
        print(f'verify_auth ERROR: {e}')

    finally:
        # Inchide cursorul si conexiunea la baza de date
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()
