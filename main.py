from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField("Cafe Location", validators=[DataRequired()])
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = StringField('Coffe Rating', validators=[DataRequired()])
    wifi = StringField("Wifi", validators=[DataRequired()])
    power = StringField("Power Socket", validators=[DataRequired()])

    submit = SubmitField('Submit', )


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        print("True")
        
        line = "\n"
        cafe = line + form.cafe.data
        location = form.cafe_location.data
        open_time = form.opening_time.data
        close = form.closing_time.data
        coffee = form.coffee_rating.data
        wifi = form.wifi.data
        power = form.power.data
        cafe_data_a = ','.join([cafe, location, open_time, close, coffee, wifi, power])

        with open("cafe-data.csv", "a") as file:
            file.write(cafe_data_a)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    print(list_of_rows)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
