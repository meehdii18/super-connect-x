import os
import tkinter as tk
import customtkinter
from PIL import Image


app = customtkinter.CTk()
app.title("SUPER CONNECT X")
app.geometry("1050x675")
app.resizable(False, False)

def select_frame_by_name(name):
    # set button color for selected button
    home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
    frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

    # show selected frame
    if name == "home":
        home_frame.grid(row=1, column=0, sticky="nsew")  # Change column to 0
    else:
        home_frame.grid_forget()
    if name == "frame_2":
        second_frame.grid(row=1, column=0, sticky="nsew")  # Change column to 0
    else:
        second_frame.grid_forget()
    if name == "frame_3":
        third_frame.grid(row=1, column=0, sticky="nsew")  # Change column to 0
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


# Base theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# set grid layout 1x2

app.grid_rowconfigure(1, weight=10)
app.grid_columnconfigure(0, weight=1)

# load images with light and dark mode image
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")),
                                    size=(26, 26))
large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
chat_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "game.png")), size=(20, 20))
add_user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "end.png")), size=(20, 20))

# create navigation frame
navigation_frame = customtkinter.CTkFrame(app, corner_radius=0)
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.configure(height=70)
nav_frame_height = navigation_frame.winfo_reqheight()
app.rowconfigure(0, minsize=nav_frame_height)

navigation_frame_label = customtkinter.CTkLabel(navigation_frame, text="  SUPER CONNECT X", image=logo_image,
                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
navigation_frame_label.grid(row=0, column=0)
navigation_frame_label.place(relx=0.1, rely=0.5, anchor="center")  # Adjust rely as needed

home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="MAIN MENU",
                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                      hover_color=("gray70", "gray30"),
                                      font=customtkinter.CTkFont(size=15, weight="bold"),
                                      image=home_image, anchor="w", command=home_button_event)
home_button.grid(row=0, column=1, sticky="ew")
home_button.place(relx=0.35, rely=0.5, anchor="center")  # Adjust rely as needed

frame_2_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="GAME FRAME",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         font=customtkinter.CTkFont(size=15, weight="bold"),
                                         image=chat_image, anchor="w", command=frame_2_button_event)
frame_2_button.grid(row=0, column=2, sticky="ew")
frame_2_button.place(relx=0.5, rely=0.5, anchor="center")  # Adjust rely as needed

frame_3_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="END MENU",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         font=customtkinter.CTkFont(size=15, weight="bold"),
                                         image=add_user_image, anchor="w", command=frame_3_button_event)
frame_3_button.grid(row=0, column=3, sticky="ew")
frame_3_button.place(relx=0.65, rely=0.5, anchor="center")

appearance_mode_menu = customtkinter.CTkOptionMenu(navigation_frame, values=["System", "Light", "Dark"],
                                                   command=change_appearance_mode_event)
appearance_mode_menu.grid(row=0, column=4, sticky="w")
appearance_mode_menu.place(relx=0.85, rely=0.5, anchor="w")

# Main Menu
home_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
home_frame.grid(row=1, column=0, sticky="nsew")
home_frame.grid_columnconfigure(0, weight=2)

home_frame_large_image_label = customtkinter.CTkLabel(home_frame, text="", image=large_test_image)
home_frame_large_image_label.grid(row=0, column=0, )


var_column = tk.IntVar()
var_row = tk.IntVar()
var_requiredcoins = tk.IntVar()
var_difficulty = tk.IntVar()

home_frame_column_text = customtkinter.CTkLabel(home_frame, text="Nombre de colonnes : ", fg_color="transparent",
                                                font=customtkinter.CTkFont(size=20, weight="bold"))
home_frame_column_text.grid(row=1, column=0)
home_frame_column_text.place(relx=0.32, rely=0.298)
home_frame_column_slider = customtkinter.CTkSlider(home_frame, from_=3,to=10,number_of_steps=8,variable=var_column)
home_frame_column_slider.grid(row=1, column=0)
home_frame_column_slider.place(relx=0.55, rely=0.3)
home_frame_column_slider.set(7)
home_frame_column_val = customtkinter.CTkLabel(home_frame, textvariable=var_column, fg_color="transparent")
home_frame_column_val.grid(row=1, column=0)
home_frame_column_val.place(relx=0.6425, rely=0.25)


home_frame_row_text = customtkinter.CTkLabel(home_frame, text="Nombre de lignes : ", fg_color="transparent",
                                             font=customtkinter.CTkFont(size=20, weight="bold"))
home_frame_row_text.grid(row=1, column=0)
home_frame_row_text.place(relx=0.35, rely=0.398)
home_frame_row_slider = customtkinter.CTkSlider(home_frame,from_=3,to=10,number_of_steps=8,variable=var_row)
home_frame_row_slider.grid(row=1, column=0)
home_frame_row_slider.place(relx=0.55, rely=0.4)
home_frame_row_slider.set(6)
home_frame_row_val = customtkinter.CTkLabel(home_frame, textvariable=var_row, fg_color="transparent")
home_frame_row_val.grid(row=1, column=0)
home_frame_row_val.place(relx=0.6425, rely=0.35)


home_frame_coins_text = customtkinter.CTkLabel(home_frame, text="Nombre de jetons pour gagner : ",
                                               fg_color="transparent",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
home_frame_coins_text.grid(row=1, column=0)
home_frame_coins_text.place(relx=0.235, rely=0.498)


home_frame_coins_slider = customtkinter.CTkSlider(home_frame, from_=3, to=10,
                                                  number_of_steps=8, variable=var_requiredcoins)
home_frame_coins_slider.grid(row=1, column=0)
home_frame_coins_slider.place(relx=0.55, rely=0.5)
home_frame_coins_slider.set(4)
home_frame_coins_val = customtkinter.CTkLabel(home_frame, textvariable=var_requiredcoins, fg_color="transparent")
home_frame_coins_val.grid(row=1, column=0)
home_frame_coins_val.place(relx=0.6425, rely=0.45)




home_frame_difficulty_text = customtkinter.CTkLabel(home_frame, text="Difficulté de l'IA :", fg_color="transparent",
                                                    font=customtkinter.CTkFont(size=20, weight="bold"))
home_frame_difficulty_text.grid(row=1, column=0)
home_frame_difficulty_text.place(relx=0.365, rely=0.59)


home_frame_difficulty_slider = customtkinter.CTkSlider(home_frame, from_=1, to=6, number_of_steps=6,
                                                        variable=var_difficulty)
home_frame_difficulty_slider.grid(row=1, column=0)
home_frame_difficulty_slider.place(relx=0.55, rely=0.6)
home_frame_difficulty_slider.set(3)
home_frame_difficulty_val = customtkinter.CTkLabel(home_frame, textvariable=var_difficulty, fg_color="transparent")
home_frame_difficulty_val.grid(row=1, column=0)
home_frame_difficulty_val.place(relx=0.6425, rely=0.55)

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
player1_color_menu.place(relx=0.555, rely=0.68)  # Adjust position as needed

player2_color_menu = customtkinter.CTkOptionMenu(home_frame, values=available_colors, variable=player2_color)
player2_color_menu.grid(row=1, column=0)
player2_color_menu.place(relx=0.555, rely=0.75)  # Adjust position as needed

player1_color_menu_text = customtkinter.CTkLabel(home_frame, text="Couleur du joueur :", fg_color="transparent",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
player1_color_menu_text.grid(row=1, column=0)
player1_color_menu_text.place(relx=0.35, rely=0.68)

player2_color_menu_text = customtkinter.CTkLabel(home_frame, text="Couleur de l'ordinateur :", fg_color="transparent",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
player2_color_menu_text.grid(row=1, column=0)
player2_color_menu_text.place(relx=0.305, rely=0.75)

# Game Frame
second_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

# End Menu
third_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

# select default frame
select_frame_by_name("home")

app.mainloop()
