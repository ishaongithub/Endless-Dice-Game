# -*- coding: utf-8 -*-
"""
Created on Sun May  8 11:02:43 2022

@author: ishar
"""

from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()
root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(bg="cyan")
img= ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1= Label(root, text="Player 1", bg="red", fg="white")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2= Label(root, text="Player 2", bg="red", fg="white")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

player_1_score_label=Label(root,bg="red", fg="white" )
player_1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player_2_score_label=Label(root,bg="red", fg="white" )
player_2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)

random_dice_label=Label(root, bg="chocolate", fg="white")
random_dice_label.place(relx=0.5, rely=0.5, anchor=CENTER)

player_1_score=0
def player1():
    global player_1_score
    random_no=random.randint(1,6)
    random_dice_label["text"]="Player 1 Dice Number : "+str(random_no)
    player_1_score=player_1_score+random_no
    player_1_score_label["text"]=str(player_1_score)
    
player_1_btn= Button(root, image=img, command=player1)
player_1_btn.place(relx=0.1, rely=0.6, anchor=CENTER)

player_2_score=0
def player2():
    global player_2_score
    random_no2=random.randint(1,6)
    random_dice_label["text"]="Player 2 Dice Number : "+str(random_no2)
    player_2_score=player_2_score+random_no2
    player_2_score_label["text"]=str(player_2_score)
    
player_2_btn= Button(root, image=img, command=player2)
player_2_btn.place(relx=0.9, rely=0.6, anchor=CENTER)



root.mainloop()