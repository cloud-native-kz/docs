# Клиентские API

## Обзор API

| API | Описание |
| --- | --- |
| `registerPush` | Регистрация для использования службы push-уведомлений (должна быть вызвана после того, как пользователь приложения согласится с Политикой конфиденциальности для использования службы push-уведомлений). |
| `unRegisterPush` | Отмена регистрации для отключения службы push-уведомлений. |
| `setRegistrationID` | Установка ID устройства для push-уведомлений. RegistrationID — это уникальный идентификатор устройства, получающего push-уведомления. По умолчанию этот ID автоматически генерируется при успешной регистрации службы push-уведомлений, но вы также можете установить его вручную. **Примечание! Если вы вызываете этот API, убедитесь, что вызвали его до**`registerPush`**.**Варианты использования: если вы интегрировали как службу Chat-сообщений, так и службу Push на устройстве, и предполагается, что ID пользователя Chat имеет значение "user123", если вы хотите отправить push-сообщения на "user123", вам нужно вызвать этот интерфейс, чтобы установить ID устройства следующим образом:`Push.setRegistrationID("user123", () => {});` |
| `getRegistrationID` | После успешной регистрации службы push-уведомлений вы можете вызвать этот интерфейс, чтобы получить уникальный идентификатор устройства, получающего push-уведомления, это RegistrationID. |
| `getNotificationExtInfo` | При получении offline push-уведомлений нажмите на строку уведомлений, чтобы открыть приложение, и вызовите этот интерфейс, чтобы получить информацию расширения push-уведомлений. |
| `addPushListener` | Добавить слушателя Push. |
| `removePushListener` | Удалить слушателя Push. |
| `disablePostNotificationInForeground` | Когда приложение находится на переднем плане, включить/отключить уведомления на панели уведомлений (по умолчанию включено). |
| `createNotificationChannel` | Создать канал уведомлений клиента. Этот API может реализовать функцию пользовательского рингтона на платформе Android. |

## Детали интерфейса

### Регистрация службы Push

#### API

```
registerPush(SDKAppID, appKey, onSuccess, onError)
```

#### Описание параметров:

| Параметры | Тип | Описание | Путь доступа |
| --- | --- | --- | --- |
| SDKAppID | Number | SDKAppID для Push Service Push. | [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier) ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6f1a39cec3ff11ef85bd525400454e06.png) |
| appKey | String | Ключ клиента для Push Service Push. |  |
| onSuccess | Function | Callback для успешной регистрации push-уведомлений. | - |
| onError | Function ï½undefined | Callback для неудачной регистрации push-уведомлений. | - |

### Отмена регистрации для отключения службы push-уведомлений

#### API

```
unRegisterPush(onSuccess, onError)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| onSuccess | Function | Callback для успешной отмены регистрации push-уведомлений. |
| onError | Function ï½undefined | Callback для неудачной отмены регистрации push-уведомлений. |

### Установка идентификатора push ID — RegistrationID

> **Примечание:** Если вы вызываете этот API, убедитесь, что вызвали его до `registerPush`.

#### API

```
setRegistrationID(registrationID, onSuccess)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| registrationID | String | Пользовательский идентификатор push ID. |
| onSuccess | Function | Callback после успешной установки пользовательского идентификатора push ID. |

### Получение идентификатора push ID — RegistrationID

> **Примечание:** Если вы вызвали интерфейс `setRegistrationID` для установки ID идентификатора, этот интерфейс вернёт установленный вами ID идентификатора, в противном случае он вернёт случайное значение, сгенерированное Push SDK.

#### API

```
getRegistrationID(onSuccess)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| onSuccess | Function | Callback для успешного получения push ID. |

### Получение информации расширения Push

#### API

```
getNotificationExtInfo(onSuccess)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| onSuccess | Function | Callback для успешного получения содержимого нажатого pass-through. |

### Добавление слушателя Push

#### API

```
addPushListener(eventName: string, listener: (data: any) => void);
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| eventName | String | Тип события Push. |
| listener | Function | Метод обработки события Push. |

### Удаление слушателя Push

#### API

```
removePushListener(eventName: string, listener?: (data: any) => void);
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| eventName | String | Тип события Push. |
| listener | Function \| undefined | Метод обработки события Push. |

### Включение/отключение уведомлений на панели уведомлений, когда приложение находится на переднем плане

#### API

```
disablePostNotificationInForeground(disable: boolean);
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| disable | boolean | Включение/отключение уведомлений на панели уведомлений, когда приложение находится на переднем плане. По умолчанию включено: true: отключить уведомления на панели уведомлений, когда приложение находится на переднем плане; false: включить уведомления на панели уведомлений, когда приложение находится на переднем плане |

### Создание канала уведомлений клиента

#### API

```
createNotificationChannel(options: any, onSuccess: (data: any) => void);
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| options.channelID | String | ID пользовательского канала. OPPO: channelID в [Console -> Access Configuration](https://console.trtc.io/chat/push-plugin-push-identifier). |
| options.channelName | String | Имя пользовательского канала. |
| options.channelDesc | String \| undefined | Описание пользовательского канала. |
| options.channelSound | String \| undefined | Тон оповещения пользовательского канала, имя аудиофайла без расширения. Аудиофайл должен быть размещён в `MyReactNativeApp/android/app/src/main/res/raw`. Например: `options.channelSound = private_ring`, который устанавливает `MyReactNativeApp/android/app/src/main/res/raw/private_ring.mp3` в качестве пользовательского тона оповещения. |
| onSuccess | Function | Функция обратного вызова для успешного вызова API. |


---
*Источник: [https://trtc.io/document/67585](https://trtc.io/document/67585)*

---
*Источник (EN): [client-apis.md](./client-apis.md)*
