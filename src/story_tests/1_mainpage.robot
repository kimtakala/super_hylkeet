*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Test Cases ***
Page Loads
    Go To  ${HOME_URL}
    Title Should Be  Reference app

Entering Valid Information The Citation Is Accepted
    Go To  ${HOME_URL}
    Input Text  title  scientific study
    Input Text  key  123
    Input Text  authors  Hylkeet et. al.
    Input Text  year  1234
    Select From List By Value  type  article
    Input Text  doi  www.da_doih.fi/123/
    Input Text  pages  123
    Input Text  volume  13.
    Input Text  publisher  Nature
    Input Text  tags  animals, wild
    Textfield Value Should Be  tags  animals, wild
    Click Button  submit
    Title Should Be  Reference app
    ${value}=  Get Value  tags
    Should Be Empty  ${value}

Entering Valid Information The Citation Is Shown On Page
    Go To  ${HOME_URL}
    Input Text  title  very scientific study
    Input Text  key  vip123
    Input Text  authors  Hylkeet et. al. et. co.
    Input Text  year  2001
    Select From List By Value  type  article
    Input Text  doi  www.da_doih.fi/123/666
    Input Text  pages  124
    Input Text  volume  12.
    Input Text  publisher  Nature
    Click Button  submit
    Title Should Be  Reference app
    Page Should Contain  very scientific study
    ${value}=  Get Value  tags
    Should Be Empty  ${value}


# After adding two todos and marking one done, there is one unfinished
#     Go To  ${HOME_URL}
#     Click Link  Create new todo
#     Input Text  content  Buy milk
#     Click Button  Create
#     Click Link  Create new todo
#     Input Text  content  Clean house
#     Click Button  Create
#     Click Button  //li[div[contains(text(), 'Buy milk')]]/form/button
#     Page Should Contain  things still unfinished: 1
#     Page Should Contain  Buy milk, done
