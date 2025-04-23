import numpy
import numpy as np
import ydf
import pandas as pd
from emotions import types
from emotions.base_emotion import BaseEmotion
from personality.base_character import BaseCharacter


class Person:
    IDs = {
        5: "1",
        3: "2",
        2: "3",
        1: "4",
        0: "5",
        4: "6"
    }
    IDs_rev = {
        "1": 5,
        "2": 3,
        "3": 2,
        "4": 1,
        "5": 0,
        "6": 4
    }

    def __init__(self, character: BaseCharacter):
        self.character: BaseCharacter = character
        self.model = ydf.load_model("model")

    def emotion_define(self, relationship=None, **kwargs) -> BaseEmotion:
        direction = kwargs["direction"]
        timeline = kwargs["timeline"]
        emotion_strength, emotion_indication = self._emotion_strength_and_indication(
            desire_value=kwargs["desire_value"],
            know_probability=kwargs["know_probability"],
            own_probability=kwargs["own_probability"],
            surprise_coef=kwargs["surprise_coef"]
        )
        emotion_type = self._get_emotion_type(kwargs["needs_percent"], direction, relationship)
        emotions: BaseEmotion = types[emotion_type][(emotion_indication, direction, timeline)]
        emotions.count_emotion_shade(emotion_value=emotion_strength)
        return emotions

    def _get_emotion_type(
            self,
            needs_percent: list[float],
            direction: bool,
            relationship: int
    ) -> str:
        df = pd.DataFrame(columns=["0", "1", "2", "3", "4", "5", "6"])
        df.loc[0] = needs_percent
        prediction = list(self.model.predict(df))[0]
        if direction or not relationship:
            prediction[self.IDs_rev["2"]] = -1
            prediction[self.IDs_rev["4"]] = -1
            prediction[self.IDs_rev["5"]] = -1
            prediction[self.IDs_rev["6"]] = -1
        if relationship == 1:
            prediction[self.IDs_rev["6"]] = -1
        elif relationship == -1:
            prediction[self.IDs_rev["4"]] = -1
            prediction[self.IDs_rev["5"]] = -1
        ans = self.IDs[int(np.argmax(prediction))]
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
