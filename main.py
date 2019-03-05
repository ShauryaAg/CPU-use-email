import smtplib, ssl, psutil

senderEmail = "sender@gmail.com" #put in your own email address
senderPass = input("Enter Password: ") #Enter your password
receiverEmail = "reciever@example.com" #change this to receiver's email

cpu_use_threshold = 50 #percent after which we want to send the email
interval = 1000 #interval in seconds

while True:
    cpu_per_usage = psutil.cpu_percent(interval=interval)


    port=465
    context = ssl.create_default_context()


    #Next, log in to the server
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(senderEmail, senderPass)
        server.ehlo()


        #Message to be sent
        msg = "Your CPU usage is more than" + str(cpu_use_threshold)


        if (cpu_per_usage > cpu_use_threshold):
            server.sendmail(senderEmail, receiverEmail, msg)
