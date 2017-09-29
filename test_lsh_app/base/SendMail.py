# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class SendMail:
    def mail(self,resultFilesList):
        sender = 'zhouxin@lsh123.com'
        receivers = 'zhouxin901008@qq.com,zhouxin@lsh123.com'


        message = MIMEMultipart()
        message['From'] = Header("zhouxin@lsh123.com", 'utf-8')
        message['To'] =  receivers

        subject = '测试'
        message['Subject'] = Header(subject, 'utf-8')

        message.attach(MIMEText('商城接口测试结果...\n', 'plain', 'utf-8'))

        for resultFile in resultFilesList:
            att = MIMEText(open(resultFile, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="'+resultFile.split("/")[-1]+'"'
            message.attach(att)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect('smtp.qiye.163.com', 25)
            smtpObj.login(sender, 'Zhouxin111162')
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.quit()
            print "邮件发送成功"
        except smtplib.SMTPException,e:
            print "Error: 无法发送邮件",e