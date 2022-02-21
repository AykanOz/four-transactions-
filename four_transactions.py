from cProfile import label
from cgitb import text
from tkinter import *
from turtle import end_fill
from unittest import result
import random
#import time

root = Tk()
root.geometry("450x300+500+200")
root.title("Math Game")
root.iconbitmap("math_game.ico")

def get_secim():
    result = secim.get()
    if result == 1:
        root.destroy()
        
        def questions():
            question_lbl["text"] = "Aşağıdaki işlemin sonucu kaçtır?"
            num1 = random.randint(2,10)
            num2 = random.randint(2,10)
            num1_entry.insert(1,str(num1))
            num2_entry.insert(1,str(num2))
        def next():
            num1 = random.randint(2,10)
            num2 = random.randint(2,10)
            num1_entry.delete(0,"end")
            num2_entry.delete(0,"end")
            num1_entry.insert(1,str(num1))
            num2_entry.insert(1,str(num2))
            answer_entry.delete(0,"end")
            result_lbl["text"] = ""
            

        def toplama():
            result = int(num1_entry.get()) + int(num2_entry.get())
         
            if result == int(answer_entry.get()):
                result_lbl["text"] = "Tebrikler, doğru cevap!!"
                
            else:
                result_lbl["text"] = "Bilemedin, tekrar dene!!" 
                
        game = Tk()
        game.geometry("450x300+500+200")
        game.title("Toplama Oyunu")
        game.iconbitmap("math_game.ico")
        
        frame = Canvas(game,bg="#add8e6")
        frame.place(relx=0.05,rely=0.05,relheight=0.20,relwidth=0.9)
        game_name = Label(frame,text="Toplama Oyunu",bg="#add8e6",fg="red",font=("Arial bold",20))
        game_name.pack(pady=15)

        frame_middle= Canvas(game,bg="#add8e6")
        frame_middle.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.55)
        question_lbl = Label(frame_middle,bg="#add8e6",font=("Arial",12))
        question_lbl.pack(pady=18)
        num1_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num1_entry.place(relx=0.25,rely=0.35)
        plus_lbl = Label(frame_middle,text="+",font=("Arial",18))
        plus_lbl.place(relx=0.38,rely=0.35)
        num2_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num2_entry.place(relx=0.45,rely=0.35)
        equal_lbl=Label(frame_middle,text="=",font=("Arial",18))
        equal_lbl.place(relx=0.58,rely=0.35)
        answer_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        answer_entry.place(relx=0.65,rely=0.35)
        confirm_btn= Button(frame_middle,command=toplama,text="Gönder",bg="#add8e6")
        confirm_btn.place(relx=0.45,rely=0.60)
        next_btn = Button(frame_middle,text="Sonraki",bg="#add8e6",command=next)
        next_btn.place(relx=0.65,rely=0.6)
        start_btn=Button(frame_middle,text="Başlat",bg="#add8e6",command=questions)
        start_btn.place(relx=0.25,rely=0.6)

        frame_bottom= Canvas(game,bg="#add8e6")
        frame_bottom.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.25)
        result_lbl = Label(frame_bottom,bg="#add8e6",font=("Arial",18))
        result_lbl.pack(pady=17)
        
        
        game.mainloop()
                 
            
    elif result == 2:
        root.destroy()
        
        def questions():
            question_lbl["text"] = "Aşağıdaki işlemin sonucu kaçtır?"
            while True:
                num1 = random.randint(2,20)
                num2 = random.randint(2,10)
                if num1 > num2:
                    num1_entry.insert(1,str(num1))
                    num2_entry.insert(1,str(num2))
                    break
        def next():
            while True:
                num1 = random.randint(2,20)
                num2 = random.randint(2,10)
                if num1 > num2:
                    num1_entry.delete(0,"end")
                    num2_entry.delete(0,"end")
                    num1_entry.insert(1,str(num1))
                    num2_entry.insert(1,str(num2))
                    answer_entry.delete(0,"end")
                    result_lbl["text"] = ""
                    break

        def cikarma():
            result = int(num1_entry.get()) - int(num2_entry.get())
         
            if result == int(answer_entry.get()):
                result_lbl["text"] = "Tebrikler, doğru cevap!!"
                
            else:
                result_lbl["text"] = "Bilemedin, tekrar dene!!" 
                
        game = Tk()
        game.geometry("450x300+500+200")
        game.title("Çıkarma Oyunu")
        game.iconbitmap("math_game.ico")
        
        frame = Canvas(game,bg="#add8e6")
        frame.place(relx=0.05,rely=0.05,relheight=0.20,relwidth=0.9)
        game_name = Label(frame,text="Çıkarma Oyunu",bg="#add8e6",fg="red",font=("Arial bold",20))
        game_name.pack(pady=15)

        frame_middle= Canvas(game,bg="#add8e6")
        frame_middle.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.55)
        question_lbl = Label(frame_middle,bg="#add8e6",font=("Arial",12))
        question_lbl.pack(pady=18)
        num1_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num1_entry.place(relx=0.25,rely=0.35)
        plus_lbl = Label(frame_middle,text="-",font=("Arial",18))
        plus_lbl.place(relx=0.38,rely=0.35)
        num2_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num2_entry.place(relx=0.45,rely=0.35)
        equal_lbl=Label(frame_middle,text="=",font=("Arial",18))
        equal_lbl.place(relx=0.58,rely=0.35)
        answer_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        answer_entry.place(relx=0.65,rely=0.35)
        confirm_btn= Button(frame_middle,command=cikarma,text="Gönder",bg="#add8e6")
        confirm_btn.place(relx=0.45,rely=0.60)
        next_btn = Button(frame_middle,text="Sonraki",bg="#add8e6",command=next)
        next_btn.place(relx=0.65,rely=0.6)
        start_btn=Button(frame_middle,text="Başlat",bg="#add8e6",command=questions)
        start_btn.place(relx=0.25,rely=0.6)

        frame_bottom= Canvas(game,bg="#add8e6")
        frame_bottom.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.25)
        result_lbl = Label(frame_bottom,bg="#add8e6",font=("Arial",18))
        result_lbl.pack(pady=17)
        
        
        game.mainloop()
    elif result == 3:
        root.destroy()
        
        def questions():
            question_lbl["text"] = "Aşağıdaki işlemin sonucu kaçtır?"
            num1 = random.randint(2,10)
            num2 = random.randint(2,10)
            num1_entry.insert(1,str(num1))
            num2_entry.insert(1,str(num2))
        def next():
            num1 = random.randint(2,10)
            num2 = random.randint(2,10)
            num1_entry.delete(0,"end")
            num2_entry.delete(0,"end")
            num1_entry.insert(1,str(num1))
            num2_entry.insert(1,str(num2))
            answer_entry.delete(0,"end")
            result_lbl["text"] = ""
            

        def carpma():
            result = int(num1_entry.get()) * int(num2_entry.get())
         
            if result == int(answer_entry.get()):
                result_lbl["text"] = "Tebrikler, doğru cevap!!"
                
            else:
                result_lbl["text"] = "Bilemedin, tekrar dene!!" 
                
        game = Tk()
        game.geometry("450x300+500+200")
        game.title("Çarpma Oyunu")
        game.iconbitmap("math_game.ico")
        
        frame = Canvas(game,bg="#add8e6")
        frame.place(relx=0.05,rely=0.05,relheight=0.20,relwidth=0.9)
        game_name = Label(frame,text="Çarpma Oyunu",bg="#add8e6",fg="red",font=("Arial bold",20))
        game_name.pack(pady=15)

        frame_middle= Canvas(game,bg="#add8e6")
        frame_middle.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.55)
        question_lbl = Label(frame_middle,bg="#add8e6",font=("Arial",12))
        question_lbl.pack(pady=18)
        num1_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num1_entry.place(relx=0.25,rely=0.35)
        plus_lbl = Label(frame_middle,text="x",font=("Arial",18))
        plus_lbl.place(relx=0.38,rely=0.35)
        num2_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num2_entry.place(relx=0.45,rely=0.35)
        equal_lbl=Label(frame_middle,text="=",font=("Arial",18))
        equal_lbl.place(relx=0.58,rely=0.35)
        answer_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        answer_entry.place(relx=0.65,rely=0.35)
        confirm_btn= Button(frame_middle,command=carpma,text="Gönder",bg="#add8e6")
        confirm_btn.place(relx=0.45,rely=0.60)
        next_btn = Button(frame_middle,text="Sonraki",bg="#add8e6",command=next)
        next_btn.place(relx=0.65,rely=0.6)
        start_btn=Button(frame_middle,text="Başlat",bg="#add8e6",command=questions)
        start_btn.place(relx=0.25,rely=0.6)

        frame_bottom= Canvas(game,bg="#add8e6")
        frame_bottom.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.25)
        result_lbl = Label(frame_bottom,bg="#add8e6",font=("Arial",18))
        result_lbl.pack(pady=17)
        
        
        game.mainloop()
    elif result == 4:
        root.destroy()
        
        def questions():
            question_lbl["text"] = "Aşağıdaki işlemin sonucu kaçtır?"

            while True:
                num1 = random.randint(1,100)
                num2 = random.randint(2,10)
                if (num1>num2) and (num1%num2==0 and num1//num2 < 10):
                    num1_entry.insert(1,str(num1))
                    num2_entry.insert(1,str(num2))
                    break
                  
        def next():
            while True:
                num1 = random.randint(1,100)
                num2 = random.randint(2,10)
                if (num1>num2) and (num1%num2==0 and num1//num2 < 10):
                    num1_entry.delete(0,"end")
                    num2_entry.delete(0,"end")
                    num1_entry.insert(1,str(num1))
                    num2_entry.insert(1,str(num2))
                    answer_entry.delete(0,"end")
                    result_lbl["text"] = ""
                    break
                    
                    

        def bolme():
            result = int(num1_entry.get()) / int(num2_entry.get())
         
            if result == int(answer_entry.get()):
                result_lbl["text"] = "Tebrikler, doğru cevap!!"
                
            else:
                result_lbl["text"] = "Bilemedin, tekrar dene!!" 
                
        game = Tk()
        game.geometry("450x300+500+200")
        game.title("Bölme Oyunu")
        game.iconbitmap("math_game.ico")
        
        frame = Canvas(game,bg="#add8e6")
        frame.place(relx=0.05,rely=0.05,relheight=0.20,relwidth=0.9)
        game_name = Label(frame,text="Bölme Oyunu",bg="#add8e6",fg="red",font=("Arial bold",20))
        game_name.pack(pady=15)

        frame_middle= Canvas(game,bg="#add8e6")
        frame_middle.place(relx=0.05,rely=0.25,relwidth=0.9,relheight=0.55)
        question_lbl = Label(frame_middle,bg="#add8e6",font=("Arial",12))
        question_lbl.pack(pady=18)
        num1_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num1_entry.place(relx=0.25,rely=0.35)
        plus_lbl = Label(frame_middle,text="/",font=("Arial",18))
        plus_lbl.place(relx=0.38,rely=0.35)
        num2_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        num2_entry.place(relx=0.45,rely=0.35)
        equal_lbl=Label(frame_middle,text="=",font=("Arial",18))
        equal_lbl.place(relx=0.58,rely=0.35)
        answer_entry = Entry(frame_middle,width=3,justify="center",font=("Arial",18))
        answer_entry.place(relx=0.65,rely=0.35)
        confirm_btn= Button(frame_middle,command=bolme,text="Gönder",bg="#add8e6")
        confirm_btn.place(relx=0.45,rely=0.60)
        next_btn = Button(frame_middle,text="Sonraki",bg="#add8e6",command=next)
        next_btn.place(relx=0.65,rely=0.6)
        start_btn=Button(frame_middle,text="Başlat",bg="#add8e6",command=questions)
        start_btn.place(relx=0.25,rely=0.6)

        frame_bottom= Canvas(game,bg="#add8e6")
        frame_bottom.place(relx=0.05,rely=0.7,relwidth=0.9,relheight=0.25)
        result_lbl = Label(frame_bottom,bg="#add8e6",font=("Arial",18))
        result_lbl.pack(pady=17)
        
        
        game.mainloop()

secim = IntVar()

frame = Canvas(root,bg="#add8e6")
frame.place(relx=0.05,rely=0.05,relheight=0.25,relwidth=0.9)
game_label = Label(frame,text="Oyunlar",bg="#add8e6",fg="red",font=("Arial bold",16))
game_label.pack(padx=10,pady=10)
game_option = Label(frame,text="Lütfen Bir Oyun Seç",bg="#add8e6",font=("Arial",10))
game_option.pack(padx=5,pady=3)

frame_left = Canvas(root,bg="#add8e6")
frame_left.place(relx=0.05,rely=0.31,relheight=0.65,relwidth=0.5)

oyun_toplama = Radiobutton(frame_left,value=1,variable=secim,text="Toplama",bg="#add8e6",font=("Arial",12))
oyun_toplama.pack(padx=25,pady=10,anchor=NW)
oyun_cikarma = Radiobutton(frame_left,value=2,variable=secim,text="Çıkarma",bg="#add8e6",font=("Arial",12))
oyun_cikarma.pack(padx=25,pady=10,anchor=NW)
oyun_carpma = Radiobutton(frame_left,value=3,variable=secim,text="Çarpma",bg="#add8e6",font=("Arial",12))
oyun_carpma.pack(padx=25,pady=10,anchor=NW)
oyun_bolme = Radiobutton(frame_left,value=4,variable=secim,text="Bölme",bg="#add8e6",font=("Arial",12))
oyun_bolme.pack(padx=25,pady=10,anchor=NW)

frame_right = Canvas(root,bg="#add8e6")
frame_right.place(relx=0.56,rely=0.31,relheight=0.65,relwidth=0.39)
secim_btn = Button(frame_right,text="Seç",command=get_secim,height=2,width=10,font="Arial 12",bg="#add8e6")
secim_btn.pack(padx=10,pady=60)



root.mainloop()
