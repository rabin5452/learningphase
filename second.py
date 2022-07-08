from cProfile import label
from tkinter import*

from matplotlib.pyplot import text
root=Tk(className='CTP')
root.geometry('500x500')
s=str()
def submit(text1):
    if text1=='=' or text1=='/' or text1=='*' or text1=='-' or text1=='+': 
        
        
    global s
    s=s+text1
    entryall=Label(text=s).grid(column=5,row=5)


button9=Button(root,text='9',width=5,border=5,command=(lambda:submit('9')))
button9.grid(column=0,row=2)
button8=Button(root,text='8',width=5,border=5,command=(lambda:submit('8')))
button8.grid(column=1,row=2)
button7=Button(root,text='7',width=5,border=5,command=(lambda:submit('7')))
button7.grid(column=2,row=2)
button6=Button(root,text='6',width=5,border=5,command=(lambda:submit('6')))
button6.grid(column=0,row=3)
button5=Button(root,text='5',width=5,border=5,command=(lambda:submit('5')))
button5.grid(column=1,row=3)
button4=Button(root,text='4',width=5,border=5,command=(lambda:submit('4')))
button4.grid(column=2,row=3)
button3=Button(root,text='3',width=5,border=5,command=(lambda:submit('3')))
button3.grid(column=0,row=4)
button2=Button(root,text='2',width=5,border=5,command=(lambda:submit('2')))
button2.grid(column=1,row=4)
button1=Button(root,text='1',width=5,border=5,command=(lambda:submit('1')))
button1.grid(column=2,row=4)
button0=Button(root,text='0',width=5,border=5,command=(lambda:submit('0')))
button0.grid(column=1,row=5)
buttonplus=Button(root,text='+',width=5,border=5).grid(column=2,row=5)
buttonsub=Button(root,text='-',width=5,border=5).grid(column=0,row=5)
buttonequal=Button(root,text='=',width=5,border=5).grid(column=0,row=6)
buttondiv=Button(root,text='/',width=5,border=5).grid(column=1,row=6)
buttonmul=Button(root,text='*',width=5,border=5).grid(column=2,row=6)
root.mainloop()