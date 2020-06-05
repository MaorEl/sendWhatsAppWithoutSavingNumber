from tkinter import *
import webbrowser

url_prefix = 'https://web.whatsapp.com/send?phone=972'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def change_format_of_phone(phone_number):
    return ''.join(phone_number[1:].split('-'))


def open_chrome(phone_number, event=None):
    phone_number = change_format_of_phone(phone_number)
    url = url_prefix + phone_number
    webbrowser.get(chrome_path).open(url)


def main():
    window = Tk()
    window.title("Send WhatsApp Msg without saving number")
    lbl = Label(window, text="Enter Phone number:", font=("Arial Bold", 30))
    lbl.grid(column=1, row=0)
    lbl_empty1 = Label(window, text="", font=("Arial Bold", 30))
    lbl_empty1.grid(column=1,row=1)
    text_phone_number = StringVar()
    text_phone_number_entry = Entry(window,width=20, textvariable=text_phone_number, font=("Arial Bold", 30))
    text_phone_number_entry.bind('<Button-3>',rClicker, add='')

    text_phone_number_entry.grid(column=1,row=2)
    lbl_empty2 = Label(window, text="", font=("Arial Bold", 30))
    lbl_empty2.grid(column=1,row=3)
    btn = Button(window, text="Open WhatsApp Web", bg="green", command=lambda: open_chrome(text_phone_number.get()),
                 font=("Arial Bold", 30))
    window.bind("<Return>", lambda x: open_chrome(text_phone_number.get()))

    btn.grid(column=1, row=4)
    window.mainloop()


def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()

        nclst=[
               (' Cut', lambda e=e: rClick_Cut(e)),
               (' Copy', lambda e=e: rClick_Copy(e)),
               (' Paste', lambda e=e: rClick_Paste(e)),
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print (' - rClick menu, something wrong')
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print (' - rClickbinder, something wrong')
        pass


main()
