"""Expected Conditions for WebDriverWait.

Custom conditions to use with `driver.wait.until()`.

Functions
----------
* element_displayed(element)
* element_disappears(element)
* elements_displayed(elements)

Usage
------
code-example::
    from framework.drivercore import waitconditions as wc
    self.driver.wait.until(wc.element_displayed(self.map.element))

Arguments
----------
An Element or Elements object.

Using the Map class is the recommended way to pass in the elements,
but you can also pass in a `find_element()` or `find_elements()` method call.
"""

__author__ = 'Carlos Kidman'


from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebElement
from framework.drivercore.element import Element, Elements


class element_displayed(object):
    """ An expectation for checking that an element is present on the DOM
    of a page. This does not necessarily mean that the element is visible.

    Returns
    --------
    The WebElement once it is located
    """
    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        by, value = self.element.locator
        element = _find_element(driver, by, value)
        return element


class element_disappears(object):
    """ An expectation for checking that an element is not present
    on the DOM of a page.

    Returns
    --------
    True if the element is not displayed, else False
    """
    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        try:
            by, value = self.element.locator
            _find_element(driver, by, value).is_displayed
            return False
        except:
            return True


class elements_displayed(object):
    """ An expectation for checking that at least
    one element is found when looking for a collection of elements.

    Returns
    --------
    The elements if length is greater than zero, else False
    """
    def __init__(self, elements):
        self.elements = elements

    def __call__(self, driver):
        by, value = self.elements.locator
        elements = _find_elements(driver, by, value)

        if len(elements) > 0:
            return elements
        else:
            return False


def _find_element(driver, by, value):
    """Looks up an element. Logs and re-raises ``WebDriverException``
    if thrown."""
    try:
        return driver.find_element(by, value)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e


def _find_elements(driver, by, value):
    try:
        return driver.find_elements(by, value)
    except WebDriverException as e:
        raise e
