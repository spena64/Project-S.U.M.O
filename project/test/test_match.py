import os, sys
sys.path.append('../src')
import match
import threading
import time

def test_addPlayers1():
    matchObj = match.Match()
    matchObj.addPlayer('0000', [50, 50], 1, 30, 1)
    assert matchObj.getPlayerState('0000')["x"]

def test_addPlayers2():
    matchObj = match.Match()
    matchObj.addPlayer('0000', [100, 50], 1, 30, 1)
    assert matchObj.getPlayerState('0000')["x"]

def test_movePlayer1():
    matchObj = match.Match()
    matchObj.addPlayer('0000', [25, 25], 1, 30, 1)
    matchThread = threading.Thread(target=matchObj.runGameLoop, daemon=True)
    matchThread.start()
    matchObj.setPlayerInput('0000', 0, 1)
    time.sleep(0.05)
    assert matchObj.getPlayerState('0000')["y"] > 25

def test_movePlayer2():
    matchObj = match.Match()
    matchObj.addPlayer('0000', [25, 25], 1, 30, 1)
    matchThread = threading.Thread(target=matchObj.runGameLoop, daemon=True)
    matchThread.start()
    matchObj.setPlayerInput('0000', -1, -1)
    time.sleep(0.05)
    assert matchObj.getPlayerState('0000')["x"] < 25
    assert matchObj.getPlayerState('0000')["y"] < 25

def test_normalize1():
    matchObj = match.Match()
    vector = matchObj.normalizeInput(1, 1)
    assert vector[0].__round__(3) == 0.707
    assert vector[1].__round__(3) == 0.707

def test_normalize2():
    matchObj = match.Match()
    vector = matchObj.normalizeInput(-1, 1)
    assert vector[0].__round__(3) == -0.707
    assert vector[1].__round__(3) == 0.707

def test_normalize3():
    matchObj = match.Match()
    vector = matchObj.normalizeInput(2, 3)
    assert vector[0].__round__(3) == 0.555
    assert vector[1].__round__(3) == 0.832

def test_normalize4():
    matchObj = match.Match()
    vector = matchObj.normalizeInput(0, 0)
    assert vector[0].__round__(3) == 0.0
    assert vector[1].__round__(3) == 0.0
