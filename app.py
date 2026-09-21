from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Redgum Tutoring System Running"


@app.route('/students')
def get_students():
    return jsonify({
        "status": "success",
        "students": [
            {"id": "S-0311", "name": "Kai Lombardo", "year": 11, "subject": "Physics"},
            {"id": "S-0402", "name": "Ella Nguyen", "year": 11, "subject": "Physics"}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)