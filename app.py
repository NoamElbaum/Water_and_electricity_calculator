from flask import Flask, render_template, request, redirect
from forms import dataForm
import sqlEditor as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super123'
wPrice = 9
ePrice = 0.58


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = dataForm()
    result = {}
    if form.is_submitted():
        result = request.form
        print(result)
        for x in result:
            if x == 'apartmentA':
                error = sql.addVal('apartment_a', wPrice, ePrice, result['water'], result['electricity'])
            elif x == 'apartmentB':
                error = sql.addVal('apartment_b', wPrice, ePrice, result['water'], result['electricity'])
        if error == 1:
            return 'invalid values'
        return render_template('index.html')
    return render_template('dataPage.html', form=form)


@app.route('/infoA')
def infoA():
    data = sql.getData('apartment_a')
    return render_template('info.html', rows=len(data[0]), dates=data[0], water=data[1], elect=data[2], total_w=data[3],
                           total_e=data[4], pay=data[5])


@app.route('/infoB')
def infoB():
    data = sql.getData('apartment_b')
    return render_template('info.html', val=data)


if __name__ == '__main__':
    app.run(debug=True)
