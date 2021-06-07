"""
@authors:
- Małgorzata Kufel,
- Karolina Urbaniak,
- Maciej Urban
"""

import tkinter as tk
from tkinter import ttk
import numpy as np
import colors as col
from sorting_algorithms import bubble_sort

############################
# main app window settings #
############################

app_window = tk.Tk()
app_window.title("Sorting algorithm visualization")
app_window.geometry("800x600")
app_window.config(bg=col.WHITE)
app_window.resizable(1, 1)

# configure the grid of the app window
app_window.columnconfigure(0, weight=1)
app_window.rowconfigure(0, weight=1)

# main frame of the application embedded directly into app_window and its grid
# settings
main_frame = tk.Frame(app_window, bg=col.BLACK)
main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=18)
main_frame.columnconfigure(0, weight=5)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=5)


###########################################################
# functions used to manipulate the data in the app window #
###########################################################

def generate_data():
    """Used to generate and draw a random list of integers to sort onto
    canvas"""

    global data
    data = []
    for i in range(50):
        random_value = np.random.randint(0, 150)
        data.append(random_value)

    draw_data(data, [col.DARK_BLUE for x in range(len(data))])


def draw_data(data, colors):
    """Used to draw provided data onto the canvas

    Args:
        data (list): list of integers to be displayed
        colors (list): list of colors used for displaying data
    """
    data_canvas.delete("all")
    x_width = data_canvas.winfo_width() / (len(data) + 1)
    canvas_height = data_canvas.winfo_height()
    offset = 4
    spacing = 2
    # normalizes the data by scaling every value to the max value
    normalizedData = [x / max(data) for x in data]

    # this part goes over every every data point and creates a rectangle for
    # each of them, size is calculated by scaling to both current width and
    # height of the window
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height * (1 - 0.95 * height)
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        data_canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])

    app_window.update_idletasks()


def get_speed():
    """Returns delay value based on chosen speed

    Returns:
        float: time delay value
    """
    if menu_speed.get() == "slow":
        return 0.5
    elif menu_speed.get() == "medium":
        return 0.2
    else:
        return 0.01


def start_sorting():
    """This will start sorting the displayed data using the chosen algo"""
    global data
    time_delay = get_speed()

    if menu_algo.get() == "Bubble sort":
        bubble_sort(data, draw_data, time_delay)


#######################################
# objects displayed in the app window #
#######################################

# data used to fill the objects created below
algorithm_list = ["Bubble sort", "Quicksort"]
sorting_speeds = ["slow", "medium", "fast"]

# everything related to choosing choosing
algorithm_name = tk.StringVar()

label_algo = tk.Label(
    main_frame, text="Algorithm: ", fg=col.BLACK, bg=col.WHITE
)
label_algo.grid(row=0, column=1, padx=10, pady=5)
menu_algo = ttk.Combobox(
    main_frame, textvariable=algorithm_name, values=algorithm_list
)
menu_algo.grid(row=0, column=2, padx=5, pady=5)
menu_algo.current(0)

# everything related to choosing speed
algorithm_speed_name = tk.StringVar()

label_speed = tk.Label(
    main_frame, text="Sorting speed: ", fg=col.BLACK, bg=col.WHITE
)
label_speed.grid(row=1, column=1, padx=10, pady=5, sticky=tk.N)
menu_speed = ttk.Combobox(
    main_frame, textvariable=algorithm_speed_name, values=sorting_speeds
)
menu_speed.grid(row=1, column=2, padx=5, pady=5, sticky=tk.N)
menu_speed.current(1)

# button used to generate and display the generated data
generate_data_button = tk.Button(
    main_frame, text="Generate data", command=generate_data, bg=col.LIGHT_GRAY
)
generate_data_button.grid(row=2, column=1, padx=5, pady=5)

# button used to start the sorting process
sort_button = tk.Button(
    main_frame, text="Sort", command=start_sorting, bg=col.LIGHT_GRAY
)
sort_button.grid(row=2, column=2, padx=5, pady=5)

# canvas that will be filled with random data, sorted data is displayed in
# realtime in this canvas
data_canvas = tk.Canvas(main_frame, bg=col.DARK_GRAY)
data_canvas.grid(
    row=3, column=0, columnspan=4, sticky=(tk.N, tk.S, tk.E, tk.W)
)
data_canvas.update()

# start of the main loop of the application
app_window.mainloop()
