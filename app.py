from flask import Flask
from datetime import datetime


app = Flask(__name__)

FIRST_NAMES = ['Herbie', 'Jessica', 'Fluffles']
LAST_NAMES = ['McPufflestein', 'McDonald']


@app.route('/api/cryptopuff/<token_id>')
def cryptopuff(token_id):
    num_first_names = len(FIRST_NAMES)
    num_last_names = len(LAST_NAMES)
    cryptopuff_name = "%s %s" % (FIRST_NAMES[token_id % num_first_names], LAST_NAMES[token_id % num_last_names])
    return {
        'name': cryptopuff_name,
        'description': "Generic puff description. This really should be customized.",
    }

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)