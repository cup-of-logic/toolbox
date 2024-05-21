import tkinter as tk
import math

class Calculator:
    def __init__(self):
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.WINDOW_X_POS, self.WINDOW_Y_POS = 300, 400, 100, 100
        self.com_text = ""
        self.shift_on = False
        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{self.WINDOW_X_POS}+{self.WINDOW_Y_POS}")
        self.root.resizable(False, False)
        self.root.title("Calculator")
        self.root.configure(bg="white")
        self.root.iconbitmap("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\calculator.ico")

        self.main_frame = tk.Frame(self.root, background="white")

        self.text = tk.Entry(self.main_frame, width=18, font=("Consolas", 20), relief=tk.SUNKEN, state="readonly", borderwidth=5, background="white")

        self.button_SHIFT = tk.Button(self.main_frame, text="SHIFT", width=14, height=2, command=lambda: self.update("SHIFT"))
        self.button_AC = tk.Button(self.main_frame, text="AC", width=6, height=2, command=lambda: self.update("CLEAR"))
        self.button_DEL = tk.Button(self.main_frame, text="DEL", width=6, height=2, command=lambda: self.update("DEL"))
        self.button_H = tk.Button(self.main_frame, text="H", width=6, height=2, command=lambda: self.update("HISTORY"))

        self.button_brack1 = tk.Button(self.main_frame, text="(", width=6, height=2, command=lambda: self.update("("))
        self.button_brack2 = tk.Button(self.main_frame, text=")", width=6, height=2, command=lambda: self.update(")"))
        self.button_sin = tk.Button(self.main_frame, text="sin", width=6, height=2, command=lambda: self.update("sin(") if self.shift_on==False else self.update("cosec("))
        self.button_cos = tk.Button(self.main_frame, text="cos", width=6, height=2, command=lambda: self.update("cos(") if self.shift_on==False else self.update("sec("))
        self.button_tan = tk.Button(self.main_frame, text="tan", width=6, height=2, command=lambda: self.update("tan(") if self.shift_on==False else self.update("cot("))

        self.button_7 = tk.Button(self.main_frame, text="7", width=6, height=2, command=lambda: self.update("7"))
        self.button_8 = tk.Button(self.main_frame, text="8", width=6, height=2, command=lambda: self.update("8"))
        self.button_9 = tk.Button(self.main_frame, text="9", width=6, height=2, command=lambda: self.update("9"))
        self.button_fact = tk.Button(self.main_frame, text="!", width=6, height=2, command=lambda: self.update("!"))
        self.button_pow = tk.Button(self.main_frame, text="^", width=6, height=2, command=lambda: self.update("^") if self.shift_on==False else self.update("√("))

        self.button_4 = tk.Button(self.main_frame, text="4", width=6, height=2, command=lambda: self.update("4"))
        self.button_5 = tk.Button(self.main_frame, text="5", width=6, height=2, command=lambda: self.update("5"))
        self.button_6 = tk.Button(self.main_frame, text="6", width=6, height=2, command=lambda: self.update("6"))
        self.button_pi = tk.Button(self.main_frame, text="π", width=6, height=2, command=lambda: self.update("π") if self.shift_on==False else self.update("e"))
        self.button_log = tk.Button(self.main_frame, text="log", width=6, height=2, command=lambda: self.update("log(") if self.shift_on==False else self.update("ln("))

        self.button_1 = tk.Button(self.main_frame, text="1", width=6, height=2, command=lambda: self.update("1"))
        self.button_2 = tk.Button(self.main_frame, text="2", width=6, height=2, command=lambda: self.update("2"))
        self.button_3 = tk.Button(self.main_frame, text="3", width=6, height=2, command=lambda: self.update("3"))
        self.button_add = tk.Button(self.main_frame, text="+", width=6, height=2, command=lambda: self.update("+"))
        self.button_sub = tk.Button(self.main_frame, text="-", width=6, height=2, command=lambda: self.update("-"))

        self.button_0 = tk.Button(self.main_frame, text="0", width=6, height=2, command=lambda: self.update("0"))
        self.button_point = tk.Button(self.main_frame, text=".", width=6, height=2, command=lambda: self.update("."))
        self.button_equal = tk.Button(self.main_frame, text="=", width=6, height=2, command=lambda: self.update("EQUAL"))
        self.button_mult = tk.Button(self.main_frame, text="×", width=6, height=2, command=lambda: self.update("×"))
        self.button_div = tk.Button(self.main_frame, text="÷", width=6, height=2, command=lambda: self.update("÷"))



        self.main_frame.pack()
        self.text.grid(row=0, column=0, sticky="w", pady=15, columnspan=5)

        self.button_SHIFT.grid(row=1, column=0, columnspan=2, pady=5)
        self.button_AC.grid(row=1, column=2, columnspan=1, pady=5)
        self.button_DEL.grid(row=1, column=3, columnspan=1, pady=5)
        self.button_H.grid(row=1, column=4, columnspan=1, pady=5)

        self.button_brack1.grid(row=2, column=0, columnspan=1, pady=5)
        self.button_brack2.grid(row=2, column=1, columnspan=1, pady=5)
        self.button_sin.grid(row=2, column=2, columnspan=1, pady=5)
        self.button_cos.grid(row=2, column=3, columnspan=1, pady=5)
        self.button_tan.grid(row=2, column=4, columnspan=1, pady=5)

        self.button_7.grid(row=3, column=0, columnspan=1, pady=5)
        self.button_8.grid(row=3, column=1, columnspan=1, pady=5)
        self.button_9.grid(row=3, column=2, columnspan=1, pady=5)
        self.button_fact.grid(row=3, column=3, columnspan=1, pady=5)
        self.button_pow.grid(row=3, column=4, columnspan=1, pady=5)

        self.button_4.grid(row=4, column=0, columnspan=1, pady=5)
        self.button_5.grid(row=4, column=1, columnspan=1, pady=5)
        self.button_6.grid(row=4, column=2, columnspan=1, pady=5)
        self.button_pi.grid(row=4, column=3, columnspan=1, pady=5)
        self.button_log.grid(row=4, column=4, columnspan=1, pady=5)

        self.button_1.grid(row=5, column=0, columnspan=1, pady=5)
        self.button_2.grid(row=5, column=1, columnspan=1, pady=5)
        self.button_3.grid(row=5, column=2, columnspan=1, pady=5)
        self.button_add.grid(row=5, column=3, columnspan=1, pady=5)
        self.button_sub.grid(row=5, column=4, columnspan=1, pady=5)

        self.button_0.grid(row=6, column=0, columnspan=1, pady=5)
        self.button_point.grid(row=6, column=1, columnspan=1, pady=5)
        self.button_equal.grid(row=6, column=2, columnspan=1, pady=5)
        self.button_mult.grid(row=6, column=3, columnspan=1, pady=5)
        self.button_div.grid(row=6, column=4, columnspan=1, pady=5)


        self.text.config(insertwidth=0, insertofftime=100000)
        self.root.mainloop()

    def update(self, comm):
        match comm:
            case "CLEAR":
                self.com_text = ""
            case "SHIFT":
                self.shift_on = True if self.shift_on == False else False
                self.shift_update()
            case "DEL":
                self.delete()
            case "HISTORY":
                pass
            case "EQUAL":
                self.com_text = self.evaluate()
            case _:
                self.com_text = str(self.com_text) + comm

        self.text.configure(state="normal")
        self.text.delete(0, tk.END)
        self.text.insert(0, self.com_text)
        self.text.configure(state="readonly")

    def shift_update(self):
        if self.shift_on:
            self.button_sin["text"] = "cosec"
            self.button_cos["text"] = "sec"
            self.button_tan["text"] = "cot"
            self.button_pow["text"] = "√"
            self.button_pi["text"] = "e"
            self.button_log["text"] = "ln"
        else:
            self.button_sin["text"] = "sin"
            self.button_cos["text"] = "cos"
            self.button_tan["text"] = "tan"
            self.button_pow["text"] = "^"
            self.button_pi["text"] = "π"
            self.button_log["text"] = "log"

    def evaluate(self):
        self.com_text = self.com_text.replace("^", "**")
        self.com_text = self.com_text.replace("×", "*")
        self.com_text = self.com_text.replace("÷", "/")
        self.com_text = self.com_text.replace("e", "math.e")
        self.com_text = self.com_text.replace("π", "math.pi")
        self.com_text = self.com_text.replace("√", "math.sqrt")
        self.com_text = self.com_text.replace("sin", "math.sin")
        self.com_text = self.com_text.replace("cos", "math.cos")
        self.com_text = self.com_text.replace("tan", "math.tan")
        self.com_text = self.com_text.replace("cosec", "1/math.sin")
        self.com_text = self.com_text.replace("sec", "1/math.cos")
        self.com_text = self.com_text.replace("cot", "1/math.tan")
        self.com_text = self.com_text.replace("log", "math.log10")
        self.com_text = self.com_text.replace("ln", "math.log")

        self.calc_fact()

        try:
            result = str(eval(self.com_text))
        except:
            result = "ERROR"
        return result

    def calc_fact(self):
        for char in self.com_text:
            num = ""
            if char == "!":
                for i in range(self.com_text.index("!")-1, -1, -1):
                    if self.com_text[i].isdigit():
                        num = self.com_text[i] + num
                    else:
                        break
                temp = num
                try:
                    num = str(math.factorial(int(num)))
                except:
                    num = "float(\"inf\")"
                self.com_text = self.com_text.replace(f"{temp}!", num)

    def delete(self):
        self.com_text = self.com_text[:-1]



if __name__ == '__main__':
    Calculator()
