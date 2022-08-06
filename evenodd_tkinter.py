from tkinter import *
window= Tk()
window.geometry("750x250")
user_label= Label(text='Enter a num is it odd or even? ')
user_input= Entry(window)
user_input.pack()
user_label.pack()
user_input.pack()
print(type(user_input.get()))
track_clicks = 0

def even():
    global track_clicks
    global output
    track_clicks+=1
    n=user_input.get()
    if track_clicks > 1 and output.winfo_exists() == 1:
        output.destroy()
        track_clicks += 1
    if str.isnumeric(n) == True:
        if (int(n)) % 2 == 0:
            output = Label(window, text='Even')
            output.pack()
        elif (int(n)) == 0:
            output = Label(window, text='It is neither even nor odd')
            output.pack()
        elif (int(n)) %2 !=0:
            output = Label(window, text='Odd')
            output.pack()
    else:
        if n.find('.')==True:
            output= Label(window,text='Decimals are not even nor odd numbers because they are not whole numbers')
            output.pack()
        else:
            output = Label(window,text='Invalid input, please enter an integer')
            output.pack()
button= Button(window,text='Enter',command=even,fg='white',bg='black')
button.pack()
window.mainloop()











