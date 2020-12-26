from datetime import datetime
from typing import Optional

from django import forms
from django.forms.widgets import CheckboxInput
from django.http import HttpRequest
from siteforms.composers.bootstrap4 import Bootstrap4, SUBMIT
from siteforms.toolbox import ModelForm

from ..forms.widgets import RstEditWidget
from ..models import Article, User


class CommonEntityForm(ModelForm):
    """Базовый класс для форм создания/редактирования сущностей."""

    pythonz_form = forms.CharField(widget=forms.HiddenInput(), initial='1')

    def __init__(self, *args, request: HttpRequest = None, src: str = None, id: str = '', **kwargs):
        super().__init__(*args, request=request, src=src, id=id, **kwargs)

    def clean_year(self) -> str:

        year = self.cleaned_data['year'] or ''
        year = year.strip()

        if year:
            if len(year) != 4 or not year.isdigit() or not (1900 < int(year) <= datetime.now().year):
                raise forms.ValidationError('Такой год не похож на правду.')

        return year

    class Composer(Bootstrap4):

        opt_submit = 'Сохранить'

        attrs = {
            SUBMIT: {'class': 'btn btn-block btn-success'},
        }


class RealmEditBaseForm(CommonEntityForm):
    """Базовый класс для форм создания/редактирования сущностей, принадлежащим областям."""

    def __init__(self, *args, user: Optional[User] = None, **kwargs):

        super().__init__(*args, **kwargs)

        if self._meta.model is not Article:  # Запрещаем управлять статусом везде, кроме Статей.

            if user is not None:
                if not user.is_superuser and not user.is_staff:
                    try:
                        del self.fields['status']

                    except KeyError:  # Нет такого поля на форме.
                        pass

        instance = kwargs.get('instance', None)

        for field_name in self.fields:

            fld = self.fields[field_name]

            if field_name == 'description':
                fld.widget = forms.Textarea(attrs={'rows': 3})

            elif field_name == 'text_src':
                fld.widget = RstEditWidget(attrs={'rows': 12})
                fld.strip = False  # Обрубать размеченный текст не следует.

            # Эти изменения нужны для стилизации форм.
            if isinstance(self.fields[field_name].widget, CheckboxInput):
                self.fields[field_name].is_checkbox = True

            fld.widget.attrs['class'] = 'form-control input-sm'

            # Эти связи потребуются в некоторых виджетах.
            fld.widget.model = instance
            fld.widget.field_name = field_name
