from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory, session
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

class Investor(User):
    __tablename__ = 'investors'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    businessname = db.Column(db.String(100))
    investment_interest = db.Column(db.String(100))
    business_website = db.Column(db.String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'investor',
    }

class Mentor(User):
    __tablename__ = 'mentors'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    area_of_expertise = db.Column(db.String(50))
    years_of_experience = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'mentor',
    }

class Entrepreneur(User):
    __tablename__ = 'entrepreneurs'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    years_of_experience = db.Column(db.Integer)
    businessname = db.Column(db.String(100))
    business_type = db.Column(db.String(100))
    business_stage = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'entrepreneur',
    }

# Serve CSS, JS, Images, and Fonts from the templates directory
@app.route('/<path:folder>/<path:filename>')
def custom_static(folder, filename):
    valid_folders = ['css', 'js', 'images', 'fonts']
    if folder in valid_folders:
        return send_from_directory(os.path.join('templates', folder), filename)
    else:
        # Return 404 for invalid folder requests
        return render_template('404.html'), 404

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

# Route to handle user registration
@app.route('/register/<role>', methods=['POST'])
def register(role):
    try:
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')
        phone_number = request.form.get('phone_number')
        linkedin_url = request.form.get('linkedin_url')

        if role == "mentor":
            new_user = Mentor(
                full_name=full_name,
                email=email,
                password=password,
                phone_number=phone_number,
                linkedin_url=linkedin_url,
                area_of_expertise=request.form.get('area_of_expertise'),
                years_of_experience=int(request.form.get('years_of_experience', 0)),
                role="mentor"
            )
        elif role == "entrepreneur":
            new_user = Entrepreneur(
                full_name=full_name,
                email=email,
                password=password,
                phone_number=phone_number,
                linkedin_url=linkedin_url,
                years_of_experience=int(request.form.get('years_of_experience', 0)),
                businessname=request.form.get('business_name'),
                business_type=request.form.get('business_type'),
                business_stage=request.form.get('stage'),
                role="entrepreneur"
            )
        elif role == "investor":
            new_user = Investor(
                email=email,
                password=password,
                phone_number=phone_number,
                linkedin_url=linkedin_url,
                businessname=request.form.get('business_name'),
                investment_interest=request.form.get('investment_interest'),
                business_website=request.form.get('business_website'),
                role="investor"
            )
        else:
            flash("Invalid role provided.")
            return redirect(url_for('registration'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for(f'{role}_dashboard'))

    except IntegrityError:
        db.session.rollback()
        flash("Email already exists. Please use a different email.")
        return redirect(url_for('registration'))
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for(f'{role}_dashboard'))

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('log')
        password = request.form.get('pwd')
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_role'] = user.role
            session['user_name'] = user.full_name  # Set the full_name here

            if user.role == 'mentor':
                return redirect(url_for('mentor_dashboard'))
            elif user.role == 'entrepreneur':
                return redirect(url_for('entrepreneur_dashboard'))
            elif user.role == 'investor':
                return redirect(url_for('investor_dashboard'))
            else:
                flash("Invalid user role.")
                return redirect(url_for('login'))

        flash("Invalid email or password.")
        return redirect(url_for('login'))

    return render_template('sign_in.html')
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))

def setup():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
