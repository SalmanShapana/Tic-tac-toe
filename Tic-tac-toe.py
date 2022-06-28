
from tkinter import *
import numpy as np

board=np.array([[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]])

root2=Tk()
def click():
  mylabel=Label(root2,text="choose X or O")
  mylabel.pack()

  myButtonX=Button(root2,bg='blue',text="X" ,command=chooseX)
  myButtonX.pack(side = LEFT)
  myButtonO=Button(root2,bg='red',text="O",command=chooseO)
  myButtonO.pack(side = RIGHT)
  root2.mainloop()

def row_win(board, player):
     for x in range(len(board)):
         win = True
         for y in range(len(board)):
              if board[x, y] != player:
                   win = False
                   break
         if win == True:
               return(win)
     return(win)

def col_win(board, player):
    for x in range(len(board)):
          win = True
          for y in range(len(board)):
              if board[y][x] != player:
                   win = False
                   break
          if win == True:
               return(win)
    return(win)     

def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
      if board[x, x] != player:
        win =False
    if win:
        return win
    win = True
    if win:
         for x in range(len(board)):
              y= len(board) - 1- x
              if board[x, y] != player:
                  win = False
    return win 
player_play=""

# play

title=None   
def buttonpushed(root):
     root.destroy()
def message(text):
  root=Tk()
  w=Label(root,text=text)
  w.pack()
  myButton=Button(root,text="Exit",command=lambda :buttonpushed(root))
  myButton.pack()
  root.mainloop()
def evaluate(board):
    winner =0
    for player in [1, 2]:
        if (row_win(board, player) or col_win(board,player) or diag_win(board,player)):
            winner=player       
    if (np.all(board!=0)) and winner == 0:
        winner = -1
    return winner  

def changegtext(root,x,globaltext,a,b):
  # global globaltext
  global title
  global board
  global player_play
  global player_One

  if globaltext.get() in["X","O"]:
    return False

  s=0
  play=""
  if x==player_One:
    play="player two"
    s=1
  else:
      play="player One"
      s=2  
  globaltext.set(x)
  if x=="X":
   board[a][b]=s
  
   player_play="O"

   title.set("this is %s " %(play) +player_play )
  else:
   board[a][b]=s

   player_play="X"

   title.set("this is %s "%(play) +player_play)
  
  if(evaluate(board)==1):
    root.destroy()
    message("player one win")
  if(evaluate(board)==2):
    root.destroy()
    message("player Two win")
  if (evaluate(board)== -1):
    root.destroy()
    message("GAME OVER") 


def XO():
    
    global player_play
    global player_One
    root=Tk()
    globaltext=StringVar()
    globaltext1=StringVar()
    globaltext2=StringVar()
    globaltext3=StringVar()
    globaltext4=StringVar()
    globaltext5=StringVar()
    globaltext6=StringVar()
    globaltext7=StringVar()
    globaltext8=StringVar()
    global title
    player_play=player_One
    title=StringVar()
    title.set("this is player one symbol".replace("symbol",player_play))
    globaltext.set("")
    root.geometry("400x400")
    UL=Label(root, width=10,height=5, relief = "groove",textvariable=globaltext)
    UL.place(relx = 0.15,anchor ='nw')
    UL.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext,0,0))
    UM=Label(root,width=10,height=5,relief = "groove", textvariable=globaltext1)
    UM.pack()
    UM.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext1,0,1))
    UR=Label(root,width=10,height=5,relief = "groove",textvariable=globaltext2)
    UR.place(relx = 0.85,rely = 0.0,anchor ='ne')
    UR.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext2,0,2))
    ML=Label(root,width=10,height=5,relief = "groove",textvariable=globaltext3)
    ML.place(relx = 0.269,
                   rely = 0.376,
                   anchor = 'center')
    ML.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext3,1,0))                   
    MM=Label(root,width=10,height=5,relief = "groove",textvariable=globaltext4)
    MM.place(relx = 0.5,
                   rely = 0.376,
                   anchor = 'center')
    MM.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext4,1,1))                   

    MR=Label(root,width=10,height=5,relief = "groove",textvariable=globaltext5)
    MR.place(relx = 0.73,
                   rely = 0.376,
                   anchor = 'center')
    MR.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext5,1,2))                   

    DL=Label(root,width=10,height=5,relief = "groove",textvariable=globaltext6)
    DL.place(relx = 0.146,
                 rely = .752,
                 anchor ='sw')
    DL.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext6,2,0))                   

    DM=Label(root,width=10,height=5,relief = "groove",textvariable=globaltext7)
    DM.place(relx = 0.382,
                 rely = .75,
                 anchor ='sw')
    DM.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext7,2,1))                   

    DR=Label(root,width=10,height=5,relief = "groove",textvariable=globaltext8)
    DR.place(relx = 0.615,
                 rely = .75,
                 anchor ='sw')
    DR.bind("<Button-1>",lambda a:changegtext(root,player_play,globaltext8,2,2))                   

    Player_des=Label(root,width=45,height=5,relief = "groove",textvariable=title)
    Player_des.place(relx = 0.5,
                 rely = 1.0,
                 anchor ='s')
    
    root.mainloop()


player_One=None
player_Two=None

def chooseX():
 global player_One
 global player_Two
 player_One="X"
 player_Two="O"
 root2.destroy()
 XO()

  
def chooseO():
 global player_One
 global player_Two
 player_One="O"
 player_Two="X"
 root2.destroy()
 XO()

  
click()
# print(player_One)