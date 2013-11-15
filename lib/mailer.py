import smtplib
import time
from email.mime.text import MIMEText

def mail(body):
  mail_body=body
  mail_from='john.zhao@qq.com'
  mail_to=['13522032151@139.com']
  msg=MIMEText(mail_body, _subtype='plain', _charset='UTF-8')
  msg['Subject']='Every day every news'
  msg['From']=mail_from
  msg['To']=';'.join(mail_to)
  msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
  smtp=smtplib.SMTP()
  smtp.connect('smtp.qq.com')
  smtp.login('363602094@qq.com','!@#zx19880427')
  smtp.sendmail(mail_from,mail_to,msg.as_string())
  smtp.quit()
  print 'ok'