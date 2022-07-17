import random

name = ['uoia', 'airone', 'scemotta', 'shhh', '']
PAROLE_CONSENTITE = ["regola 4", "piedi", "bunkerino"]


def generate_reply():
    return 'Zitta '+name[random.randint(0, 4)]


def check_message(msg):
    if not any(s in msg.lower().split() for s in PAROLE_CONSENTITE):
        return False
    return True
