import tkinter as tk
from tkinter import ttk

class Convert:
    def __init__(self):
        self.WIDTH, self.HEIGHT, self.X_POS, self.Y_POS = 430, 300, 300, 100
        self.list_items = ["Binary", "Octal", "Decimal", "Hexadecimal", "Text"]
        self.input_text = self.output_text = ""

        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.title("Converter")
        self.root.iconbitmap("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\number_base.ico")
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}")

        self.image = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\trans.png").subsample(30)

        self.to_label = tk.Label(self.root, text="To:")
        self.from_label = tk.Label(self.root, text="From:")
        self.to_list = ttk.Combobox(self.root, width=20, values=self.list_items)
        self.from_list = ttk.Combobox(self.root, width=20, values=self.list_items)
        self.button = tk.Button(self.root, image=self.image, command=self.operate)
        self.input_label = tk.Label(self.root, text="INPUT:", font=("Arial", 10))
        self.input_box = tk.Text(self.root, width=50, height=5, wrap=tk.WORD, relief=tk.GROOVE)
        self.output_label = tk.Label(self.root, text="OUTPUT:", font=("Arial", 10))
        self.output_box = tk.Text(self.root, width=50, height=5, wrap=tk.WORD, relief=tk.GROOVE)

        self.from_label.grid(row=0, column=0, padx=(10, 0), pady=10)
        self.from_list.grid(row=0, column=1, pady=10)
        self.to_label.grid(row=0, column=2, padx=(20, 0), pady=10)
        self.to_list.grid(row=0, column=3, pady=10)
        self.button.grid(row=0, column=4, padx=10, pady=10)
        self.input_label.grid(row=1, column=0, columnspan=5, stick='w', padx=(10, 0))
        self.input_box.grid(row=2, column=0, columnspan=5, sticky='w', padx=(10, 0), pady=10)
        self.output_label.grid(row=3, column=0, columnspan=5, stick='w', padx=(10, 0))
        self.output_box.grid(row=4, column=0, columnspan=5, sticky='w', padx=(10, 0), pady=10)

        self.from_list.set("Select an option")
        self.to_list.set("Select an option")

        self.root.mainloop()

    def operate(self):

        from_base = self.from_list.get()
        from_base = 2 if from_base == "Binary" else 8 if from_base == "Octal" else 10 if from_base == "Decimal" else 16 if from_base == "Hexadecimal" else "Text" if from_base == "Text" else "ERROR"
        to_base = self.to_list.get()
        to_base = 2 if to_base == "Binary" else 8 if to_base == "Octal" else 10 if to_base == "Decimal" else 16 if to_base == "Hexadecimal" else "Text" if to_base == "Text" else "ERROR"

        self.input_text = self.input_box.get("1.0", tk.END)

        if from_base == 'ERROR' or to_base == 'ERROR':
            self.output_text = 'ERROR'
        elif from_base == 'Text' and to_base == 2:
            self.output_text = self.text_to_bin(self.input_text)
        elif from_base == 2 and to_base == 'Text':
            self.output_text = self.bin_to_text(self.input_text)
        elif type(from_base) == type(1) and type(to_base) == type(1):
            num = self.input_text
            frac = 0
            if '.' in num:
                frac = num[num.index('.') + 1:]
                num = num[:num.index('.')]
                frac = self.frac_calc(frac, from_base, to_base)

            dec = int(num, from_base)
            if to_base == 2:
                self.output_text = bin(dec)[2:]
            elif to_base == 8:
                self.output_text = oct(dec)[2:]
            elif to_base == 16:
                self.output_text = hex(dec)[2:].upper()
            elif to_base == 10:
                self.output_text = dec

            self.output_text = str(self.output_text) + '.' + str(frac)

        else:
            self.output_text = 'ERROR'


        self.output_box.delete('1.0', tk.END)
        self.output_box.insert('1.0', str(self.output_text))

    def text_to_bin(self, text):
        output = ''
        for char in text:
            asc = ord(char)
            binary = bin(asc)[2:]
            for i in range(8-len(binary)):
                binary = '0' + binary

            output += binary + ' '

        return output.strip()

    def bin_to_text(self, binary):
        output = ''
        bin_list = binary.split(' ')

        for binary in bin_list:
            dec = int(binary, 2)
            char = chr(dec)
            output += char

        return output

    def frac_calc(self, frac, from_base, to_base):
        frac = frac[:-1]
        dec = 0
        i = -1
        out = ''
        for dig in frac:
            if dig.isalpha():
                dig = ord(dig) - 55
            dec = dec + (int(dig) * (from_base ** i))
            i -= 1

        if to_base == 10:
            ret = str(dec)[2:]
            count = 0
            for i in range(len(ret)-1, -1, -1):
                if ret[i] == '0':
                    count += 1
                else:
                    break
            print(count)
            return ret[:len(ret)-count]

        for i in range(16):
            dec = dec * to_base
            if int(dec) > 9:
                out = out + chr(int(dec) + 55)
            else:
                out = out + str(int(dec))

            dec = dec - int(dec)

        count = 0
        for i in range(len(out) - 1, -1, -1):
            if out[i] == '0':
                count += 1
            else:
                break

        return out[:len(out)-count]


if __name__ == '__main__':
    Convert()