# Клиентские API

## TIMPush - TIMPushManager

@interface TIMPushManager : NSObject  :Класс интерфейса Push Plugin.

### Обзор API

#### Интерфейсы регистрации/отмены регистрации Push Service

| API | Описание |
| --- | --- |
| [registerPush](#registerPush) | Регистрация Push Service (должна быть вызвана после того, как пользователь приложения согласился с политикой конфиденциальности для использования push-сервиса). |
| [unRegisterPush](#unRegisterPush) | Отмена регистрации и отключение push-сервиса. |
| [setRegistrationID](#setRegistrationID) | RegistrationID — это уникальный идентификатор устройства, получающего push-уведомления. По умолчанию этот ID автоматически генерируется при успешной регистрации push-сервиса, но вы также можете настроить его вручную. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. Обратите внимание, что при удалении и переустановке приложения RegistrationID изменится, поэтому необходимо вызвать интерфейс setRegistrationID перед регистрацией push-сервиса. |
| [getRegistrationID](#getRegistrationID) | После успешной регистрации push-сервиса вы можете получить уникальный идентификатор устройства, получающего push-уведомления, то есть RegistrationID, вызвав интерфейс getRegistrationID. Вы можете отправлять сообщения на указанное устройство на основе RegistrationID. |

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

### Статистика по коэффициенту доставки Push в TIMPush

Если вам нужно отслеживать данные доставки и клика push-уведомлений, необходимо активно вызвать эту функцию в Notification Service Extension.

| API | Описание |
| --- | --- |
| [handleNotificationServiceRequest:appGroupID:callback:](#handleNotificationServiceRequest) | Поддерживает вызов только в методе '- didReceiveNotificationRequest:withContentHandler:' Notification Service Extension. AppGroupID идентифицирует App Group, общую для основного приложения и Extension. Необходимо настроить в возможности App Groups основного приложения. |

### Описание интерфейсов

#### Описание функции

##### + (void)registerPush:(int) sdkAppId appKey:(NSString *) appKey succ:(TIMPushSuccessCallback) successCallback fail:(TIMPushFailedCallback) failedCallback;

Регистрация Push Service. Пожалуйста, правильно передайте параметры sdkAppId и appKey для регистрации push-сервиса.

- Описание параметров:

| Параметр | Описание | Путь получения |
| --- | --- | --- |
| sdkAppId | ID приложения, назначенный вам консолью Chat. | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f1c6c46bc37411efb54a52540099c741.png) |
| appKey | Ключ клиента, назначенный вам консолью Chat. |  |

- Пример кода:

```
 const int sdkAppId = your sdkAppId; static const NSString *appKey = @"Client Key"; [TIMPushManager registerPush:sdkAppId appKey:appKey succ:^(NSData * _Nonnull deviceToken) {     //   } fail:^(int code, NSString * _Nonnull desc) {    //error }];
```

##### + (void)unRegisterPush:(TIMPushCallback) successCallback fail:(TIMPushFailedCallback) failedCallback;

Отмена регистрации и отключение push-сервиса

- Пример кода:

```
 [TIMPushManager unRegisterPush:^{      //success    } fail:^(int code, NSString * _Nonnull desc) {      //error  }];
```

##### + (void)setRegistrationID:(NSString *)registrationID callback: (TIMPushCallback) callback;

Установить идентификатор push ID, используемый для регистрации push-сервиса, то есть RegistrationID, который необходимо вызвать перед регистрацией push-сервиса.

- Описание параметров:

| Параметр | Описание |
| --- | --- |
| registrationID | Push ID устройства, который изменится после удаления и переустановки. |

##### + (void)getRegistrationID:(TIMPushValueCallback) callback;

После успешной регистрации push-сервиса получить идентификатор push ID, то есть RegistrationID.

##### + (void)addPushListener:(id<TIMPushListener>)listener

Добавить слушатель Push.

##### + (void)removePushListener:(id<TIMPushListener>)listener

Удалить слушатель Push.

##### + (void)disablePostNotificationInForeground:(BOOL)disable;

Отключить всплывающие окна строки уведомлений, когда приложение находится на переднем плане. Когда Push SDK получает онлайн-push, он автоматически добавляет уведомление в строку уведомлений. Если вы хотите обрабатывать онлайн-push сообщения самостоятельно, вы можете вызвать этот интерфейс, чтобы отключить функцию автоматического всплывающего окна строки уведомлений.

- Описание параметров:

| Параметр | Описание |
| --- | --- |
| disable | true: закрыто, false: открыто |

##### + (void)handleNotificationServiceRequest:(UNNotificationRequest *)request appGroupID:(NSString *)appGroupID callback:(TIMPushNotificationExtensionCallback)callback

Статистика по коэффициенту доставки Push в TIMPush

1. Необходимо реализовать метод `- applicationGroupID` в файле AppDelegate.m, возвращающий ID App Group.
2. И вызвать эту функцию в методе '- didReceiveNotificationRequest:withContentHandler:' Notification Service Extension.

> **Примечание:**AppGroupID идентифицирует App Group, общую для основного приложения и Extension. Необходимо настроить в возможности App Groups основного приложения.

- Описание параметров:

| request | [Параметры, передаваемые обратным вызовом UNNotificationServiceExtension](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension/1648229-didreceivenotificationrequest) |
| --- | --- |
| appGroupID | AppGroupID идентифицирует App Group, общую для основного приложения и Extension. Необходимо настроить в возможности App Groups основного приложения. |
| callback | typedef void(^TIMPushNotificationExtensionCallback)(UNNotificationContent *content)  Обратный вызов функции статистики, несущей информацию о содержимом. |

- Пример кода:

```
@implementation NotificationService- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {    //AppGroupID идентифицирует App Group, общую для основного приложения и Extension. Необходимо настроить в возможности App Groups основного приложения.    //Формат: group + [mainBundleID] + key    //Например, group.com.tencent.im.pushkey    NSString * appGroupID = kTIMPushAppGorupKey;    __weak typeof(self) weakSelf = self;    [TIMPushManager handleNotificationServiceRequest:request appGroupID:appGroupID callback:^(UNNotificationContent *content) {        weakSelf.bestAttemptContent = [content mutableCopy];        // Измените содержимое уведомления здесь...        // self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]", self.bestAttemptContent.title];        weakSelf.contentHandler(weakSelf.bestAttemptContent);    }];}@end
```

## TIMPush - TIMPushListener

@protocol TIMPushListener <NSObject> :Протокол слушателя Push

### Обзор API

| API | Описание |
| --- | --- |
| onRecvPushMessage | Получено push-сообщение. |
| onRevokePushMessage | Получено уведомление об отзыве push-сообщения. |
| onNotificationClicked | Обратный вызов нажатия на сообщение в строке уведомлений |

### Описание интерфейсов

#### Описание функций-членов

##### - (void)onRecvPushMessage:(TIMPushMessage *)message;

Получено push-сообщение, содержимое сообщения.

##### - (void)onRevokePushMessage:(NSString *)messageID;

Получено уведомление об отзыве push-сообщения, messageID уникально идентифицирует сообщение.

##### - (void)onNotificationClicked:(NSString *)ext;

Обратный вызов нажатия на сообщение в строке уведомлений.


---
*Источник: [https://trtc.io/document/67574](https://trtc.io/document/67574)*

---
*Источник (EN): [client-apis.md](./client-apis.md)*
