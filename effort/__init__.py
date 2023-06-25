import time
import random

from settings import LANGUAGE_CODE

from otree.api import *

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
        # For the full experiment, wait_page_arrival is set in previous app
        # For testing
        if subsession.session.config["name"] == "effort":

            players = subsession.get_players()

            for player in players:
                player.participant.wait_page_arrival = time.time()
                player.participant.is_dropout = False


class C(BaseConstants):
    NAME_IN_URL = 'effort'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 50
    TASK_TIMER = 300 # 300 (5 minutes)
    WAIT_PAGE_TIME_OUT = 1200 # 1200 (20 minutes).

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.IntegerField(label=Lexicon.number_entered_question, max=1000, min=0)
    sum_of_numbers = models.IntegerField()  

def waiting_too_long(player):
    return time.time() - player.participant.wait_page_arrival > C.WAIT_PAGE_TIME_OUT

def group_by_arrival_time_method(self, waiting_players):

    if len(waiting_players) >= 4:
        return waiting_players[:4]
    
    for player in waiting_players:
        if waiting_too_long(player):
            # Mark as a drop_out, to fast forward through the rest of the app
            player.participant.is_dropout = True
            # make a single-player group.
            return [player]

# PAGES
class SetGroupsWaitPage(WaitPage):

    group_by_arrival_time = True

    body_text = Lexicon.group_wait_page_text

    @staticmethod
    def after_all_players_arrive(group: Group):
        # save each participant's current group ID so it can be
        # accessed in the next app.

        possible_group_types = []
        if group.session.config["include_mixed_groups"]:
            possible_group_types.append("Mixed")
        if group.session.config["include_luck_groups"]:
            possible_group_types.append("Luck")
        if group.session.config["include_merit_groups"]:
            possible_group_types.append("Merit")

        if len(possible_group_types) == 0:
            raise ValueError("No group types allowed in the session. \nContact the experimenter to start a new session with a different configuration.")

        group_type = random.choice(possible_group_types)

        for p in group.get_players():
            participant = p.participant
            participant.past_group_id = group.id
            participant.group_type = group_type
            participant.app_stage = "Effort"

    @staticmethod
    def is_displayed(player):
        if player.participant.is_dropout:
            return False
        return player.round_number == 1


class Intro(Page):

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        # Only show this on the first round
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.effort_score = 0
        player.participant.time_up = False
        player.participant.expiry = time.time() + C.TASK_TIMER


class AddNumbers(Page):
    """
    The player has to add some numbers together using mental arithmetic
    If they get it correct, they get a point
    They can keep playing until the countdown timer runs out
    """
    form_model = "player"
    form_fields = ["number_entered"]

    timer_text = Lexicon.timer_text
    # Handles the timer

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False 
        return True

    @staticmethod
    def vars_for_template(player: Player):
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        number_3 = random.randint(1,100)
        number_4 = random.randint(1,100)
        number_5 = random.randint(1,100)
        player.sum_of_numbers = number_1 + number_2 + number_3 + number_4 + number_5
    
        return{
            "number_1": number_1,
            "number_2": number_2,
            "number_3": number_3,
            "number_4": number_4,
            "number_5": number_5,
            "current_score": player.participant.effort_score,
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Give the participant a point if they get it correct
        if player.sum_of_numbers == player.number_entered:
            player.participant.effort_score += 1
    
    @staticmethod
    def get_timeout_seconds(player: Player):
        
        # Check how long the participant has left
        time_left = player.participant.expiry - time.time()
        if time_left < 1:
            player.participant.time_up = True
        return time_left


class Results(Page):
    
    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False        
        if player.round_number == C.NUM_ROUNDS:
            return True
        return player.participant.vars['time_up']   

    @staticmethod
    def vars_for_template(player: Player):
        return{
            "current_score": player.participant.vars['effort_score'],
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon
        }

    # If we're out of time move to next app in the sequence
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if len(upcoming_apps) > 0:
            player.participant.wait_page_arrival = time.time()
            return upcoming_apps[0]


page_sequence = [SetGroupsWaitPage, Intro, AddNumbers, Results]