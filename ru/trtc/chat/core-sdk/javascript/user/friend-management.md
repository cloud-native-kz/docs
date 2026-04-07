# Управление друзьями

## Обзор функции

Chat SDK поддерживает управление друзьями, и пользователи могут добавлять и удалять друзей, а также устанавливать отправку сообщений только друзьям.

> **Примечание:** По умолчанию Chat SDK не проверяет связь при отправке персональных сообщений. Этот параметр по умолчанию обычно применяется в сценариях обслуживания клиентов, где необходимость добавления агента обслуживания клиентов в друзья перед общением неэффективна.
> Чтобы реализовать функцию "добавить в друзья перед отправкой сообщения", вы можете войти в [Chat Console](https://console.trtc.io/chat/login-message), выбрать **Конфигурация функций** > **Вход и сообщения** > **Проверка связи**, и включить **Проверка связи для персональных сообщений**. После включения пользователь может отправлять сообщения только друзьям. Если пользователь отправляет сообщение пользователю, который не является другом, SDK выдаст код ошибки 20009.

## Получение контактов

Контакты, кэшированные в SDK, могут быть получены. При обновлении контактов SDK отправит событие `TencentCloudChat.EVENT.FRIEND_LIST_UPDATED`.

##### **API**

```
chat.getFriendList();
```

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getFriendList();promise.then(function(imResponse) {  const friendList = imResponse.data; // Контакты}).catch(function(imError) {  console.warn('getFriendList error:', imError); // Ошибка получения контактов});
```

## Добавление друга

##### **API**

```
chat.addFriend(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| to | String | ID пользователя |
| source | String | Источник друга. Состоит из двух частей: префикса и ключевого слова. Первая часть — это `AddSource_Type_`, а вторая должна быть строкой длиной до 8 байт. Рекомендуется использовать английское слово или его аббревиатуру в качестве ключевого слова. Например, если ключевое слово — `Android`, это поле будет `AddSource_Type_Android`. |
| wording | String \| undefined | Замечания при добавлении в друзья, могут содержать до 256 байт. |
| type | String \| undefined | Способ добавления в друзья (двусторонний по умолчанию). Допустимые значения: `TencentCloudChat.TYPES.SNS_ADD_TYPE_SINGLE` (одностороннее добавление в друзья, где пользователь B находится в списке друзей пользователя A, но не наоборот) `TencentCloudChat.TYPES.SNS_ADD_TYPE_BOTH` (двустороннее добавление в друзья, где пользователь B находится в списке друзей пользователя A и наоборот) |
| remark | String \| undefined | Замечания друга, могут содержать до 96 байт. |
| groupName | String \| undefined | Имя списка, может содержать до 30 байт. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// Добавить другаlet promise = chat.addFriend({  to: 'user1',  source: 'AddSource_Type_Web',  remark: 'Jane',  groupName: 'Friend',  wording: 'I'm user0',  type: TencentCloudChat.TYPES.SNS_ADD_TYPE_BOTH,});promise.then(function(imResponse) {  // Запрос на добавление в друзья успешно отправлен  const { code } = imResponse.data;  if (code === 30539) {    // 30539 указывает, что пользователь user1 установил способ обработки запроса на добавление в друзья    // на ручное принятие полученных запросов на добавление в друзья.    // SDK вызовет событие TencentCloudChat.EVENT.FRIEND_APPLICATION_LIST_UPDATED.  } else if (code === 0) {    // 0 указывает, что пользователь user1 установил способ обработки запроса на добавление в друзья    // на автоматическое принятие всех полученных запросов на добавление в друзья.    // SDK вызовет событие TencentCloudChat.EVENT.FRIEND_LIST_UPDATED.  }}).catch(function(imError) {  console.warn('addFriend error:', imError); // Ошибка при добавлении друга});
```

## Удаление друга

Удаление друзей. Поддерживается как одностороннее, так и двустороннее удаление.

> **Примечание:** Рекомендуется включать до 100 значений `userID` в `userIDList` за раз, так как большой пакет данных может быть отклонен бэкендом, который требует, чтобы пакет данных не превышал 1 МБ.

##### **API**

```
chat.deleteFriend(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userIDList | Array | Список значений `userID` друзей, которые необходимо удалить. Количество значений `userID` не может превышать 100 за один запрос. |
| type | String \| undefined | Режим удаления (двустороннее удаление по умолчанию). Допустимые значения: `TencentCloudChat.TYPES.SNS_DELETE_TYPE_SINGLE` (одностороннее удаление, где пользователь B удаляется из списка друзей пользователя A, но не наоборот) `TencentCloudChat.TYPES.SNS_DELETE_TYPE_BOTH` (двустороннее удаление, где пользователь B удаляется из списка друзей пользователя A и наоборот) |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
TencentCloudChat
```

## Проверка связи дружбы

##### **API**

```
chat.checkFriend(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userIDList | Array | Список значений `userID` для проверки. Количество значений `userID` не может превышать 1 000 за один запрос. |
| type | String \| undefined | Режим проверки (двусторонняя проверка по умолчанию). Допустимые значения: `TencentCloudChat.TYPES.SNS_CHECK_TYPE_SINGLE` (одностороннее проверка, где список друзей пользователя A проверяется на предмет пользователя B, но не наоборот) `TencentCloudChat.TYPES.SNS_CHECK_TYPE_BOTH` (двусторонняя проверка, где список друзей пользователя A проверяется на предмет пользователя B и наоборот) |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
TencentCloudChat
```

## Получение профиля друга

Получить полные данные друга (включая стандартные поля друга и пользовательские поля друга) и полные данные профиля (включая стандартные поля профиля и пользовательские поля профиля) указанного друга.

##### **API**

```
chat.getFriendProfile(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userIDList | Array | Список значений `userID` друзей. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.getFriendProfile({  userIDList: ['user0','user1']});promise.then(function(imResponse) {  const { friendList, failureUserIDList } = imResponse.data;  friendList.forEach((friend) => {  });  failureUserIDList.forEach((item) => {    const { userID, code, message } = item;  });}).catch(function(imError) {  console.warn('getFriendProfile error:', imError);});
```

## Обновление друзей

Обновить данные цепочки отношений друга, поддерживая только обновления `remark` и `friendCustomField`.

##### **API**

```
chat.updateFriend(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userID | String | Значение `userID` друга |
| remark | String | Замечания друга, могут содержать до 96 байт. |
| friendCustomField | Array.<Object> | Коллекция пар пользовательских полей ключ-значение, которые можно использовать в соответствии с потребностями бизнеса. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// обновить замечание другаlet promise = chat.updateFriend({  userID: 'user1',  remark: 'helloworld'});promise.then(function(imResponse) {  console.log(imResponse.data);}).catch(function(imError) {  console.warn('getFriendProfile error:', imError);});
```

```
let promise = chat.updateFriend({  userID: 'user1',  friendCustomField: [    { key: 'Tag_SNS_Custom_test1', value: 'hello' },    { key: 'Tag_SNS_Custom_test2', value: 'world' },  ]});promise.then(function(imResponse) {  console.log(imResponse.data);}).catch(function(imError) {  console.warn('getFriendProfile error:', imError);});
```

## Получение списка запросов на добавление в друзья

Получить список запросов на добавление в друзья, кэшированный SDK. При обновлении списка запросов на добавление в друзья SDK отправит событие TencentCloudChat.EVENT.FRIEND_APPLICATION_LIST_UPDATED.

> **Примечание:** Если параметр `allowType` в вашем профиле (получённый через интерфейс `getMyProfile`) установлен на `TencentCloudChat.TYPES.ALLOW_TYPE_ALLOW_ANY` (при добавлении в друзья: разрешение любому добавлять вас в друзья), этот интерфейс не сможет получить список запросов на добавление в друзья.

##### **API**

```
chat.getFriendApplicationList();
```

##### **Параметры**

Отсутствуют

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
// обновить замечание другаlet promise = chat.updateFriend({  userID: 'user1',  remark: 'helloworld'});promise.then(function(imResponse) {  console.log(imResponse.data);}).catch(function(imError) {  console.warn('getFriendProfile error:', imError);});
```

## Принятие запроса на добавление в друзья

##### **API**

```
chat.acceptFriendApplication(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userID | String | `userID` ожидающего запроса на добавление в друзья. |
| remark | String | Замечания друга, могут содержать до 96 байт. |
| type | String | `TencentCloudChat.TYPES.SNS_APPLICATION_AGREE` - Согласиться на добавление в качестве одностороннего друга. `TencentCloudChat.TYPES.SNS_APPLICATION_AGREE_AND_ADD` - Согласиться и добавить в качестве двустороннего друга. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.acceptFriendApplication({  userID: 'user1',  remark: 'My Customer Service 1',  type: TencentCloudChat.TYPES.SNS_APPLICATION_AGREE_AND_ADD});promise.then(function(imResponse) {}).catch(function(imError) {  console.warn('acceptFriendApplication error:', imError);});
```

## Отклонение запроса на добавление в друзья

##### **API**

```
chat.refuseFriendApplication(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userID | String | `userID` ожидающего запроса на добавление в друзья. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.refuseFriendApplication({  userID: 'user1',});promise.then(function(imResponse) {}).catch(function(imError) {  console.warn('refuseFriendApplication error:', imError);});
```

## Удаление запроса на добавление в друзья

##### **API**

```
chat.deleteFriendApplication(options);
```

##### **Параметры**

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| userID | String | `userID` ожидающего запроса на добавление в друзья. |
| type | String | `TencentCloudChat.TYPES.SNS_APPLICATION_AGREE` - Согласиться на добавление в качестве одностороннего друга. `TencentCloudChat.TYPES.SNS_APPLICATION_AGREE_AND_ADD` - Согласиться и добавить в качестве двустороннего друга. |

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.refuseFriendApplication({  userID: 'user1',});promise.then(function(imResponse) {}).catch(function(imError) {  console.warn('refuseFriendApplication error:', imError);});
```

## Отметить запрос на добавление в друзья как прочитанный

##### **API**

```
chat.setFriendApplicationRead();
```

##### **Параметры**

Отсутствуют

##### **Возвращаемое значение**

`Promise`

##### **Примеры**

```
let promise = chat.setFriendApplicationRead();promise.then(function(imResponse) {}).catch(function(imError) {  console.warn('setFriendApplicationRead error:', imError);});
```


---
*Источник: [https://trtc.io/document/48158](https://trtc.io/document/48158)*

---
*Источник (EN): [friend-management.md](./friend-management.md)*
