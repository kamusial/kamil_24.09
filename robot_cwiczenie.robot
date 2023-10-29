*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${name}    Kamil@costa.pl
${password}     pass233

*** Keywords ***
Open My Browser
    Open Browser    https://gotujmy.pl/forum/    Chrome
    Maximize Browser Window
    Sleep    3
    Run Keyword And Ignore Error     Scroll Element Into View    //*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]
    Run Keyword And Ignore Error    click button    //*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]
    Run Keyword And Ignore Error    click button    xpath=//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]
*** Test Cases ***
Registration
    Open My Browser
    sleep   1
    Click Element    xpath=//*[@id="navTop"]/nav/ul[1]/li[2]/a
    sleep   1
    Run Keyword And Ignore Error    click button    xpath=//*[@id="tcf277-permissions-modal"]/div[3]/div/button[2]
    sleep   1
    input text    //*[@id="f_cmu_email"]    ${name}
    input text    //*[@id="f_cmu_email2"]    ${name}
    input text    //*[@id="f_cmu_password"]     ${password}
    input text    //*[@id="f_cmu_password2"]    ${password}
    Checkbox Should Not Be Selected  //*[@id="newsletter_agree"]
    select checkbox  //*[@id="newsletter_agree"]
    Checkbox Should Not Be Selected  //*[@id="user_register_form"]/fieldset/label[2]/input
    select checkbox  //*[@id="user_register_form"]/fieldset/label[2]/input
    Checkbox Should Not Be Selected  //*[@id="user_register_form"]/fieldset/label[3]/input
    select checkbox  //*[@id="user_register_form"]/fieldset/label[3]/input
    sleep    3
    Click Button    //*[@id="user_register_form"]/fieldset/footer/button
    sleep    3
