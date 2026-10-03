import re
from playwright.sync_api import Page, expect


def test_choose_another_day(first_day_page: Page):
    """Testa att klick på knappen "Välj en annan dag" återställer sidan
    till ursprungsläget """
    # Hitta button med texten "Välj en annan dag"
    another_day_button = first_day_page.get_by_role(
        "button", name=re.compile("Välj en annan dag"))

    expect(another_day_button).to_be_visible()

    # Klicka på knappen "Välj en annan dag"
    another_day_button.click()

    # Finns knappen "Första" synlig igen?
    first_button = first_day_page.get_by_role(
        "button", name="Första")

    expect(first_button).to_be_visible()

# -----------------------------------------------------------------------


def test_open_sprint_planning(first_day_page: Page):
    """Testa att det går att se Sprint planning"""
    # Hitta button med texten "Sprint planning"
    sprint_planning_button = first_day_page.get_by_role(
        "button", name=re.compile("Sprint planning"))

    expect(sprint_planning_button).to_be_visible()

    # Klicka på knappen "Sprint planning"
    sprint_planning_button.click()

    # Finns rubriken "Sprint planning" på sidan?
    sprint_planning_heading = first_day_page.get_by_role(
        "heading", name="Sprint planning")

    expect(sprint_planning_heading).to_be_visible()

# -----------------------------------------------------------------------


def test_open_daily_standup(first_day_page: Page):
    """Testa att det går att se Daily standup"""

    # Hitta button med texten "Daily standup"
    daily_standup_button = first_day_page.get_by_role(
        "button", name=re.compile("Daily standup"))

    expect(daily_standup_button).to_be_visible()

    # Klicka på knappen "Daily standup"
    daily_standup_button.click()

    # Finns rubriken "Daily standup" på sidan?
    daily_standup_heading = first_day_page.get_by_role(
        "heading", name="Daily standup")

    expect(daily_standup_heading).to_be_visible()

# -----------------------------------------------------------------------


def test_open_in_the_middle(agile_helper_page: Page):
    """Testa att det går att öppna valet "Någonstans mitt i" """

    # Hitta button med texten "Någonstans mitt i"
    middle_button = agile_helper_page.get_by_role(
        "button", name="Någonstans mitt i")

    # Klicka på knappen
    middle_button.click()

    # Finns texten "Mitt i sprinten" på sidan
    middle_text = agile_helper_page.get_by_text("Mitt i sprinten.")

    expect(middle_text).to_be_visible()

# -----------------------------------------------------------------------


def test_open_sprint_review(last_day_page: Page):
    """Testa att det går att se Sprint review"""
    # Hitta button med texten "Sprint review"
    sprint_review_button = last_day_page.get_by_role(
        "button", name=re.compile("Sprint review"))

    expect(sprint_review_button).to_be_visible()

    # Klicka på knappen "Sprint review"
    sprint_review_button.click()

    # Finns rubriken "Sprint review"?
    sprint_review_heading = last_day_page.get_by_role(
        "heading", name="Sprint review")

    expect(sprint_review_heading).to_be_visible()

# -----------------------------------------------------------------------


def test_open_sprint_retrospective(last_day_page: Page):
    """Testa att det går att se Sprint retrospective"""
    # Hitta button med texten "Sprint retrospective"
    sprint_retrospective_button = last_day_page.get_by_role(
        "button", name=re.compile("Sprint retrospective"))

    expect(sprint_retrospective_button).to_be_visible()

    # Klicka på knappen "Sprint retrospective"
    sprint_retrospective_button.click()

    # Finns rubriken "Sprint retrospective"?
    sprint_retrospective_heading = last_day_page.get_by_role(
        "heading", name="Sprint retrospective")
    expect(sprint_retrospective_heading).to_be_visible()
