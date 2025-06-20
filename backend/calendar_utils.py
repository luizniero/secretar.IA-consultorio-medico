"""Google Calendar utilities for listing available slots and creating events."""

import os
import datetime as dt
from typing import List

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = os.environ.get("CALENDAR_ID")
SERVICE_ACCOUNT_FILE = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")


def _get_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)
    return service


async def list_available_slots(days: int = 7) -> List[dt.datetime]:
    """Return available slots in the next `days` days."""
    # In a real implementation, this function would check existing events in the
    # calendar and compute free time slots. Here we return placeholder values.
    now = dt.datetime.utcnow()
    return [now + dt.timedelta(days=1, hours=9)]


async def create_calendar_event(
    summary: str,
    description: str,
    start: dt.datetime | None = None,
    duration_minutes: int = 30,
):
    if start is None:
        start = dt.datetime.utcnow() + dt.timedelta(days=1)
    end = start + dt.timedelta(minutes=duration_minutes)

    event = {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start.isoformat() + "Z"},
        "end": {"dateTime": end.isoformat() + "Z"},
    }

    # Placeholder for Google Calendar API call
    # service = _get_service()
    # event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

    return event
