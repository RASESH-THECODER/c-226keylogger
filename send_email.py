import smtplib, ssl

from django.dispatch import receiver

def sendemail(message):
	smtp_server="smtp.gmail.com"
	port=587
	sender_email="gandhiraseshk30@gmail.com"
	password="raseshk30"
	receiver_email="sangeetachauhan13@gmail.com"

	context=ssl.create_default_context

	try:
		server=smtplib.SMTP(smtp_server,port)
		server.starttls(context=context)
		server.login(sender_email,password)
		server,sendemail(sender_email,receiver_email,message)
	

	except Exception as e:
		print(e)
	finally:
		server.quit()

