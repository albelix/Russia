import time
import random

from otree.api import *

from game import C as gameConstants

from settings import LANGUAGE_CODE

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
        if subsession.session.config["name"] == "quiz":

            players = subsession.get_players()
            groups = [players[i:i+4] for i in range(0, len(players), 4)]

            for group in groups:
                group_code = random.randint(1,100000)
                
                if 'group_type' in subsession.session.config.keys():
                    group_type = subsession.session.config["group_type"]
                else:
                    group_type = "Mixed"

                for player in group:
                    player.participant.group_type = group_type
                    player.participant.effort_score = random.randint(0,10)
                    player.participant.past_group_id = group_code
                    player.participant.is_dropout = False
                    player.participant.wait_page_arrival = time.time()
                    player.participant.app_stage = "Effort" # Participants will come from Effort


class C(BaseConstants):
    NAME_IN_URL = 'quiz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    WAIT_PAGE_TIME_OUT = 1200


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    private = models.FloatField(label=Lexicon.private_question,
                                choices=[0, 20, 40, 60],
                                widget=widgets.RadioSelectHorizontal
                                )

    public = models.FloatField(label=Lexicon.public_question,
                                    choices=[0, 20, 40, 60],
                                    widget=widgets.RadioSelectHorizontal
                                    )
    success = models.FloatField(label=Lexicon.success_question,
                                  choices=[0, 20, 40, 60],
                                  widget=widgets.RadioSelectHorizontal
                                  )

    fail = models.IntegerField(label=Lexicon.failure_question,
                                       choices=[0, 20, 40, 60],
                                       widget=widgets.RadioSelectHorizontal
                                       )

    fair_rich = models.IntegerField(label=Lexicon.fair_rich_question, max=1000, min=0)

    fair_poor = models.IntegerField(label=Lexicon.fair_poor_question, max=1000, min=0)

def waiting_too_long(player):

    waiting_time_so_far = time.time() - player.participant.wait_page_arrival

    return  waiting_time_so_far > C.WAIT_PAGE_TIME_OUT

def set_endowments(group):

    # Get participants
    players = group.get_players()
    participants = [player.participant for player in players]
    # Randomise participants
    random.shuffle(participants)

    group_types = [participant.group_type for participant in participants]

    unique_group_types = list(set(group_types))
    if len(unique_group_types) == 1:
        group_type = unique_group_types[0]
    else:
        raise ValueError("Group participants don't have all the same group type")

    if len(participants) != 4:
        # If not a valid group, skip all this
        # Should only apply when we have had drop outs already
        return None

    # If "Mixed" group_type then choose an actual_group_type of either Luck or Merit
    if group_type == "Mixed":
        if random.random() > 0.5:
            actual_group_type = "Luck"
        else:
            actual_group_type = "Merit"
    else:
        actual_group_type = group_type

    if actual_group_type == "Luck":
  
        participants[0].vars.update(task_chosen="Luck", wealth="rich", actual_group_type=actual_group_type)
        participants[1].vars.update(task_chosen="Luck", wealth="rich", actual_group_type=actual_group_type)
        participants[2].vars.update(task_chosen="Luck", wealth="poor", actual_group_type=actual_group_type)
        participants[3].vars.update(task_chosen="Luck", wealth="poor", actual_group_type=actual_group_type)

        # Record the winner
        participants.sort(key=lambda p:p.effort_score, reverse=True)
        # Update depending on bonus level decided
        participants[0].vars.update(effort_bonus=50)

    elif actual_group_type == "Merit":

        # Sort participants by their effort score
        participants.sort(key=lambda p:p.effort_score, reverse=True)

        # Set the top two scorers with high endowments, bottom two with low
        participants[0].vars.update(task_chosen="Effort", wealth="rich", actual_group_type=actual_group_type)
        participants[1].vars.update(task_chosen="Effort", wealth="rich", actual_group_type=actual_group_type)
        participants[2].vars.update(task_chosen="Effort", wealth="poor", actual_group_type=actual_group_type)
        participants[3].vars.update(task_chosen="Effort", wealth="poor", actual_group_type=actual_group_type)

    else:
        raise ValueError("No valid group type selected!")

    # Set the participant account to the endowment level
    for participant in participants:
        if participant.wealth == "rich":
            participant.vars.update(funds = gameConstants.ENDOWMENT_RICH)
            participant.vars.update(endowment=gameConstants.ENDOWMENT_RICH)
        elif participant.wealth == "poor":
            participant.vars.update(funds = gameConstants.ENDOWMENT_POOR)
            participant.vars.update(endowment=gameConstants.ENDOWMENT_POOR)

def group_by_arrival_time_method(self, waiting_players):

    waiting_groups = {}

    # Group ALL players at this stage, not just active players
    for player in self.get_players():
        if "app_stage" in player.participant.vars.keys():
            if player.participant.app_stage == "Quiz Grouping":
                if player not in waiting_players:
                    waiting_players.append(player)

    for player in waiting_players:
        # If the player is a dropout, just put them in a single group
        # and move them on
        if player.participant.is_dropout:
            return [player]

        group_id = player.participant.past_group_id
        if group_id not in waiting_groups:
            # since 'd' is initially empty, we need to initialize an empty list (basket)
            # each time we see a new group ID.
            waiting_groups[group_id] = []
        players_in_my_group = waiting_groups[group_id]
        players_in_my_group.append(player)
        if len(players_in_my_group) == 4:
            for player in players_in_my_group:
                player.participant.app_stage = "Quiz"
            return players_in_my_group
        
        if waiting_too_long(player):
            # Mark as a drop_out, to fast forward through the rest of the app
            player.participant.is_dropout = True
            # make a single-player group.
            return [player]

        player.participant.app_stage="Quiz Grouping"



# PAGES
class SetEndowmentsWaitPage(WaitPage):

    group_by_arrival_time = True

    body_text = Lexicon.group_wait_page_text

    # Maybe do an is_displayed here to handle players waiting too long if the group isn't coming through
    # Check the guthub repo fo the old version
    
    after_all_players_arrive = set_endowments


class GroupAssigned(Page):

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        return True     
    
    @staticmethod
    def vars_for_template(player: Player):
        return {'gameConstants': gameConstants,
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}

class Instructions(Page):

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        return True
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}

class Quiz(Page):
    
    form_model = "player"
    form_fields = ["private", "public", "success", 
        "fail", "fair_rich", "fair_poor"]

    def error_message(self, response):
        if response['private'] != 60:
            return Lexicon.quiz_error_message.format(1)
        elif response['public'] != 40:
            return Lexicon.quiz_error_message.format(2)
        elif response['success'] != 20:
            return Lexicon.quiz_error_message.format(3)
        elif response['fail'] != 0:
            return Lexicon.quiz_error_message.format(4)

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        return True

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.participant.is_dropout = True

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}


class Results(Page):

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        return True

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}


class FinalMessage(Page):

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        return True

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "LANGUAGE_CODE": LANGUAGE_CODE,
            "Lexicon": Lexicon}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.wait_page_arrival = time.time()


page_sequence = [
    SetEndowmentsWaitPage,
    GroupAssigned,
    Instructions,
    Quiz,
    Results,
    FinalMessage
]
