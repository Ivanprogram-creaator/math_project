class BaseCharacter:
    """Base class for Unga's type of characters
    Unga's type of character builds on four binary params:
    I/E - introversion/extravert
    N/S - intuition/sensing
    T/F - thinking/feeling
    J/P - judging/perceiving
    """

    def __init__(self, positivity: float, emotional_ratio: float, emotion_function: callable = None):
        self.emotional_ratio: float = emotional_ratio
        self.positivity: float = positivity
        self.emotion_function: callable = emotion_function if emotion_function else self.base_function

    def base_function(self, success_probability: float, desire_value: float, surprise_coef: float) -> float:
        emotion_strength = (success_probability - self.positivity) * self.emotional_ratio * desire_value * (
                    surprise_coef + 0.5) ** 1.5
        return emotion_strength
