*** Settings ***
Resource         0_resource.robot
Suite Setup      Suite Setup Steps
Suite Teardown   Close Browser

*** Keywords ***
Suite Setup Steps
    Open And Configure Browser

*** Variables ***
${BOOK-BIBTEX}  @book{123,\\s*id\\s*= "[^"]*",\\s*key\\s*= "123",\\s*title\\s*= "scientific study",\\s*year\\s*= 1975,\\s*pages\\s*= "110",\\s*volume\\s*= "1",\\s*publisher\\s*= "Otava",\\s*tags\\s*= "science,\\s*book",\\s*citation_url\\s*= "www.example.com",\\s*timestamp\\s*= "[^"]*",\\s*}

*** Test Cases ***
Page Loads
    Go To  ${HOME_URL}
    Title Should Be  Reference app

BibTeX-code is generated correctly
    Go To  ${HOME_URL}
    Click Button  select_all
    Click Button  generate
    Wait Until Element Is Visible  xpath=//textarea[@id='bibtexTextarea']
    ${generated_bibtex}=  Get Text  xpath=//textarea[@id='bibtexTextarea']
    Should Match Regexp  ${generated_bibtex}  ${BOOK-BIBTEX}