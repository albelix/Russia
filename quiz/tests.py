from otree.api import Currency as c, currency_range, expect, Bot
from . import *

class PlayerBot(Bot):


    cases = ['correct', 'private_wrong', 'public_wrong', 'success_wrong', 'fail_wrong']

    def play_round(self):


        yield GroupAssigned
        yield Instructions

        yield SubmissionMustFail(Quiz)

        answers = dict(private=60, public=40, success=20, 
                fail=0, fair_rich=1, fair_poor=1)

        if self.case == 'correct':
            yield (
                Quiz,
                answers
            )
            yield Results
            yield FinalMessage

        if self.case == 'private_wrong':
            answers["private"] = 20
            yield SubmissionMustFail(Quiz, answers)

        if self.case == 'public_wrong':
            answers["public"] = 0
            yield SubmissionMustFail(Quiz, answers)        

        if self.case == 'success_wrong':
            answers["success"] = 0
            yield SubmissionMustFail(Quiz, answers)        

        if self.case == 'fail_wrong':
            answers["fail"] = 20
            yield SubmissionMustFail(Quiz, answers)        
