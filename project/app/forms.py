from django import forms


class AddEat(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "title"}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': "title"}), )
    category = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': "title"}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': "title"}))


class AddCategory(forms.Form):
    title = forms.CharField()


class AddOrder(forms.Form):
    product = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "title"}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': "title"}))
    price = forms.IntegerField()
