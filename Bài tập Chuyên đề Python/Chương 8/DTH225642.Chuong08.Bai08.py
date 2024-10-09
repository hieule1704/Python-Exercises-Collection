import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5.0/9.0
        return round(celsius, 2)
    except ValueError:
        return None


def perform_conversion():
    fahrenheit = fahrenheit_entry.get()
    celsius = fahrenheit_to_celsius(fahrenheit)
    if celsius is not None:
        result_label.config(text=f'Do C la: {celsius} °C')
    else:
        messagebox.showerror("Error", "Please enter a valid temperature in °F.")


def main():
    global fahrenheit_entry, result_label
    window = tk.Tk()
    window.title('Temperature Converter: °F to °C')

    ttk.Label(window, text='Nhap °F:').grid(row=0, column=0, sticky='e')
    fahrenheit_entry = ttk.Entry(window)
    fahrenheit_entry.grid(row=0, column=1)

    convert_button = ttk.Button(window, text='Chuyen doi °C', command=perform_conversion)
    convert_button.grid(row=2, column=0, columnspan=2)

    result_label = ttk.Label(window, text='')
    result_label.grid(row=3, column=0, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()