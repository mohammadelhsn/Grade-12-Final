import playsound
import time
import pathlib

audio = pathlib.Path().resolve()

playsound.playsound("afterpary.wav")

while True:
    time.sleep(5)
    print("hi")
