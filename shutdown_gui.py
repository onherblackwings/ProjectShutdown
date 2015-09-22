from Tkinter import *
import tkMessageBox
import Tkinter as tk
import subprocess

def shutdown_button_click():
    
    if len(entry1.get())== 0 and len(entry2.get())==0:
            tkMessageBox.showinfo("No Entry Alert!", "Please Enter Data!")

    else:
        hours=int(entry1.get())
        minutes=int(entry2.get())
        if hours<0:
            tkMessageBox.showinfo("You are not Brett Easton Ellis.", "Please do not enter a value Less Than Zero.")

        elif minutes>59 or minutes<0:
            tkMessageBox.showinfo("There is no Negative Time!","Please enter value ranging from 0 to 59 only.")

        else:
            
            mins=hours*60
            seconds=minutes*60
            total_seconds=(mins*60)+seconds
            total_seconds=str(total_seconds)
            print "Shutdown in: "+str(hours)+" hours "+str(minutes)+" minutes."
            tkMessageBox.showinfo("SHUTDOWN INITIATED!","Shutdown in: "+str(hours)+" hour(s) "+str(minutes)+" minute(s).")   
            subprocess.call(["shutdown.exe", "-s", "-t", total_seconds])
            

def restart_button_click():
     if len(entry1.get())== 0 and len(entry2.get())==0:
            tkMessageBox.showinfo("No Entry Alert!", "Please Enter Data!")

     else:
         hours=int(entry1.get())
         minutes=int(entry2.get())
         if hours<0:
             tkMessageBox.showinfo("You are not Brett Easton Ellis.", "Please do not enter a value Less Than Zero.")

         elif minutes>59 or minutes<0:
             tkMessageBox.showinfo("There is no Negative Time!","Please enter value ranging from 0 to 59 only.")

         else:
             
             mins=hours*60
             seconds=minutes*60
             total_seconds=(mins*60)+seconds
             total_seconds=str(total_seconds)
             print "Restart in: "+str(hours)+" hours "+str(minutes)+" minutes."
             tkMessageBox.showinfo("RESTART INITIATED!","Your computer will restart in: "+str(hours)+" hour(s) "+str(minutes)+" minute(s).")   
             subprocess.call(["shutdown.exe", "-r", "-t", total_seconds])
             
    
def hibernate_button_click():
    print "Hibernating Now!"
    subprocess.call(["shutdown.exe", "-h"])
    #tkMessageBox.showinfo("Hibernating Now!")



def abort_button_click():
    print "Shutdown/Restart Aborted!"
    subprocess.call(["shutdown.exe","-a"])
    tkMessageBox.showinfo("ABORT INITIATED!","Shutdown/Restart Aborted!")

root=Tk()
root.title("Shutdown")
root.resizable(False,False)


entry1=Entry(root, width=25)
entry2=Entry(root, width=25)
entry1.insert(10,0)
entry2.insert(10,0)
label1=Label(root, text="Hours").grid(row=0, column=0)
entry1.grid(row=1, column=0)

label2=Label(root, text="Minutes").grid(row=2, column=0)
entry2.grid(row=3, column=0)

Button(root, text="Shutdown", width=25, command=shutdown_button_click).grid(row=4,column=0)
Button(root, text="Restart", width=25, command=restart_button_click).grid(row=5,column=0)
Button(root, text="Hibernate", width=25, command=hibernate_button_click).grid(row=6,column=0)
Button(root, text="Abort Process", width=25, command=abort_button_click).grid(row=7,column=0)


root.mainloop()

