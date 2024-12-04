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

Deleting **BOOK** Citation Works
    Go To  ${HOME_URL}
    Element Should Be Visible  xpath=//label[contains(text(), 'H. Maisteri: scientific study, 1975')]
    Click Button  xpath=//h4[label[contains(text(),'H. Maisteri: scientific study, 1975')]]//button[@class='delete-btn']
    Wait Until Page Does Not Contain Element  xpath=//h4[label[contains(text(), 'H. Maisteri: scientific study, 1975')]]  timeout=10s
    Log  Element should not be visible now
    Element Should Not Be Visible  xpath=//h4[label[contains(text(), 'H. Maisteri: scientific study, 1975')]]
