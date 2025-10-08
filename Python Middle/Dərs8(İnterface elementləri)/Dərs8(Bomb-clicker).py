# modulu kodumuza import(daxil) edirik
import tkinter # tkinter - qrafik interfeys elementləri yaratmaqa yol açır


initial_time = 10
time_left = initial_time # başlanğıc göstərici
score = 0 
is_active = True # "Enter"(yenidən başla) basmaq üçün icasə



# əsas pəncərə (oyun üçün)
root = tkinter.Tk()
root.title("Oyun") # pəncərənin başlığı
root.geometry("600x600") # pəncərənin ölçüləri
root.resizable(False, False) # ölçülərin dəyişmək olmur



# proqramın ikonun təyin edirik, əgər yoxdursa, səhf verməsin
try:
    root.iconbitmap("bomb.ico")
except Exception:
    pass



# başlıq yazısı - istifadəçının oyuna başlaması üçün göstəriş
# label - tekst, <p> in html
info_label = tkinter.Label(root, text = f"Başlamaq üçün [Enter] basın", font = ("Comic Sans MS", 14))
info_label.pack()

# vaxt göstəricisi
time_label = tkinter.Label(root, text = f"Vaxt: {time_left}", font = ("Comic Sans MS", 14))
time_label.pack()

# xal göstəricisi
score_label = tkinter.Label(root, text = f"Xal: {score}", font = ("Comic Sans MS", 14))
score_label.pack()



# bomba üçün gərəkən gif-ləri qeyd edirik
img_1 = tkinter.PhotoImage(file = "1.gif")
img_2 = tkinter.PhotoImage(file = "2.gif")
img_3 = tkinter.PhotoImage(file = "3.gif")
img_4 = tkinter.PhotoImage(file = "4.gif")



# bomba şəklini yerləşdiririk
bomb_element = tkinter.Label(image = img_1)
bomb_element.pack()



# oyunda olan "click" yəni əsas düymə
click_button = tkinter.Button(root, text = "Click!", bg = "black", fg = "white",
                              width = 15, font = ("Comic Sans MS", 14), state = "disabled")
click_button.pack()



# funksiyalar
# düyməyə basanda bəzi məntiqi alqoritmlər işləyir
def click():
    global score
    if(is_active):
        score += 1
        score_label.config(text = f"Xal: {score}")

# vaxt taymerinin azalması
def countdown():
    global time_left, is_active
    if(is_active and time_left > 0):
        time_left -= 1
        time_label.config(text = f"Vaxt: {time_left}")
        root.after(1000, countdown) # hər 1 saniyədən bir, 1 saniyə azalır
    elif(time_left == 0):
            end_game()

# oyunun başlatmaq 
def start_game(event = None):
    global time_left, score, is_active
    score = 0
    time_left = initial_time
    is_active = True
    score_label.config(text = f"Xal: {score}")
    time_label.config(text = f"Vaxt: {time_left}")
    info_label.config(text = f"Başlamaq üçün [Enter] basın")
    click_button.config(state = "normal")
    countdown()

# oyunun bitməsi
def end_game():
    global is_active
    is_active = False
    click_button.config(state = "disabled")
    info_label.config(text = f"Vaxt bitdi! GPS: {score / initial_time}")



# commandların, və funksiyaların əlarələri
click_button.config(command = click)
root.bind("<Return>", start_game)



# pəncərəni açıq saxlamaq üçün
root.mainloop()