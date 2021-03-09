from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ldjflkjdaf_lkjadlfkj_akldjflkjaflkjadljf'


class TestForm(FlaskForm):
    dogs_answer = RadioField(
        'Любите ли вы собак?',
        choices=[('yes', 'Естественно'), ('no', 'Фууу! нет')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    agent_answer = RadioField(
        'Спонсируют ли вас из других стран?',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    kvn_answer = RadioField(
        'Отношение к КВН?',
        choices=[('yes', 'Непосредственное'), ('no', 'Кто этот Ваш КВН?')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    kege_answer = RadioField(
        'Сдаете ли Вы КЭГЕ21?',
        choices=[('yes', 'Конечно, да, конечно!'), ('no', 'Нет, Я Костя Тодышев')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    submit = SubmitField('Узнать результат')


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm()
    if form.validate_on_submit():
        return render_template(
            'result.html',
            dogs=form.dogs_answer.data,
            agent=form.agent_answer.data,
            kvn = form.dogs_answer.data,
            kege=form.kege_answer.data
        )
    return render_template('test.html', form=form)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)