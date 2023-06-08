from flask import Flask, render_template, redirect
from app.config import Config
from app.shipping_form import ShippingForm
app=Flask(__name__)
from flask_migrate import Migrate
from app.models import db

db.init_app(app)
migrate = Migrate(app, db)

app.config.from_object(Config)


@app.route('/')
def home():
    return '<h1>Package Tracker</h1>'



@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()

    if form.validate_on_submit():
        # Process the form data and perform necessary actions
        # Redirect to the root endpoint on successful form submission
        return redirect('/')

    return render_template('shipping_request.html', form=form)
