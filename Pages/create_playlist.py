from selenium.webdriver.common.by import By
from Pages.BaseApp import BasePage
from Functions.Highlight import highlight
from selenium.webdriver.common.keys import Keys
import allure
import random, string

#Локаторы
class CreateNewPlayListPageLocators:
    LOCATOR_CreateNewPlayList =             (By.CSS_SELECTOR, ".playlist_type_new")         # Клик на "+" для создания нового плейлиста
    LOCATOR_CheckTitleValueNewPlayList =    (By.CSS_SELECTOR, ".page-playlist__title")      # Заголовок нового плейлиста. Для проверки и последующего переименования
    LOCATOR_PlaylistForDelete =             (By.CSS_SELECTOR, ".playlist__title-link")   # Созданный плейлист с названием "Мой плейлист"
    LOCATOR_OpenPlaylistContextMenu =       (By.CSS_SELECTOR, ".d-context-menu__opener")    # Кнопка вызова контекстного меню в плейлисте
    LOCATOR_DeleteContextMenu =             (By.XPATH, "//*[contains(text(),'Удалить плейлист')]") # Кнопка удаления плейлиста в контектсном меню
    LOCATOR_DeleteConfirmation =            (By.CSS_SELECTOR, ".deco-button-caution")       # Кнопка Да для подтверждения удаления плейлиста
    LOCATOR_ContextMenu =                   (By.CSS_SELECTOR, ".d-context-menu .d-tooltip__message") #Для проверки текста в контектсном меню

class CreateNewPlaylist(BasePage):

    """
        Функция создания нового плейлиста.
    """
    @allure.step("Создание нового плейлиста")
    def create_playlist(self):
        with allure.step("Клик на создание нового плейлиста"):
            create_new_playlist = self.find_element(CreateNewPlayListPageLocators.LOCATOR_CreateNewPlayList)
            highlight(create_new_playlist)
            # скролим до элемента из-за рекламы сверху
            self.driver.execute_script("arguments[0].scrollIntoView();", create_new_playlist)
            create_new_playlist.click()

    """
        Функция проверки, что плейлист создан
    """

    @allure.step("Проверка, что новый плейлист создан")
    def check_title_new_playlist(self):
        with allure.step("Проверяем наличие 'Плейлист пока пуст'"):
            # Эталонный текст
            success_text = "Новый плейлист"
            element_success = self.find_element(CreateNewPlayListPageLocators.LOCATOR_CheckTitleValueNewPlayList).getAttribute("value")

            # Сравниваем полученный текст от элемента с эталонным
            assert (str(element_success) != success_text), \
                "Эталонный текст не равен текущему.\n" + \
                "Текущий: " + element_success + "\nЭталонный: " + success_text

    """
        Функция переименования созданного плейлиста
    """
    @allure.step("Переименование созданного плейлиста")
    def rename_new_playlist(self):
        global playlist_name   # будем использовать в функции delete_new_playlist ()
        playlist_name = "Мой плейлист [" + ''.join(random.choice(string.ascii_letters) for i in range(5)) + "]"

        with allure.step("переименовываем плейлист"):
            playlist_title = self.find_element(CreateNewPlayListPageLocators.LOCATOR_CheckTitleValueNewPlayList)
            highlight (playlist_title)
            playlist_title.click()
            playlist_title.send_keys(Keys.CONTROL + 'a')    # Выделяем весь текст
            playlist_title.send_keys(playlist_name)         # Указываем название плейлиста
            playlist_title.send_keys(Keys.ENTER)            # Сохраняем нажатием на Enter

    """
            Функция удаления созданного плейлиста
    """
    @allure.step("Переименование созданного плейлиста")
    def delete_new_playlist(self):

        with allure.step("Ищем созданный плейлист и открываем его"):
            # Находим все тайтлы всех плейлистов
            playlist_for_delete = self.find_elements(CreateNewPlayListPageLocators.LOCATOR_PlaylistForDelete)
            # в цикле пробиваем наш плейлист, если совпдает -> кликаем на найденный плейлист и выходим из цикла
            for my_list in playlist_for_delete:
                if my_list.text == playlist_name:
                    # скролим до нашего плейлиста из-за рекламы сверху
                    self.driver.execute_script("arguments[0].scrollIntoView();", my_list)  # Делаем скрол до плейлиста, т.к реклама сверху
                    highlight (my_list)
                    my_list.click()
                    break

        with allure.step("Ищем кнопку контектсного меню, открываем ее и жмем на 'удалить плейлист'"):
            # ищем кнопку контектсного меню, клик на нее
            context_menu_button = self.find_element(CreateNewPlayListPageLocators.LOCATOR_OpenPlaylistContextMenu)
            context_menu_button.click()
            # ищем пункт "удалить плейлист"
            delete_context_menu_button = self.find_element(CreateNewPlayListPageLocators.LOCATOR_DeleteContextMenu)
            delete_context_menu_button.click()

        with allure.step("Подтверждаем удаление, нажав на 'Да'"):
            # В контекстном меню жмем "да"
            Delete_confirmation = self.find_element(CreateNewPlayListPageLocators.LOCATOR_DeleteConfirmation)
            Delete_confirmation.click()

        with allure.step("Проверяем среди всех названий плейлистов, что удален тот, который создавали"):
            # находим все тайтлы всех плейлистов
            all_playlist_title = self.find_elements(CreateNewPlayListPageLocators.LOCATOR_PlaylistForDelete)
            # загоняем их в список
            list = [x.text for x in all_playlist_title if len(x.text) > 0]
            # Пробиваем , что название созданного плейлиста не входит в список найденных названий других плейлистов
            assert (playlist_name not in str(list)), "В меню присутствуют: " + str(playlist_name)
            return list
