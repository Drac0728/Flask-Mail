from flask import Flask
from flask_mail import Mail, Message
from os import environ as env

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = env.get("EMAIL_USER")
app.config['MAIL_PASSWORD'] = env.get("EMAIL_PASS")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def home():
    
    return "Hello World!"

@app.route('/sendMail')
def sendMail():
    
    msg = Message('Hello', sender='gpt.sahaj28@gmail.com', recipients=['gpt.sahaj28@gmail.com'])
    msg.body = "Hi there, A mail from flask mailand this message is send from environt varibale "

    mail.send(msg)

    return "mail Send"

if __name__ == "__main__":
    app.run(debug=True)

