from test_automation.page_objects.base_page import BasePage


class TimesheetPage(BasePage):

    _timesheets_locator = ('CSS_SELECTOR', '.x-title-item')
    _submit_button_locator = ('CSS_SELECTOR', '[data-ref=btnInnerEl]')

    def verify_on_page(self):
        self.get_visible_element(self._timesheets_locator)

    def verify(self):
        self.get_present_element(self._submit_button_locator)
        # etc...
