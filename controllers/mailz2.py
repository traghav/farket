from gluon.tools import Mail
mail = Mail()
mail.settings.server = 'smtp.gmail.com:587' 
mail.settings.sender = 'farketco@gmail.com'
mail.settings.login = 'farketco:biglebaowski'
def index():
	for x in xrange(1,10):
		mail.send('raghav.toshniwal@gmail.com',str(x),"Autogenerated I swear.")
	
	return "Great Success na?!"