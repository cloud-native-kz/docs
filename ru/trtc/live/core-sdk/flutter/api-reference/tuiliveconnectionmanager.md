# TUILiveConnectionManager

Copyright (c) 2024 Tencent. All rights reserved.

Модуль:   TUILiveConnectionManager @ TUIKitEngine

Функции: Соответствующие API для Live Connection. Функции на этой странице поддерживаются только для типа комнаты прямого эфира ([TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

**TUILiveConnectionManager**

## TUILiveConnectionObserver

| Список функций | Описание |
| --- | --- |
| [onConnectionUserListChanged](https://www.tencentcloud.com/document/product/647/69265#7be00604bd4d27805a839b743954a95c) | Получено уведомление об изменении списка подключённых пользователей. |
| [onConnectionRequestReceived](https://www.tencentcloud.com/document/product/647/69265#1b2ccc6866435842e1ef670ad196739f) | Обратный вызов при получении приглашения на подключение |
| [onConnectionRequestCancelled](https://www.tencentcloud.com/document/product/647/69265#703c0713cd90cb0fa60f2ddc91ce7555) | Обратный вызов отмены приглашения |
| [onConnectionRequestAccept](https://www.tencentcloud.com/document/product/647/69265#c99794669422490e9e678a12455f6ee9) | Обратный вызов принятия приглашения |
| [onConnectionRequestReject](https://www.tencentcloud.com/document/product/647/69265#70326770790d9053e5eb46ed3b3d797a) | Обратный вызов отклонения приглашения |
| [onConnectionRequestTimeout](https://www.tencentcloud.com/document/product/647/69265#ad2ca9383794b28927e2ed7d46d56c2e) | Обратный вызов истечения времени ожидания приглашения |

## TUILiveConnectionManager

| Список функций | Описание |
| --- | --- |
| [addObserver](https://www.tencentcloud.com/document/product/647/69265#0d177d4d2cc08cb4127697f20321d2b1) | Добавить обратный вызов события |
| [removeObserver](https://www.tencentcloud.com/document/product/647/69265#e327b25415e3471f7989f04d3660833f) | Удалить обратный вызов события |
| [requestConnection](https://www.tencentcloud.com/document/product/647/69265#21dada6328cc57d6ace44a695445f85c) | Инициировать запрос на подключение |
| [cancelConnectionRequest](https://www.tencentcloud.com/document/product/647/69265#cba46056186507a80a12a048324a378b) | Отменить запрос на подключение |
| [acceptConnection](https://www.tencentcloud.com/document/product/647/69265#2f98de3bbbf0d38fc9360c1b6046444c) | Принять приглашение на подключение |
| [rejectConnection](https://www.tencentcloud.com/document/product/647/69265#c34f51562701b317ca5bddc81e09c035) | Отклонить приглашение на подключение |
| [disconnect](https://www.tencentcloud.com/document/product/647/69265#ca0b949411f91ee15345ee889c08f8c9) | Выйти из линии подключения комнаты |

## Типы структурированных данных

| Список функций | Описание |
| --- | --- |
| [TUIConnectionUser](https://www.tencentcloud.com/document/product/647/69265#ce98cb6cc271975f063e0469f66ffcce) | Информация о подключённом пользователе |
| [TUIConnectionRequestResult](https://www.tencentcloud.com/document/product/647/69265#4140d6d8-4c42-454e-9236-379c72421e1c) | Результат запроса подключения |

## Типы перечислений

| Типы перечислений | Описание |
| --- | --- |
| [TUIConnectionCode](https://www.tencentcloud.com/document/product/647/69265#92daac9cd74ffae905ec2f0dbd85a61e) | Статус приглашения на подключение |

## onConnectionUserListChanged

**Получено уведомление об изменении списка подключённых пользователей.**

```
  OnConnectionUserListChanged onConnectionUserListChanged =         (List<TUIConnectionUser> connectedList,          List<TUIConnectionUser> joinedList,          List<TUIConnectionUser> leavedList) {};
```

| Параметр | Описание |
| --- | --- |
| connectedList | Список подключённых пользователей. |
| joinedList | Список недавно присоединившихся пользователей. |
| leavedList | Список пользователей, покинувших подключение. |

## onConnectionRequestReceived

**Обратный вызов при получении приглашения на подключение**

```
OnConnectionRequestReceived onConnectionRequestReceived =         (TUIConnectionUser inviter,           List<TUIConnectionUser> inviteeList,          String extensionInfo) {};
```

| Параметр | Описание |
| --- | --- |
| inviter | Информация инициатора приглашения. |
| inviteeList | Список приглашённых пользователей для подключения. |
| extensionInfo | Прозрачная передача информации. |

## onConnectionRequestCancelled

**Обратный вызов отмены приглашения**

```
OnConnectionRequestCancelled onConnectionRequestCancelled =      (TUIConnectionUser inviter) {};
```

| Параметр | Описание |
| --- | --- |
| inviter | Информация инициатора приглашения. |

## onConnectionRequestAccept

**Обратный вызов принятия приглашения**

```
OnConnectionRequestAccept onConnectionRequestAccept =      (TUIConnectionUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| invitee | Информация приглашённого пользователя. |

## onConnectionRequestReject

**Обратный вызов отклонения приглашения**

```
  OnConnectionRequestReject onConnectionRequestReject =      (TUIConnectionUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| invitee | Информация приглашённого пользователя. |

## onConnectionRequestTimeout

**Обратный вызов истечения времени ожидания приглашения**

```
OnConnectionRequestTimeout onConnectionRequestTimeout =      (TUIConnectionUser inviter,       TUIConnectionUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| inviter | Информация инициатора приглашения. |
| invitee | Информация приглашённого пользователя. |

## addObserver

**Добавить обратный вызов события**

```
void addObserver(TUILiveConnectionObserver observer);
```

| Параметр | Описание |
| --- | --- |
| observer | Контролируемые экземпляры. |

## removeObserver

**Удалить обратный вызов события**

```
 void removeObserver(TUILiveConnectionObserver observer);
```

| Параметр | Описание |
| --- | --- |
| observer | Контролируемые экземпляры. |

## requestConnection

**Инициировать запрос на подключение**

```
Future<TUIValueCallBack<TUIConnectionRequestResult>> requestConnection      (List<String> roomIdList,       int timeout,        String extensionInfo);
```

| Параметр | Описание |
| --- | --- |
| roomIdList | Список идентификаторов комнат для приглашения на подключение. |
| timeout | Время ожидания |
| extensionInfo | Расширенная информация. |

## cancelConnectionRequest

**Отменить запрос на подключение**

```
Future<TUIActionCallback> cancelConnectionRequest(List<String> roomIdList);
```

| Параметр | Описание |
| --- | --- |
| roomIdList | Список идентификаторов комнат, для которых отменен запрос на подключение. |

## acceptConnection

**Принять приглашение на подключение**

```
Future<TUIActionCallback> acceptConnection(String roomId);
```

| Параметр | Описание |
| --- | --- |
| roomId | Идентификатор комнаты. |

## rejectConnection

**Отклонить приглашение на подключение**

```
Future<TUIActionCallback> rejectConnection(String roomId);
```

| Параметр | Описание |
| --- | --- |
| roomId | Идентификатор комнаты. |

## disconnect

**Выйти из линии подключения комнаты**

```
 Future<TUIActionCallback> disconnect();
```

> **Примечание:** Вызов этого API приведёт к выходу из состояния линии подключения комнаты. Может быть вызван только в подключённом состоянии.

## TUIConnectionUser

**Информация о подключённом пользователе**

| Типы перечислений | Описание |
| --- | --- |
| roomId | Идентификатор комнаты подключения. |
| userId | Идентификатор подключённого пользователя. |
| userName | Имя пользователя подключённого пользователя. |
| avatarUrl | Адрес аватара подключённого пользователя. |
| joinConnectionTime | Метка времени начала подключения. |

## TUIConnectionRequestResult

| Типы перечислений | Описание |
| --- | --- |
| requestMap | Карта результатов запроса подключения |

## TUIConnectionCode

**Статус приглашения на подключение**

| Пример ошибки | Значение | Описание |
| --- | --- | --- |
| unknown | -1 | Статус по умолчанию. |
| success | 0 | Запрос на подключение отправлен успешно. |
| roomNotExists | 1 | Комната для приглашения на подключение не существует. |
| connecting | 2 | Приглашённая комната уже находится в списке приглашений или подключена. |
| connectingOtherRoom | 3 | Приглашённая комната подключена к другим комнатам. |
| connetionFull | 4 | Текущее количество подключений достигло максимального лимита. |
| retry | 5 | Внутренняя ошибка, рекомендуется повторить попытку. |


---
*Источник: [https://trtc.io/document/69265](https://trtc.io/document/69265)*

---
*Источник (EN): [tuiliveconnectionmanager.md](./tuiliveconnectionmanager.md)*
