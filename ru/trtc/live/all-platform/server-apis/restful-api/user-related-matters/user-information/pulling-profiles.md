# Получение профилей

## Обзор функции

- Этот API используется для получения полей профиля друзей и других пользователей.
- Этот API может получать [стандартные поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520) и [пользовательские поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520).
- Рекомендуется получать поля профиля не более чем 100 пользователей за раз, чтобы избежать сбоя пакета ответа из-за избыточного объёма данных.
- Убедитесь, что все учётные записи в запросе импортированы в консоль Chat. В противном случае на бэкенде Chat будет выведена ошибка.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/profile/portrait_get?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В следующей таблице описаны изменённые параметры при вызове этого API. Для других параметров см. раздел [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, где находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/profile/portrait_get | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учётная запись администратора приложения. Для получения дополнительной информации см. раздел **App Admin** в статье [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учётной записью администратора приложения. Для получения подробной информации см. раздел [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который должен быть `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

- **Чтение одного поля профиля пользователя**

```
{  "To_Account":["id1"],  "TagList":  [      "Tag_Profile_IM_Nick"  ]}
```

- **Чтение нескольких полей профиля одного пользователя**

```
{  "To_Account":["id1"],  "TagList":  [      "Tag_Profile_IM_Nick",      "Tag_Profile_IM_AllowType",      "Tag_Profile_IM_SelfSignature",      "Tag_Profile_Custom_Test"  ]}
```

- **Чтение одного поля профиля нескольких пользователей**

```
{  "To_Account":["id1","id2","id3"],  "TagList":  [      "Tag_Profile_IM_Nick"  ]}
```

- **Чтение нескольких полей профиля нескольких пользователей**

```
{  "To_Account":["id1","id2","id3","id4"],  "TagList":  [      "Tag_Profile_IM_Nick",      "Tag_Profile_IM_AllowType",      "Tag_Profile_IM_SelfSignature",      "Tag_Profile_Custom_Test"  ]}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| To_Account | Array | Обязательное | UserID пользователей, чьи поля профиля должны быть получены. Примечание: поля профиля не более 100 пользователей могут быть получены каждый раз, чтобы предотвратить сбой пакета ответа из-за избыточного объёма данных. |
| TagList | Array | Обязательное | Тег поля профиля, которое необходимо получить. Поддерживаемые поля включают:Стандартные поля профиля. Для получения дополнительной информации см. раздел [Стандартные поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520).Пользовательские поля профиля. Для получения дополнительной информации см. раздел [Пользовательские поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520). |

### Пример ответа

- **Чтение одного поля профиля пользователя**

```
{  "UserProfileItem":  [      {          "To_Account":"id1",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest1"              }          ],          "ResultCode":0,          "ResultInfo":""      }  ],  "ActionStatus":"OK",  "ErrorCode":0,  "ErrorInfo":"",  "ErrorDisplay":""}
```

- **Чтение нескольких полей профиля одного пользователя**

```
{  "UserProfileItem":  [      {          "To_Account":"id1",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest1"              },              {                  "Tag":"Tag_Profile_IM_AllowType",                  "Value":"AllowType_Type_NeedConfirm"              },              {                  "Tag":"Tag_Profile_IM_SelfSignature",                  "Value":"I'm Test1"              },              {                  "Tag":"Tag_Profile_Custom_Test",                  "Value":"Custom Data1"              }          ],          "ResultCode":0,          "ResultInfo":""      }  ],  "ActionStatus":"OK",  "ErrorCode":0,  "ErrorInfo":"",  "ErrorDisplay":""}
```

- **Чтение одного поля профиля нескольких пользователей**

```
{  "UserProfileItem":  [      {          "To_Account":"id1",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest1"              }          ],          "ResultCode":0,          "ResultInfo":""      },      {          "To_Account":"id2",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest2"              }          ],          "ResultCode":0,          "ResultInfo":""      },      {          "To_Account":"id3",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest3"              }          ],          "ResultCode":0,          "ResultInfo":""      }  ],  "ActionStatus":"OK",  "ErrorCode":0,  "ErrorInfo":"",  "ErrorDisplay":""}
```

- **Чтение нескольких полей профиля нескольких пользователей**

```
{  "UserProfileItem":  [      {          "To_Account":"id1",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest1"              },              {                  "Tag":"Tag_Profile_IM_AllowType",                  "Value":"AllowType_Type_NeedConfirm"              },              {                  "Tag":"Tag_Profile_IM_SelfSignature",                  "Value":"I'm Test1"              },              {                  "Tag":"Tag_Profile_Custom_Test",                  "Value":"Custom Data1"              }          ],          "ResultCode":0,          "ResultInfo":""      },      {          "To_Account":"id2",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest2"              },              {                  "Tag":"Tag_Profile_IM_AllowType",                  "Value":"AllowType_Type_DenyAny"              },              {                  "Tag":"Tag_Profile_IM_SelfSignature",                  "Value":"I'm Test2"              },              {                  "Tag":"Tag_Profile_Custom_Test",                  "Value":"Custom Data2"              }          ],          "ResultCode":0,          "ResultInfo":""      },      {          "To_Account":"id3",          "ProfileItem":          [              {                  "Tag":"Tag_Profile_IM_Nick",                  "Value":"NickNameTest3"              },              {                  "Tag":"Tag_Profile_IM_AllowType",                  "Value":"AllowType_Type_AllowAny"              },              {                  "Tag":"Tag_Profile_IM_SelfSignature",                  "Value":"I'm Test3"              },              {                  "Tag":"Tag_Profile_Custom_Test",                  "Value":"Custom Data3"              }          ],          "ResultCode":0,          "ResultInfo":""      },      {          "To_Account":"id4",          "ResultCode":40006,          "ResultInfo":"Err_Profile_PortraitGet_Read_Custom_Data_Fail"      }  ],  "Fail_Account":["id4"],  "ActionStatus":"OK",  "ErrorCode":0,  "ErrorInfo":"",  "ErrorDisplay":""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| UserProfileItem | Array | Структурированная информация возвращаемого профиля пользователя. |
| To_Account | String | UserID пользователя. |
| ProfileItem | Array | Возвращаемый массив объектов профиля пользователя. Каждый объект в массиве содержит тег и значение. |
| Tag | String | Возвращаемое имя объекта профиля. Объекты профиля включают:Стандартные поля профиля. Для получения дополнительной информации см. раздел [Стандартные поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520).Пользовательские поля профиля. Для получения дополнительной информации см. раздел [Пользовательские поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520). |
| Value | uint64_t/string/bytes | Значение полученного объекта профиля. Для получения дополнительной информации см. раздел [Поля профиля](https://intl.cloud.tencent.com/document/product/1047/33520). |
| ResultCode | Integer | Результат обработки To_Account. 0: Успешно. Другие значения: Ошибка. |
| ResultInfo | String | Описание ошибки `To_Account`. Это поле пусто, если запрос успешен. |
| Fail_Account | Array | Список пользователей, для которых обработка не удалась. Это поле возвращается только при ошибке хотя бы одного пользователя. |
| ActionStatus | String | Результат запроса. `OK` означает, что запрос был успешным. `FAIL` означает, что запрос не удался. |
| ErrorCode | Integer | Код ошибки. `0`: Успешно; другие значения: Ошибка |
| ErrorInfo | String | Подробная информация об ошибке. |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте. |

## Коды ошибок

Код состояния HTTP, возвращаемый этим API, всегда равен 200, если не возникает ошибка сети (например, ошибка 502). Конкретный код ошибки и детали можно найти в полях ответа `ErrorCode` и `ErrorInfo` соответственно.
Для общих кодов ошибок (60000 до 79999) см. раздел [Коды ошибок](https://intl.cloud.tencent.com/document/product/1047/34348).
В следующей таблице описаны коды ошибок, относящиеся к этому API:

| Код ошибки | Описание |
| --- | --- |
| 40001 | Неверный параметр запроса. Проверьте ваш запрос согласно описанию ошибки. |
| 40002 | Ошибка параметра запроса. To_Account не указан. |
| 40003 | Запрошенная учётная запись не существует. |
| 40004 | Запрос требует прав администратора приложения. |
| 40006 | Внутренняя ошибка сервера. Попробуйте позже. |
| 40007 | Нет разрешения на чтение полей профиля. |
| 40009 | Тег поля профиля не существует. |

## Инструмент отладки API

Используйте [онлайн-инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/profile/portrait_get) для отладки этого API.

## Ссылки

Настройка профилей ([v4/profile/portrait_set](https://intl.cloud.tencent.com/document/product/1047/34916)).


---
*Источник: [https://trtc.io/document/34917](https://trtc.io/document/34917)*

---
*Источник (EN): [pulling-profiles.md](./pulling-profiles.md)*
