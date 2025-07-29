from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('submit.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
        if request.method == 'POST':
            try:
                # Handle form submission
                name = request.form.get('name')
                email = request.form.get('email')
                message = request.form.get('message')
                write_to_csv(name, email, message)
                return redirect(url_for('thank_you'))
            except:'Did not save to database'
        else:
            return 'Something went wrong, please try again.'
        
def write_to_file(name, email, message):
    # Here you would typically handle the form submission, e.g., save to a database or send an email.
    with open('database.txt', 'a') as f:
        f.write(f'Name: {name}, Email: {email}, Message: {message}\n')

def write_to_csv(name, email, message):
    with open('database.csv', 'a', newline ='') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])
    
if __name__ == '__main__':
    app.run(debug=True)
