from flask import Blueprint, session, redirect, url_for, render_template, jsonify, request, flash

from services.transfer_services import get_all_warehouse, get_items_in_warehouse, process_transfer

# Creeaza un blueprint pentru gestionarea transferurilor
transfer_bp = Blueprint('transfer', __name__)

@transfer_bp.route('/transfer')
def transfer():
    # Verifica daca utilizatorul este autentificat (exista in sesiune)
    if 'user' not in session:
        return redirect(url_for('auth.auth'))

    # Obtine lista depozitelor
    warehouses = get_all_warehouse()

    # Randeaza pagina de transfer cu depozitele
    return render_template('transfer.html',
                           warehouses = warehouses)

@transfer_bp.route('/get_items_in_warehouse/<int:warehouse_id>')
def get_items_in_warehouse_route(warehouse_id):
    # Obtine itemele din depozitul specificat
    items = get_items_in_warehouse(warehouse_id)  # Functia interogheaza baza de date
    # Returneaza itemele in format JSON
    return jsonify(items)

@transfer_bp.route('/submit_transfer', methods=['POST'])
def submit_transfer():
    # Preia datele din formular
    source_warehouse_id = request.form.get('source_warehouse_id')
    item_id = request.form.get('item_id')
    destination_warehouse_id = request.form.get('destination_warehouse_id')

    # Daca toate datele sunt disponibile
    if source_warehouse_id and item_id and destination_warehouse_id:
        # Apeleaza functia pentru procesarea transferului
        transfer_successful = process_transfer()

        if transfer_successful:
            flash("Transfer completed successfully!", "success")
        else:
            flash("Error in processing transfer.", "error")

    # Redirectioneaza inapoi pe pagina de dashboard
    return redirect(url_for('dashboard.dashboard'))  # Redirectionare
