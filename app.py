from flask import Flask

# Importa blueprint-urile care gestioneaza diferite rute din aplicatie
from routes.add_routes import add_bp
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.transfer_routes import transfer_bp
from services.core_services import secret_key  # Secret Key pentru securitatea aplicatiei

# Creeaza instanta aplicatiei Flask
app = Flask(__name__)

# Seteaza cheia secreta pentru sesiuni si operatiuni de securitate
app.secret_key = secret_key

# Inregistreaza blueprint-urile care contin rutele pentru diferite sectiuni ale aplicatiei
app.register_blueprint(auth_bp)  # Rute pentru autentificare
app.register_blueprint(dashboard_bp)  # Rute pentru dashboard
app.register_blueprint(transfer_bp)  # Rute pentru transferuri de iteme
app.register_blueprint(add_bp)  # Rute pentru adaugarea de iteme, utilizatori sau depozite

# Verifica daca acest script este rulat direct (nu importat ca modul)
if __name__ == '__main__':
    # Porneste serverul Flask pe orice IP si activeaza modul de debug pentru erori detaliate
    app.run(host='0.0.0.0', debug=True)
