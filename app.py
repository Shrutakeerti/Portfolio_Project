from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '0dd98bf054626851ca4484790f4a060c05fcec610269f66d311f7bfd860cf1ee'

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
print("Checking files in:", UPLOAD_FOLDER)
print("Files:", os.listdir(UPLOAD_FOLDER))  



db = SQLAlchemy(app)

# Model for Contact Messages
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Experience Page
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_message = Contact(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        flash('Message Sent Successfully!', 'success')

    return render_template('contact.html')


# Debug: Check if cv.pdf exists
print("Checking files in:", UPLOAD_FOLDER)
print("Files:", os.listdir(UPLOAD_FOLDER))  # This will print all files inside the folder

@app.route('/download_cv')
def download_cv():
    return send_from_directory('static/uploads', 'CV.pdf', as_attachment=True)

@app.route('/skills')
def skills():
    return render_template('skills.html')





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=False)

