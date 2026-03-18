# SeatGridView

## Введение в API

SeatGridView — это базовый элемент управления, разработанный нами для UIKit голосовой комнаты чата. Этот основной элемент управления предоставляет богатый набор API, таких как открытие/закрытие голосовой комнаты чата, управление позициями мест в прямой трансляции, например подача заявки на место, приглашение на место, изменение позиции места и удаление пользователя с места.

## Обзор API

| **API** | **Описание** |
| --- | --- |
| [SeatGridView](https://www.tencentcloud.com/document/product/647/66793#d147f174-e55a-4ba2-bbaf-2792c9419650) | Создание объекта SeatGridView, поддержка **программного создания** и **загрузки из XML**. |
| [startMicrophone](https://www.tencentcloud.com/document/product/647/66793#1032095a-ba39-4820-aac9-6399f497ec6d) | Включение локального микрофона |
| [stopMicrophone](https://www.tencentcloud.com/document/product/647/66793#c739e487-b83b-4a78-b432-3f84d867ffa2) | Отключение локального микрофона |
| [muteMicrophone](https://www.tencentcloud.com/document/product/647/66793#b866f4a7-1951-41b8-8629-dd613a030fd5) | Приостановка публикации локального аудиопотока |
| [unmuteMicrophone](https://www.tencentcloud.com/document/product/647/66793#33b60d36-7ebe-4691-918a-7973122f6cb0) | Возобновление публикации локального аудиопотока |
| [startVoiceRoom](https://www.tencentcloud.com/document/product/647/66793#fa10462e-e188-4879-9be5-2c2d6a222b6d) | Ведущий создает комнату и начинает трансляцию |
| [stopVoiceRoom](https://www.tencentcloud.com/document/product/647/66793#89f1f933-1771-4f4e-81af-5e0d38dce48e) | Ведущий останавливает трансляцию и удаляет комнату |
| [joinVoiceRoom](https://www.tencentcloud.com/document/product/647/66793#8c23ef17-5f8a-4ddd-b803-f78bd3a18f17) | Зритель входит в комнату ведущего |
| [leaveVoiceRoom](https://www.tencentcloud.com/document/product/647/66793#cdba89b2-1d72-4603-9077-c97d158e2fef) | Зритель покидает комнату ведущего |
| [updateRoomSeatMode](https://www.tencentcloud.com/document/product/647/66793#db8d3b1f-26b4-4e79-896a-dc00cc32caac) | Обновление режима микрофона комнаты |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/66793#00371c4a-dda3-4035-8bd2-318591fa7d0f) | Ведущий отвечает на заявку на микрофон/Зритель отвечает на приглашение на микрофон |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/66793#dedaef30-7e34-4d1d-87d3-7cad0c60a2d6) | Ведущий отменяет приглашение на микрофон/Зритель отменяет заявку на микрофон |
| [takeSeat](https://www.tencentcloud.com/document/product/647/66793#c771b29e-ad6c-4cc6-beb6-10a0e2206b11) | Включение микрофона |
| [moveToSeat](https://www.tencentcloud.com/document/product/647/66793#680e8c90-7f4e-4918-aeaf-a6a25fe24ebd) | Отключение микрофона |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/66793#012b0c17-e336-42c1-9b8f-065981ba626e) | Отключение микрофона |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/66793#087189d3-5cf1-4aa3-b465-4f48454c46bf) | Ведущий приглашает пользователя включить микрофон |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/66793#f1ff3b22-c3e2-47ce-8f62-4447149f4148) | Ведущий удаляет пользователя с микрофона |
| [lockSeat](https://www.tencentcloud.com/document/product/647/66793#f538dc5d-6dda-4597-863a-8f771d6ba296) | Ведущий блокирует позицию микрофона (включая блокировку позиции, блокировку статуса аудио и блокировку статуса видео) |
| [setLayoutMode](https://www.tencentcloud.com/document/product/647/66793#c69ad7f9-71ab-4b3b-8529-8e1a10abebd1) | Ведущий устанавливает режим макета для списка микрофонов |
| [setSeatViewAdapter](https://www.tencentcloud.com/document/product/647/66793#58713969-f561-4dd1-aa5d-f188888358dd) | Установка адаптера для представления мест |
| [addObserver](https://www.tencentcloud.com/document/product/647/66793#bc6933f2-783a-4059-8164-d4566dbebe06) | Установка обратных вызовов событий |
| [removeObserver](https://www.tencentcloud.com/document/product/647/66793#b0de0bf4-56d2-4b8d-baa3-165e2dab8a3c) | Удаление обратных вызовов событий |

## Подробная информация об API

### SeatGridView

Создание экземпляра объекта SeatGridView. Поддерживает **программное создание** и **загрузку из XML**.

```
public SeatGridView(Context context)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| context | Context | Объект контекста Android |

**Возвращаемое значение:** SeatGridView

### startMicrophone

Включение локального микрофона.

```
void startMicrophone(ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### stopMicrophone

Отключение локального микрофона.

```
void stopMicrophone()
```

**Возвращаемое значение:** void

### muteMicrophone

Приостановка публикации локального аудиопотока.

```
void muteMicrophone()
```

**Возвращаемое значение:** void

### unmuteMicrophone

Возобновление публикации локального аудиопотока.

```
void unmuteMicrophone(ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### startVoiceRoom

Ведущий создает комнату и начинает трансляцию.

```
void startVoiceRoom(RoomInfo roomInfo, GetRoomInfoCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomInfo | RoomInfo | Информация для создания комнаты прямой трансляции |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### stopVoiceRoom

Ведущий останавливает трансляцию и удаляет комнату.

```
void stopVoiceRoom(ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### joinVoiceRoom

Зритель входит в комнату ведущего.

```
void joinVoiceRoom(String roomId, GetRoomInfoCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomId | String | ID комнаты прямой трансляции |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### leaveVoiceRoom

Зритель покидает комнату ведущего.

```
void leaveVoiceRoom(ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### updateRoomSeatMode

Обновление режима микрофона комнаты.

```
void updateRoomSeatMode(SeatMode seatMode, ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| seatMode | SeatMode | FREE_TO_TAKE: режим свободного места, зритель может свободно занимать место без заявки;APPLY_TO_TAKE: режим подачи заявки на место, зритель требует согласия ведущего для занятия места. |
| callback | ActionCallback | Обратный вызов операции. |

**Возвращаемое значение:** void

### responseRemoteRequest

Ведущий отвечает на заявку на микрофон/Зритель отвечает на приглашение на микрофон.

```
void responseRemoteRequest(String userId, boolean agree, ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| userId | String | ID пользователя, дающего ответ, если текущая роль — зритель, ID можно оставить пустым |
| agree | boolean | Принять ли заявку, true: принять заявку, false: отклонить заявку |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### cancelRequest

Ведущий отменяет приглашение на микрофон/Зритель отменяет заявку на микрофон

```
void cancelRequest(String userId, ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| userId | String | ID отмененного пользователя, если текущая роль — зритель, ID можно оставить пустым |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### takeSeat

Запрос на выступление (в режиме выступления требуется заявка)

```
void takeSeat(int index, int timeout, VoiceRoomDefine.RequestCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| index | int | Номер позиции микрофона для подключения |
| timeout | int | Период ожидания в секундах. Если установить на 0, SDK не будет выполнять проверку ожидания или срабатывать обратный вызов ожидания |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### moveToSeat

Перемещение микрофона (эту функцию могут вызывать только пользователи, которые уже находятся на месте)

```
void moveToSeat(int index, ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| index | int | Номер позиции микрофона для перемещения |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### leaveSeat

Активное покидание места

```
void leaveSeat(ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### takeUserOnSeatByAdmin

Ведущий приглашает пользователя включить микрофон

```
void takeUserOnSeatByAdmin(int index, String userId, int timeout, VoiceRoomDefine.RequestCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| index | int | Номер позиции микрофона приглашения |
| userId | String | ID приглашенного пользователя |
| timeout | int | Период ожидания в секундах. Если установить на 0, SDK не будет выполнять проверку ожидания или срабатывать обратный вызов ожидания |
| callback | VoiceRoomDefine.RequestCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### kickUserOffSeatByAdmin

Ведущий удаляет пользователя с микрофона

```
void kickUserOffSeatByAdmin(String userId, ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| userId | String | ID пользователя, удаляемого с микрофона |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### lockSeat

Отключение микрофона, ведущий блокирует позицию микрофона (включая блокировку позиции, блокировку статуса аудио и блокировку статуса видео)

```
void lockSeat(int seatIndex, TUIRoomDefine.SeatLockParams params, ActionCallback callback)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| seatIndex | int | Номер позиции микрофона для блокировки |
| params | TUIRoomDefine.SeatLockParams | Параметры отключения микрофона. См. подробное описание: TUIRoomDefine.SeatLockParams |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:** void

### setLayoutMode

Установка режима макета для списка микрофонов.

```
void setLayoutMode(LayoutMode layoutModel, SeatViewLayoutConfig layoutConfig)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| layoutModel | [LayoutMode](https://www.tencentcloud.com/document/product/647/66793#9054f6cd-8773-447d-9139-3a65d2e9a42f) | Режимы макета списка микрофонов, поддерживаются макет элементов, макет сетки, вертикальный макет, пользовательский макет. |
| layoutConfig | [SeatViewLayoutConfig](https://www.tencentcloud.com/document/product/647/66793#005ea306-be1d-4523-aff0-b8cb65853266) | Информация конфигурации макета, действительна только в режиме пользовательского макета |

**Возвращаемое значение:** void

### setSeatViewAdapter

Установка адаптера для представления микрофона.

```
void setSeatViewAdapter(VoiceRoomDefine.SeatViewAdapter adapter)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| adapter | [SeatViewAdapter](https://www.tencentcloud.com/document/product/647/66793#293c3d02-4706-45e4-b1f1-64e9eae8fb57) | Адаптер представления места |

**Возвращаемое значение:** void

### addObserver

Установка обратных вызовов событий.

```
void addObserver(SeatGridViewObserver observer)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| observer | [SeatGridViewObserver](https://www.tencentcloud.com/document/product/647/66793#4749ed20-b069-4691-98be-b39e4d477478) | Объект обратного вызова основного компонента |

**Возвращаемое значение:** void

### removeObserver

Удаление обратных вызовов событий.

```
void removeObserver(SeatGridViewObserver observer)
```

**Параметр:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| observer | [SeatGridViewObserver](https://www.tencentcloud.com/document/product/647/66793#4749ed20-b069-4691-98be-b39e4d477478) | Объект обратного вызова основного компонента |

**Возвращаемое значение:** void

## Определение типов

| Тип | Описание |
| --- | --- |
| [LayoutMode](https://www.tencentcloud.com/document/product/647/66793#9054f6cd-8773-447d-9139-3a65d2e9a42f) | Режимы макета списка позиций мест, поддерживаются макет элементов, макет сетки, вертикальный макет и пользовательский макет |
| [SeatViewLayoutRowAlignment](https://www.tencentcloud.com/document/product/647/66793#b22ba27c-695a-4ea9-9739-7d18450a39b1) | Выравнивание макета позиции места |
| [RequestType](https://www.tencentcloud.com/document/product/647/66793#f1f2b39d-2e01-49d4-a5eb-402564d7f0c4) | Тип заявки (заявка на выступление и приглашение на выступление) |
| [Size](https://www.tencentcloud.com/document/product/647/66793#287537f0-ad04-4e6a-b22a-4e7cea633be3) | Размер макета позиции места |
| [SeatViewLayoutConfig](https://www.tencentcloud.com/document/product/647/66793#005ea306-be1d-4523-aff0-b8cb65853266) | Информация конфигурации макета позиции микрофона |
| [SeatViewLayoutRowConfig](https://www.tencentcloud.com/document/product/647/66793#a2174da5-9786-4f90-a09e-01b3d9a99a2f) | Информация конфигурации строки макета мест |
| [RequestCallback](https://www.tencentcloud.com/document/product/647/66793#43c7b85d-9c84-4111-a3a3-b2c2e3271e17) | Обратный вызов заявки |
| [SeatViewAdapter](https://www.tencentcloud.com/document/product/647/66793#293c3d02-4706-45e4-b1f1-64e9eae8fb57) | Адаптер представления места |

### LayoutMode

Режимы макета списка позиций мест

| Тип | Описание |
| --- | --- |
| FOCUS | Макет элементов |
| GRID | Макет сетки |
| VERTICAL | Вертикальный макет |
| FREE | Пользовательский макет |

### SeatViewLayoutRowAlignment

Выравнивание макета позиции места

| Тип | Описание |
| --- | --- |
| START | Позиция места близко к началу |
| END | Позиция места близко к концу |
| CENTER | Позиция места близко к середине |
| SPACE_BETWEEN | Нет пространства перед первым и после последнего мест, остальное пространство равномерно распределено между другими местами |
| SPACE_AROUND | Половина пространства распределена перед первым и после последнего мест, остальное пространство равномерно распределено между другими местами |
| SPACE_EVENLY | Остальное пространство равномерно распределено между всеми местами |

### RequestType

Тип заявки

| Тип | Описание |
| --- | --- |
| APPLY_TO_TAKE_SEAT | Заявка на выступление |
| INVITE_TO_TAKE_SEAT | Приглашение на выступление |

### Size

Размер макета позиции места

| Тип | Описание |
| --- | --- |
| width | Ширина макета |
| height | Высота макета |

### SeatViewLayoutConfig

Информация конфигурации макета позиции микрофона

| Тип | Описание |
| --- | --- |
| rowConfigs | Список всей информации конфигурации строк в макете мест, см. [SeatViewLayoutRowConfig](https://www.tencentcloud.com/document/product/647/66793#a2174da5-9786-4f90-a09e-01b3d9a99a2f) для деталей. |
| rowSpacing | Расстояние между строками мест |

### SeatViewLayoutRowConfig

Информация конфигурации строки макета мест

| Тип | Описание |
| --- | --- |
| count | Количество мест, отображаемых в этой строке |
| seatSpacing | Горизонтальное расстояние между каждым местом в этой строке (действительно только при выравнивании START, END или CENTER) |
| seatSize | Размер макета места в этой строке |
| alignment | Выравнивание макета в этой строке ([SeatViewLayoutRowAlignment](https://www.tencentcloud.com/document/product/647/66793#b22ba27c-695a-4ea9-9739-7d18450a39b1)) |

### RequestCallback

Обратный вызов на заявку на выступление/приглашение на выступление

| API | Описание |
| --- | --- |
| [onAccepted](https://www.tencentcloud.com/document/product/647/66793#47d95d62-30bd-498f-b28d-1374aa6bc1aa) | Заявка принята |
| [onRejected](https://www.tencentcloud.com/document/product/647/66793#e11ca47d-e1a2-4262-93f5-3a47314b075f) | Заявка отклонена |
| [onCancelled](https://www.tencentcloud.com/document/product/647/66793#cfb3a227-6b8a-46ef-81ee-403888140d27) | Заявка отменена |
| [onTimeout](https://www.tencentcloud.com/document/product/647/66793#7f4dfc89-27fa-4d20-abcc-f32bcf91b443) | Истечение времени ожидания заявки |
| [onError](https://www.tencentcloud.com/document/product/647/66793#bf674805-17b7-4113-b166-6beaa22cb695) | Исключение заявки |

### SeatViewAdapter

Интерфейс адаптера представления места, вы можете настроить отображение пользовательского интерфейса каждого места путем реализации этого интерфейса.

| API | Описание |
| --- | --- |
| [createSeatView](https://www.tencentcloud.com/document/product/647/66793#23b3931d-345f-4193-82ed-f9ff8c9890cf) | Обратный вызов при создании макета одного места. |
| [updateSeatView](https://www.tencentcloud.com/document/product/647/66793#a4508d98-522b-4cc6-83f3-e1d2e2ee8bda) | Обратный вызов при обновлении представления места. |
| [updateUserVolume](https://www.tencentcloud.com/document/product/647/66793#283e2cca-68b0-48b4-92f6-cc15b40db7f2) | Обратный вызов при обновлении громкости пользователя. |

## Подробная информация об обратных вызовах событий

### onAccepted

Заявка на выступление/приглашение на выступление принято.

```
void onAccepted(TUIRoomDefine.UserInfo userInfo);
```

**Параметр:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация пользователя, ответившего на текущую заявку |

**Возвращаемое значение:** void

### onRejected

Заявка на выступление/приглашение на выступление отклонено.

```
void onRejected(TUIRoomDefine.UserInfo userInfo);
```

**Параметр:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация пользователя, ответившего на текущую заявку |

**Возвращаемое значение:** void

### onCancelled

Заявка на выступление/приглашение на выступление отменено.

```
void onCancelled(TUIRoomDefine.UserInfo userInfo);
```

**Параметр:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация пользователя, отменившего заявку |

**Возвращаемое значение:** void

### onTimeout

Истечение времени ожидания для заявки на выступление/приглашения на выступление.

```
void onTimeout(TUIRoomDefine.UserInfo userInfo);
```

**Параметр:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация пользователя, инициировавшего заявку |

**Возвращаемое значение:** void

### onError

Ошибка при заявке на выступление/приглашении на выступление.

```
void onError(TUIRoomDefine.UserInfo userInfo, TUICommonDefine.Error error, String message);
```

**Параметр:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация пользователя, инициировавшего заявку |
| error | TUICommonDefine.Error | Код ошибки |
| message | String | Сообщение об ошибке |

**Возвращаемое значение:** void

### createSeatView

Обратный вызов при создании макета одного места, требуется возвратить ваше пользовательское представление, основное представление поможет вам создать представление.

```
View createSeatView(SeatGridView seatGridView, TUIRoomDefine.SeatInfo seatInfo);
```

**Параметр:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatGridView | SeatGridView | Основной компонент голосовой комнаты чата |
| seatInfo | SeatInfo | Информация о месте |

**Возвращаемое значение:** View

### updateSeatView

Обратный вызов при обновлении представления места, вы можете обновить представление вашего места на основе информации seatInfo, возвращаемой обратным вызовом.

```
void updateSeatView(SeatGridView seatGridView, TUIRoomDefine.SeatInfo seatInfo, View seatView);
```

**Параметр:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatGridView | SeatGridView | Основной компонент голосовой комнаты чата |
| seatInfo | SeatInfo | Информация о месте |
| seatView | View | Текущее обновляемое представление места |

**Возвращаемое значение:** void

### updateUserVolume

Обратный вызов при обновлении громкости пользователя, вы можете обновить представление вашего места на основе возвращаемого уровня громкости.

```
void updateUserVolume(SeatGridView seatGridView, int volume, View s

---
*Источник (EN): [seatgridview.md](./seatgridview.md)*
