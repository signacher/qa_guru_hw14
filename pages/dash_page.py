import time

import allure
from selene.support.shared import browser
from selene import have, query, be
import selene


class DashPage:
    def publication_news(self, text_publication):
        with allure.step('Открываем форму отправки новости'):
            browser.element('#news').click()
        with allure.step('Вызываем редактор в поле ввода текста новости'):
            browser.element('.DraftEditorMui5').click()

        with allure.step('Вводим в поле ввода текст новости'):
            browser.element('//div[@class="notranslate public-DraftEditor-content" and @role="combobox"]'
                            ).type(text_publication).press_tab()

        time.sleep(1)

        with allure.step('Нажимаем кнопку Опубликовать'):
            browser.element('#SENDNEWSBUTTON').should(be.clickable).click()

        time.sleep(1)

        browser.driver.refresh()

        with allure.step('Проверяем наличие новости в ленте после обновления страницы по тексту новости'):
            browser.all('.CommonmarkRender-Paragraph')[0].should(have.text(text_publication))


    def like_publication(self):
        with allure.step('Нажимаем нравится'):
            browser.all('.NewsActions-Like')[0].click()
        with allure.step('Обновляем страницу'):
            browser.driver.refresh()
        with allure.step('проверяем число лайков'):
            browser.all('.Bable')[1].should(have.text('1'))

    def delete_publication(self,text_publication):
        with allure.step('Вызываем контекстное меню'):
            browser.element('.ContextMenu-Toggle').perform(selene.command.js.click)
        with allure.step('В меню выбираем Удалить'):
            browser.all('.ContextMenu-Item').element_by(have.text('Удалить')).click()
        with allure.step('Нажимаем Подтвердить удаление'):
            button_confirm = browser.all('.Confirm-Button').element_by(have.text('Подтвердить'))
            button_confirm.click()
            time.sleep(2)
            browser.driver.refresh()
            browser.element('.CommonmarkRender-Paragraph').should(be.present)

        with allure.step('Проверяем отсутствие публикации в ленте по тексту'):
            text_last_publication = browser.element('.CommonmarkRender-Paragraph').should(be.present).get(query.text)
            print('Текст последней публикации в ленте после удаления: ',text_last_publication)
            assert text_last_publication != text_publication,f'Публикация не удалена!!!Текст последней публикации: {text_last_publication}'

    def publication_thanks(self,text_publication):
        with allure.step('Открываем форму отправки благодарности'):
            browser.element('#thanks').click()
        with allure.step('Вводим Кого поблагодарить'):
            # browser.all('.MuiOutlinedInput-input')[1].click()
            # browser.all('.MuiListItem-root').element_by(have.text('Тестер Первый')).click().press_tab()
            browser.all('.MuiOutlinedInput-input')[1].click().send_keys('Тестер Первый')
            time.sleep(1)
            browser.element('.PrivateSwitchBase-input').click()
            browser.all('.MuiOutlinedInput-root')[1].click()
            browser.all('.MuiOutlinedInput-input')[1].press_escape()
        with allure.step('Вызываем редактор в поле ввода текста благодарности'):
            browser.element('.DraftEditorMui5').click()
        with allure.step('Вводим в поле ввода текст благодарности'):
            browser.element('//div[@class="notranslate public-DraftEditor-content" and @role="combobox"]'
                            ).type(text_publication)
            time.sleep(1)
        with allure.step('Вводим сумму благодарности'):
            browser.element('//input[@inputmode="numeric"]').click().type('5')
        with allure.step('Выбираем причину благодарности'):
            browser.all('.MuiAutocomplete-endAdornment')[1].click()
            browser.all('.MuiAutocomplete-option').element_by(have.text('Забота о продукте')).click()
        with allure.step('Нажимаем кнопку Опубликовать'):
            browser.element('#SENDNEWSBUTTON').should(be.clickable).click()
            time.sleep(1)

        browser.driver.refresh()

        with allure.step('Проверяем наличие благодарности в ленте после обновления страницы по тексту'):
            browser.all('.CommonmarkRender-Paragraph')[0].should(have.text(text_publication))
            time.sleep(1)

    def publication_comment(self):
        with allure.step('Вводим текст комментария'):
            browser.all('.public-DraftEditorPlaceholder-inner')[0].click()
            browser.all('.public-DraftStyleDefault-block')[1].type('Текст комментария')
            browser.all('.Button_border')[1].click()
            time.sleep(1)
        with allure.step('Проверяем появление комментария'):
            browser.all('.CommonmarkRender-Paragraph')[1].should(have.text('Текст комментария'))
            browser.driver.refresh()
        with allure.step('Проверяем yналичие комментария после обновления страницы'):
            browser.all('.CommonmarkRender-Paragraph')[1].should(have.text('Текст комментария'))