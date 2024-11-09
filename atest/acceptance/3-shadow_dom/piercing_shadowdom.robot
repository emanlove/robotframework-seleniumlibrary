*** Settings ***
Documentation     Tests different supported xpath strategies
Library           SeleniumLibrary    shadowdom_piercing=True
Resource          resource_shadowdom.robot
Suite Setup       Open Browser    ${FRONT_PAGE}    ${BROWSER}    alias=shadowdom
...                   remote_url=${REMOTE_URL}
Suite Teardown    Close All Browsers
Test Setup        Go To Page "shadow_dom.html"

*** Test Cases ***
Multiple Locators with double arrows as separator should work
    [Setup]    Go To Page "links.html"
    Page Should Contain Element    css:div#div_id >> xpath:a[6] >> id:image1_id
