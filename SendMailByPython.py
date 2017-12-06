import smtplib

host = "smtp.gmail.com"
port = 587
username = "your email username" #gmail_username in this case
password = "your password" #password of that gmail account
from_email = username
to_mail_list = ["testmail3018@gmail.com", "rasel_cse07@gmail.com"]
gmail_connection = smtplib.SMTP(host, port)
#gmail_connection is just an instance of smtplib ---> SMTP class,it can be renamed to whatever we want
#from smtplib import SMTP --> gmail_connection = SMTP(host, port)
gmail_connection.ehlo()
gmail_connection.starttls()
gmail_connection.login(username, password)
gmail_connection.sendmail(from_email, to_mail_list, "this is a mail from code")
gmail_connection.quit()
#this should be completed by importing all exceptions and using some block of code which handles exception_handling so if there is an error occurs,the server is not down on our end.
