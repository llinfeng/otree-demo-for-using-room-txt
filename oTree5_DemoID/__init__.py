from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'oTree5_DemoID'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    self_reported_id = models.IntegerField(min = 1)


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = [
            'self_reported_id'
            ]


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if int(player.self_reported_id) == int(player.participant.label):
            player.payoff += cu(1)
        else:
            pass

    @staticmethod
    def vars_for_template(player : Player):
        return {
                'the_participant_id' : player.participant.label
                }




class Results(Page):
    def vars_for_template(player : Player):
        return {
                'participant_id' : player.participant.label,
                'payoff_for_display' : player.payoff
                }


page_sequence = [MyPage,  Results]
