import random
from colorama import Fore, init
import os
import time


init(autoreset=True)
if os.name =="posix":
    sistema = "clear"
else:
    sistema = "cls"

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA]
while True:
    for i in range(30):
        treeText = " " * (29 - i)
        treeText += "".join([random.choice(colors) + ("#" if j % 2 == 0 else " ") for j in range(i * 2 + 1)])
        print(treeText)
    for i in range(3):
        print(" " * 27 + f"{'# '.join([random.choice(colors) for _ in range(3)])}#")
    time.sleep(0.5)
    os.system(sistema)