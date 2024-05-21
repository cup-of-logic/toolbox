from googletrans import Translator, LANGUAGES
import tkinter as tk

class Translate:
    def __init__(self):
        self.WIDTH, self.HEIGHT, self.X_POS, self.Y_POS = 500, 300, 300, 100
        self.trans_text = self.text = self.from_lang = self.to_lang = ""
        self.translator = Translator()

        self.main()

    def main(self):
        self.root = tk.Toplevel()
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}")
        self.root.title("Language Translator")
        self.root.iconbitmap("D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\language.ico")

        self.im_trans = tk.PhotoImage(file="D:\\Priyanshu Maity\\Python\\PROJECTS\\Toolbox\\icons\\trans.png").subsample(30)

        self.from_label = tk.Label(self.root, text="From:").grid(row=0, column=0, padx=(20, 0), pady=(10, 10))
        self.from_entry = tk.Entry(self.root, width=30)
        self.from_entry.grid(row=0, column=1, pady=(10, 10))

        self.to_label = tk.Label(self.root, text="To:").grid(row=0, column=2, padx=(20, 0), pady=(10, 10))
        self.to_entry = tk.Entry(self.root, width=30)
        self.to_entry.grid(row=0, column=3, pady=(10, 10))

        self.text_label = tk.Label(self.root, text="Text:").grid(row=1, column=0, padx=(20, 0))
        self.text_entry = tk.Entry(self.root, width=60)
        self.text_entry.grid(row=1, column=1, columnspan=3)

        self.trans_button = tk.Button(self.root, image=self.im_trans, command=self.click_button).grid(row=1, column=4)

        self.disp_label = tk.Label(self.root, text="", font=("Arial, 10"))
        self.disp_label.grid(row=2, column=0, columnspan=5, padx=(10, 0), pady=(30, 0), sticky="w")

        self.root.mainloop()

    def click_button(self):
        try:
            self.from_lang = self.from_entry.get()
            self.to_lang = self.to_entry.get()
            self.text = self.text_entry.get()

            self.trans_text = self.translator.translate(self.text, src=self.from_lang, dest=self.to_lang).text

            if len(self.trans_text) > 50:
                c = 0
                for i in range(len(self.trans_text)):
                    if c > 50 and self.trans_text[i] == " ":
                        self.trans_text = self.trans_text[:i] + "\n" + self.trans_text[i+1:]
                        c = 0
                    c += 1

            self.disp_label.configure(text=self.trans_text)
        except:
            self.disp_label.configure(text="ERROR!")


if __name__ == '__main__':
    Translate()