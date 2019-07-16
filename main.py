import tkinter
from tkinter import ttk
import datetime


def calculate_remaining(year, month, day):
    given = datetime.datetime(year=year, month=month, day=day)
    now = datetime.datetime.now()
    diff = given - now

    if diff.days < 0:
        diff = datetime.timedelta()

    return diff


def apply_label():
    try:
        diff = calculate_remaining(int(year.get()), int(month.get()), int(day.get()))
    except:
        return

    days, seconds = diff.days, diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    remaining.set("{}일 {}시간 {}분 {}.{:0<3}초 남았습니다.".format(days, hours, minutes, seconds, diff.microseconds // 1000))
    remaining_label.after(10, apply_label)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('D-day calculator')

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S), padx=5, pady=5)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    year = tkinter.StringVar()
    month = tkinter.StringVar()
    day = tkinter.StringVar()
    remaining = tkinter.StringVar(value="남았습니다.")

    year_entry = ttk.Entry(mainframe, width=6, textvariable=year)
    year_entry.grid(column=0, row=0, sticky=(tkinter.W, tkinter.E), padx=5, pady=5)
    year_label = ttk.Label(mainframe, text="년")
    year_label.grid(column=1, row=0, sticky=(tkinter.W, tkinter.E), pady=5)

    month_entry = ttk.Entry(mainframe, width=4, textvariable=month)
    month_entry.grid(column=2, row=0, sticky=(tkinter.W, tkinter.E), padx=5, pady=5)
    month_label = ttk.Label(mainframe, text="월")
    month_label.grid(column=3, row=0, sticky=(tkinter.W, tkinter.E), pady=5)

    day_entry = ttk.Entry(mainframe, width=4, textvariable=day)
    day_entry.grid(column=4, row=0, sticky=(tkinter.W, tkinter.E), padx=5, pady=5)
    day_label = ttk.Label(mainframe, text="일 까지")
    day_label.grid(column=5, row=0, sticky=(tkinter.W, tkinter.E), pady=5)

    remaining_label = ttk.Label(mainframe, textvariable=remaining)
    remaining_label.grid(column=0, row=1, columnspan=6, sticky=(tkinter.S, tkinter.E), padx=5, pady=5)

    button = ttk.Button(mainframe, text="Calculate", command=apply_label)
    button.grid(column=5, row=2, sticky=tkinter.E)

    apply_label()

    root.mainloop()
