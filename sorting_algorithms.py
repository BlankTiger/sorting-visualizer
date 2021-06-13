"""
@authors:
- Małgorzata Kufel,
- Karolina Urbaniak,
- Maciej Urban
"""
import colors as col
from time import sleep


def bubble_sort(data, draw_data, time_delay):
    """Bubble sort with a modification that allows drawing of the sorted data
    in realtime with a specified delay

    Args:
        data (list): list of random data to sort
        draw_data (function): function that draws the specified data
        time_delay (float): an amount of time that the app will wait for
            between the next sort
    """

    sorted = True
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                sorted = False
                # this uses a passed function from the main app code
                draw_data(
                    data,
                    [
                        col.LIGHT_GREEN if x == j or x == j + 1 else col.BLUE
                        for x in range(len(data))
                    ],
                )
                sleep(time_delay)
            else:
                draw_data(
                    data,
                    [
                        col.YELLOW if x == j or x == j + 1 else col.BLUE
                        for x in range(len(data))
                    ],
                )
                sleep(time_delay)
        if sorted:
            break


def unoptimized_bubble_sort(data, draw_data, time_delay):
    """Bubble sort without optimizations and with a modification that allows
    drawing of the sorted data in realtime with a specified delay

    Args:
        data (list): list of random data to sort
        draw_data (function): function that draws the specified data
        time_delay (float): an amount of time that the app will wait for
            between the next sort
    """
    sorted = True
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                sorted = False
                data[j], data[j + 1] = data[j + 1], data[j]

                # this uses a passed function from the main app code
                draw_data(
                    data,
                    [
                        col.LIGHT_GREEN if x == j or x == j + 1 else col.BLUE
                        for x in range(len(data))
                    ],
                )
                sleep(time_delay)
            else:
                draw_data(
                    data,
                    [
                        col.YELLOW if x == j or x == j + 1 else col.BLUE
                        for x in range(len(data))
                    ],
                )
                sleep(time_delay)
        if sorted:
            break
