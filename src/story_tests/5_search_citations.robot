# This is a test file that tests the search functionality

*** Settings ***
Resource         0_resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset And Initialize With One Of Each Citation Type


*** Test Cases ***
# Search Citations By *empty*
#     Go To  ${HOME_URL}
#     Click Button  search
#     Title Should Be  Reference app
#     ${citations}=  Get WebElements  xpath=.//div[@class='citation']
#     Length Should Be  ${citations}  4

#! alla olevat ovat place holdereita

# Search Citations By "hylje"
#     ${search_phrase}=  Set Variable  hylje
#     Go To  ${HOME_URL}
#     Input Text  search  ${search_phrase}
#     Click Button  submit
#     Title Should Be  Reference app
#     ${citations}=  Get WebElements  xpath=//div[@class='citation']
#     All Elements Should Contain Search Phrase  ${citations}  ${search_phrase}
#     Length Should Be  ${citations}  1

# Sorting Citations By Author In Ascending Order
#     Go To  ${HOME_URL}
#     Select From List By Value  sorting_key  author
#     Select From List By Value  sorting_order  ASC
#     Click Button  submit
#     Title Should Be  Reference app
#     ${citations}=  Get WebElements  xpath=//div[@class='citation']
#     ${authors}=  Get Citation Authors  ${citations}
#     Should Be Sorted  ${authors}  ascending


*** Keywords ***
#! Placeholder

# Get Citation Years
#     [Arguments]  ${citations}
#     ${years}=  Create List
#     FOR  ${citation}  IN  @{citations}
#         ${year}=  Get Text  ${citation}  xpath=.//div[@class='year']
#         Append To List  ${years}  ${year}
#     END
#     RETURN  ${years}

All Elements Should Contain Search Phrase
    [Arguments]  ${list}  ${search_phrase}
    FOR  ${item}  IN  ${list}
        Should Contain  ${item}  ${search_phrase}
    END
