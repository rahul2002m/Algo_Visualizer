import time
from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Algo Visualizer')
root.geometry('855x550')
root.config(bg='grey')

algo_var = StringVar()
srch = StringVar()
data = []

#_____________________________________________ Draw data ___________________________________________________#


def drdata(data, clr):
    canva.delete('all')
    ch = 380
    cw = 800
    xw = cw / (len(data) + 1)
    ofs = 30
    sp = 10
    n = [i / max(data) for i in data]
    for i, h in enumerate(n):
        x0 = i * xw + ofs + sp
        y0 = ch - h * 320
        x1 = (i + 1) * xw + ofs
        y1 = ch

        canva.create_rectangle(x0, y0, x1, y1, fill=clr[i])
        canva.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


#__________________________________________________ Draw data ___________________________________________________#

#__________________________________________________  Generate  ________________________________________________#


def gen():
    global data
    minv = int(minen.get())
    maxv = int(maxen.get())
    size = int(sizen.get())
    data = []
    for i in range(size):
        data.append(random.randrange(minv, maxv + 1))
    drdata(data, ['red' for i in range(len(data))])


#__________________________________________________  Generate  ________________________________________________#

#_________________________________________________ Merge Sort ____________________________________________________#


def mergesort(data, drdata, speed):
    merge_sort(data, 0, len(data) - 1, drdata, speed)


def merge_sort(data, l, r, drdata, speed):
    if l < r:
        mid = (l + r) // 2
        merge_sort(data, l, mid, drdata, speed)
        merge_sort(data, mid + 1, r, drdata, speed)
        merge(data, l, mid, r, drdata, speed)


def merge(data, l, mid, r, drdata, speed):
    drdata(data, clrar(len(data), l, mid, r))
    time.sleep(speed)
    left_data = data[l:mid + 1]
    right_data = data[mid + 1:r + 1]

    li = ri = 0
    for i in range(l, r + 1):
        if li < len(left_data) and ri < len(right_data):
            if left_data[li] <= right_data[ri]:
                data[i] = left_data[li]
                li += 1
            else:
                data[i] = right_data[ri]
                ri += 1
        elif li < len(left_data):
            data[i] = left_data[li]
            li += 1
        else:
            data[i] = right_data[ri]
            ri += 1

    drdata(data, ['green' if l <= c <= r else 'white' for c in range(len(data))])
    time.sleep(speed)


def clrar(n, l, mid, r):
    clr = []
    for i in range(n):
        if l <= i <= r:
            if l <= i <= mid:
                clr.append('yellow')
            else:
                clr.append('blue')
        else:
            clr.append('white')

    return clr


#_________________________________________________ Merge Sort ____________________________________________________#

#_________________________________________________ Quick Sort ____________________________________________________#


def partition(data, start, end, drdata, speed):
    pivot = data[end]

    drdata(data, getlcr(len(data), start, end, start, start))
    time.sleep(speed)

    for i in range(start, end):
        if data[i] < pivot:
            drdata(data, getlcr(len(data), start, end, start, i, True))
            time.sleep(speed)

            data[i], data[start] = data[start], data[i]
            start += 1
        drdata(data, getlcr(len(data), start, end, start, i))
        time.sleep(speed)

    drdata(data, getlcr(len(data), start, end, start, end, True))
    time.sleep(speed)
    data[end], data[start] = data[start], data[end]
    return start


def quicksort(data, start, end, drdata, speed):
    if start < end:
        pi = partition(data, start, end, drdata, speed)
        quicksort(data, start, pi - 1, drdata, speed)
        quicksort(data, pi + 1, end, drdata, speed)


def getlcr(n, start, end, s, ci, iswap=False):
    clr = []
    for i in range(n):
        if start <= i <= end:
            clr.append('gray')
        else:
            clr.append('white')
        if i == end:
            clr[i] = 'blue'
        elif i == s:
            clr[i] = 'red'
        elif i == ci:
            clr[i] = 'yellow'
        if iswap:
            if i == s or i == ci:
                clr[i] = 'green'
    return clr


#_________________________________________________ Quick Sort ____________________________________________________#

#_________________________________________________ Selection Sort ____________________________________________________#


def selectionSort(data, drdata, speed):
    for i in range(len(data)):
        mini = i
        for j in range(i + 1, len(data)):
            if data[mini] > data[j]:
                mini = j
                drdata(data, ['blue' if c == mini or c == i else 'red' for c in range(len(data))])
                time.sleep(speed)
        data[i], data[mini] = data[mini], data[i]
        drdata(data, ['green' if c == i or c == mini else 'red' for c in range(len(data))])
        time.sleep(speed)
    drdata(data, ['green' for i in range(len(data))])

#_________________________________________________ Selection Sort ____________________________________________________#

#_________________________________________________ Bubble Sort ____________________________________________________#


def bubbleSort(data, drdata, speed):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drdata(data, ['green' if c == j or c == j + 1 else 'red' for c in range(len(data))])
                time.sleep(speed)
    drdata(data, ['green' for i in range(len(data))])


#_________________________________________________ Bubble Sort ____________________________________________________#

#_________________________________________________ Linear Search ____________________________________________________#


def linear_search(data, drdata, speed, x):
    for i in range(len(data)):
        if data[i] == int(x):
            drdata(data, ['green' if c == i else 'red' for c in range(len(data))])
            time.sleep(speed)
            break
        else:
            drdata(data, ['yellow' if c == i else 'red' for c in range(len(data))])
            time.sleep(speed)

#_________________________________________________ Linear Search ____________________________________________________#

#_________________________________________________ Binary Search ____________________________________________________#


def clrarr(data, low, mid, high):
    clr = []
    for i in range(len(data)):
        if i == mid:
            clr.append('yellow')
        elif i == low or i == high:
            clr.append('blue')
        else:
            clr.append('red')
    return clr


def bin_srch(data, drdata, speed, x):
    mergesort(data, drdata, speed)
    low = 0
    high = (len(data))-1
    while low <= high:
        mid = (low+high)//2
        drdata(data, clrarr(data, low, mid, high))
        time.sleep(speed)
        if data[mid] == x:
            drdata(data, ['green' if c == mid else 'red' for c in range(len(data))])
            time.sleep(speed)
            break
        elif data[mid] > x:
            high = mid-1
            drdata(data, ['blue' if i == low or i == high else 'red' for i in range(len(data))])
            time.sleep(speed)
        else:
            low = mid+1
            drdata(data, ['blue' if i == low or i == high else 'red' for i in range(len(data))])
            time.sleep(speed)

#_________________________________________________ Binary Search ____________________________________________________#

#_________________________________________________ Start Button ____________________________________________________#


def strt():
    global data

    if algo_var.get() == 'Quick Sort':
        quicksort(data, 0, len(data) - 1, drdata, speed.get())
        drdata(data, ['green' for i in range(len(data))])

    elif algo_var.get() == 'Bubble Sort':
        bubbleSort(data, drdata, speed.get())

    elif algo_var.get() == 'Merge Sort':
        mergesort(data, drdata, speed.get())
        drdata(data, ['green' for i in range(len(data))])

    elif algo_var.get() == 'Selection Sort':
        selectionSort(data, drdata, speed.get())

    elif algo_var.get() == 'Linear Search':
        linear_search(data, drdata, speed.get(), srch.get())

    elif algo_var.get() == 'Binary Search':
        bin_srch(data, drdata, speed.get(), int(srch.get()))

#_________________________________________________ Start Button ____________________________________________________#

#_________________________________________________ GUI ____________________________________________________#


uif = Frame(root, width=600, height=200, bg='grey')
uif.grid(row=0, column=0, padx=10, pady=5)

canva = Canvas(root, width=830, height=380, bg='white')
canva.grid(row=1, column=0, padx=10, pady=5)

Label(uif, text="Algorithm: ", bg='grey', fg='black', font=('algerian', 12)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
alg = ttk.Combobox(uif, textvariable=algo_var, values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Selection Sort', 'Linear Search', 'Binary Search'])
alg.grid(row=0, column=1, padx=5, pady=5)
alg.current(0)

speed = Scale(uif, from_=5.0, to=0.1, length=200, digits=2, resolution=0.1, orient=HORIZONTAL,
              label='Select Speed(sec)')
speed.grid(row=0, column=2, padx=5, pady=5)

Label(uif, text='Enter Search Key : ').place(x=491, y=5)
Entry(uif, textvariable=srch).grid(row=0, column=3, padx=5, pady=5)

Button(uif, text='Start', command=strt, bg='green', fg='white', height=1, width=10).grid(row=0, column=4, padx=5, pady=5)

sizen = Scale(uif, from_=3, to=50, resolution=1, orient=HORIZONTAL, label='Dataset Size')
sizen.grid(row=1, column=0, padx=5, pady=5, sticky=W)

minen = Scale(uif, from_=1, to=10, resolution=1, orient=HORIZONTAL, label='Minimum Value')
minen.grid(row=1, column=1, padx=5, pady=5, sticky=W)

maxen = Scale(uif, from_=10, to=100, resolution=1, orient=HORIZONTAL, label='Maximum Value')
maxen.grid(row=1, column=2, padx=5, pady=5, sticky=W)

Button(uif, text='Generate Sample Set', command=gen, bg='White').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()


#_________________________________________________ GUI ____________________________________________________#