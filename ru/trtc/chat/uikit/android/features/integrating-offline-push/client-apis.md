# Клиентские API

## TIMPush - TIMPushManager

public abstract class TIMPushManager: Интерфейс класса плагина Push.

### Обзор API

#### Интерфейсы регистрации/отмены регистрации в услуге Push

| API | Описание |
| --- | --- |
| [registerPush](#registerPush) | Зарегистрироваться в услуге push и прочитать файл конфигурации timpush-configs.json из проекта (Этот интерфейс можно использовать только после того, как пользователь приложения согласился с политикой конфиденциальности). |
| [unRegisterPush](#unRegisterPush) | Отменить регистрацию и отключить услугу push. |
| [setRegistrationID](#setRegistrationID) | RegistrationID — это уникальный идентификатор устройства, получающего push-уведомления. По умолчанию этот ID автоматически генерируется при успешной регистрации в услуге push, но вы также можете настроить его вручную. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. Обратите внимание, что переустановка приложения изменит RegistrationID, поэтому вам нужно вызвать интерфейс setRegistrationID перед регистрацией в услуге push. |
| [getRegistrationID](#getRegistrationID) | После успешной регистрации в услуге push вы можете получить уникальный идентификатор устройства, получающего push-уведомления, то есть RegistrationID, вызвав интерфейс getRegistrationID. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. |

#### Интерфейс глобального прослушивания Push

| API | Описание |
| --- | --- |
| [addPushListener](#addPushListener) | Добавить слушатель Push. |
| [removePushListener](#removePushListener) | Удалить слушатель Push. |

#### Интерфейс пользовательской конфигурации

| API | Описание |
| --- | --- |
| [forceUseFCMPushChannel](#forceUseFCMPushChannel) | Указать автономный push для использования канала FCM на устройстве. Это должно быть вызвано перед регистрацией в услуге push. |
| [disablePostNotificationInForeground](#aae128cb-d4c0-4e24-a5bb-9945dd7efbfa) | Отключить панель уведомлений, когда приложение находится на переднем плане. |

### Детали интерфейса

#### Статические открытые функции-члены

static TIMPushManager getInstance(): Получает экземпляр менеджера TIMPushManager.

#### Описание функции-члена

##### abstract void registerPush(Context context, int sdkAppId, String appKey, TIMPushCallback callback)

Зарегистрироваться в услуге автономного push: пожалуйста, правильно передайте параметры sdkAppId и appKey для регистрации в услуге push.

Примечание: Если вы уже интегрировали продукт Chat, пожалуйста, вызовите этот интерфейс после успешного входа в Chat. Установите параметр appKey в null, чтобы включить возможность автономного push.

Описание параметров:

| Параметр | Описание | Путь получения |
| --- | --- | --- |
| sdkAppId | ID приложения, назначенный вам консолью Chat. | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7f83398cc37411ef86f2525400bf7822.png) |
| appKey | Ключ клиента, назначенный вам консолью Chat. |  |

> **Примечание:** Вам нужно использовать API входа, предоставленный [TUILogin](https://github.com/TencentCloud/chat-uikit-android/blob/main/TUIKit/TUICore/tuicore/src/main/java/com/tencent/qcloud/tuicore/TUILogin.java) компонента TUICore для входа; плагин автоматически определит это и зарегистрирует услугу push. Если вы не хотите использовать API, предоставленный [TUILogin](https://github.com/TencentCloud/chat-uikit-android/blob/main/TUIKit/TUICore/tuicore/src/main/java/com/tencent/qcloud/tuicore/TUILogin.java), вам нужно вручную вызвать этот интерфейс для регистрации услуги после завершения операции входа.

##### abstract void unRegisterPush(TIMPushCallback callback)

Отменить регистрацию для закрытия услуг автономного push, вызовите перед выходом из учетной записи Chat.

> **Примечание:** Если вы не хотите использовать услугу push, вы можете вручную вызвать этот интерфейс для отмены регистрации услуги. Если вы выходите, используя API выхода, предоставленный [TUILogin](https://github.com/TencentCloud/chat-uikit-android/blob/main/TUIKit/TUICore/tuicore/src/main/java/com/tencent/qcloud/tuicore/TUILogin.java) компонента TUICore, плагин автоматически определит это и отменит регистрацию услуги push.

##### abstract void setRegistrationID(String registrationID, TIMPushCallback callback)

Установить идентификатор push ID, используемый для регистрации в услуге push, то есть RegistrationID, который необходимо вызвать перед регистрацией в услуге push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| registrationID | Уникальный ID для push-уведомлений на устройстве, который может измениться при переустановке. |

##### abstract void getRegistrationID(TIMPushCallback callback)

После успешной регистрации в услуге push получить идентификатор push ID, то есть RegistrationID.

##### abstract void addPushListener([TIMPushListener](#TIMPushListener) listener)

Добавить слушатель Push

##### abstract void removePushListener([TIMPushListener](#TIMPushListener) listener)

Удалить слушатель Push

##### abstract void forceUseFCMPushChannel(boolean enable)

Указать автономный push для использования канала FCM на устройстве. Это должно быть вызвано перед регистрацией в услуге push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| enable | true: Использовать канал FCM. false: Использовать встроенный канал. |

##### abstract void disablePostNotificationInForeground(boolean disable)

Отключить панель уведомлений, когда приложение находится на переднем плане, отключено по умолчанию.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| disable | true: отключить. false: включить. |

## TIMPush - TIMPushListener

public abstract class TIMPushListener: Класс слушателя Push

### Обзор API

| API | Описание |
| --- | --- |
| onRecvPushMessage | Получено сообщение Push. |
| onRevokePushMessage | Получено уведомление об отзыве сообщения Push. |
| onNotificationClicked | Обратный вызов при нажатии на сообщение в панели уведомлений. |

### Детали интерфейса

#### Описание функции-члена

##### void onRecvPushMessage(TIMPushMessage message)

Получено сообщение Push, содержание сообщения.

##### void onRevokePushMessage(String messageID)

Получено уведомление об отзыве сообщения Push, messageID уникально идентифицирует сообщение.

##### void onNotificationClicked(String ext)

Обратный вызов при нажатии на сообщение в панели уведомлений.

> **Примечание:** Сертификат push в консоли должен быть настроен как "открыть определенный интерфейс в приложении" и использовать значение по умолчанию, чтобы вступить в силу.


---
*Источник: [https://trtc.io/document/67571](https://trtc.io/document/67571)*

---
*Источник (EN): [client-apis.md](./client-apis.md)*
