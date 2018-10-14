import pytest
from weather_app.app import get_weather


def test_get_weather():
    weather = get_weather("Granada, ES")
    if type(weather) == type(dict):
        pass


