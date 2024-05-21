'''
import keyboard

def is_key_pressed(key):
    return keyboard.is_pressed(key)

while True:
    if is_key_pressed('a'):
        print("Key 'a' is pressed!")
    if is_key_pressed('b'):
        print("Key 'b' is pressed!")
'''

'''
import pyperclip

def check_clipboard():
    previous_clipboard_content = ""
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content != previous_clipboard_content:
            print("Clipboard content:", clipboard_content)
            previous_clipboard_content = clipboard_content

if __name__ == "__main__":
    try:
        check_clipboard()
    except:
        pass
'''

'''
import tkinter as tk

def on_button_click(button_number):
    print("Button clicked:", button_number)

root = tk.Tk()
root.geometry("400x400")

# Function to create a button and attach the callback function
def create_button(button_number):
    return tk.Button(root, text=f"Button {button_number}", command=lambda: on_button_click(button_number))

# Create a hundred buttons using a loop
for i in range(1, 101):
    button = create_button(i)
    button.pack()

root.mainloop()
'''

# import keyboard
# while True:
#     if keyboard.read_key() == "ctrl+c":
#         print("You pressed 'a'.")
#         break


# import keyboard
#
# def on_ctrl_c_release(event):
#     if not keyboard.is_pressed('ctrl') and not keyboard.is_pressed('c'):
#         print("Ctrl+C released")
#
# # Register the callback for Ctrl+C release
# keyboard.on_release_key('ctrl', on_ctrl_c_release)



# from googletrans import Translator, LANGUAGES
# translator = Translator()
#
# print("Available languages:")
# for code, language in LANGUAGES.items():
#     print(f"{code}: {language}")
#
# source = input("Enter text to convert: ")
# translated_text = Translator.translate(text=source, src='english', dest='bengali')
# print(translated_text.text, translated_text.pronunciation)
import tkinter as tk

# Function to handle button click
def button_click(button_text):
    canvas.create_text(100, 100, text=f"Button Clicked: {button_text}", fill="red")

# Create the main application window
root = tk.Tk()
root.title("Canvas with Buttons")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create and place multiple buttons on the canvas
buttons = []

button_texts = ["Button 1", "Button 2", "Button 3", "Button 4"]

for i, text in enumerate(button_texts):
    button = tk.Button(root, text=text, command=lambda t=text: button_click(t))
    buttons.append(button)
    canvas.create_window(50, 50 + i * 40, window=button)

root.mainloop()

