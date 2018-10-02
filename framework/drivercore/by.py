"""Wrapper of Selenium's By class.

Simplifies the locator mechanisms used by Driver.

Usage
------
Using Selenium By:
    - driver.find_element(By.CSS_SELECTOR, "ul[data-testid='foo']")
    - driver.find_element_by_css_selector("ul[cool-attr='bar']")

Using new by:
    - driver.find_element(by.text('foo'))
    - driver.find_element(by.css("ul[cool-attr='bar']"))
"""

__author__ = 'Carlos Kidman'


from selenium.webdriver.common.by import By


def id(_id):
    """Locator by ID.
    
    Arguments
    ----------
    * _id (str): value of the "id" attribute.

    Returns
    --------
    Locator as Tuple of (By.ID, _id)
    """
    return By.ID, _id


def name(name):
    """Locator by name.
    
    Arguments
    ----------
    * name (str): value of the "name" attribute.

    Returns
    --------
    Locator as Tuple of (By.NAME, name)
    """
    return By.NAME, name


def css(css):
    """Locator by css selector.
    
    Arguments
    ----------
    * css (str): the css selector query.

    Returns
    --------
    Locator as Tuple of (By.CSS_SELECTOR, css)
    """
    return By.CSS_SELECTOR, css


def xpath(xpath):
    """Locator by xpath.
    
    Arguments
    ----------
    * xpath (str): the xpath query.

    Returns
    --------
    Locator as Tuple of (By.XPATH, xpath)
    """
    return By.XPATH, xpath


def link_text(text):
    """Locator by link text.
    
    Arguments
    ----------
    * text (str): the text value of the 'a' element.

    Returns
    --------
    Locator as Tuple of (By.LINK_TEXT, text)
    """
    return By.LINK_TEXT, text


def contains(text):
    """Locator by text contains.
    
    Arguments
    ----------
    * text (str): text() (or innerText) property contains the text.

    Returns
    --------
    Locator as Tuple of (By.XPATH, xpath query)
    """
    return By.XPATH, f"//*[contains(text(), '{text}')]"


def text(text):
    """Locator by text matches.
    
    Arguments
    ----------
    * text (str): text() (or innerText) property matches the text.

    Returns
    --------
    Locator as Tuple of (By.XPATH, xpath query)
    """
    return By.XPATH, f"//*[text()='{text}']"


def testid(_id):
    """Locator by data-testid.
    
    Arguments
    ----------
    * _id (str): value of the "data-testid" attribute.

    Returns
    --------
    Locator as Tuple of (By.XPATH, xpath query)
    """
    return By.XPATH, f"//*[@data-testid='{_id}']"
