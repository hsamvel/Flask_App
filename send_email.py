def s_mail(tb, by, img, img_file):
    import smtplib
    import os
    from email.message import EmailMessage
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    for el in tb:
        msg = MIMEMultipart()
        # msg = EmailMessage()
        mess = by + " (" + img + ")"
        message = MIMEText(mess)
        msg.attach(message)
        with open("C:\\Users\\Neo Graph Games\\Desktop\\Flask Web App Tutorial\\" + img_file, "rb") as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=img_file)
        msg.attach(image)
        # msg.set_content(message)
        msg['Subject'] = 'From rendering website'
        msg['From'] = el
        msg['To'] = el

        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("renderingwebsite11@gmail.com","hbomzrcnfccleifh" )#"dvzmvvvvfrpdglav"(mygmail) #hbomzrcnfccleifh(websitegmail)
        server.send_message(msg)
        server.quit()

