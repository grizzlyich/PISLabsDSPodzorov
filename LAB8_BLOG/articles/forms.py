from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "text")

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if Article.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("Запись с таким названием уже существует.")
        return title
