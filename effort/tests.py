from otree.api import Currency as c, currency_range, expect, Bot
from . import *

import time

class PlayerBot(Bot):

    def play_round(self):

        if self.round_number == 1:
            yield Intro
            yield AddNumbers, dict(number_entered=0)

        if self.round_number == 2:
            self.player.participant.time_up = True
            yield AddNumbers, dict(number_entered=0)
            