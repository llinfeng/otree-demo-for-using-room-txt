from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = [
            'self_reported_id'
            ]

    def before_next_page(self):
        if int(self.player.self_reported_id) == int(self.participant.label):
            self.player.payoff += c(1)
        else:
            pass

    def vars_for_template(self):
        return {
                'the_participant_id' : self.participant.label
                }

class Results(Page):

    def vars_for_template(self):
        return {
                'participant_id' : self.participant.label,

                'payoff_for_display' : self.player.payoff
                }



page_sequence = [MyPage, Results]
