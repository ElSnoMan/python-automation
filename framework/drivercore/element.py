"""Classes and functionalities relevant to the WebElement implementation.

Most of Selenium wants to be wrapped or extended for better control
of states, configs, and actions. This module deals with anything
pertaining to WebElement and its instances.

Classes
--------
Element:
    * Wrapper of Selenium's WebElement

Elements:
    * Wrapper for list of Element
"""

__author__ = "Carlos Kidman"


from collections.abc import Sequence
from selenium.webdriver.remote.webelement import WebElement, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains


class Element():
    """Wrapper of WebElement."""
    def __init__(self, webelement, name=""):
        self.by = None
        self.locator_str = None
        self.name = name
        self._webelement = webelement

    @property
    def current(self):
        return self._webelement

    @property
    def current_driver(self):
        return self.current.parent

    @property
    def id(self):
        return self.current.id

    @property
    def is_displayed(self):
        return self.current.is_displayed

    @property
    def is_enabled(self):
        return self.current.is_enabled

    @property
    def is_selected(self):
        return self.current.is_selected

    @property
    def locator(self):
        """The Locator used to find this element.

        This makes it simple to unpack and use for many of Selenium's APIs.
        
        Returns
        --------
        Tuple of the 'by mechanism' and the 'value' as (by, locator_str)
        """
        return (self.by, self.locator_str)

    @property
    def parent(self):
        js = 'return arguments[0].parentElement'
        parent = self.current_driver.execute_script(js)
        return Element(parent, '')

    @property
    def size(self) -> dict:
        return self.current.size

    @property
    def tag_name(self):
        return self.current.tag_name

    @property
    def text(self):
        return self.current.text

    def clear(self):
        self.current.clear()

    def click(self):
        self.current.click()

    def find_element(self, locator, name=""):
        by, string = locator
        web_element = self.current.find_element(by, string)
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

    def get_attribute(self, attr):
        return self.current.get_attribute(attr)

    def get_property(self, name):
        return self.current.get_property(name)

    def hover(self):
        hover = ActionChains(self.current_driver)
        hover.move_to_element(self.current).perform()

    def screenshot(self, filename):
        self.current.screenshot(filename)

    def send_keys(self, string):
        if self.get_attribute("value") == None or "":
            self.current.send_keys(string)

        elif self.get_attribute("value") != string:
            self.clear()
            self.current.send_keys(string)

        else:
            pass

    def submit(self):
        self.current.submit()


class Elements(Sequence):
    """Wrapper for list of Elements.
    
    Enables lists of Element and includes the `locator` property
    for working with many of WebDriver's APIs like WebDriverWait.
    """
    def __init__(self, webelements):
        self.by = None
        self.locator_str = None
        self.current = [Element(e) for e in webelements]

    @property
    def locator(self):
        return self.by, self.locator_str

    def __getitem__(self, index):
        return self.current[index]

    def __len__(self):
        return len(self.current)
