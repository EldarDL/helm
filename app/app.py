from flask import Flask, jsonify, make_response
import csv

app = Flask(__name__)


@app.route('/characters', methods=['GET'])
def get_characters():
    results = []
    with open('../csv/rick_and_morty_characters.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            results.append(row)
    return make_response(jsonify(results), 200)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return make_response(jsonify({'status': 'OK'}), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


