import time

import allure
from selene.support.shared import browser
from selene import have, query, be
import selene
from selenium.webdriver import ActionChains


class DashPage:
    def publication_news(self):
        with allure.step('Открываем форму отправки новости'):
            browser.element('#news').click()
        with allure.step('Вызываем редактор в поле ввода текста новости'):
            browser.element('.DraftEditorMui5').click()

        with allure.step('Вводим в поле ввода текст новости'):
            browser.element('//div[@class="notranslate public-DraftEditor-content" and @role="combobox"]').type('Новость тест').press_tab()

        time.sleep(1)

        with allure.step('Нажимаем кнопку Опубликовать'):
            # browser.all('.MuiButton-sizeLarge').element_by(have.exact_text('ОПУБЛИКОВАТЬ')).perform(selene.command.js.click)
            browser.element('#SENDNEWSBUTTON').should(be.clickable).click()

        time.sleep(1)

        browser.driver.refresh()

        with allure.step('Проверяем наличие новости в ленте после обновления страницы по тексту новости'):
            browser.all('.CommonmarkRender-Paragraph')[0].should(have.text('Новость тест'))


    def like_news(self):
        with allure.step('Нажимаем нравится'):
            browser.all('.NewsActions-Like')[0].click()
        with allure.step('Обновляем страницу'):
            browser.driver.refresh()
        with allure.step('проверяем число лайков'):
            browser.all('.Bable')[1].should(have.text('1'))


    def delete_news(self):
        with allure.step('Вызываем контекстное меню'):
            browser.element('.ContextMenu-Toggle').perform(selene.command.js.click)
        with allure.step('В меню выбираем Удалить'):
            browser.all('.ContextMenu-Item').element_by(have.text('Удалить')).click()
        with allure.step('Нажимаем Подтвердить удаление'):
            button_confirm = browser.all('.Confirm-Button').element_by(have.text('Подтвердить'))
            button_confirm.click()
            browser.driver.refresh()
            browser.element('.CommonmarkRender-Paragraph').should(be.present)

        with allure.step('Проверяем отсутствие новости в ленте по тексту новости'):
            news = browser.element('.CommonmarkRender-Paragraph').should(be.present).get(query.text)
            print('Текст последней публикации в ленте после удаления: ',news)
            assert news != 'Новость тест',f'Новость не удалена!!!Текст новости {news}'

    def publication_thanks(self):
        with allure.step('Открываем форму отправки благодарности'):
            browser.element('#thanks').click()
        with allure.step('Вводим Кого поблагодарить'):
            browser.all('.MuiOutlinedInput-input')[1].click()
            browser.all('.MuiAvatar-root').element_by(have.exact_text('Арнольд Шварцнегер')).perform(selene.command.js.click)
            time.sleep(4)

        # with allure.step('Вводим в поле ввода текст новости'):
        #     browser.element('//div[@class="notranslate public-DraftEditor-content" and @role="combobox"]').type(
        #     'Новость тест').press_tab()

    time.sleep(1)


