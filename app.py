import re
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index_function():
    return render_template("index.html")


@app.route('/result', methods=['post'])
def result_function():
    if request.method == 'POST':
        regex = request.form['in_1']
        test_string = request.form['in_2']
        match = [(ele.start(), ele.end())
                 for ele in re.finditer(regex, test_string, flags=re.IGNORECASE)]
    count = len(match)
    return render_template("result.html", r=regex, t=test_string, match=match, count=count)


if __name__ == '__main__':
    app.run(debug=True)
