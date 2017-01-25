from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=50)


class BookedForm(forms.Form):
    nickname = forms.CharField(label='nickname', max_length=100)
    date_from = forms.DateField(label='date_from', input_formats=['%Y-%m-%d', ])
    date_to = forms.DateField(label='date_to', input_formats=['%Y-%m-%d', ])


class SearchForm(forms.Form):
    city = forms.CharField(label='city', max_length=30)
    date_from = forms.DateField(label='date_from', input_formats=['%Y-%m-%d', ])
    date_to = forms.DateField(label='date_to', input_formats=['%Y-%m-%d', ])