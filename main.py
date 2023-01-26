from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, SelectField,TextAreaField, SubmitField)
from wtforms.validators import DataRequired
# from basic import db, Role # Import database info

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class infoform(FlaskForm):
    cust_name = StringField('Name of Vehicle owner:-',
                            validators=[DataRequired()])
    dealer = SelectField('Select Dealer:-', choices=[(
        '', 'Select Dealer'), ('a', 'a'), ('b', 'b'), ('c', 'c')], validators=[DataRequired()])
    rating = RadioField('Rate Your Dealer:-', choices=[('1', '1'), ('2', '2'), ('3', '3'), (
        '4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('fp.html')
    # return render_template('fp.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = infoform()
    if form.validate_on_submit():
        session['cust_name'] = form.cust_name.data
        session['dealer'] = form.dealer.data
        session['rating'] = form.rating.data
        session['feedback'] = form.feedback.data
        return redirect(url_for("thankyou"))
    return render_template('02-feedback.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('03-thankyou.html')

if __name__ == "__main__":
     app.run(debug=True)