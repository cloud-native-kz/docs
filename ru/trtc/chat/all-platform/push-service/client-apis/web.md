# Web

## Обзор API

| API | Описание |
| --- | --- |
| `registerPush` | Регистрация сервиса push-уведомлений (этот API необходимо вызвать для использования сервиса push-уведомлений только после получения согласия пользователя на политику конфиденциальности). |
| `unRegisterPush` | Отключение сервиса push-уведомлений. |
| `addPushListener` | Добавление слушателя Push-уведомлений. |
| `removePushListener` | Удаление слушателя Push-уведомлений. |

## Детальное описание API

### Регистрация сервиса Push-уведомлений

#### API

```
registerPush(options): Promise;
```

#### Описание параметров Options

| Параметр | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Number | SDKAppID сервиса Push-уведомлений. Для справки: [Quick Integration > Prerequisites > Enabling a Service](https://www.tencentcloud.com/document/product/1047/75529#ef1e073e-23da-422d-b06b-f13fcda46734) для получения SDKAppID. |
| appKey | String | Ключ клиента сервиса Push-уведомлений. Для справки: [Quick Integration > Prerequisites > Enabling a Service](https://www.tencentcloud.com/document/product/1047/75529#ef1e073e-23da-422d-b06b-f13fcda46734) для получения AppKey |
| userID | String | Регистрация userID пользователя для сервиса push-уведомлений. Уникальный идентификатор пользователя, определяемый вами, может содержать только прописные и строчные буквы (a-z, A-Z), цифры (0-9), подчеркивание и дефис. |

### Отключение сервиса Push-уведомлений

#### API

```
unRegisterPush(): Promise;
```

### Добавление слушателя Push-уведомлений

#### API

```
addPushListener(eventName: string, listener: (data: any) => void);
```

#### Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| eventName | String | Тип события push-уведомления.`WebPush.EVENT.MESSAGE_RECEIVED`: поступление нового уведомления`WebPush.EVENT.MESSAGE_REVOKED`: отзыв уведомления`WebPush.EVENT.NOTIFICATION_CLICKED`: клик по уведомлению |
| listener | Function | Метод обработки события push-уведомления. |

### Удаление слушателя Push-уведомлений

#### API

```
removePushListener(eventName: string, listener?: (data: any) => void);
```

#### Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| eventName | String | Тип события push-уведомления.`WebPush.EVENT.MESSAGE_RECEIVED`: поступление нового уведомления`WebPush.EVENT.MESSAGE_REVOKED`: отзыв уведомления`WebPush.EVENT.NOTIFICATION_CLICKED`: клик по уведомлению |
| listener | Function \| undefined | Метод обработки события push-уведомления. |


---
*Источник: [https://trtc.io/document/75688](https://trtc.io/document/75688)*

---
*Источник (EN): [web.md](./web.md)*
