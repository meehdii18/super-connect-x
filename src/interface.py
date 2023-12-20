import customtkinter
import os
import platform
from PIL import Image


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


app = customtkinter.CTk()
app.title("SUPER CONNECT X")
app.geometry("1050x675")
app.resizable(False, False)

# Base theme
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

"""
if(platform.system() == "Windows"):
    import pywinstyles
    pywinstyles.apply_style(app, acrylic)
"""

# set grid layout 1x2

app.grid_rowconfigure(1, weight=10)
app.grid_columnconfigure(0, weight=1)

# load images with light and dark mode image
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")),
                                    size=(26, 26))
large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
chat_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "game.png")), size=(20, 20))
add_user_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "end.png")),size=(20, 20))

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
                                      image=home_image, anchor="w", command=home_button_event)
home_button.grid(row=0, column=1, sticky="ew")
home_button.place(relx=0.35, rely=0.5, anchor="center")  # Adjust rely as needed



frame_2_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="GAME FRAME",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=chat_image, anchor="w", command=frame_2_button_event)
frame_2_button.grid(row=0, column=2, sticky="ew")
frame_2_button.place(relx=0.5, rely=0.5, anchor="center")  # Adjust rely as needed

frame_3_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="END MENU",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=add_user_image, anchor="w", command=frame_3_button_event)
frame_3_button.grid(row=0, column=3, sticky="ew")
frame_3_button.place(relx=0.65, rely=0.5, anchor="center")  # Adjust rely as needed



appearance_mode_menu = customtkinter.CTkOptionMenu(navigation_frame, values=["Dark", "Light", "System"],
                                                   command=change_appearance_mode_event)
appearance_mode_menu.grid(row=0, column=4, sticky="w")
appearance_mode_menu.place(relx=0.85, rely=0.5, anchor="w")  # Adjust rely as needed


# Main Menu
home_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
home_frame.grid(row=1, column=0, sticky="nsew")  # Change row to 0
home_frame.grid_columnconfigure(0, weight=2)

home_frame_large_image_label = customtkinter.CTkLabel(home_frame, text="", image=large_test_image)
home_frame_large_image_label.grid(row=0, column=0,)

home_frame_button_1 = customtkinter.CTkButton(home_frame, text="", image=image_icon_image)
home_frame_button_1.grid(row=1, column=0)


# Game Frame
second_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

# End Menu
third_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")

# select default frame
select_frame_by_name("home")

app.mainloop()
