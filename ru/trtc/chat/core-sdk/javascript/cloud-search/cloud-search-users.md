# Поиск облачных пользователей

## Описание функции

Поиск облачных пользователей с поддержкой быстрого поиска по ключевым словам. Пользователи могут быстро найти известных пользователей, таких как друзья или отслеживаемые контакты, с помощью этого API; одновременно они также могут использовать ключевые слова для поиска новых пользователей, расширения социального круга или поиска интересующих их пользователей.

> **Примечания:** Функция трансляции сообщений доступна только для клиентов Pro Plus и Enterprise. Её можно использовать после [приобретения Pro Plus и Enterprise](https://trtc.io/buy/chat); версия Free Trial поддерживает [определённый лимит бесплатной пробной версии](https://www.tencentcloud.com/document/product/1047/67651#d1113f0d-47e8-4211-82c0-00d2efb72586), действительный в течение одного месяца. Функция облачного поиска пользователей поддерживается начиная с **v3.5.0**. Область поиска: нечёткий поиск по никнеймам всех пользователей на основе ключевых слов, точный поиск по userID всех пользователей. Профиль в списке полученных пользователей является неполным (включает только аватар, никнейм, userID, пол, дату рождения, selfSignature и т. д., что достаточно для отображения списка результатов поиска пользователей, исключая пользовательские поля). Для запроса подробного профиля пользователя см.: [getUserProfile](https://www.tencentcloud.com/document/product/1047/48161#querying-the-profile-of-another-user). Максимальное количество результатов поиска за один раз составляет 100. Этот API имеет лимит облачной частоты 2 раза/секунду и лимит локального вызова API 20 раз/5 секунд.

## Поиск облачных пользователей

##### API

```
chat.searchCloudUsers(options);
```

##### Параметры

Параметр options имеет тип Object и содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| keywordList | Array | `обязательно` Список ключевых слов, поддержка до 5 ключевых слов. |
| keywordListMatchType | String \| undefined | Тип сопоставления списка ключевых слов: or: поиск с отношением "или" (по умолчанию) and: поиск с отношением "и" |
| gender | String \| undefined | Пол пользователя, если не указан, по умолчанию поиск по всем полам. Представление пола: `TencentCloudChat.TYPES.GENDER_FEMALE` Женщина `TencentCloudChat.TYPES.GENDER_MALE` Мужчина |
| miniBirthday | Number \| undefined | Минимальная дата рождения пользователя, например 19900101. |
| maxBirthday | Number \| undefined | Максимальная дата рождения пользователя, при установке вместе с `miniBirthday` должна быть больше или равна `miniBirthday`, например 20240101. |
| cursor | String \| undefined | Начальная позиция для каждого поиска облачных пользователей. Не передавайте `cursor` при первом поиске. Для продолжения поиска укажите значение `cursor`, возвращённое последним вызовом API `searchCloudUsers`. |
| count | Number \| undefined | Количество результатов поиска облачных пользователей за один поиск. Значение по умолчанию — 20, максимальное значение — 100. |

##### **Возвращаемое значение**

`Promise`

| Название | Тип | Описание |
| --- | --- | --- |
| totalCount | Number | Общее количество пользователей, соответствующих условию поиска. |
| searchResultList | Array | Список профилей пользователей `Profile`, соответствующих условию поиска, включающий только аватар `avatar`, никнейм `nick`, учётную запись пользователя `userID`, пол `gender`, дату рождения `birthday` и самоподпись `selfSignature`. Это может удовлетворить потребности отображения списка результатов поиска пользователей и не включает пользовательские поля. Для подробного профиля пользователя см.: [getUserProfile](https://www.tencentcloud.com/document/product/1047/48161#querying-the-profile-of-another-user). |
| cursor | String | Курсор, необходимый для вызова API поиска для продолжения извлечения. |

##### **Пример**

```
// Search specified keyword list and birth date range// - Search users with 'test' or 'user' in their profile, and whose birth date is before 20240101let promise = chat.searchCloudUsers({   keywordList: ['test', 'user'],   maxBirthday: 20240101,}); promise.then(function(imResponse) { // User search successful   const { totalCount, cursor, searchResultList } = imResponse.data;   console.log(totalCount); // Total number of users meeting the search condition   console.log(cursor); // Starting position for the next cloud search, if not present, indicates search results are fully retrieved   console.log(searchResultList); // List of users meeting the search condition, return paginated grouping results, maximum 100 per page, count set   for (let i = 0; i < searchResultList.length; i++) {      const profileItem = searchResultList[i];      const { userID, nick, gender, avatar } = profileItem;      console.log(userID); // User ID      console.log(nick); // User nickname      console.log(gender); // User gender      console.log(avatar); // User avatar    }}).catch(function(imError) {   console.error(imError); // search user failed});
```


---
*Источник: [https://trtc.io/document/67679](https://trtc.io/document/67679)*

---
*Источник (EN): [cloud-search-users.md](./cloud-search-users.md)*
