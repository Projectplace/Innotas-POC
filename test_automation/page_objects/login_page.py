from test_automation.page_objects.base_page import BasePage


class LoginPage(BasePage):

    urls = {1: 'https://q3.innotas.io/home.pa?entityType=timesheet&id=1708586024',
            2: '',
            3: '',
            4: ''}  # These would obviously have better names

    _username_locator = ('CSS_SELECTOR', '#login')
    _password_locator = ('CSS_SELECTOR', '#password')
    _login_button_locator = ('CSS_SELECTOR', '#UserPassForm button')
    _timesheets_locator = ('CSS_SELECTOR', '.x-title-item')

    def login(self, username, password):
        self.get('https://q3.innotas.io/index.jsp')
        self.enter_text(self._username_locator, username)
        self.enter_text(self._password_locator, password)
        self.click(self._login_button_locator)
        self.get_visible_element(self._timesheets_locator)
        return self

    def login_at(self, link, username, password):
        self.get("https://www.google.com")
        self.get(self.urls.get(link))
        alert = self.switch_to.alert
        alert.authenticate(username, password)

    def go_to_timesheets(self):
        from test_automation.page_objects.timesheet_page import TimesheetPage

        self.get(self.urls.get(1))
        self.get_visible_element(self._timesheets_locator)
        return TimesheetPage(self.driver)
