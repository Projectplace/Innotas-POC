import assertpy
from basepage import BasePage as DriverPage
from basepage.wait import ActionWait


class BasePage(DriverPage):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)

    @staticmethod
    def assert_that(value):
        return assertpy.assert_that(value)

    def wait_for_element_text(self, locator, text, params=None, timeout=10):

        def _do_wait():
            elements = self.get_present_elements(locator, params, timeout=0)
            for element in elements:
                txt = self.get_text(element)
                if txt is not None and text in txt:
                    return True
            return False

        return ActionWait(timeout).until(_do_wait, "Element text was never populated!")

    @staticmethod
    def get_compliant_locator(by, locator, params=None):
        """
        Returns a tuple of by and locator prepared with optional parameters.

        :param by: Type of locator (ie. CSS, ClassName, etc)
        :param locator: element locator
        :param params: (optional) locator parameters
        :return: tuple of by and locator with optional parameters
        """
        from selenium.webdriver.common.by import By

        if params is not None and not isinstance(params, dict):
            raise TypeError("<params> need to be of type <dict>, was <{}>".format(params.__class__.__name__))

        return getattr(By, by), locator.format(**(params or {}))
