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

    HARD_TO_SAY_CHOICE = [999, ('Затрудняюсь ответить')]
#    CITIES = [(int(i.get('code')), i.get('name')) for i in settings.CITIES] + [(13, _('Другой'))]
#    GENDER_CHOICES = [[0, _('Мужской')], [1, _('Женский')]]
#    IS_OCCUPIED_CHOICES = [[False, _('Нет')], [True, _('Да')]]
    Big5 = [
        [1, ('Полностью согласен')],
        [2, ('Скорее согласен')],
        [3, ('Ни то чтобы согласен - ни то чтобы нет')],
        [3, ('Скорее не согласен')],
        [4, ('Совершенно не согласен')],
        HARD_TO_SAY_CHOICE
    ]

    MARITAL_STATUS_CHOICES = [
        [1, ('Не женаты/не замужем')],
        [2, ('Женаты/замужем')],
        [3, ('В отношениях, но официально не состоите в браке')],
        [4, ('Разведены')],
        [5, ('Живете отдельно от супруга/и')],
        [6, ('Вдовец/Вдова')],
        HARD_TO_SAY_CHOICE
    ]
    CITY_SIZE_CHOICES = [
        (1, '< 2,000'),
        (2, '2,000 - 5,000'),
        (3, '5,001- 10,000'),
        (4, '10,001 - 20,000'),
        (5, '20,001 - 50,000'),
        (6, '50,001 - 100,000'),
        (7, '100,001 - 500,000'),
        (8, '> 500,000'),
        (9, ('1 млн. и более')),
    ]
    SAME_MORAL_CHOICES = [
        [1, ('Совершенно согласен')],
        [2, ('Скорее согласен')],
        [3, ('Скорее не согласен')],
        [4, ('Совершенно не согласен')],
        HARD_TO_SAY_CHOICE,
        [6, ('Без ответа, я атеист')]
    ]
    CHURCH_ATTENDANCE_CHOICES = [
        [0, ('Вообще не бываю')],
        [1, ('1 раз в месяц или реже')],
        [2, ('2-3 раза в месяц')],
        [3, ('4 раза в месяц или чаще')],
        HARD_TO_SAY_CHOICE,
        [5, ('Без ответа, я атеист')]
    ]
    JUSTIFIED_CHOICES = range(1, 11)
    RISK_CHOICES = range(0, 11)
    AGREEMENT_CHOICES = [
        [1, ('Безусловно согласия, сплоченности')],
        [2, ('Скорее согласия, сплоченности')],
        [3, ('Скорее несогласия, разобщенности')],
        [4, ('Безусловно несогласия, разобщенности')],
        HARD_TO_SAY_CHOICE
    ]
    PROUDTOBE = [
        [1, ('Очень горжусь')],
        [2, ('Скорее горжусь')],
        [3, ('Скорее не горжусь')],
        [4, ('Совсем не горжусь')],
        [5, ('Не чувствую себя частью своего народа')],
        HARD_TO_SAY_CHOICE
    ]
    OFTENOT = [
        [1, ('Никогда')],
        [2, ('Почти никогда')],
        [3, ('Иногда')],
        [4, ('Довольно часто')],
        [5, ('Очень часто')],
        HARD_TO_SAY_CHOICE
    ]
    SAFESTATE = [
        [1, ('Абсолютно безопасная')],
        [2, ('Довольно безопасная')],
        [3, ('Довольно опасная')],
        [4, ('Опасная')],
        HARD_TO_SAY_CHOICE
    ]
    SATIS_CHOICES = range(0, 11)

    HAPPY_CHOICES = [
        [0, ('Несчастливый человек')],
        [1, ('Счастливый человек')],
    ]
    TRUSTCHOICES4DNK = [
        [1, ('Полностью доверяю')],
        [2, ('В некоторой степени доверяю')],
        [3, ('Не очень доверяю')],
        [4, ('Совсем не доверяю')],
        HARD_TO_SAY_CHOICE
    ]
    INCREMENTCHOICES5DNK = [
        [1, ('Безусловно увеличился')],
        [2, ('Скорее увеличился')],
        [3, ('Не изменился')],
        [4, ('Скорее уменьшился')],
        [5, ('Безусловно уменьшился')],
        HARD_TO_SAY_CHOICE,
    ]
    SimilarChoices6DNK = [
        [1, ('Очень похож на меня')],
        [2, ('Похож на меня')],
        [3, ('Отчасти похож на меня')],
        [4, ('Немного похож на меня')],
        [5, ('Не похож на меня')],
        [6, ('Совсем не похож на меня')],
    ]

    AgreementChoices5DNK = [
        [1, ('Совершенно согласен')],
        [2, ('Скорее согласен')],
        [3, ('И да и нет')],
        [4, ('Скорее не согласен')],
        [5, ('Совершенно не согласен')],
        HARD_TO_SAY_CHOICE
    ]
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

    Rus_hardtimes = models.FloatField(label=Lexicon.Rus_hardtimes_label,
                                           choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                           widget=widgets.RadioSelectHorizontal
                                           )

    Freedom = models.FloatField(label=Lexicon.Freedom_label,
                             choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                             widget=widgets.RadioSelectHorizontal
                             )

    Abuse = models.FloatField(label=Lexicon.Abuse_label,
                             choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                             widget=widgets.RadioSelectHorizontal
                             )

    Risk = models.FloatField(label=Lexicon.Risk_label,
                                           choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                           widget=widgets.RadioSelectHorizontal
                                           )

    redidenceplace = models.CharField(
        label=("""Место жительства (населенный пункт, регион)""")
    )

    city_size = models.PositiveIntegerField(
        label=(
            """    Сколько человек (приблизительно) проживало в том населенном пункте, где Вы жили в возрасте 16 лет?"""),
        choices=C.CITY_SIZE_CHOICES,
        widget=widgets.RadioSelect())

    pride = models.IntegerField(
        label=(
            'Насколько Вы гордитесь быть частью своего народа?'),
        choices=C.PROUDTOBE,
        widget=widgets.RadioSelect()
    )

    general_trust = models.PositiveIntegerField(
        label=("""Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми 
            осторожность никогда не повредит?"""),
        choices=[
            [2, ("Нужно быть очень осторожным с другими людьми")],
            [1, ("Большинству людей можно вполне доверять")],
        ],
        widget=widgets.RadioSelect()
    )

    trust_family = models.IntegerField(
        label=("""Скажите, насколько Вы доверяете каждой из следюущих категорий лиц: полностью, в некоторой 
        степени, не очень, 
        или совсем не доверяете? Ваша семья"""),
        choices=C.TRUSTCHOICES4DNK,
        widget=widgets.RadioSelectHorizontal
    )
    trust_neighbours = models.IntegerField(
        label=("""Ваши соседи"""),
        choices=C.TRUSTCHOICES4DNK,
        widget=widgets.RadioSelectHorizontal
    )
    trust_stranger = models.IntegerField(
        label=("""Люди, с которыми Вы не знакомы"""),
        choices=C.TRUSTCHOICES4DNK,
        widget=widgets.RadioSelectHorizontal
    )
    trust_church = models.IntegerField(
        label=("""Скажите, насколько Вы доверяете следующим институтам: полностью, в некоторой 
        степени, не очень, или совсем не доверяете? Церковь"""),
        choices=C.TRUSTCHOICES4DNK,
    )
    trust_army = models.IntegerField(
        label=("""Армия"""),
        choices=C.TRUSTCHOICES4DNK,
    )
    trust_socmed = models.IntegerField(
        label=("""Социальные сети (VK, Telegram и др.)"""),
        choices=C.TRUSTCHOICES4DNK,
    )
    trust_government = models.IntegerField(
        label=("""Правительство"""),
        choices=C.TRUSTCHOICES4DNK,
    )
    trust_president = models.IntegerField(
        label=("""Президент"""),
        choices=C.TRUSTCHOICES4DNK,
    )
    trust_parliament = models.IntegerField(
        label=("""Парламент"""),
        choices=C.TRUSTCHOICES4DNK,
    )
    trust_regional_authorities = models.IntegerField(
        label=("""Региональная власть"""),
        choices=C.TRUSTCHOICES4DNK,
    )

    dtrust = models.IntegerField(
        label=(
            'По Вашему мнению, за последний год изменился или не изменился уровень доверия людей друг к '
            'другу? Если изменился, то увеличился или уменьшился?'),
        choices=C.INCREMENTCHOICES5DNK,
        widget=widgets.RadioSelect()
    )

    lastmonth = models.IntegerField(
        label=(
            'Как часто за последний месяц Вы чувствовали, что полностью контролируете ход событий?'),
        choices=C.OFTENOT,
        widget=widgets.RadioSelect()
    )

    safety = models.IntegerField(
        label=(
            'Скажите, пожалуйста, насколько сейчас безопасная или опасная обстановка там, где Вы живете?'),
        choices=C.SAFESTATE,
        widget=widgets.RadioSelect()
    )

    moreagreement = models.PositiveIntegerField(
        verbose_name='''Как Вы думаете, сегодня в нашей стране среди людей больше согласия, сплоченности или
         несогласия, разобщенности?''',
        choices=C.AGREEMENT_CHOICES,
        widget=widgets.RadioSelect()
    )


    motivation_part1 = models.TextField(
        label=("""Пожалуйста, опишите Вашу стратегию в игре: как Вы определяли вкладывать ли на 
        личный или на групповой счет?""")
    )

    motivation_part2 = models.TextField(
        label=("""Пожалуйста, вспомните Ваши эмоции в игре: как Вы реагировали на вклады других членов 
        Вашей группы на групповой счет?""")
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
        form_fields = ["WVS_luck", "WVS_responsibility", "Rus_hardtimes", "Freedom", "Abuse", "Risk"]

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

class Trust(Page):

    form_model = "player"
    form_fields = ["redidenceplace", "pride", "city_size", "general_trust","trust_family","trust_neighbours",
    "trust_stranger","trust_church","trust_army","trust_socmed","trust_government","trust_president",
    "trust_parliament","trust_regional_authorities","dtrust", "lastmonth", "safety", "moreagreement",
                   "motivation_part1", "motivation_part2"]

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


page_sequence = [WVS, ExtraDemographics, Trust, ThankYou]
