import time

def highlight(element):
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)

    original_style = element.get_attribute('style')
    apply_style("border: 2px solid red;")
    time.sleep(.5)
    apply_style(original_style)