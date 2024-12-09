from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for

from services.auth_services import verify_auth

# Creeaza un blueprint pentru gestionarea autentificarii
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def auth():
    # Verifica daca utilizatorul este deja autentificat (exista in sesiune)
    if 'user' in session:
        # Daca este autentificat, redirectioneaza-l la dashboard
        return redirect(url_for('dashboard.dashboard'))

    # Daca nu este autentificat, afiseaza pagina de autentificare
    return render_template('auth.html')

@auth_bp.route('/', methods=['POST'])
def verify():
    try:
        # Preia datele de autentificare din cererea JSON
        username = request.json.get('username')
        password = request.json.get('password')

        # Verifica datele de autentificare
        user_data = verify_auth(username, password)

        # Daca datele de autentificare sunt corecte, salveaza informatiile in sesiune
        if user_data:
            session['user'] = user_data
            return redirect(url_for('dashboard.dashboard'))

        # Daca datele sunt incorecte, ridica o eroare
        raise ValueError('Nume de utilizator sau parola incorecta.')

    except ValueError as ve:
        # Returneaza mesajul de eroare in format JSON
        return jsonify({'error_message': str(ve)}), 401

@auth_bp.route('/logout')
def logout():
    # Sterge utilizatorul din sesiune (deconecteaza-l)
    session.pop('user', None)
    # Redirectioneaza la pagina de autentificare
    return redirect(url_for('auth.auth'))
