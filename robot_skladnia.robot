*** Variables ***
${string}   piesek
@{list}     pierszy     drugi    trzeci     czwarty     piąty
@{list_of_numbers}      1   2   3   4   5
&{dictionary}   slowo=${string}     numer=30    lista=@{list}
@{imiona}   Kamil   Marta   Auugusto    Marek
@{nazwiska}    Kowalski     Malinowski  Nowak   nijaki

*** Test Cases ***
For Loop In Range 10
    FOR    ${i}     IN RANGE    10
        Log     ${i}
        Log to console    ${i}
    END

For Loop In Rage 4 10
    FOR    ${i}     IN RANGE    4    10
        Log     ${i}
        Log to console    ${i}
    END

For Loop In Rage 4 20 With Step 3
    FOR    ${i}     IN RANGE    4    20    3
        Log     ${i}
        Log to console    ${i}
    END

For Loop In List
    FOR    ${item}    IN    @{list_of_numbers}
        IF    ${item}==3    Log     ${item}
    END

For Loop In Dictionary
    Log    ${dictionary}
    FOR   ${keys_and_values}    IN    &{dictionary}
        Log     ${keys_and_values}
    END