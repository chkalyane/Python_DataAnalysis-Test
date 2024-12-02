from flask import Blueprint, jsonify, render_template_string
import numpy as np
import os
import io
import pandas as pd
import matplotlib.pyplot as plt
import base64

salesapi_bp = Blueprint('sales_bp', __name__)

@salesapi_bp.route('/get_sales', methods=['GET'])
def get_topfive():
    # Get the absolute path to the file
    file_path = os.path.abspath('C:/Users/kk185305/source/upskill/Python_DataAnalysis/blueprints/api/SalesRecords.csv')
    df = pd.read_csv(file_path)
    return df.head(5).to_json()

@salesapi_bp.route('/get_chart', methods=['GET'])
def get_chart():
    file_path = os.path.abspath('C:/Users/kk185305/source/upskill/Python_DataAnalysis/blueprints/api/SalesRecords.csv')
    df = pd.read_csv(file_path)
    df.plot()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    
    return render_template_string('<img src="data:image/png;base64,{{plot_url}}"/>', plot_url=plot_url)