from functools import cached_property

from django.http import HttpRequest
from django.shortcuts import render, redirect


class BaseController:
    _CLASS_FORM = None
    _PAGE_CONTEXT: dict[str, dict] = {}
    _FORM_REDIRECT_PAGE: str = ""

    def __init__(self, request: HttpRequest) -> None:
        self._request: HttpRequest = request
        self._is_post: bool = request.method == "POST"

    @cached_property
    def form(self):
        if self._is_post:
            return self._CLASS_FORM(self._request.POST)

        return self._CLASS_FORM()

    def _is_form_submitted(self) -> bool:
        if not self._is_post or not self.form.is_valid():
            return False

        return self._form_submit()

    def _form_submit(self) -> bool:
        self.form.save()

        return True

    def form_page(self):
        if self._is_form_submitted():
            return redirect(self._FORM_REDIRECT_PAGE)

        return self._render_form_page()

    def _render_form_page(self):
        return render(self._request, "form.html",
            {
                "form": self.form,
                **self._PAGE_CONTEXT.get("form", {})
            }
        )
