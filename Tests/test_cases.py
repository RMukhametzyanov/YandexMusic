from Pages.authorization import Authorization
from Pages.playradio import PlayRadio
from Pages.create_playlist import CreateNewPlaylist

#smoke
"""
    Тест-кейс авторизации. Входим на сайт, указываем данные, авторизуемся. Проверяем, что авторизовались.
"""
def test_authorization(browser):
    authorization_main_page = Authorization(browser)
    authorization_main_page.go_to_site()
    authorization_main_page.login_button()
    authorization_main_page.sign_in('ForTestLogin', 'ForTestLogin123')
    authorization_main_page.sign_in_check()

#acceptance
"""
    Тест-кейс включения Радио. Авторизуемся, включаем Радио, выбираем волну, лайкаем песню. 
    Проверяем, что песня добавилась в плейлист Мне нравится. Удаляем ее оттуда
"""
def test_playradio(browser):
    authorization_main_page = Authorization(browser)
    authorization_main_page.go_to_site()
    authorization_main_page.login_button()
    authorization_main_page.sign_in('ForTestLogin', 'ForTestLogin123')
    authorization_main_page.sign_in_check()
    playradio_main_page = PlayRadio(browser)
    playradio_main_page.choose_radio()
    playradio_main_page.radio_sentiment()
    playradio_main_page.sentiment_spring()
    playradio_main_page.like_song()
    playradio_main_page.my_music()
    playradio_main_page.like_song_playlist()
    playradio_main_page.check_like_music()
    playradio_main_page.delete_song()
    playradio_main_page.check_song_deleted()

"""
    Тест кейс создания плейлиста и его удаления. Авторизуемся, создаем плейлист. 
    Проверяем, что он действительно создан. 
    Удаляем плейлист. Проверяем, что он действительно удален.
"""
def test_create_playlist(browser):
    authorization_main_page = Authorization(browser)
    authorization_main_page.go_to_site()
    authorization_main_page.login_button()
    authorization_main_page.sign_in('ForTestLogin', 'ForTestLogin123')
    authorization_main_page.sign_in_check()

    playradio_main_page = PlayRadio(browser)
    playradio_main_page.my_music()

    create_playlist_main_page = CreateNewPlaylist(browser)
    create_playlist_main_page.create_playlist()
    create_playlist_main_page.rename_new_playlist()

    playradio_main_page.my_music()
    create_playlist_main_page.delete_new_playlist()
