import tkinter as tk

class Doc:
    def __init__(self):
        self.WIDTH, self.HEIGHT, self.X_POS, self.Y_POS = 500, 360, 300, 100

        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')
        self.root.title('Document Detailer')
        self.root.iconbitmap('D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\document.ico')

        self.im_enter = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\enter.png").subsample(30)

        self.text_label = tk.Label(self.root, text="TEXT:")
        self.text_box = tk.Text(self.root, width=59, height=10, wrap=tk.WORD)
        self.word_label = tk.Label(self.root, text="Number of words: 0")
        self.line_label = tk.Label(self.root, text="Number of lines: 0")
        self.space_label = tk.Label(self.root, text="Number of spaces: 0")
        self.vowel_label = tk.Label(self.root, text="Number of vowels: 0")
        self.cons_label = tk.Label(self.root, text="Number of consonants: 0")
        self.button = tk.Button(self.root, image=self.im_enter, command=self.on_button_click)

        self.text_label.grid(row=0, column=0, padx=11, pady=(10, 1), sticky='w')
        self.text_box.grid(row=1, column=0, padx=11)
        self.word_label.grid(row=2, column=0,  padx=11, pady=(10, 0), sticky='w')
        self.line_label.grid(row=3, column=0,  padx=11, pady=1, sticky='w')
        self.space_label.grid(row=4, column=0,  padx=11, pady=1, sticky='w')
        self.vowel_label.grid(row=5, column=0,  padx=11, pady=1, sticky='w')
        self.cons_label.grid(row=6, column=0,  padx=11, pady=1, sticky='w')
        self.button.grid(row=7, column=0, padx=11, pady=4)

        self.root.mainloop()

    def on_button_click(self):
        text = self.text_box.get('1.0', tk.END)
        if text == '\n':
            self.word_label.config(text='Number of words: 0')
            self.line_label.config(text='Number of lines: 0')
            self.space_label.config(text='Number of spaces: 0')
            self.vowel_label.config(text='Number of vowels: 0')
            self.cons_label.config(text='Number of consonants: 0')
            return

        if text[-1:] != '\n':
            text = text + '\n'

        lines = spaces = vowels = cons = 0

        for i in text:
            if i == ' ':
                spaces += 1
            if i.isalpha():
                if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                    vowels += 1
                else:
                    cons += 1
            if i == '\n':
                lines += 1

        text = text.replace('\n', ' ')
        word_list = text.split(' ')
        word_list = list(filter(self.rem_null, word_list))
        words = len(word_list)

        self.word_label.config(text=f'Number of words: {words}')
        self.line_label.config(text=f'Number of lines: {lines}')
        self.space_label.config(text=f'Number of spaces: {spaces}')
        self.vowel_label.config(text=f'Number of vowels: {vowels}')
        self.cons_label.config(text=f'Number of consonants: {cons}')

    def rem_null(self, word):
        if word == ' ' or word == '' or word == '\n':
            return False
        else:
            return True




if __name__ == '__main__':
    Doc()
