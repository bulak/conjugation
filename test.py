import random
import tkinter as tk
from tkinter import simpledialog

from fr_test import FrenchTester


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Le French Tester")
        self.tester = FrenchTester()
        self.pack()
#        self.create_widgets()
#        self.ask_question()
        self.run_test()

    def run_test(self):
        outtext = tk.Label(self, "French conjugation test")
        intext = tk.Entry(self, width=20)
        for verb, tense, answer in self.tester.prepare_test():
            if not answer:
                print("Problem: {} | {}".format(verb, tense))
                continue
            possible_prenoms = self.tester.prenoms[len(answer)]
            prenoms = random.sample(possible_prenoms, 2)
            for prenom in prenoms:
                prenom_index = possible_prenoms.index(prenom)
                question = "'{}' - '{}' - '{}': ".format(
                    verb, "/".join(tense), prenom)
                response = self.ask_question(question)
                outtext.configure(text=question)
                if response != answer[prenom_index]:
                    print("Non! C'est <<{}>>".format(answer[prenom_index]))


    def ask_question(self, question):
        answer = simpledialog.askstring(
            "Input", question, parent=self.master)
        return answer
        
    def create_board(self):
        self.board = {}
        for r in range(3):
            for c in range(4):
                self.board[(r, c)] = tk.Button(
                    self, text = "O").grid(row=r, column=c)
                
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
