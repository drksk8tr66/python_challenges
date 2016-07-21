from tkinter import *

morse = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..')
decode = lambda s: "".join([" " if x == '/' else chr(morse.index(x) + 97) for x in re.split('[^\.\-/]+', s)])
encode = lambda s: " ".join(["/" if x == " " else morse[ord(x) - 97] if ord(x) in range(97, 123) else "" for x in s.lower()]).strip()
coded_msg = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.canvas = Canvas(fr, height=100, width=100)
        self.canvas.pack()
        self.rect = self.canvas.create_rectangle(25, 25, 75, 75, fill="white")
        self.do_blink = False
        self.input_text = Entry(self)
        self.input_text.pack()
        self.morse_msg = self.input_text.get()
        self.i = 0
        start_button = Button(self, text="start blinking", command=self.start_blinking)
        stop_button = Button(self, text="stop blinking", command=self.stop_blinking)
        start_button.pack()
        stop_button.pack()

    def start_blinking(self):
        self.i = 0
        self.do_blink = True
        self.input_text.get()
        msg = self.input_text.get()
        self.morse_msg = encode(msg)
        print(self.morse_msg)
        self.blink()

    def stop_blinking(self):
        self.do_blink = False

    def blink_on(self):
        if self.do_blink:
            self.canvas.itemconfigure(self.rect, fill="red")

    def blink_off(self):
        if self.do_blink:
            self.canvas.itemconfigure(self.rect, fill="white")
            if self.i == len(self.morse_msg)-1:
                self.do_blink = False
            else:
                self.i += 1
                self.after(200, self.blink)

    def blink(self):
        if self.do_blink:
            if self.morse_msg[self.i] == '.':
                print(self.i)
                print("short")
                self.canvas.itemconfigure(self.rect, fill="red")
                self.after(500, self.blink_off)
            elif self.morse_msg[self.i] == '-':
                print(self.i)
                print("long")
                self.canvas.itemconfigure(self.rect, fill="red")
                self.after(1000, self.blink_off)
            elif self.morse_msg[self.i] == '/':
                print(self.i)
                print("pass")
                self.i += 1
                self.after(500, self.blink)
            else:
                self.i += 1
                self.after(500, self.blink)


if __name__ == "__main__":
    root = MyApp()
    root.mainloop()
