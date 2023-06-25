import random
import itertools  
import time

from otree.api import *

from settings import LANGUAGE_CODE

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

doc = """
Your app description
"""


def creating_session(subsession):

    if subsession.round_number == 1:
        # The below code only runs if we are running this app in isolation - not in the full experiment
        # If running this app in isolation, set the participant vars so that it works
        # For the full experiment, group type should be set earlier
        # For testing
        if subsession.session.config["name"] == "game":

            players = subsession.get_players()
            groups = [players[i:i+4] for i in range(0, len(players), 4)]

            for group in groups:
                group_code = random.randint(1,100000)
                endowments = itertools.cycle([C.ENDOWMENT_POOR, C.ENDOWMENT_RICH])

                for player in group:
                    this_endowment = next(endowments)
                    player.participant.funds = this_endowment
                    player.participant.past_group_id = group_code
                    player.participant.is_dropout = False
                    player.participant.wait_page_arrival = time.time()
                    player.participant.app_stage = "Quiz" # Participants will come from Effort


class C(BaseConstants):
    NAME_IN_URL = 'game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10 # 10
    GROUP_TARGET = 160 # 160
    PRIVATE_TARGET = 60 # 60
    MAX_CONTRIBUTION = 20
    ENDOWMENT_RICH = 120
    ENDOWMENT_POOR = 80
    TIME_OUT = 600
    WAIT_PAGE_TIME_OUT = 1200


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    contribution_private = models.IntegerField(label=Lexicon.contribution_private_question, min=0)
    contribution_public = models.IntegerField(label=Lexicon.contribution_public_question, min=0)


def waiting_too_long(player):
    return time.time() - player.participant.wait_page_arrival > C.WAIT_PAGE_TIME_OUT


def group_by_arrival_time_method(self, waiting_players):

    # Group ALL players at this stage, not just active players
    for player in self.get_players():
        if "app_stage" in player.participant.vars.keys():
            if player.participant.app_stage == "Game Grouping":
                if player not in waiting_players:
                    waiting_players.append(player)

    waiting_groups = {}

    for player in waiting_players:
        group_id = player.participant.past_group_id
        if group_id not in waiting_groups:
            # since 'd' is initially empty, we need to initialize an empty list (basket)
            # each time we see a new group ID.
            waiting_groups[group_id] = []
        players_in_my_group = waiting_groups[group_id]
        players_in_my_group.append(player)
        if len(players_in_my_group) == 4:
            for player in players_in_my_group:
                player.participant.app_stage = "Game"
            return players_in_my_group

        if waiting_too_long(player):
            # Mark as a drop_out, to fast forward through the rest of the app
            player.participant.is_dropout = True
            # make a single-player group.
            return [player]

        player.participant.app_stage="Game Grouping"


def setup_group(group):

    for player in group.get_players():
        player.participant.vars.update(group_pot = 0)
        player.participant.vars.update(private_pot = 0)
        player.participant.vars.update(public_invested = 0)
        player.participant.vars.update(IDQualtrics=random.randint(1,1000000)) # Not needed for all labs

    
def update_group_pot_and_ruin(group):

    # Update group pot
    group_contribution = 0
    for player in group.get_players():
        player_contribution = player.field_maybe_none("contribution_public")
        if player_contribution == None:
            player_contribution = 0
        group_contribution += player_contribution

    for player in group.get_players():
        player.participant.group_pot += group_contribution

    # Update ruin
    if group.round_number == C.NUM_ROUNDS:
        for player in group.get_players():
            if player.participant.group_pot >= C.GROUP_TARGET:
                player.participant.vars.update(public_target_met = True)
            else:
                player.participant.vars.update(public_target_met = False)

            if player.participant.private_pot >= C.PRIVATE_TARGET:
                player.participant.vars.update(private_target_met = True)
            else:
                player.participant.vars.update(private_target_met = False)

# PAGES
class GroupWaitPage(WaitPage):
    group_by_arrival_time = True

    after_all_players_arrive = setup_group

    body_text = Lexicon.group_wait_page_text

    @staticmethod
    def is_displayed(player):
        if player.participant.is_dropout:
            return False
        return player.round_number == 1


class Contribution(Page):

    form_model = 'player'
    form_fields = ['contribution_private', 'contribution_public']

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        return True

    @staticmethod
    def vars_for_template(self):
        max_allowed_contribution = min(C.MAX_CONTRIBUTION, self.participant.funds)
        private_remaining = C.PRIVATE_TARGET - self.participant.private_pot
        public_remaining = C.GROUP_TARGET - self.participant.group_pot

        return dict(
            max_allowed_contribution = max_allowed_contribution,
            private_remaining = private_remaining,
            public_remaining = public_remaining,
            LANGUAGE_CODE= LANGUAGE_CODE,
            Lexicon= Lexicon
            )


    def error_message(self, response):

        # Check repsonse is not more than the player's total amount left
        if response['contribution_private'] + response['contribution_public']  > self.participant.funds:
            return Lexicon.error_total_contribution_greater_than_funds

        if response['contribution_private'] + response['contribution_public']  > 20:
            return Lexicon.error_total_contribution_greater_than_20


    @staticmethod
    def before_next_page(player, timeout_happened):

        if timeout_happened:
            player.contribution_public = 0
            player.contribution_private = 0
            player.participant.is_dropout = True

        # Private contribution
        player.participant.funds -= player.contribution_private
        player.participant.private_pot += player.contribution_private
        # Public contribution
        player.participant.funds -= player.contribution_public
        player.participant.public_invested += player.contribution_public


    @staticmethod
    def get_timeout_seconds(player):
        return C.TIME_OUT

class ContributionResultsWaitPage(WaitPage):   

    after_all_players_arrive = 'update_group_pot_and_ruin'

    body_text = Lexicon.group_wait_page_text

    @staticmethod
    def is_displayed(player: Player):
        if player.participant.is_dropout:
            return False
        return True


class GroupResult(Page):
    @staticmethod
    def is_displayed(player):
        if player.participant.is_dropout:
            return False
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player):
        if "effort_bonus" in player.participant.vars:
            effort_bonus = player.participant.vars["effort_bonus"]
        else:
            effort_bonus = 0

        if LANGUAGE_CODE == "de":
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds / 10, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(4 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

        elif LANGUAGE_CODE == "en":
            # Payoffs for Cairo
            #if player.participant.private_target_met or player.participant.public_target_met:
            #   funds_converted = round(player.participant.funds * 1.5, 2)
            #else:
            #   funds_converted = 0
            #total_payout_local_currency = round(50 + effort_bonus + funds_converted, 2)
            #player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

            # Payoffs for Warwick
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds / 10, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(4 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

        elif LANGUAGE_CODE == "zh":
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds / 2, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(15 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

        elif LANGUAGE_CODE == "it":
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds * 0.08, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(5 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

        elif LANGUAGE_CODE == "fr":
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds / 10, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(5 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

        elif LANGUAGE_CODE == "ko":
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds * 100, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(5000 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

        elif LANGUAGE_CODE == "es":
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds * 350, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(14000 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)

        elif LANGUAGE_CODE == "ru":
            if player.participant.private_target_met or player.participant.public_target_met:
                funds_converted = round(player.participant.funds * 5, 2)
            else:
                funds_converted = 0
            total_payout_local_currency = round(200 + effort_bonus + funds_converted, 2)
            player.participant.vars.update(total_payout_local_currency = total_payout_local_currency)


        else:
            funds_converted = None
            total_payout_local_currency = None

        return dict(
            effort_bonus = effort_bonus,
            funds_converted = funds_converted,
            total_payout_local_currency = total_payout_local_currency,
            LANGUAGE_CODE=LANGUAGE_CODE,
            Lexicon=Lexicon
            )


page_sequence = [
    GroupWaitPage,
    Contribution, 
    ContributionResultsWaitPage, 
    GroupResult,
    ]