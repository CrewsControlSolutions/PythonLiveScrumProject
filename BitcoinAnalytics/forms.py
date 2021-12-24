from django.forms import ModelForm
from .models import Competitor


class CompetitorForm(ModelForm):
    class Meta:
        model = Competitor
        fields = '__all__'


# class CompetitorListForm(ModelForm):
#     class Meta:
#         model = CompetitorList
#         fields = '__all__'
