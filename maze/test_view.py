from views.end import EndView
from views.start import StartView
import pytest

# this tests the Endview Class

@pytest.fixture
def end():
    return EndView()

@pytest.fixture
def start():
    return StartView()    



def test_position(end,start):
    """
    testing for correct button position
    """
    assert end.rect.x == 300    
    assert end.rect.y == 300

    assert start.rect.x == 500    
    assert start.rect.y == 250


