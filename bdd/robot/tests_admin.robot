*** Settings ***
Library           SeleniumLibrary
Library           String
Test Setup        Открыть сессию
Test Teardown     Выход из сессии


*** Variables ***
${SERVER}           192.168.50.45
${BROWSER}          Chrome
${DELAY}            0
${VALID USER}       user
${VALID PASSWORD}   bitnami1
${LOGIN ADMIN URL}  http://${SERVER}/admin
${IGNORE SERT}      "--ignore-certificate-errors"


*** Keywords ***

Открыть сессию
    Open Browser                        ${LOGIN ADMIN URL}    ${BROWSER}    options=add_argument(${IGNORE SERT})
    Maximize Browser Window
    Set Selenium Speed                  ${DELAY}

Ввести логин админа
    Input Text                          css:input[name="username"]    ${VALID USER}

Ввести пароль
    Input Text                          css:input[name="password"]    ${VALID PASSWORD}

Нажать на кнопку Login
    Click Button                        css:.btn-primary

Заголовок должен быть
    [Arguments]                         ${title}
    Title Should Be                     ${title}

Авторизация
    Ввести логин админа
    Ввести пароль
    Нажать на кнопку Login

Выход из сессии
    Click Element                       css:.nav li span
    Close Browser

Открыть каталог товаров
    ${href} =	Get Element Attribute	css:#collapse1 > li:nth-child(2) a  href
    Go To   ${href}

Найти товары на странице
    ${count} =  Get Element Count       css:tbody tr
    Should Be True  ${count}            <= 20

Выбрать элемент
    [Arguments]         ${product_number}
    Select Checkbox     css:tbody tr:nth-child(${product_number}) [type="checkbox"]

Получить Имя продукта
    [Arguments]                        ${product_number}
    ${product_name}=   Get Text   css:tbody tr:nth-child(${product_number}) td:nth-child(3)
    [Return]   ${product_name}

Скопировать элемент
    Click Button                       css:button[data-original-title="Copy"]

Проверить значения
    [Arguments]      ${first_value}  ${second_value}
    Should Be True   "${first_value}" == "${second_value}"

Удалить продукт
    Click Button     css:button[data-original-title="Delete"]

Подтвердить алерт
    Alert Should Be Present     action=ACCEPT

Нажать Редактировать продукт
    [Arguments]       ${product_number}
    ${locator}   Catenate    css:tbody tr:nth-child(${product_number})   [data-original-title="Edit"]
    Click Element      ${locator}

Редактировать Имя продукта
    [Arguments]     ${product_name}
    Input text      css:#input-name1    ${product_name}

Сохранить продукт
    Click Element   css:[data-original-title="Save"]

Текст на плашке
    ${text}    Get Text   css:.alert-success
    ${string}    Get Substring	  ${text}   0    -2
    [Return]   ${string}


*** Test Cases ***

Авторизация в админку
    Авторизация
    Заголовок должен быть    Dashboard

Количество товаров на странице
    Авторизация
    Открыть каталог товаров
    Найти товары на странице

Копирование продукта
    Авторизация
    Открыть каталог товаров
    ${first_product_name} =    Получить Имя продукта     7
    Выбрать элемент     7
    Скопировать элемент
    ${second_product_name} =    Получить Имя продукта     8
    Проверить значения   ${first_product_name}  ${second_product_name}

Удаление продукта
    Авторизация
    Открыть каталог товаров
    Выбрать элемент        1
    Скопировать элемент
    Выбрать элемент        2
    Удалить продукт
    Подтвердить алерт

Редактирование продукта
    Авторизация
    Открыть каталог товаров
    Нажать Редактировать продукт                   7
    Редактировать Имя продукта               Тест:Новое имя продукта
    Сохранить продукт
    ${text}    Текст на плашке
    Проверить значения    Success: You have modified products!    ${text}




