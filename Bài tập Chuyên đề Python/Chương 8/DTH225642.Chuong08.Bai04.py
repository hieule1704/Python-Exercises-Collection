from tkinter import *


def press_button(button_text):
    current_text = entry.get()
    if button_text == 'C':
        entry.delete(0, END)
    elif button_text == '=':
        try:
            result = eval(current_text)
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.delete(0, END)
            entry.insert(END, 'Error')
    else:
        entry.insert(END, button_text)


def main(button_text=None):
    root = Tk()
    root.title("Calculator")

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    row_count = 1
    col_count = 0

    for button_text in buttons:
        button = Button(root, text=button_text, width=5, height=2, command=lambda button_text=button_text: press_button(button_text))
        button.grid(row=row_count, column=col_count)
        col_count += 1
        if col_count > 3:
            col_count = 0
            row_count += 1

    global entry
    entry = Entry(root, width=20, font=('Arial', 14))
    entry.grid(row=0, column=0, columnspan=4)

    root.mainloop()


if __name__ == "__main__":
    main()
