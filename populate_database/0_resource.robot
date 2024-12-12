# This is a resource file for the tests that defines the main keywords to be used in the tests

*** Settings ***
Library  SeleniumLibrary
Library  Collections


*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.05 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   true

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Citations
    Go To  ${RESET_URL}

Load Main Page
    Go To  ${HOME_URL}
    Title Should Be  Reference app

Reset Application And Go To Home Page
    Reset Citations
    Go To  ${HOME_URL}

Enter Book Citation 1
    Click Button  reference
    Select From List By Value  type  book
    Input Text  title_book  Seal Biology and Ecology
    Input Text  key_book  SBE2020
    Input Text  authors_book  Dr. Seal Expert, Dr. Marine Biologist
    Input Text  publisher_book  Oceanic Press
    Input Text  year_book  2020
    Input Text  volume_book  2
    Input Text  pages_book  302
    Input Text  series_book  Marine Life Series
    Input Text  address_book  New York
    Input Text  edition_book  3
    Input Text  month_book  February
    Input Text  note_book  Comprehensive Guide
    Input Text  tags_book  seal biology, marine ecology
    Input Text  citation_url_book  www.oceanicpress.com/seal-biology
    Textfield Value Should Be  id=tags_book  seal biology, marine ecology
    Click Button  submit_book

Enter Book Citation 2
    Click Button  reference
    Select From List By Value  type  book
    Input Text  title_book  The Science of Seals
    Input Text  key_book  SS2021
    Input Text  authors_book  Dr. Marine Biologist
    Input Text  publisher_book  Marine Press
    Input Text  year_book  2021
    Input Text  volume_book  1
    Input Text  pages_book  350
    Input Text  series_book  Marine Biology Series
    Input Text  address_book  San Francisco
    Input Text  edition_book  1
    Input Text  month_book  April
    Input Text  note_book  Comprehensive Study on Seals
    Input Text  tags_book  marine biology, seals
    Input Text  citation_url_book  www.marinepress.com/science-of-seals
    Textfield Value Should Be  id=tags_book  marine biology, seals
    Click Button  submit_book

Enter Book Citation 3
    Click Button  reference
    Select From List By Value  type  book
    Input Text  title_book  Marine Mammals: An Overview
    Input Text  key_book  MM2022
    Input Text  authors_book  Dr. Ocean Explorer
    Input Text  publisher_book  Oceanic Press
    Input Text  year_book  2022
    Input Text  volume_book  3
    Input Text  pages_book  400
    Input Text  series_book  Marine Life Series
    Input Text  address_book  Miami
    Input Text  edition_book  2
    Input Text  month_book  May
    Input Text  note_book  In-depth Analysis
    Input Text  tags_book  marine mammals, oceanography
    Input Text  citation_url_book  www.oceanicpress.com/marine-mammals
    Textfield Value Should Be  id=tags_book  marine mammals, oceanography
    Click Button  submit_book

Enter Inproceedings Citation 1
    Click Button  reference
    Select From List By Value  type  inproceedings
    Input Text  title_inproceedings  Advances in Seal Research
    Input Text  booktitle_inproceedings  Proceedings of the Marine Biology Conference
    Input Text  key_inproceedings  ASR2021
    Input Text  authors_inproceedings  Dr. Marine Biologist
    Input Text  year_inproceedings  2021
    Input Text  editor_inproceedings  Dr. Ocean Explorer
    Input Text  volume_inproceedings  15
    Input Text  series_inproceedings  Marine Biology Series
    Input Text  pages_inproceedings  120-130
    Input Text  address_inproceedings  Helsinki
    Input Text  month_inproceedings  July
    Input Text  organization_inproceedings  Marine Biology Association
    Input Text  publisher_inproceedings  Marine Press
    Input Text  note_inproceedings  Important Findings
    Input Text  tags_inproceedings  marine biology, conference
    Input Text  citation_url_inproceedings  www.marineconference.com/advances-seal-research
    Textfield Value Should Be  id=tags_inproceedings  marine biology, conference
    Click Button  submit_inproceedings

Enter Inproceedings Citation 2
    Click Button  reference
    Select From List By Value  type  inproceedings
    Input Text  title_inproceedings  Seal Behavior Studies
    Input Text  booktitle_inproceedings  Proceedings of the Arctic Wildlife Conference
    Input Text  key_inproceedings  SBS2020
    Input Text  authors_inproceedings  Dr. Arctic Researcher
    Input Text  year_inproceedings  2020
    Input Text  editor_inproceedings  Dr. Polar Scientist
    Input Text  volume_inproceedings  8
    Input Text  series_inproceedings  Arctic Wildlife Series
    Input Text  pages_inproceedings  75-85
    Input Text  address_inproceedings  Reykjavik
    Input Text  month_inproceedings  March
    Input Text  organization_inproceedings  Arctic Wildlife Institute
    Input Text  publisher_inproceedings  Polar Press
    Input Text  note_inproceedings  Behavioral Analysis
    Input Text  tags_inproceedings  arctic, wildlife, conference
    Input Text  citation_url_inproceedings  www.arcticconference.com/seal-behavior-studies
    Textfield Value Should Be  id=tags_inproceedings  arctic, wildlife, conference
    Click Button  submit_inproceedings

Enter Inproceedings Citation 3
    Click Button  reference
    Select From List By Value  type  inproceedings
    Input Text  title_inproceedings  Seal Population Dynamics
    Input Text  booktitle_inproceedings  Proceedings of the Oceanic Research Symposium
    Input Text  key_inproceedings  SPD2019
    Input Text  authors_inproceedings  Dr. Oceanic Biologist
    Input Text  year_inproceedings  2019
    Input Text  editor_inproceedings  Dr. Marine Scientist
    Input Text  volume_inproceedings  12
    Input Text  series_inproceedings  Oceanic Research Series
    Input Text  pages_inproceedings  200-210
    Input Text  address_inproceedings  Sydney
    Input Text  month_inproceedings  November
    Input Text  organization_inproceedings  Oceanic Research Institute
    Input Text  publisher_inproceedings  Oceanic Press
    Input Text  note_inproceedings  Population Study
    Input Text  tags_inproceedings  oceanography, conference
    Input Text  citation_url_inproceedings  www.oceanicsymposium.com/seal-population-dynamics
    Textfield Value Should Be  id=tags_inproceedings  oceanography, conference
    Click Button  submit_inproceedings

Enter Article Citation 1
    Click Button  reference
    Select From List By Value  type  article
    Input Text  title_article  The Impact of Climate Change on Seals
    Input Text  key_article  CC2021
    Input Text  authors_article  Dr. Climate Researcher
    Input Text  year_article  2021
    Input Text  journal_article  Environmental Science Journal
    Input Text  volume_article  12
    Input Text  pages_article  150-160
    Input Text  month_article  June
    Input Text  doi_article  10.5678/envsci.2021.12345
    Input Text  note_article  Detailed Study on Climate Effects
    Input Text  tags_article  climate change, seals
    Input Text  citation_url_article  www.envsci-journal.com/climate-change-seals
    Textfield Value Should Be  id=tags_article  climate change, seals
    Click Button  submit_article

Enter Article Citation 2
    Click Button  reference
    Select From List By Value  type  article
    Input Text  title_article  Seal Migration Patterns
    Input Text  key_article  SMP2020
    Input Text  authors_article  Dr. Marine Biologist
    Input Text  year_article  2020
    Input Text  journal_article  Marine Biology Journal
    Input Text  volume_article  8
    Input Text  pages_article  220-230
    Input Text  month_article  September
    Input Text  doi_article  10.2345/marbiol.2020.67890
    Input Text  note_article  Insights into Migration
    Input Text  tags_article  migration, seals
    Input Text  citation_url_article  www.marbiol-journal.com/seal-migration
    Textfield Value Should Be  id=tags_article  migration, seals
    Click Button  submit_article

Enter Article Citation 3
    Click Button  reference
    Select From List By Value  type  article
    Input Text  title_article  Seal Population Genetics
    Input Text  key_article  SPG2019
    Input Text  authors_article  Dr. Geneticist
    Input Text  year_article  2019
    Input Text  journal_article  Genetics Research Journal
    Input Text  volume_article  15
    Input Text  pages_article  300-310
    Input Text  month_article  December
    Input Text  doi_article  10.3456/genres.2019.54321
    Input Text  note_article  Genetic Diversity Study
    Input Text  tags_article  genetics, seals
    Input Text  citation_url_article  www.genres-journal.com/seal-genetics
    Textfield Value Should Be  id=tags_article  genetics, seals
    Click Button  submit_article
    
Enter Misc Citation 1
    Click Button  reference
    Select From List By Value  type  misc
    Input Text  title_misc  Seal Conservation Efforts
    Input Text  key_misc  SCE2020
    Input Text  authors_misc  Dr. Conservationist
    Input Text  howpublished_misc  Online Report
    Input Text  month_misc  January
    Input Text  year_misc  2020
    Input Text  note_misc  Detailed Conservation Strategies
    Input Text  tags_misc  conservation, seals
    Input Text  citation_url_misc  www.conservation.org/seal-efforts
    Textfield Value Should Be  id=tags_misc  conservation, seals
    Click Button  submit_misc
    
Enter Misc Citation 2
    Click Button  reference
    Select From List By Value  type  misc
    Input Text  title_misc  Seal Tracking Data
    Input Text  key_misc  STD2019
    Input Text  authors_misc  Dr. Marine Tracker
    Input Text  howpublished_misc  Dataset
    Input Text  month_misc  August
    Input Text  year_misc  2019
    Input Text  note_misc  GPS Tracking Information
    Input Text  tags_misc  tracking, seals, dataset
    Input Text  citation_url_misc  www.marinedata.org/seal-tracking
    Textfield Value Should Be  id=tags_misc  tracking, seals, dataset
    Click Button  submit_misc
    
Enter Misc Citation 3
    Click Button  reference
    Select From List By Value  type  misc
    Input Text  title_misc  Seal Rehabilitation Programs
    Input Text  key_misc  SRP2021
    Input Text  authors_misc  Dr. Marine Veterinarian
    Input Text  howpublished_misc  Rehabilitation Report
    Input Text  month_misc  November
    Input Text  year_misc  2021
    Input Text  note_misc  Success Stories and Data
    Input Text  tags_misc  rehabilitation, seals
    Input Text  citation_url_misc  www.rehabprograms.org/seals
    Textfield Value Should Be  id=tags_misc  rehabilitation, seals
    Click Button  submit_misc
