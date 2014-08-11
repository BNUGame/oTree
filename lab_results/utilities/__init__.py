import lab_results.models as models
import otree.views
import otree.test
from otree.common import Money, money_range
import otree.forms

class Page(otree.views.Page):
    z_models = models

    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.treatment = models.Treatment()
        self.match = models.Match()
        self.participant = models.Participant()


class SubsessionWaitPage(otree.views.SubsessionWaitPage):

    z_models = models

    def z_autocomplete(self):
        self.subsession = models.Subsession()


class MatchWaitPage(otree.views.MatchWaitPage):

    z_models = models

    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.treatment = models.Treatment()
        self.match = models.Match()

class Form(otree.forms.Form):

    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.treatment = models.Treatment()
        self.match = models.Match()
        self.participant = models.Participant()

class Bot(otree.test.Bot):

    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.treatment = models.Treatment()
        self.match = models.Match()
        self.participant = models.Participant()


class InitializeParticipant(otree.views.InitializeParticipant):
    z_models = models


class InitializeExperimenter(otree.views.InitializeExperimenter):
    z_models = models
