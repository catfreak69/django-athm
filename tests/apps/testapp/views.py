import json
from pathlib import Path

from django.shortcuts import render

athm_config_fixture = (
    Path(__file__).resolve().parent.parent.parent / "fixtures" / "athm_config.json"
)


def home_view(request):
    with athm_config_fixture.open() as fp:
        return render(request, "home.html", context=json.load(fp))
