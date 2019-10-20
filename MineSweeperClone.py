import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from threading import Timer
import math



def setWin():
    setWin = tk.Tk()

    # Choose an integer with a square root
    size = 100

    # Number goes down for increased difficulty
    difficulty = 4

    size = tk.IntVar()
    size.set(100)
    difficulty = tk.IntVar()
    difficulty.set(5)


    def start():
        sizeGL = size.get()
        diffGL = difficulty.get()
        print(size, difficulty)
        setWin.destroy()
        gameLoop(sizeGL, diffGL)


    sizeBut = tk.Label(setWin, text = "Select Size")
    sizeBut.grid(row=0, column=0)
    sizeRad100 = tk.Radiobutton(setWin, text = "Small", variable = size, value=100)
    sizeRad100.grid(row=0, column=1)
    sizeRad225 = tk.Radiobutton(setWin, text = "Medium", variable = size, value=225)
    sizeRad225.grid(row=0, column=2)
    sizeRad400 = tk.Radiobutton(setWin, text = "Large", variable = size, value=400)
    sizeRad400.grid(row=0, column=3)
    sizeRad625 = tk.Radiobutton(setWin, text= "Very Large", variable=size, value=625)
    sizeRad625.grid(row=0, column=4)



    diffBut = tk.Label(setWin, text = "Select Size")
    diffBut.grid(row=1, column=0)
    diffRad5 = tk.Radiobutton(setWin, text = "Easy", variable = difficulty, value=25)
    diffRad5.grid(row=1, column=1)
    diffRad25 = tk.Radiobutton(setWin, text = "Hard", variable = difficulty, value=5)
    diffRad25.grid(row=1, column=2)


    #TODO Start Button
    startBut = tk.Button(setWin, text = "Start", width = 20, command = start)
    startBut.grid(row=2, column=0)

    print(size)
    setWin.mainloop()

def gameLoop(size, difficulty):

    master = tk.Tk()
    notBombList = []
    def btnFunction(event):
        button = event.widget.grid_info()
        event.widget.destroy()
        row = button['row']
        column = button['column']
        notBombList.remove((row,column))
        print(len(notBombList))
        if len(notBombList) < 1:
            winLabel = tk.Label(master, text = "You Won", bg = "red", width = 26, height = 5, relief = 'sunken')
            winLabel.config(font=(40))
            winLabel.grid(row = 2, column =  1, rowspan = 5, columnspan = 8, sticky = tk.E + tk.W)

    bombList = []
    def endGame(event):
        event.widget.destroy()
        endGame = tk.Label(master, text = "Game Over", bg = "red", width = 26, height = 5, relief = 'sunken')
        endGame.config(font=(40))
        endGame.grid(row = 2, column =  1, rowspan = 5, columnspan = 8, sticky = tk.E + tk.W)
        t = Timer(3, lambda: endGame.config(text="You're Dead"))
        s = Timer(6, lambda: endGame.config(text = "Play Again?"))
        t.start()
        s.start()
        for label in master.grid_slaves():
            stuff1 = int(label.grid_info()['row'])
            stuff2 = int(label.grid_info()['column'])
            stuff3 = label.winfo_class()

            for coords in bombList:
                k,j = coords
                if stuff1 == k and stuff2 == j and stuff3 == 'Button':
                    label.grid_forget()


    image = Image.open("bomb2.jpg")
    photo = ImageTk.PhotoImage(image)
    photoThing = tk.PhotoImage(master = master)

    nums = np.arange(size, dtype = int)
    zeros = np.zeros(size, dtype = int)
    bombNum = (size//difficulty)
    # bombNum = 25
    # sqrt = 10
    zeros[:][:bombNum] = -1
    np.random.shuffle(zeros)
    sqrt = int(math.sqrt(size))
    nums = nums.reshape((sqrt,sqrt))
    zeros = zeros.reshape((sqrt,sqrt))

    bombs = 0
    k = 0
    for i in nums:
        numsk1 = nums[k]
        zerok1 = zeros[k]
        j = 0
        for y in zerok1:
            bombs = -1
            if y == -1:
                pass
            else:
                bombs=0
                if k-1 < 0:
                    above = "No Top"
                else:
                    above = zeros[k-1][j]
                    if above < 0:
                        bombs += 1
                    else:
                        pass
                if k + 1 > 9:
                    below = "No Bottom"
                else:
                    below = zeros[k+1][j]
                    if below < 0:
                        bombs += 1
                    else:
                        pass
                if j-1<0:
                    left = 'no left'
                else:
                    left = zeros[k][j-1]
                    if left < 0:
                        bombs += 1
                    else:
                        pass
                if j+1 >9:
                    right = 'no right'
                else:
                    right = zeros[k][j+1]
                    if right < 0:
                        bombs += 1
                    else:
                        pass
                zeros[k][j] = bombs


            if bombs == -1:
                lab = tk.Label(master, image = photoThing, width = 6)
                lab.grid(row=k, column = j)
                bombList.append((k,j))
            elif bombs == 0:
                lab = tk.Label(master, text = bombs, width = 3, fg = 'green')
                lab.grid(row=k, column=j)
                notBombList.append((k,j))
            elif bombs == 1:
                lab = tk.Label(master, text = bombs, width = 3, fg = 'blue')
                lab.grid(row=k, column = j)
                notBombList.append((k,j))
            elif bombs == 2:
                lab = tk.Label(master, text = bombs, width = 3, fg = 'orange')
                lab.grid(row=k, column=j)
                notBombList.append((k,j))
            elif bombs == 3:
                lab = tk.Label(master, text = bombs, width = 3, fg = 'red')
                lab.grid(row=k, column=j)
                notBombList.append((k,j))
            else:
                lab = tk.Label(master, text=bombs, width = 3, fg = 'black')
                lab.grid(row = k, column = j)
            if bombs == -1:
                btn = tk.Button(master, width=3)
                btn.grid(row=k, column=j)
                btn.bind('<Button-1>', endGame)
            else:
                btn = tk.Button(master, width=3)
                btn.grid(row=k, column=j)
                btn.bind('<Button-1>', btnFunction)
            j +=1
        k +=1
    master.mainloop()



if __name__ == '__main__':
    setWin()