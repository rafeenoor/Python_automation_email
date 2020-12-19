import smtplib # Simple Mail Transfer Protocol
server = smtplib.SMTP('smtp.gmail.com', 587) #creating server
server.starttls() #telling server that this is secure u can turst
server.login('Email','Password'); #You need to provide your login email and Password
server.sendmail('Your Email',
                'Receiver email',
                'message');

# The code wont work u have to mange ur google account and
# go to security and select  Less secure app access and turn it on!!