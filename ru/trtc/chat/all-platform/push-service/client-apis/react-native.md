# React Native

## Обзор API

| API | Описание |
| --- | --- |
| `registerPush` | Регистрация для службы push-уведомлений (должна быть вызвана после согласия пользователя приложения с Политикой конфиденциальности для использования службы push-уведомлений). |
| `unRegisterPush` | Отмена регистрации для отключения службы push-уведомлений. |
| `setRegistrationID` | Установить ID устройства для Push-уведомлений. RegistrationID — это уникальный идентификационный номер устройства, получающего push-уведомления. По умолчанию этот ID автоматически генерируется при успешной регистрации в службе push-уведомлений, но вы также можете установить его вручную. **Важно! Если вы используете этот API, убедитесь, что вы вызываете его перед** `registerPush` **.**Примеры использования: если вы интегрировали как службу Chat-сообщений, так и службу Push-уведомлений на устройстве, и предполагается, что userID пользователя Chat имеет значение "user123", если вы хотите отправлять push-уведомления пользователю "user123", вам необходимо вызвать этот интерфейс для установки ID устройства следующим образом:`Push.setRegistrationID("user123", () => {});` |
| `getRegistrationID` | После успешной регистрации в службе push-уведомлений вы можете вызвать этот интерфейс для получения уникального идентификационного номера устройства, получающего push-уведомления, который является RegistrationID. |
| `getNotificationExtInfo` | При получении автономных push-уведомлений нажмите на уведомление в строке уведомлений, чтобы открыть приложение, и вызовите этот интерфейс для получения информации о расширении push-уведомления. |
| `addPushListener` | Добавить слушатель push-уведомлений. |
| `removePushListener` | Удалить слушатель push-уведомлений. |
| `disablePostNotificationInForeground` | Когда приложение находится в foreground, включить/отключить уведомления в строке уведомлений (по умолчанию включено). |
| `createNotificationChannel` | Создать канал уведомлений клиента. Этот API может реализовать функцию пользовательского звука на платформе Android. |

## Описание интерфейсов

### Регистрация в службе push-уведомлений

#### API

```
registerPush(SDKAppID, appKey, onSuccess, onError)
```

#### Описание параметров:

| Параметры | Тип | Описание | Путь доступа |
| --- | --- | --- | --- |
| SDKAppID | Number | SDKAppID для Push Service Push. | [Chat Console](https://console.trtc.io/chat/push-plugin-push-identifier) ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/26bc39b9c36e11ef85bd525400454e06.png) |
| appKey | String | Ключ клиента для Push Service Push. |  |
| onSuccess | Function | Обратный вызов успешной регистрации push-уведомлений. | - |
| onError | Function ï½undefined | Обратный вызов при ошибке регистрации push-уведомлений. | - |

### Отмена регистрации для отключения службы push-уведомлений

#### API

```
unRegisterPush(onSuccess, onError)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| onSuccess | Function | Обратный вызов успешной отмены регистрации push-уведомлений. |
| onError | Function ï½undefined | Обратный вызов при ошибке отмены регистрации push-уведомлений. |

### Установка идентификатора push ID RegistrationID

> **Важно:** Если вы используете этот API, убедитесь, что вы вызываете его перед `registerPush`.

#### API

```
setRegistrationID(registrationID, onSuccess)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| registrationID | String | Пользовательский идентификатор push ID. |
| onSuccess | Function | Обратный вызов после успешной установки пользовательского идентификатора push ID. |

### Получение идентификатора push ID RegistrationID

> **Важно:** Если вы вызвали интерфейс `setRegistrationID` для установки идентификатора, этот интерфейс вернёт установленный вами идентификатор, в противном случае он вернёт случайное значение, сгенерированное Push SDK.

#### API

```
getRegistrationID(onSuccess)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| onSuccess | Function | Обратный вызов при успешном получении push ID. |

### Получение информации о расширении Push-уведомления

#### API

```
getNotificationExtInfo(onSuccess)
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| onSuccess | Function | Обратный вызов при успешном получении содержимого пройденной информации. |

### Добавление слушателя push-уведомлений

#### API

```
addPushListener(eventName: string, listener: (data: any) => void);
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| eventName | String | Тип события push-уведомления. |
| listener | Function | Метод обработки события push-уведомления. |

### Удаление слушателя push-уведомлений

#### API

```
removePushListener(eventName: string, listener?: (data: any) => void);
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| eventName | String | Тип события push-уведомления. |
| listener | Function \| undefined | Метод обработки события push-уведомления. |

### Включение/отключение уведомлений в строке уведомлений, когда приложение находится в foreground

#### API

```
disablePostNotificationInForeground(disable: boolean);
```

#### Описание параметров:

| Параметры | Тип | Описание |
| --- | --- | --- |
| disable | boolean | Включение/отключение уведомлений в строке уведомлений, когда приложение находится в foreground, по умолчанию включено: true: отключение уведомлений в строке уведомлений, когда приложение находится в foregroundfalse: включение уведомлений в строке уведомлений, когда приложение находится в foreground |

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
| options.channelSound | String \| undefined | Звук оповещения пользовательского канала, имя аудиофайла без расширения. Аудиофайл должен быть размещён в `MyReactNativeApp/android/app/src/main/res/raw`. Например: `options.channelSound = private_ring`, что устанавливает `MyReactNativeApp/android/app/src/main/res/raw/private_ring.mp3` в качестве пользовательского звука оповещения. |
| onSuccess | Function | Функция обратного вызова при успешном вызове API. |


---
*Источник: [https://trtc.io/document/67557](https://trtc.io/document/67557)*

---
*Источник (EN): [react-native.md](./react-native.md)*
