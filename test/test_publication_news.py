import allure
from pages.login_page import LoginPage
from pages.dash_page import DashPage


@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('Публикация новости в ленте')
def test_publication_news():
    login = LoginPage()
    login.login_user()

    publication = DashPage()
    publication.publication_news()
    publication.delete_news()




