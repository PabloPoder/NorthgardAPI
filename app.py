from flask import Flask, jsonify
from clans import clans

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "@ZOMBKLAN (northgard api)"})


@app.route('/clans')
def getClans():
    return jsonify({"northgard_clans": clans, "creators": "@ZOMBKLAN"})


@app.route('/clans/<string:name>')
def getClan(name):
    name = name.title()
    clansFounded = [clan for clan in clans if clan['name'] == name]

    if len(clansFounded) > 0:
        return jsonify({"northgard_clan": clansFounded[0], "creators": "@ZOMBKLAN"})

    return jsonify({"message": f"clan {name} not founded", "creators": "@ZOMBKLAN"}), 200


if __name__ == '__main__':
    app.run(debug=True)
