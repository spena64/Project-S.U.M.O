import os, sys
sys.path.append('../src')
import match
import threading
import time

def test_add_players_1():
    match_obj = match.Match()
    match_obj.add_player('0000', [50, 50], 0.25, 30, 1)
    assert match_obj.get_player_state('0000')["x"] == 50

def test_add_players_2():
    match_obj = match.Match()
    match_obj.add_player('0000', [100, 50], 0.25, 30, 1)
    assert match_obj.get_player_state('0000')["x"] == 100

def test_move_player_1():
    match_obj = match.Match()
    match_obj.add_player('0000', [400, 400], 0.25, 30, 1)
    match_obj.add_player('0001', [400, 400], 0.25, 30, 1)
    match_thread = threading.Thread(target=match_obj.run_game_loop, daemon=True)
    match_thread.start()
    match_obj.set_player_input('0000', 0, 1)
    time.sleep(0.05)
    assert match_obj.get_player_state('0000')["x"] == 400
    assert match_obj.get_player_state('0000')["y"] > 400

def test_move_player_2():
    match_obj = match.Match()
    match_obj.add_player('0000', [400, 400], 0.25, 30, 1)
    match_obj.add_player('0001', [400, 400], 0.25, 30, 1)
    match_thread = threading.Thread(target=match_obj.run_game_loop, daemon=True)
    match_thread.start()
    match_obj.set_player_input('0000', -1, -1)
    time.sleep(0.05)
    assert match_obj.get_player_state('0000')["x"] < 400
    assert match_obj.get_player_state('0000')["y"] < 400

def test_normalize_1():
    match_obj = match.Match()
    vector = match_obj.normalize_input(1, 1)
    assert vector[0].__round__(3) == 0.707
    assert vector[1].__round__(3) == 0.707

def test_normalize_2():
    match_obj = match.Match()
    vector = match_obj.normalize_input(-1, 1)
    assert vector[0].__round__(3) == -0.707
    assert vector[1].__round__(3) == 0.707

def test_normalize_3():
    match_obj = match.Match()
    vector = match_obj.normalize_input(2, 3)
    assert vector[0].__round__(3) == 0.555
    assert vector[1].__round__(3) == 0.832

def test_normalize_4():
    match_obj = match.Match()
    vector = match_obj.normalize_input(0, 0)
    assert vector[0].__round__(3) == 0.0
    assert vector[1].__round__(3) == 0.0
