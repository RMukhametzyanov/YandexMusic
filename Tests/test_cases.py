from Pages.authorization import Authorization
from Pages.playradio import PlayRadio
from Pages.clean_playlist import CleanPlaylist

def test_authorization(browser):
    authorization_main_page = Authorization(browser)
    authorization_main_page.go_to_site()
    authorization_main_page.login_button()
    authorization_main_page.sign_in('ForTestLogin', 'ForTestLogin123')
    authorization_main_page.sign_in_check()

def test_playradio(browser):
    authorization_main_page = Authorization(browser)
    authorization_main_page.go_to_site()
    authorization_main_page.login_button()
    authorization_main_page.sign_in('ForTestLogin', 'ForTestLogin123')
    authorization_main_page.sign_in_check()
    playradio_main_page = PlayRadio(browser)
    playradio_main_page.go_to_site()
    playradio_main_page.choose_radio()
    playradio_main_page.radio_sentiment()
    playradio_main_page.sentiment_spring()
    playradio_main_page.like_song()
    playradio_main_page.my_music()
    playradio_main_page.like_song_playlist()
    playradio_main_page.check_like_music()


def test_clean_play_list(browser):
    authorization_main_page = Authorization(browser)
    authorization_main_page.go_to_site()
    authorization_main_page.login_button()
    authorization_main_page.sign_in('ForTestLogin', 'ForTestLogin123')
    authorization_main_page.sign_in_check()
    cleanplaylist_main_page = CleanPlaylist(browser)
    cleanplaylist_main_page.go_to_site()
    cleanplaylist_main_page.my_music()
    cleanplaylist_main_page.like_song_playlist()
    cleanplaylist_main_page.delete_song()
    cleanplaylist_main_page.check_song_deleted()
