*** Settings ***
Resource         0_resource.robot
Suite Setup      Suite Setup Steps
Suite Teardown   Close Browser

*** Keywords ***
Suite Setup Steps
    Open And Configure Browser
    Reset Citations

*** Variables ***
${BOOK-BIBTEX}  '@book{123, id = ".*", key = "123", title = "scientific study", year = 1975, pages = "110", volume = "1", publisher = "Otava", tags = "science, book", citation_url = "www.example.com", timestamp = ".*" }'

*** Test Cases ***
Page Loads
    Go To  ${HOME_URL}
    Title Should Be  Reference app

Entering Valid Information The **BOOK** Citation Is Accepted
    Go To  ${HOME_URL}
    Click Button  reference
    Select From List By Value  type  book
    Input Text  title_book  scientific study
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

*** Test Cases ***
BibTeX-code is generated correctly
    Go To  ${HOME_URL}
    Click Button  select_all
    Click Button  generate
    Wait Until Element Is Visible  xpath=//textarea[@id='bibtexTextarea']
    ${generated_bibtex}=  Get Text  xpath=//textarea[@id='bibtexTextarea']
    Should Match Regexp  ${generated_bibtex}  @book{123,\\s*id\\s*= "[^"]*",\\s*key\\s*= "123",\\s*title\\s*= "scientific study",\\s*year\\s*= 1975,\\s*pages\\s*= "110",\\s*volume\\s*= "1",\\s*publisher\\s*= "Otava",\\s*tags\\s*= "science,\\s*book",\\s*citation_url\\s*= "www.example.com",\\s*timestamp\\s*= "[^"]*",\\s*}
