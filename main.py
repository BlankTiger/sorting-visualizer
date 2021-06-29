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
from sorting_algorithms import (
    bubble_sort,
    insert_sort,
    quick_sort,
    shellsort,
    unoptimized_bubble_sort,
)

############################
# main app window settings #
############################

app_window = tk.Tk()
app_window.title("Sorting algorithm visualization")
app_window.iconbitmap("logo.ico")
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
    for _ in range(50):
        random_value = np.random.randint(0, 51)
        data.append(random_value)

    draw_data(data, [col.DARK_BLUE for _ in range(len(data))])


def draw_data(data, colors):
    """Used to draw provided data onto the canvas

    Args:
        data (list): list of integers to be displayed
        colors (list): list of colors used for displaying data
    """

    # checks if it should draw to the canvas, if running is False it means that
    # app should be stopped
    if running is False:
        exit()
    data_canvas.delete("all")
    x_width = data_canvas.winfo_width() / (len(data) + 1)
    canvas_height = data_canvas.winfo_height()
    offset = 6
    spacing = 3
    # normalizes the data by scaling every value to the max value
    normalizedData = [x / max(data) for x in data]

    # this part goes over every data point and creates a rectangle for
    # each of them, size is calculated by scaling to both current width and
    # height of the window
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height * (1 - 0.98 * height)
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        data_canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])

    data_canvas.update()


def get_speed():
    """Returns delay value based on chosen speed

    Returns:
        float: time delay value
    """
    if menu_speed.get() == "slow":
        return 0.5
    elif menu_speed.get() == "medium":
        return 0.2
    elif menu_speed.get() == "realtime":
        return 0
    else:
        return 0.01


def start_sorting():
    """This will start sorting the displayed data using the chosen algo"""
    global data
    time_delay = get_speed()

    if menu_algo.get() == "Bubble sort":
        bubble_sort(data, draw_data, time_delay)

    elif menu_algo.get() == "Unoptimized Bubble sort":
        unoptimized_bubble_sort(data, draw_data, time_delay)

    elif menu_algo.get() == "Quicksort":
        quick_sort(data, 0, len(data) - 1, draw_data, time_delay)

    elif menu_algo.get() == "Shellsort":
        shellsort(data, draw_data, time_delay)

    elif menu_algo.get() == "Insert sort":
        insert_sort(data, draw_data, time_delay)


##################################
# objects displayed in the frame #
##################################

# data used to fill the objects created below
algorithm_list = [
    "Bubble sort",
    "Unoptimized Bubble sort",
    "Quicksort",
    "Shellsort",
    "Insert sort",
]
sorting_speeds = ["slow", "medium", "fast", "realtime"]

# everything related to choosing an algorithm
algorithm_name = tk.StringVar()

label_algo = tk.Label(
    main_frame, text="Algorithm: ", fg=col.WHITE, bg=col.BLACK
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
    main_frame, text="Sorting speed: ", fg=col.WHITE, bg=col.BLACK
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
    main_frame,
    text="Sort",
    command=start_sorting,
    bg=col.LIGHT_GRAY,
)
sort_button.grid(row=2, column=2, padx=5, pady=5)

# canvas that will be filled with random data, sorted data is displayed in
# realtime in this canvas
data_canvas = tk.Canvas(main_frame, bg=col.DARK_GRAY)
data_canvas.grid(
    row=3, column=0, columnspan=4, sticky=(tk.N, tk.S, tk.E, tk.W)
)


# snippet used to control closing of the app
running = True


def destroy_window():
    global running
    running = False
    exit()


# defining how the app should behave when user clicks the "X" button
app_window.protocol("WM_DELETE_WINDOW", destroy_window)

# start of the main loop of the application
app_window.mainloop()
