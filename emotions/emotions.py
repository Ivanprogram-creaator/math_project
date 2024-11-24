from emotions.base_emotion import BaseEmotion


class Interest(BaseEmotion):
    def __init__(self):
        super().__init__('Интерес')


class Joy(BaseEmotion):
    def __init__(self):
        super().__init__('Радость')


class Grief(BaseEmotion):
    def __init__(self):
        super().__init__('Горе')


class Fear(BaseEmotion):
    def __init__(self):
        super().__init__('Страх')


class Hope(BaseEmotion):
    def __init__(self):
        super().__init__('Надежда')


class Rage(BaseEmotion):
    def __init__(self):
        super().__init__('Гнев')


class Neglect(BaseEmotion):
    def __init__(self):
        super().__init__('Пренебрежение')


class Satisfaction(BaseEmotion):
    def __init__(self):
        super().__init__('Удовлетворение')


# ==================================================================================================================== #

class Guilt(BaseEmotion):
    def __init__(self):
        super().__init__('Вина')


class Irresponsibility(BaseEmotion):
    def __init__(self):
        super().__init__('Безответственность')


class SelfEsteem(BaseEmotion):
    def __init__(self):
        super().__init__('Самоуважение')


class Responsibility(BaseEmotion):
    def __init__(self):
        super().__init__('Ответственность')


class Contempt(BaseEmotion):
    def __init__(self):
        super().__init__('Презрение')


class Antipathy(BaseEmotion):
    def __init__(self):
        super().__init__('Антипатия')


class Sympathy(BaseEmotion):
    def __init__(self):
        super().__init__('Симпатия')


class Respect(BaseEmotion):
    def __init__(self):
        super().__init__('Уважение')


# ==================================================================================================================== #

class Shame(BaseEmotion):
    def __init__(self):
        super().__init__('Стыд')


class Pride(BaseEmotion):
    def __init__(self):
        super().__init__('Гордость')


class Shyness(BaseEmotion):
    def __init__(self):
        super().__init__('Застенчивость')


class Confidence(BaseEmotion):
    def __init__(self):
        super().__init__('Уверенность в себе')


class Disgust(BaseEmotion):
    def __init__(self):
        super().__init__('Отвращение')


class Admiration(BaseEmotion):
    def __init__(self):
        super().__init__('Восхищение')


class Perturbation(BaseEmotion):
    def __init__(self):
        super().__init__('Возмущение')


class Approval(BaseEmotion):
    def __init__(self):
        super().__init__('Одобрение')


# ==================================================================================================================== #

class JoyForAnother(BaseEmotion):
    def __init__(self):
        super().__init__('Радость за другого')


class Pity(BaseEmotion):
    def __init__(self):
        super().__init__('Жалость')


class Greed(BaseEmotion):
    def __init__(self):
        super().__init__('Жадность')


class Generosity(BaseEmotion):
    def __init__(self):
        super().__init__('Щедрость')


class Envy(BaseEmotion):
    def __init__(self):
        super().__init__('Зависть')


class Thanksgiving(BaseEmotion):
    def __init__(self):
        super().__init__('Благодарность')


class Gloating(BaseEmotion):
    def __init__(self):
        super().__init__('Злорадство')


class Goodwill(BaseEmotion):
    def __init__(self):
        super().__init__('Доброжелательность')


# ==================================================================================================================== #

class Resentment(BaseEmotion):
    def __init__(self):
        super().__init__('Обида')


class Delight(BaseEmotion):
    def __init__(self):
        super().__init__('Восторг')


class Seeking(BaseEmotion):
    def __init__(self):
        super().__init__('Заискивание')


class Pretentiosity(BaseEmotion):
    def __init__(self):
        super().__init__('Претенциозность')


class Insult(BaseEmotion):
    def __init__(self):
        super().__init__('Оскорбление')


class Adoration(BaseEmotion):
    def __init__(self):
        super().__init__('Обожание')


class Suspiciousness(BaseEmotion):
    def __init__(self):
        super().__init__('Подозрительность')


class Credulity(BaseEmotion):
    def __init__(self):
        super().__init__('Доверчивость')


# ==================================================================================================================== #

class Bitterness(BaseEmotion):
    def __init__(self):
        super().__init__('Горечь')


class Celebration(BaseEmotion):
    def __init__(self):
        super().__init__('Торжество')


class Humiliation(BaseEmotion):
    def __init__(self):
        super().__init__('Униженность')


class Superiority(BaseEmotion):
    def __init__(self):
        super().__init__('Превосходство')


class Arrogance(BaseEmotion):
    def __init__(self):
        super().__init__('Надменность')


class Flattery(BaseEmotion):
    def __init__(self):
        super().__init__('Лесть')


class Indignation(BaseEmotion):
    def __init__(self):
        super().__init__('Негодование')


class SelfSatisfaction(BaseEmotion):
    def __init__(self):
        super().__init__('Самодовольство')
