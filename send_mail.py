import smtplib
from email.mime.text import MIMEText

def send_mail(first_name, last_name, email, phone):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '73163a1ff1923b'
    password = '24f783b6cba454'
    message = f"<h3>New Potential Customer Showing Interest</h3><ul><li>Customer: {first_name} {last_name}</li><li>Email: {email}</li><li>Phone Number: {phone}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Interest in Soda Shack'
    msg['From'] = sender_email
    msg['To'] = receiver_email


    with smtplib.SMTP(smtp_server, port) as server:
       server.login(login, password)
       server.sendmail(sender_email, receiver_email, msg.as_string())