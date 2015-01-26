import smtplib

from pylons import config
from email.mime.text import MIMEText

mailto = [config.get('smtp.contact_user')]
mail_server = config.get('smtp.server', 'smtp.exmail.qq.com')
mail_user = config.get('smtp.user','ms_scm@missionsky.com')
mail_password = config.get('smtp.password', 'ms_server1_scm')

def send_mail(subject, content):
    msg = MIMEText(content, _subtype="html", _charset="utf-8")
    msg['Subject'] = subject
    msg['From'] = mail_user
    msg['To'] = ';'.join(mailto)

    try:
        server = smtplib.SMTP()
        server.connect(mail_server)
        server.login(mail_user, mail_password)

        server.sendmail(mail_user, mailto, msg.as_string())
        server.close()
        return True
    except Exception, e:
        return False