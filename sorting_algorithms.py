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

    Color information:
    - rectangles that are swapped are shown as green,
    - rectangles that are just checked are shown as yellow.

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

    Color information:
    - rectangles that are swapped are shown as green,
    - rectangles that are just checked are shown as yellow.


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


def partition(data, start, end, draw_data, time_delay):
    """Function that serves the purpose of partitioning the provided list of
    random numbers to sort

    Color information:
    - rectangles that are swapped are light green.

    Args:
        data (list): list of random data to sort
        start (int): index of the first item we want to get pivot from
        end (int): index of the last item we want to get pivot from
        draw_data (function): function that allows for data drawing onto the
            canvas
        time_delay (float): an amount of time that the app will wait for
            between the next sort

    Returns:
        int: index of the number by which the list will be split in quicksort
    """
    i = start + 1
    pivot = data[start]

    for j in range(start + 1, end + 1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            draw_data(
                data,
                [
                    col.RED
                    if x == start
                    else col.LIGHT_GREEN
                    if x == i + 1 or x == j
                    else col.PURPLE
                    if x > start and x <= end
                    else col.BLUE
                    for x in range(len(data))
                ],
            )
            sleep(time_delay)
            i += 1

    data[start], data[i - 1] = data[i - 1], data[start]
    draw_data(
        data,
        [
            col.LIGHT_GREEN if x == start or x == i - 1 else col.BLUE
            for x in range(len(data))
        ],
    )
    sleep(time_delay)

    return i - 1


def quick_sort(data, start, end, draw_data, time_delay):
    """Quicksort function with a modification that allows for drawing of the
    sorted data onto the canvas

    Color information:
    - rectangles that are swapped are light green,
    - to the left and to the right of the pivot in the partitioned list,
      rectangles are yellow,
    - rectangle that represents the pivot is red.

    Args:
        data (list): list of random data to sort
        start (int): index of the first item from which we want to sort
        end (int): index of the last item we want to sort
        draw_data (function): function that allows for data drawing onto the
            canvas
        time_delay (float): an amount of time that the app will wait for
            between the next sort

    Returns:
        int: index of the number by which the list will be split in quicksort
    """
    if start < end:
        pivot_position = partition(data, start, end, draw_data, time_delay)
        draw_data(
            data,
            [
                col.YELLOW
                if x >= start and x < pivot_position
                else col.RED
                if x == pivot_position
                else col.YELLOW
                if x > pivot_position and x <= end
                else col.BLUE
                for x in range(len(data))
            ],
        )
        sleep(time_delay)
        quick_sort(data, start, pivot_position - 1, draw_data, time_delay)
        draw_data(
            data,
            [
                col.YELLOW
                if x >= pivot_position + 1 and x < end
                else col.RED
                if x == pivot_position
                else col.YELLOW
                if x < pivot_position
                else col.BLUE
                for x in range(len(data))
            ],
        )
        sleep(time_delay)
        quick_sort(data, pivot_position + 1, end, draw_data, time_delay)
    # draw_data(data, [col.BLUE for x in range(len(data))])
    draw_data(data, list(map(lambda x: col.BLUE, data)))


def shellsort(data, draw_data, time_delay):
    """Shellsort with a modification that allows
    drawing of the sorted data in realtime with a specified delay

    Color information:
    - rectangles that are swapped are light green,
    - if rectangles are just checked they appear as yellow,
    - when we write down the temp back into the data it appears as red.

    Args:
        data (list): list of random data to sort
        draw_data (function): function that draws the specified data
        time_delay (float): an amount of time that the app will wait for
            between the next sort
    """

    br = len(data) // 2  # gap
    while br > 0:
        for i in range(br, len(data)):
            temp = data[i]
            j = i
            while br <= j and data[j - br] > temp:
                draw_data(
                    data,
                    [
                        col.LIGHT_GREEN if x == i or x == i + 1 else col.BLUE
                        for x in range(len(data))
                    ],
                )
                sleep(time_delay)
                data[j] = data[j - br]
                j -= br

            draw_data(
                data,
                [col.RED if x == j else col.BLUE for x in range(len(data))],
            )
            sleep(time_delay)
            data[j] = temp
        br //= 2


def insert_sort(data, draw_data, time_delay):
    """Insert sort algorithm with a modification that allows drawing of the
    sorted data in realtime with specified time delay

    Color information:
    - selected value appears as pink when first chosen,
    - rectangles that are swapped are light green,
    - when we plug selected rectangle back it appears as red.

    Args:
        data (list): list of random data to sort
        draw_data (function): function that draws the specified data
        time_delay (float): an amount of time that the app will wait for
            between the next sort
    """

    for i in range(1, len(data)):

        selected = data[i]

        draw_data(
            data,
            [
                col.PINK if x == data.index(selected) else col.BLUE
                for x in range(len(data))
            ],
        )
        sleep(time_delay)

        j = i - 1
        while j >= 0 and selected < data[j]:
            data[j + 1] = data[j]
            draw_data(
                data,
                [
                    col.LIGHT_GREEN if x == j or x == j + 1 else col.BLUE
                    for x in range(len(data))
                ],
            )
            sleep(time_delay)
            j -= 1
        data[j + 1] = selected
        draw_data(
            data,
            [
                col.RED if x == data.index(selected) else col.BLUE
                for x in range(len(data))
            ],
        )
        sleep(time_delay)
