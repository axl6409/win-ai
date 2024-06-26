from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    api_key = db.Column(db.String(200), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(f"Received data: {data}")  # Log pour le débogage
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')  # Changement ici
    new_user = User(email=data['email'], password=hashed_password, api_key=data['api_key'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(f"Login attempt: {data['email']}")  # Log pour le débogage
    user = User.query.filter_by(email=data['email']).first()
    if user:
        print(f"User found: {user.email}")  # Log pour le débogage
        if check_password_hash(user.password, data['password']):
            print("Password check passed")  # Log pour le débogage
            return jsonify({"email": user.email, "api_key": user.api_key})
        else:
            print("Password check failed")  # Log pour le débogage
    else:
        print("User not found")  # Log pour le débogage
    return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
