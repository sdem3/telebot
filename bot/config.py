TOKEN = "5694485123:AAHFGjLTG9MljSTIEa_4jEuE-zeE0Dp1tGI"

class Question:
    def __init__(self, text, keyboard):
        self.text = text

        self.keyboard = keyboard

class Answer:
    def __init__(self, text, value):
        self.text = text
        self.value = value