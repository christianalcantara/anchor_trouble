# -*- coding: utf-8 -*-
# Autor: christian
from django import forms
from anchor_trouble.lib import GasStation
import os


class SendFileForm(forms.Form):
    gas_station = None
    file = forms.FileField(
        label="File", required=True
    )

    def clean_file(self):
        data = self.cleaned_data['file']
        ext = os.path.splitext(data.name)[-1].lower()
        if ext != '.txt':
            raise forms.ValidationError("'.txt' required: Invalid file extension '{0}'.".format(ext))
        try:
            gas_station  = GasStation(data.read())
            self.gas_station = gas_station.data
        except Exception as e:
            raise forms.ValidationError(e)

        return data
