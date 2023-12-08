# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import schedule, time, os, smtplib 

def sendMail():
  email = "Don't forget to take a break!" 
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = "recipient@email.com" 
  msg['From'] = username 
  msg['Subject'] = "Take a BREAK" 
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 



def printMe():
  print("⏰ Sending Reminder")
  sendMail()

schedule.every(1).hour.do(printMe) 

while True:
  schedule.run_pending()
  time.sleep(1)
```
<details> <summary> 👀 Answer </summary>

```python
import schedule, time, os, smtplib 
from email.mime.multipart import MIMEMultipart # Missing imports
from email.mime.text import MIMEText 

password = os.environ['mailPassword'] # Missing secrets, you need to add these yourself or you will still get an error 
username = os.environ['mailUsername']

def sendMail():
  email = "Don't forget to take a break!" 
  server = "smtp.gmail.com" 
  port = 587 
  s = smtplib.SMTP(host = server, port = port) 
  s.starttls() 
  s.login(username, password) 

  msg = MIMEMultipart() 
  msg['To'] = "recipient@email.com" 
  msg['From'] = username 
  msg['Subject'] = "Take a BREAK" 
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg) 
  del msg 



def printMe():
  print("⏰ Sending Reminder")
  sendMail()

schedule.every(1).hours.do(printMe) # Singular interval

while True:
  schedule.run_pending()
  time.sleep(1)
```
</details>