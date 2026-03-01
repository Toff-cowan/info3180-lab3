from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    """Contact form with name, email, subject and message."""

    name = StringField(
        "Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Please enter your full name"},
    )
    email = StringField(
        "E-mail",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Please enter your e-mail address"},
    )
    subject = StringField(
        "Subject",
        validators=[DataRequired()],
        render_kw={"placeholder": "Please enter the subject for your message."},
    )
    message = TextAreaField(
        "Message",
        validators=[DataRequired()],
        render_kw={"placeholder": "Please enter the message you would like to send."},
    )
    submit = SubmitField("Send")
