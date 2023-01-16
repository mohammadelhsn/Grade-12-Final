from winsound import *
from time import sleep
import pathlib

print(str(pathlib.Path(__file__).parent / "rickroll.wav"))
PlaySound("rickroll.wav", SND_ASYNC | SND_FILENAME | SND_LOOP)
while True:
    sleep(5)
    print("hi")
