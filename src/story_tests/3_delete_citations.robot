# This is a test file that test the delete functionality for each of the citation types

*** Settings ***
Resource         0_resource.robot
Suite Setup      Suite Setup Steps
Suite Teardown   Close Browser

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

Deleting **ARTICLE** Citation Works
    Go To  ${HOME_URL}
    Element Should Be Visible  xpath=//label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]
    Click Button  xpath=//h4[label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]]//button[@class='delete-btn']
    Wait Until Page Does Not Contain Element    xpath=//h4[label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]]    timeout=10s
    Element Should Not Be Visible  xpath=//label[contains(text(), 'D. Seal Expert: groundbreaking research, 2020')]




