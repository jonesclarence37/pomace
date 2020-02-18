# pylint: disable=unused-import,import-outside-toplevel

import atexit as _atexit

from pomelo import cli as _cli


def _display_settings():
    from pomelo.settings import settings

    line = ""
    if settings.browser.name:
        line += settings.browser.name.capitalize()
        if settings.browser.headless:
            line += " (headless)"
    if line and settings.site.domain:
        line += f" -- {settings.site.url}"

    if line:
        print(line)


if __name__ == '__main__':
    _atexit.register(_cli.quit_browser)
    _display_settings()
    _cli.launch_browser()

    from pomelo.shared import browser
    from pomelo import Page, autopage
    from pomelo.settings import settings

    page = autopage()