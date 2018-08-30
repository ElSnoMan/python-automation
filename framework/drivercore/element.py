"""Classes and functionalities relevant to the WebElement implementation.

Most of Selenium wants to be wrapped or extended for better control
of states, configs, and actions. This module deals with anything
pertaining to WebElement and its instances.

Classes:
    - Element: Wrapper of Selenium's WebElement
"""

__author__ = "Carlos Kidman"

from selenium.webdriver.remote.webelement import WebElement, WebDriverException


class Element:
    def __init__(self, webelement: WebElement):
        self.by = None
        self.locator_str = None
        self._webelement = webelement

    @property
    def current_driver(self):
        return self._webelement.parent

    @property
    def id(self):
        return self._webelement.id

    @property
    def is_displayed(self):
        return self._webelement.is_displayed

    @property
    def is_enabled(self):
        return self._webelement.is_enabled

    @property
    def is_selected(self):
        return self._webelement.is_selected

    @property
    def locator(self) -> tuple:
        if self.by == None or self.locator_str == None:
            raise ValueError("by and/or locator_str properies are null")
        return (self.by, self.locator_str)

    @property
    def size(self) -> dict:
        return self._webelement.size

    @property
    def tag_name(self):
        return self._webelement.tag_name

    @property
    def text(self):
        return self._webelement.text

    def clear(self):
        self._webelement.clear()

    def click(self):
        self._webelement.click()

    def find_element(self, by, string):
        return self._webelement.find_element(by, string)

    def find_elements(self, by, string):
        return self._webelement.find_elements(by, string)

    def get_attribute(self, attr):
        return self._webelement.get_attribute(attr)

    def get_property(self, name):
        return self._webelement.get_property(name)

    def screenshot(self, filename):
        self._webelement.screenshot(filename)

    def send_keys(self, string):
        self._webelement.send_keys(string)

    def submit(self):
        self._webelement.submit()
