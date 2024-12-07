import numpy

import config
from emotions import types
from emotions.base_emotion import BaseEmotion
from personality.base_character import BaseCharacter
from personality.characters import ENTJ


class Person:
    def __init__(self, character: BaseCharacter):
        self.character: BaseCharacter = character

    def emotion_define(self, relationship=None, **kwargs) -> BaseEmotion:
        direction = kwargs["direction"]
        timeline = kwargs["timeline"]
        emotion_strength, emotion_indication = self._emotion_strength_and_indication(
            desire_value=kwargs["desire_value"],
            know_probability=kwargs["know_probability"],
            own_probability=kwargs["own_probability"],
            surprise_coef=kwargs["surprise_coef"]
        )
        emotion_type = self._get_emotion_type(emotion_strength, kwargs["needs_percent"], direction, relationship)
        emotions: BaseEmotion = types[emotion_type][(emotion_indication, direction, timeline)]
        emotions.count_emotion_shade(emotion_strength)
        return emotions

    def _get_emotion_type(
            self,
            emotion_strength: float,
            needs_percent: list[float],
            direction: bool,
            relationship: int
    ) -> str:
        data = config.EMOTIONS_TYPES_PERCENT
        if direction or not relationship:
            del data["2"]
            del data["4"]
            del data["5"]
            del data["6"]
        if relationship == 1:
            del data["6"]
        elif relationship == -1:
            del data["4"]
            del data["5"]
        for key, val in data.items():
            data[key] = (numpy.array(needs_percent) * numpy.array(val) * emotion_strength).sum()
        ans = max(data, key=data.get)
        return ans

    def _emotion_strength_and_indication(
            self,
            desire_value: float,
            know_probability: float,
            own_probability: float,
            surprise_coef: float
    ) -> (float, int):
        probability_percentage = self._probability_count(know_probability, own_probability)
        emotion_value = self.character.emotion_function(
            success_probability=probability_percentage,
            desire_value=desire_value,
            surprise_coef=surprise_coef
        )
        emotion_indication = numpy.sign(emotion_value)

        print(abs(emotion_value), emotion_indication)

        return abs(emotion_value), emotion_indication

    @staticmethod
    def _probability_count(know_probability: float, own_probability: float) -> float:
        return own_probability / know_probability
