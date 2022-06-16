from flask import Flask, render_template, request
from controller.index_controller import get_index

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index_page():
    return get_index()
