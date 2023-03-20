from django import forms
import calendar


class JudgementsFilterForm(forms.Form):
    year = forms.ChoiceField(
        choices=[("", "")] + [(str(year), str(year)) for year in range(2009, 2024)]
    )
    month = forms.ChoiceField(
        choices=[("", "")]
        + [(str(i), month) for i, month in enumerate(calendar.month_name) if i != 0],
        required=False,
    )

    # You can also set the label of the fields using the `label` attribute
    year.label = "year"
    month.label = "month"
    # print(YEAR_CHOICES, MONTH_CHOICES)


class JudgementsSearchForm(forms.Form):
    search_query = forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "Type your query here"}),
    )


class JudgementsPDFForm(forms.Form):
    search_link = forms.URLField(
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "enter pdf file link"}),
    )
