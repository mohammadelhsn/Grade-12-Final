from typing import List
from graphics import *
import winsound
import random
import time
import os

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

    def playSong(self, song):
        return self


class Settings:
    difficulty = ""
    players = 1
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
                print("Instruction button clicked!")
                defaultScreen.close()
                self.instructions()
                break
            if SETTINGS_BUTTON.clicked(pt):
                defaultScreen.close()
                print("Settings button clicked")
                self.settings()
                break
            if PLAY_BUTTON.clicked(pt):
                print("Play button clicked")
                defaultScreen.close()
                self.gameScreen()
                break
        defaultScreen.close()

    def gameScreen(self):
        gameScreen = GraphWin("Game Screen", 800, 500)
        Image(Point(0, 0), "Blue Sky.gif").draw(gameScreen)

        while True:
            # check for keys that are pressed, if they are pressed, move the character around.
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
        Text(MUSIC_ON.getCenter(), "ON").setSize(15).draw(settingsScreen)
        Text(MUSIC_OFF.getCenter(), "OFF").setSize(15).draw(settingsScreen)

        while True:
            if self._settings.music.isEnabled() == "ON":
                MUSIC_OFF.setFill("")
                MUSIC_ON.setFill("orange")
            else:
                MUSIC_ON.setFill("")
                MUSIC_OFF.setFill("orange")

            pt = settingsScreen.getMouse()

            if MUSIC_ON.clicked(pt):
                print("Music ON Clicked")
                self._settings.music.enabled = True
                continue
            if MUSIC_OFF.clicked(pt):
                print("Music OFF Clicked")
                self._settings.music.enabled = False
                continue
            continue

    def instructions(self):
        instructionsScreen = GraphWin("Instructions", 800, 500)
        Image(Point(0, 0), "Settings page.gif").draw(instructionsScreen)
        instructionsScreen.getMouse()
        instructionsScreen.close()


while True:
    game = Game()
    game.defaultScreen()
