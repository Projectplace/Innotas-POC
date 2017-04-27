from base_page import BasePage


class ProjectPage(BasePage):

    _project_locator = ('CSS_SELECTOR', '.entityDetailSectionEditorEdit')
    _project_name_locator = ('CSS_SELECTOR', '.x-title-item')

    def verify_on_page(self):
        self.get_visible_element(self._project_locator)

    def verify(self):
        self.assert_that('Hardware Modernization').is_equal_to(self.get_text(self._project_name_locator))
