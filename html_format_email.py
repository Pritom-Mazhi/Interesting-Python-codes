import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host = "smtp.gmail.com"
port = 587
username = "testmail3018"
password = "testing3018"
from_email = username
to_mail_list = ["testmail3018@gmail.com", "rasel_cse07@gmail.com"]


try:
    gmail_connection = smtplib.SMTP(host, port)
    #gmail_connection is just an instance of smtplib ---> SMTP class,it can be renamed to whatever we want
    #from smtplib import SMTP --> gmail_connection = SMTP(host, port)
    gmail_connection.ehlo()
    gmail_connection.starttls()
    gmail_connection.login(username, password)
    # gmail_connection.sendmail(from_email, to_mail_list, "this is a mail from code")
    # gmail_connection.quit()
    #this should be completed by importing all exceptions and using some block of code which handles exception_handling so if there is an error occurs,the server is not down on our end.

    the_message = MIMEMultipart("alternative")
    the_message["Subject"] = "hi there! trying to send some html formatted message"
    #Subject - - s capital letter
    the_message["From"] = from_email
    #From - - f in capital letter

    #the_message["To"] = to_mail_list - - encoding error

    #the_message["To"] = to_mail_list[0] - - no error but we don't need it because ...gmail_connection.sendmail(arg1,arg2,arg3) we wrote down there
    #the_message["To"] = to_mail_list[1]


    plain_txt = "testing the message"
    html_txt = """\
    <html>
    <head></head>
    <body>
    <p>Hey<br>
        Testing this email <b>message</b> Tried By <a href="https://github.com/Pritom-Mazhi">Pritom Mazhi</a>
    </p>

    </body>
    </html>

    """

    #building the parts of the message in formation
    part1 = MIMEText(plain_txt, 'plain')
    part2 = MIMEText(html_txt, 'html')

    #attaching the formation to the message to be send
    the_message.attach(part1)
    the_message.attach(part2)

    #to display in an accurate way
    #the_message.as_string() - - written in the next line

    #sending
    gmail_connection.sendmail(from_email, to_mail_list, the_message.as_string())
    gmail_connection.quit()

except smtplib.SMTPException:
    print("error sending message")
    #handling exceptions
