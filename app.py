from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')  # Ensure your homepage HTML is named index.html and placed in the 'templates' folder

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

