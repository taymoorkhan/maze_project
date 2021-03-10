from models.score import Score
import pytest



@pytest.fixture
def score():
    return Score(10)

@pytest.fixture
def score2():
    return Score(15,'KOBE')



def test_constructor_invalid_int():
    """
    test that a ValueError is raised 
    """
    try:
        with pytest.raises(ValueError):
            player = Score('10') 


    except:
        assert False   

def test_constructor_invalid_incorrectvalue():
    """
    test that a ValueError is raised 
    """
    try:
        with pytest.raises(ValueError):
            player = Score(-100) 


    except:
        assert False 


def test_score_property(score):
    """[summary] test the getter of score class

    :param score: instance
    :type score: Score
    """
    assert type(Score.score) == property
    assert score.score == 10 

def test_name_property(score):
    """[summary] test getter for name of player

    :param score: instance
    :type score: Score
    """
    assert type(Score.name) == property
    assert score.name == 'Player' 








    

def test_dict_return(score):
    """[summary] test the return value

    :param score: instance
    :type score: Score
    """

    assert score.to_dict() == {"name": 'Player', "score": 10}       