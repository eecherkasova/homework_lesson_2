import pytest
import selene
from selene import be, have


@pytest.fixture
def window():
    selene.browser.config.window_height = 350
    selene.browser.config.window_width = 550



def test_google_search(window):
    selene.browser.open('https://google.com')
    selene.browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    selene.browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    selene.browser.quit()

def test_no_result(window):
    selene.browser.open('https://google.com')
    selene.browser.element('[name="q"]').should(be.blank).type('qaswdefrgtyhujk').press_enter()
    selene.browser.element('[class="card-section"]').should(have.text('По запросу qaswdefrgtyhujk ничего не найдено'))

