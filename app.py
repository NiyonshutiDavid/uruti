<<<<<<< HEAD
from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
=======
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
>>>>>>> 2a526ad1732e23680cffbab7aa7b6c7c71858658

# Initialize Flask app and dependencies
app = Flask(__name__)
<<<<<<< HEAD
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uruti.db'  # database URI
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
=======
app.secret_key = "your_secret_key"

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uruti.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Entrepreneur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    linkedin_profile = db.Column(db.String(200), nullable=True)
    business_name = db.Column(db.String(100), nullable=False)
    business_type = db.Column(db.String(50), nullable=False)
    stage_of_business = db.Column(db.String(50), nullable=False)
    needs_investment = db.Column(db.Boolean, nullable=False)

class Investor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    linkedin_profile = db.Column(db.String(200), nullable=True)
    preferred_investment_stage = db.Column(db.String(50), nullable=False)
    typical_investment_size = db.Column(db.String(50), nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    business_website = db.Column(db.String(200), nullable=True)

class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    linkedin_profile = db.Column(db.String(200), nullable=True)
    area_of_expertise = db.Column(db.String(50), nullable=False)
    years_of_experience = db.Column(db.Integer, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entrepreneur_id = db.Column(db.Integer, db.ForeignKey('entrepreneur.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    cover_image = db.Column(db.String(200), nullable=True)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    commenter_name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

# Routes for projects
@app.route('/submit_project', methods=['GET', 'POST'])
def submit_project():
    if request.method == 'POST':
        if 'user_role' in session and session['user_role'] == 'entrepreneur':
            entrepreneur_id = session['user_id']
            title = request.form['title']
            short_description = request.form['short_description']
            long_description = request.form['long_description']
            cover_image = request.form.get('cover_image')

            project = Project(
                entrepreneur_id=entrepreneur_id,
                title=title,
                short_description=short_description,
                long_description=long_description,
                cover_image=cover_image
            )
            db.session.add(project)
            db.session.commit()
            flash("Project submitted successfully!", "success")
            return redirect(url_for('entrepreneur_dashboard'))
        else:
            flash("Unauthorized access", "error")
            return redirect(url_for('login'))

    return render_template('submit_project.html')

@app.route('/browse_projects')
def browse_projects():
    projects = Project.query.all()
    return render_template('browse_projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_details(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_details.html', project=project)

# Routes for resources
@app.route('/add_resource', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author_name = request.form['author_name']

        resource = Resource(
            title=title,
            description=description,
            author_name=author_name
        )
        db.session.add(resource)
        db.session.commit()
        flash("Resource added successfully!", "success")
        return redirect(url_for('resources'))

    return render_template('add_resource.html')

@app.route('/resource/<int:resource_id>', methods=['GET', 'POST'])
def resource_details(resource_id):
    resource = Resource.query.get_or_404(resource_id)

    if request.method == 'POST':
        comment_text = request.form['comment_text']
        commenter_name = request.form['commenter_name']

        comment = Comment(
            resource_id=resource.id,
            comment_text=comment_text,
            commenter_name=commenter_name
        )
        db.session.add(comment)
        db.session.commit()
        flash("Comment added successfully!", "success")

    comments = Comment.query.filter_by(resource_id=resource.id).all()
    return render_template('resource_details.html', resource=resource, comments=comments)

# Other routes and initialization (unchanged)
>>>>>>> 2a526ad1732e23680cffbab7aa7b6c7c71858658

@app.route('/<path:folder>/<path:filename>')
def custom_static(folder, filename):
    valid_folders = ['css', 'js', 'images', 'fonts']
    if folder in valid_folders:
        return send_from_directory(os.path.join('templates', folder), filename)
    else:
        return "Invalid folder", 404

@app.route('/')
def home():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/about/')
def about():
    return render_template('about-us.html')

@app.route('/contact/')
def contact():
    return render_template('contact-us.html')

@app.route('/registration/')
def registration():
    return render_template('registration.html')
=======
# Initialize database
with app.app_context():
    db.create_all()
>>>>>>> 2a526ad1732e23680cffbab7aa7b6c7c71858658

@app.route('/sign_in/')
def sign_in():
    return render_template('sign_in.html')
    
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

# Initialize the database

def setup():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
