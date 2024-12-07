class BaseEmotion:
    """Base class for emotions"""

    def __init__(self, name: str, shades: dict = None):
        self.name: str = name
        self.shades: dict = shades if shades else {0: [name, '"Эмоция"'], 10: ['Горечь']}
        self.shade = None

    def count_emotion_shade(self, emotion_value: float) -> None:
        shade_key = min(self.shades.keys(), key=lambda x: emotion_value - x if emotion_value - x >= 0 else 10000000)
        self.shade = self.shades[shade_key]

    def __repr__(self):
        return f"Возникла эмоция {self.name} с типом {self.shade[1]}"
