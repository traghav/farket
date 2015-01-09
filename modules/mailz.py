from gluon.tools import Mail
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'farketco@gmail.com' 
mail.settings.login = 'farketco:biglebaowski'
def index(email,sub,message):
	mail.send(email,sub,message)