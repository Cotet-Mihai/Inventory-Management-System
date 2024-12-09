from services.core_services import create_connection


def get_all_items():
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a selecta toate itemele din tabelul 'items'
        sql_query = "SELECT * FROM items"
        cursor.execute(sql_query)

        # Obtine toate rezultatele
        results = cursor.fetchall()

        # Daca sunt iteme, le returneaza, altfel returneaza o lista goala
        if results:
            return results
        else:
            return []

    except Exception as e:
        print(f'get_all_items ERROR: {e}')

    finally:
        # Inchide conexiunea si cursorul
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()


def get_all_warehouses():
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a selecta toate depozitele din tabelul 'warehouses'
        sql_query = "SELECT * FROM warehouses"
        cursor.execute(sql_query)

        # Obtine toate rezultatele
        results = cursor.fetchall()

        # Daca sunt depozite, le returneaza, altfel returneaza o lista goala
        if results:
            return results
        else:
            return []

    except Exception as e:
        print(f'get_all_warehouses ERROR: {e}')

    finally:
        # Inchide conexiunea si cursorul
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()


def get_all_item_transfers_with_names():
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a selecta transferurile si a le sorta dupa data transferului
        sql_query = """
        SELECT 
            it.transfer_id, 
            i.name AS item_name, 
            w.name AS warehouse_name, 
            u.username AS user_name, 
            it.transfer_datetime, 
            it.transfer_type 
        FROM item_transfer it
        JOIN items i ON it.item_id = i.id
        JOIN warehouses w ON it.warehouse_id = w.id
        JOIN users u ON it.user_id = u.id
        ORDER BY it.transfer_datetime DESC  -- Sorteaza descrescator dupa data transferului
        """
        cursor.execute(sql_query)

        # Obtine toate rezultatele
        results = cursor.fetchall()

        # Daca exista transferuri, le returneaza, altfel returneaza o lista goala
        if results:
            return results
        else:
            return []

    except Exception as e:
        print(f'get_all_item_transfers_with_names ERROR: {e}')

    finally:
        # Inchide conexiunea si cursorul
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()