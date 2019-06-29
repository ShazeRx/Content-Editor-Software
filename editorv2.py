import tkinter
import re


def delete_div_class():
    text = textfield.get('1.0', 'end-1c')
    text  = re.sub(r"<div.*?>",'',text,flags=re.IGNORECASE)
    text  = re.sub(r"<\s*/div.*?>",'',text,flags=re.IGNORECASE)
    text  = re.sub(r"class=\"([^\"]*)\"",'',text,flags=re.IGNORECASE)





    textfield.delete('1.0', tkinter.END)
    textfield.insert(tkinter.END, text)
def delete_empty_spaces():
    text = textfield.get('1.0', 'end-1c')

    text = re.sub(r"<br />", '', text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*p.*>[^/w]</p\s*>", '', text, flags=re.IGNORECASE)
    textfield.delete('1.0', tkinter.END)
    textfield.insert(tkinter.END, text)
def sentence_case():
    text = textfield.get('1.0', 'end-1c')
    textfield.delete('1.0', tkinter.END)
    textfield.insert(tkinter.END,text.capitalize())
def make_titles():
    text = textfield.get('1.0', 'end-1c')
    text = re.sub(r"<\s*p\s*>\s*<\s*strong\s*>", '<h2>', text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*/strong\s*><\s*/p\s*>\s*", '</h2>', text, flags=re.IGNORECASE)
    textfield.delete('1.0', tkinter.END)
    textfield.insert(tkinter.END, text)


window = tkinter.Tk()
window.title("Content Editor Software")
tkinter.Label(window, text='Paste above your text to format', justify=tkinter.LEFT, padx=10).pack()
scroll = tkinter.Scrollbar(window)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
textfield = tkinter.Text(window, height=2, width=30)
textfield.pack(side=tkinter.LEFT, fill=tkinter.Y)
scroll.config(command=textfield.yview)
textfield.config(yscrollcommand=scroll.set)
button = tkinter.Button(window, text='Delete div/class', command=delete_div_class)
button.pack()
button = tkinter.Button(window, text='Delete empty spaces', command=delete_empty_spaces)
button.pack()
button = tkinter.Button(window, text='Sentence Case', command=sentence_case)
button.pack()
button = tkinter.Button(window, text='Make Titles', command=make_titles)
button.pack()
label = tkinter.Label(window, text='Developed by Memento Code', justify=tkinter.LEFT, padx=10)
label.pack()
window.maxsize(500, 500)
window.minsize(300, 300)
window.mainloop()