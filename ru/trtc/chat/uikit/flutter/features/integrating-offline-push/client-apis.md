# API клиента

## TencentCloudChatPush

class TencentCloudChatPush: Класс интерфейса плагина Push.

## Обзор API

### Интерфейс регистрации/отмены регистрации службы Push

| API | Описание |
| --- | --- |
| [registerPush](#0686c8e9-27c3-4a2e-9176-1e81b925a6f3) | Зарегистрировать службу Push, опционально переопределить информацию о push из JSON параметра интерфейса. |
| [unRegisterPush](#unRegisterPush) | Отменить регистрацию службы Push. |
| [setRegistrationID](#setRegistrationID) | RegistrationID — это уникальный идентификатор устройства получения push-уведомлений. По умолчанию этот ID автоматически генерируется при успешной регистрации службы push, но вы можете также установить его вручную. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. Учтите, что переустановка приложения изменит RegistrationID, поэтому необходимо вызвать интерфейс setRegistrationID перед регистрацией службы push. |
| [getRegistrationID](#getRegistrationID) | После успешной регистрации службы push вы можете получить уникальный идентификатор устройства получения push-уведомлений, то есть RegistrationID, вызвав интерфейс getRegistrationID. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. |

### Интерфейс глобального прослушивания Push

| API | Описание |
| --- | --- |
| [addPushListener](#addPushListener) | Добавить слушатель Push. |
| [removePushListener](#removePushListener) | Удалить слушатель Push. |

### Интерфейс пользовательской конфигурации

| API | Описание |
| --- | --- |
| [forceUseFCMPushChannel](#forceUseFCMPushChannel) | Указать, что автономная отправка должна использовать канал FCM для устройства. Это необходимо вызвать перед регистрацией службы push. |
| [disablePostNotificationInForeground](#disablePostNotificationInForeground) | Отключить уведомление в строке состояния, когда приложение находится в foreground. |

## Детали интерфейса

### Класс плагина Push

TencentCloudChatPush(): Получить экземпляр плагина TencentCloudChatPush, который является статичным singleton. Последующие шаги выполняются через этот экземпляр singleton для вызовов методов.

### Описание функций-членов

#### registerPush

Зарегистрировать службу Push, должна быть вызвана после успешного входа учетной записи Chat.

**Пример кода:**

```
void _onNotificationClicked({required String ext, String? userID, String? groupID}) {  print("_onNotificationClicked: $ext, userID: $userID, groupID: $groupID");  /// Custom Processing}TencentCloudChatPush().registerPush(    onNotificationClicked: _onNotificationClicked,    apnsCertificateID: Your configured Certificate ID);
```

**Описание параметров:**

| Параметр |  | Тип | Описание |  |
| --- | --- | --- | --- | --- |
| onNotificationClicked | ext | String | Полная информация ext, переносимая сообщением, указывается отправителем. Если не указана, имеется значение по умолчанию. Вы можете проанализировать это поле для навигации на соответствующую страницу. |  |
|  | userID | String? | Этот параметр соответствует userID. Автоматически пытается проанализировать строку JSON ext для получения userID другой стороны в одиночном чате.**Примечание:**Если вы не настроили поле ext, которое по умолчанию задано SDK или UIKit, вы можете использовать здесь анализ по умолчанию. Если попытка анализа не удалась, это будет null. |  |
|  | groupID | String? | Этот параметр соответствует groupID. Автоматически пытается проанализировать строку JSON ext для получения информации groupID для групповых чатов.**Примечание:**Если вы не настроили поле ext, которое по умолчанию задано SDK или UIKit, вы можете использовать здесь анализ по умолчанию. Если попытка анализа не удалась, это будет null. |  |
| apnsCertificateID |  | int? | ID сертификата push-уведомления iOS, который вы настроили. |  |

#### unRegisterPush

Отменить регистрацию службы автономной отправки.

**Пример кода:**

```
TencentCloudChatPush().unRegisterPush();
```

#### setRegistrationID

Установить ID push, используемый для регистрации службы автономной отправки, то есть RegistrationID, который необходимо вызвать перед регистрацией службы push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| registrationID | ID push устройства, который изменится после переустановки. |

**Пример кода:**

```
TencentCloudChatPush().setRegistrationID(registrationID: registrationID);
```

#### getRegistrationID

После успешной регистрации для службы автономной отправки получить ID push, то есть RegistrationID.

**Пример кода:**

```
TencentCloudChatPush().getRegistrationID();
```

#### addPushListener

Добавить слушатель Push

**Пример кода:**

```
TIMPushListener timPushListener = TIMPushListener(  onRecvPushMessage: (TimPushMessage message) {      String messageLog = message.toLogString();      debugPrint(          "message: $messageLog");      },  onRevokePushMessage: (String messageId) {    debugPrint(        "message: $messageId");  },  onNotificationClicked: (String ext) {    debugPrint(        "ext: $ext");  });TencentCloudChatPush.addPushListener(listener: timPushListener);
```

#### removePushListener

Удалить слушатель Push

**Пример кода:**

```
TIMPushListener timPushListener = TIMPushListener(  onRecvPushMessage: (TimPushMessage message) {      String messageLog = message.toLogString();      debugPrint(          "message: $messageLog");      },  onRevokePushMessage: (String messageId) {    debugPrint(        "message: $messageId");  },  onNotificationClicked: (String ext) {    debugPrint(        "ext: $ext");  });TencentCloudChatPush.removePushListener(listener: timPushListener);
```

#### forceUseFCMPushChannel

Указать, что автономная отправка должна использовать канал FCM для устройства. Это необходимо вызвать перед регистрацией службы push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| enable | true: использовать канал FCM.false: использовать встроенный канал. |

**Пример кода:**

```
TencentCloudChatPush.forceUseFCMPushChannel(enable: true);
```

#### disablePostNotificationInForeground

Отключить всплывающие уведомления в строке состояния, когда приложение находится в foreground. Когда Push SDK получает онлайн Push, он автоматически добавит Notification в строку состояния. Если вы хотите обрабатывать онлайн Push-сообщения самостоятельно, вы можете вызвать этот интерфейс для отключения функции автоматического всплывающего окна в строке состояния.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| disable | true: отключитьfalse: включить |

**Пример кода:**

```
TencentCloudChatPush.disablePostNotificationInForeground(disable: true);
```


---
*Источник: [https://trtc.io/document/67581](https://trtc.io/document/67581)*

---
*Источник (EN): [client-apis.md](./client-apis.md)*
