# Поиск облачных групп

## Описание функции

Поиск облачных групп позволяет пользователям быстро находить существующие группы или открывать новые группы по ключевым словам. Пользователи могут быстро найти существующие группы через этот API и изучить интересующие их группы, которые они еще не посещали, с помощью ключевых слов, что облегчает управление и участие в деятельности групп социального круга.

> **Примечания:** Функция поиска облачных групп доступна только для клиентов Pro Plus и Enterprise. Она может быть использована после [покупки Pro Plus и Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro&language=en); версия Free Trial поддерживает [определенный лимит бесплатного пробного периода](https://www.tencentcloud.com/document/product/1047/67651#d1113f0d-47e8-4211-82c0-00d2efb72586), действительный в течение одного месяца. Функция поиска облачных групп поддерживается начиная с **v3.5.0**. Область поиска: выполняется нечеткий поиск совпадений всех названий групп по ключевым словам и точный поиск совпадений всех идентификаторов групп. Информация в списке групп, полученном через этот API, неполная (включает только идентификатор группы, аватар группы, название группы, тип группы, текущее количество членов, описание группы, идентификатор владельца группы и т. д.). Для запроса подробной информации о группе см.: [getGroupProfile](https://www.tencentcloud.com/document/product/1047/48184#getting-the-group-profile). Максимальное количество результатов поиска за один раз составляет 100. Прямые группы (TencentCloudChat.TYPES.GRP_AVCHATROOM) не поддерживаются для поиска. Этот API имеет ограничение облачной частоты 2 раз/сек и ограничение локального вызова API 20 раз/5 сек.

## Поиск облачных групп

##### API

```
chat.searchCloudGroups(options);
```

##### Параметры

Параметр options имеет тип Object и содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| keywordList | Array | `обязательный` Список ключевых слов, поддерживает до 5 ключевых слов. |
| keywordListMatchType | String \| undefined | Тип сопоставления списка ключевых слов: or: поиск с отношением "или" (по умолчанию) and: поиск с отношением "и" |
| groupTypeList | Array \| undefined | Если не предоставлен, по умолчанию выполняется поиск по всем типам групп (прямые группы не поддерживаются (`TencentCloudChat.TYPES.GRP_AVCHATROOM`)). Типы групп: `TencentCloudChat.TYPES.GRP_WORK` группа работы друзей `TencentCloudChat.TYPES.GRP_PUBLIC` группа социального общения незнакомцев `TencentCloudChat.TYPES.GRP_MEETING` временная группа встреч `TencentCloudChat.TYPES.GRP_COMMUNITY` сообщество |
| cursor | String \| undefined | Начальная позиция для каждого поиска облачных групп. Не передавайте `cursor` для первого поиска. Для продолжения поиска заполните значение `cursor`, возвращенное последним вызовом API `searchCloudGroups`. |
| count | Number \| undefined | Количество результатов для каждого поиска облачных групп. Значение по умолчанию составляет 20, максимальное значение составляет 100. |

##### **Возвращаемое значение**

`Promise`

| Имя | Тип | Описание |
| --- | --- | --- |
| totalCount | Number | Общее количество групп, соответствующих критериям поиска. |
| searchResultList | Array | Список профилей групп `Group`, соответствующих критериям поиска, включает только идентификатор группы `groupID`, аватар группы `avatar`, название группы `name`, тип группы `type`, текущее количество членов `memberCount`, описание группы `introduction` и идентификатор владельца группы `ownerID`, что может удовлетворить потребности отображения списка результатов поиска. Для подробной информации о группе см.: [getGroupProfile](https://www.tencentcloud.com/document/product/1047/48184#getting-the-group-profile). |
| cursor | String | Курсор, необходимый для вызова API поиска для продолжения получения данных. |

##### **Пример**

```
// Список указанных ключевых слов и типов групп для поиска// - Поиск групп, где 'test' или 'user' появляются в списке пользователей, а тип группы - 'группа социального общения незнакомцев (TencentCloudChat.TYPES.GRP_PUBLIC)' или 'группа работы друзей (TencentCloudChat.TYPES.GRP_WORK)'let promise = chat.searchCloudGroups({   keywordList: ['test', 'user'],   groupTypeList: [TencentCloudChat.TYPES.GRP_PUBLIC, TencentCloudChat.TYPES.GRP_WORK],}); promise.then(function(imResponse) {   // Поиск группы выполнен успешно   const { totalCount, cursor, searchResultList } = imResponse.data;   console.log(totalCount); // Общее количество групп, соответствующих критериям поиска   console.log(cursor); // Начальная позиция для следующего облачного поиска, если не присутствует, указывает на полное получение результатов поиска   console.log(searchResultList); // Группы, соответствующие критериям поиска, возвращают постраничные результаты группировки, максимум 100 за раз, на основе входного значения count   for (let i = 0; i < searchResultList.length; i++) {      const groupItem = searchResultList[i];      const { groupID, name, type, avatar, memberCount, introduction, ownerID } = groupItem;      console.log(groupID); // Идентификатор группы      console.log(name); // Название группы      console.log(type); // Тип группы      console.log(avatar); // Аватар группы      console.log(memberCount); // Текущее количество членов      console.log(introduction); // Описание группы      console.log(ownerID); // Идентификатор пользователя владельца группы    }}).catch(function(imError) {   console.error(imError); // поиск пользователя не выполнен});
```


---
*Источник: [https://trtc.io/document/67681](https://trtc.io/document/67681)*

---
*Источник (EN): [cloud-search-groups.md](./cloud-search-groups.md)*
