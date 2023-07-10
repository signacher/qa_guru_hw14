import allure
from pages.login_page import LoginPage
from pages.dash_page import DashPage


@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Благодарность')
@allure.story('1.Публикация благодарности в ленте')
def test_publication_thanks():
    text_thanks = 'Текст благодарности тест'
    login = LoginPage()
    login.login_user()

    publication = DashPage()
    publication.publication_thanks(text_thanks)


@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Благодарность')
@allure.story('2.Публикация комментария к благодарности')
def test_publication_comment():
    publication = DashPage()
    publication.publication_comment()

@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.epic('UI')
@allure.feature('Благодарность')
@allure.story('3.Удаление благодарности')
def test_delete_thanks():
    text_thanks = 'Текст благодарности тест'
    publication = DashPage()
    publication.delete_publication(text_thanks)
