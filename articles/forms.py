from .models import Articles
from django.forms import ModelForm


class articleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','description','featured_image','tags']
        