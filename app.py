from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
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

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
