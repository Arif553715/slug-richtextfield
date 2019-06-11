from django import forms
from .models import BlogPost, BlogCategory
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from django import forms
from django.core.mail import send_mail
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
import re
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = ('__all__')
        # fields = ('title', 'category', 'description', 'status', 'publish')


'''
class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    status = forms.IntegerField()

    description = forms.CharField(widget=CKEditorWidget)
    # publish = forms.BooleanField(required=True)

    # def __init__(self, user, *args, **kwargs):
    #     super(BlogPostForm, self).__init__(*args, **kwargs)
    #     self.fields['category'] = forms.ChoiceField(
    #         choices=[(o.id, str(o)) for o in BlogPost.objects.filter(user=user)]
    #     )


class CrispyBlogPostForm(BlogPostForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('status', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Send')
        )
'''

