from otree.api import Currency as c, currency_range, expect, Bot
from . import *

class PlayerBot(Bot):
    def play_round(self):

        yield ParticipantInfo

        yield SubmissionMustFail(ParticipantConsent, dict(consent=False))

        yield ParticipantConsent, dict(consent=True)

        yield SubmissionMustFail(DemographicData)

        yield SubmissionMustFail(DemographicData, dict(age=None, gender=None))

        yield DemographicData, dict(age="18-24", gender="Female")

