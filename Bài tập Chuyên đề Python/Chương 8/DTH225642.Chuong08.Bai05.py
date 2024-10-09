import tkinter as tk
from tkinter import messagebox


def change_password():
    old_pass = old_pass_entry.get()
    new_pass = new_pass_entry.get()
    confirm_pass = confirm_pass_again_entry.get()

    if old_pass == new_pass:
        messagebox.showerror("Error", "New password must be different from the old password.")
        return
    if new_pass != confirm_pass:
        messagebox.showerror("Error", "New password and confirmation do not match.")
        return

    messagebox.showinfo("Success", "Password successfully changed.")
    # Normally update the password storage with new_pass here


def close_window():
    root.destroy()


def main():
    global root, old_pass_entry, new_pass_entry, confirm_pass_again_entry
    root = tk.Tk()
    root.title("Enter New Password")

    tk.Label(root, text="Old Password:").grid(row=0, column=0, sticky="e")
    old_pass_entry = tk.Entry(root, show="*")
    old_pass_entry.grid(row=0, column=1)

    tk.Label(root, text="New Password:").grid(row=1, column=0, sticky="e")
    new_pass_entry = tk.Entry(root, show="*")
    new_pass_entry.grid(row=1, column=1)

    tk.Label(root, text="Enter New Password Again:").grid(row=2, column=0, sticky="e")
    confirm_pass_again_entry = tk.Entry(root, show="*")
    confirm_pass_again_entry.grid(row=2, column=1)

    ok_btn = tk.Button(root, text="OK", command=change_password)
    ok_btn.grid(row=3, column=0, pady=(10,0))

    cancel_btn = tk.Button(root, text="Cancel", command=close_window)
    cancel_btn.grid(row=3, column=1, pady=(10,0))

    root.geometry("300x110")
    root.mainloop()


if __name__ == "__main__":
    main()