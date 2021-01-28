from king_utils import utils

# Provision of sample lines from briefing document

valid_gameinstallation = "gameinstallation|jane|1|1587583122"
invalid_gameinstallation = "gameinstallation|jane|1587583122"

valid_gamepurchase = "gamepurchase|jane|1|1 Free Life|1587583122"
invalid_gamepurchase = "gamepurchase|jane|4|Skip Level Booster|1587583122"

valid_gamestart = "gamestart|jane|1|1587583122"
invalid_gamestart = "gamestart|jane|2|abcdefg"


def test_pass_gameinstallation():
    assert utils.line_check(valid_gameinstallation) == True

def test_fail_gameinstallation():
    assert utils.line_check(invalid_gameinstallation) == False

def test_pass_gamepurchase():
    assert utils.line_check(valid_gamepurchase) == True

def test_fail_gamepurchase():
    assert utils.line_check(invalid_gamepurchase) == False

def test_pass_gamestart():
    assert utils.line_check(valid_gamestart) == True

def test_fail_gamestart():
    assert utils.line_check(invalid_gamestart) == False
