from selene import browser, be, have


def test_success(browser_settings):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_fail(browser_settings):
    text = "вдлыомдшщгу9гповмлдтотол"
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('div.card-section').should(have.text(f'Your search - {text} - did not match any documents.'))
