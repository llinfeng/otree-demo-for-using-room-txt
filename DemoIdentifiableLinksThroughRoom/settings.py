from os import environ

SESSION_CONFIGS = [
    dict(
       name='Demo1_oTree3',
       display_name="Demo app for rendering and checking participant.id",
       num_demo_participants=3,
       app_sequence=['DemoAppForParticipantID']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

ROOMS = [
    dict(
        name='room_with_numerical_id',
        display_name='1,2,3...',
        participant_label_file='_rooms/room_with_20_seats.txt',
        use_secure_urls=True
    ),
    dict(
        name='room_with_char_id',
        display_name='A,B,C,...',
        participant_label_file='_rooms/room_with_char_as_seats.txt',
        use_secure_urls=True
    )
    ]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'h)3bg=kiiuuzf97$tyom3(l9fmrgh(rmg+h3l2fzeaa+@b=z&2'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
