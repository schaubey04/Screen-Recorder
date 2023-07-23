from tkinter import *
import pyscreenrec

shivam=Tk()
shivam.title("Screen Recorder")
shivam.geometry("400x600")
shivam.resizable(False,False)
shivam.configure(bg="white")

def start_rec():
    file=filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()
def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()
rec=pyscreenrec.ScreenRecorder()

#icon
image_icon=PhotoImage(file="icon.png")
shivam.iconphoto(False,image_icon)

#background image

image1=PhotoImage(file="yellow.png")
Label(shivam,image=image1,bg="white").place(x=-2,y=35)

image2=PhotoImage(file="blue.png")
Label(shivam,image=image2,bg="white").place(x=223,y=200)

#heading

lbl=Label(shivam,text="Screen Recorder",bg="#fff",font=("arial 15 bold"))
lbl.pack(pady=20)

image3=PhotoImage(file="recording.png")
Label(shivam,image=image3,bd=0).pack(pady=30)


#entry
filename=StringVar()
entry=Entry(shivam,textvariable=filename,width=18,font=("arial 15"))
entry.place(x=100,y=350)
filename.set("ShivamRecordingGUI1")

#buttons

start=Button(shivam,text="Start",font="arial 20",bd=0,command=start_rec)
start.place(x=140,y=250)

image4=PhotoImage(file="pause.png")
pause=Button(shivam,image=image4,bd=0,bg="#fff",command=pause_rec)
pause.place(x=50,y=450)

image5=PhotoImage(file="resume.png")
resume=Button(shivam,image=image5,bd=0,bg="#fff",command=resume_rec)
resume.place(x=150,y=450)

image6=PhotoImage(file="stop.png")
stop=Button(shivam,image=image6,bd=0,bg="#fff",command=stop_rec)
stop.place(x=250,y=450)




shivam.mainloop()