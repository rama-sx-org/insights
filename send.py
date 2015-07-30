import sys
import chilkat

#  The mailman object is used for sending and receiving email.
mailman = chilkat.CkMailMan()

#  Any string argument automatically begins the 30-day trial.
success = mailman.UnlockComponent("30-day trial")
if (success != True):
    print mailman.lastErrorText()
    sys.exit()

#  Set the SMTP server.
mailman.put_SmtpHost("smtp.chilkatsoft.com")

#  Set the SMTP login/password (if required)
mailman.put_SmtpUsername("myUsername")
mailman.put_SmtpPassword("myPassword")

#  Create a new email object
email = chilkat.CkEmail()

email.put_Subject("Bye Bye Old DVR")
email.put_Body("Hassle free upgrades to QuantumTV")
email.put_From("verizon <support@chilkatsoft.com>")
#  Use the 10-digit phone number and SMS gateway domain here:
email.AddTo("Satheeth","7680986709@txt.att.net")

#  Call SendEmail to connect to the SMTP server and send.
#  The connection (i.e. session) to the SMTP server remains
#  open so that subsequent SendEmail calls may use the
#  same connection.
success = mailman.SendEmail(email)
if (success != True):
    print mailman.lastErrorText()
    sys.exit()

#  Some SMTP servers do not actually send the email until
#  the connection is closed.  In these cases, it is necessary to
#  call CloseSmtpConnection for the mail to be  sent.
#  Most SMTP servers send the email immediately, and it is
#  not required to close the connection.  We'll close it here
#  for the example:
success = mailman.CloseSmtpConnection()
if (success != True):
    print mailman.lastErrorText()

print "Mail Sent"
