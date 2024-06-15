FINAL_PROJECT_SPRINT_5_VALERIA_MALETS_TEAM_9:
UI Test for site: https://stellarburgers.nomoreparties.site/

FOLDER PAGES CONTAINS:
1. FILE stellar_burgers_page : XPATH for elements

FOLDER test contains files with test for site functionality:

1. conftest.py - all project fixtures
2. constructor_section_test.py: 3 tests for testing functionality constructor
3. go_to_my_account_test.py: 1 test for proceeding to user's account
4. login_test.py: 4 tests: 

    4.1 TEST: success login via "Личный кабинет" button from main site page
    4.2 TEST: success login via "Войти в аккаунт" button
    4.3 TEST: success login  from registration page
    4.4 TEST: success login  from reset password page
5. logout_test.py: 1 test 
6. registration_test.py: 2 tests: success registration test, invalid password test
7. transition_to_constructor_test.py: 1 test for testing the proceeding to constructor from account page.
Changes after comments:
8. config.py file is added : WebLink saved
9. registration_test.py : Added functions to generate random email address and invalid password.
10. All the time.sleep was changed to waiting with the expected conditions
11. Added classes
12. construction_section_test.py: Asserts and element's Xpath are updated

UPDATES 15.06:
1. data.py file added
2. helpers.py  file added
3. consrtuctor_section_test.py: asserts were edited, XPaths to the element have been changed
