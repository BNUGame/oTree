# -*- coding: utf-8 -*-
"""Documentation at https://github.com/oTree-org/otree/wiki"""

from otree.db import models
import otree.models
from otree import forms


doc = """
Stag hunt is a game that describes a conflict between safety and social cooperation.
Two players go out on a hunt, and each can privately choose to hunt a stag or hunt a hare.
To hunt a stag, a player must have the cooperation of the other player in order to succeed.
A player can hunt a hare without the other player, but a hare is worth less than a stag.
Source code <a href="https://github.com/oTree-org/oTree/tree/master/stag_hunt" target="_blank">here</a>.
"""


class Subsession(otree.models.BaseSubsession):

    name_in_url = 'stag_hunt'


class Treatment(otree.models.BaseTreatment):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    stag_stag_amount = models.MoneyField(
        default=0.20,
        doc="""Payoff if both players choose stag"""
    )

    stag_hare_amount = models.MoneyField(
        default=0.00,
        doc="""Payoff if the player chooses stag but the other hare"""
    )

    hare_stag_amount = models.MoneyField(
        default=0.10,
        doc="""Payoff if the player chooses hare but the other stag"""
    )

    hare_hare_amount = models.MoneyField(
        default=0.10,
        doc="""Payoff if both players choose hare"""
    )


class Match(otree.models.BaseMatch):

    # <built-in>
    treatment = models.ForeignKey(Treatment)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    players_per_match = 2


class Player(otree.models.BasePlayer):

    # <built-in>
    match = models.ForeignKey(Match, null=True)
    treatment = models.ForeignKey(Treatment, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    decision = models.CharField(
        default=None,
        doc="""The player's choice""",
        widget=forms.RadioSelect()
    )

    def decision_choices(self):
        return ['Stag', 'Hare']

    def other_player(self):
        """Returns other player in match"""
        return self.other_players_in_match()[0]

    def set_payoff(self):

        payoff_matrix = {
            'Stag': {
                'Stag': self.treatment.stag_stag_amount,
                'Hare': self.treatment.stag_hare_amount,
            },
            'Hare': {
                'Stag': self.treatment.hare_stag_amount,
                'Hare': self.treatment.hare_hare_amount,
            }
        }
        self.payoff = payoff_matrix[self.decision][self.other_player().decision]


def treatments():

    return [Treatment.create()]