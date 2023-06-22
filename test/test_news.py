import allure
import pytest

from pages.login_page import LoginPage
from pages.dash_page import DashPage


@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('1. Публикация новости в ленте')
@pytest.mark.skip
def test_publication_news():
    text_news = 'Новость тест'
    login = LoginPage()
    login.login_user()

    publication = DashPage()
    publication.publication_news(text_news)

@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('2. Поставить лайк')
@pytest.mark.skip
def test_like_news():
    publication = DashPage()
    publication.like_publication()


@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('3. Удаление новости из ленты')
@pytest.mark.skip
def test_delete_news():
    text_news = 'Новость тест'
    publication = DashPage()
    publication.delete_publication(text_news)




