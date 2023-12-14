import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Create the main Tkinter window
root = customtkinter.CTk()

# Configure window
root.title("CustomTkinter complex_example.py")
root.geometry(f"{1100}x{580}")

# Configure grid layout (4x4)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)

# Create sidebar frame with widgets
sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)

logo_label = customtkinter.CTkLabel(sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, command=lambda: print("sidebar_button click"))
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, command=lambda: print("sidebar_button click"))
sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, command=lambda: print("sidebar_button click"))
sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

appearance_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"],
                                                          command=lambda mode: customtkinter.set_appearance_mode(mode))
appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

scaling_label = customtkinter.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

scaling_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                  command=lambda scaling: customtkinter.set_widget_scaling(int(scaling.replace("%", "")) / 100))
scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

# Create main entry and button
entry = customtkinter.CTkEntry(root, placeholder_text="CTkEntry")
entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

main_button_1 = customtkinter.CTkButton(master=root, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

# Create textbox
textbox = customtkinter.CTkTextbox(root, width=250)
textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

# Create tabview
tabview = customtkinter.CTkTabview(root, width=250)
tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
tabview.add("CTkTabview")
tabview.add("Tab 2")
tabview.add("Tab 3")
tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

optionmenu_1 = customtkinter.CTkOptionMenu(tabview.tab("CTkTabview"), dynamic_resizing=False,
                                           values=["Value 1", "Value 2", "Value Long Long Long"])
optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
combobox_1 = customtkinter.CTkComboBox(tabview.tab("CTkTabview"),
                                       values=["Value 1", "Value 2", "Value Long....."])
combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
string_input_button = customtkinter.CTkButton(tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                              command=lambda: print("Open CTkInputDialog"))
string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
label_tab_2 = customtkinter.CTkLabel(tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
label_tab_2.grid(row=0, column=0, padx=20, pady=20)

# Create radiobutton frame
radiobutton_frame = customtkinter.CTkFrame(root)
radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

radio_var = tkinter.IntVar(value=0)
label_radio_group = customtkinter.CTkLabel(master=radiobutton_frame, text="CTkRadioButton Group:")
label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")

radio_button_1 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=0)
radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

radio_button_2 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=1)
radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

radio_button_3 = customtkinter.CTkRadioButton(master=radiobutton_frame, variable=radio_var, value=2)
radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

# Create slider and progressbar frame
slider_progressbar_frame = customtkinter.CTkFrame(root, fg_color="transparent")
slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
slider_progressbar_frame.grid_columnconfigure(0, weight=1)
slider_progressbar_frame.grid_rowconfigure(4, weight=1)

seg_button_1 = customtkinter.CTkSegmentedButton(slider_progressbar_frame)
seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

progressbar_1 = customtkinter.CTkProgressBar(slider_progressbar_frame)
progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

progressbar_2 = customtkinter.CTkProgressBar(slider_progressbar_frame)
progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

slider_1 = customtkinter.CTkSlider(slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

slider_2 = customtkinter.CTkSlider(slider_progressbar_frame, orientation="vertical")
slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")

progressbar_3 = customtkinter.CTkProgressBar(slider_progressbar_frame, orientation="vertical")
progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

# Create scrollable frame
scrollable_frame = customtkinter.CTkScrollableFrame(root, label_text="CTkScrollableFrame")
scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
scrollable_frame.grid_columnconfigure(0, weight=1)

scrollable_frame_switches = []
for i in range(100):
    switch = customtkinter.CTkSwitch(master=scrollable_frame, text=f"CTkSwitch {i}")
    switch.grid(row=i, column=0, padx=10, pady=(0, 20))
    scrollable_frame_switches.append(switch)

# Create checkbox and switch frame
checkbox_slider_frame = customtkinter.CTkFrame(root)
checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

checkbox_1 = customtkinter.CTkCheckBox(master=checkbox_slider_frame)
checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")

checkbox_2 = customtkinter.CTkCheckBox(master=checkbox_slider_frame)
checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")

checkbox_3 = customtkinter.CTkCheckBox(master=checkbox_slider_frame)
checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

# Set default values
sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
checkbox_3.configure(state="disabled")
checkbox_1.select()
scrollable_frame_switches[0].select()
scrollable_frame_switches[4].select()
radio_button_3.configure(state="disabled")
string_input_button.configure(command=lambda: print("Open CTkInputDialog"))
optionmenu_1.set("CTkOptionmenu")
combobox_1.set("CTkComboBox")

slider_1.configure(command=progressbar_2.set)
slider_2.configure(command=progressbar_3.set)

progressbar_1.configure(mode="indeterminate")
progressbar_1.start()

textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
seg_button_1.set("Value 2")

# Main loop
root.mainloop()
