# This is a test file that tests the search functionality

*** Settings ***
Resource         0_resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset And Initialize With One Of Each Citation Type


*** Variables ***
${search_phrase}  scientific

*** Test Cases ***
Search Citations By Research Phrase
    Go To  ${HOME_URL}
    Input Text  search  ${search_phrase}
    Click Button  search_button
    Title Should Be  Reference app
    Wait Until Element Is Visible  xpath=//h4[@class='title']  timeout=10s
    ${citations}=  Get WebElements  xpath=//h4[@class='title']
    ${titles}=  Get Citation Titles  ${citations}
    Length Should Be  ${titles}  1
    Sleep  5s

*** Keywords ***
Get Citation Titles
    [Arguments]  ${citations}
    ${titles}=  Create List
    FOR  ${citation}  IN  @{citations}
        ${title}=  Get Text  ${citation}
        Append To List  ${titles}  ${title}
    END
    RETURN  ${titles}