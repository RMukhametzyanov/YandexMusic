from selenium.webdriver.common.by import By
from Pages.BaseApp import BasePage
from Functions.Highlight import highlight
import time
import allure


#Локаторы
class PlayRadioPageLocators:
    LOCATOR_Radio_button =                  (By.CSS_SELECTOR, "[data-name='radio']")            # Кнопка "радио" в ленте на главной
    LOCATOR_RadioSentiment_button =         (By.CSS_SELECTOR, "[href='/radio/mood']")    # Кнопка "настроение" (радиоволна на радио)
    LOCATOR_SentimentSpring_button =        (By.XPATH, "//*[contains(text(),'Весеннее')]")      # Кнопка "Весеннее" (радиоволна в разделе "Настроение" на радио)
    LOCATOR_LikeSong_button =               (By.CSS_SELECTOR, ".d-like_theme-player")           # Кнопка "Нравится" в плеере
    LOCATOR_MyMusic =                       (By.CSS_SELECTOR, ".head__user-button")             # Кнопка "Моя музыка" в шапке для проверки
    LOCATOR_MyMusicUserName =               (By.CSS_SELECTOR, ".user__name")                    # Имя пользователя в разделе Моя музыка
    LOCATOR_MyFavoriteSong =                (By.CSS_SELECTOR, "[title='Мне нравится']")         # Кнопка "Мне нравится" (плей лист)
    LOCATOR_MyMusicPlayList =               (By.XPATH, "//*[contains(text(),'Плейлисты')]")     # Кнопка Плейлисты в разделе Моя музыка

    LOCATOR_LikeSongName =                  (By.CSS_SELECTOR, ".track__name-innerwrap")         # Название песни в плеере (для проверки песни, которая понравилась)
    LOCATOR_LikeSongArtist =                (By.CSS_SELECTOR, ".track__artists")                # Название исполнителя в плеере (Для проверки песни, которая понравилась)

    LOCATOR_LikeSongNameInMyPlaylist =      (By.CSS_SELECTOR, ".d-track__name")                 # Название первой песни в моем плейлисте
    LOCATOR_LikeSongArtistInMyPlaylist =    (By.CSS_SELECTOR, ".d-track__artists")              # Название исполнителя первой песни в моем плейлисте

class PlayRadio(BasePage):

    """
        Функция перехода в раздел Радио.
    """
    @allure.step("Переход в раздел Радио")
    def choose_radio(self):
        with allure.step("Поиск и клик по кнопке Радио"):
            choose_radio = self.find_element(PlayRadioPageLocators.LOCATOR_Radio_button)
            highlight(choose_radio)
            choose_radio.click()
            return choose_radio

    """
        Функция перехода в раздел Настроение на Радио. 
    """
    @allure.step("Выбор волны Настроение на радио")
    def radio_sentiment(self):
        with allure.step("Поиск и клик по кнопке Настроение (волна на Радио)"):
            sentiment_button = self.find_element(PlayRadioPageLocators.LOCATOR_RadioSentiment_button)
            highlight(sentiment_button)
            sentiment_button.click()
            return sentiment_button

    """
        Функция перехода на волну Весеннее в разделе Настроение на Радио. 
    """
    @allure.step("Выбор волны Весеннее в разделе Настроение на Радио")
    def sentiment_spring (self):
        with allure.step("слип, чтоб драйвер успел закрыть всплывающее окно 'Показывать уведомления' "
                         "(в conftest.py настройки профиля на разрешение показывать уведомления"):
            time.sleep(2)

        with allure.step("Поиск и клик по кнопке Весеннее (волна в разделе Настроение)"):
            spring_button = self.find_element(PlayRadioPageLocators.LOCATOR_SentimentSpring_button)
            highlight(spring_button)
            spring_button.click()
            return spring_button

    """
        Функция поставить отметку "Мне нравится" в проигрываемом плеере. 
    """
    @allure.step("Отметить 'Мне нравится' в плеере")
    def like_song(self):
        with allure.step("Поиск и клик по кнопке Мне нравится в плеере"):
            like_button = self.find_element(PlayRadioPageLocators.LOCATOR_LikeSong_button)
            highlight(like_button)
            like_button.click()

        with allure.step("Определение глобальных переменных: название песни и название артиста в плеере.  "
                         "Для дальнейшего сравнения их в плей-листе, что оно добавилось (метод check_like_music()"):
            global like_song_name, like_song_artist
            like_song_name = self.find_element(PlayRadioPageLocators.LOCATOR_LikeSongName).text
            like_song_artist = self.find_element(PlayRadioPageLocators.LOCATOR_LikeSongArtist).text
            print ("\nНазвание песни: ", like_song_name)
            print ("Название исполнителя: ", like_song_artist)

    """
        Функция перехода в раздел Моя музыка.
    """
    @allure.step("Переход в раздел 'Моя музыка'")
    def my_music(self):
        with allure.step("Поиск и клик по кнопке Моя музыка"):
            my_music_button = self.find_element(PlayRadioPageLocators.LOCATOR_MyMusic)
            highlight(my_music_button)
            my_music_button.click()

        with allure.step("Проверка, что имя пользователя отображается"):
            element_success = self.find_element(PlayRadioPageLocators.LOCATOR_MyMusicUserName).is_displayed()
            assert element_success, "Имя пользователя не отображается"
            return my_music_button

    """
        Функция перехода в плейлист Мне нравится.
    """
    @allure.step("Открытие плей листа с названием 'Мне нравится'")
    def like_song_playlist(self):
        with allure.step("Поиск и клик по кнопке Плейлисты, чтобы отобразить плейлисты"):
            choose_my_playlist = self.find_element(PlayRadioPageLocators.LOCATOR_MyMusicPlayList)
            highlight(choose_my_playlist)
            choose_my_playlist.click()

        with allure.step("Поиск и клик по плейлисту с названием 'Мне нравится'"):
            choose_my_favorite_playlist = self.find_element(PlayRadioPageLocators.LOCATOR_MyFavoriteSong)
            #делаем скрол до элемента, т.к. может появится реклама сверху, которая опустит наш элемент
            self.driver.execute_script("arguments[0].scrollIntoView();", choose_my_favorite_playlist)
            highlight(choose_my_favorite_playlist)
            choose_my_favorite_playlist.click()
            return choose_my_favorite_playlist

    """
        Функция проверки отмеченной песни в плеере, что она попала в плейлист Мне нравится.
        Сравниваем название и исполнителя песни из плеера с названием и исполнителем песни в плейлисте.
    """
    @allure.step("Проверка, что песня их плеера находится в плейлисте 'Мне нравится'")
    def check_like_music(self):
        with allure.step("Проверяем имя песни"):
            element_success_songname = self.find_element(PlayRadioPageLocators.LOCATOR_LikeSongNameInMyPlaylist).text
            assert (element_success_songname == like_song_name), \
                "Эталонный текст не равен текущему.\n" + \
                "Текущий: " + element_success_songname + "\nЭталонный: " + like_song_name

        with allure.step("Проверяем название исполнителя песни"):
            element_success_songartist = self.find_element(PlayRadioPageLocators.LOCATOR_LikeSongArtistInMyPlaylist).text
            assert (element_success_songartist == like_song_artist), \
                "Эталонный текст не равен текущему.\n" + \
                "Текущий: " + element_success_songartist + "\nЭталонный: " + like_song_artist
