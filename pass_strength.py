import tkinter as tk
import random

class Password:
    def __init__(self):
        self.WIDTH, self.HEIGHT, self.X_POS, self.Y_POS = 400, 150, 300, 200
        self.pass_str = 0

        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')
        self.root.title('Password')
        self.root.iconbitmap("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\password.ico")

        self.entry = tk.Entry(self.root, width=50, font=('Arial', 10))
        self.gen_button = tk.Button(self.root, text="Generate", command=self.generate)
        self.str_button = tk.Button(self.root, text="Check Strength", command=self.check_str)
        self.str_label = tk.Label(self.root, text="Password Strength: 0/50")

        self.entry.grid(row=0, column=0, columnspan=2, padx=21, pady=20)
        self.gen_button.grid(row=1, column=0, sticky='e', padx=(0, 15))
        self.str_button.grid(row=1, column=1, sticky='w')
        self.str_label.grid(row=2, column=0, columnspan=2, pady=15)

        self.root.mainloop()

    def check_str(self):
        self.pass_str = 0
        text = self.entry.get()

        if text == '':
            self.str_label.configure(text='Password Strength: 0/50')
            return

        length = len(text)
        small_flag = cap_flag = char_flag = num_flag = False

        if length > 32:
            self.pass_str += 20
        elif length > 16:
            self.pass_str += 10
        elif length > 8:
            self.pass_str += 5
        else:
            self.pass_str -= 10

        for char in text:
            if char.isalpha():
                if char.islower():
                    self.pass_str += 3
                    small_flag = True
                else:
                    self.pass_str += 5
                    cap_flag = True
            elif char.isnumeric():
                self.pass_str += 6
                num_flag = True
            else:
                self.pass_str += 7
                char_flag = True

        if char_flag and num_flag and cap_flag and small_flag:
            self.pass_str += 10
        else:
            self.pass_str -= 10

        if self.pass_str > 50:
            self.pass_str = 50

        self.str_label.configure(text=f'Password Strength: {self.pass_str}/50')

    def generate(self):
        text = self.entry.get()
        length = random.randint(8, 40)

        if len(text) > length:
            length += 5

        choice_list = ["NUM", "ALPHA", "CHAR"]
        char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '.', '_']

        for i in range(length - len(text)):
            ch = random.choice(choice_list)
            if ch == "NUM":
                text += str(random.randint(0, 9))
            elif ch == "ALPHA":
                case = random.randint(0, 1)
                if case == 0:
                    text += chr(random.randint(97, 122))
                else:
                    text += chr(random.randint(65, 90))
            else:
                text += random.choice(char_list)

        self.entry.delete('0', tk.END)
        self.entry.insert(tk.END, text)

        self.check_str()


if __name__ == '__main__':
    Password()