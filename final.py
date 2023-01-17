#############################################################################
# Author: Mohammad El-Hassan
# Description: Final Project
# Date Created: 01/16/2023
# Date Modified: 01/16/2023
#############################################################################
from winsound import PlaySound, SND_ASYNC, SND_ALIAS, SND_PURGE, SND_FILENAME, SND_LOOP
from typing import List
from graphics import *
import threading
import random
import time
import os


def clickAnimation(rectangle: Rectangle):
    rectangle.setFill("orange")
    time.sleep(0.3)
    rectangle.setFill("")


def setInterval(func, sec: int):
    def func_wrapper():
        setInterval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests
try:
    import pyttsx3
except ModuleNotFoundError:
    os.system("pip install pyttsx3")
    import pyttsx3


class Music:
    enabled: bool
    song: str

    def __init__(self) -> None:
        self.enabled = False
        self.song = ""

    def isEnabled(self):
        if self.enabled == True:
            return "ON"
        else:
            return "OFF"

    def getSong(self):
        return self.song

    def stop(self):
        PlaySound(None, SND_ASYNC)

    def playSong(self, song):
        self.song = song
        print(self.song)
        PlaySound(self.song, SND_ASYNC | SND_FILENAME | SND_LOOP)
        return self


class Settings:
    difficulty: str
    players: int
    music: Music

    def __init__(self) -> None:
        self.difficulty = "medium"
        self.players = 1
        self.music = Music()

    def viewDifficulty(self):
        return self.difficulty

    def viewPlayers(self):
        return self.players

    def updateDifficulty(self, newValue):
        self.difficulty = newValue
        return self


class Player:
    playerName: str
    playerFile: str

    def __init__(self, name, file) -> None:
        self.playerName = name
        self.playerFile = file

    def viewName(self):
        return self.playerName

    def getFile(self):
        return self.playerFile

    def updateName(self, newName):
        self.playerName = newName
        return self

    def updateFile(self, newFile):
        self.playerFile = newFile
        return self


class Ball:
    img: str

    def __init__(self, img) -> None:
        self.img = img

    def respawn(self):
        pass

    def moveDown(self):
        pass


class Game:
    screen: str
    _settings: Settings
    players: List[Player]
    balls: List[Ball]

    def __init__(self):
        self._settings = Settings()

    def viewSettings(self):
        return self._settings

    def viewPlayers(self):
        return self.players

    def viewBalls(self):
        return self.balls

    def addPlayer(self, name, file):
        self.players.append(Player(name, file))
        return self

    def defaultScreen(self):
        defaultScreen = GraphWin("Dodge The Balls", 800, 500)
        Image(Point(0, 0), "Settings page.gif").draw(defaultScreen)
        defaultScreen.setCoords(
            -(defaultScreen.width / 2),
            -(defaultScreen.height / 2),
            (defaultScreen.width / 2),
            (defaultScreen.height / 2),
        )
        PLAY_BUTTON = Rectangle(Point(-100, -20), Point(100, 20)).draw(defaultScreen)
        Text(PLAY_BUTTON.getCenter(), "PLAY").setSize(20).draw(defaultScreen)
        INSTURCTION_BUTTON = Rectangle(Point(-100, -20), Point(0, -40)).draw(
            defaultScreen
        )
        Text(INSTURCTION_BUTTON.getCenter(), "INSTRUCTIONS").setSize(10).draw(
            defaultScreen
        )
        SETTINGS_BUTTON = Rectangle(Point(0, -20), Point(100, -40)).draw(defaultScreen)
        Text(SETTINGS_BUTTON.getCenter(), "SETTINGS").setSize(10).draw(defaultScreen)
        while True:
            pt = defaultScreen.getMouse()
            if INSTURCTION_BUTTON.clicked(pt):
                clickAnimation(INSTURCTION_BUTTON)
                print("Instruction button clicked!")
                defaultScreen.close()
                self.instructions()
                break
            if SETTINGS_BUTTON.clicked(pt):
                clickAnimation(SETTINGS_BUTTON)
                defaultScreen.close()
                print("Settings button clicked")
                self.settings()
                break
            if PLAY_BUTTON.clicked(pt):
                clickAnimation(PLAY_BUTTON)
                print("Play button clicked")
                defaultScreen.close()
                self.gameScreen()
                break
        defaultScreen.close()

    def gameScreen(self):
        gameScreen = GraphWin("Game Screen", 800, 500)
        Image(Point(0, 0), "Blue Sky.gif").draw(gameScreen)
        while True:
            break
        gameScreen.getMouse()
        gameScreen.close()

    def settings(self):
        settingsScreen = GraphWin("Settings", 800, 500)
        Image(Point(0, 0), "Settings page.gif").draw(settingsScreen)
        settingsScreen.setCoords(
            -(settingsScreen.width / 2),
            -(settingsScreen.height / 2),
            (settingsScreen.width / 2),
            (settingsScreen.height / 2),
        )
        MUSIC_ON = Rectangle(Point(-350, 150), Point(-300, 200)).draw(settingsScreen)
        MUSIC_OFF = Rectangle(Point(-250, 150), Point(-200, 200)).draw(settingsScreen)
        AFTERPARTY = Rectangle(Point(-350, 50), Point(-250, 100))
        BIGGESTBIRD = Rectangle(Point(-200, 50), Point(-100, 100))
        RICKROLL = Rectangle(Point(-50, 50), Point(50, 100))
        SEARCH = Rectangle(Point(275, 50), Point(350, 100))
        BACK = Rectangle(Point(-50, -150), Point(50, -200)).draw(settingsScreen)
        Text(MUSIC_ON.getCenter(), "ON").setSize(15).draw(settingsScreen)
        Text(MUSIC_OFF.getCenter(), "OFF").setSize(15).draw(settingsScreen)
        at = Text(AFTERPARTY.getCenter(), "AFTER PARTY").setSize(10)
        bbt = Text(BIGGESTBIRD.getCenter(), "BIGGEST BIRD").setSize(10)
        rrt = Text(RICKROLL.getCenter(), "RICK ROLL").setSize(10)
        entry = Entry(Point(175, 75), 17)
        st = Text(SEARCH.getCenter(), "Search\nText")
        Text(BACK.getCenter(), "BACK").draw(settingsScreen)
        while True:
            if self._settings.music.isEnabled() == "ON":
                MUSIC_OFF.setFill("")
                MUSIC_ON.setFill("orange")
            else:
                MUSIC_ON.setFill("")
                MUSIC_OFF.setFill("orange")
            pt = settingsScreen.getMouse()
            if MUSIC_ON.clicked(pt):
                clickAnimation(MUSIC_ON)
                print("Music ON Clicked")
                self._settings.music.enabled = True
                AFTERPARTY.draw(settingsScreen)
                BIGGESTBIRD.draw(settingsScreen)
                RICKROLL.draw(settingsScreen)
                SEARCH.draw(settingsScreen)
                at.draw(settingsScreen)
                bbt.draw(settingsScreen)
                rrt.draw(settingsScreen)
                entry.draw(settingsScreen)
                st.draw(settingsScreen)
                continue
            if MUSIC_OFF.clicked(pt):
                clickAnimation(MUSIC_OFF)
                self._settings.music.enabled = False
                AFTERPARTY.undraw()
                BIGGESTBIRD.undraw()
                RICKROLL.undraw()
                SEARCH.undraw()
                at.undraw()
                bbt.undraw()
                rrt.undraw()
                entry.undraw()
                st.undraw()
                self._settings.music.stop()
                continue
            if AFTERPARTY.clicked(pt):
                clickAnimation(AFTERPARTY)
                PlaySound("afterparty.wav", SND_ASYNC | SND_FILENAME | SND_LOOP)
            if BIGGESTBIRD.clicked(pt):
                clickAnimation(BIGGESTBIRD)
                PlaySound("biggestbird.wav", SND_ASYNC | SND_FILENAME | SND_LOOP)
            if RICKROLL.clicked(pt):
                clickAnimation(RICKROLL)
                PlaySound("rickroll.wav", SND_ASYNC | SND_FILENAME | SND_LOOP)
            if SEARCH.clicked(pt):
                clickAnimation(SEARCH)
                query = entry.getText()
                engine = pyttsx3.init()
                response = requests.get(
                    f"https://some-random-api.ml/lyrics?title={query}"
                )
                data = response.json()
                lyrics = data["lyrics"].split("\n")
                if len(data) == 1:
                    print("No result(s) found! Please try a different song!")
                result_name = data["title"]
                engine.save_to_file(lyrics, f"{result_name}.wav")
                engine.runAndWait()
                PlaySound(f"{result_name}.wav", SND_ASYNC | SND_FILENAME | SND_LOOP)
            if BACK.clicked(pt):
                clickAnimation(BACK)
                settingsScreen.close()
                break
            continue

    def instructions(self):
        instructionsScreen = GraphWin("Instructions", 800, 500)
        Image(Point(0, 0), "Settings page.gif").draw(instructionsScreen)
        instructionsScreen.getMouse()
        instructionsScreen.close()


while True:
    game = Game()
    game.defaultScreen()
