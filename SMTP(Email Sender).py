import smtplib

passowrd = 'kkegxnpobrgcotwv'
my_email = 'example1@gmail.com'
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=passowrd)
    connection.sendmail(
        from_addr='example1@gmail.com',
        to_addrs='example2@gmail.com',
        msg='subject:Flight Notification\n\n hello'
    )


