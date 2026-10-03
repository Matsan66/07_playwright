import pytest
from playwright.sync_api import Page


@pytest.fixture
def agile_helper_page(page: Page):
    """Öppnar Agile Helper."""
    page.goto("https://lejonmanen.github.io/agile-helper/")
    return page

@pytest.fixture
def first_day_page(agile_helper_page: Page):
    """Öppnar Agile Helper och väljer första dagen."""
    agile_helper_page.get_by_role("button", name="Första").click()
    return agile_helper_page


@pytest.fixture
def last_day_page(agile_helper_page: Page):
    """Öppnar Agile Helper och väljer sista dagen."""
    agile_helper_page.get_by_role("button", name="Sista").click()
    return agile_helper_page