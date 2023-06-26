from otree.api import Currency as c, currency_range, expect, Bot
from . import *

import time

class PlayerBot(Bot):

    cases = [
        {"contribution_public":0, "contribution_private":0},
        {"contribution_public":0, "contribution_private":1},
        {"contribution_public":1, "contribution_private":0},
    ]

    def play_round(self):

        contribution_private = self.case["contribution_private"]
        contribution_public = self.case["contribution_public"]

        yield (
            Contribution, 
            dict(
                contribution_private=contribution_private, 
                contribution_public=contribution_public)
            )

        if self.round_number == C.NUM_ROUNDS:
            print("In here")
            expect(self.participant.group_pot, C.NUM_ROUNDS * 4 * contribution_public)
            expect(self.participant.private_pot, C.NUM_ROUNDS * contribution_private)
            yield GroupResult
