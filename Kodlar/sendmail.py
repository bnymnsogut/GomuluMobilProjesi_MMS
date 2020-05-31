import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
def SendAlert():

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  email = 'buraya epostamızı giriyoruz'
  password = 'buraya sifremizi giriyoruz'
  server.login(email, password)
  
  send_to_email = 'buraya gonderecegimiz epostamızı giriyoruz'
  subject = 'NOTIFICATION'
  message = 'This is my message'
  file_location = 'picture.jpg'
  
  msg = MIMEMultipart()
  msg['From'] = email
  msg['To'] = send_to_email
  msg['Subject'] = subject

  msg.attach(MIMEText(message, 'plain'))

  # Setup the attachment
  filename = os.path.basename(file_location)
  attachment = open(file_location, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(attachment.read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

  # Attach the attachment to the MIMEMultipart object
  msg.attach(part)

  #server = smtplib.SMTP('smtp.gmail.com', 587)
  #server.starttls()
  #server.login(email, password)
  text = msg.as_string()
  server.sendmail(email, send_to_email, text)
  server.quit()

SendAlert()
