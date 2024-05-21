import tkinter as tk
import csv

class Wordle:
    def __init__(self):
        self.WIDTH, self.HEIGHT, self.X_POS, self.Y_POS = 180, 300, 300, 100
        self.CSV_PATH = "D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\wordle_solutions.csv"
        self.solutions = []
        self.output = ""

        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.title('')
        self.root.resizable(False, False)
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')
        self.root.iconbitmap('D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\wordle.ico')

        self.create_list()

        self.im_go = tk.PhotoImage(file='D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\enter.png').subsample(30)
        self.placed_label = tk.Label(self.root, text="PLACED LETTERS:")
        self.placed_entry_1 = tk.Entry(self.root, width=3)
        self.placed_entry_2 = tk.Entry(self.root, width=3)
        self.placed_entry_3 = tk.Entry(self.root, width=3)
        self.placed_entry_4 = tk.Entry(self.root, width=3)
        self.placed_entry_5 = tk.Entry(self.root, width=3)

        self.valid_label = tk.Label(self.root, text="VALID LETTERS:")
        self.valid_entry_1 = tk.Entry(self.root, width=3)
        self.valid_entry_2 = tk.Entry(self.root, width=3)
        self.valid_entry_3 = tk.Entry(self.root, width=3)
        self.valid_entry_4 = tk.Entry(self.root, width=3)
        self.valid_entry_5 = tk.Entry(self.root, width=3)

        self.invalid_label = tk.Label(self.root, text="INVALID LETTERS:")
        self.invalid_entry = tk.Entry(self.root, width=25)
        self.button = tk.Button(self.root, image=self.im_go, command=self.get_words)
        self.output_box = tk.Text(self.root, width=20, height=6, relief=tk.FLAT, background='#f0f0f0', wrap=tk.WORD)

        self.placed_label.grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 0))
        self.placed_entry_1.grid(row=1, column=0, padx=(10, 0))
        self.placed_entry_2.grid(row=1, column=1)
        self.placed_entry_3.grid(row=1, column=2)
        self.placed_entry_4.grid(row=1, column=3)
        self.placed_entry_5.grid(row=1, column=4)
        self.valid_label.grid(row=2, column=0, columnspan=5, padx=10, pady=(10, 0))
        self.valid_entry_1.grid(row=3, column=0, padx=(10, 0))
        self.valid_entry_2.grid(row=3, column=1)
        self.valid_entry_3.grid(row=3, column=2)
        self.valid_entry_4.grid(row=3, column=3)
        self.valid_entry_5.grid(row=3, column=4)
        self.invalid_label.grid(row=4, column=0, columnspan=5, padx=10, pady=(10, 0))
        self.invalid_entry.grid(row=5, column=0, columnspan=5, padx=10)
        self.button.grid(row=6, column=0, columnspan=5, pady=10)
        self.output_box.grid(row=7, column=0, columnspan=10, sticky='w', padx=(20, 0))

        self.root.mainloop()

    def create_list(self):
        self.solutions = []
        with open(self.CSV_PATH, 'r') as file:
            csv_reader = csv.reader(file)
            for word in csv_reader:
                self.solutions.append(word[0])

        self.solutions = self.solutions[1:]

    def get_words(self):
        self.create_list()

        placed_list = [self.placed_entry_1.get().lower(), self.placed_entry_2.get().lower(), self.placed_entry_3.get().lower(), self.placed_entry_4.get().lower(), self.placed_entry_5.get().lower()]
        valid_list = [self.valid_entry_1.get().lower(), self.valid_entry_2.get().lower(), self.valid_entry_3.get().lower(), self.valid_entry_4.get().lower(), self.valid_entry_5.get().lower()]
        invalid = self.invalid_entry.get().lower()
        temp = ''
        for letter in invalid:
            if 97 <= ord(letter) <= 122:
                temp = temp + letter
        invalid = temp

        i = 0
        # Filters
        while i < len(self.solutions):
            solution = self.solutions[i]
            for j in range(5):
                if placed_list[j] != '' and solution[j] != placed_list[j]:
                    self.solutions.remove(solution)
                    i -= 1
                    break

                if valid_list[j] != '' and not(valid_list[j] in solution):
                    self.solutions.remove(solution)
                    i -= 1
                    break
            i += 1

        for i in range(97, 123):
            j = 0
            while j < len(self.solutions):
                solution = self.solutions[j]
                if (chr(i) in invalid) and (chr(i) in solution):
                    self.solutions.remove(solution)
                    j -= 1

                j += 1

        # Display
        self.solutions = list(set(self.solutions))
        self.output = " ".join(self.solutions)
        self.output_box.delete('1.0', tk.END)
        self.output_box.insert('1.0', self.output)



if __name__ == '__main__':
    Wordle()