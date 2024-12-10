*** Settings ***
Resource         0_resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Application And Go To Home Page

*** Test Cases ***
Entering Citation Using Doi
    Go To  ${HOME_URL}
    Click Button  reference
    Select From List By Value  type  doi
    Input Text  doi  10.1007/978-3-319-46547-0_16
    Input Text  key  And16
    Input Text  tags data
    Click Button  submit_doi
    Page Should Contain Text  A. Nuzzolese: Conference Linked Data: The ScholarlyData Project, 2016