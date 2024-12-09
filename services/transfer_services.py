from flask import request, redirect, url_for, session

from services.core_services import create_connection


def get_warehouse_id_by_name(warehouse_name):
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a selecta ID-ul depozitului dupa nume
        sql_query = "SELECT id FROM warehouses WHERE name = %s"
        cursor.execute(sql_query, (warehouse_name,))

        # Obține rezultatul
        result = cursor.fetchone()

        # Daca gaseste un rezultat, returneaza ID-ul
        if result:
            return result[0]
        else:
            raise ValueError(f"No warehouse found with name '{warehouse_name}'")

    except Exception as e:
        print(f'get_warehouse_id_by_name ERROR: {e}')
        return None

    finally:
        # Inchide conexiunea si cursorul
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()

def get_all_warehouse():
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a obtine toate depozitele
        sql_query = "SELECT * FROM warehouses"
        cursor.execute(sql_query)

        # Obține toate rezultatele
        results = cursor.fetchall()

        # Returneaza o lista cu toate depozitele
        return results

    except Exception as e:
        print(f'get_all_warehouse_names ERROR: {e}')
        return []

    finally:
        # Inchide conexiunea si cursorul
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()

def get_items_in_warehouse(warehouse_id):
    connection = None
    cursor = None

    try:
        # Creaza conexiunea la baza de date
        connection = create_connection()
        cursor = connection.cursor()

        # Interogare SQL pentru a selecta itemele unice dintr-un depozit, bazate pe data transferului
        sql_query = """
        SELECT 
            i.id AS item_id, 
            i.name AS item_name, 
            it.transfer_datetime 
        FROM items i
        JOIN item_transfer it ON i.id = it.item_id
        WHERE it.warehouse_id = %s
        AND it.transfer_datetime = (
            SELECT MAX(sub_it.transfer_datetime)
            FROM item_transfer sub_it
            WHERE sub_it.item_id = it.item_id
        )
        AND it.transfer_datetime = (
            SELECT MAX(it2.transfer_datetime)
            FROM item_transfer it2
            WHERE it2.item_id = it.item_id
            AND it2.warehouse_id = %s
        )
        ORDER BY it.transfer_datetime DESC;
        """
        cursor.execute(sql_query, (warehouse_id, warehouse_id))

        # Obtine toate rezultatele
        results = cursor.fetchall()

        # Structureaza rezultatele ca o lista de dictionare
        items = [{'item_id': row[0], 'item_name': row[1], 'transfer_datetime': row[2]} for row in results]
        return items

    except Exception as e:
        print(f'get_items_in_warehouse ERROR: {e}')
        return []

    finally:
        # Inchide conexiunea si cursorul
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()

def process_transfer():
    connection = None
    cursor = None

    try:
        item_id = request.form['item_id']
        destination_warehouse_id = request.form['destination_warehouse_id']
        transfer_type = 'standard'  # sau alta logica pentru tipul transferului
        user_id = session['user'][0]  # Trebuie sa iei ID-ul utilizatorului autentificat

        # Interogare pentru a salva transferul in baza de date
        connection = create_connection()
        cursor = connection.cursor()

        sql_query = """
                INSERT INTO item_transfer (item_id, warehouse_id, user_id, transfer_datetime, transfer_type)
                VALUES (%s, %s, %s, NOW(), %s)
                """
        cursor.execute(sql_query, (item_id, destination_warehouse_id, user_id, transfer_type))

        connection.commit()
        cursor.close()
        connection.close()

        # Redirectioneaza catre dashboard sau un mesaj de succes
        return redirect(url_for('dashboard.dashboard'))  # sau un mesaj de succes
    except Exception as e:
        print(f"Error in process_transfer: {e}")

        return print('ERROR')  # sau un mesaj de eroare

    finally:
        # Inchide conexiunea si cursorul
        if cursor is not None and connection is not None:
            cursor.close()
            connection.close()