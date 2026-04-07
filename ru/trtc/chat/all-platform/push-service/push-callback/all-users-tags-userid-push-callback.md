# Всех пользователей / Теги / Обратный вызов Push по UserID

#### Описание функции

После включения плагина push результаты push-уведомлений можно перенаправить на бэкенд приложения путем настройки базового обратного вызова.

#### Примечания

- Этот обратный вызов относится к событийному обратному вызову после распространения вниз по потоку. Чтобы предотвратить перегрузку бэкенда приложения большим количеством запросов обратного вызова, **QPS по умолчанию: 1000 раз/с**. Чрезмерно частые обратные вызовы будут повторены с задержкой. Если вам необходимо изменить QPS в соответствии с требованиями бизнеса, вы можете отправить [тикет](https://trtc.io/zh/login/redirect?s_url=https://console.tencentcloud.com/workorder/category) для подачи заявки.
- Для включения этого обратного вызова необходимо настроить URL обратного вызова и включить соответствующий переключатель для этого обратного вызова. Дополнительные сведения о методе настройки см. в документации [Webhooks](https://intl.cloud.tencent.com/document/product/1047/34520).
- Во время этого обратного вызова бэкенд Chat инициирует HTTP POST-запрос на бэкенд приложения.
- После получения запроса обратного вызова бэкенд приложения должен проверить, соответствует ли SDKAppID, содержащийся в URL запроса, его собственному SDKAppID.
- Для получения дополнительной информации, связанной с безопасностью, обратитесь к документу [Обзор сторонних обратных вызовов: соображения безопасности](https://intl.cloud.tencent.com/document/product/1047/34354).

### Описание API

#### Пример URL запроса:

В следующем примере URL обратного вызова, настроенный в конфигурации приложения, — это `https://www.example.com`

Пример:

```
https://www.example.com?SdkAppid=$SDKAppID&CallbackCommand=$CallbackCommand&contenttype=json
```

#### Параметры запроса

| Поле | Описание |
| --- | --- |
| https | Протокол запроса — HTTPSМетод запроса — POST |
| www.example.com | URL обратного вызова |
| SdkAppid | SDKAppID, выделенный консолью Instant Messaging при создании приложения |
| CallbackCommand | Фиксированное значение: Push.AllMemberPush |
| contenttype | Полезная нагрузка запроса фиксирована как JSON |

#### Пример пакета запроса

```
{    "Events": [   // Длина массива events варьируется от 1 до 100      {        "CallbackCommand":"Push.AllMemberPush",        "EventType": 1,                                                // Тип события, EventType=1 указывает на оффлайн push        "TaskId": "657bf434_537529d8_2000005e80aa873_2780d131_bc614e", // TaskId для push всех членов/Теги/одиночный push        "TaskTime": 1557481127,                                        // Временная метка, когда была инициирована задача push всех членов, в секундах        "EventTime": 1557481128,                                       // Временная метка, когда произошло событие, в секундах        "To_Account": "user2",                                         // Получатель        "PushPlatform": 1,                                             // Поставщик        "PushStage": 1,                                                // Этап push        "ErrCode": 0,                                                  // Результат события push        "ErrInfo": "OK"                                                // Описание результата события push, может быть пусто      },      {        "CallbackCommand":"Push.AllMemberPush",        "EventType": 2,                                                // Тип события, EventType=2 указывает на онлайн push        "TaskId": "657bf434_537529d8_2000005e80aa873_2780d131_9",      // TaskId для push всех членов/Теги/одиночный push        "TaskTime": 1557481127,                                        // Временная метка, когда была инициирована задача push всех членов, в секундах        "EventTime": 1557481129,                                       // Временная метка, когда произошло событие, в секундах        "To_Account": "user3",                                         // Получатель        "PushPlatform": 0,                                             // Поставщик        "PushStage": 1,                                                // Этап push        "ErrCode": 0,                                                  // Результат события push        "ErrInfo": "OK"                                                // Описание результата события push, может быть пусто      },      ....    ]}
```

#### Поля пакета запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| Events | Array [ Event Object ] | Содержимое пакетного обратного вызова, содержащее данные для до 100 событий обратного вызова (объект Event) |

##### Структура объекта Event

| Поле | Тип | Описание |
| --- | --- | --- |
| CallbackCommand | String | Команда обратного вызова |
| EventType | Integer | Тип события:EventType = 1 указывает на оффлайн pushEventType = 2 указывает на онлайн push |
| TaskId | String | ID задачи, возвращаемый при отправке push всем членам |
| DataId | String | Пользовательский идентификатор бизнеса, который прозрачно передается в запросе обратного вызова push. |
| TaskTime | Integer | Временная метка, когда была инициирована задача push всех членов, в секундах |
| EventTime | Integer | Временная метка, когда произошло событие, в секундах |
| To_Account | String | UserID получателя |
| PushPlatform | Integer | Поставщик push (для онлайн push EventType = 2, поставщик не различается, по умолчанию 0):PushPlatform = 0 указывает на неизвестного поставщикаPushPlatform = 1 указывает на Apple APNS pushPushPlatform = 2 указывает на Xiaomi pushPushPlatform = 3 указывает на Huawei pushPushPlatform = 4 указывает на Google FCM pushPushPlatform = 5 указывает на Meizu pushPushPlatform = 6 указывает на OPPO pushPushPlatform = 7 указывает на vivo pushPushPlatform = 8 указывает на Honor push |
| DeviceType | Integer | Поставщик push (для оффлайн push EventType = 1, поставщик не различается, по умолчанию 0):PushPlatform = 0 указывает на неизвестное устройствоPushPlatform = 1 указывает на устройство Apple APNSPushPlatform = 2 указывает на устройство XiaomiPushPlatform = 3 указывает на устройство HuaweiPushPlatform = 4 указывает на устройство Google FCMPushPlatform = 5 указывает на устройство MeizuPushPlatform = 6 указывает на устройство OPPOPushPlatform = 7 указывает на устройство vivoPushPlatform = 8 указывает на устройство Honor |
| PushStage | Integer | Этап push:PushStage = 1 указывает на отправку pushPushStage = 2 указывает на получение pushPushStage = 3 указывает на клик по push |
| ErrCode | Integer | Результат события push:ErrCode = 0 указывает на успехErrCode, отличный от нуля, указывает на сбой |
| ErrInfo | String | Описание результата события push, может быть пусто |

#### Пример пакета ответа

```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0 // 0 означает успех обратного вызова, 1 означает ошибку обратного вызова}
```

#### Описание полей пакета ответа

| Поле | Тип | Описание |
| --- | --- | --- |
| ActionStatus | String | Результат обработки запроса:OK Обозначает успешную обработкуFAILURE обозначает неудачное выполнение |
| ErrorCode | Integer | Код ошибки |
| ErrorInfo | String | Описание ошибки |


---
*Источник: [https://trtc.io/document/67551](https://trtc.io/document/67551)*

---
*Источник (EN): [all-users-tags-userid-push-callback.md](./all-users-tags-userid-push-callback.md)*
