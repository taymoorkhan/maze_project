from models.score_manager import ScoreManager
from models.score import Score
import pytest


@pytest.fixture
def scoremanager():
    return ScoreManager()


@pytest.fixture
def score():
    return Score(10)

@pytest.fixture
def score2():
    return Score(15,'KOBE')        


def test_score_manager(scoremanager):
    """[summary]test the connstuctor in score manager

    :param scoremanager: instance
    :type scoremanager: ScoreManager
    """

    assert len(scoremanager._scores) == 0
    assert type(scoremanager._scores) == dict 


def test_score(score):
    """[summary] test the return values of score class

    :param score: instance
    :type score: Score
    """

    assert score._name == 'Player'
    assert score._score == 10 

def test_add_score(score,scoremanager):
    """Test the adding and length methods of ScoreManager

    :param score: Instance
    :type score: Score
    :param scoremanager: instance
    :type scoremanager: ScoreManager
    """

    scoremanager.add_score(score)
    assert len(scoremanager._scores) == 1

    assert scoremanager.scores[0] == 10
    
    assert scoremanager.__len__() == 1 


def test_manager_scores_property(scoremanager):
    assert type(ScoreManager.scores) == property 


   
def test_manager_remove_scores_user(scoremanager, score):
    """[summary] Checks the remove_score method

    :param scoremanager: instance
    :type scoremanager: ScoreManager
    :param score: instance
    :type score: Score
    """
    for _ in range(0, 5):
        scoremanager.add_score(score)

    scoremanager.remove_score("Player")

    assert len(scoremanager) == 0


def test_manager_serialize(scoremanager, score):
    """Checks to see if the correct format is returned 

    :param scoremanager: instance
    :type scoremanager: ScoreManager
    :param score: instance
    :type score: Score
    """
    scoremanager.add_score(score) 
    assert scoremanager.serialize() == {"scores": [{'name': 'Player', 'score': 10}]}  

def test_score_order(scoremanager, score, score2):
    """This test checks to see if scores are put in the correct order

    :param scoremanager: instance
    :type scoremanager: ScoreManager
    :param score: instance
    :type score: Score
    :param score2: instance
    :type score2: Score
    """
    scoremanager.add_score(score)
    scoremanager.add_score(score2)

    assert scoremanager.get_scores() == [{"name": 'KOBE' , "score": 15},{"name": 'Player' , "score": 10}]    