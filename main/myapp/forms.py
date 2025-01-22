from django import forms
from django.forms import ModelForm
from .models import ArtWork

# Create a form
arts = ArtWork.objects.all()
class BidForm(ModelForm):
    class Meta:
        model = ArtWork
        fields = ('initialBid',)
        labels = {
            'initialBid': '',
        }

        widgets = {
            'initialBid': forms.NumberInput(attrs={'class': 'block w-full  border-0 bg-[#1c1c1c] text-white rounded-sm focus:outline-red-700 focus:ring focus:ring-red-700', 'id': 'newAmount', 'placeholder': ''}),
        }
        # py manage.py tailwind start