import smtplib
from tkinter import messagebox

def send_msg(sender_email, sender_password, to, subject, message):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            # Extended Hello - identifying ourselves(client) to mail server
            smtp.ehlo()

            # Start Transport Layer Security - encrypt your traffic
            smtp.starttls()
            
            smtp.ehlo()
                
            #login your account
            smtp.login(sender_email, sender_password)
                     
            msg = f'Subject: {subject}\n\n{message}'

            smtp.sendmail(sender_email, to, msg)

    except Exception as e:
        messagebox.showinfo("Something went wrong",f"Error: {e}")

    else:
        messagebox.showinfo("","Mail sent successfully !")
