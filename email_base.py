import smtplib
from email.mime.text import MIMEText
from email.header import Header

import traceback

class EmailBase(object):
    def __init__(self, mail_user, mail_pass, mail_host, mail_user_alias=None):
        self.__mail_user = mail_user
        self.__mail_pass = mail_pass
        self.__mail_host = mail_host
        self.__mail_user_alias = mail_user_alias
        """
        smtp服务器:
            新浪:smtp.sina.com
            新浪VIP:smtp.vip.sina.com
            搜狐:smtp.sohu.com
            126:smtp.126.com
            139:smtp.139.com
            163:smtp.163.com
            qq:smtp.qq.com
            gmail:smtp.gmail.com
        """

        self.__smtp_obj = None

    def __del__(self):
        self.close()

    def connect(self):
        if self.__smtp_obj:
            return None

        try:
            self.__smtp_obj = smtplib.SMTP_SSL(host=self.__mail_host, local_hostname="localhost", port=465, timeout=30)
            self.__smtp_obj.login(self.__mail_user, self.__mail_pass)
        except:
            return traceback.format_exc()

        return None

    def close(self):
        if self.__smtp_obj:
            self.__smtp_obj.close()
            self.__smtp_obj = None

    def send_email(self, email_message):

        if not self.__smtp_obj:
            return "not connect"

        if type(email_message) is not EmailMessage:
            return "email_message Type error"

        try:
            message = MIMEText(email_message.content(), email_message.subtype(), "utf-8")
            message["From"] = self.__mail_user if not self.__mail_user_alias else "{0}<{1}>".format(self.__mail_user_alias, self.__mail_user)
            message["To"] = ','.join([str(e) for e in email_message.receivers()])
            message["Subject"] = Header(email_message.subject(), "utf-8")
            self.__smtp_obj.sendmail(self.__mail_user, email_message.receivers(), message.as_string())
            return None
        except:
            return traceback.format_exc()

class EmailMessage(object):

    def __init__(self, receivers=None, subject=None, content=None, subtype="plain"):
        self.__receivers = receivers
        self.__subject = subject
        self.__content = content
        self.__subtype = subtype

    def receivers(self):
        return self.__receivers
    def subject(self):
        return self.__subject
    def content(self):
        return self.__content
    def subtype(self):
        return self.__subtype

