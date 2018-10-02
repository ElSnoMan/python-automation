"""Classes and functionalities relevant to the WebDriver implementation.

Most of Selenium wants to be wrapped or extended for better control
of states, configs, and actions. This module deals with anything
pertaining to the WebDriver and its instances.

Classes
--------
Driver:
    * Wrapper of Selenium's WebDriver

Functions
----------
factory_create_driver(browser):
    * create specified instances of WebDriver
"""

__author__ = "Carlos Kidman"


import os
import platform
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.remote.webelement import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from framework.drivercore.element import Element, Elements


class Driver:
    """Wrapper of Selenium's WebDriver.
    
    Arguments
    ----------
    * browser (str): name of browser. ('chrome', 'firefox', etc.)
    """
    def __init__(self, browser):
        self.browser = browser
        self._driver = factory_create_driver(browser)
        self.wait = WebDriverWait(self._driver, 30, ignored_exceptions=(
            NoSuchElementException, 
            WebDriverException, 
            StaleElementReferenceException, 
            ElementNotVisibleException))

    @property
    def current(self):
        return self._driver

    @property
    def current_window_handle(self):
        return self.current.current_window_handle

    @property
    def page_source(self):
        return self.current.page_source

    @property
    def switch_to(self):
        return self.current.switch_to

    @property
    def title(self):
        return self.current.title

    @property
    def url(self):
        return self.current.current_url

    @property
    def window_handles(self):
        return self.current.window_handles

    def back(self):
        self.current.back()

    def close(self):
        self.current.close()

    def execute_script(self, js, *args):
        self.current.execute_script(js, args)

    def execute_async_script(self, js, *args):
        self.current.execute_async_script(js, args)

    def find_element(self, locator, name=""):
        by, string = locator
        web_element = self.wait.until(lambda drvr: drvr.find_element(by, string))
        element = Element(web_element, name)
        element.by = by
        element.locator_str = string
        return element

    def find_elements(self, locator):
        by, string = locator
        web_elements = self.current.find_elements(by, string)
        elements = Elements(web_elements)
        elements.by = by
        elements.locator_str = string
        return elements

    def forward(self):
        self.current.forward()

    def goto(self, url):
        self.current.get(url)

    def maximize_window(self):
        self.current.maximize_window()

    def quit(self):
        self.current.quit()

    def refresh(self):
        self.current.refresh()

    def save_screenshot(self, filename) -> bool:
        return self.current.save_screenshot(filename)


def factory_create_driver(browser):
    """Driver Factory.

    Builds a new instance of WebDriver and attaches its
    services to the browser's executable found in the `_drivers` directory.
    
    Arguments
    ----------
    * browser (str): name of the browser to build.

    Raises
    --------
    WebDriverException if invalid browser name.

    Returns
    --------
    New instance of WebDriver of the specified type.
    """
    driver = None
    os_name = platform.system().lower()
    driver_path = f"{os.getcwd()}/_drivers/{os_name}"

    if browser == "chrome":
        driver = Chrome(f"{driver_path}/chromedriver")

    elif browser == "firefox":
        driver = Firefox(f"{driver_path}/geckodriver")

    if driver == None:
        raise WebDriverException(f"invalid browser specified: {browser}")

    # doesn't maximize on mac or linux
    driver.maximize_window()
    return driver
