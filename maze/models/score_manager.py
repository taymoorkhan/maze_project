from models.score import Score
import json


class ScoreManager:
    """ This class uses aggregation to manage a collection of `Score` instances """

    def __init__(self):
        """ Uses a dictionary to store the scores obj with name keys"""
        self._scores = dict()

    @property
    def scores(self):
        """ Property Scores (list of values) """
        return list(self._scores.keys())

    def add_score(self, new_score, conditional=False):
        """[summary]
        adds a score to the score class
        :param score: obj of score class
        :type score: instance
        """

        if conditional == True:
            for score in self.scores:
                if new_score._score > score:
                    self._scores[new_score._score] = new_score
                    bar = 6000
                    for key in self._scores.keys():
                        if key < bar:
                            bar = key

                    for key in self._scores.keys():
                        if key == bar:
                            del self._scores[key]
                            return

        else:
            self._scores[new_score._score] = new_score

    def remove_score(self, name):
        """[summary]
        removes a score obj entry from the manager class
        :param name: obj
        :type name: instance of score class
        """
        for key, value in self._scores.items():
            if name == value._name:
                del self._scores[key]
                return

    def __len__(self):
        """ Returns an integer (number of items managed by the instance) """
        return len(self._scores)

    def get_scores(self):
        """[summary]

        :return: returns a dict representation of all the scores
        :rtype: list
        """
        getScore = []

        for score in self._scores.values():
            getScore.append(score.to_dict())
        return sorted(getScore, key=lambda i: i['score'], reverse=True)

    def serialize(self):
        """return a dictionary representation of scores
        """
        return {"scores": self.get_scores()}

    def to_json(self):
        """ writes to a json file

        :param json_file: file to write to
        :type json_file: json
        """
        # serialize data and store in json obj
        json_object = json.dumps(self.serialize())
        # write to json file
        with open("models/scores.json", "w") as outfile:
            outfile.write(json_object)

    def from_json(self):
        """ reads data from a json file and creates instance of score to add to instance of score manager

        :param json_file: json file
        :type json_file: JSON
        """
        # Opening JSON file 
        with open("models/scores.json", 'r') as openfile:
            # Reading from json file 
            json_object = json.load(openfile)
            count = 0
            for obj in json_object['scores']:
                name = obj['name']
                score = Score(obj['score'], obj['name'])
                self.add_score(score)

