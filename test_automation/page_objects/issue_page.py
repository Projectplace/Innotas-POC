from base_page import BasePage


class IssuePage(BasePage):

    _issue_locator = ('CSS_SELECTOR', '[data-ref="innerCt"]')
    _issue_title_locator = ('CSS_SELECTOR', '.x-title-item')

    def verify_on_page(self):
        self.get_visible_element(self._issue_locator)

    def verify(self):
        self.assert_that('Project Log: Outdated hardware causing difficulties during upgrade').\
            is_equal_to(self.get_text(self._issue_title_locator))


class IssueSectionPage(IssuePage):

    _issue_section_locator = ('CSS_SELECTOR', '.x-toolbar')
    _alert_rows_locator = ('CSS_SELECTOR', '.x-grid-item')

    def verify_on_page(self):
        self.get_visible_element(self._issue_section_locator)

    def get_alert_rows(self):
        return self.get_visible_elements(self._alert_rows_locator)

    def verify(self):
        super(IssueSectionPage, self).verify()
        self.assert_that(self.get_alert_rows()).is_length(2)