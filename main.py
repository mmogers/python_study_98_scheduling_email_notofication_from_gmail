import schedule, time, os, random, ast
import smtplib #email service`

from email.mime.multipart import MIMEMultipart #email service
from email.mime.text import MIMEText #email service text format

password = os.environ['mailPass']
username = os.environ['mailUsername']


def getRandomQuote(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
      content = file.read()

  con_list = ast.literal_eval(content)
  quotes = content.split('\', \'')
  random_quote = random.choice(quotes)
  return random_quote


def sendEmail():
  email = getRandomQuote("quotes.txt")
  server = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(username, password)
  
  msg = MIMEMultipart()
  msg['To'] = "blabla@yahoo.com"
  msg['From'] = username
  msg['Subject'] = "A new qoute for you!"
  msg.attach(MIMEText(email, 'plain'))
  s.send_message(msg)
  del msg
  

def printMe():
  print("⏰ Sending reminder")
  sendEmail()

schedule.every(15).seconds.do(printMe)

while True:
  schedule.run_pending()
  time.sleep(1)


  
