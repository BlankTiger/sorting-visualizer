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


def partition(data, start, end, draw_data, time_delay):
    i = start + 1
    pivot = data[start]

    for j in range(start + 1, end + 1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            draw_data(
                data,
                [
                    col.LIGHT_GREEN if x == i or x == j else col.BLUE
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
    if start < end:
        pivot_position = partition(data, start, end, draw_data, time_delay)
        quick_sort(data, start, pivot_position - 1, draw_data, time_delay)
        draw_data(
            data,
            [
                col.PURPLE
                if x >= start and x < pivot_position
                else col.YELLOW
                if x == pivot_position
                else col.PURPLE
                if x > pivot_position and x <= end
                else col.BLUE
                for x in range(len(data))
            ],
        )
        sleep(time_delay)
        quick_sort(data, pivot_position + 1, end, draw_data, time_delay)
        draw_data(
            data,
            [
                col.PURPLE
                if x >= start and x < pivot_position
                else col.YELLOW
                if x == pivot_position
                else col.PURPLE
                if x > pivot_position and x <= end
                else col.BLUE
                for x in range(len(data))
            ],
        )
        sleep(time_delay)

    draw_data(data, [col.BLUE for x in range(len(data))])


def shellsort(data, draw_data, time_delay):
    """Shellsort with a modification that allows
    drawing of the sorted data in realtime with a specified delay

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
                data[j] = data[j - br]
                j -= br
                draw_data(
                    data,
                    [
                        col.LIGHT_GREEN if x == i or x == i + 1 else col.BLUE
                        for x in range(len(data))
                    ],
                )
                sleep(time_delay)
            else:
                draw_data(
                    data,
                    [
                        col.YELLOW if x == i or x == i + 1 else col.BLUE
                        for x in range(len(data))
                    ],
                )
                sleep(time_delay)
            data[j] = temp
            draw_data(
                data,
                [col.RED if x == j else col.BLUE for x in range(len(data))],
            )
            sleep(time_delay)
        br //= 2


def insert_sort(data, draw_data, time_delay):
    """Funkcja sortująca przez wstawianie, która pozwala na rysowanie
    sortowanych danych w czasie rzeczywistym z określonym opóźnieniem.

    Args:
        data (list): lista liczb całkowitych do posortowania
        draw_data (function): funkcja rysująca na płótnie określone dane
        time_delay (float): ilość czasu, ile aplikacja odczeka po każdym etapie
            sortowania
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
                col.RED
                if x == data.index(selected) or x == j + 1
                else col.BLUE
                for x in range(len(data))
            ],
        )
        sleep(time_delay)
