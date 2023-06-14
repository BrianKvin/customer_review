from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy 
from send_mail import send_mail
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Cityzen4@localhost/reviewdb'
db = SQLAlchemy(app)

class Review(db.Model):
    __tablename__ = 'customer_review_table'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    retailer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __repr__(self):
        return f"Review('{self.customer}', '{self.retailer}', '{self.rating}', '{self.comments}')"

@app.route('/')
def index():
    logo_url = url_for('static', filename='img/hive-logo.svg')
    return render_template('index.html', logo_url=logo_url)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        retailer = request.form['retailer']
        rating = request.form['rating']
        comments = request.form['comments']
        print(f"{customer}, {retailer}, {rating}, {comments}")
        if customer == '' or retailer == '':
            logo_url = url_for('static', filename='img/hive-logo.svg')
            return render_template('index.html', message='Please enter required fields', logo_url=logo_url)
        
        

        review = Review(customer=customer, retailer=retailer, rating=rating, comments=comments)
        db.session.add(review)
        db.session.commit()
        send_mail(customer, retailer, rating, comments)
        logo_url = url_for('static', filename='img/hive-logo.svg')
        return render_template('success.html', logo_url=logo_url)

@app.route('/feedback')
def feedback():
    reviews = Review.query.all()
    for review in reviews:
        print(len(reviews))
    return "Success"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)