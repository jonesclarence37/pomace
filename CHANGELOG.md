# 0.8 (2021-05-12)

- Added `exec` command to run Python scripts.
- Added randomization of the browser's user agent.
- Fixed Flask 2.0 incompatibility.

# 0.7 (2021-03-26)

- Updated shutdown sequence to delete `geckodriver.log` automatically.
- Changed `Page.text` to return just the extracted text from a page.
- Added `Page.identity` as a checksum of the page's text.
- Added an experimental `pomace serve` mode to invoke Pomace as a web API.

# 0.6 (2021-01-02)

- Renamed automatic page load function from `autopage()` to `auto()`.
- Updated page model schema to `locators: { inclusions: [], exclusions: [] }`.
- Added automatic attempts to try multiple indices when locating elements.
- Fixed page matching to find exact patterns before abstract ones.

# 0.5 (2020-12-28)

- Added automatic cleanup of unused locators.
- Added prompt when no locators match.
- Added `clean` command to force cleanup of unused actions.
- Added `clone` command to download models from Git repositories.

# 0.4 (2020-11-14)

- Fixed handling of automatic browser updates.

# 0.3 (2020-10-01)

- Added `text` and `html` properties to pages.
- Updated actions to support `delay=0` override.
- Updated `URL` to support comparison to strings.

# 0.2 (2020-08-10)

- Added support for `$BROWSER` environment variable on CI.
- Added `fake.person.honorific` property.
- Changed shell command from `dev` to `shell`.

# 0.1 (2020-07-03)

- Initial release.
