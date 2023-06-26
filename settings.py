from os import environ


SESSION_CONFIGS = [
    dict(
        name='consent',
        display_name="Consent",
        app_sequence=['consent'],
        num_demo_participants=8,
    ),
    dict(
        name='effort',
        display_name="Effort",
        app_sequence=['effort'],
        num_demo_participants=8,
    ),
    dict(
        name='quiz',
        display_name="Quiz",
        app_sequence=['quiz'],
        num_demo_participants=8,
    ),
    dict(
        name='game',
        display_name="Game",
        app_sequence=['game'],
        num_demo_participants=8,
    ),
    dict(
        name='payment',
        display_name="Payment",
        app_sequence=['payment'],
        num_demo_participants=8,
    ),
    dict(
        name='full_experiment',
        display_name="Full Experiment",
        app_sequence=['consent', 'effort', 'quiz', 'game', 'payment'],
        num_demo_participants=8,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, 
    participation_fee=0.00, 
    doc="",
    include_luck_groups=True,
    include_merit_groups=True,
    include_mixed_groups=True
)

# These fields used to store data for participants between apps and rounds
PARTICIPANT_FIELDS = [
    "effort_score", 
    "endowment", 
    "funds", 
    "group_type", 
    "actual_group_type",
    "group_code", 
    "wealth", 
    "time_up", # Effort task
    "expiry", # Effort task
    'past_group_id',
    "public_invested", # Game
    "public_target_met", # Game
    "private_target_met", # Game
    "private_pot", # Game
    "group_pot", # Game
    "is_dropout", # Everything
    "wait_page_arrival",
    "effort_bonus",
    "total_payout_local_currency",
    "task_chosen",
    "app_stage",
    "IDQualtrics" #QUaltrics
    ]

# WARNING - SESSION CONFIGS ARE SHARED AMONG ALL PLAYERS IN A SESSION, ACROSS GROUPS
SESSION_FIELDS = [
    ]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ru'

# Use the LAB_CODE if you need to customise something for your lab's experiment
# Usually you can leave this set to "default" (options: "loyola" / "bogota")
LAB_CODE = "default"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

URLQUALTRICS="https://investigadoresloyola.eu.qualtrics.com/jfe/form/SV_9podTkjduCcDvgi"

ROOMS = [
    dict(
        name="solutions",
        display_name = "Full Experiment",
        participant_label_file='_rooms/participant_labels.txt',
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '5134823306041'

INSTALLED_APPS = ['otree']
