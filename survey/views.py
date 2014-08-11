# -*- coding: utf-8 -*-
import survey.forms as forms
from survey.utilities import Page, MatchWaitPage, SubsessionWaitPage
from otree.common import Money, money_range

class Start(Page):

    template_name = 'survey/Start.html'

    def variables_for_template(self):
        if self.participant.payoff is None:
            self.participant.set_payoff()

    def body_text(self):
        return "Waiting for the other participants."


class Demographics(Page):

    form_class = forms.DemographicsForm
    template_name = 'survey/Survey.html'


class CognitiveReflectionTest(Page):

    form_class = forms.CognitiveReflectionTestForm
    template_name = 'survey/Survey.html'

    def after_valid_form_submission(self):
        self.participant.crt_bat = self.participant.crt_bat_float * 100


class End(Page):

    template_name = 'survey/End.html'


def pages():

    return [SubsessionWaitPage,
            Start,
            Demographics,
            CognitiveReflectionTest,
            End]
