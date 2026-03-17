import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI','sqlite:///default.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT-SECRET_KEY', 'clave-insegura')

from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
db.imit_app(app)
migrate = Migrate(app,db)
jwt = JWTManager(app)

from routes import api_bp

app.register_blueprint(api_bp, url_prefix='/api')


if __name__ == '__main__':
    puerto= int(os.getenv('PORT', 5000))
    modo_debug = os.getenv('FLASK_DEBUG') == 'True'
    app.run(port = puerto, debug = modo_debug)