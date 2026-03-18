# Unity

PushManager

public class PushManager: класс интерфейса плагина Push

### Обзор API

#### API регистрации/отмены регистрации сервиса Push

| API | Описание |
| --- | --- |
| [RegisterPush](#RegisterPush) | Регистрация сервиса push (API должен быть вызван для использования сервиса push после получения согласия пользователя на политику конфиденциальности). |
| [UnRegisterPush](#UnRegisterPush) | Отключение сервиса push. |
| [SetRegistrationID](#SetRegistrationID) | RegistrationID — это уникальный идентификатор устройства приёма push-уведомлений. По умолчанию он автоматически создаётся при успешной регистрации сервиса push. Вы также можете настроить параметры вручную. На основе RegistrationID вы можете отправлять сообщения на указанные устройства. Важно отметить, что удаление и переустановка устройства изменят RegistrationID, поэтому вам необходимо вызвать API setRegistrationID до регистрации сервиса push. |
| [GetRegistrationID](#GetRegistrationID) | После успешной регистрации сервиса push вы можете получить уникальный идентификационный номер устройства приёма push-уведомлений, то есть RegistrationID, путём вызова API getRegistrationID. На основе RegistrationID вы можете отправлять сообщения на указанные устройства. |

#### Интерфейс глобального прослушивания Push

| API | Описание |
| --- | --- |
| [AddPushListener](#AddPushListener) | Добавить слушатель Push. |
| [RemovePushListener](#RemovePushListener) | Удалить слушатель Push. |

#### API пользовательской конфигурации

| API | Описание |
| --- | --- |
| [ForceUseFCMPushChannel](#ForceUseFCMPushChannel) | Назначить канал офлайн-push устройства для использования канала FCM, необходимо зарегистрировать сервис push перед вызовом. |
| [DisablePostNotificationInForeground](#DisablePostNotificationInForeground) | Отключить всплывающие уведомления, когда приложение находится на переднем плане. |

### Описание API

#### Описание функций-членов

##### abstract void RegisterPush(Context context, int sdkAppId, String appKey, PushCallback callback)

Регистрация сервиса push. Просто передайте sdkAppId и appKey для завершения регистрации сервиса push.

Описание параметров:

| Параметр | Описание | Путь доступа |
| --- | --- | --- |
| sdkAppId | ID приложения, назначенный вам в консоли IM. | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/543aafe0a7e711f0bf2352540044a08e.png) |
| appKey | Ключ клиента, назначенный вам в консоли IM. |  |

##### abstract void UnRegisterPush(PushCallback callback)

Отмена регистрации и отключение сервиса push.

##### abstract void SetRegistrationID(String registrationID, PushCallback callback)

Установить ID push (RegistrationID), используемый для регистрации сервиса push, который должен быть вызван до регистрации сервиса push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| registrationID | Уникальный идентификационный номер push устройства изменится после удаления и переустановки. |

##### abstract void GetRegistrationID(PushCallback callback)

После успешной регистрации сервиса push получить ID push (RegistrationID).

##### abstract void AddPushListener([PushListener](#PushListener) listener)

Добавить слушатель Push.

##### abstract void RemovePushListener([PushListener](#PushListener) listener)

Удалить слушатель Push

##### abstract void ForceUseFCMPushChannel(boolean enable)

Назначить канал офлайн-push устройства для использования канала FCM, необходимо зарегистрировать сервис push перед вызовом.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| enable | true: использовать канал FCM. false: использовать локальный канал устройства. |

##### abstract void DisablePostNotificationInForeground(boolean disable)

Отключить строку уведомлений на панели при нахождении приложения на переднем плане. Когда Push SDK получает онлайн push, он автоматически добавляет уведомление на панель уведомлений. Если вы хотите обработать онлайн push-сообщение самостоятельно, вы можете вызвать этот API для отключения функции автоматического всплывания строки уведомлений.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| disable | true: отключено. false: включено |

## PushListener

public class PushListener: класс слушателя Push

### Обзор API

| API | Описание |
| --- | --- |
| onRecvPushMessage | Получено push-сообщение. |
| onRevokePushMessage | Получено уведомление об отзыве push-сообщения. |
| onNotificationClicked | Webhook нажатия на сообщение на панели уведомлений. |

### Описание API

#### Описание функций-членов

##### void onRecvPushMessage(TIMPushMessage message)

Получено push-сообщение. Получено сообщение.

##### void onRevokePushMessage(string messageID)

Получено уведомление об отзыве push-сообщения, messageID — уникальный идентификатор сообщения.

##### void onNotificationClicked(String ext)

Webhook нажатия на сообщение на панели уведомлений.

> **Примечание:** Настройте сертификат Push в консоли на "открыть указанную страницу в приложении" и используйте значение, заполненное по умолчанию, чтобы это вступило в силу.


---
*Источник: [https://trtc.io/document/73935](https://trtc.io/document/73935)*

---
*Источник (EN): [unity.md](./unity.md)*
