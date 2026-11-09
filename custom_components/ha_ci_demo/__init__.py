"""HA CI Demo — a minimal integration used to exercise the release pipeline.

This repository exists to prove the CI stack end to end: a real release, a real
zip asset, real notes. It ships no device support and is not meant for users.
"""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

type DemoConfigEntry = ConfigEntry[None]


async def async_setup_entry(hass: HomeAssistant, entry: DemoConfigEntry) -> None:
    """Set up the integration from a config entry."""
    entry.runtime_data = None


async def async_unload_entry(hass: HomeAssistant, entry: DemoConfigEntry) -> None:
    """Unload a config entry."""
