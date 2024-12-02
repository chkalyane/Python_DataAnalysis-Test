from flask import *

import matplotlib as ma
import seaborn as sb
from blueprints.home.home import home_blueprint
from blueprints.charts.charts import charts_blueprint
from flask_restful import Resource, Api
from blueprints.api.calculator import  calculator_bp
from blueprints.api.salesapi import  salesapi_bp

app= Flask(__name__)
app.register_blueprint(home_blueprint)
app.register_blueprint(charts_blueprint, url_for="/charts")
app.register_blueprint(calculator_bp)
app.register_blueprint(salesapi_bp)
Api(app)

@app.route("/")
def default():
    return render_template("home/templates/home/index.html")

@app.route("/metrics")
#home page
def metrics():
    return render_template("metrics.html")

if __name__ == "__main__":
    app.run(debug=True)