import smtplib
import time
from email.mime.text import MIMEText

def mail(body):
  mail_body=body
  mail_from='john.zhao@i-click.cn'
  mail_to=['363602094@qq.com']
  msg=MIMEText(mail_body)
  msg['Subject']='Every day every news'
  msg['From']=mail_from
  msg['To']=';'.join(mail_to)
  msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
  smtp=smtplib.SMTP()
  smtp.connect('smtp.qiye.163.com')
  smtp.login('john.zhao@i-click.cn','!@#qwe123')
  smtp.sendmail(mail_from,mail_to,msg.as_string())
  smtp.quit()
  print 'ok'