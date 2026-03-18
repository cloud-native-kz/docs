# SeatGridWidget

## Введение в API

SeatGridWidget — это базовый элемент управления, разработанный нами для UIKit комнаты голосового чата. Этот основной элемент управления предоставляет различные API, такие как включение/отключение комнаты голосового чата, управление позициями микрофона в комнате прямой трансляции, включая подачу заявки на режим микрофона, приглашение докладчиков, перемещение позиций микрофона и удаление пользователя с микрофона.

## Обзор API

| API | Описание |
| --- | --- |
| [SeatGridController](https://www.tencentcloud.com/document/product/647/69245#de18fda1-4686-42a1-9592-3be78342b946) | Создание объекта SeatGridController |
| [SeatGridWidget](https://www.tencentcloud.com/document/product/647/69245#d147f174-e55a-4ba2-bbaf-2792c9419650) | Создание объекта SeatGridWidget |
| [startMicrophone](https://www.tencentcloud.com/document/product/647/69245#1032095a-ba39-4820-aac9-6399f497ec6d) | Открыть локальный микрофон |
| [stopMicrophone](https://www.tencentcloud.com/document/product/647/69245#c739e487-b83b-4a78-b432-3f84d867ffa2) | Закрыть локальный микрофон |
| [muteMicrophone](https://www.tencentcloud.com/document/product/647/69245#b866f4a7-1951-41b8-8629-dd613a030fd5) | Приостановить публикацию локального аудиопотока |
| [unmuteMicrophone](https://www.tencentcloud.com/document/product/647/69245#33b60d36-7ebe-4691-918a-7973122f6cb0) | Возобновить публикацию локального аудиопотока |
| [startVoiceRoom](https://www.tencentcloud.com/document/product/647/69245#fa10462e-e188-4879-9be5-2c2d6a222b6d) | Анкор создает комнату прямой трансляции и начинает трансляцию. |
| [stopVoiceRoom](https://www.tencentcloud.com/document/product/647/69245#c739e487-b83b-4a78-b432-3f84d867ffa2) | Анкор прекращает трансляцию и уничтожает комнату прямой трансляции. |
| [joinVoiceRoom](https://www.tencentcloud.com/document/product/647/69245#8c23ef17-5f8a-4ddd-b803-f78bd3a18f17) | Аудитория присоединяется к комнате прямой трансляции анкора. |
| [leaveVoiceRoom](https://www.tencentcloud.com/document/product/647/69245#cdba89b2-1d72-4603-9077-c97d158e2fef) | Аудитория выходит из комнаты прямой трансляции анкора. |
| [updateRoomSeatMode](https://www.tencentcloud.com/document/product/647/69245#db8d3b1f-26b4-4e79-896a-dc00cc32caac) | Обновить режим сидений в комнате. |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/69245#00371c4a-dda3-4035-8bd2-318591fa7d0f) | Анкор отвечает на заявку о микрофоне / Аудитория отвечает на приглашение о микрофоне |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/69245#dedaef30-7e34-4d1d-87d3-7cad0c60a2d6) | Анкор отменяет приглашение на микрофон / Аудитория отменяет заявку на микрофон |
| [takeSeat](https://www.tencentcloud.com/document/product/647/69245#c771b29e-ad6c-4cc6-beb6-10a0e2206b11) | Стать докладчиком. |
| [moveToSeat](https://www.tencentcloud.com/document/product/647/69245#680e8c90-7f4e-4918-aeaf-a6a25fe24ebd) | Переместить сидение. |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/69245#012b0c17-e336-42c1-9b8f-065981ba626e) | Покинуть сидение. |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/69245#087189d3-5cf1-4aa3-b465-4f48454c46bf) | Анкор приглашает пользователей говорить. |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/69245#f1ff3b22-c3e2-47ce-8f62-4447149f4148) | Анкор удаляет пользователя с сидения. |
| [lockSeat](https://www.tencentcloud.com/document/product/647/69245#f538dc5d-6dda-4597-863a-8f771d6ba296) | Анкор блокирует сидение (включая блокировку позиции, блокировку статуса аудио и блокировку статуса видео) |
| [setLayoutMode](https://www.tencentcloud.com/document/product/647/69245#c69ad7f9-71ab-4b3b-8529-8e1a10abebd1) | Анкор устанавливает режим макета списка сидений. |
| [addObserver](https://www.tencentcloud.com/document/product/647/69245#bc6933f2-783a-4059-8164-d4566dbebe06) | Установить обратный вызов события |
| [removeObserver](https://www.tencentcloud.com/document/product/647/69245#b0de0bf4-56d2-4b8d-baa3-165e2dab8a3c) | Удалить обратный вызов события |

## Детали API

### SeatGridController

Создание экземпляра объекта `SeatGridController`. `SeatGridController` отвечает за предоставление API для сценария комнаты голосового чата.

```
SeatGridController()
```

**Возвращаемое значение:** SeatGridController

### SeatGridWidget

Создание экземпляра `SeatGridWidget`. `SeatGridWidget` отвечает за отрисовку UI сидений.

```
SeatGridWidget(    {super.key,    required this.controller,    this.seatWidgetBuilder,    this.onSeatWidgetTap});
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| key | Key? | Как Flutter управляет заменой параметров старого виджета на новый виджет |
| controller | [SeatGridController](https://www.tencentcloud.com/document/product/647/69245#de18fda1-4686-42a1-9592-3be78342b946) | Контроллер SeatGridWidget, отвечающий за предоставление API в сценарии комнаты голосового чата |
| seatWidgetBuilder | [SeatWidgetBuilder](https://www.tencentcloud.com/document/product/647/69245#2f992991-4d2d-4690-a145-203464cec215) | Конструктор пользовательского виджета сидения |
| onSeatWidgetTap | [OnSeatWidgetTap](https://www.tencentcloud.com/document/product/647/69245#5a80a5d2-86ad-4ec7-8a28-85d9163cc5ed) | Обратный вызов события нажатия на сидение |

**Возвращаемое значение:** SeatGridWidget

### startMicrophone

Открыть локальный микрофон.

```
Future<TUIActionCallback> startMicrophone()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### stopMicrophone

Закрыть локальный микрофон.

```
void stopMicrophone()
```

**Возвращаемое значение:** void

### muteMicrophone

Приостановить публикацию локального аудиопотока.

```
Future<TUIActionCallback> muteMicrophone()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### unmuteMicrophone

Возобновить публикацию локального аудиопотока.

```
Future<TUIActionCallback> unmuteMicrophone()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### startVoiceRoom

Анкор создает комнату прямой трансляции и начинает трансляцию.

```
Future<TUIValueCallBack<TUIRoomInfo>> startVoiceRoom(TUIRoomInfo roomInfo)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomInfo | [TUIRoomInfo](https://www.tencentcloud.com/document/product/647/69251#RoomInfo) | Информация о создании комнаты прямой трансляции |

**Возвращаемое значение:** Future<[TUIValueCallBack](https://www.tencentcloud.com/document/product/647/69251#TUIValueCallBack%3CT%3E)<[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/69251#RoomInfo)>>

### stopVoiceRoom

Анкор прекращает трансляцию и уничтожает комнату прямой трансляции.

```
Future<TUIActionCallback> stopVoiceRoom()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### joinVoiceRoom

Аудитория присоединяется к комнате прямой трансляции анкора.

```
Future<TUIValueCallBack<TUIRoomInfo>> joinVoiceRoom(String roomId)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | ID комнаты прямой трансляции |

**Возвращаемое значение:** Future<[TUIValueCallBack](https://www.tencentcloud.com/document/product/647/69251#TUIValueCallBack%3CT%3E)<[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/69251#RoomInfo)>>

### leaveVoiceRoom

Аудитория выходит из комнаты прямой трансляции анкора.

```
Future<TUIActionCallback> leaveVoiceRoom()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### updateRoomSeatMode

Обновить режим сидений в комнате.

```
Future<TUIActionCallback> updateRoomSeatMode(TUISeatMode seatMode)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| seatMode | [TUISeatMode](https://www.tencentcloud.com/document/product/647/69251#TUISeatMode) | Свободно занять: В режиме свободного говорения аудитория может свободно присоединяться к подиуму без подачи заявки. applyToTake: Аудитория становится докладчиками только после согласия вещателя. |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### responseRemoteRequest

Анкор отвечает на заявку о микрофоне / Аудитория отвечает на приглашение о микрофоне.

```
Future<TUIActionCallback> responseRemoteRequest(String userId, bool agree)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя, который отвечает на пользователя. Если текущая роль — аудитория, ID можно оставить пустым. |
| agree | bool | Принять ли запросы: true для принятия, false для отклонения запросов |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### cancelRequest

Анкор отменяет приглашение на микрофон / Аудитория отменяет заявку на микрофон

```
Future<TUIActionCallback> cancelRequest(String userId)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя, для которого отменяется запрос. Если текущая роль — аудитория, ID можно оставить пустым. |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### takeSeat

Запросить говорить (требуется подача заявки в режиме говорения)

```
Future<RequestCallback> takeSeat(int seatIndex, int timeout)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| index | int | ID позиции микрофона для говорения |
| timeout | int | Период ожидания в секундах. Если установлено значение 0, SDK не будет выполнять обнаружение тайм-аута или запускать обратный вызов тайм-аута. |

**Возвращаемое значение:** Future<[RequestCallback](https://www.tencentcloud.com/document/product/647/69245#1080ad78-303e-457f-897a-8f7e6ca60450)>

### moveToSeat

Удалить сидение (эта функция может быть вызвана только пользователем, уже находящимся на сидении)

```
Future<TUIActionCallback> moveToSeat(int index)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| index | int | ID позиции микрофона, на которую необходимо переместиться |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### leaveSeat

Стать слушателем.

```
Future<TUIActionCallback> leaveSeat()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### takeUserOnSeatByAdmin

Анкор приглашает пользователей говорить.

```
Future<RequestCallback> takeUserOnSeatByAdmin(int seatIndex, String userId, int timeout)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| index | int | ID приглашенной позиции микрофона |
| userId | String | ID приглашенного пользователя |
| timeout | int | Период ожидания в секундах. Если установлено значение 0, SDK не будет выполнять обнаружение тайм-аута или запускать обратный вызов тайм-аута. |

**Возвращаемое значение:** Future<[RequestCallback](https://www.tencentcloud.com/document/product/647/69245#1080ad78-303e-457f-897a-8f7e6ca60450)>

### kickUserOffSeatByAdmin

Анкор удаляет пользователя с сидения.

```
Future<TUIActionCallback> kickUserOffSeatByAdmin(String userId)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID удаленного пользователя |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### lockSeat

Отключить докладчика. Анкор блокирует сидение (включая блокировку позиции, блокировку статуса аудио и блокировку статуса видео)

```
Future<TUIActionCallback> lockSeat(int index, TUISeatLockParams lockMode)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| seatIndex | int | ID позиции микрофона, которую необходимо заблокировать. |
| lockMode | [TUISeatLockParams](https://www.tencentcloud.com/document/product/647/69251#080212f8-d6ce-4430-b745-2fdd5ef8c330) | Параметры отключения микрофона |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/69251#TUIActionCallback)>

### setLayoutMode

Установить режим макета списка сидений.

```
void setLayoutMode(LayoutMode layoutMode, SeatWidgetLayoutConfig? layoutConfig)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| layoutMode | [LayoutMode](https://www.tencentcloud.com/document/product/647/69245#9054f6cd-8773-447d-9139-3a65d2e9a42f) | Режим макета списка позиций сидений поддерживает фокусный макет, макет сетки, вертикальный макет и свободный макет. |
| layoutConfig | [SeatWidgetLayoutConfig](https://www.tencentcloud.com/document/product/647/69245#005ea306-be1d-4523-aff0-b8cb65853266) | Информация о конфигурации макета действует только в режиме свободного макета. |

**Возвращаемое значение:** void

### addObserver

Установить обратный вызов события.

```
void addObserver(SeatGridWidgetObserver observer)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| observer | [SeatGridWidgetObserver](https://www.tencentcloud.com/document/product/647/69245#7bf5d75e-dd5a-4b3e-b462-3a31a3cefc22) | Объект обратного вызова основного компонента |

**Возвращаемое значение:** void

### removeObserver

Удалить обратный вызов события.

```
void removeObserver(SeatGridWidgetObserver observer)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| observer | [SeatGridWidgetObserver](https://www.tencentcloud.com/document/product/647/69245#7bf5d75e-dd5a-4b3e-b462-3a31a3cefc22) | Объект обратного вызова основного компонента |

**Возвращаемое значение:** void

## Определение типов

| **Тип** | **Значение** |
| --- | --- |
| [SeatWidgetBuilder](https://www.tencentcloud.com/document/product/647/69245#2f992991-4d2d-4690-a145-203464cec215) | Конструктор пользовательского виджета сидения |
| [OnSeatWidgetTap](https://www.tencentcloud.com/document/product/647/69245#5a80a5d2-86ad-4ec7-8a28-85d9163cc5ed) | Событие нажатия на сидение |
| [OnRoomDismissed](https://www.tencentcloud.com/document/product/647/69245#7fafce42-c335-4cc0-9aca-72a2702a7160) | Получено событие уничтожения комнаты |
| [OnKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/69245#b0c03cac-652f-421a-ab6a-e72eb99473f1) | Получено событие удаления из комнаты |
| [OnSeatRequestReceived](https://www.tencentcloud.com/document/product/647/69245#b4b4436b-4301-4cc9-8e9f-d6a1daefc34b) | Получено событие запроса на говорение / Получено событие приглашения на говорение |
| [OnSeatRequestCancelled](https://www.tencentcloud.com/document/product/647/69245#bf52fbac-61ab-47dc-8989-d86e78eb58ef) | Событие отмены запроса на говорение / приглашения на говорение |
| [OnKickedOffSeat](https://www.tencentcloud.com/document/product/647/69245#2c5e6f5d-a92d-4bf5-aeb5-feb62cfa4d77) | Получено событие удаления пользователя с микрофона |
| [OnUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/69245#62acca5b-e203-47bb-9e26-4a44ac22975e) | Событие изменения статуса аудио пользователя. |
| [LayoutMode](https://www.tencentcloud.com/document/product/647/69245#9054f6cd-8773-447d-9139-3a65d2e9a42f) | Режим макета списка позиций сидений поддерживает фокусный макет, макет сетки, вертикальный макет и пользовательский макет. |
| [SeatWidgetLayoutRowAlignment](https://www.tencentcloud.com/document/product/647/69245#b22ba27c-695a-4ea9-9739-7d18450a39b1) | Режим выравнивания макета сидений |
| [RequestType](https://www.tencentcloud.com/document/product/647/69245#f1f2b39d-2e01-49d4-a5eb-402564d7f0c4) | Тип запроса (подача заявки на режим микрофона и приглашение на говорение) |
| [RequestResultType](https://www.tencentcloud.com/document/product/647/69245#43c7b85d-9c84-4111-a3a3-b2c2e3271e17) | Тип результата запроса |
| [RequestCallback](https://www.tencentcloud.com/document/product/647/69245#1080ad78-303e-457f-897a-8f7e6ca60450) | Обратный вызов результата запроса |
| [SeatWidgetLayoutConfig](https://www.tencentcloud.com/document/product/647/69245#005ea306-be1d-4523-aff0-b8cb65853266) | Информация о конфигурации макета сидений |
| [SeatWidgetLayoutRowConfig](https://www.tencentcloud.com/document/product/647/69245#a2174da5-9786-4f90-a09e-01b3d9a99a2f) | Информация о конфигурации макета строки макета сидений |

### SeatWidgetBuilder

Конструктор пользовательского `widget` сидения

```
typedef SeatWidgetBuilder = Widget Function(    BuildContext context,    ValueNotifier<TUISeatInfo> seatInfoNotifier,    ValueNotifier<int> volumeNotifier);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| context | BuildContext | Контекст |
| seatInfoNotifier | ValueNotifier<[TUISeatInfo](https://www.tencentcloud.com/document/product/647/69251#SeatInfo)> | Уведомитель информации о сидении |
| volumeNotifier | ValueNotifier<int> | Уведомитель информации об громкости |

### OnSeatWidgetTap

Событие нажатия на сидение

```
typedef OnSeatWidgetTap = void Function(TUISeatInfo seatInfo);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| seatInfo | [TUISeatInfo](https://www.tencentcloud.com/document/product/647/69251#SeatInfo) | Информация о позиции микрофона |

### OnRoomDismissed

Получено событие уничтожения комнаты

```
typedef OnRoomDismissed = void Function(String roomId);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | ID комнаты |

### OnKickedOutOfRoom

Получено событие удаления из комнаты

```
typedef OnKickedOutOfRoom = void Function(String roomId, TUIKickedOutOfRoomReason reason, String message);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | ID комнаты |
| reason | TUIKickedOutOfRoomReason | Причина удаления |
| message | String | Информация об удалении |

### OnSeatRequestReceived

Получено событие запроса на говорение / Получено событие приглашения на говорение

```
typedef OnSeatRequestReceived = void Function(RequestType type, TUIUserInfo userInfo);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| type | [RequestType](https://www.tencentcloud.com/document/product/647/69245#f1f2b39d-2e01-49d4-a5eb-402564d7f0c4) | Тип запроса |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/69251#UserInfo) | Информация о запрашивающем |

### OnSeatRequestCancelled

Событие отмены запроса на говорение / приглашения на говорение

```
typedef OnSeatRequestCancelled = void Function(RequestType type, TUIUserInfo userInfo);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| type | [RequestType](https://www.tencentcloud.com/document/product/647/69245#f1f2b39d-2e01-49d4-a5eb-402564d7f0c4) | Тип запроса |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/69251#UserInfo) | Информация об операторе |

### OnKickedOffSeat

Получено событие удаления пользователя с микрофона

```
typedef OnKickedOffSeat = void Function(TUIUserInfo userInfo);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/69251#UserInfo) | Информация об операторе |

### OnUserAudioStateChanged

Событие изменения статуса аудио пользователя

```
typedef OnUserAudioStateChanged = void Function(TUIUserInfo userInfo, bool hasAudio, TUIChangeReason reason);
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userInfo | [TUIUserInfo](https://www.tencentcloud.com/document/product/647/69251#UserInfo) | Информация об операторе |
| hasAudio | bool | Присутствует ли аудиопоток |
| reason | [TUIChangeReason](https://www.tencentcloud.com/document/product/647/69251#ChangeReason) | Причина изменения аудиопотока |

### LayoutMode

Режим макета списка позиций сидений

| Значение перечисления | Значение |
| --- | --- |
| focus | Фокусный макет |
| grid | Макет сетки |
| vertical | Вертикальный макет |
| free | Пользовательский макет |

### SeatWidgetLayoutRowAlignment

Режим выравнивания макета сидений

| Значение перечисления | Значение |
| --- | --- |
| start | Переместить сидение ближе к начальной позиции |
| end | Переместить сидение ближе к конечной позиции |
| center | Переместить сидение ближе к промежуточной позиции |
| spaceBetween | Не оставляйте пространство перед

---
*Источник (EN): [seatgridwidget.md](./seatgridwidget.md)*
