from flask import Blueprint, jsonify
import pandas as pd
import numpy as np

calculator_bp = Blueprint('calculator_bp', __name__)

@calculator_bp.route('/get_numbers', methods=['GET'])
def get_numbers():
    numbers = [1, 2]
    return jsonify(numbers)