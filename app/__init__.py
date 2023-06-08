from flask import Flask, render_template
from app.config import Config
app=Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def home():
    return '<h1>Package Tracker</h1>'