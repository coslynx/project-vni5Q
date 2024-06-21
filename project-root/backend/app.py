import os
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = 'data/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def validate_csv_files(file1, file2):
    if file1.filename.split('.')[-1] != 'csv' or file2.filename.split('.')[-1] != 'csv':
        return False
    return True

def process_csv_files(file1, file2):
    group_info = pd.read_csv(file1)
    hostel_info = pd.read_csv(file2)
    
    # Add your logic to process CSV files here
    
    return allocation_results

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Missing files'}), 400
    
    file1 = request.files['file1']
    file2 = request.files['file2']
    
    if file1.filename == '' or file2.filename == '':
        return jsonify({'error': 'Empty file name'}), 400
    
    if validate_csv_files(file1, file2):
        allocation_results = process_csv_files(file1, file2)
        return jsonify({'allocation_results': allocation_results}), 200
    else:
        return jsonify({'error': 'Invalid file format. Must be CSV'}), 400

if __name__ == '__main__':
    app.run()