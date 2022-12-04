from tkinter.simpledialog import askstring
import qrcode
import os
from tkinter import *
from tkinter import messagebox
import threading
import sys


def create_qrcode(main_window, user_url):
    """
    This function creates a qrcode out of a user url site
    :param main_window: Tkinter object
    :param user_url:StringVar
    :return: None
    """
    try:
        image_folder = os.getcwd() + '\\Images'
        if not (os.path.exists(image_folder)):
            os.makedirs('Images')
        url_path = user_url.get()
        if url_path == '':
            messagebox.showwarning("Warning", "Url can't be empty!")
            return
        img = qrcode.make(user_url.get())
        new_window = Tk()
        new_window.tk.eval(f'tk::PlaceWindow {new_window._w} center')
        new_window.withdraw()
        response = askstring(title="Finished successfully!", prompt="Choose a name for your file", parent=new_window)
        img_full_name = image_folder + "\\" + response + '.png'
        img.save(img_full_name)
        response = messagebox.askokcancel("Summary", "Make a new qr?")
        label = Label(new_window, text=response)
        label.pack()
        if response == 1:
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            exit_response = messagebox.showwarning("Exit", "Bye Bye!")
            Label(new_window, text=exit_response).pack()
            new_window.destroy()
            main_window.quit()
            main_window.destroy()
    # Catch qrcode Exceptions
    except qrcode.ERROR_CORRECT_H as h:
        print(h)
    except qrcode.ERROR_CORRECT_Q as q:
        print(q)
    except qrcode.ERROR_CORRECT_M as m:
        print(m)
    except qrcode.ERROR_CORRECT_L as l:
        print(l)


def main():
    """
    Main function-run Tkinter ui
    :return: None
    """
    main_window = Tk()
    main_window.tk.eval(f'tk::PlaceWindow {main_window._w} center')
    main_window.title("QRCode Creator")
    main_window.geometry('800x600')
    main_window.config(bg='azure')
    user_url = StringVar(main_window)
    Label(main_window, text='The Qr Creator', bg='azure', fg='black', font=('Times', 20, 'bold')).place(x=300, y=20)
    Label(main_window, text='Enter Url', bg='azure2', anchor="e", justify=LEFT).place(x=360, y=100)
    Entry(main_window, textvariable=user_url, width=100, font=('calibre', 10, 'normal')).place(x=50, y=160)
    Button(main_window, borderwidth=10, text="Start", bg='ivory3', font=('calibre', 13),
           command=threading.Thread(target=create_qrcode, args=(main_window, user_url)).start).place(x=360, y=200)
    main_window.mainloop()


if __name__ == '__main__':
    main()
