import tkinter

def edit_content():
    text=textfield.get('1.0','end-1c')
    for i in range(0,len(text)):
        if i+1<=len(text):

            if text[i]=="<" and text[i+1]=='d' or text[i]=='<' and text[i+1]=="/" and text[i+2]=='d' and i+2<=len(text):



                while True:

                    if text[i]=='>':

                        text=text[:i]+text[i+1:]

                        break
                    else:

                        text = text[:i] + text[i + 1:]




    
    textfield.delete('1.0',tkinter.END)
    textfield.insert(tkinter.END,text)









window=tkinter.Tk()
window.title("Content Editor Software")
tkinter.Label(window,text='Paste above your text to format', justify=tkinter.LEFT,padx = 10).pack()
scroll=tkinter.Scrollbar(window)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
textfield=tkinter.Text(window,height=2,width=30)
textfield.pack(side=tkinter.LEFT,fill=tkinter.Y)
scroll.config(command=textfield.yview)
textfield.config(yscrollcommand=scroll.set)
button=tkinter.Button(window,text='Lets Try!',command=edit_content)
button.pack()
label=tkinter.Label(window,text='Developed by Memento Code', justify=tkinter.LEFT,padx=10)
label.pack()
window.maxsize(500,500)
window.minsize(300,300)
window.mainloop()