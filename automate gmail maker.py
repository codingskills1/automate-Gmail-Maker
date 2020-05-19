from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image 
import tkinter as tk 
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time 

# Window Infomation 
window = Tk()
window.title("Gmail Maker")
window.geometry("700x400")
window.resizable(width = None, height = None)

# Google Picture

canvas = Canvas(window, width = 70, height = 70)
canvas.place(x = 20, y = 30)
img = ImageTk.PhotoImage(Image.open("gmail.png")) 
canvas.create_image(0, 0, anchor=NW, image=img) 

# Labels

firstname_lbl = Label(window, text = "Name", font=("Arial Bold", 10))
firstname_lbl.place(x = 10, y = 130)

lastname_lbl = Label(window, text = "LastName")
lastname_lbl.place(x = 300, y = 150)

user_name_lbl = Label(window, text = "Username", font=("Arial Bold", 10))
user_name_lbl.place(x = 10, y = 190)

pass_lbl = Label(window, text = "Password", font=("Arial Bold", 10))
pass_lbl.place(x = 10, y = 240)

confirm_lbl = Label(window, text = "Confirm")
confirm_lbl.place(x = 300, y = 260)

under_lbl = Label(window, text = "First Name")
under_lbl.place(x = 100, y = 150)

under_pass = Label(window, text = "Password")
under_pass.place(x = 100, y = 260)

gmail_label = tk.Label(window, text = "Gmail Maker", font=("Arial Bold", 20), fg = "black")
gmail_label.place(x = 100, y = 30)

# Entries 
firstname_entry = Entry(window, width = 25)
firstname_entry.place(x = 100, y = 130)
firstname_entry.focus()

lastname_entry = Entry(window, width = 25)
lastname_entry.place(x = 300 , y = 130)

username_entry = Entry(window, width = 50)
username_entry.place(x = 100, y = 190)

pass_entry = Entry(window, show = "*" , width = 25)
pass_entry.place(x = 100 , y = 240)

confirm_entry = Entry(window, show = "*" , width = 25)
confirm_entry.place(x = 300, y = 240)

def show_pass():
	pass_entry = Entry(window, show = "" , width = 25)
	pass_entry.place(x = 100 , y = 240)
	confirm_entry = Entry(window, show = "" , width = 25)
	confirm_entry.place(x = 300, y = 240)

def hide_pass():
	pass_entry = Entry(window, show = "*" , width = 25)
	pass_entry.place(x = 100 , y = 240)
	confirm_entry = Entry(window, show = "*" , width = 25)
	confirm_entry.place(x = 300, y = 240)


# Button 
btn_pass = Button(window, text = "Show", command = show_pass)
btn_pass.place(x = 470, y = 240)

btn_hide = Button(window, text = "Hide", command = hide_pass)
btn_hide.place(x = 560, y = 240)
# Validation 
def clicked():
	# First Name Validation
	if firstname_entry.get() == "":
		messagebox.showerror("error","Enter Your Name")
		btn = tk.Button(window, text = "Next", fg = "blue", command = clicked)
		btn.place(x = 400, y = 280)

	elif len(firstname_entry.get()) < 2:
		messagebox.showerror("error","Enter Valid Name")

	elif len(firstname_entry.get()) > 20:
		messagebox.showerror("error","Your Name Is Not Valid")

	# LastName Validation
	if lastname_entry.get() == "":
		messagebox.showerror("error", "Enter Your LastName")

	elif len(lastname_entry.get()) < 2:
		messagebox.showerror("error", "Enter Valid LastName")

	elif len(lastname_entry.get()) > 20:
		messagebox.showerror("error", "Your LastName Is Too Long")

	# UserName Validation 
	if username_entry.get() == "":
		messagebox.showerror("error", "Enter Your UserName")

	elif len(username_entry.get()) < 12:
		messagebox.showerror("error", "Enter Valid UserName")

	elif len(username_entry.get()) > 40:
		messagebox.showerror("error", "Your UserName Is Not Valid")

	elif "@gmail.com" not in username_entry.get() and "@email.com" not in username_entry.get():
		messagebox.showerror("error", "Enter Valid UserName ")

	# Password Validation
	if pass_entry.get() == "":
		messagebox.showerror("error", "Enter Your Password")

	elif len(pass_entry.get()) < 8:
		messagebox.showerror("error", "Your Password at least should be 8")

	elif len(pass_entry.get()) > 100:
		messagebox.showerror("error", "Maximum password characters is 100")

	# Confirm Password Validation 
	if pass_entry.get() != confirm_entry.get():
		messagebox.showerror("error", "Password's doesn't mach")

	if confirm_entry.get() == "":
		messagebox.showerror("error", "Enter Your Password Again(Confirm Your Password)")
	# Main 
	else:
		if firstname_entry.get() != "" and lastname_entry.get() != "" and username_entry.get() != "" and pass_entry.get() != "" and confirm_entry.get() != "" and len(firstname_entry.get()) > 2 and len(username_entry.get()) > 12 and len(pass_entry.get()) > 8 and len(username_entry.get()) < 30 and len(firstname_entry.get()) < 20 and len(pass_entry.get()) < 100:
			messagebox.showinfo("MohammadHossein says:", "Your Account Have Been Created Successfully wait for selenium to enter all of the information to gmail.com")
			
			driver = webdriver.Chrome()

			driver.get("https://accounts.google.com/SignUp")

			elem = driver.find_element_by_name("firstName")

			elem_lastname = driver.find_element_by_name("lastName")

			elem_user = driver.find_element_by_name("Username")

			elem_password = driver.find_element_by_name("Passwd")

			elem_confirm = driver.find_element_by_name("ConfirmPasswd")


			elem.clear()

			elem_lastname.clear()

			elem_user.clear()

			elem_password.clear()

			elem_confirm.clear()

			elem.send_keys(firstname_entry.get())
			elem_lastname.send_keys(lastname_entry.get())
			elem_user.send_keys(username_entry.get())
			elem_password.send_keys(pass_entry.get())
			elem_confirm.send_keys(confirm_entry.get())
			elem_confirm.send_keys(Keys.RETURN)





# Button 
btn = tk.Button(window, text = "Next", fg = "blue", command = clicked)

btn.place(x = 400, y = 280)





window.mainloop()







