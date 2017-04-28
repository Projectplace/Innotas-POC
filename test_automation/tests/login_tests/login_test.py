from test_automation.page_objects.login_page import LoginPage

# Feature: Arrive properly at various destinations after a login challenge

# Background:
# The user gets a link in an email to a specific Innotas page/object
# And the user follows this link in a fresh browser
# And the user does not allow the browser to cache HTTP-Auth credentials (the native username/password box)


# Scenario: User from Non-SSO Customer Following Timesheet Links
def test_login_to_timesheets(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('timesheets').\
        verify()


def test_login_to_timesheets2(driver, creds):
    LoginPage(driver).\
        login_at(link='timesheets', username=creds.username, password=creds.password).\
        verify()


def test_login_to_timesheets3(driver, do_auth):
    LoginPage(driver).\
        logged_in_at(link='timesheets', auth=do_auth).\
        verify()


def test_login_to_timesheets4(driver, creds):
    LoginPage(driver).\
        login_with_alert(link='timesheets', username=creds.username, password=creds.password).\
        verify()


# Scenario: User from Non-SSO Customer Following Anchor Link to a Project
def test_login_to_project(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('project').\
        verify()


def test_login_to_project2(driver, creds):
    LoginPage(driver).\
        login_at(link='project', username=creds.username, password=creds.password).\
        verify()


def test_login_to_project3(driver, do_auth):
    LoginPage(driver).\
        logged_in_at(link='project', auth=do_auth).\
        verify()


def test_login_to_project4(driver, creds):
    LoginPage(driver).\
        login_with_alert(link='project', username=creds.username, password=creds.password).\
        verify()


# Scenario: User from a Non-SSO Customer Follows Parameterized Issue Link
def test_login_to_issue(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('issue').\
        verify()


def test_login_to_issue2(driver, creds):
    LoginPage(driver).\
        login_at(link='issue', username=creds.username, password=creds.password).\
        verify()


def test_login_to_issue3(driver, do_auth):
    LoginPage(driver).\
        logged_in_at(link='issue', auth=do_auth).\
        verify()


def test_login_to_issue4(driver, creds):
    LoginPage(driver).\
        login_with_alert(link='issue', username=creds.username, password=creds.password).\
        verify()


# Scenario: User from a Non-SSO Customer Follows an Anchor Link to an Issue Section
def test_login_to_issue_section(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to('issue_section').\
        verify()


def test_login_to_issue_section2(driver, creds):
    LoginPage(driver).\
        login_at(link='issue_section', username=creds.username, password=creds.password).\
        verify()


def test_login_to_issue_section3(driver, do_auth):
    LoginPage(driver).\
        logged_in_at(link='issue_section', auth=do_auth).\
        verify()


def test_login_to_issue_section4(driver, creds):
    LoginPage(driver).\
        login_with_alert(link='issue_section', username=creds.username, password=creds.password).\
        verify()
