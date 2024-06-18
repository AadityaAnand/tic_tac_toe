import tkinter as tk
from tkinter import messagebox

#Intialization of the application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

player = "X"
buttons = [[None, None, None], [None, None, None], [None, None, None]]

#Checking winner
def winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
        if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            return True
        if buttons[2][0]["text"] == buttons[1][1]["text"] == buttons[0][2]["text"] != "":
            return True
    return False

#Checking draw
def check_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

#resetting the game
def reset():
    global player
    player = "X"
    for row in buttons:
        for button in row:
            button["text"] = ""

#Clicking the button
def button_click(row, col):
    global player
    if buttons[row][col]["text"] == "" and not winner():
        buttons[row][col]["text"] = player
        if winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
            reset()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
            reset()
        else:
            player = "O" if player == "X" else "X"

#Game board
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 40), width=5, height=2, command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col)


root.mainloop()