from typing import Union

from django import forms
from django.forms.utils import flatatt
from django.forms.widgets import TextInput
from django.template import loader
from django.utils.encoding import force_str
from django.utils.html import format_html

from ..generics.models import RealmBaseModel
from ..models import Place


class RealmWidget:

    # См. RealmEditBaseForm
    model: RealmBaseModel
    field_name: str


class ReadOnlyWidget(forms.Widget, RealmWidget):
    """Представляет поле только для чтения."""

    def value_from_datadict(self, data, files, name):
        return getattr(self.model, self.field_name)  # Чтобы поле не считалось изменённым.

    def render(self, name, value, attrs=None, renderer=None) -> str:

        if hasattr(self, 'initial'):
            value = self.initial

        return f"{value or ''}"


class PlaceWidget(TextInput, RealmWidget):
    """Представляет поле для редактирования места."""

    _place_cached: bool = False
    _place_cache: Place = None

    def render(self, name, value, attrs=None, renderer=None) -> str:

        if value and self.model:
            value = self.model.place.geo_title  # Выводим полное название места.

        return super().render(name, value, attrs=attrs)

    def value_from_datadict(self, data, files, name) -> Union[str, int]:
        """Здесь получаем из строки наименования места объект места.

        :param data:
        :param files:
        :param name:

        """
        place_name = data.get(name, None)

        if not place_name:
            return ''

        if not self._place_cached:  # value_from_datadict может быть вызван несколько раз. Кешируем.
            self._place_cached = True
            self._place_cache = Place.create_place_from_name(place_name)

        if self._place_cache is None:
            return ''

        return self._place_cache.id


class RstEditWidget(forms.Widget):
    """Реализует виджет для редактирования и предпросмотра текста в rst-подобном формате."""

    def __init__(self, attrs=None):

        default_attrs = {'cols': '40', 'rows': '10'}

        if attrs:
            default_attrs.update(attrs)

        super().__init__(default_attrs)

    def render(self, name, value, attrs=None, renderer=None) -> str:

        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, {'name': name})

        html = loader.render_to_string('sub/rst_hints.html')

        return format_html(html, flatatt(final_attrs), force_str(value))
