from django.forms import Form

class BaseForm(Form):
    _LABEL_NAME: dict[str, str] = {}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.help_text = ""

            if field_name in self._LABEL_NAME:
                field.label = self._LABEL_NAME[field_name]
