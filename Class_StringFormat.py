import datetime 

class MessageUser():
  User_Details = []
  Messages = []
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
          self.Messages.append(formatted_message)  
        return self.Messages
      else:
          return []
        
      
obj = MessageUser()
obj.add_user("Pritom", 123.32, email='hello@shorboshesh.com') 
obj.add_user("jon Snow", 94.23)
obj.add_user("Sean", 93.23)
obj.add_user("Emilee", 193.23)
obj.add_user("Marie", 13.23)
obj.get_details()

print(obj.make_message())
      
    
      
    
    
