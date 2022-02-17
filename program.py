
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

password = 'aditi.2401'
def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

root = Tk()
root.title("Title")
root.geometry('600x600')

def raise_frame(frame): #function that allows to switch between two frames for implemnting different things
    frame.tkraise()


frame = Frame(root, relief='raised', borderwidth=2) #mainframe of page
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

copy_of_image = Image.open(r'C:\Users\arvin\Desktop\CSS\IA\lightblue.jpg')
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

firstpassword = StringVar()
choice = StringVar()
filenameencrypt = StringVar()
keynamencrypt = StringVar()
filenamedecrypt = StringVar()
keynamedecrypt = StringVar()
center_frame = Frame(frame, relief='raised',bg="grey",width=700,height=350)
#-------------------------functions---------------------------------------------#

def Encrypt():
    filename = filenameencrypt.get()
    print(filename)
    key = int(keynamencrypt.get())
    print("hello from the other side")
    path_to_folder= r'C:\Users\arvin\Desktop\CSS\IA'
    print(os.path.join(path_to_folder,filename))
    file = open(os.path.join(r'C:\Users\arvin\Desktop\CSS\IA',filename),"rb")
    data = file.read()
    file.close()
    data = bytearray(data)
    print(data)

    for index ,value in enumerate(data):
        
        data[index]=value^key

    file = open('corrupted-'+filename,'wb')
    file.write(data)

    file.close()
def Decrypt():
         filename = filenamedecrypt.get()
         key = int(keynamedecrypt.get())
         print("hello from the other side")
         path_to_folder= r'C:\Users\arvin\Desktop\CSS\IA'
         file = open(os.path.join(r'C:\Users\arvin\Desktop\CSS\IA',filename),"rb")
         print(os.path.join(path_to_folder,filename))
         data = file.read()
         file.close()
         data = bytearray(data)
         print(data)
        
         for index ,value in enumerate(data):
             data[index]=value^key
        
         file = open(filename,'wb')
         file.write(data)
         file.close()
def authenticate():
    firstpassword1 = firstpassword.get()
    if firstpassword1==password:
        mainframe = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(mainframe, text ="Entry Granted",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        proceedButton = Button(mainframe,text="Proceed!",bg="lightblue",fg="black",relief="raised",command=raise_frame(frame1))
        proceedButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
        proceedButton.place( anchor="n",relx=0.5,rely=0.8)

    else:
        deniedframe = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        deniedframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(deniedframe, text ="Entry Denied",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        tryButton = Button(deniedframe,text="Try Again ?",bg="lightblue",fg="black",relief="raised",command=lambda:raise_frame(center_frame))
        tryButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
        tryButton.place( anchor="n",relx=0.5,rely=0.8)


     


def startencryption():
    print("reached here ")
    choice1 = choice.get()
    print(type(choice1))
    if choice1=='1':
        print("if part ")
        mainframe1 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        mainframe1.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(mainframe1, text ="Entry Granted",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        proceedButton1 = Button(mainframe1,text="Proceed!",bg="lightblue",fg="black",relief="raised",command=raise_frame(frame2))
        proceedButton1.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
        proceedButton1.place( anchor="n",relx=0.5,rely=0.8)
    else:
        mainframe4 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
        mainframe4.place(relx=0.5, rely=0.5, anchor=CENTER)
        msg = Label(mainframe4, text ="Entry Granted",bg="lightskyblue",fg="black")
        msg.config(font=("Courier", 20))
        msg.place( anchor="n",relx=0.5,rely=0.2)
        proceedButton3 = Button(mainframe4,text="Proceed!",bg="lightblue",fg="black",relief="raised",command=raise_frame(frame4))
        proceedButton3.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
        proceedButton3.place( anchor="n",relx=0.5,rely=0.8)
        
        

def originalpic():
    print("reached here too ")
    
    
    
    print("if part ")
    # mainframe2 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
    # mainframe2.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    
    # proceedButton1 = Button(mainframe2,text="Proceed!",bg="lightblue",fg="black",relief="raised",command=raise_frame(frame3))
    # proceedButton1.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
    # proceedButton1.place( anchor="n",relx=0.5,rely=0.8)
    raise_frame(frame3)
   



        



#---------------------------------- page which gives user the choice to  encrypt or decrypt--------------------------#

frame1 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
msg = Label(frame1, text ="Enter 1 to Encrypt A file or 2 to Decrypt a File ",bg="lightskyblue",fg="black")
msg.config(font=("Courier", 20))
msg.place( anchor="n",relx=0.5,rely=0.2)
entry1 = Entry(frame1,bd=5,textvariable=choice) #entry box for name
entry1.place(anchor="n",relx=0.5,rely=0.4)
submit1 = Button(frame1,text="Submit!",bg="lightblue",fg="black",relief="raised",command=startencryption)
submit1.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submit1.place( anchor="n",relx=0.5,rely=0.6)
#-----------------------------------Main Page------------------------------------#
 #center frame for the functionalities
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
w = Label(center_frame, text ="Welcome to FileSecure System",bg="lightskyblue",fg="black")
w.config(font=("Courier", 20))
w.place( anchor="n",relx=0.5,rely=0.2)

w1 = Label(center_frame, text ="Enter The Password",bg="lightskyblue",fg="black")
w1.config(font=("Courier", 20))
w1.place( anchor="n",relx=0.5,rely=0.4)

entry1 = Entry(center_frame,bd=5,textvariable=firstpassword) #entry box for name
entry1.place(anchor="n",relx=0.5,rely=0.6)

submitButton = Button(center_frame,text="Submit!",bg="lightblue",fg="black",relief="raised",command=authenticate)
submitButton.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButton.place( anchor="n",relx=0.5,rely=0.8)


#--------------displaying original pic frame-------------------------------------#




#-------------decrypting file page------------------------------------------------#

frame4 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
frame4.place(relx=0.5, rely=0.5, anchor=CENTER)
msg = Label(frame4, text ="Decrypting File",bg="lightskyblue",fg="black")
msg.config(font=("Courier", 20))
msg.place( anchor="n",relx=0.5,rely=0.2)

w2 = Label(frame4, text ="Enter The Filename ",bg="lightskyblue",fg="black")
w2.config(font=("Courier", 20))
w2.place( anchor="n",relx=0.3,rely=0.4)

entry2 = Entry(frame4,bd=5,textvariable=filenamedecrypt) #entry box for name
entry2.place(anchor="n",relx=0.7,rely=0.4)

w3 = Label(frame4, text ="Enter The Key",bg="lightskyblue",fg="black")
w3.config(font=("Courier", 20))
w3.place( anchor="n",relx=0.3,rely=0.6)

entry3 = Entry(frame4,bd=5,textvariable=keynamedecrypt) #entry box for name
entry3.place(anchor="n",relx=0.7,rely=0.6)


submitButtonencrypt = Button(frame4,text="Submit!",bg="lightblue",fg="black",relief="raised",command = Decrypt)
submitButtonencrypt.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButtonencrypt.place( anchor="n",relx=0.5,rely=0.8)


#-------------------encrypting file page--------------------------------------------------------#

frame2 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
frame2.place(relx=0.5, rely=0.5, anchor=CENTER)
msg = Label(frame2, text ="Encrypting File",bg="lightskyblue",fg="black")
msg.config(font=("Courier", 20))
msg.place( anchor="n",relx=0.5,rely=0.2)

w2 = Label(frame2, text ="Enter The Filename ",bg="lightskyblue",fg="black")
w2.config(font=("Courier", 20))
w2.place( anchor="n",relx=0.3,rely=0.4)

entry2 = Entry(frame2,bd=5,textvariable=filenameencrypt) #entry box for name
entry2.place(anchor="n",relx=0.7,rely=0.4)

w3 = Label(frame2, text ="Enter The Key",bg="lightskyblue",fg="black")
w3.config(font=("Courier", 20))
w3.place( anchor="n",relx=0.3,rely=0.6)

entry3 = Entry(frame2,bd=5,textvariable=keynamencrypt) #entry box for name
entry3.place(anchor="n",relx=0.7,rely=0.6)


submitButtonencrypt = Button(frame2,text="Submit!",bg="lightblue",fg="black",relief="raised",command = Encrypt)
submitButtonencrypt.config(font=("Courier", 10)) #submit button on register page to submit data values after registering
submitButtonencrypt.place( anchor="n",relx=0.5,rely=0.8)

frame3 = Frame(frame, relief='raised',bg="grey",width=700,height=350)
frame3.place(relx=0.5, rely=0.5, anchor=CENTER)

image = Image.open(r"C:\Users\arvin\Desktop\CSS\IA\pic.jpg")
photo = ImageTk.PhotoImage(image.resize((196, 196)))

label = Label(frame3, image=photo, bg='green')

label.pack()
label.image = photo
label.pack()


#--------------------------------------------helper code--------------------------------------------------------#


        



# userpassword = 'user'
# print('Welcome to filesecure system!')
# passwordu = input('Enter the password ')
# flag=0
# if passwordu==password:
#     print('Entry Granted')
#     flag=1
# else:
#     print('Entry Denied.')
# if flag==1:
#     while True:
#         choice = int(input('Enter 1 to encrypt a file or 2 to decrypt the file '))
    
#         if choice==1:
#             filename = (input('Enter the filename '))
#             key = int(input('Enter the key '))
#             Encrypt(filename,key)
#         elif choice==2:
#             filename1= (input('Enter the filename '))
#             password1 = input('Enter the user password ')
            
#             key1 = int(input('Enter the key '))
#             if password1==userpassword:
#                 Decrypt(filename1,key1)
#             else:
#                 print('Access Denied ')
            
raise_frame(center_frame)
root.mainloop()
