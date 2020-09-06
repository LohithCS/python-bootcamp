import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()

smtp_object.starttls()

email = input("enter your email id: ")
password = getpass.getpass("enter your password here: (App password for gmail)")
smtp_object.login(email,password)

from_address = email
to_address = input("enter the email id of recipient")
subject = input("enter the subject line")
message = input("enter your message here ")
msg = "Subject: " + subject + "\n" + message
print(msg)
smtp_object.sendmail(from_address,to_address,msg)
