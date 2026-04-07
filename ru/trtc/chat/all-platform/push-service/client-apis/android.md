# Android

## TIMPush - TIMPushManager

public abstract class TIMPushManager: Интерфейсный класс плагина Push.

### Обзор API

#### Интерфейс регистрации/отмены регистрации сервиса Push

| API | Описание |
| --- | --- |
| [registerPush](https://www.tencentcloud.com/document/product/1047/60557#registerPush) | Регистрация сервиса Push. Информация push читается из файла конфигурации timpush-configs.json в проекте (этот интерфейс должен быть вызван после того, как пользователь приложения согласился с политикой конфиденциальности для использования сервиса push). |
| [unRegisterPush](https://www.tencentcloud.com/document/product/1047/60557#unRegisterPush) | Отмена регистрации и отключение сервиса push. |
| [setRegistrationID](https://www.tencentcloud.com/document/product/1047/60557#setRegistrationID) | RegistrationID — это уникальный идентификационный номер устройства-получателя push. По умолчанию этот идентификатор автоматически генерируется при успешной регистрации сервиса push, но вы также можете настроить его вручную. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. Обратите внимание, что удаление и переустановка приложения изменит RegistrationID, поэтому необходимо вызвать интерфейс setRegistrationID перед регистрацией сервиса push. |
| [getRegistrationID](https://www.tencentcloud.com/document/product/1047/60557#getRegistrationID) | После успешной регистрации сервиса push вы можете получить уникальный идентификационный номер устройства-получателя push, то есть RegistrationID, вызвав интерфейс getRegistrationID. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. |

#### Интерфейс глобального прослушивания Push

| API | Описание |
| --- | --- |
| [addPushListener](https://www.tencentcloud.com/document/product/1047/60557#addPushListener) | Добавить слушатель Push. |
| [removePushListener](https://www.tencentcloud.com/document/product/1047/60557#removePushListener) | Удалить слушатель Push. |

#### Интерфейс пользовательской конфигурации

| API | Описание |
| --- | --- |
| [forceUseFCMPushChannel](https://www.tencentcloud.com/document/product/1047/60557#forceUseFCMPushChannel) | Указать, что автономный push должен использовать канал FCM для устройства. Это должно быть вызвано перед регистрацией сервиса push. |
| [disablePostNotificationInForeground](https://www.tencentcloud.com/document/product/1047/60557#disablePostNotificationInForeground) | Отключить уведомление в строке состояния, когда приложение находится на переднем плане. |

### Описание интерфейса

#### Статические открытые функции-члены

static TIMPushManager getInstance(): Получает экземпляр менеджера TIMPushManager.

#### Описание функций-членов

##### abstract void registerPush(Context context, int sdkAppId, String appKey, TIMPushCallback callback)

Регистрация сервиса Push. Пожалуйста, правильно передайте параметры sdkAppId и appKey для регистрации сервиса push.

Описание параметров:

| Параметр | Описание | Путь получения |
| --- | --- | --- |
| sdkAppId | Идентификатор приложения, выданный вам консолью Chat. | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f235d333c36e11efad4f52540044a08e.png) |
| appKey | Ключ клиента, выданный вам консолью Chat. |  |

##### abstract void unRegisterPush(TIMPushCallback callback)

Отмена регистрации и отключение сервиса push.

##### abstract void setRegistrationID(String registrationID, TIMPushCallback callback)

Установить идентификатор push ID, используемый для регистрации сервиса push, т.е. RegistrationID, который должен быть вызван перед регистрацией сервиса push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| registrationID | Уникальный идентификатор для push-уведомлений на устройстве, который может измениться при удалении и переустановке. |

##### abstract void getRegistrationID(TIMPushCallback callback)

После успешной регистрации в сервисе push получите идентификатор push ID, т.е. RegistrationID.

##### abstract void addPushListener([TIMPushListener](#TIMPushListener) listener)

Добавить слушатель Push

##### abstract void removePushListener([TIMPushListener](#TIMPushListener) listener)

Удалить слушатель Push

##### abstract void forceUseFCMPushChannel(boolean enable)

Указать, что автономный push должен использовать канал FCM для устройства. Это должно быть вызвано перед регистрацией сервиса push.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| enable | true: использовать канал FCM. false: использовать собственный канал. |

##### abstract void disablePostNotificationInForeground(boolean disable)

Отключить всплывающие уведомления в строке состояния, когда приложение находится на переднем плане. Когда SDK Push получает онлайн-Push, он автоматически добавляет уведомление в строку состояния. Если вы хотите обрабатывать онлайн-Push сообщения самостоятельно, вы можете вызвать этот интерфейс для отключения функции автоматического всплывающего уведомления в строке состояния.

Описание параметров:

| Параметр | Описание |
| --- | --- |
| disable | true: отключить. false: включить |

## TIMPush - TIMPushListener

public abstract class TIMPushListener: Класс слушателя Push

### Обзор API

| API | Описание |
| --- | --- |
| onRecvPushMessage | Получено Push сообщение. |
| onRevokePushMessage | Получено уведомление об отзыве Push сообщения. |
| onNotificationClicked | Обратный вызов при клике на сообщение в строке состояния. |

### Описание интерфейса

#### Описание функций-членов

##### void onRecvPushMessage(TIMPushMessage message)

Получено Push сообщение, содержание сообщения.

##### void onRevokePushMessage(String messageID)

Получено уведомление об отзыве Push сообщения. messageID уникально идентифицирует сообщение.

##### void onNotificationClicked(String ext)

Обратный вызов при клике на сообщение в строке состояния.

> **Примечание:** Сертификат push в консоли должен быть настроен как "открыть определенный интерфейс внутри приложения" и использовать значение заполнения по умолчанию, чтобы вступить в силу.


---
*Источник: [https://trtc.io/document/60557](https://trtc.io/document/60557)*

---
*Источник (EN): [android.md](./android.md)*
