# Импорт друзей

## Обзор функции

- Этот API используется для импорта односторонних друзей пакетами.
- Рекомендуется импортировать друзей одного пользователя пакетами, чтобы избежать конфликтов записи из-за одновременных записей.

## Описание вызова API

### Пример URL запроса

```
https://xxxxxx/v4/sns/friend_import?sdkappid=88888888&identifier=admin&usersig=xxx&random=99999999&contenttype=json
```

### Параметры запроса

В таблице ниже описаны измененные параметры при вызове этого API. Для других параметров см. [Обзор RESTful API](https://intl.cloud.tencent.com/document/product/1047/34620).

| Параметр | Описание |
| --- | --- |
| xxxxxx | Доменное имя, соответствующее стране/региону, в котором находится ваш SDKAppID.Китай: `console.tim.qq.com`Сингапур: `adminapisgp.im.qcloud.com`Сеул: `adminapikr.im.qcloud.com`Токио: `adminapijpn.im.qcloud.com`Франкфурт: `adminapiger.im.qcloud.com`Кремниевая долина: `adminapiusa.im.qcloud.com`Джакарта: `adminapiidn.im.qcloud.com` |
| v4/sns/friend_import | API запроса |
| sdkappid | SDKAppID, назначенный консолью Chat при создании приложения |
| identifier | Учетная запись администратора приложения. Дополнительные сведения см. в разделе **App Admin** в документе [Аутентификация входа](https://intl.cloud.tencent.com/document/product/1047/33517). |
| usersig | Подпись, созданная учетной записью администратора приложения. Подробнее см. в разделе [Создание UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |
| random | Случайное 32-битное целое число без знака в диапазоне от 0 до 4294967295. |
| contenttype | Формат запроса, который должен быть всегда `json`. |

### Максимальная частота вызовов

200 вызовов в секунду

### Пример запроса

- **Базовый формат**

```
{  "From_Account":"id",  "AddFriendItem":  [      {          "To_Account":"id1",          "AddSource":"AddSource_Type_XXXXXXXX"      }  ]}
```

- **Ответ на полный запрос**

```
{  "From_Account":"id",  "AddFriendItem":  [      {          "To_Account":"id1",          "Remark":"remark1",          "RemarkTime":1420000001,          "GroupName":["Friends"],          "AddSource":"AddSource_Type_XXXXXXXX",          "AddWording":"I'm Test1",          "AddTime":1420000001,          "CustomItem":          [              {                  "Tag":"Tag_SNS_Custom_XXXX",                  "Value":"Test"              },              {                  "Tag":"Tag_SNS_Custom_YYYY",                  "Value":0              }          ]      }  ]}
```

- **Ответ на пакетный запрос**

```
{  "From_Account":"id",  "AddFriendItem":  [      {          "To_Account":"id1",          "AddSource":"AddSource_Type_XXXXXXXX"      },      {          "To_Account":"id2",          "Remark":"remark2",          "RemarkTime":1420000001,          "GroupName":["Friends"],          "AddSource":"AddSource_Type_XXXXXXXX",          "AddWording":"I'm Test2",          "AddTime":1420000001      },      {          "To_Account":"id3",          "Remark":"remark3",          "RemarkTime":1420000001,          "GroupName":["Colleagues","Friends"],          "AddSource":"AddSource_Type_XXXXXXXX",          "AddWording":"I'm Test3",          "AddTime":1420000001,          "CustomItem":          [              {                  "Tag":"Tag_SNS_Custom_XXXX",                  "Value":"Test"              },              {                  "Tag":"Tag_SNS_Custom_YYYY",                  "Value":0              }          ]      }  ]}
```

### Поля запроса

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| From_Account | String | Да | UserID, инициирующий запрос. |
| AddFriendItem | Array | Да | Структурный объект друга, количество друзей в одном запросе не должно превышать 1000. |
| To_Account | String | Да | `UserID` друга. |
| Remark | String | Нет | Примечание друга, установленное `From_Account` для `To_Account`. Дополнительные сведения см. в разделе [Стандартные поля друга](https://intl.cloud.tencent.com/document/product/1047/33521). |
| RemarkTime | Integer | Нет | Время добавления примечания к `To_Account` от `From_Account`. |
| GroupName | Array | Нет | Информация о группе `To_Account`, добавленная `From_Account`. Дополнительные сведения см. в разделе [Стандартные поля друга](https://intl.cloud.tencent.com/document/product/1047/33521). |
| AddSource | String | Да | Источник, из которого добавлен друг. Дополнительные сведения см. в разделе [Стандартные поля друга](https://intl.cloud.tencent.com/document/product/1047/33521). |
| AddWording | String | Нет | Примечание, которое пользователь, инициирующий запрос друга, пишет о пользователе, которого нужно добавить. Дополнительные сведения см. в разделе [Стандартные поля друга](https://intl.cloud.tencent.com/document/product/1047/33521). |
| AddTime | Integer | Нет | Время установления отношения дружбы между `From_Account` и `To_Account`. |
| CustomItem | Array | Нет | Пользовательские данные друга `To_Account`, установленные `From_Account`. Каждый элемент имеет поле Tag и поле Value. Дополнительные сведения см. в разделе [Пользовательские поля друга](https://intl.cloud.tencent.com/document/product/1047/33521). |
| Tag | String | Нет | Имя пользовательского поля друга. Для его использования сначала подайте заявку на пользовательское поле друга в [консоли Chat](https://console.tencentcloud.com/im), выбрав **App Configuration** > **Feature Configuration**. |
| Value | String/Integer | Нет | Значение пользовательского поля друга. |

### Пример ответа

- **Ответ на базовый или полный запрос**

```
{  "ResultItem":  [      {          "To_Account":"id1",          "ResultCode":0,          "ResultInfo":""      }  ],  "ActionStatus":"OK",  "ErrorCode":0,  "ErrorInfo":"",  "ErrorDisplay":""}
```

- **Ответ на пакетный запрос**

```
{  "ResultItem":  [      {          "To_Account":"id1",          "ResultCode":0,          "ResultInfo":""      },      {          "To_Account":"id2",          "ResultCode":30010,          "ResultInfo":"Err_SNS_FriendImport_My_Friend_Num_Exceed_Threshold"      },      {          "To_Account":"id3",          "ResultCode":30002,          "ResultInfo":"Err_SNS_FriendImport_SdkAppId_Illegal"      }  ],  "Fail_Account":["id2","id3"],  "ActionStatus":"OK",  "ErrorCode":0,  "ErrorInfo":"",  "ErrorDisplay":""}
```

### Поля ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ResultItem | Array | Результат добавления друзей в пакетном режиме, который является массивом UserID и соответствующих результатов. |
| To_Account | String | UserID, который вы запросили добавить в качестве друга. |
| ResultCode | Integer | Результат для `To_Account`. `0`: Успешно. Другие значения: Ошибка. Подробнее о ненулевых результатах см. [Коды ошибок](#ErrorCode). |
| ResultInfo | String | Описание ошибки для `To_Account`. Это поле пусто, если запрос успешен. |
| Fail_Account | Array | Список пользователей, обработка которых не удалась. Это поле возвращается только при сбое обработки по крайней мере одного пользователя. |
| ActionStatus | String | Результат запроса. `OK`: Успешно. `FAIL`: Ошибка. |
| ErrorCode | Integer | Код ошибки. `0`: Успешно. Другие значения: Ошибка. Подробнее о ненулевых результатах см. [Коды ошибок](#ErrorCode). |
| ErrorInfo | String | Подробная информация об ошибке |
| ErrorDisplay | String | Подробная информация, отображаемая на клиенте |

## Коды ошибок

| Код ошибки | Описание |
| --- | --- |
| 30001 | Неправильный параметр запроса. Проверьте ваш запрос согласно описанию ошибки. |
| 30002 | SDKAppID не совпадает. |
| 30003 | Запрашиваемая учетная запись не существует. |
| 30004 | Запрос требует разрешений администратора приложения. |
| 30006 | Внутренняя ошибка сервера. Попробуйте еще раз. |
| 30007 | Тайм-аут сети. Попробуйте позже. |
| 30008 | Произошел конфликт записи из-за одновременных операций записи. Рекомендуется использовать пакетную обработку. |
| 30010 | Количество друзей достигло верхнего предела системы. |
| 30011 | Достигнут максимальный размер списка друзей. |

## Инструмент отладки API

Используйте [онлайн-инструмент отладки RESTful API](https://tcc.tencentcs.com/im-api-tool/index.html#/v4/sns/friend_import) для отладки этого API.

## Рекомендации

- [Добавление друзей](https://intl.cloud.tencent.com/document/product/1047/34902)
- [Обновление друзей](https://intl.cloud.tencent.com/document/product/1047/34904)
- [Удаление друзей](https://intl.cloud.tencent.com/document/product/1047/34905)
- [Удаление всех друзей](https://intl.cloud.tencent.com/document/product/1047/34906)
- [Проверка друзей](https://intl.cloud.tencent.com/document/product/1047/34907)
- [Получение списка друзей](https://intl.cloud.tencent.com/document/product/1047/34908)
- [Получение указанных друзей](https://intl.cloud.tencent.com/document/product/1047/34910)


---
*Источник: [https://trtc.io/document/34903](https://trtc.io/document/34903)*

---
*Источник (EN): [importing-friends.md](./importing-friends.md)*
