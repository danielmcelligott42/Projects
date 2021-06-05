from tkinter import *
from time import *
import random

root=Tk()
frame=Frame(root)
can = Canvas(root, width=400, height=400,bg="black")
can.pack(side=TOP)

textlab = StringVar()
class Counter(object):
    def __init__(self):
        self._counter = 0

    def getCounter(self):
        return self._counter

    def setCounter(self):
        raise NotImplementedError("Not implemented")

    def increment(self):
        self._counter = self._counter + 1

    counter = property(getCounter)

def addtocounter(event):
    counter.increment()
    global counter2
    counter2 = counter2 + 1







def start():
    global t1
    t1 = time()
    can.delete("shape")
    xpos = random.randint(1, 360) #360 instead of 400 so that all of the square will fit in canvas
    ypos = random.randint(1, 360)
    can.create_polygon(xpos, ypos, xpos+40, ypos, xpos+40, ypos+40, xpos, ypos+40,fill="pink", tags="shape")
    can.tag_bind("shape", "<Button-1>", lambda x: combination())


def getTime():
    t2=time()
    tdif=t2-t1
    ttotal=[]
    ttotal.append(tdif)
    if tdif<2:
        addtocounter(1)
        if counter2%10==0:
            remainder=counter2//10
            n=remainder*10
            diff="Congrats your score is now " +str(n)
            textlab.set(diff)


        else:
            diff = "That took " + str(t2 - t1) + " seconds" + "\n" + "Your score is now " + str(counter2)
            textlab.set(diff)

def randColour():
    clist=["red","blue","orange","pink","yellow","purple","brown","gray","olive","hotpink"]
    global col
    col=random.choice(clist)
    can.itemconfig("shape",fill=col)
def close():
    root.bind("<Return>", lambda e: root.destroy())


def combination():
    getTime()
    start()
    close()
def endGame():
    t3=time()
    t=t3-t4
    global counter2
    if counter2!=0:

        avg=t/counter2
        mystring="Thanks for playing" +"\n" +"Your total time was " +str(t) +"\n" +"Your score was " +str(counter2) +"\n" \
                 +"Your average time per click was " +str(avg) +"\n" +"Press enter to exit game"

        textlab.set(mystring)

        counter2=0
    else:
        errormsg="Your score is zero"
        textlab.set(errormsg)



counter=Counter()
global counter2
counter2=0


but1 = Button(frame, text="Start", command=start)
but1.grid(row=1, column=1)

but2=Button(frame,text="Change colour",command=randColour)
but2.grid(row=1,column=2)

but3=Button(frame,text="Get results",command=endGame)
but3.grid(row=1,column=3)


lab=Label(root,textvariable=textlab)
lab.pack()

t4=time()


frame.pack(side=BOTTOM)
root.mainloop()