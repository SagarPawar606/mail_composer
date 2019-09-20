import tkinter as tk
from tkinter import messagebox
from sendmail import send_msg
import requests

def Start(master):
    frame = tk.Frame(master)
    tk.Label(frame, text="Enter your Gmail address :", padx=10, pady=5).grid(row=0, column=0, sticky='w')
    tk.Label(frame, text="Enter your password :", padx=10, pady=5).grid(row=1, column=0, sticky='w')
    mail = tk.Entry(frame)
    password = tk.Entry(frame, show="*")
    startbtn = tk.Button(frame, text="Start", command = lambda:get_credentials(mail, password, master))
    closebtn = tk.Button(frame, text="Cancel", command=master.destroy)

    frame.pack()
    mail.grid(row=0, column=1)
    password.grid(row=1, column=1)
    startbtn.grid(row=2, column=0, sticky='e', padx=5)
    closebtn.grid(row=2, column=1, sticky='w', padx=5)
    
def get_credentials(mail, password, master):
    
    mailid = mail.get()
    pwd = password.get()
    # if len(mailid)==0 or len(pwd)==0 or '@gmail.com' not in mailid:
    #     messagebox.showwarning("Warning","Please Enter valid input !")
    # else:
    logindict.update({"email":mailid, "password":pwd})
    master.destroy()
    main_window()
        
     
    
def main_window():
    new_root = tk.Tk()
    #top_frames
    top_frame = tk.Frame(new_root)
    tk.Label(top_frame, text="GmailComposer", font=("Arial Black", 20)).pack()

    #indicators_frame
    indicatorframe = tk.Frame(new_root)
    internt_conn = check_internet()

    internet_conn_label = tk.Label(indicatorframe, font=("Arial Black", 15))
    internet_conn_label.pack(side='top')
    if internt_conn:
        internet_conn_label.config(text="✔    Internet Available", fg="green")
    else:
        internet_conn_label.config(text="✗  Check Your Internet Connection", fg="red")
    
    
    #content_Frame
    frame = tk.Frame(new_root)
    li = logindict['email'].split('@')
    username = li[0]
    tk.Label(frame, text="Hello, {} !".format(username), font=("Arial Black", 15)).grid(row=0, column=0, sticky='w', padx=10, pady=8)
    tk.Label(frame, text="To :", font=("Arial", 15)).grid(row=1, column=0, sticky='w', padx=10, pady=8)
    tk.Label(frame, text="Subject :", font=("Arial", 15)).grid(row=2, column=0, sticky='w', padx=10, pady=8)
    tk.Label(frame, text="Message :", font=("Arial", 15)).grid(row=3, column=0, sticky='w', padx=10, pady=8)
    
    to = tk.Entry(frame, width=50)
    subject = tk.Entry(frame, width=50)
    message = tk.Text(frame, width=70, height=10)
    sendbtn = tk.Button(frame, text="Send", command = lambda:grab_details(to, subject, message))
    cancel_btn = tk.Button(frame, text="Cancel", command = new_root.destroy)

    to.grid(row=1, column=1, sticky='w', padx=10, pady=8)
    subject.grid(row=2, column=1, sticky='w', padx=10, pady=8)
    message.grid(row=3, column=1, sticky='w', padx=10, pady=8)
    sendbtn.grid(row=4, column=1, sticky='w', padx=10, pady=8, ipadx=10)
    cancel_btn.grid(row=4, column=2, sticky='w', padx=10, pady=8, ipadx=10)

    #frames_pack
    top_frame.pack()
    frame.pack(side='left')
    indicatorframe.pack(fill='x', expand=True, side='left')

    new_root.geometry('1200x450')
    new_root.resizable(width=False, height=False)
    new_root.mainloop()
    
def grab_details(to, subject, message):
    sender_email = logindict['email']
    sender_password = logindict['password']
    to = to.get().strip()
    subject = subject.get().strip()
    message = message.get('1.0', 'end-1c')
    if not('@' or '.com') in to:
        messagebox.showerror("","Please Enter valid email address !")
        return
    yesno = True
    if len(subject)==0 or len(message)==0:
        yesno = messagebox.askyesno("","Blank subject or message ! Still want to proceed?")
    if yesno is True:
        send_msg(sender_email, sender_password, to, subject, message)
    else:
        return    

def check_internet():
    #checks whether internet conncetion is available or not
    try:
        _ = requests.get('http://www.google.com/', timeout=2)
        return True
    except requests.ConnectionError:
        print("No internet connection")
    return False
        
    
def main():
    Start(root)
    
    
logindict = {}
root = tk.Tk()
root.title("GmailComposer")
root.geometry('300x100')
root.resizable(width=False, height=False)

main()

root.mainloop()
