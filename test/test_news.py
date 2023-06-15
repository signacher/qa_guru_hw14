import allure
from pages.login_page import LoginPage
from pages.dash_page import DashPage


@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('1. Публикация новости в ленте')
def test_publication_news():
    login = LoginPage()
    login.login_user()

    publication = DashPage()
    publication.publication_news()

@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('Поставить лайк')
def test_like_news():
    publication = DashPage()
    publication.like_news()

@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('3. Удаление новости из ленты')
def test_delete_news():
    publication = DashPage()
    publication.delete_news()




