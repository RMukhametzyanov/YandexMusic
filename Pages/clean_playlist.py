from selenium.webdriver.common.by import By
from Pages.BaseApp import BasePage
from Functions.Highlight import highlight
from selenium.webdriver.common.action_chains import ActionChains #Для ховера на песне в плей-листе
import time
import allure



#Локаторы
class CleanPlayListPageLocators:
    LOCATOR_MyMusic =                       (By.CSS_SELECTOR, ".head__user-button")         # Кнопка "Моя музыка" в шапке для проверки
    LOCATOR_MyMusicUserName =               (By.CSS_SELECTOR, ".user__name")                # Имя пользователя в разделе Моя музыка
    LOCATOR_MyMusicPlayList =               (By.CSS_SELECTOR, "[title='Мне нравится']")     # Кнопка "Мне нравится" (плей лист)
    LOCATOR_LikeSongNameInMyPlaylist =      (By.CSS_SELECTOR, ".d-track__name")             # Название первой песни в моем плейлисте
    LOCATOR_LikeSongArtistInMyPlaylist =    (By.CSS_SELECTOR, ".d-track__artists")          # Название исполнителя первой песни в моем плейлисте
    LOCATOR_DeleteSong_button =             (By.CSS_SELECTOR, "[title='Удалить трек']")     # Удаление песни их плей-листа
    LOCATOR_PlaylistEmpty =                 (By.CSS_SELECTOR, ".playlist-dummy__title")     # Все песни в плейлисте

class CleanPlaylist(BasePage):

    @allure.step("Переход в раздел 'Моя музыка'")
    def my_music(self):
        with allure.step("Поиск и клик по кнопке 'Моя музыка'"):
            my_music_button = self.find_element(CleanPlayListPageLocators.LOCATOR_MyMusic)
            highlight(my_music_button)
            my_music_button.click()

        with allure.step("Проверка на имя пользователя, что переход осуществлен"):
            success_text = "ForTestLogin"
            element_success = self.find_element(CleanPlayListPageLocators.LOCATOR_MyMusicUserName).text
            # Сравниваем полученный текст от элемента с эталонным
            assert (element_success == success_text), \
                "Эталонный текуст не равен текущему.\n" + \
                "Текущий: " + element_success + "\nЭталонный: " + success_text

    @allure.step("Открытие плей листа с названием 'Мне нравится'")
    def like_song_playlist(self):
        with allure.step("Cлип, чтоб драйвер успел закрыть всплывающее окно 'Показывать уведомления' "
                         "(в conftest.py настройки профиля на разрешение показывать уведомления"):
            time.sleep(2)

        with allure.step("Поиск и клик по плейлисту с названием 'Мне нравится'"):
            choose_my_playlist = self.find_element(CleanPlayListPageLocators.LOCATOR_MyMusicPlayList)
            highlight(choose_my_playlist)
            choose_my_playlist.click()
            return choose_my_playlist

    @allure.step("Удаление песни из плейлиста")
    def delete_song(self):
        with allure.step("Поиск песни в плейлисте"):
            name_song_for_delete = self.find_element(CleanPlayListPageLocators.LOCATOR_LikeSongNameInMyPlaylist)
            highlight(name_song_for_delete)

        with allure.step("Ховер по песне для отображения кнопки 'удалить'"):
            hover = ActionChains(self.driver).move_to_element(name_song_for_delete)
            hover.perform()

        with allure.step("Поиск и клик по кнопке 'Удаление'"):
            delete_song = self.find_element(CleanPlayListPageLocators.LOCATOR_DeleteSong_button)
            highlight(delete_song)
            delete_song.click()

    @allure.step("Проверка на пустой плейлист")
    def check_song_deleted(self):
        with allure.step("Проверяем наличие 'Плейлист пока пуст'"):
            # Эталонный текст
            success_text = "Плейлист пока пуст"
            element_success = self.find_element(CleanPlayListPageLocators.LOCATOR_PlaylistEmpty).text
            # Сравниваем полученный текст от элемента с эталонным
            assert (element_success == success_text), \
                "Эталонный текст не равен текущему.\n" + \
                "Текущий: " + element_success + "\nЭталонный: " + success_text
