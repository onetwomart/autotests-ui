import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_box = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_box).to_be_visible()
        expect(courses_box).to_have_text('Courses')

        icon_is_visible = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_is_visible).to_be_visible()

        no_results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_text).to_be_visible()
        expect(no_results_text).to_have_text('There is no results')

        results_from_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(results_from_text).to_be_visible()
        expect(results_from_text).to_have_text('Results from the load test pipeline will be displayed here')

        chromium_page_with_state.wait_for_timeout(5000)