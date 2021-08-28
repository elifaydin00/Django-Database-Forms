from django import forms
from .models import Review

#class ReviewForm(forms.Form):
#    user_name=forms.CharField(label="Your name",max_length=100)
#    review_text=forms.CharField(label="Your opinion",widget=forms.Textarea,max_length=300)
#    rating=forms.IntegerField(label="Your rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model=Review
        fields = "__all__"
        labels={
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your rating"
        }
        error_mesages={
            "user_name":{
                "required":"Your name must not be empty!",
                "max_length":"Please enter a shorter name",
                }
        }
