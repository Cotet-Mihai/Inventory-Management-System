from flask import Blueprint, url_for, redirect, render_template, session

from services.dashboard_services import get_all_items, get_all_warehouses, get_all_item_transfers_with_names

# Creeaza un blueprint pentru gestionarea dashboard-ului
dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # Verifica daca utilizatorul este autentificat (exista in sesiune)
    if 'user' not in session:
        # Daca nu este autentificat, redirectioneaza la pagina de autentificare
        return redirect(url_for('auth.auth'))

    # Preia informatiile utilizatorului din sesiune
    user = session['user']

    # Obtine toate itemele, depozitele si transferurile de iteme din baza de date
    items = get_all_items()
    warehouses = get_all_warehouses()
    transfers = get_all_item_transfers_with_names()

    # Randeaza pagina de dashboard cu informatiile necesare
    return render_template('dashboard.html',
                           username = user[1],  # Numele utilizatorului
                           items = items,  # Lista cu itemele
                           warehouses = warehouses,  # Lista cu depozitele
                           transfers = transfers)  # Lista cu transferurile de iteme
