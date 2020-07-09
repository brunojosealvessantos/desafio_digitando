import pyautogui
import pyperclip
import time


class Bot:
    def __init__(self):
        pass

    def escrever(self, texto):
        pyperclip.copy(texto)
        pyautogui.click(x=27, y=73, duration=2)
        pyautogui.hotkey('ctrl', 'v')


bot = Bot()
bot.escrever('Mestres da Automação!')
