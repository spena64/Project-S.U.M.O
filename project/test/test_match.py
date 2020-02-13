import os, sys
sys.path.append('../src')
import match
import time

def test_addPlayers1():
    match1 = match.Match()
    match1.addPlayer('0000', [50, 50], 1, 30, 1)
    assert match1.getPlayerLocation('0000') == [50, 50]

def test_addPlayers2():
    match1 = match.Match()
    match1.addPlayer('0000', [100, 50], 1, 30, 1)
    assert match1.getPlayerLocation('0000') == [100, 50]

def test_movePlayer1():
    match1 = match.Match()
    match1.addPlayer('0000', [25, 25], 1, 30, 1)
    match1.start()
    match1.setPlayerInput('0000', [0, 1])
    time.sleep(0.05)
    assert match1.getPlayerLocation('0000')[1] > 25
