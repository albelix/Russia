from otree.api import *

from settings import LANGUAGE_CODE, LAB_CODE

if LAB_CODE == "loyola":
    from settings import URLQUALTRICS


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


def creating_session(subsession):

    if subsession.round_number == 1:
        # The below code only runs if we are running this app in isolation - not in the full experiment
        # If running this app in isolation, set the participant vars so that it works
        # For the full experiment, group type should be set earlier
        # For testing
        if subsession.session.config["name"] == "payment":

            players = subsession.get_players()
            for player in players:
                player.participant.is_dropout=False
                player.participant.IDQualtrics = "test-id"
                player.participant.total_payout_local_currency = "test-amount"


class C(BaseConstants):
    NAME_IN_URL = 'payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    WVS_luck = models.FloatField(label=Lexicon.WVS_luck_label,
                                choices=[1,2,3,4,5,6,7,8,9,10],
                                widget=widgets.RadioSelectHorizontal
                                )

    WVS_responsibility = models.FloatField(label=Lexicon.WVS_responsibility_label,
                                choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 widget=widgets.RadioSelectHorizontal
                                 )
    email_address = models.StringField(label="Please provide your Warwick (or other) email address. NOTE: This is used only for payment purposes. Your data will be anonymised.")

    income = models.StringField(label=Lexicon.ExtraDemographics_income_label,
            choices=Lexicon.ExtraDemographics_income_choices
            )

    field_of_study = models.StringField(label=Lexicon.ExtraDemographics_field_of_study_label,
            choices=[
                Lexicon.humanities, 
                Lexicon.economics,
                Lexicon.psychology,
                Lexicon.social_science_other,
                Lexicon.natural_science,
                Lexicon.applied_science,
                Lexicon.science_other,
                Lexicon.other,
                Lexicon.prefer_not_to_say
                ]
            )

    macarthur_ladder = models.StringField(label=Lexicon.ExtraDemographics_macarthur_ladder_label,
                                choices=["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", Lexicon.prefer_not_to_say],
                                 )

    telefono = models.StringField(label=Lexicon.telefono
                                  )

    telefono2 = models.StringField(label=Lexicon.telefono2
                                  )

    metodopago = models.StringField(label=Lexicon.metodopago,
                                choices=Lexicon.metodopago_choices
                                )


# PAGES
class WVS(Page):
    form_model = "player"
    if LANGUAGE_CODE == "en":
        form_fields = ["WVS_luck", "WVS_responsibility", "email_address"]
    elif LANGUAGE_CODE == "hu":
        form_fields = ["WVS_luck", "WVS_responsibility", "email_address"]
    else:
        form_fields = ["WVS_luck", "WVS_responsibility"]
    # removed "email_address" for Colombia

    @staticmethod
    def is_displayed(player):
        if player.participant.is_dropout:
            return False
        return True

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}


class ExtraDemographics(Page):

    form_model = "player"
    if LAB_CODE == "bogota":
        form_fields = ["income", "field_of_study", "macarthur_ladder", "telefono", "telefono2", "metodopago"]
    else:
        form_fields = ["income", "field_of_study", "macarthur_ladder"]

    @staticmethod
    def is_displayed(player):
        if player.participant.is_dropout:
            return False
        return True

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon,
            "LAB_CODE": LAB_CODE}

    def error_message(self, response):
        if LAB_CODE == "bogota":
            if response['telefono2'] != response['telefono']:
                return Lexicon.telefono_error_message
        else:
            return False


class ThankYou(Page):

    @staticmethod
    def vars_for_template(player: Player):
        if LAB_CODE == "loyola":
            return {"LANGUAGE_CODE": LANGUAGE_CODE,
                "Lexicon": Lexicon,
                "LAB_CODE":LAB_CODE,
                "URLQUALTRICS": URLQUALTRICS+"?ID="+str(player.participant.IDQualtrics)+"&Payoff="+str(player.participant.total_payout_local_currency)+"&Session_Code="+str(player.session.code)
                }
        elif LAB_CODE == "bogota":
            return {"LANGUAGE_CODE": LANGUAGE_CODE,
                "Lexicon": Lexicon,
                "LAB_CODE":LAB_CODE
                }
        else:
            return {
                "LANGUAGE_CODE": LANGUAGE_CODE,
                "Lexicon": Lexicon,
                "LAB_CODE": LAB_CODE}            


page_sequence = [WVS, ExtraDemographics, ThankYou]
