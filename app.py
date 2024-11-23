from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and dependencies
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uruti.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Base User Model (common fields for all types)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    linkedin_url = db.Column(db.String(255))
    role = db.Column(db.String(20), nullable=False)  # "mentor", "entrepreneur", "investor"
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

# Mentor Class (inherits from User)
class Mentor(User):
    __tablename__ = 'mentors'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    area_of_expertise = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'mentor',
    }

# Entrepreneur Class (inherits from User)
class Entrepreneur(User):
    __tablename__ = 'entrepreneurs'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    years_of_experience = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'entrepreneur',
    }

# Investor Class (inherits from User)
class Investor(User):
    __tablename__ = 'investors'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    investment_interest = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'investor',
    }

# Serve CSS, JS, Images, and Fonts from the templates directory (css, fonts, images, js)
@app.route('/<path:folder>/<path:filename>')
def custom_static(folder, filename):
    valid_folders = ['css', 'js', 'images', 'fonts']  # Add other asset folders if needed
    if folder in valid_folders:
        return send_from_directory(os.path.join('templates', folder), filename)
    else:
        return "Invalid folder", 404

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to render the Resources page
@app.route('/resources')
def resources():
    return render_template('resources.html')  # Ensure you have a resources.html file in the templates folder

# Route to render the About Us page
@app.route('/about')
def about():
    return render_template('about-us.html')  # Ensure you have a about.html file in the templates folder

# Route to render the Contact Us page
@app.route('/contact')
def contact():
    return render_template('contact-us.html')  # Ensure you have a contact.html file in the templates folder

# Route to render the Registration page
@app.route('/registration')
def registration():
    return render_template('registration.html')  # Ensure you have a registration.html file in the templates folder

# Route to handle user registration
@app.route('/register/<role>', methods=['POST'])
def register(role):
    try:
        # Common fields for all roles
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')
        phone_number = request.form.get('phone_number')
        linkedin_url = request.form.get('linkedin_url')

        # Role-specific logic
        if role == "mentor":
            area_of_expertise = request.form.get('area_of_expertise')
            new_user = Mentor(
                full_name=full_name,
                email=email,
                password=password,
                phone_number=phone_number,
                linkedin_url=linkedin_url,
                area_of_expertise=area_of_expertise,
                role="mentor"
            )
        elif role == "entrepreneur":
            years_of_experience = request.form.get('years_of_experience', 0)
            new_user = Entrepreneur(
                full_name=full_name,
                email=email,
                password=password,
                phone_number=phone_number,
                linkedin_url=linkedin_url,
                years_of_experience=int(years_of_experience),
                role="entrepreneur"
            )
        elif role == "investor":
            investment_interest = request.form.get('investment_interest')
            new_user = Investor(
                full_name=full_name,
                email=email,
                password=password,
                phone_number=phone_number,
                linkedin_url=linkedin_url,
                investment_interest=investment_interest,
                role="investor"
            )
        else:
            flash("Invalid role provided.")
            return redirect(url_for('registration'))

        # Save to database
        db.session.add(new_user)
        db.session.commit()

        # Redirect to role-specific dashboard
        return redirect(url_for(f'{role}_dashboard'))

    except IntegrityError:
        db.session.rollback()
        flash("Email already exists. Please use a different email.")
        return redirect(url_for('registration'))
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for('registration'))

# Dashboards for each role
@app.route('/dashboard/mentor')
def mentor_dashboard():
    return render_template('mentor_dashboard.html')

@app.route('/dashboard/entrepreneur')
def entrepreneur_dashboard():
    return render_template('ent_dashboard.html')

@app.route('/dashboard/investor')
def investor_dashboard():
    return render_template('inv_dashboard.html')

@app.route('/login')
def login():
    return render_template('sign_in.html')

# Initialize the database

def setup():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)