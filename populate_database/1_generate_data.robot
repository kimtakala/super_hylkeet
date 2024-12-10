# This is a script to populate the database

*** Settings ***
Resource         0_resource.robot
Suite Setup      Run Keywords  Open And Configure Browser  Reset Application And Go To Home Page
Suite Teardown   Close Browser
Test Setup       Load Main Page



*** Test Cases ***
Enter Data Into Database
    Go To  ${HOME_URL}
    Enter Book Citation 1
    Enter Book Citation 2
    Enter Book Citation 3
    Enter Article Citation 1
    Enter Article Citation 2
    Enter Article Citation 3
    Enter Inproceedings Citation 1
    Enter Inproceedings Citation 2
    Enter Inproceedings Citation 3
    Enter Misc Citation 1
    Enter Misc Citation 2
    Enter Misc Citation 3
