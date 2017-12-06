import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host = "smtp.gmail.com"
port = 587
username = "testmail3018"
password = "testing3018"
from_email = username
to_mail_list = ["testmail3018@gmail.com", "rasel_cse07@gmail.com"]#to_email always have to be a list
#not using this list anymore in this programme



class MessageUser():
  User_Details = []
  Messages = []
  Email_Message = []
  base_message = """Hi {name}!
  Thank you for the purchase on {date}.
  We hope you are exicted about using it. Just as a
  reminder the purcase total was ${total}.
  Have a great time!

  from Pritom_Mazhi
  """

  def add_user(self, name, amount, email=None):
    name = name[0].upper() + name[1:].lower() #Capitalizing the first letter of all names - formatted name
    amount = "%.2f" %(amount) #formatted amount
    detail = {
      "name" : name,
      "amount" : amount,
    }
    today = datetime.date.today()
    date_text = '{tday.day}/{tday.month}/{tday.year}'.format(tday=today) #formatted date
    detail["date"] = date_text
    if email is not None:
      detail["email"] = email
    self.User_Details.append(detail)

  def get_details(self):
      return self.User_Details

  def make_message(self):
      if len(self.User_Details) > 0:
        for detail in self.get_details():  #for detail in self.User_Details
          name = detail["name"]
          amount = detail["amount"]
          date = detail["date"]
          #email = detail["email"]
          message = self.base_message
          formatted_message = message.format(
            name = name,
            total = amount,
            date = date
            )
          user_email = detail.get("email")
          if user_email:
              user_data = {
              "email" : user_email,
              "message" : formatted_message
              }
              self.Email_Message.append(user_data)
          else:
              self.Messages.append(formatted_message)

        return self.Messages
      else:
          return []

  def send_email(self):
      self.make_message()
      if len(self.Email_Message) > 0:
          for item in self.Email_Message:
              user_email = item["email"]
              user_message = item["message"]
              try:
                  gmail_connection = smtplib.SMTP(host, port)
                  gmail_connection.ehlo()
                  gmail_connection.starttls()
                  gmail_connection.login(username, password)

                  the_message = MIMEMultipart("alternative")
                  the_message["Subject"] = "billing messages or messages like that"
                  the_message["From"] = from_email
                  the_message["To"] = user_email

                  part1 = MIMEText(user_message, 'plain')
                  the_message.attach(part1)

                  gmail_connection.sendmail(from_email, [user_email], the_message.as_string())
                  #to_email always have to be a list
                  gmail_connection.quit()

              except smtplib.SMTPException:
                  print("error sending mails or messages")
                  #return False - could be used here instead of using below but while iterating this wouldn't be good
          return True
      return False







obj = MessageUser()
obj.add_user("Pritom", 123.32, email='testmail3018@gmail.com')
obj.add_user("jon Snow", 94.23, email='testmail3018@gmail.com')
obj.add_user("Sean", 93.23, email='testmail3018@gmail.com')
obj.add_user("Emilee", 193.23, email='testmail3018@gmail.com')
obj.add_user("Marie", 13.23, email='testmail3018@gmail.com')
obj.get_details()

obj.send_email()
