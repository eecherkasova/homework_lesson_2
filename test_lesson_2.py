import pytest
from selene import be, have
from selene.support.shared import browser

@pytest.fixture
def window():
    browser.config.window_height(300)
    browser.config.window_width(500)



def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.quit()

def test_no_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qaswdefrgtyhujk').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу qaswdefrgtyhujk ничего не найдено'))

