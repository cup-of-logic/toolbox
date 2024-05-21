import tkinter as tk

class Schedule:
    def __init__(self):
        self.WIDTH, self.HEIGHT, self.X_POS, self.Y_POS = 600, 300, 300, 100
        self.schedule = {}

        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')
        self.root.title("Schedule Manager")
        self.root.iconbitmap('D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\calendar.ico')

        self.add_button = tk.Button(self.root, text='Add Schedule')
        self.check_button = tk.Button(self.root, text='Check Schedule')

        self.add_button.grid(row=0, column=0, padx=(10, 0), pady=10)
        self.check_button.grid(row=0, column=1, padx=10, pady=10)


        self.root.mainloop()


if __name__ == '__main__':
    Schedule()