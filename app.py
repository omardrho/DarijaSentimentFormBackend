from flask import Flask, request
from flask_cors import CORS
import csv

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={r"/save-data": {"origins": "http://localhost:4200"}})
@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json
    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ['sentence', 'sentiment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
    return 'Data saved successfully'

if __name__ == '__main__':
    app.run()