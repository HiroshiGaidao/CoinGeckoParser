import requests
from flask import Flask, render_template, request
import pars

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request)
    if request.method == 'POST':
        print(request)
        if request.form.get('Update') == 'View and Update':
            _data, _time = pars.pars()
            return render_template('index.html', dataset=_data, time=_time)
        elif request.form.get('Hide') == 'Hide':
            _data, _time = pars.pars()
            return render_template('index.html')
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html')


