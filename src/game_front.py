import os
import customtkinter
import pyglet
from CTkMessagebox import CTkMessagebox
from PIL import Image

from game_console import init, add_coin, check_valid_play, check_victory, min_max, use_perk, undo, check_full_grid

# Initialize the application
app = customtkinter.CTk()

# Set the title of the application
app.title("SUPER CONNECT X")

# Set the geometry of the application
app.geometry("1080x720")

# Set the resizable property of the application
app.resizable(False, False)


def select_frame_by_name(name):
    """
    Function to select a frame by its name.
    It sets the button color for the selected button and shows the selected frame.

    Parameters:
    name (str): The name of the frame to be selected.
    """
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
    """
    Function to handle the event when the home button is clicked.
    It selects the home frame.
    """
    select_frame_by_name("home")


def frame_2_button_event():
    """
    Function to handle the event when the frame 2 button is clicked.
    It selects the frame 2.
    """
    select_frame_by_name("frame_2")


def frame_3_button_event():
    """
    Function to handle the event when the frame 3 button is clicked.
    It selects the frame 3.
    """
    select_frame_by_name("frame_3")


def change_appearance_mode_event(new_appearance_mode):
    """
    Function to handle the event when the appearance mode is changed.
    It sets the appearance mode to the new mode.

    Parameters:
    new_appearance_mode (str): The new appearance mode to be set.
    """
    customtkinter.set_appearance_mode(new_appearance_mode)


def launch_confirmation():
    """
    Function to handle the event when the game is about to be launched.
    It shows a confirmation message box and if the user confirms, it starts the game.
    """
    launch = CTkMessagebox(title="Lancer une partie",
                           message="Voulez-vous lancez la partie avec les paramètres séléctionnés ?",
                           option_1="Non", option_2="Oui", sound=False, corner_radius=20)
    if launch.get() == "Oui":
        frame_2_button_event()
        start_game()


def quit_confirmation():
    """
    Function to handle the event when the game is about to be quit.
    It shows a confirmation message box and if the user confirms, it quits the game.
    """
    end_game = CTkMessagebox(title="Quitter le jeu", message="Voulez-vous vraiment quitter le jeu ?", icon="warning",
                             option_1="Oui", option_2="Non", sound=False)
    if end_game.get() == "Oui":
        app.destroy()


def start_game():
    """
    Function to start the game.
    It destroys the previous game canvas and buttons, and initializes a new game with the selected parameters.
    """
    global buttons
    try:
        game_canvas.destroy()
        for button in buttons:
            button.destroy()
        buttons = []
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
    """
    Function to display the game board.
    It creates the game board on the canvas with the given parameters.

    Parameters:
    canvas (CTkCanvas): The canvas to display the game board on.
    game_board (list): The game board to be displayed.
    player1_color (str): The color of the player 1's coins.
    player2_color (str): The color of the player 2's coins.
    cell_size (int, optional): The size of each cell. Defaults to 70.
    padding (int, optional): The padding around each cell. Defaults to 10.
    """
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
                                               hover_color=player1_color,
                                               command=lambda col=i: button_event(col)))
        buttons[i].grid(row=0, column=i, padx=(4, 4))


def button_event_turn(number, game_state):
    """
    Function to handle the event when a button is clicked.
    It checks if the play is valid, adds the coin, checks for victory, and advances the game.

    Parameters:
    number (int): The number of the button that was clicked.
    game_state (list): The current state of the game.
    """
    if check_valid_play(number, game_state[0]):
        game_state[0] = add_coin(number, 1, game_state[0])
        game_advance.append(game_state)
        if check_victory(var_requiredcoins.get(), game_state[0]) == 1:
            win(1)
        else:
            value = min_max(game_state, var_requiredcoins.get(), var_difficulty.get(), True)
            ai_col = value[0]
            if (ai_col == "perk"):
                if game_state[1][1] != True :
                    game_state = use_perk(game_state)
                    game_state[1][1] = True
            else:
                game_state[0] = add_coin(ai_col, 2, game_state[0])
            game_state[2] = 1
            game_advance.append(game_state)
        if check_victory(var_requiredcoins.get(), game_state[0]) == 2:
            win(2)
        if check_full_grid(game_state[0], (True, True)):
            win(0)
    else:
        impossible_move_event()


def button_event(number):
    """
    Function to handle the event when a button is clicked.
    It calls the button_event_turn function with the number of the button that was clicked.

    Parameters:
    number (int): The number of the button that was clicked.
    """
    global game_state
    global game_advance
    global undo_button

    undo_button.configure(state="enabled")
    if number == 0:
        button_event_turn(0, game_state)

    elif number == 1:
        button_event_turn(1, game_state)

    elif number == 2:
        button_event_turn(2, game_state)

    elif number == 3:
        button_event_turn(3, game_state)

    elif number == 4:
        button_event_turn(4, game_state)

    elif number == 5:
        button_event_turn(5, game_state)

    elif number == 6:
        button_event_turn(6, game_state)

    elif number == 7:
        button_event_turn(7, game_state)

    display_game_board(game_canvas, game_state[0], player1_color.get(), player2_color.get())


def initialize_game(columns, rows, required_coins, difficulty, player1_color, player2_color):
    """
    Function to initialize the game.
    It creates the game board and sets the initial game state.

    Parameters:
    columns (int): The number of columns in the game board.
    rows (int): The number of rows in the game board.
    required_coins (int): The number of coins required to win.
    difficulty (int): The difficulty level of the game.
    player1_color (str): The color of the player 1's coins.
    player2_color (str): The color of the player 2's coins.
    """
    global game_canvas
    global game_state
    global game_advance
    global undo_button

    game_board = init(columns, rows)
    game_state = [game_board, [False, False], 1]
    game_advance = [game_state]
    game_canvas = customtkinter.CTkCanvas(second_frame, width=columns * 70, height=rows * 70,
                                          background="#201c24", borderwidth=0)
    game_canvas.grid(row=0, column=0, sticky="nsew")
    game_canvas.place(relx=0.5, rely=0.55, anchor="center")

    perk_button = customtkinter.CTkButton(second_frame, text="Atout",
                                          command=lambda: perk_button_event(game_state, perk_button),
                                          height=50,
                                          font=customtkinter.CTkFont(family="Montserrat", size=25, weight="bold"))
    perk_button.place(relx=0.04, rely=0.9)

    undo_button = customtkinter.CTkButton(second_frame, text="Undo", height=50, command=undo_event, state="disabled",
                                          font=customtkinter.CTkFont(family="Montserrat", size=25, weight="bold"))
    undo_button.place(relx=0.85, rely=0.9)

    display_game_board(game_canvas, game_state[0], player1_color, player2_color)

    print("| NEW GAME STARTED | Columns :", columns, " Rows:", rows, " Required coins:", required_coins, " Difficulty:",
          difficulty,
          " Player color:", player1_color, " AI color:", player2_color)


def undo_event():
    """
    Function to handle the event when the undo button is clicked.
    It undoes the last move and updates the game board.
    """
    global game_advance
    undo(game_advance)
    print(game_advance)
    display_game_board(game_canvas, game_advance[-1][0], player1_color.get(), player2_color.get())


def impossible_move_event():
    """
    Function to handle the event when an impossible move is attempted.
    It shows a message box informing the user that the move is impossible.
    """
    message = CTkMessagebox(title="Jeton impossible à placer",
                            message="La colonne est remplie, veuillez en choisir une autre pour jouer.",
                            option_1="Compris", sound=False, corner_radius=20)


def perk_button_event(game_board, button):
    """
    Function to handle the event when the perk button is clicked.
    It shows a message box asking the user if they want to use the perk.
    If the user confirms, it uses the perk and updates the game board.

    Parameters:
    game_board (list): The current game board.
    button (CTkButton): The perk button.
    """
    global game_advance
    perk_msg = CTkMessagebox(title="Utiliser l'atout",
                             message="L'atout va supprimer les jetons de la ligne du bas, attention il ne peut être utilisé"
                                     "qu'une seule fois par partie",
                             option_1="Non", option_2="Oui", sound=False, corner_radius=20)
    if perk_msg.get() == "Oui":
        game_state = use_perk(game_board)
        game_advance.append(game_state)
        display_game_board(game_canvas, game_advance[-1], player1_color.get(), player2_color.get())
        button.configure(state="disabled")
        print("L'atout a été utilisé.")


def win(winner):
    """
    Function to handle the win of the game.
    It create a text for the annoucement on the last frame and select it.

    Parameters:
    winner (int): The winner of the game or 0.
    """
    global game_advance
    frame_3_button_event()
    if winner == 1:
        winner_text.configure(text="Vous avez gagné !", text_color="green")
        winner_text.place(relx=0.465, rely=0.7)
    if winner == 2:
        winner_text.configure(text="Vous avez perdu, l'IA à gagné !", text_color="red")
        winner_text.place(relx=0.434, rely=0.7)
    if winner == 0:
        winner_text.configure(text="Egalité!", text_color="orange")
        winner_text.place(relx=0.48, rely=0.7)


"""
Set base theme to dark
"""
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

"""
Load font for the interface
"""
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'Montserrat-Bold.ttf')
pyglet.font.add_file(font_path)
custom_font = customtkinter.CTkFont(family="Montserrat", size=20)

app.grid_rowconfigure(1, weight=10)
app.grid_columnconfigure(0, weight=1)

"""
Load image for the interface
"""
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(40, 40))
banner_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(650, 195))
home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
chat_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "game.png")), size=(20, 20))
add_user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "end.png")), size=(20, 20))
start_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "start.png")), size=(50, 50))

"""
Create navigation frame which show what frame are we in
"""
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

home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="MENU",
                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                      hover_color=("gray70", "gray30"),
                                      font=customtkinter.CTkFont(family="Montserrat", size=15, weight="bold"),
                                      image=home_image, anchor="w")
home_button.grid(row=0, column=1, sticky="ew")
home_button.place(relx=0.35, rely=0.5, anchor="center")

frame_2_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="JEU",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         font=customtkinter.CTkFont(family="Montserrat", size=15, weight="bold"),
                                         image=chat_image, anchor="w")
frame_2_button.grid(row=0, column=2, sticky="ew")
frame_2_button.place(relx=0.5, rely=0.5, anchor="center")

frame_3_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="FIN DE PARTIE",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         font=customtkinter.CTkFont(family="Montserrat", size=15, weight="bold"),
                                         image=add_user_image, anchor="w")
frame_3_button.grid(row=0, column=3, sticky="ew")
frame_3_button.place(relx=0.65, rely=0.5, anchor="center")

appearance_mode_menu = customtkinter.CTkOptionMenu(navigation_frame, values=["Dark", "Light", "System"],
                                                   command=change_appearance_mode_event)
appearance_mode_menu.grid(row=0, column=4, sticky="w")
appearance_mode_menu.place(relx=0.85, rely=0.5, anchor="w")

"""
Create the main menu frame where we select all the settings for the game and start it
"""
home_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
home_frame.grid(row=1, column=0, sticky="nsew")
home_frame.grid_columnconfigure(0, weight=2)

home_frame_large_image_label = customtkinter.CTkLabel(home_frame, text="", image=banner_image)
home_frame_large_image_label.grid(row=0, column=0)
home_frame_large_image_label.place(relx=0.2, rely=-0.025)

var_column = customtkinter.IntVar()
var_row = customtkinter.IntVar()
var_requiredcoins = customtkinter.IntVar()
var_difficulty = customtkinter.IntVar()

home_frame_column_text = customtkinter.CTkLabel(home_frame, text="Nombre de colonnes : ", fg_color="transparent",
                                                font=customtkinter.CTkFont(family="Montserrat", size=20, weight="bold"))
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
                                             font=customtkinter.CTkFont(family="Montserrat", size=20, weight="bold"))
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
                                               font=customtkinter.CTkFont(family="Montserrat", size=20, weight="bold"))
home_frame_coins_text.grid(row=1, column=0)
home_frame_coins_text.place(relx=0.235, rely=0.498 + 0.03)

home_frame_coins_slider = customtkinter.CTkSlider(home_frame, from_=3, to=5,
                                                  number_of_steps=8, variable=var_requiredcoins)
home_frame_coins_slider.grid(row=1, column=0)
home_frame_coins_slider.place(relx=0.55, rely=0.5 + 0.03)
home_frame_coins_slider.set(4)
home_frame_coins_val = customtkinter.CTkLabel(home_frame, textvariable=var_requiredcoins, fg_color="transparent")
home_frame_coins_val.grid(row=1, column=0)
home_frame_coins_val.place(relx=0.6425, rely=0.45 + 0.03)

home_frame_difficulty_text = customtkinter.CTkLabel(home_frame, text="Difficulté de l'IA :", fg_color="transparent",
                                                    font=customtkinter.CTkFont(family="Montserrat", size=20,
                                                                               weight="bold"))
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

# Create var for player color choices
player1_color = customtkinter.StringVar()
player2_color = customtkinter.StringVar()

# Set default color
player1_color.set(available_colors[0])
player2_color.set(available_colors[1])

# Create menu for player color choices
player1_color_menu = customtkinter.CTkOptionMenu(home_frame, values=available_colors, variable=player1_color)
player1_color_menu.grid(row=1, column=0)
player1_color_menu.place(relx=0.555, rely=0.68 + 0.03)  # Adjust position as needed

player2_color_menu = customtkinter.CTkOptionMenu(home_frame, values=available_colors, variable=player2_color)
player2_color_menu.grid(row=1, column=0)
player2_color_menu.place(relx=0.555, rely=0.75 + 0.03)  # Adjust position as needed

player1_color_menu_text = customtkinter.CTkLabel(home_frame, text="Couleur du joueur :", fg_color="transparent",
                                                 font=customtkinter.CTkFont(family="Montserrat", size=20,
                                                                            weight="bold"))
player1_color_menu_text.grid(row=1, column=0)
player1_color_menu_text.place(relx=0.35, rely=0.68 + 0.03)

player2_color_menu_text = customtkinter.CTkLabel(home_frame, text="Couleur de l'ordinateur :", fg_color="transparent",
                                                 font=customtkinter.CTkFont(family="Montserrat", size=20,
                                                                            weight="bold"))
player2_color_menu_text.grid(row=1, column=0)
player2_color_menu_text.place(relx=0.305, rely=0.75 + 0.03)

home_frame_start_button = customtkinter.CTkButton(home_frame, text="", image=start_image, fg_color="transparent",
                                                  command=launch_confirmation, hover=False)
home_frame_start_button.grid(row=1, column=0)
home_frame_start_button.place(relx=0.46, rely=0.86)

"""
Create game frame (all the labels and canvas are handled in functions above)
"""
second_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

"""
Create end game frame where it shows the winner and buttons to restart / quit the game
"""
third_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

gamer_over_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "game_over.png")), size=(600, 360))
game_over_label = customtkinter.CTkLabel(third_frame, text="", image=gamer_over_image, fg_color="transparent")
game_over_label.place(relx=0.25, rely=0.1)

winner_text = customtkinter.CTkLabel(third_frame, text="X à gagné !", fg_color="transparent",
                                     font=customtkinter.CTkFont(family="Montserrat", size=20))
winner_text.grid(row=1, column=0)

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
