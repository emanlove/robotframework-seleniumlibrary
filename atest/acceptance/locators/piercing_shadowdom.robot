*** Settings ***
Documentation     Tests different supported xpath strategies
Test Setup        Go To Page "shadow_dom.html"
Resource          ../resource.robot

*** Test Cases ***
Multiple Locators with double arrows as separator should work
    [Setup]    Go To Page "links.html"
    Page Should Contain Element    css:div#div_id >> xpath:a[6] >> id:image1_id
