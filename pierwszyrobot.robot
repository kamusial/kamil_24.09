*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***
Log In Wikipedia
    [Arguments]      ${login}      ${password}
    Open Browser      https://pl.wikipedia.org    chrome
    Maximize Browser Window
    Run Keyword And Ignore Error    Click Element    id:nieistniejace
    Wait Until Element Is Visible    id:pt-login-2    5
    Click Element    id:pt-login-2
    Input Text    id:wpName1    ${login}
    Input Password    id:wpPassword1    ${password}
    Click Button    id:wpLoginAttempt
    sleep    5
*** Test Cases ***
Successful login
    Log In Wikipedia      RobotTests      RobotFramework
    input text    name:search   Teoria Wielkiego Podrywu
    click button    xpath=/html/body/div[1]/header/div[2]/div/div/div/form/div/button
