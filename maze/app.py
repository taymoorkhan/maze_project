from flask import Flask, request ,render_template
from models.score_manager import ScoreManager
from models.score import Score
import json

app = Flask(__name__)


@app.route('/')
def all_scores():
    """[summary] displays a list of all the scores in the scores database

    :return: [description]
    :rtype: web page
    """
    manager1 = ScoreManager()
    manager1.from_json()
    return render_template("index.html", results= manager1.serialize())



if __name__ == "__main__":
    app.run(debug=True)