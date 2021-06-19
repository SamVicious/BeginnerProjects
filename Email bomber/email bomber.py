import smtplib
emails = open('emailpass.txt', 'r')
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
import time
for email in emails:
	conn.login(email.split(':')[0],email.split(':')[1])
	for i in range(3):
		conn.sendmail(email.split(':')[0], 'sam.aquarkorius8@gmail.com', 'Subject : Hey, Dear victim\n\nThis email is sent from a email bomber script. Don\'t worry this is not serious\n\n-Sam')
		time.sleep(5)
