import otree.test
from otree.common import Money, money_range
import matching_pennies.views as views
from matching_pennies.utilities import Bot
import random


class ParticipantBot(Bot):

    def play(self):

        # both players choose their heads or tails
        choice = random.choice(self.participant.PENNY_CHOICES)[0]
        self.submit(views.Choice, {"penny_side": choice})

        # results after choices
        self.submit(views.Results)
