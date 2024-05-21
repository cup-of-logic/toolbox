import tkinter as tk
import pyperclip
import clipboard
import keyboard
import pickle


class Clipboard:
    def __init__(self):
        self.clip_list = []
        self.clip_on = False
        self.get_data()
        self.open_clip(self.clip_on, 300, 100)

    def get_data(self):
        with open("clipboard_data.pkl", "rb") as file:
            self.clip_list = pickle.load(file)

    def open_clip(self, clip_status, x_pos, y_pos):
        self.clip_on = clip_status
        width, height, x, y = 300, 500, x_pos, y_pos
        self.clip_win = tk.Toplevel()
        self.clip_win.geometry(f"{width}x{height}+{x}+{y}")
        self.clip_win.resizable(False, False)
        self.clip_win.title("Clipboard")
        self.clip_win.iconbitmap("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\clipboard.ico")
        self.clip_win.configure(bg='lightgrey')

        self.im_copy = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\copy.png").subsample(40)
        self.im_del2 = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\del2.png").subsample(40)
        self.im_del = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\del.png").subsample(30)

        self.top_frame = tk.Frame(self.clip_win)
        self.bottom_frame = tk.Frame(self.clip_win)
        self.clip_check = tk.Checkbutton(self.top_frame, text="Clipboard ON", command=self.toggle_clip)
        self.clip_check.grid(row=0, column=0, sticky='w')
        self.del_all_button = tk.Button(self.top_frame, image=self.im_del, width=20, height=20, command=self.del_all)
        self.del_all_button.grid(row=0, column=1, padx=173)

        if self.clip_on:
            self.clip_check.select()
        self.update_clip()

        self.top_frame.pack(side=tk.TOP, pady=(0, 1))
        self.bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.clip_win.bind("<ButtonRelease-1>", lambda _: self.auto_clip(True))
        self.clip_win.bind("<Control-KeyRelease-c>", lambda _: self.auto_clip(True))

        self.clip_win.protocol("WM_DELETE_WINDOW", self.save_data)
        self.clip_win.mainloop()

    def toggle_clip(self):
        self.clip_on = True if not self.clip_on else False
        self.prev_clip_cont = pyperclip.paste()

    def auto_clip(self, flag):
        if self.clip_on:
            self.clip_cont = pyperclip.paste()
            if self.clip_cont != self.prev_clip_cont:
                self.clip_list.append(self.clip_cont)
                self.prev_clip_cont = self.clip_cont

                if flag:
                    x_pos, y_pos = self.clip_win.winfo_x(), self.clip_win.winfo_y()
                    self.clip_win.destroy()
                    self.open_clip(True, x_pos, y_pos)

    def update_clip(self):
        i = 0
        for text in self.clip_list:
            self.clip_entry = tk.Entry(self.bottom_frame, width=40)
            self.clip_entry.insert(0, text)
            self.clip_entry.grid(row=i, column=0, pady=5, padx=5)

            self.clip_copy_button = tk.Button(self.bottom_frame, image=self.im_copy, command=lambda t=text: self.copy_clip(t))
            self.clip_copy_button.grid(row=i, column=1)
            self.clip_del_button = tk.Button(self.bottom_frame, image=self.im_del2, command=lambda index=i: self.delete_clip(index))
            self.clip_del_button.grid(row=i, column=2, padx=3)
            i += 1

    def copy_clip(self, text):
        self.clip_on = False
        clipboard.copy(text)

    def delete_clip(self, index):
        self.clip_entry.destroy()
        self.clip_copy_button.destroy()
        self.clip_del_button.destroy()
        del self.clip_list[index]

        x_pos, y_pos = self.clip_win.winfo_x(), self.clip_win.winfo_y()
        self.clip_win.destroy()
        self.open_clip(False, x_pos, y_pos)

    def del_all(self):
        self.clip_list = []
        x_pos, y_pos = self.clip_win.winfo_x(), self.clip_win.winfo_y()
        self.clip_win.destroy()
        self.open_clip(False, x_pos, y_pos)

    def save_data(self):
        text = self.clip_list
        with open("clipboard_data.pkl", "wb") as file:
            pickle.dump(text, file)
        self.clip_win.destroy()


if __name__ == '__main__':
    Clipboard()
