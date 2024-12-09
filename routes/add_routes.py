from flask import Blueprint, render_template, session, redirect, url_for, request

from services.add_services import add_item_to_db, add_warehouse_to_db, add_user_to_db

# Creeaza un blueprint pentru gestionarea rutele de adaugare
add_bp = Blueprint('add', __name__)

@add_bp.route('/add')
def add():
    # Verifica daca utilizatorul este conectat, daca nu, redirectioneaza la pagina de autentificare
    if 'user' not in session:
        return redirect(url_for('auth.auth'))

    return render_template('add.html')  # Renderizeaza formularul de adaugare

@add_bp.route('/add_item', methods=['POST'])
def add_item():
    # Preia datele din formular pentru adaugarea unui item
    category = request.form['category']
    name = request.form['name']
    price = request.form['price']

    # Adauga item-ul in baza de date
    add_item_to_db(category, name, price)

    # Redirectioneaza utilizatorul la dashboard sau alta pagina de succes
    return redirect(url_for('dashboard.dashboard'))

@add_bp.route('/add_warehouse', methods=['POST'])
def add_warehouse():
    # Preia datele din formular pentru adaugarea unui depozit
    name = request.form['name']
    address = request.form['address']

    # Adauga depozitul in baza de date
    add_warehouse_to_db(name, address)

    # Redirectioneaza utilizatorul la dashboard sau alta pagina de succes
    return redirect(url_for('dashboard.dashboard'))

@add_bp.route('/add_user', methods=['POST'])
def add_user():
    # Preia datele din formular pentru adaugarea unui utilizator
    username = request.form['username']
    password = request.form['password']

    # Adauga utilizatorul in baza de date
    add_user_to_db(username, password)

    # Redirectioneaza utilizatorul la dashboard sau alta pagina de succes
    return redirect(url_for('dashboard.dashboard'))
