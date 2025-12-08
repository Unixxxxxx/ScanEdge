from flask import Flask, render_template
from flask_mail import Mail, Messages

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kritikas101traveler@gmail.com' 
app.config['MAIL_PASSWORD'] = 'Apple123@'

mail = Mail(app)

@app.route("/send")
def send_email():
    msg = Message(
        subject="Welcome to My App",
        sender="@gmail.com",
        recipients=["receiver@example.com"]
    )

    html_body = render_template("email.html",
                                name="Bikku",
                                link="https://google.com")

    msg.html = html_body

    mail.send(msg)

    return "Email sent successfully!"

