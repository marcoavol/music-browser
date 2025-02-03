"""The Music Browser integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Music Browser component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Music Browser from a config entry."""
    # Retrieve user ID from the config entry
    user_id = entry.data.get("user_id")

    # Store OAuth credentials in the config entry
    oauth_credentials = {
        "user_id": user_id,
        "access_token": "your_access_token",
        "refresh_token": "your_refresh_token",
        "expires_at": "expiration_timestamp",
    }
    hass.config_entries.async_update_entry(entry, data=oauth_credentials)
    return True
