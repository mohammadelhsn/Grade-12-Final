import winsound


def test():
    winsound.PlaySound("biggestbird.wav", winsound.SND_ASYNC)
    stopsound = int(input("press 1 stop sound"))
    if stopsound == 1:
        winsound.PlaySound(None, winsound.SND_ASYNC)
    else:
        pass


test()
