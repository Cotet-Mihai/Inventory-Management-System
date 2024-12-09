from services.core_services import create_connection


def add_item_to_db(category, name, price):
    """
    Adauga un nou item in baza de date.

    :param category: Categoria itemului (str)
    :param name: Numele itemului (str)
    :param price: Pretul itemului (float)
    :return: ID-ul itemului inserat, sau None daca a aparut o eroare.
    """
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a insera un nou item
        sql_query = """
        INSERT INTO items (category, name, price)
        VALUES (%s, %s, %s);
        """
        cursor.execute(sql_query, (category, name, price))

        # Confirma modificarile in baza de date
        connection.commit()

        # Returneaza ID-ul noului item
        return cursor.lastrowid

    except Exception as e:
        print(f'add_item ERROR: {e}')
        return None

    finally:
        # Inchide cursorul si conexiunea la baza de date
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()

def add_user_to_db(username, password):
    """
    Adauga un nou utilizator in baza de date.

    :param username: Numele de utilizator al noului utilizator (str)
    :param password: Parola pentru noul utilizator (str)
    :return: ID-ul utilizatorului inserat, sau None daca a aparut o eroare.
    """
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a insera un nou utilizator
        sql_query = """
        INSERT INTO users (username, password)
        VALUES (%s, %s);
        """
        cursor.execute(sql_query, (username, password))

        # Confirma modificarile in baza de date
        connection.commit()

        # Returneaza ID-ul noului utilizator
        return cursor.lastrowid

    except Exception as e:
        print(f'add_user ERROR: {e}')
        return None

    finally:
        # Inchide cursorul si conexiunea la baza de date
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()

def add_warehouse_to_db(name, address):
    """
    Adauga un nou depozit in baza de date.

    :param name: Numele depozitului (str)
    :param address: Adresa depozitului (str)
    :return: ID-ul depozitului inserat, sau None daca a aparut o eroare.
    """
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a insera un nou depozit
        sql_query = """
        INSERT INTO warehouses (name, address)
        VALUES (%s, %s);
        """
        cursor.execute(sql_query, (name, address))

        # Confirma modificarile in baza de date
        connection.commit()

        # Returneaza ID-ul noului depozit
        return cursor.lastrowid

    except Exception as e:
        print(f'add_warehouse ERROR: {e}')
        return None

    finally:
        # Inchide cursorul si conexiunea la baza de date
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()
