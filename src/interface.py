import os
import tkinter as tk
import webbrowser as wb

import customtkinter
import pyglet
from CTkMessagebox import CTkMessagebox
from PIL import Image

from console_connect_x import init

app = customtkinter.CTk()
app.title("SUPER CONNECT X")
app.geometry("1080x720")
app.resizable(False, False)


def select_frame_by_name(name):
    # set button color for selected button
    home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
    frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

    # show selected frame
    if name == "home":
        home_frame.grid(row=1, column=0, sticky="nsew")
    else:
        home_frame.grid_forget()
    if name == "frame_2":
        second_frame.grid(row=1, column=0, sticky="nsew")
    else:
        second_frame.grid_forget()
    if name == "frame_3":
        third_frame.grid(row=1, column=0, sticky="nsew")
    else:
        third_frame.grid_forget()


def home_button_event():
    select_frame_by_name("home")


def frame_2_button_event():
    select_frame_by_name("frame_2")


def frame_3_button_event():
    select_frame_by_name("frame_3")


def change_appearance_mode_event(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


def launch_confirmation():
    launch = CTkMessagebox(title="Lancer une partie",
                           message="Voulez-vous lancez la partie avec les paramètres séléctionnés ?",
                           option_1="Non", option_2="Oui", sound=True, corner_radius=20)
    if launch.get() == "Oui":
        frame_2_button_event()
        start_game()


def quit_confirmation():
    end_game = CTkMessagebox(title="Quitter le jeu", message="Voulez-vous vraiment quitter le jeu ?", icon="warning",
                             option_1="Oui", option_2="Non", sound=True)
    if end_game.get() == "Oui":
        app.destroy()


def start_game():
    try:
        game_canvas.destroy()
        for button in buttons:
            button.destroy()
        buttons_frame.destroy()
    except NameError:
        pass

    columns = var_column.get()
    rows = var_row.get()
    required_coins = var_requiredcoins.get()
    difficulty = var_difficulty.get()
    player1_color_choice = player1_color.get().lower()
    player2_color_choice = player2_color.get().lower()
    initialize_game(columns, rows, required_coins, difficulty, player1_color_choice, player2_color_choice)


def display_game_board(canvas, game_board, player1_color, player2_color, cell_size=70, padding=10):
    global buttons
    global buttons_frame
    for row_idx, row in enumerate(game_board):
        for col_idx, cell in enumerate(row):
            x1 = col_idx * cell_size + 6
            y1 = row_idx * cell_size + 6
            x2 = x1 + cell_size - padding
            y2 = y1 + cell_size - padding
            canvas.create_oval(x1, y1, x2, y2, fill="white")

            if cell == 1:
                canvas.create_oval(x1, y1, x2, y2, fill=player1_color, outline=player1_color)
            elif cell == 2:
                canvas.create_oval(x1, y1, x2, y2, fill=player2_color, outline=player2_color)

    buttons = []
    col = var_column.get()
    row = var_row.get()
    buttons_frame = customtkinter.CTkFrame(second_frame, height=40, width=70 * col)
    buttons_frame.grid(row=0, column=col)
    buttons_frame.place(relx=0.5, rely=0.5 - (0.055 * row), anchor="center")
    for i in range(col):
        buttons.append(customtkinter.CTkButton(buttons_frame, width=65, height=35, corner_radius=100, text=str(i + 1),
                                               hover_color=player1_color, command=lambda col=i: button_event(col)))
        buttons[i].grid(row=0, column=i, padx=(4, 4))


def button_event(number):
    print("Button", number)
    if (number == 0):
        wb.open_new_tab('https://www.youtube.com/watch?v=Il9nwPlMZm4')
    elif (number == 1):
        wb.open_new_tab("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    elif (number == 2):
        wb.open_new_tab("https://www.youtube.com/watch?v=BO-pNmfojao")
    elif (number == 3):
        wb.open_new_tab("https://www.youtube.com/watch?v=T6jLL7ycJhY")
    elif (number == 4):
        wb.open_new_tab("https://www.youtube.com/watch?v=8444Uu-Gdsw")
    elif (number == 5):
        wb.open_new_tab("https://www.youtube.com/watch?v=Ap011D65du8")
    elif (number == 6):
        wb.open_new_tab("https://www.youtube.com/watch?v=HGeCH5uKlYQ")
    elif (number == 7):
        wb.open_new_tab("https://www.youtube.com/watch?v=4qUb7I1O-n0")


def initialize_game(columns, rows, required_coins, difficulty, player1_color, player2_color):
    global game_canvas
    global game_board
    game_board = init(columns, rows)
    game_canvas = customtkinter.CTkCanvas(second_frame, width=columns * 70, height=rows * 70)
    game_canvas.grid(row=0, column=0, sticky="nsew")
    game_canvas.place(relx=0.5, rely=0.55, anchor="center")

    game_board[0][0] = 1
    game_board[0][1] = 2
    display_game_board(game_canvas, game_board, player1_color, player2_color)

    print("| NEW GAME STARTED | Columns :", columns, " Rows:", rows, " Required coins:", required_coins, " Difficulty:",
          difficulty,
          " Player color:", player1_color, " AI color:", player2_color)


# Base theme
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Load font
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'Montserrat-Bold.ttf')
pyglet.font.add_file(font_path)
custom_font = customtkinter.CTkFont(family="Montserrat", size=20)

# set grid layout 1x2
app.grid_rowconfigure(1, weight=10)
app.grid_columnconfigure(0, weight=1)

# load images with light and dark mode image
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(40, 40))
banner_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(650, 195))
home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
chat_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "game.png")), size=(20, 20))
add_user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "end.png")), size=(20, 20))
start_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "start.png")), size=(50, 50))

# create navigation frame
navigation_frame = customtkinter.CTkFrame(app, corner_radius=0)
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.configure(height=70)
nav_frame_height = navigation_frame.winfo_reqheight()
app.rowconfigure(0, minsize=nav_frame_height)

navigation_frame_label = customtkinter.CTkLabel(navigation_frame, text="  SUPER CONNECT X", image=logo_image,
                                                compound="left",
                                                font=customtkinter.CTkFont(family="Montserrat", size=15, weight="bold"))
navigation_frame_label.grid(row=0, column=0)
navigation_frame_label.place(relx=0.1, rely=0.5, anchor="center")

home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="MAIN MENU",
                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                      hover_color=("gray70", "gray30"),
                                      font=customtkinter.CTkFont(family="Montserrat", size=15, weight="bold"),
                                      image=home_image, anchor="w", command=home_button_event)
home_button.grid(row=0, column=1, sticky="ew")
home_button.place(relx=0.35, rely=0.5, anchor="center")

frame_2_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="GAME FRAME",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         font=customtkinter.CTkFont(family="Montserrat", size=15, weight="bold"),
                                         image=chat_image, anchor="w", command=frame_2_button_event)
frame_2_button.grid(row=0, column=2, sticky="ew")
frame_2_button.place(relx=0.5, rely=0.5, anchor="center")

frame_3_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="END MENU",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         font=customtkinter.CTkFont(family="Montserrat", size=15, weight="bold"),
                                         image=add_user_image, anchor="w", command=frame_3_button_event)
frame_3_button.grid(row=0, column=3, sticky="ew")
frame_3_button.place(relx=0.65, rely=0.5, anchor="center")

appearance_mode_menu = customtkinter.CTkOptionMenu(navigation_frame, values=["Dark", "Light", "System"],
                                                   command=change_appearance_mode_event)
appearance_mode_menu.grid(row=0, column=4, sticky="w")
appearance_mode_menu.place(relx=0.85, rely=0.5, anchor="w")

# Main Menu
home_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
home_frame.grid(row=1, column=0, sticky="nsew")
home_frame.grid_columnconfigure(0, weight=2)

home_frame_large_image_label = customtkinter.CTkLabel(home_frame, text="", image=banner_image)
home_frame_large_image_label.grid(row=0, column=0)
home_frame_large_image_label.place(relx=0.2, rely=-0.025)

var_column = tk.IntVar()
var_row = tk.IntVar()

var_requiredcoins = tk.IntVar()
var_difficulty = tk.IntVar()

home_frame_column_text = customtkinter.CTkLabel(home_frame, text="Nombre de colonnes : ", fg_color="transparent",
                                                font=customtkinter.CTkFont(family="Montserrat", size=20))
home_frame_column_text.grid(row=1, column=0)
home_frame_column_text.place(relx=0.32, rely=0.298 + 0.03)
home_frame_column_slider = customtkinter.CTkSlider(home_frame, from_=3, to=8, number_of_steps=5, variable=var_column)
home_frame_column_slider.grid(row=1, column=0)
home_frame_column_slider.place(relx=0.55, rely=0.3 + 0.03)
home_frame_column_slider.set(7)
home_frame_column_val = customtkinter.CTkLabel(home_frame, textvariable=var_column, fg_color="transparent")
home_frame_column_val.grid(row=1, column=0)
home_frame_column_val.place(relx=0.6425, rely=0.25 + 0.03)

home_frame_row_text = customtkinter.CTkLabel(home_frame, text="Nombre de lignes : ", fg_color="transparent",
                                             font=customtkinter.CTkFont(family="Montserrat", size=20))
home_frame_row_text.grid(row=1, column=0)
home_frame_row_text.place(relx=0.35, rely=0.398 + 0.03)
home_frame_row_slider = customtkinter.CTkSlider(home_frame, from_=3, to=8, number_of_steps=5, variable=var_row)
home_frame_row_slider.grid(row=1, column=0)
home_frame_row_slider.place(relx=0.55, rely=0.4 + 0.03)
home_frame_row_slider.set(6)
home_frame_row_val = customtkinter.CTkLabel(home_frame, textvariable=var_row, fg_color="transparent")
home_frame_row_val.grid(row=1, column=0)
home_frame_row_val.place(relx=0.6425, rely=0.35 + 0.03)

home_frame_coins_text = customtkinter.CTkLabel(home_frame, text="Nombre de jetons pour gagner : ",
                                               fg_color="transparent",
                                               font=customtkinter.CTkFont(family="Montserrat", size=20))
home_frame_coins_text.grid(row=1, column=0)
home_frame_coins_text.place(relx=0.235, rely=0.498 + 0.03)

home_frame_coins_slider = customtkinter.CTkSlider(home_frame, from_=3, to=10,
                                                  number_of_steps=8, variable=var_requiredcoins)
home_frame_coins_slider.grid(row=1, column=0)
home_frame_coins_slider.place(relx=0.55, rely=0.5 + 0.03)
home_frame_coins_slider.set(4)
home_frame_coins_val = customtkinter.CTkLabel(home_frame, textvariable=var_requiredcoins, fg_color="transparent")
home_frame_coins_val.grid(row=1, column=0)
home_frame_coins_val.place(relx=0.6425, rely=0.45 + 0.03)

home_frame_difficulty_text = customtkinter.CTkLabel(home_frame, text="Difficulté de l'IA :", fg_color="transparent",
                                                    font=customtkinter.CTkFont(family="Montserrat", size=20))
home_frame_difficulty_text.grid(row=1, column=0)
home_frame_difficulty_text.place(relx=0.365, rely=0.59 + 0.03)

home_frame_difficulty_slider = customtkinter.CTkSlider(home_frame, from_=1, to=6, number_of_steps=6,
                                                       variable=var_difficulty)
home_frame_difficulty_slider.grid(row=1, column=0)
home_frame_difficulty_slider.place(relx=0.55, rely=0.6 + 0.03)
home_frame_difficulty_slider.set(3)
home_frame_difficulty_val = customtkinter.CTkLabel(home_frame, textvariable=var_difficulty, fg_color="transparent")
home_frame_difficulty_val.grid(row=1, column=0)
home_frame_difficulty_val.place(relx=0.6425, rely=0.55 + 0.03)

# Define available colors
available_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

# Create StringVar for player color choices
player1_color = tk.StringVar()
player2_color = tk.StringVar()

# Set default color
player1_color.set(available_colors[0])
player2_color.set(available_colors[1])

# Create OptionMenu for player color choices
player1_color_menu = customtkinter.CTkOptionMenu(home_frame, values=available_colors, variable=player1_color)
player1_color_menu.grid(row=1, column=0)
player1_color_menu.place(relx=0.555, rely=0.68 + 0.03)  # Adjust position as needed

player2_color_menu = customtkinter.CTkOptionMenu(home_frame, values=available_colors, variable=player2_color)
player2_color_menu.grid(row=1, column=0)
player2_color_menu.place(relx=0.555, rely=0.75 + 0.03)  # Adjust position as needed

player1_color_menu_text = customtkinter.CTkLabel(home_frame, text="Couleur du joueur :", fg_color="transparent",
                                                 font=customtkinter.CTkFont(family="Montserrat", size=20))
player1_color_menu_text.grid(row=1, column=0)
player1_color_menu_text.place(relx=0.35, rely=0.68 + 0.03)

player2_color_menu_text = customtkinter.CTkLabel(home_frame, text="Couleur de l'ordinateur :", fg_color="transparent",
                                                 font=customtkinter.CTkFont(family="Montserrat", size=20))
player2_color_menu_text.grid(row=1, column=0)
player2_color_menu_text.place(relx=0.305, rely=0.75 + 0.03)

home_frame_start_button = customtkinter.CTkButton(home_frame, text="", image=start_image, fg_color="transparent",
                                                  command=launch_confirmation, hover=False)
home_frame_start_button.grid(row=1, column=0)
home_frame_start_button.place(relx=0.46, rely=0.86)

# Game Frame
second_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

# End Menu
third_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

gamer_over_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "game_over.png")), size=(600, 360))
game_over_label = customtkinter.CTkLabel(third_frame, text="", image=gamer_over_image, fg_color="transparent")
game_over_label.place(relx=0.25, rely=0.1)

winner_text = customtkinter.CTkLabel(third_frame, text="X à gagné !", fg_color="transparent",
                                     font=customtkinter.CTkFont(family="Montserrat", size=20))
winner_text.grid(row=1, column=0)
winner_text.place(relx=0.495, rely=0.7)

exit_button = customtkinter.CTkButton(third_frame, text="Quitter le jeu", height=50, width=200,
                                      font=customtkinter.CTkFont(family="Montserrat", size=20, weight="bold"),
                                      hover_color="red", command=quit_confirmation)
exit_button.place(relx=0.3, rely=0.8)

restart_button = customtkinter.CTkButton(third_frame, text="Relancer une partie", height=50, width=200,
                                         font=customtkinter.CTkFont(family="Montserrat", size=20, weight="bold"),
                                         hover_color="green",
                                         command=home_button_event)
restart_button.place(relx=0.6, rely=0.8)

# select default frame
select_frame_by_name("home")

app.mainloop()
