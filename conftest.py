import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: da, de, en-gb, es, fr, it, ru, uk")


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def ch_lang(request):
    lang = request.config.getoption("language")
    ch_lang = None
    if lang == "da":
        print("\nstart language Dansk")
        ch_lang = "da"
    elif lang == "de":
        print("\nstart language Deutsch")
        ch_lang = "de"
    elif lang == "en-gb":
        print("\nstart language British English")
        ch_lang = "en-gb"
    elif lang == "es":
        print("\nstart language Español")
        ch_lang = "es"
    elif lang == "fr":
        print("\nstart language Français")
        ch_lang = "fr"
    elif lang == "it":
        print("\nstart language Italiano")
        ch_lang = "it"
    elif lang == "ru":
        print("\nstart language Русский")
        ch_lang = "ru"
    elif lang == "uk":
        print("\nstart language Українська")
        ch_lang = "uk"
    else:
        raise pytest.UsageError("--language should be da, de, en-gb, es, fr, it, ru, uk")
    yield ch_lang
