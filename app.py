import random
from flask import Flask, Response


app = Flask(__name__)


def weighted_choice(lst):
    total_weight = sum(obj['weight'] for obj in lst)
    selected_weight = random.uniform(0, total_weight)

    for obj in lst:
        if selected_weight < obj['weight']:
            return obj

        selected_weight -= obj['weight']


@app.route('/', methods=['GET'])
def get_heart():
    answers = [
        {'weight': 0.01, 'code': 200, 'text': '200 OK. you win.'},
        {'weight': 1, 'code': 303, 'text': '303 See other.'},
        {'weight': 1, 'code': 410, 'text': '410 My mind already gone.'},
        {'weight': 1, 'code': 503, 'text': '503 Unavailable for you.'}
    ]
    selected_answer = weighted_choice(answers)
    response = Response(selected_answer['text'], selected_answer['code'])
    return response


@app.route('/', methods=['PUT'])
def put_heart():
    answers = [
        {'weight': 0.1, 'code': 202, 'text': '202 Accepted. Thank you.'},
        {'weight': 1, 'code': 403, 'text': '403 Forbidden. No way!'},
        {'weight': 1, 'code': 406, 'text': '406 I cannot accept.'},
    ]
    selected_answer = weighted_choice(answers)
    response = Response(selected_answer['text'], selected_answer['code'])
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
