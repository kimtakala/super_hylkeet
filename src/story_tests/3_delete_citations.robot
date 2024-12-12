# This is a test file that tests the deleting functionality for each of the citation types

*** Settings ***
Resource         0_resource.robot
Suite Setup      Suite Setup Steps
Suite Teardown   Close Browser
Test Setup       Reset And Initialize With One Of Each Citation Type

*** Keywords ***
Suite Setup Steps
    Open And Configure Browser


*** Test Cases ***
Page Loads
    Go To  ${HOME_URL}
    Title Should Be  Reference app

Deleting **INPROCEEDINGS** Citation Works
    Go To  ${HOME_URL}
    Element Should Be Visible  xpath=//label[contains(text(), 'S. Researcher: conference paper, 2021')]
    Click Button  xpath=//h4[label[contains(text(), 'S. Researcher: conference paper, 2021')]]//button[@class='delete-btn']
    Wait Until Page Does Not Contain Element    xpath=//h4[label[contains(text(), 'S. Researcher: conference paper, 2021')]]    timeout=10s
    Element Should Not Be Visible  xpath=//label[contains(text(), 'S. Researcher: conference paper, 2021')]

Deleting **MISC** Citation Works
    Go To  ${HOME_URL}
    Element Should Be Visible  xpath=//label[contains(text(), 'M. Author: misc research, 2021')]
    Click Button  xpath=//h4[label[contains(text(), 'M. Author: misc research, 2021')]]//button[@class='delete-btn']
    Wait Until Page Does Not Contain Element    xpath=//h4[label[contains(text(), 'M. Author: misc research, 2021')]]    timeout=10s
    Element Should Not Be Visible  xpath=//label[contains(text(), 'M. Author: misc research, 2021')]

Deleting **BOOK** Citation Works
    Go To  ${HOME_URL}
    Element Should Be Visible  xpath=//label[contains(text(), 'H. Maisteri: scientific study, 1975')]
    Click Button  xpath=//h4[label[contains(text(),'H. Maisteri: scientific study, 1975')]]//button[@class='delete-btn']
    Wait Until Page Does Not Contain Element  xpath=//h4[label[contains(text(), 'H. Maisteri: scientific study, 1975')]]  timeout=10s
    Log  Element should not be visible now
    Element Should Not Be Visible  xpath=//h4[label[contains(text(), 'H. Maisteri: scientific study, 1975')]]

Deleting **ARTICLE** Citation Works
    Go To  ${HOME_URL}
    Element Should Be Visible  xpath=//label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]
    Click Button  xpath=//h4[label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]]//button[@class='delete-btn']
    Wait Until Page Does Not Contain Element    xpath=//h4[label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]]    timeout=10s
    Element Should Not Be Visible  xpath=//label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]




