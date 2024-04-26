"""Tests."""

from datetime import datetime
from unittest.mock import patch, Mock

import pytest


@pytest.fixture
def patch_previous_day():
    """If no solar is forecasted today, it will start returning tomorrow values."""
    with patch("forecast_solar.models.Estimate.now", Mock(return_value=PREVIOUS_DAY)):
        yield


@pytest.fixture
def patch_now():
    """Patch datetime to return payload datetime."""
    with patch("forecast_solar.models.Estimate.now", Mock(return_value=NOW)):
        yield


@pytest.fixture
def patch_near_end_today():
    """Patch datetime to return payload datetime."""
    with patch("forecast_solar.models.Estimate.now", Mock(return_value=NEAR_END_TODAY)):
        yield


PREVIOUS_DAY = datetime.fromisoformat("2022-10-15T23:48:36.170479+02:00")
NOW = datetime.fromisoformat("2022-10-15T07:48:36.170479+00:00")
NEAR_END_TODAY = datetime.fromisoformat("2022-10-15T16:48:36.170479+00:00")

PAYLOAD = {
    "message": {
        "code": 0,
        "info": {
            "distance": 0.969,
            "place": "2333 DC Leiden, Zuid-Holland, NL",
            "timezone": "Europe/Amsterdam",
        },
        "ratelimit": {"limit": 12, "period": 3600, "remaining": 10},
        "text": "",
        "type": "success",
    },
    "result": {
        "watts": {
            "2022-10-15T08:05:00+02:00": 0,
            "2022-10-15T09:00:00+02:00": 53,
            "2022-10-15T10:00:00+02:00": 68,
            "2022-10-15T11:00:00+02:00": 64,
            "2022-10-15T12:00:00+02:00": 83,
            "2022-10-15T13:00:00+02:00": 409,
            "2022-10-15T14:00:00+02:00": 1008,
            "2022-10-15T15:00:00+02:00": 1079,
            "2022-10-15T16:00:00+02:00": 788,
            "2022-10-15T17:00:00+02:00": 667,
            "2022-10-15T18:00:00+02:00": 337,
            "2022-10-15T18:50:00+02:00": 0,
            "2022-10-16T08:07:00+02:00": 0,
            "2022-10-16T09:00:00+02:00": 265,
            "2022-10-16T10:00:00+02:00": 288,
            "2022-10-16T11:00:00+02:00": 444,
            "2022-10-16T12:00:00+02:00": 542,
            "2022-10-16T13:00:00+02:00": 685,
            "2022-10-16T14:00:00+02:00": 1090,
            "2022-10-16T15:00:00+02:00": 953,
            "2022-10-16T16:00:00+02:00": 685,
            "2022-10-16T17:00:00+02:00": 357,
            "2022-10-16T18:00:00+02:00": 155,
            "2022-10-16T18:48:00+02:00": 0,
        },
        "watt_hours": {
            "2022-10-15T08:05:00+02:00": 0,
            "2022-10-15T09:00:00+02:00": 24,
            "2022-10-15T10:00:00+02:00": 85,
            "2022-10-15T11:00:00+02:00": 151,
            "2022-10-15T12:00:00+02:00": 225,
            "2022-10-15T13:00:00+02:00": 471,
            "2022-10-15T14:00:00+02:00": 1180,
            "2022-10-15T15:00:00+02:00": 2224,
            "2022-10-15T16:00:00+02:00": 3158,
            "2022-10-15T17:00:00+02:00": 3886,
            "2022-10-15T18:00:00+02:00": 4388,
            "2022-10-15T18:50:00+02:00": 4528,
            "2022-10-16T08:07:00+02:00": 0,
            "2022-10-16T09:00:00+02:00": 117,
            "2022-10-16T10:00:00+02:00": 394,
            "2022-10-16T11:00:00+02:00": 760,
            "2022-10-16T12:00:00+02:00": 1253,
            "2022-10-16T13:00:00+02:00": 1867,
            "2022-10-16T14:00:00+02:00": 2755,
            "2022-10-16T15:00:00+02:00": 3777,
            "2022-10-16T16:00:00+02:00": 4596,
            "2022-10-16T17:00:00+02:00": 5117,
            "2022-10-16T18:00:00+02:00": 5373,
            "2022-10-16T18:48:00+02:00": 5435,
        },
        "watt_hours_period": {
            "2022-10-15T08:05:00+02:00": 0,
            "2022-10-15T09:00:00+02:00": 24,
            "2022-10-15T10:00:00+02:00": 61,
            "2022-10-15T11:00:00+02:00": 66,
            "2022-10-15T12:00:00+02:00": 74,
            "2022-10-15T13:00:00+02:00": 246,
            "2022-10-15T14:00:00+02:00": 709,
            "2022-10-15T15:00:00+02:00": 1044,
            "2022-10-15T16:00:00+02:00": 934,
            "2022-10-15T17:00:00+02:00": 728,
            "2022-10-15T18:00:00+02:00": 502,
            "2022-10-15T18:50:00+02:00": 140,
            "2022-10-16T08:07:00+02:00": 0,
            "2022-10-16T09:00:00+02:00": 117,
            "2022-10-16T10:00:00+02:00": 277,
            "2022-10-16T11:00:00+02:00": 366,
            "2022-10-16T12:00:00+02:00": 493,
            "2022-10-16T13:00:00+02:00": 614,
            "2022-10-16T14:00:00+02:00": 888,
            "2022-10-16T15:00:00+02:00": 1022,
            "2022-10-16T16:00:00+02:00": 819,
            "2022-10-16T17:00:00+02:00": 521,
            "2022-10-16T18:00:00+02:00": 256,
            "2022-10-16T18:48:00+02:00": 62,
        },
        "watt_hours_day": {"2022-10-15": 4528, "2022-10-16": 5435},
    },
}
