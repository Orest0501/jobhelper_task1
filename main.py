from flask import Flask, jsonify

app = Flask(__name__)

sub1 = {
    "id": 1,
    "name": "Українська мова і література"
}
sub2 = {
    "id": 2,
    "name": "Українська мова"
}
sub3 = {
    "id": 3,
    "name": "Математика"
}
sub4 = {
    "id": 4,
    "name": "Історія України"
}
sub5 = {
    "id": 5,
    "name": "Іноземна мова"
}
sub6 = {
    "id": 6,
    "name": "Творчий конкурс"
}
sub7 = {
    "id": 7,
    "name": "Біологія"
}
sub8 = {
    "id": 8,
    "name": "Географія"
}
sub9 = {
    "id": 9,
    "name": "Фізика"
}
sub10 = {
    "id": 10,
    "name": "Хімія"
}
sub11 = {
    "id": 11,
    "name": "Німецька мова"
}

list_of_subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10]


@app.route('/sub', methods=['GET'])
def get():
    return jsonify(list_of_subject)


@app.route('/sub', methods=['POST'])
def post():
    list_of_subject.append(sub11)
    return jsonify(list_of_subject)


@app.route('/sub', methods=["PUT"])
def put():
    sub1.update({"id": 12,
                 "name": "Українська мова і література"})
    return jsonify(sub1)


@app.route('/sub', methods=["DELETE"])
def delete():
    list_of_subject.remove(sub4)

    return jsonify("{id : 4}")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
