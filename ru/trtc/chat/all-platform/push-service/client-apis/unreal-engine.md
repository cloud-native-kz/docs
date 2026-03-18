# Unreal Engine

## TIMPush - PushManager

PushManager: класс интерфейса подключаемого модуля Push

### Обзор API

#### API регистрации/отмены регистрации сервиса Push

| API | Описание |
| --- | --- |
| [RegisterPush](#RegisterPush) | Зарегистрировать сервис push (этот API необходимо вызвать для использования сервиса push только после согласия пользователя приложения с политикой конфиденциальности). |
| [UnRegisterPush](#UnRegisterPush) | Отключить сервис push. |
| [SetRegistrationID](#SetRegistrationID) | RegistrationID — это уникальный идентификатор устройства получения push. По умолчанию он автоматически генерируется при успешной регистрации сервиса push, и вы также можете настроить параметры вручную. На основе RegistrationID вы можете отправлять сообщения на указанное устройство. Заметьте, что удаление и переустановка приложения изменят RegistrationID, поэтому необходимо вызвать API setRegistrationID перед регистрацией сервиса push. |
| [GetRegistrationID](#GetRegistrationID) | После успешной регистрации сервиса push вы можете получить уникальный идентификационный номер устройства получения push, то есть RegistrationID, вызвав API getRegistrationID. На основе RegistrationID вы можете отправлять сообщения на указанное устройство. |

#### Глобальный интерфейс прослушивания для Push

| API | Описание |
| --- | --- |
| [AddPushListener](#AddPushListener) | Добавить слушатель Push. |
| [RemovePushListener](#RemovePushListener) | Удалить слушатель Push. |

#### API пользовательской конфигурации

| API | Описание |
| --- | --- |
| [ForceUseFCMPushChannel](#ForceUseFCMPushChannel) | Указать, что push устройства в режиме offline должен использовать канал FCM, необходимо зарегистрировать сервис push перед вызовом. |
| [DisablePostNotificationInForeground](#DisablePostNotificationInForeground) | Отключить всплывающие уведомления, когда приложение находится в foreground. |

### Детали API

#### Статическая открытая функция-член

static PushManager* GetInstance(): Получить экземпляр менеджера PushManager.

#### Описание функций-членов

##### virtual void RegisterPush(int sdkAppId, const FString& appKey, PushValueCallback<FString>* callback) = 0;

Зарегистрировать сервис push, передав оба параметра sdkAppId и appKey, и просто зарегистрировать сервис push.

Описание параметров:

| Параметр | Описание | Путь доступа |
| --- | --- | --- |
| sdkAppId | ID приложения, назначенный вам консолью IM. | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6379c346a7e711f0bf2352540044a08e.png) |
| appKey | Ключ клиента, назначенный вам консолью IM. |  |

##### virtual void UnRegisterPush(PushCallback* callback) = 0;

Отменить регистрацию и отключить сервис push.

##### virtual void SetRegistrationID(const FString& registrationID, PushCallback* callback) = 0;

Установить флаг ID push, используемый для регистрации сервиса push, то есть RegistrationID, который необходимо вызвать перед регистрацией сервиса push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| registrationID | Уникальный идентификационный номер push устройства может измениться после удаления и переустановки. |

##### virtual void GetRegistrationID(PushValueCallback<FString>* callback) = 0;

После успешной регистрации сервиса push получить флаг ID push, то есть RegistrationID.

##### virtual void AddPushListener(PushListener* listener) = 0;

Добавить слушатель Push

##### virtual void RemovePushListener(PushListener* listener) = 0;

Удалить слушатель Push

##### virtual void ForceUseFCMPushChannel(bool enable) = 0;

Указать, что push устройства в режиме offline должен использовать канал FCM, необходимо зарегистрировать сервис push перед вызовом.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| enable | true: Использовать канал FCM. false: Использовать локальный канал устройства. |

##### virtual void DisablePostNotificationInForeground(bool disable) = 0;

Отключить всплывающие уведомления в строке уведомлений, когда приложение находится в foreground. Когда Push SDK получает online push, он автоматически добавляет подсказку уведомления в строку уведомлений. Если вы хотите обработать сообщения online push самостоятельно, вы можете вызвать этот API, чтобы отключить функцию автоматического всплывающего окна уведомлений.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| disable | true: Отключено. false: Включено. |

## PushListener

PushListener: класс слушателя Push

### Обзор API

| API | Описание |
| --- | --- |
| OnRecvPushMessage | Получено сообщение push. |
| OnRevokePushMessage | Получено уведомление об отзыве сообщения push. |
| OnNotificationClicked | Webhook нажатия на сообщение в строке уведомлений. |

### Детали API

#### Описание функций-членов

##### virtual void OnRecvPushMessage(const PushMessage& message) {}

Получено сообщение push. Сообщение получено.

##### virtual void OnRevokePushMessage(const FString& messageID) {}

Получено уведомление об отзыве сообщения push. messageID: уникальный идентификатор сообщения.

##### virtual void OnNotificationClicked(const FString& ext) {}

Webhook нажатия на сообщение в строке уведомлений.

> **Примечание:** Примечание: Push Certificate в консоли должен быть настроен на "открытие указанной страницы в приложении" и использование заполнения по умолчанию для вступления в силу.


---
*Источник: [https://trtc.io/document/73936](https://trtc.io/document/73936)*

---
*Источник (EN): [unreal-engine.md](./unreal-engine.md)*
