from flask import Flask, render_template, make_response

import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)


@app.route('/more')
def learn_more():
    return render_template('learn-more.html')


@app.route('/resume')
def resume():
    binary_pdf = open('static/pdfs/Singh_Resume_.pdf', 'rb').read()
    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
            'inline; filename=%s.pdf' % 'yourfilename'
    return response


if __name__ == '__main__':
    app.run(debug=True)
