"""Diagnostics support for the HA CI Demo integration."""

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.core import HomeAssistant

from . import DemoConfigEntry

TO_REDACT = {"api_key", "password", "token", "unique_id"}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: DemoConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    return {
        "entry": async_redact_data(dict(entry.data), TO_REDACT),
        "options": async_redact_data(dict(entry.options), TO_REDACT),
    }
