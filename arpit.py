print('hi i am arpit')
a = 23
print(type(a))
ripta = 'siloy'
print(type(ripta))
food = ['burger','pizza','frenchfries','maaza']
print(type(food))
from tkinter import *
root = Tk()
root.title('addition')
root.geometry('400x200')
show_result = Label(root)
def add():
    result =439+384
    show_result['text']=result
    
btn = Button(root,text='add',command =add)
btn.pack()

show_result.pack()
root.mainloop()