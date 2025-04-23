from emotions.base_emotion import BaseEmotion
MOOD = 0
EMOTION = 2.8
AFFECT = 10

class Interest(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Любопытство', '"Настроение"'],
            EMOTION: ['Интерес', '"Эмоция"'],
            AFFECT: ['Увлечение', '"Аффект"']
        }
        super().__init__('Интерес', shades=shades)


class Joy(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Счастье', '"Настроение"'],
            EMOTION: ['Радость', '"Эмоция"'],
            AFFECT: ['Экстаз', '"Аффект"']
        }
        super().__init__('Радость', shades=shades)


class Grief(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Уныние', '"Настроение"'],
            EMOTION: ['Горе', '"Эмоция"'],
            AFFECT: ['Отчаяние', '"Аффект"']
        }
        super().__init__('Горе', shades=shades)


class Fear(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Тревога', '"Настроение"'],
            EMOTION: ['Страх', '"Эмоция"'],
            AFFECT: ['Ужас', '"Аффект"']
        }
        super().__init__('Страх', shades=shades)


class Hope(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Оптимизм', '"Настроение"'],
            EMOTION: ['Надежда', '"Эмоция"'],
            AFFECT: ['Надежда', '"Аффект"']
        }
        super().__init__('Надежда', shades=shades)


class Rage(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Раздражение', '"Настроение"'],
            EMOTION: ['Гнев', '"Эмоция"'],
            AFFECT: ['Ярость', '"Аффект"']
        }
        super().__init__('Гнев', shades=shades)


class Neglect(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Безразличие', '"Настроение"'],
            EMOTION: ['Пренебрежение', '"Эмоция"'],
            AFFECT: ['Ненависть', '"Аффект"']
        }
        super().__init__('Пренебрежение', shades=shades)


class Satisfaction(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Спокойствие', '"Настроение"'],
            EMOTION: ['Удовлетворение', '"Эмоция"'],
            AFFECT: ['Удовлетворение', '"Аффект"']
        }
        super().__init__('Удовлетворение', shades=shades)


# ==================================================================================================================== #

class Guilt(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Грусть', '"Настроение"'],
            EMOTION: ['Вина', '"Эмоция"'],
            AFFECT: ['Вина', '"Аффект"']
        }
        super().__init__('Вина', shades=shades)


class Irresponsibility(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Безответственность', '"Настроение"'],
            EMOTION: ['Безответственность', '"Эмоция"'],
            AFFECT: ['Безответственность', '"Аффект"']
        }
        super().__init__('Безответственность', shades=shades)


class SelfEsteem(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Уверенность', '"Настроение"'],
            EMOTION: ['Самоуважение', '"Эмоция"'],
            AFFECT: ['Самоуважение', '"Аффект"']
        }
        super().__init__('Самоуважение', shades=shades)


class Responsibility(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Серьезность', '"Настроение"'],
            EMOTION: ['Ответственность', '"Эмоция"'],
            AFFECT: ['Решительность', '"Аффект"']
        }
        super().__init__('Ответственность', shades=shades)


class Contempt(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Презрение', '"Настроение"'],
            EMOTION: ['Презрение', '"Эмоция"'],
            AFFECT: ['Ненависть', '"Аффект"']
        }
        super().__init__('Презрение', shades=shades)


class Antipathy(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Антипатия', '"Настроение"'],
            EMOTION: ['Антипатия', '"Эмоция"'],
            AFFECT: ['Антипатия', '"Аффект"']
        }
        super().__init__('Антипатия', shades=shades)


class Sympathy(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Симпатия', '"Настроение"'],
            EMOTION: ['Симпатия', '"Эмоция"'],
            AFFECT: ['Симпатия', '"Аффект"']
        }
        super().__init__('Симпатия', shades=shades)


class Respect(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Уважение', '"Настроение"'],
            EMOTION: ['Уважение', '"Эмоция"'],
            AFFECT: ['Уважение', '"Аффект"']
        }
        super().__init__('Уважение', shades=shades)


# ==================================================================================================================== #

class Shame(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Досада', '"Настроение"'],
            EMOTION: ['Стыд', '"Эмоция"'],
            AFFECT: ['Ужас', '"Аффект"']
        }
        super().__init__('Стыд', shades=shades)


class Pride(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Уверенность', '"Настроение"'],
            EMOTION: ['Гордость', '"Эмоция"'],
            AFFECT: ['Гордость', '"Аффект"']
        }
        super().__init__('Гордость', shades=shades)


class Shyness(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Неловкость', '"Настроение"'],
            EMOTION: ['Застенчивость', '"Эмоция"'],
            AFFECT: ['Испуг', '"Аффект"']
        }
        super().__init__('Застенчивость', shades=shades)


class Confidence(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Спокойствие', '"Настроение"'],
            EMOTION: ['Уверенность в себе', '"Эмоция"'],
            AFFECT: ['Уверенность в себе', '"Аффект"']
        }
        super().__init__('Уверенность в себе', shades=shades)


class Disgust(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Отвращение', '"Настроение"'],
            EMOTION: ['Отвращение', '"Эмоция"'],
            AFFECT: ['Брезгливость', '"Аффект"']
        }
        super().__init__('Отвращение', shades=shades)


class Admiration(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Благоговение', '"Настроение"'],
            EMOTION: ['Восхищение', '"Эмоция"'],
            AFFECT: ['Восхищение', '"Аффект"']
        }
        super().__init__('Восхищение', shades=shades)


class Perturbation(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Раздражение', '"Настроение"'],
            EMOTION: ['Возмущение', '"Эмоция"'],
            AFFECT: ['Гнев', '"Аффект"']
        }
        super().__init__('Возмущение', shades=shades)


class Approval(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Удовлетворение', '"Настроение"'],
            EMOTION: ['Одобрение', '"Эмоция"'],
            AFFECT: ['Одобрение', '"Аффект"']
        }
        super().__init__('Одобрение', shades=shades)


# ==================================================================================================================== #

class JoyForAnother(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Радость за другого', '"Настроение"'],
            EMOTION: ['Радость за другого', '"Эмоция"'],
            AFFECT: ['Счастье', '"Аффект"']
        }
        super().__init__('Радость за другого', shades=shades)


class Pity(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Сожаление', '"Настроение"'],
            EMOTION: ['Жалость', '"Эмоция"'],
            AFFECT: ['Печаль', '"Аффект"']
        }
        super().__init__('Жалость', shades=shades)


class Greed(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Жадность', '"Настроение"'],
            EMOTION: ['Жадность', '"Эмоция"'],
            AFFECT: ['Жадность', '"Аффект"']
        }
        super().__init__('Жадность', shades=shades)


class Generosity(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Удовлетворение', '"Настроение"'],
            EMOTION: ['Щедрость', '"Эмоция"'],
            AFFECT: ['Радость', '"Аффект"']
        }
        super().__init__('Щедрость', shades=shades)


class Envy(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Недовольство', '"Настроение"'],
            EMOTION: ['Зависть', '"Эмоция"'],
            AFFECT: ['Гнев', '"Аффект"']
        }
        super().__init__('Зависть', shades=shades)


class Thanksgiving(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Благодарность', '"Настроение"'],
            EMOTION: ['Благодарность', '"Эмоция"'],
            AFFECT: ['Благодарность', '"Аффект"']
        }
        super().__init__('Благодарность', shades=shades)


class Gloating(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Удовлетворение', '"Настроение"'],
            EMOTION: ['Злорадство', '"Эмоция"'],
            AFFECT: ['Радость', '"Аффект"']
        }
        super().__init__('Злорадство', shades=shades)


class Goodwill(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Доброжелательность', '"Настроение"'],
            EMOTION: ['Доброжелательность', '"Эмоция"'],
            AFFECT: ['Доброжелательность', '"Аффект"']
        }
        super().__init__('Доброжелательность', shades=shades)


# ==================================================================================================================== #

class Resentment(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Досада', '"Настроение"'],
            EMOTION: ['Обида', '"Эмоция"'],
            AFFECT: ['Гнев', '"Аффект"']
        }
        super().__init__('Обида', shades=shades)


class Delight(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Оптимизм', '"Настроение"'],
            EMOTION: ['Восторг', '"Эмоция"'],
            AFFECT: ['Экстаз', '"Аффект"']
        }
        super().__init__('Восторг', shades=shades)


class Seeking(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Заискивание', '"Настроение"'],
            EMOTION: ['Заискивание', '"Эмоция"'],
            AFFECT: ['Заискивание', '"Аффект"']
        }
        super().__init__('Заискивание', shades=shades)


class Pretentiosity(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Непонимание', '"Настроение"'],
            EMOTION: ['Претенциозность', '"Эмоция"'],
            AFFECT: ['Раздражение', '"Аффект"']
        }
        super().__init__('Претенциозность', shades=shades)


class Insult(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Раздражение', '"Настроение"'],
            EMOTION: ['Оскорбление', '"Эмоция"'],
            AFFECT: ['Оскорбление', '"Аффект"']
        }
        super().__init__('Оскорбление', shades=shades)


class Adoration(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Восхищение', '"Настроение"'],
            EMOTION: ['Обожание', '"Эмоция"'],
            AFFECT: ['Обожание', '"Аффект"']
        }
        super().__init__('Обожание', shades=shades)


class Suspiciousness(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Неспокойство', '"Настроение"'],
            EMOTION: ['Подозрительность', '"Эмоция"'],
            AFFECT: ['Тревога', '"Аффект"']
        }
        super().__init__('Подозрительность', shades=shades)


class Credulity(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Открытость', '"Настроение"'],
            EMOTION: ['Доверчивость', '"Эмоция"'],
            AFFECT: ['Доверчивость', '"Аффект"']
        }
        super().__init__('Доверчивость', shades=shades)


# ==================================================================================================================== #

class Bitterness(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Разочарование', '"Настроение"'],
            EMOTION: ['Горечь', '"Эмоция"'],
            AFFECT: ['Печаль', '"Аффект"']
        }
        super().__init__('Горечь', shades=shades)


class Celebration(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Торжество', '"Настроение"'],
            EMOTION: ['Торжество', '"Эмоция"'],
            AFFECT: ['Торжество', '"Аффект"']
        }
        super().__init__('Торжество', shades=shades)


class Humiliation(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Униженность', '"Настроение"'],
            EMOTION: ['Униженность', '"Эмоция"'],
            AFFECT: ['Униженность', '"Аффект"']
        }
        super().__init__('Униженность', shades=shades)


class Superiority(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Уверенность', '"Настроение"'],
            EMOTION: ['Превосходство', '"Эмоция"'],
            AFFECT: ['Превосходство', '"Аффект"']
        }
        super().__init__('Превосходство', shades=shades)


class Arrogance(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['', '"Настроение"'],
            EMOTION: ['', '"Эмоция"'],
            AFFECT: ['', '"Аффект"']
        }
        super().__init__('Надменность', shades=shades)


class Flattery(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Надменность', '"Настроение"'],
            EMOTION: ['Надменность', '"Эмоция"'],
            AFFECT: ['Презрение', '"Аффект"']
        }
        super().__init__('Лесть', shades=shades)


class Indignation(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Раздражение', '"Настроение"'],
            EMOTION: ['Негодование', '"Эмоция"'],
            AFFECT: ['Гнев', '"Аффект"']
        }
        super().__init__('Негодование', shades=shades)


class SelfSatisfaction(BaseEmotion):
    def __init__(self):
        shades = {
            MOOD: ['Удовлетворение', '"Настроение"'],
            EMOTION: ['Самодовольство', '"Эмоция"'],
            AFFECT: ['Восторг', '"Аффект"']
        }
        super().__init__('Самодовольство', shades=shades)
