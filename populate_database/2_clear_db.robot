# This is a script to clear the database

*** Settings ***
Resource         0_resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Load Main Page

*** Test Cases ***

CLEAR ALL
    Reset Citations
