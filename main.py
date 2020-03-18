from email_base import EmailBase
from email_base import EmailMessage


def main():
    mail_user = ""
    mail_user_alias = ""
    mail_pass = ""
    mail_host = ""

    email = EmailBase(mail_user, mail_pass, mail_host, mail_user_alias)
    errinfo = email.connect()
    if errinfo:
        print("conn err:", errinfo)
        return

    print("conn sucess!!!")

    message = EmailMessage([mail_user], "email_base test", "hello world!!!")
    errinfo = email.send_email(message)
    if errinfo:
        print("err:", errinfo)
    else:
        print("sucess!!!")


if __name__ == "__main__":
    main()
