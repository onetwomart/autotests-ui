import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('dmitr.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('user')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('pass')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state_new.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state_new.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_box = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_box).to_be_visible()
        expect(courses_box).to_have_text('Courses')

        icon_is_visible = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_is_visible).to_be_visible()

        no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_text).to_be_visible()
        expect(no_results_text).to_have_text('There is no results')

        results_from_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(results_from_text).to_be_visible()
        expect(results_from_text).to_have_text('Results from the load test pipeline will be displayed here')

        page.wait_for_timeout(5000)