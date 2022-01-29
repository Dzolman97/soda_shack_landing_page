from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost'
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zcqrvruizcmwqe:1f165cfa0e2a7255b4665c6c2369ce730c453a09ce37eaac2e161a8deca11a8a@ec2-35-170-85-206.compute-1.amazonaws.com:5432/dae2b0cu7d9556'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class People(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(350), unique=True)
    phone = db.Column(db.String(10), unique=True)

    def __init__(self, first_name, last_name, email, phone):
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
       self.phone = phone


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
       first_name = request.form['first-name']
       last_name = request.form['last-name']
       email = request.form['email']
       phone = request.form['phone']
       # Form data comes through

       if db.session.query(People).filter(People.email == email).count() == 0:
          data = People(first_name, last_name, email, phone)
          db.session.add(data)
          db.session.commit()
          send_mail(first_name, last_name, email, phone)
          return render_template('success.html')
       return render_template('index.html', message='You have already subscribed! Thank you!')

if __name__ == '__main__':
    app.run()