from emotions import types
from emotions.base_emotion import BaseEmotion
from personality.base_character import BaseCharacter
from personality.characters import ENTJ


class Person:
    def __init__(self, character: BaseCharacter):
        self.character: BaseCharacter = character

    def emotion_define(self, **kwargs) -> BaseEmotion:
        emotion_strength, emotion_indication = self._emotion_strength_and_indication(
            desire_value=kwargs["desire_value"],
            know_probability=kwargs["know_probability"],
            own_probability=kwargs["own_probability"]
        )
        emotion_type = self._get_emotion_type(kwargs['args'])
        direction = self._get_direction(kwargs['args'])
        timeline = self._get_timeline(kwargs["args"])
        emotion: BaseEmotion = types[emotion_type][(emotion_indication, direction, timeline)]
        emotion.count_emotion_shade(emotion_strength)
        return emotion

    def _get_timeline(self, *args) -> bool:
        return True

    def _get_direction(self, *args) -> bool:
        return True

    def _get_emotion_type(self, *args) -> str:
        return '1'

    def _emotion_strength_and_indication(
            self,
            desire_value: float,
            know_probability: float,
            own_probability: float
    ) -> (float, int):
        probability_percentage = self._probability_count(know_probability, own_probability)
        emotion_value = self.character.emotion_function(
            success_probability=probability_percentage,
            desire_value=desire_value
        )
        emotion_indication = self._emotion_indication(emotion_value)

        print(abs(emotion_value), emotion_indication)

        return abs(emotion_value), emotion_indication

    @staticmethod
    def _probability_count(know_probability: float, own_probability: float) -> float:
        return own_probability / know_probability

    @staticmethod
    def _emotion_indication(emotion_value: float) -> int:
        if emotion_value == abs(emotion_value):
            return 1
        else:
            return -1


person = Person(ENTJ())
print(person.emotion_define(desire_value=110,
                            know_probability=1,
                            own_probability=0.6,
                            args=[]
                            ))
