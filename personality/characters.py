from personality.base_character import BaseCharacter


class ENTP(BaseCharacter):
    def __init__(self):
        super().__init__(0.4, 2.3)


class ENFP(BaseCharacter):
    def __init__(self):
        super().__init__(0.4, 1)


class INTP(BaseCharacter):
    def __init__(self):
        super().__init__(0.55, 0.7)


class INFP(BaseCharacter):
    def __init__(self):
        super().__init__(0.65, 0.7)


class ESTP(BaseCharacter):
    def __init__(self):
        super().__init__(0.55, 1.5)


class ESFP(BaseCharacter):
    def __init__(self):
        super().__init__(0.53, 2.3)


class ISTP(BaseCharacter):
    def __init__(self):
        super().__init__(0.55, 0.7)


class ISFP(BaseCharacter):
    def __init__(self):
        super().__init__(0.45, 1)


class ESFJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.45, 2)


class ENFJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.45, 2)


class ISFJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.45, 1.7)


class INFJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.4, 2.3)


class ESTJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.5, 0.9)


class ENTJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.43, 1.6)


class INTJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.37, 0.8)


class ISTJ(BaseCharacter):
    def __init__(self):
        super().__init__(0.42, 2)
