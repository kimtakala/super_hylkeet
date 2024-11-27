*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Test Cases ***
Page Loads
    Go To  ${HOME_URL}
    Title Should Be  Reference app


Entering Valid Information The **BOOK** Citation Is Accepted
    Go To  ${HOME_URL}
    Click Button  reference
    Select From List By Value  type  book
    Input Text  title  scientific study
    Input Text  key  123
    Input Text  authors  Hylje Maisteri
    Input Text  publisher  Otava
    Input Text  year  1975
    Input Text  volume  1
    Input Text  pages  110
    Input Text  series  Science Series
    Input Text  address  Helsinki
    Input Text  edition  2nd
    Input Text  month  January
    Input Text  note  Important Study
    Input Text  tags  science, book
    Input Text  citation_url  www.example.com
    Textfield Value Should Be  id=tags  science, book
    Click Button  submit
    Title Should Be  Reference app
    ${value}=  Get Value  id=tags
    Should Be Empty  ${value}


# Entering Valid Information The **INPROCEEDINGS** Citation Is Accepted
#     Go To  ${HOME_URL}
#     Click Button  reference
#     Select From List By Value  type  inproceedings
#     Input Text  title  conference paper
#     Input Text  booktitle  proceedings of the seal conference
#     Input Text  key  789
#     Input Text  authors  Seal Researcher
#     Input Text  year  2021
#     Input Text  editor  Dr. Editor
#     Input Text  volume/number  10
#     Input Text  series  Conference Series
#     Input Text  pages  50-60
#     Input Text  address  Turku
#     Input Text  month  June
#     Input Text  organization  Seal Organization
#     Input Text  publisher  Academic Press
#     Input Text  note  Noteworthy Paper
#     Input Text  tags  conference, inproceedings
#     Input Text  url  www.conference-example.com
#     Textfield Value Should Be  id=tags  conference, inproceedings
#     Click Button  submit
#     Title Should Be  Reference app
#     ${value}=  Get Value  id=tags
#     Should Be Empty  ${value}


# Entering Valid Information The **ARTICLE** Citation Is Accepted
#     Go To  ${HOME_URL}
#     Click Button  reference
#     Select From List By Value  type  article
#     Input Text  title  groundbreaking research
#     Input Text  key  456
#     Input Text  authors  Dr. Seal Expert
#     Input Text  year  2020
#     Input Text  journal  Science Journal
#     Input Text  volume  5
#     Input Text  pages  200-210
#     Input Text  month  March
#     Input Text  doi  10.1234/example.doi
#     Input Text  note  Significant Findings
#     Input Text  tags  research, article
#     Input Text  citation_url  www.research-example.com
#     Textfield Value Should Be  id=tags  research, article
#     Click Button  submit
#     Title Should Be  Reference app
#     ${value}=  Get Value  id=tags
#     Should Be Empty  ${value}


# Entering Valid Information The Citation Is Shown On Page
#     Go To  ${HOME_URL}
#     Click Button  reference
#     Select From List By Value  type  article
#     Input Text  title  very scientific study
#     Input Text  key  vip123
#     Input Text  authors  Hylkeet et. al. et. co.
#     Input Text  year  2001
#     Input Text  doi  www.da_doih.fi/123/666
#     Input Text  pages  124
#     Input Text  volume  12.
#     Input Text  publisher  Nature
#     Click Button  submit
#     Title Should Be  Reference app
#     Page Should Contain  very scientific study
#     ${value}=  Get Value  tags
#     Should Be Empty  ${value}


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
