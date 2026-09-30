"""Tests for the HA CI Demo diagnostics."""

from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.ha_ci_demo.const import DOMAIN
from custom_components.ha_ci_demo.diagnostics import async_get_config_entry_diagnostics


async def test_diagnostics_redact_secrets(hass: HomeAssistant) -> None:
    """Data and options come back with every secret redacted."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={"host": "demo.local", "api_key": "secret"},
        options={"token": "secret", "interval": 30},
    )
    entry.add_to_hass(hass)

    result = await async_get_config_entry_diagnostics(hass, entry)

    assert result == {
        "entry": {"host": "demo.local", "api_key": "**REDACTED**"},
        "options": {"token": "**REDACTED**", "interval": 30},
    }
