from selenium.webdriver.common.by import By
from Pages.BaseApp import BasePage
from Functions.Highlight import highlight

import allure


"""
Данные для входа: ForTestLogin / ForTestLogin123
"""
class AuthorizationPageLocators:
    LOCATOR_login_button =          (By.CSS_SELECTOR, ".log-in")                    #Кнопка "Войти" для перехода к форме авторизации
    LOCATOR_LoginName_field =       (By.XPATH, "//*[@id='passp-field-login']")      #поле ввода Логина
    LOCATOR_SignIn_button =         (By.CSS_SELECTOR,".passp-sign-in-button")       #Кнопка "Войти" для непосредственной авторизации
    LOCATOR_PassWord_field =        (By.CSS_SELECTOR, "[name='passwd']")            #Поле ввода пароля
    LOCATOR_MyMusic =               (By.CSS_SELECTOR, ".head__user-button")         #"Моя музыка" в шапке. для проверки


class Authorization(BasePage):

    @allure.step("Переход на форму авторизации по кнопке 'Войти'")
    def login_button(self):
        with allure.step("Клик по кнопке Войти"):
            login_button = self.find_element(AuthorizationPageLocators.LOCATOR_login_button)
            highlight(login_button)
            login_button.click()
            return login_button

    @allure.step("Ввод логина и пароля")
    def sign_in (self, login, password):
        with allure.step("Переключаю фокуса на соседнюю вкладку"):
            #Определение второй вкладки и переключение на нее через switch_to_window
            windows_after = self.driver.window_handles[1]
            self.driver.switch_to_window(windows_after)

        with allure.step("Ввод логина"):
            login_name = self.find_element(AuthorizationPageLocators.LOCATOR_LoginName_field)
            highlight(login_name)
            login_name.click()
            login_name.send_keys(login)

        with allure.step("Переключаю форму для ввода пароля"):
            sign_in = self.find_element(AuthorizationPageLocators.LOCATOR_SignIn_button)
            highlight(sign_in)
            sign_in.click()

        with allure.step("Ввод пароля"):
            login_password = self.find_element(AuthorizationPageLocators.LOCATOR_PassWord_field)
            highlight(login_password)
            login_password.click()
            login_password.send_keys(password)

        with allure.step("Клик на Войти после указания всех данных"):
            sign_in = self.find_element(AuthorizationPageLocators.LOCATOR_SignIn_button)
            highlight(sign_in)
            sign_in.click()

    @allure.step('Проверка после входа. Чекаем "Моя музыка"')
    def sign_in_check(self):
        with allure.step("Переключаю на первую вкладку"):
            #Определение первой вкладки и переключение на нее через switch_to_window, т.к. форма авторизации была на второй вкладке
            windows_before = self.driver.window_handles[0]
            self.driver.switch_to_window(windows_before)

        with allure.step("Сравнение с эталонным текстом"):
            #Эталонный текст
            success_text = "Моя музыка"
            element_success = self.find_element(AuthorizationPageLocators.LOCATOR_MyMusic).text
            #Сравниваем полученный текст от элемента с эталонным
            assert (element_success == success_text), "Эталонный текст не равен текущему.\n" + "Текущий: " + element_success + "\nЭталонный: " + success_text
