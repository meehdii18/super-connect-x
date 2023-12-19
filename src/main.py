import tkinter as tk

import customtkinter as ctk

# Define the size of the game board
boardWidth, boardHeight = 7, 6
grid = [[0 for _ in range(boardWidth)] for _ in range(boardHeight)]


# Function to handle button clicks
def add_coin(col):
    def _add_coin():
        player = 1  # Assume player 1 is the human player
        row = boardHeight - 1
        actualcoin = grid[row][col]
        while actualcoin != 0 and row > 0:
            row -= 1
            actualcoin = grid[row][col]
        grid[row][col] = player
        canvas.create_oval(col * 100 + 10, (boardHeight - row) * 100 + 60, (col + 1) * 100 - 10,
                           (boardHeight - row) * 100 + 140, fill="yellow" if player == 1 else "red")

    return _add_coin


# Create a window
window = tk.Tk()
window.title("Super Connect 4")

# Create a canvas in the window
canvas = ctk.CTkCanvas(window, width=boardWidth * 100, height=boardHeight * 100 + 50, background="blue")
canvas.pack()

# Draw the game board on the canvas
for row in range(boardHeight):
    for col in range(boardWidth):
        canvas.create_oval(col * 100 + 10, (boardHeight - row) * 100 + 60,
                           (col + 1) * 100 - 10, (boardHeight - row) * 100 + 140, fill="white")

# Create a button for each column
for col in range(boardWidth):
    button = ctk.CTkButton(window, text=f"Column {col + 1}", command=add_coin(col), width=100, height=50)
    button.place(x=col * 100, y=0)

window.mainloop()
