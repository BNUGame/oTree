# -*- coding: utf-8 -*-
import prisoner.models as models
from django import forms
from prisoner.utilities import Form
import otree.forms


class DecisionForm(Form):

    class Meta:
        model = models.Participant
        fields = ['decision']
        widgets = {'decision': forms.RadioSelect()}
