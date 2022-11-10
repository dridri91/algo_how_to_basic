from tkinter import *
import time 

grid = [[0,0,0]for i in range(3)]
end = False
turn = 1
tie = 0

def test(i,j):
    global grid,turn,end,tie
    if not end:
        if turn%2:
            color = '#00ff00'
            letter = 'X'
        else:
            color = '#0000ff'
            letter = 'O'
        
        a = Button(frame,width=10,height=5,background=color,font = ("Helvetica","20"))
        a.grid(row=i, column=j)
        a.configure(text=letter)
        grid[i-1][j]=turn
        tie+=1
        print(end)
        turn = turn%2+1
        a = Button(frame, height=3, width=20,font = ("Helvetica","10"))
        a.grid(row=0,column=1)
        a.configure(text=f"j{turn} à vous de jouer !")
        check(grid,turn)

def check(grid,turn):
    global end,tie
    diag1 = []
    diag2 = []
    for i in range(3):
        column = []

        for e in range(3):
            column.append(grid[e][i])

        if set(grid[i]) in ({2},{1}) or set(column) in ({2},{1}): # Check les colonnes et lignes
            end = True

        diag1.append(grid[i][i])
        diag2.append(grid[2-i][i])

    if set(diag2) in ({2},{1}) or set(diag1) in ({2},{1}):
        end = True

    if end:
        a = Button(frame, height=3, width=20,font = ("Helvetica","10"))
        a.grid(row=0,column=1)
        a.configure(text=f"le joueur {(turn+1)%2} a gagné !!")
    
    if tie==9:
        a = Button(frame, height=3, width=20,font = ("Helvetica","10"))
        a.grid(row=0,column=1)
        a.configure(text=f"Pas de gagnant !!")
        end = True

window = Tk()
window.title('tic tac toe')
window.geometry('1000x1000')
window.config(background='#000000')

frame = Frame(window,bg='#000000')

for i in range(3):
    for j in range(3):
        Button(frame, height=5, width=10,command=lambda a=i+1,b=j:test(a,b),font = ("Helvetica","20")).grid(row=i+1,column=j)

a = Button(frame, height=3, width=20,font = ("Helvetica","10"))
a.grid(row=0,column=1)
a.configure(text="j1 à vous de jouer !")

frame.pack(expand=True)
#window.attributes('-fullscreen',True)
window.mainloop()
