import os, sys
sys.path.append('../src')
import mymodule

def test_givevalue():
    assert mymodule.give_value() == 3
