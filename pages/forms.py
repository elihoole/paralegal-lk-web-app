from django import forms


class JudgementsFilterForm(forms.Form):
    YEAR_CHOICES = [("", "")] + [(str(year), str(year)) for year in range(2009, 2024)]
    MONTH_CHOICES = [("", "")] + [(str(month), str(month)) for month in range(1, 13)]

    # print(YEAR_CHOICES, MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    month = forms.ChoiceField(choices=MONTH_CHOICES)
