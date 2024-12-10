# This is a test file that tests the sorting functionality for each of the sorting types in both ascending and descending order

*** Settings ***
Resource         0_resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset And Initialize With One Of Each Citation Type


*** Test Cases ***
Sorting Citations By Year In Ascending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  year
    Select From List By Value  sorting_order  ASC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${years}=  Get Citation Years  ${citations}
    Should Be Sorted  ${years}  ascending

Sorting Citations By Author In Ascending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  author
    Select From List By Value  sorting_order  ASC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${authors}=  Get Citation Authors  ${citations}
    Should Be Sorted  ${authors}  ascending

Sorting Citations By Time Added In Ascending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  time_added
    Select From List By Value  sorting_order  ASC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${times}=  Get Citation Times  ${citations}
    Should Be Sorted  ${times}  ascending

Sorting Citations By Title In Ascending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  title
    Select From List By Value  sorting_order  ASC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${titles}=  Get Citation Titles  ${citations}
    Should Be Sorted  ${titles}  ascending

Sorting Citations By Year In Descending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  year
    Select From List By Value  sorting_order  DESC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${years}=  Get Citation Years  ${citations}
    Should Be Sorted  ${years}  descending

Sorting Citations By Author In Descending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  author
    Select From List By Value  sorting_order  DESC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${authors}=  Get Citation Authors  ${citations}
    Should Be Sorted  ${authors}  descending

Sorting Citations By Time Added In Descending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  time_added
    Select From List By Value  sorting_order  DESC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${times}=  Get Citation Times  ${citations}
    Should Be Sorted  ${times}  descending

Sorting Citations By Title In Descending Order
    Go To  ${HOME_URL}
    Select From List By Value  sorting_key  title
    Select From List By Value  sorting_order  DESC
    Click Button  submit
    Title Should Be  Reference app
    ${citations}=  Get WebElements  xpath=//div[@class='citation']
    ${titles}=  Get Citation Titles  ${citations}
    Should Be Sorted  ${titles}  descending

*** Keywords ***
Get Citation Years
    [Arguments]  ${citations}
    ${years}=  Create List
    FOR  ${citation}  IN  @{citations}
        ${year}=  Get Text  ${citation}  xpath=.//div[@class='year']
        Append To List  ${years}  ${year}
    END
    RETURN  ${years}

Get Citation Authors
    [Arguments]  ${citations}
    ${authors}=  Create List
    FOR  ${citation}  IN  @{citations}
        ${author}=  Get Text  ${citation}  xpath=.//div[@class='author']
        Append To List  ${authors}  ${author}
    END
    RETURN  ${authors}

Get Citation Times
    [Arguments]  ${citations}
    ${times}=  Create List
    FOR  ${citation}  IN  @{citations}
        ${time}=  Get Text  ${citation}  xpath=.//div[@class='time_added']
        Append To List  ${times}  ${time}
    END
    RETURN  ${times}

Get Citation Titles
    [Arguments]  ${citations}
    ${titles}=  Create List
    FOR  ${citation}  IN  @{citations}
        ${title}=  Get Text  ${citation}  xpath=.//div[@class='title']
        Append To List  ${titles}  ${title}
    END
    RETURN  ${titles}


Should Be Sorted
    [Arguments]  ${list}  ${order}
    ${sorted_list}=  Copy List  ${list}
    Run Keyword If  '${order}' == 'ascending'  Sort List  ${sorted_list}
    Run Keyword If  '${order}' == 'descending'  Run Keywords  Sort List  ${sorted_list}  AND  Reverse List  ${sorted_list}
    Should Be Equal  ${list}  ${sorted_list}
