from test_automation.page_objects.login_page import LoginPage


def test_login_to_timesheets(driver, creds):
    LoginPage(driver).\
        login(username=creds.username, password=creds.password).\
        go_to_timesheets().\
        verify()


def test_login_to_timesheets2(driver, creds):
    LoginPage(driver).\
        login_at(link=1, username=creds.username, password=creds.password)
