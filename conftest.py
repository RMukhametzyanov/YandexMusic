import pytest
from selenium import webdriver
import allure
from allure_commons.types import  AttachmentType
import datetime

#хук для скриншота
@pytest.hookimpl(hookwrapper = True, tryfirst = True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function", autouse=True)
def browser(request):

    with allure.step("Запускаем браузер с отключенными нотификациями"):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}  #1 = Allow, 2 = Blocked, 0 = default
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome("../Driver/chromedriver.exe", chrome_options = chrome_options )

    with allure.step("Полноэкранный режим"):
        driver.maximize_window()
    yield driver

    if request.node.rep_call.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(), name = "Screenshot", attachment_type = AttachmentType.PNG)
        except:
            pass

    driver.quit()

