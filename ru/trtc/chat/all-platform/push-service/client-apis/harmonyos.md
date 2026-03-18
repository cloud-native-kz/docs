# HarmonyOS

## Обзор API TIMPushManager

| API | Описание |
| --- | --- |
| ``[registerPush](#c624c0f8-1505-4d15-8a44-dcacbaaac784) | Зарегистрировать сервис push-уведомлений (используйте этот API для push-сервиса только после получения согласия пользователя на политику конфиденциальности). |
| ``[unRegisterPush](#a6df0ca4-f85e-4678-8db4-1498fb67606b) | Отменить регистрацию и отключить сервис push-уведомлений. |
| ``[setRegistrationID](#e54d1228-3bc5-4053-bb2a-c72d3320c7db) | RegistrationID — это уникальный идентификатор устройства получения push-уведомлений. По умолчанию он генерируется системой при успешной регистрации сервиса push. Вы также можете установить пользовательский ID регистрации. На основе RegistrationID вы можете отправлять push-сообщения на указанные устройства. Обратите внимание, что удаление и переустановка приложения на устройстве изменят RegistrationID, поэтому необходимо вызвать API setRegistrationID перед регистрацией сервиса push. |
| ``[getRegistrationID](#2557dabd-b043-4f66-bb82-34315459c8b7) | После успешной регистрации сервиса push вызовите этот API, чтобы получить уникальный идентификатор устройства получения push-уведомлений, то есть RegistrationID. |
| ``[addPushListener](#8efda8f7-f11e-40d3-a9ee-9c2fbad7f63e) | Добавить слушателя Push. |
| ``[removePushListener](#4ee794ce-67d1-4b96-b7a5-bffe18f6d521) | Удалить слушателя Push. |
| ``[disablePostNotificationInForeground](#f8fe8ed3-ce77-4241-9eb1-3fe7e0ba16d2) | Включить/отключить уведомления в строке уведомлений, когда приложение находится на переднем плане (по умолчанию: включено). |

## Описание API

### Регистрация сервиса push-уведомлений

#### API

```
registerPush(  context: Context,  sdkAppId?: number,  appKey?: string,  businessId?: number): Promise<TIMPushResult>;
```

#### Описание параметров:

| Параметр | Тип | Описание | Путь доступа |
| --- | --- | --- | --- |
| context | Context | контекст приложения | - |
| sdkAppId | number | SDKAppID сервиса push-уведомлений. |  [Chat > Push > Access Settings](https://console.trtc.io/chat/push-plugin-push-identifier) страница![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f26442447da211f0bda35254007c27c5.png) |
| appKey | String | ключ клиента сервиса push-уведомлений. |  |
| businessId | number | ID сертификата, назначенный в консоли Chat. | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f266771e7da211f080fb5254005ef0f7.png) |

### Отмена регистрации и отключение сервиса push-уведомлений

#### API

```
unRegisterPush(): Promise<TIMPushResult>;
```

### Установка идентификатора RegistrationID для push-уведомлений

> **Примечание:** Если вы вызываете этот API, убедитесь, что вы вызываете его перед `registerPush`.

#### API

```
setRegistrationID(registrationID: string): Promise<TIMPushResult>;
```

#### Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| registrationID | String | Пользовательский идентификатор push-уведомлений. |

### Получение идентификатора RegistrationID для push-уведомлений

> **Примечание:** Если вы вызвали API `setRegistrationID` для установки идентификатора, этот API вернет установленный вами идентификатор. В противном случае он вернет случайное значение, сгенерированное SDK Push.

#### API

```
getRegistrationID(): Promise<TIMPushResult>;
```

### Добавление слушателя Push

#### API

```
addPushListener(listener: TIMPushListener): void;
```

#### Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| listener | [TIMPushListener](#cff83260-e519-4071-b968-e427b2517ff1) | метод обработки событий push |

### Удаление слушателя Push

#### API

```
removePushListener(listener: TIMPushListener): void;
```

#### Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| listener | [TIMPushListener](#cff83260-e519-4071-b968-e427b2517ff1) | метод обработки событий push |

### Включение/отключение уведомлений в строке уведомлений, когда приложение находится на переднем плане

#### API

```
disablePostNotificationInForeground(disable: boolean): void;
```

#### Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| disable | boolean | Включить/отключить уведомления в строке уведомлений, когда приложение находится на переднем плане (по умолчанию: отключено). Отключить уведомления в строке уведомлений, когда приложение находится на переднем плане. false: Включить уведомления в строке уведомлений, когда приложение находится на переднем плане. |

## Обзор API TIMPushListener

| API | Описание |
| --- | --- |
| onRecvPushMessage | Получено push-сообщение. |
| onRevokePushMessage | Получено уведомление об отзыве push-сообщения. |
| onNotificationClicked | Вебхук нажатия на сообщение в строке уведомлений. |

### Описание API

#### Описание функций-членов

##### onMessageReceived(message: TIMPushMessage): void;

Получено push-сообщение. Получено сообщение.

##### onRevokePushMessage(messageID: string): void;

Получено уведомление об отзыве push-сообщения с уникальным идентификатором сообщения messageID.

##### onNotificationClicked(ext: string): void;

Вебхук нажатия на сообщение в строке уведомлений.

## Обзор API TIMPushResult

| Поле | Описание | Тип |
| --- | --- | --- |
| code | Код ошибки | number |
| message | Описание ошибки | string |
| data | Возвращаемые значения | unknown |


---
*Источник: [https://trtc.io/document/72702](https://trtc.io/document/72702)*

---
*Источник (EN): [harmonyos.md](./harmonyos.md)*
