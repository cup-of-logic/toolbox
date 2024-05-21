import tkinter as tk


class Symbols:
    def __init__(self):
        self.WIDTH, self.HEIGHT, self.X, self.Y = 600, 300, 300, 100
        self.canvas_width, self.canvas_height = 540, 240
        self.symbols, self.names, self.show_list = [], [], []
        self.text = ""
        self.search_text = ""

        self.get_data()
        self.create_show_list()
        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.title("Symbols")
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.X}+{self.Y}")
        self.root.iconbitmap("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\symbols.ico")

        self.im_search = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\search.png").subsample(10)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")

        self.search_bar = tk.Entry(self.root, width=30, font=('Arial', 12))
        self.search_button = tk.Button(self.root, image=self.im_search, width=20, height=20, command=self.create_show_list)
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, yscrollcommand=self.scrollbar.set)

        self.search_bar.grid(row=0, column=0, padx=(50, 30), pady=10, sticky='e')
        self.search_button.grid(row=0, column=1, sticky='w')

        self.set_canvas()
        self.canvas.grid(row=1, column=0, columnspan=2, padx=(30, 0))
        self.scrollbar.grid(row=1, column=2, sticky='ns')

        self.scrollbar.config(command=self.canvas.yview())
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.root.mainloop()

    def on_canvas_configure(self, event):
        # Update the scroll region to match the size of the canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def set_canvas(self):
        cell_size = 40
        self.canvas.create_line(3, 3, self.canvas_width, 3, width=1, fill='black')
        self.canvas.create_line(3, 3, 3, self.canvas_width, width=1, fill='black')
        self.canvas.create_line(3, self.canvas_height+1, self.canvas_width, self.canvas_height+1, width=1, fill='black')
        self.canvas.create_line(self.canvas_width, 3, self.canvas_width, self.canvas_height+1, width=1, fill='black')

        self.canvas.create_line(cell_size, 3, cell_size, self.canvas_width, width=1, fill='black')
        for i in range(len(self.show_list)):
            self.canvas.create_line(3, cell_size*(i+1), self.canvas_width, cell_size*(i+1), width=1, fill='black')
            self.canvas.create_text(cell_size//2, (cell_size//2) * 2 * (i+1), text=self.show_list[i][0], fill='black', font=('Arial', '10'))


    def get_data(self):
        with open('D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\unicode_data.txt', 'r', encoding='utf-8') as file:
            self.text = file.read()
        lines = self.text.split("\n")
        lines = lines[:-1]
        for line in lines:
            data = line.split(",")
            self.symbols.append(data[0])
            self.names.append(data[3])

    def create_show_list(self):
        self.show_list = []
        if self.search_text.strip() == "":
            for i in range(len(self.symbols)):
                self.show_list.append([self.symbols[i], self.names[i]])


if __name__ == '__main__':
    Symbols()