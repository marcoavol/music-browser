"""API module for Music Browser integration."""


class MusicBrowserApi:
    """Base class for music streaming API interactions."""

    def __init__(self, oauth_session, provider):
        """Initialize the API with OAuth session and provider."""
        self.oauth_session = oauth_session
        self.provider = provider

    def get_user_data(self):
        """Fetch user data from the provider."""
        raise NotImplementedError


class TidalApi(MusicBrowserApi):
    """Tidal-specific API implementation."""

    def get_user_data(self):
        """Retrieve user data from Tidal."""
        # Implement Tidal-specific logic
