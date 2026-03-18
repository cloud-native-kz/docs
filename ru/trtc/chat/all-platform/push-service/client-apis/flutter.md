# Flutter

## TencentCloudChatPush

class TencentCloudChatPush: класс интерфейса плагина Push.

## Обзор API

### Интерфейс регистрации/отмены регистрации Push-сервиса

| API | Описание |
| --- | --- |
| [registerPush](#registerPush) | Регистрация Push-сервиса, опционально переопределение информации push из параметра JSON интерфейса. |
| [unRegisterPush](#unRegisterPush) | Отмена регистрации Push-сервиса. |
| [setRegistrationID](#setRegistrationID) | RegistrationID — это уникальный идентификатор устройства получения push. По умолчанию этот ID автоматически генерируется при успешной регистрации push-сервиса, но вы также можете установить его самостоятельно. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. Обратите внимание, что удаление и переустановка приложения на устройстве изменит RegistrationID, поэтому необходимо вызвать интерфейс setRegistrationID перед регистрацией push-сервиса. |
| [getRegistrationID](#setRegistrationID) | После успешной регистрации push-сервиса вы можете получить уникальный идентификатор устройства получения push, то есть RegistrationID, вызвав интерфейс getRegistrationID. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. |

### Интерфейс глобального прослушивания Push

| API | Описание |
| --- | --- |
| [addPushListener](#addPushListener) | Добавить слушатель Push. |
| [removePushListener](#removePushListener) | Удалить слушатель Push. |

### Интерфейс пользовательской конфигурации

| API | Описание |
| --- | --- |
| [forceUseFCMPushChannel](#forceUseFCMPushChannel) | Указать использование канала FCM для оффлайн-push на устройстве. Это должно быть вызвано перед регистрацией push-сервиса. |
| [disablePostNotificationInForeground](#disablePostNotificationInForeground) | Отключить уведомление в панели уведомлений, когда приложение находится на переднем плане. |

## Подробное описание интерфейсов

### Класс плагина Push

TencentCloudChatPush(): получить экземпляр плагина TencentCloudChatPush, который является статическим синглтоном. Последующие шаги выполняются через этот экземпляр синглтона для вызовов методов.

### Описание функций-членов

#### registerPush

Регистрация Push-сервиса, должна быть вызвана после успешного входа в аккаунт Chat.

**Пример кода:**

```
void _onNotificationClicked({required String ext, String? userID, String? groupID}) {  print("_onNotificationClicked: $ext, userID: $userID, groupID: $groupID");  /// Custom Processing}TencentCloudChatPush().registerPush(    onNotificationClicked: _onNotificationClicked,    sdkAppId: Your sdkAppId,    appKey: "client key",    apnsCertificateID: Your configured Certificate ID);
```

**Описание параметров:**

| Параметр |  | Тип | Описание |  |
| --- | --- | --- | --- | --- |
| onNotificationClicked | ext | String | Полная информация ext, передаваемая сообщением, указывается отправителем. Если не указано, используется значение по умолчанию. Вы можете анализировать это поле для навигации на соответствующую страницу. |  |
|  | userID | String? | Этот параметр соответствует userID. Автоматически пытается разобрать строку ext JSON для получения userID другой стороны в одиночном чате.**Примечание:** Если вы не настроили поле ext, которое указано SDK или UIKit по умолчанию, вы можете использовать здесь разбор по умолчанию. Если попытка разбора не удалась, значение будет null. |  |
|  | groupID | String? | Этот параметр соответствует groupID. Автоматически пытается разобрать строку ext JSON для получения информации groupID для групповых чатов.**Примечание:** Если вы не настроили поле ext, которое указано SDK или UIKit по умолчанию, вы можете использовать здесь разбор по умолчанию. Если попытка разбора не удалась, значение будет null. |  |
| sdkAppId |  | int? | ID приложения, присвоенный вам консолью Chat | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7061099c2b311efb44452540044a08e.png) |
| appKey |  | String? | Ключ клиента, присвоенный вам консолью Chat |  |
| apnsCertificateID |  | int? | Этот элемент можно опустить, если метод setApnsCertificateID уже был отдельно настроен. |  |

#### unRegisterPush

Отмена регистрации сервиса оффлайн-push.

**Пример кода:**

```
TencentCloudChatPush().unRegisterPush();
```

#### setRegistrationID

Установить ID push, используемый для регистрации сервиса оффлайн-push, то есть RegistrationID, который должен быть вызван перед регистрацией push-сервиса.

Описание параметра:

| Параметр | Описание |
| --- | --- |
| registrationID | ID push устройства, который изменится после удаления и переустановки. |

**Пример кода:**

```
TencentCloudChatPush().setRegistrationID(registrationID: registrationID);
```

#### getRegistrationID

После успешной регистрации сервиса оффлайн-push получить ID push, то есть RegistrationID.

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

Указать использование канала FCM для оффлайн-push на устройстве. Это должно быть вызвано перед регистрацией push-сервиса.

Описание параметра:

| Параметр | Описание |
| --- | --- |
| enable | true: использовать канал FCM.false: использовать встроенный канал. |

**Пример кода:**

```
TencentCloudChatPush.forceUseFCMPushChannel(enable: true);
```

#### disablePostNotificationInForeground

Отключить всплывающие уведомления в панели уведомлений, когда приложение находится на переднем плане. Когда Push SDK получает онлайн-push, он автоматически добавит уведомление в панель уведомлений. Если вы хотите самостоятельно обрабатывать сообщения онлайн-push, вы можете вызвать этот интерфейс для отключения функции автоматического всплывающего уведомления.

Описание параметра:

| Параметр | Описание |
| --- | --- |
| disable | true: отключитьfalse: включить |

**Пример кода:**

```
TencentCloudChatPush.disablePostNotificationInForeground(disable: true);
```


---
*Источник: [https://trtc.io/document/60559](https://trtc.io/document/60559)*

---
*Источник (EN): [flutter.md](./flutter.md)*
