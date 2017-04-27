from test_automation.page_objects.base_page import BasePage


class LoginPage(BasePage):

    urls = {'timesheets': 'https://{0}:{1}@q3.innotas.io/home.pa?entityType=timesheet&id=1708586024',
            'project': 'https://{0}:{1}@q3.innotas.io/home.pa#%5BT5%5DT%2Fdyn%2Fproject%2FprojectInfo'
                       '.pa%3Fx%3D1493236975819%26projectid%3D1535643530%26ssaView%3Dtrue',
            'issue': 'https://{0}:{1}@q3.innotas.io/home.pa?entityType=issue&id=1538529793&tabIndex=0',
            'issue_section': 'https://{0}:{1}@q3.innotas.io/home.pa#%5B%5DE%2Fentity%2Fissue%2F1538529793%2F5'}

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
        self.get(self.urls.get(link).format(username, password))
        page = self._get_page(link)
        page.verify_on_page()
        return page

    def logged_in_at(self, link, auth):
        self.get('https://q3.innotas.io')
        for cookie in auth:
            self.add_cookie(cookie.__dict__)
        self.get(self.urls.get(link))
        page = self._get_page(link)
        page.verify_on_page()
        return page

    def go_to(self, link):
        self.get(self.urls.get(link))
        page = self._get_page(link)
        page.verify_on_page()
        return page

    def _get_page(self, link):
        if link == 'timesheets':
            from test_automation.page_objects.timesheet_page import TimesheetPage as Page
        elif link == "project":
            from test_automation.page_objects.project_page import ProjectPage as Page
        elif link == 'issue':
            from test_automation.page_objects.issue_page import IssuePage as Page
        else:
            from test_automation.page_objects.issue_page import IssueSectionPage as Page
        return Page(self.driver)
