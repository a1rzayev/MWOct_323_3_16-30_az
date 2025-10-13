# pəncərə tətbiqləri ilə işləmək üçün lazım olan modul(kitabxana) əlavə edirik
import tkinter
from tkinter import filedialog



# pəncərəni açırıq
root = tkinter.Tk()
root.geometry("600x400")
root.title("Sehrbazın Gündəliyi")
root.minsize(200, 100)
root.maxsize(1920, 1080)



# teksti əvvəlcədən qlobal dəyişən olaraq təyin edirik
text = tkinter.Text(root)
text.pack(expand = tkinter.YES, fill = tkinter.BOTH)



# yeni faylın yaradılması
def file_new():
    save_or_not = tkinter.Toplevel(root)
    save_or_not.geometry("150x70")
    save_or_not.resizable(False, False)
    save_or_not.grid_columnconfigure(0, minsize = 75)
    save_or_not.grid_columnconfigure(1, minsize = 75)

    saving_label = tkinter.Label(save_or_not, text = "Faylı yaddaşda saxlamaq istəyirsiz?")
    saving_label.grid(columnspan = 2)    

    # "bəli" və "xeyr" düymələri
    def without_saving():
        save_or_not.destroy()
        text.delete("1.0", tkinter.END)

    def saving():
        file_save()
        save_or_not.destroy()
        text.delete("1.0", tkinter.END)

    yes_button = tkinter.Button(save_or_not, text = "Bəli", command = saving, width = 8)
    no_button = tkinter.Button(save_or_not, text = "Xeyr", command = without_saving, width = 8)
    yes_button.grid(column = 0, row = 1)
    no_button.grid(column = 1, row = 1)



# faylın açılması
def file_open():
    file_name = filedialog.askopenfilename(
        initialdir="/", 
        title = "Faylı aç",
        filetypes=(("Mətn sənədləri", "*.txt"), ("Bütün sənədlər", "*.*"))
    )
    root.deiconify()

    if(file_name):
        with open(file_name, "r") as ourfile:
            text_open = ourfile.read()
        text.delete("1.0", tkinter.END)
        text.insert(tkinter.END, text_open)



# faylın yadda saxlanılması
def file_save():
    file_name = filedialog.asksaveasfilename(
        initialdir="/", 
        title = "Faylı aç",
        defaultextension="*.txt",
        filetypes=(("Mətn sənədləri", "*.txt"), ("Bütün sənədlər", "*.*"))
    )
    root.deiconify()
    
    if(file_name):
        with open(file_name, "w") as ourfile:
            text_save = text.get("1.0", tkinter.END).strip()
            ourfile.write(text_save)



# proqramdan çıxış
def file_exit():
    root.destroy()



# "kömək" funksiyası
def help():
    help_window = tkinter.Toplevel(root)
    help_window.geometry("300x80")
    help_window.resizable(False, False)

    help_label = tkinter.Label(
        help_window,
        text = "kömək üçün Əkbərə(əkbər@mail.com) müraciət edin"
    )
    help_label.pack(pady = 5)

    def back():
        help_window.destroy()

    back_button = tkinter.Button(help_window, text = "Geri", command = back, width = 10)
    back_button.pack()

    # pəncərəni bağlamaq üçün alternativ yol
    help_window.protocol("VM_DELETE_WINDOW", help_window.destroy)



# "haqqımızda" pəncərəsi
def about():
    about_window = tkinter.Toplevel(root)
    about_window.geometry("300x80")
    about_window.resizable(False, False)
    about_label = tkinter.Label(
        about_window,
        text = "Biz STEP İT proqramçılarıyıq!"
    )
    about_label.pack(pady = 5)

    def back():
        about_window.destroy()

    back_button = tkinter.Button(about_window, text = "Geri", command = back, width = 10)
    back_button.pack()

    # pəncərəni bağlamaq üçün alternativ yol
    about_window.protocol("VM_DELETE_WINDOW", about_window.destroy)



# menu yaradılması
ourmenu = tkinter.Menu(root)
root.config(menu = ourmenu)



# fayl menusu
file_menu = tkinter.Menu(ourmenu, tearoff = 0)
file_menu.add_command(label = "Yeni", command = file_new)
file_menu.add_command(label = "Aç", command = file_open)
file_menu.add_command(label = "Nə kimi saxla", command = file_save)
file_menu.add_command(label = "Çıxış", command = file_exit)
ourmenu.add_cascade(label = "Fayl", menu = file_menu)



# kömək menusu
help_menu = tkinter.Menu(ourmenu, tearoff = 0)
help_menu.add_command(label = "Kömək", command = help)
help_menu.add_command(label = "Haqqımızda", command = about)
ourmenu.add_cascade(label = "Kömək", menu = help_menu)



# tətbiqi işə salırıq
root.mainloop()