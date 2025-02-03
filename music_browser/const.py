"""Constants for the Music Browser integration."""

DOMAIN = "music_browser"

PROVIDERS = {
    "tidal": {
        "name": "Tidal",
        "authorize_url": "https://auth.tidal.com/authorize",
        "token_url": "https://auth.tidal.com/token",
        "scopes": [
            "user-read",
            "playlist-read",
            # Add other Tidal scopes as needed
        ],
    },
    # Add more providers as needed
}
