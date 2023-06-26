from otree.api import *

import time

from settings import LANGUAGE_CODE, LAB_CODE

doc = """
Your app description
"""

if LANGUAGE_CODE == 'en':
    from lexicon_en import Lexicon
elif LANGUAGE_CODE == 'fr':
    from lexicon_fr import Lexicon
elif LANGUAGE_CODE == 'ja':
    from lexicon_ja import Lexicon
elif LANGUAGE_CODE == 'de':
    from lexicon_de import Lexicon
elif LANGUAGE_CODE == 'zh':
    from lexicon_zh import Lexicon
elif LANGUAGE_CODE == 'it':
    from lexicon_it import Lexicon
elif LANGUAGE_CODE == 'es':
    from lexicon_es import Lexicon
elif LANGUAGE_CODE == 'ko':
    from lexicon_ko import Lexicon
elif LANGUAGE_CODE == 'hu':
    from lexicon_hu import Lexicon
elif LANGUAGE_CODE == 'ru':
    from lexicon_ru import Lexicon


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(label=Lexicon.consent_question,
                                  choices=[
                                      [True, Lexicon.yes],
                                  ]
                                  )
    age = models.StringField(label=Lexicon.age_question,
                              choices=["18-24","25-34","35-44","45-54","55-64","65+",Lexicon.prefer_not_to_say]
                              )
    gender = models.StringField(label=Lexicon.gender_question,
                                choices=[Lexicon.female, Lexicon.male, Lexicon.non_binary, Lexicon.other, Lexicon.prefer_not_to_say]
                                )
# removing for Japan    WorkerID = models.StringField(label=Lexicon.worker_id_question)


# PAGES
class ParticipantInfo(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}


class ParticipantConsent(Page):
    form_model = "player"
    form_fields = ["consent"]

    @staticmethod
    def vars_for_template(player: Player):
        if LAB_CODE == "bogota":
            return {"LANGUAGE_CODE": LANGUAGE_CODE,
                "Lexicon": Lexicon,
                "LAB_CODE":LAB_CODE
                }
        else:
            return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}


class DemographicData(Page):
    form_model = "player"
    form_fields = ["age", "gender"] # removed "WorkerID" from this list for Japan

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.wait_page_arrival = time.time()
        player.participant.is_dropout = False

page_sequence = [ParticipantConsent, DemographicData] # removed ParticipantInfo for Japan
