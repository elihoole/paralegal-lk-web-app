from django import forms


class JudgementsFilterForm(forms.Form):
    YEAR_CHOICES = [("", "")] + [(str(year), str(year)) for year in range(2009, 2024)]
    MONTH_CHOICES = [("", "")] + [
        (str(month), str(month))
        for month in [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
    ]

    # print(YEAR_CHOICES, MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)


class JudgementsSearchForm(forms.Form):
    search_query = forms.CharField(max_length=200, label="type your query here")
