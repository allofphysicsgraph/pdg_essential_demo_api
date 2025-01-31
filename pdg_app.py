#!/usr/bin/env python3
# Ben Payne
# Physics Derivation Graph
# https://allofphysics.com
# Creative Commons Attribution 4.0 International License
# https://creativecommons.org/licenses/by/4.0/

from flask import Flask, render_template, Blueprint, jsonify

web_app = Flask(__name__)

# http://flask.palletsprojects.com/en/1.1.x/tutorial/views/
bp = Blueprint("my_api", __name__, url_prefix="/api")



@web_app.route('/', methods=['GET', 'POST'])
def index():
    # https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates
    return render_template("hello.html")

@bp.route("/v1/list", methods=["GET"])
def api_list():
    """
    curl -s http://localhost:5000/api/v1/list | python3 -m json.tool

    """
    list_of_things = ['a', 'b']

    return jsonify(list_of_things)

web_app.register_blueprint(bp)

if __name__ == '__main__':
    web_app.run(debug=True, host="0.0.0.0")

