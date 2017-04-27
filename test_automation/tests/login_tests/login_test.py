from test_automation.page_objects.login_page import LoginPage


def test_login_to_timesheets(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('timesheets').\
        verify()


def test_login_to_timesheets2(driver, creds):
    LoginPage(driver).\
        login_at(link='timesheets', username=creds.username, password=creds.password).\
        verify()


def test_login_to_project(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('project').\
        verify()


def test_login_to_project2(driver, creds):
    LoginPage(driver).\
        login_at(link='project', username=creds.username, password=creds.password).\
        verify()


def test_login_to_issue(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('issue').\
        verify()


def test_login_to_issue2(driver, creds):
    LoginPage(driver).\
        login_at(link='issue', username=creds.username, password=creds.password).\
        verify()


def test_login_to_issue_section(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('issue_section').\
        verify()


def test_login_to_issue_section2(driver, creds):
    LoginPage(driver).\
        login_at(link='issue_section', username=creds.username, password=creds.password).\
        verify()
