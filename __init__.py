DOMAIN = "playwright"


async def async_setup(hass, config):
    hass.states.async_set("playwright.test", "Test")

    # Return boolean to indicate that initialization was successful.
    return True