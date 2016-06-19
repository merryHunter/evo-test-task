from flask import Flask, render_template, request, jsonify
from EpithetManager import EpithetManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CDS1CD4f8sd5dfd2a3fE!FWdsf1v2s68vDDSDvd23sghnjz6gukd'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    name = request.json['name']
    epithet = EpithetManager().get_epithet(unicode(name))
    return jsonify(epithet=epithet)

@app.before_first_request
def init():
    """
        Specify the filename with epithets.
        See 'epithets-shortlist.txt' for specific test-cases,
        such as lack of epithets.
    """

    EpithetManager.set_epithets_dict("epithets.txt")


if __name__ == '__main__':
    app.run()

