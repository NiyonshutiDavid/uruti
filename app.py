from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Serve CSS, JS, Images, and Fonts from the `templates` directory (css, fonts, images, js)
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
    return render_template('resources.html')  # Make sure you have a `resources.html` file in the `templates` folder

# Route to render the About Us page
@app.route('/about')
def about():
    return render_template('about.html')  # Ensure you have a `about.html` file in the `templates` folder

# Route to render the Contact Us page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Ensure you have a `contact.html` file in the `templates` folder

# Route to render the Registration page
@app.route('/registration')
def registration():
    return render_template('registration.html')  # Ensure you have a `registration.html` file in the `templates` folder

if __name__ == '__main__':
    app.run(debug=True)

