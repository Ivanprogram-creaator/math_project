from emotions.base_emotion import BaseEmotion
from emotions.emotions import *

types = {
    '1': {
        (-1, True, True): Grief(),
        (1, True, True): Joy(),
        (-1, True, False): Fear(),
        (1, True, False): Hope(),
        (-1, False, True): Rage(),
        (1, False, True): Satisfaction(),
        (-1, False, False): Neglect(),
        (1, False, False): Interest(),
    },
    '2': {
        (-1, True, True): Guilt(),
        (1, True, True): SelfEsteem(),
        (-1, True, False): Irresponsibility(),
        (1, True, False): Responsibility(),
        (-1, False, True): Contempt(),
        (1, False, True): Respect(),
        (-1, False, False): Antipathy(),
        (1, False, False): Sympathy(),
    },
    '3': {
        (-1, True, True): Shame(),
        (1, True, True): Pride(),
        (-1, True, False): Shyness(),
        (1, True, False): Confidence(),
        (-1, False, True): Disgust(),
        (1, False, True): Admiration(),
        (-1, False, False): Perturbation(),
        (1, False, False): Approval(),
    },
    '4': {
        (-1, True, True): Pity(),
        (1, True, True): JoyForAnother(),
        (-1, True, False): Greed(),
        (1, True, False): Generosity(),
        (-1, False, True): Envy(),
        (1, False, True): Thanksgiving(),
        (-1, False, False): Gloating(),
        (1, False, False): Goodwill(),
    },
    '5': {
        (-1, True, True): Resentment(),
        (1, True, True): Delight(),
        (-1, True, False): Seeking(),
        (1, True, False): Pretentiosity(),
        (-1, False, True): Insult(),
        (1, False, True): Adoration(),
        (-1, False, False): Suspiciousness(),
        (1, False, False): Credulity(),
    },
    '6': {
        (-1, True, True): Bitterness(),
        (1, True, True): Celebration(),
        (-1, True, False): Humiliation(),
        (1, True, False): Superiority(),
        (-1, False, True): Indignation(),
        (1, False, True): SelfSatisfaction(),
        (-1, False, False): Arrogance(),
        (1, False, False): Flattery(),
    },
}
