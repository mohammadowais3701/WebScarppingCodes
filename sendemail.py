import smtplib
from email.mime.text import MIMEText

msg=MIMEText("Hey bro,How are you?")
msg['Subject']="Hello Msg"
msg['From']="mohammadowais3701@gmail.com"
msg['To']='mohammadowais3701@gmail.com'

s=smtplib.SMTP('https://smtp.gmail.com',587)
s.send_message(msg)
s.quit()