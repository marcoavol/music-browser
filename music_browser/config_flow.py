"""Config flow for Music Browser integration."""

import voluptuous as vol
import logging

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers import selector

from .const import DOMAIN, PROVIDERS

LOGGER = logging.getLogger(__name__)

class MusicBrowserConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Music Browser."""

    def __init__(self) -> None:
        """Initialize the config flow."""
        self.user_id = None
        self.provider = None

    async def async_step_user_id(self, user_input=None) -> ConfigFlowResult:
        """Handle the initial step."""
        LOGGER.debug("Entering async_step_user_id with input: %s", user_input)
        if user_input is not None:
            self.user_id = user_input["user_id"]
            return await self.async_step_provider()

        users = await self._get_home_assistant_users()
        return self.async_show_form(
            step_id="user_id",
            data_schema=vol.Schema(
                {
                    vol.Required("user_id"): selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=[
                                selector.SelectOptionDict(
                                    value=user_id, label=user_name
                                )
                                for user_id, user_name in users.items()
                            ]
                        )
                    )
                }
            ),
            errors={},
        )

    async def async_step_provider(self, user_input=None) -> ConfigFlowResult:
        """Handle the provider selection step."""
        if user_input is not None:
            self.provider = user_input["provider"]
            # Ensure the provider is valid before proceeding
            if self.provider in PROVIDERS:
                return await self.async_step_oauth()
            else:
                return self.async_show_form(
                    step_id="provider",
                    data_schema=vol.Schema(
                        {
                            vol.Required("provider"): selector.SelectSelector(
                                selector.SelectSelectorConfig(
                                    options=[
                                        selector.SelectOptionDict(
                                            value=key, label=str(value["name"])
                                        )
                                        for key, value in PROVIDERS.items()
                                    ]
                                )
                            )
                        }
                    ),
                    errors={"base": "invalid_provider"},
                )

        return self.async_show_form(
            step_id="provider",
            data_schema=vol.Schema(
                {
                    vol.Required("provider"): selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=[
                                selector.SelectOptionDict(
                                    value=key, label=str(value["name"])
                                )
                                for key, value in PROVIDERS.items()
                            ]
                        )
                    )
                }
            ),
            errors={},
        )

    async def async_step_oauth(self, user_input=None) -> ConfigFlowResult:
        """Handle the OAuth step."""
        if user_input is not None:
            # Process OAuth user input here
            return self.async_create_entry(title="Music Browser", data={})

        # Show a form or message indicating the OAuth process
        return self.async_show_form(
            step_id="oauth",
            data_schema=vol.Schema({}),
            description_placeholders={"provider": self.provider},
            errors={},
        )

    async def _get_home_assistant_users(self):
        """Retrieve a list of Home Assistant users."""
        users = await self.hass.auth.async_get_users()
        # Include the owner and exclude system-generated users
        return {
            user.id: user.name or "Unnamed User"
            for user in users
            if not user.system_generated
        }
