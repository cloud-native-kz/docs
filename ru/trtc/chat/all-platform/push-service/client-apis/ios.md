# iOS

## TIMPush - TIMPushManager

@interface TIMPushManager : NSObject  : Класс интерфейса Push Plugin.

### Обзор API

#### Интерфейсы регистрации/отмены регистрации сервиса Push

| API | Описание |
| --- | --- |
| [registerPush](#registerPush) | Регистрация сервиса Push (должна быть вызвана после того, как пользователь приложения согласился с политикой конфиденциальности для использования сервиса push). |
| [unRegisterPush](#unRegisterPush) | Отмена регистрации и отключение сервиса push. |
| [setRegistrationID](#setRegistrationID) | RegistrationID — это уникальный идентификатор устройства, получающего push-уведомления. По умолчанию этот ID автоматически генерируется при успешной регистрации сервиса push, но вы также можете настроить его вручную. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. Обратите внимание, что переустановка приложения изменит RegistrationID, поэтому необходимо вызвать интерфейс setRegistrationID перед регистрацией сервиса push. |
| [getRegistrationID](#getRegistrationID) | После успешной регистрации сервиса push вы можете получить уникальный идентификатор устройства, получающего push-уведомления, то есть RegistrationID, вызвав интерфейс getRegistrationID. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. |

#### Интерфейс глобального прослушивания Push

| API | Описание |
| --- | --- |
| [addPushListener](#addPushListener) | Добавить слушатель Push. |
| [removePushListener](#removePushListener) | Удалить слушатель Push. |

#### Интерфейс пользовательской конфигурации

Установка отображения push-уведомлений на переднем плане приложения

| API | Описание |
| --- | --- |
| [disablePostNotificationInForeground](#disablePostNotificationInForeground) | Отключить строку уведомлений, когда приложение находится на переднем плане. |

### Статистика процента доставки Push от TIMPush

Если вам необходимо отслеживать данные доставки и клика push, необходимо активно вызвать эту функцию в Notification Service Extension.

| API | Описание |
| --- | --- |
| [handleNotificationServiceRequest:appGroupID:callback:](#handleNotificationServiceRequest) | Поддерживается только вызов в методе `- didReceiveNotificationRequest:withContentHandler:` Notification Service Extension. appGroup определяет App Group, общую для основного приложения и Extension. Необходимо настроить его в возможности App Groups основного приложения. |

### Детальное описание интерфейсов

#### Описание функции

##### + (void)registerPush:(int) sdkAppId appKey:(NSString *) appKey succ:(TIMPushSuccessCallback) successCallback fail:(TIMPushFailedCallback) failedCallback;

Регистрация сервиса Push. Пожалуйста, корректно передайте параметры sdkAppId и appKey для регистрации сервиса push.

- Описание параметров:

| Параметр | Описание | Путь получения |
| --- | --- | --- |
| sdkAppId | ID приложения, назначенный вам консолью Chat. | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bc8f5122c36c11ef85bd525400454e06.png) |
| appKey | Клиентский ключ, назначенный вам консолью Chat. |  |

- Пример кода:

```
 const int sdkAppId = your sdkAppId; static const NSString *appKey = @"Client Key"; [TIMPushManager registerPush:sdkAppId appKey:appKey succ:^(NSData * _Nonnull deviceToken) {     //   } fail:^(int code, NSString * _Nonnull desc) {    //error }];
```

##### + (void)unRegisterPush:(TIMPushCallback) successCallback fail:(TIMPushFailedCallback) failedCallback;

Отмена регистрации и отключение сервиса push

- Пример кода:

```
 [TIMPushManager unRegisterPush:^{      //success    } fail:^(int code, NSString * _Nonnull desc) {      //error  }];
```

##### + (void)setRegistrationID:(NSString *)registrationID callback: (TIMPushCallback) callback;

Установить идентификатор push ID, используемый для регистрации сервиса push, то есть RegistrationID, который необходимо вызвать перед регистрацией сервиса push.

- Описание параметров:

| Параметр | Описание |
| --- | --- |
| registrationID | ID идентификатора push устройства изменится при переустановке. |

##### + (void)getRegistrationID:(TIMPushValueCallback) callback;

После успешной регистрации сервиса push получить идентификатор push ID, то есть RegistrationID.

##### + (void)addPushListener:(id<TIMPushListener>)listener

Добавить слушатель Push.

##### + (void)removePushListener:(id<TIMPushListener>)listener

Удалить слушатель Push.

##### + (void)disablePostNotificationInForeground:(BOOL)disable;

Отключить всплывающие окна строки уведомлений, когда приложение находится на переднем плане. Когда Push SDK получает online Push, он автоматически добавит уведомление в строку уведомлений. Если вы хотите обрабатывать online Push сообщения самостоятельно, вы можете вызвать этот интерфейс для отключения функции автоматического всплывания уведомлений.

- Описание параметров:

| Параметр | Описание |
| --- | --- |
| disable | true: отключить; false: включить |

##### + (void)handleNotificationServiceRequest:(UNNotificationRequest *)request appGroupID:(NSString *)appGroupID callback:(TIMPushNotificationExtensionCallback)callback

Статистика процента доставки Push от TIMPush

1. Необходимо реализовать метод `- applicationGroupID` в файле AppDelegate.m, возвращающий App Group ID.
2. И вызвать эту функцию в методе `- didReceiveNotificationRequest:withContentHandler:` Notification Service Extension.

> **Примечание:** appGroup определяет App Group, общую для основного приложения и Extension. Необходимо настроить его в возможности App Groups основного приложения.

- Описание параметров:

| request | [Параметры, переданные обратным вызовом UNNotificationServiceExtension](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension/1648229-didreceivenotificationrequest) |
| --- | --- |
| appGroupID | appGroup определяет App Group, общую для основного приложения и Extension. Необходимо настроить его в возможности App Groups основного приложения. |
| callback | typedef void(^TIMPushNotificationExtensionCallback)(UNNotificationContent *content) Обратный вызов функции статистики, содержащий информацию контента |

- Пример кода:

```
@implementation NotificationService- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {    //appGroup определяет App Group, общую для основного приложения и Extension. Необходимо настроить его в возможности App Groups основного приложения.    //Формат: group + [mainBundleID] + key    //Например, group.com.tencent.im.pushkey    NSString * appGroupID = kTIMPushAppGorupKey;    __weak typeof(self) weakSelf = self;    [TIMPushManager handleNotificationServiceRequest:request appGroupID:appGroupID callback:^(UNNotificationContent *content) {        weakSelf.bestAttemptContent = [content mutableCopy];        // Modify the notification content here...        // self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]", self.bestAttemptContent.title];        weakSelf.contentHandler(weakSelf.bestAttemptContent);    }];}@end
```

## TIMPush - TIMPushListener

@protocol TIMPushListener <NSObject> : Протокол слушателя Push

### Обзор API

| API | Описание |
| --- | --- |
| onRecvPushMessage | Получено сообщение Push |
| onRevokePushMessage | Получено уведомление об отзыве сообщения Push |
| onNotificationClicked | Обратный вызов клика на сообщение в строке уведомлений |

### Детальное описание интерфейсов

#### Описание функции-члена

##### - (void)onRecvPushMessage:(TIMPushMessage *)message;

Получено сообщение Push, содержимое сообщения.

##### - (void)onRevokePushMessage:(NSString *)messageID;

Получено уведомление об отзыве сообщения Push, messageID уникально идентифицирует сообщение.

##### - (void)onNotificationClicked:(NSString *)ext;

Обратный вызов клика на сообщение в строке уведомлений.


---
*Источник: [https://trtc.io/document/60558](https://trtc.io/document/60558)*

---
*Источник (EN): [ios.md](./ios.md)*
