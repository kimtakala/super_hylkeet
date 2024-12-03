# This is a test file that submits citations to the reference app and test the delete functionality for each of the citation types

*** Settings ***
Resource  resource.robot
Suite Setup      Suite Setup Steps
Suite Teardown   Close Browser

*** Keywords ***
Suite Setup Steps
    Open And Configure Browser
    Reset Citations

*** Test Cases ***
Page Loads
    Go To  ${HOME_URL}
    Title Should Be  Reference app


Entering Valid Information The **BOOK** Citation Is Accepted
    Go To  ${HOME_URL}
    Click Button  reference
    Select From List By Value  type  book
    Input Text  title_book  scientific study!
    Input Text  key_book  123
    Input Text  authors_book  Hylje Maisteri
    Input Text  publisher_book  Otava
    Input Text  year_book  1975
    Input Text  volume_book  1
    Input Text  pages_book  110
    Input Text  series_book  Science Series
    Input Text  address_book  Helsinki
    Input Text  edition_book  2nd
    Input Text  month_book  January
    Input Text  note_book  Important Study
    Input Text  tags_book  science, book
    Input Text  citation_url_book  www.example.com
    Textfield Value Should Be  id=tags_book  science, book
    Click Button  submit_book
    Title Should Be  Reference app
    ${value}=  Get Value  id=tags_book
    Should Be Empty  ${value}


Deleting **BOOK** Citation Works
    # Navigate to the home page
    Go To  ${HOME_URL}

    # Verify the BOOK citation exists
    Element Should Be Visible  xpath=//label[contains(text(), 'H. Maisteri: scientific study!, 1975')]

    # Click the delete button for the BOOK citation
    Click Button  xpath=//h4[label[contains(text(), 'H. Maisteri: scientific study!, 1975')]]//button[@class='delete-btn']

    # Verify the BOOK citation is no longer present
    Element Should Not Be Visible  xpath=//label[contains(text(), 'H. Maisteri: scientific study!, 1975')]

Entering Valid Information The **INPROCEEDINGS** Citation Is Accepted
    Go To  ${HOME_URL}
    Click Button  reference
    Select From List By Value  type  inproceedings
    Input Text  title_inproceedings  conference paper!
    Input Text  booktitle_inproceedings  proceedings of the seal conference
    Input Text  key_inproceedings  789
    Input Text  authors_inproceedings  Seal Researcher
    Input Text  year_inproceedings  2021    
    Input Text  editor_inproceedings  Dr. Editor
    Input Text  volume_inproceedings  10
    Input Text  series_inproceedings  Conference Series
    Input Text  pages_inproceedings  50-60
    Input Text  address_inproceedings  Turku
    Input Text  month_inproceedings  June
    Input Text  organization_inproceedings  Seal Organization
    Input Text  publisher_inproceedings  Academic Press
    Input Text  note_inproceedings  Noteworthy Paper
    Input Text  tags_inproceedings  conference, inproceedings
    Input Text  citation_url_inproceedings  www.conference-example.com
    Textfield Value Should Be  id=tags_inproceedings  conference, inproceedings
    Click Button  submit_inproceedings
    Title Should Be  Reference app
    ${value}=  Get Value  id=tags_inproceedings
    Should Be Empty  ${value}

Deleting **INPROCEEDINGS** Citation Works
    # Navigate to the home page
    Go To  ${HOME_URL}

    # Verify the INPROCEEDINGS citation exists
    Element Should Be Visible  xpath=//label[contains(text(), 'S. Researcher: conference paper!, 2021')]

    # Click the delete button for the INPROCEEDINGS citation
    Click Button  xpath=//h4[label[contains(text(), 'S. Researcher: conference paper!, 2021')]]//button[@class='delete-btn']

    # Verify the INPROCEEDINGS citation is no longer present
    Element Should Not Be Visible  xpath=//label[contains(text(), 'S. Researcher: conference paper!, 2021')]

Entering Valid Information The **ARTICLE** Citation Is Accepted
    Go To  ${HOME_URL}
    Click Button  reference
    Select From List By Value  type  article
    Input Text  title_article  groundbreaking research!
    Input Text  key_article  456
    Input Text  authors_article  Dr. Seal Expert
    Input Text  year_article  2020
    Input Text  journal_article  Science Journal
    Input Text  volume_article  5
    Input Text  pages_article  200-210
    Input Text  month_article  March
    Input Text  doi_article  10.1234/example.doi
    Input Text  note_article  Significant Findings
    Input Text  tags_article  research, article
    Input Text  citation_url_article  www.research-example.com
    Textfield Value Should Be  id=tags_article  research, article
    Click Button  submit_article
    Title Should Be  Reference app
    ${value}=  Get Value  id=tags_article
    Should Be Empty  ${value}

Deleting **ARTICLE** Citation Works
    # Navigate to the home page
    Go To  ${HOME_URL}

    # Verify the ARTICLE citation exists
    Element Should Be Visible  xpath=//label[contains(text(), 'D. Seal Expert: groundbreaking research!, 2020')]

    # Click the delete button for the ARTICLE citation
    Click Button  xpath=//h4[label[contains(text(), 'D. Seal Expert: groundbreaking research!, 2020')]]//button[@class='delete-btn']

    # Verify the ARTICLE citation is no longer present
    Element Should Not Be Visible  xpath=//label[contains(text(), 'D. Seal Expert: groundbreaking research!, 2020')]

Entering Valid Information The **MISC** Citation Is Accepted
    Go To  ${HOME_URL}
    Click Button  reference
    Select From List By Value  type  misc
    Input Text  title_misc  misc research!
    Input Text  key_misc  1111
    Input Text  authors_misc  Misc Author
    Input Text  howpublished_misc  published
    Input Text  month_misc  March
    Input Text  year_misc  2021
    Input Text  note_misc  Significant Findings
    Input Text  tags_misc  research, article
    Input Text  citation_url_misc  www.research-example.com
    Textfield Value Should Be  id=tags_misc  research, article
    Click Button  submit_misc
    Title Should Be  Reference app
    ${value}=  Get Value  id=tags_misc
    Should Be Empty  ${value}

Deleting **MISC** Citation Works
    # Navigate to the home page
    Go To  ${HOME_URL}

    # Verify the MISC citation exists
    Element Should Be Visible  xpath=//label[contains(text(), 'M. Author: misc research!, 2021')]

    # Click the delete button for the MISC citation
    Click Button  xpath=//h4[label[contains(text(), 'M. Author: misc research!, 2021')]]//button[@class='delete-btn']

    # Verify the MISC citation is no longer present
    Element Should Not Be Visible  xpath=//label[contains(text(), 'M. Author: misc research!, 2021')]
