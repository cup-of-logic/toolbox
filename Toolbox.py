import tkinter as tk
import calculator
import clipboard_tool
import lang_trans
import num_convert
import document
import pass_strength
import wordle


class Tools:
    def __init__(self):
        self.WIN_WIDTH, self.WIN_HEIGHT, self.WIN_X, self.WIN_Y = 531, 425, 100, 100
        self.clp = None
        self.main()

    def main(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}+{self.WIN_X}+{self.WIN_Y}")
        self.root.resizable(False, False)
        self.root.title("HandyTools")
        self.root.iconbitmap("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\logo.ico")
        self.prep_icons()

        self.clp_button = tk.Button(self.root, image=self.im_clp, width=100, height=100, command=self.clipboard).grid(row=0, column=0)
        self.pass_button = tk.Button(self.root, image=self.im_pass, width=100, height=100, command=pass_strength.Password).grid(row=0, column=1)
        self.conv_button = tk.Button(self.root, image=self.im_conv, width=100, height=100).grid(row=0, column=2)
        self.base_conv_button = tk.Button(self.root, image=self.im_bin, width=100, height=100, command=num_convert.Convert).grid(row=0, column=3)
        self.enc_button = tk.Button(self.root, image=self.im_enc, width=100, height=100).grid(row=0, column=4)
        self.calc_button = tk.Button(self.root, image=self.im_calc, width=100, height=100, command=lambda: calculator.Calculator()).grid(row=1, column=0)
        self.lang_button = tk.Button(self.root, image=self.im_lang, width=100, height=100, command=lambda: lang_trans.Translate()).grid(row=1, column=1)
        self.curr_button = tk.Button(self.root, image=self.im_curr, width=100, height=100).grid(row=1, column=2)
        self.clock_button = tk.Button(self.root, image=self.im_clock, width=100, height=100).grid(row=1, column=3)
        self.wordle_button = tk.Button(self.root, image=self.im_wordle, width=100, height=100, command=wordle.Wordle).grid(row=1, column=4)
        self.schd_button = tk.Button(self.root, image=self.im_cal, width=100, height=100).grid(row=2, column=0)
        self.doc = tk.Button(self.root, image=self.im_doc, width=100, height=100, command=document.Doc).grid(row=2, column=1)
        
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=2, column=2)
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=2, column=3)
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=2, column=4)
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=3, column=0)
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=3, column=1)
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=3, column=2)
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=3, column=3)
        self.b = tk.Button(self.root, image=self.im_none, width=100, height=100).grid(row=3, column=4)

        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.root.mainloop()

    def prep_icons(self):
        self.im_clp = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\clipboard.png").subsample(10)
        self.im_pass = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\password.png").subsample(10)
        self.im_conv = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\convert.png").subsample(10)
        self.im_none = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\none.png").subsample(10)
        self.im_del = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\del.png").subsample(30)
        self.im_bin = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\number_base.png").subsample(10)
        self.im_enc = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\encrypt.png").subsample(10)
        self.im_calc = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\calculator.png").subsample(10)
        self.im_lang = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\language.png").subsample(10)
        self.im_curr = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\currency.png").subsample(12)
        self.im_clock = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\clock.png").subsample(10)
        self.im_mic = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\voice.png").subsample(10)
        self.im_wordle = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\wordle.png").subsample(10)
        self.im_doc = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\document.png").subsample(10)
        self.im_cal = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\calendar.png").subsample(10)

    def clipboard(self):
        self.clp = clipboard_tool.Clipboard()

    def on_close(self):
        try:
            self.clp.save_data()
        except:
            pass
        self.root.destroy()


if __name__ == '__main__':
    Tools()
