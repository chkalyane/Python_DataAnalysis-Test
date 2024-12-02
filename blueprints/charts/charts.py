from flask import Blueprint, render_template, redirect,send_file
import numpy as np
import os
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64


charts_blueprint = Blueprint('charts', __name__, template_folder='templates')

@charts_blueprint.route('/')
def index():
    return "Hello from the Blueprint!"

@charts_blueprint.route('/charts')
def charts():
    return render_template("charts/index.html")

@charts_blueprint.route('/charts.png')
def charts_png():
        data = {
            'Category': ['A', 'B', 'C', 'D'],
            'Values': [23, 45, 56, 78]
        }
        fig, ax = plt.subplots()
        ax.bar(data['Category'], data['Values'])

        # Save it to a temporary buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return send_file(buf, mimetype ='img/png')

@charts_blueprint.route('/charts1.png')
def charts1_png():
        # Load an example dataset from seaborn
    data = {
            'Category': ['A', 'B', 'C', 'D'],
            'Values': [23, 45, 56, 78]
        }
    
    # Create a seaborn plot
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x="Category", y="Values", hue="Values", ax=ax)
    
    # Save it to a temporary buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    
    return send_file(buf, mimetype='image/png')
