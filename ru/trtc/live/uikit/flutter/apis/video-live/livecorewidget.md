# LiveCoreWidget

## Введение в API

LiveCoreWidget — это базовый элемент управления, разработанный для UIKit видеотрансляции. Этот основной элемент управления предоставляет различные API, включая предварительный просмотр перед трансляцией, начало видеотрансляции, остановку видеотрансляции, подключение комнаты трансляции с аудиторией и кросс-комнатное подключение с другими трансляторами.

## Обзор API

| **API** | **Описание** |
| --- | --- |
| [LiveCoreController](https://www.tencentcloud.com/document/product/647/71717#9dc179ef-0d86-4141-9977-7ff13303e767) | Создать объект LiveCoreController |
| [LiveCoreWidget](https://www.tencentcloud.com/document/product/647/71717#LiveCoreView) | Создать объект LiveCoreWidget. |
| [startCamera](https://www.tencentcloud.com/document/product/647/71717#startCamera) | Начать захват камеры и отобразить экран на LiveCoreView. |
| [startMicrophone](https://www.tencentcloud.com/document/product/647/71717#startMicrophone) | Открыть локальный микрофон |
| [muteMicrophone](https://www.tencentcloud.com/document/product/647/71717#muteMicrophone) | Приостановить публикацию локального аудиопотока |
| [unmuteMicrophone](https://www.tencentcloud.com/document/product/647/71717#f31392be-e46b-4485-a3a3-902a9049d6e7) | Возобновить публикацию приостановленного локального аудиопотока |
| [stopCamera](https://www.tencentcloud.com/document/product/647/71717#stopCamera) | Выключить локальную камеру |
| [stopMicrophone](https://www.tencentcloud.com/document/product/647/71717#stopMicrophone) | Закрыть локальный микрофон |
| [startLiveStream](https://www.tencentcloud.com/document/product/647/71717#startLiveStream) | Транслятор создает комнату трансляции и начинает трансляцию |
| [stopLiveStream](https://www.tencentcloud.com/document/product/647/71717#stopLiveStream) | Транслятор останавливает трансляцию и удаляет комнату трансляции |
| [joinLiveStream](https://www.tencentcloud.com/document/product/647/71717#joinLiveStream) | Аудитория присоединяется к определенной комнате трансляции |
| [leaveLiveStream](https://www.tencentcloud.com/document/product/647/71717#leaveLiveStream) | Аудитория покидает определенную комнату трансляции |
| [requestIntraRoomConnection](https://www.tencentcloud.com/document/product/647/71717#requestIntraRoomConnection) | Аудитория запрашивает подключение с трансляторм |
| [cancelIntraRoomConnection](https://www.tencentcloud.com/document/product/647/71717#cancelIntraRoomConnection) | Отменить запрос на подключение с трансляторм |
| [respondIntraRoomConnection](https://www.tencentcloud.com/document/product/647/71717#respondIntraRoomConnection) | Транслятор отвечает на запрос аудитории на подключение |
| [disconnectUser](https://www.tencentcloud.com/document/product/647/71717#disconnectUser) | Транслятор отключает аудиторию |
| [terminateIntraRoomConnection](https://www.tencentcloud.com/document/product/647/71717#terminateIntraRoomConnection) | Аудитория отключается от транслятора |
| [requestCrossRoomConnection](https://www.tencentcloud.com/document/product/647/71717#requestCrossRoomConnection) | Транслятор запрашивает кросс-комнатное подключение с другим трансляторм |
| [cancelCrossRoomConnection](https://www.tencentcloud.com/document/product/647/71717#cancelCrossRoomConnection) | Отменить запрос на кросс-комнатное подключение с другим трансляторм |
| [respondToCrossRoomConnection](https://www.tencentcloud.com/document/product/647/71717#respondToCrossRoomConnection) | Транслятор отвечает на запрос на подключение |
| [terminateCrossRoomConnection](https://www.tencentcloud.com/document/product/647/71717#terminateCrossRoomConnection) | Транслятор отключается |
| [registerConnectionObserver](https://www.tencentcloud.com/document/product/647/71717#registerConnectionObserver) | Зарегистрировать обратный вызов для события подключения |
| [unregisterConnectionObserver](https://www.tencentcloud.com/document/product/647/71717#unregisterConnectionObserver) | Отменить регистрацию обратного вызова для события подключения |
| [requestBattle](https://www.tencentcloud.com/document/product/647/71717#5a298e69-e93d-4986-8406-9cdc0e994b54) | Инициировать запрос на битву |
| [cancelBattle](https://www.tencentcloud.com/document/product/647/71717#0228de17-fcaa-49ca-8dc5-a046020dd232) | Отменить запрос на битву |
| [respondToBattle](https://www.tencentcloud.com/document/product/647/71717#93c6c3bb-5e1d-46d6-bd91-ce6e43d17be9) | Ответить на запрос битвы |
| [terminateBattle](https://www.tencentcloud.com/document/product/647/71717#95c773bf-2602-42d0-82f9-d4759045b0ed) | Завершить PK |
| [registerBattleObserver](https://www.tencentcloud.com/document/product/647/71717#18d3b663-c086-4e7c-875c-6b6508bd0de1) | Зарегистрировать обратный вызов для события PK |
| [unregisterBattleObserver](https://www.tencentcloud.com/document/product/647/71717#565c44fe-d5f9-4d13-998d-b4ed4c54c111) | Отменить регистрацию обратного вызова для события PK |
| [setLayoutMode](https://www.tencentcloud.com/document/product/647/71717#setLayoutMode) | Установить режим макета для видеоизображения подключенного хоста |
| [startPreloadVideoStream](#ba916442-759a-4d6a-b7d0-7b2bc25607a1) | Начать предварительный просмотр видеопотока комнаты. |
| [stopPreloadVideoStream](#dae12088-a34a-441b-8cf9-363ea3282097) | Остановить предварительный просмотр видеопотока комнаты. |

## Детали API

### LiveCoreController

Создать экземпляр объекта LiveCoreController.

```
LiveCoreController()
```

**Возвращаемое значение:** LiveCoreController

### LiveCoreWidget

Создать экземпляр объекта LiveCoreWidget.

```
LiveCoreWidget(    {super.key,    required this.controller,    this.videoWidgetBuilder});
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| key | Key? | Flutter использует параметры для определения способа замены старого элемента управления новым |
| controller | [LiveCoreController](https://www.tencentcloud.com/document/product/647/71717#9dc179ef-0d86-4141-9977-7ff13303e767) | Контроллер LiveCoreWidget, отвечающий за предоставление API сценариев трансляции |
| videoWidgetBuilder | [VideoWidgetBuilder](https://www.tencentcloud.com/document/product/647/71717#c80fba60-cd47-4c93-afbe-64caf4428951) | Конструктор пользовательского элемента управления представлением |

**Возвращаемое значение:** LiveCoreWidget

### startCamera

Начать захват камеры и отобразить экран на LiveCoreWidget.

```
Future<TUIActionCallback> startCamera(bool useFrontCamera)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| useFrontCamera | bool | true: использовать фронтальную камеру; false: использовать тыльную камеру |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### startMicrophone

Открыть локальный микрофон.

```
Future<TUIActionCallback> startMicrophone()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### muteMicrophone

Приостановить публикацию локального аудиопотока.

```
void muteMicrophone()
```

**Возвращаемое значение:** void

### unmuteMicrophone

Возобновить публикацию приостановленного локального аудиопотока.

```
Future<TUIActionCallback> unmuteMicrophone()
```

**Возвращаемое значение:** void

### stopCamera

Выключить локальную камеру.

```
void stopCamera()
```

**Возвращаемое значение:** void

### stopMicrophone

Закрыть локальный микрофон.

```
void stopMicrophone()
```

**Возвращаемое значение:** void

### startLiveStream

Транслятор создает комнату трансляции и начинает трансляцию.

```
Future<TUIValueCallBack<TUIRoomInfo>> startLiveStream(TUIRoomInfo roomInfo)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomInfo | [TUIRoomInfo](https://www.tencentcloud.com/document/product/647/67259#RoomInfo) | Создать информацию о комнате трансляции |

**Возвращаемое значение:** Future<[TUIValueCallBack](https://www.tencentcloud.com/document/product/647/67259#TUIValueCallBack%3CT%3E)<[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/67259#RoomInfo)>>

### stopLiveStream

Транслятор останавливает трансляцию и удаляет комнату трансляции.

```
Future<TUIActionCallback> stopLiveStream()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### joinLiveStream

Аудитория присоединяется к определенной комнате трансляции.

```
Future<TUIValueCallBack<TUIRoomInfo>> joinLiveStream(String roomId)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomId | String | ID комнаты трансляции |

**Возвращаемое значение:** Future<[TUIValueCallBack](https://www.tencentcloud.com/document/product/647/67259#TUIValueCallBack%3CT%3E)<[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/67259#RoomInfo)>>

### leaveLiveStream

Аудитория покидает определенную комнату трансляции.

```
Future<TUIActionCallback> leaveLiveStream()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### requestIntraRoomConnection

Аудитория запрашивает подключение с трансляторм.

```
Future<TUIActionCallback> requestIntraRoomConnection(    String userId,    int timeout,     bool openCamera)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| userId | String | ID пользователя. Если введен ID транслятора, это означает, что аудитория запрашивает подключение с трансляторм (по умолчанию используется ID пользователя транслятора, если введена пустая строка). Для других ID пользователей это представляет приглашение транслятора соответствующему пользователю подключиться. |
| timeout | int | Продолжительность истечения запроса в секундах. |
| openCamera | bool | Открыть ли камеру при успехе. true: видеокоммуникация, false: подключение аудиомикрофона. |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### cancelIntraRoomConnection

Отменить запрос на подключение с трансляторм.

```
Future<TUIActionCallback> cancelIntraRoomConnection(String userId)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| userId | String | ID пользователя для отмены подключения микрофона. Если введен ID транслятора, это означает отмену аудиторией запроса на подключение с трансляторм (пустая строка по умолчанию использует ID пользователя транслятора). Для других ID пользователей это означает отмену трансляторм приглашения на подключение соответствующему пользователю. |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### respondIntraRoomConnection

Транслятор отвечает на запрос аудитории на подключение.

```
Future<TUIActionCallback> respondIntraRoomConnection(String userId, bool isAccepted)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| userId | String | ID пользователя аудитории ответа транслятора на подключение в комнате трансляции. Если импортирован ID пользователя транслятора, это означает ответ аудитории на приглашение транслятора (по умолчанию используется ID пользователя транслятора при вводе пустой строки). |
| isAccepted | bool | Принять ли запрос на подключение микрофона. true: предоставить запрос, false: отклонить запрос. |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### disconnectUser

Транслятор отключает аудиторию.

```
Future<TUIActionCallback> disconnectUser(String userId)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| userId | String | ID пользователя, который должен отключить транслятор |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### terminateIntraRoomConnection

Аудитория отключается от транслятора.

```
Future<TUIActionCallback> terminateIntraRoomConnection()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### requestCrossRoomConnection

Транслятор запрашивает кросс-комнатное подключение с другим трансляторм.

```
Future<TUIValueCallBack<TUIConnectionCode?>> requestCrossRoomConnection(String roomId, int timeout)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomId | String | ID комнаты для запроса кросс-комнатного подключения. |
| timeout | int | Продолжительность истечения запроса в секундах. |

**Возвращаемое значение:** Future<[TUIValueCallBack](https://www.tencentcloud.com/document/product/647/67259#TUIValueCallBack%3CT%3E)<[TUIConnectionCode](https://www.tencentcloud.com/document/product/647/69265#92daac9cd74ffae905ec2f0dbd85a61e)?>>

### cancelCrossRoomConnection

Отменить запрос на кросс-комнатное подключение с другим трансляторм.

```
Future<TUIActionCallback> cancelCrossRoomConnection(String roomId)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomId | String | ID комнаты для отмены подключения |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### respondToCrossRoomConnection

Транслятор отвечает на запрос на подключение.

```
Future<TUIActionCallback> respondToCrossRoomConnection(String roomId, bool isAccepted)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomId | String | ID комнаты для ответа на подключение |
| isAccepted | bool | Согласиться ли на подключение. true: согласиться на подключение, false: отклонить подключение. |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### terminateCrossRoomConnection

Транслятор отключается.

```
Future<TUIActionCallback> terminateCrossRoomConnection()
```

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### registerConnectionObserver

Зарегистрировать обратный вызов для события подключения.

```
void registerConnectionObserver(ConnectionObserver observer)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| observer | [ConnectionObserver](https://www.tencentcloud.com/document/product/647/71717#4749ed20-b069-4691-98be-b39e4d477478) | объект обратного вызова для события подключения |

**Возвращаемое значение:** void

### unregisterConnectionObserver

Отменить регистрацию обратного вызова для события подключения.

```
void unregisterConnectionObserver(ConnectionObserver observer)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| observer | [ConnectionObserver](https://www.tencentcloud.com/document/product/647/71717#4749ed20-b069-4691-98be-b39e4d477478) | объект обратного вызова для события подключения |

**Возвращаемое значение:** void

### requestBattle

Инициировать запрос на битву.

```
Future<TUIValueCallBack<BattleRequestCallback>> requestBattle(    TUIBattleConfig config,     List<String> userIdList,     int timeout)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| config | [TUIBattleConfig](https://www.tencentcloud.com/document/product/647/69266#6ca8b8898efedde803c17d8513bbcae7) | Конфигурация параметров PK, включая продолжительность PK и расширенную информацию. PK в настоящее время поддерживает максимальную продолжительность 300 секунд. |
| userIdList | List<String> | Пригласить userId владельца комнаты на PK |
| timeout | int | Продолжительность истечения запроса PK в секундах |

**Возвращаемое значение:** Future<[TUIValueCallBack](https://www.tencentcloud.com/document/product/647/67259#TUIValueCallBack%3CT%3E)<[BattleRequestCallback](https://www.tencentcloud.com/document/product/647/71717#c6cb7126-6f5a-40d7-af7d-1dbf39971e27)>>

### cancelBattle

Отменить запрос на битву.

```
Future<TUIActionCallback> cancelBattle(String battleId, List<String> userIdList)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| battleId | String | Уникальное представление PK |
| userIdList | List<String> | Отменить приглашение userId владельца комнаты на PK |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### respondToBattle

Ответить на запрос битвы.

```
Future<TUIActionCallback> respondToBattle(String battleId, bool isAccepted)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| battleId | String | Уникальное представление PK |
| isAccepted | bool | Предоставить приглашение PK |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### terminateBattle

Завершить PK.

```
Future<TUIActionCallback> terminateBattle(String battleId)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| battleId | String | Уникальное представление PK |

**Возвращаемое значение:** Future<[TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback)>

### registerBattleObserver

Зарегистрировать обратный вызов для события PK.

```
void registerBattleObserver(BattleObserver observer)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| observer | [BattleObserver](https://www.tencentcloud.com/document/product/647/71717#5ae5500d-fffd-4088-b14c-f5e7977fe7db) | объект обратного вызова для события PK |

**Возвращаемое значение:** void

### unregisterBattleObserver

Отменить регистрацию обратного вызова для события подключения.

```
void unregisterBattleObserver(BattleObserver observer)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| observer | [BattleObserver](https://www.tencentcloud.com/document/product/647/71717#5ae5500d-fffd-4088-b14c-f5e7977fe7db) | объект обратного вызова для события PK |

**Возвращаемое значение:** void

### setLayoutMode

Установить режим макета для видеоизображения подключенного хоста.

```
void setLayoutMode(    LayoutMode layoutMode,     bool showEmptySeat,    String? layoutJson)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| layoutMode | LayoutMode | Режим макета при подключении поддерживает макет сетки, макет плавающего окна и пользовательский макет. |
| showEmptySeat | bool | Отображать ли пустые слоты микрофона (недоступно) |
| layoutJson | String? | Строка json для макета. Для конкретного использования см. [Установка пользовательского макета](https://www.tencentcloud.com/document/product/647/69844#c8b2a34d-a77c-43cc-aede-5de27fe4e42b). |

**Возвращаемое значение:** void

### startPreloadVideoStream

Начать предварительный просмотр видеопотока комнаты.

```
void startPreloadVideoStream(    String roomId,    bool isMuteAudio,     int viewId,    TUIPlayCallback? playCallback)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomId | String | Номер комнаты для предварительного просмотра видеопотока |
| isMuteAudio | bool | Отключить ли звук видеопотока предварительного просмотра |
| viewId | int | ID представления, возвращаемый при создании VideoView |
| playCallback | TUIPlayCallback? | Функция обратного вызова видеопотока предварительного просмотра |

**Возвращаемое значение:** void

### stopPreloadVideoStream

Остановить предварительный просмотр видеопотока комнаты.

```
void stopPreloadVideoStream(String roomId)
```

**Параметры:**

| **Параметр** | **Тип** | **Значение** |
| --- | --- | --- |
| roomId | String | Остановить предварительный просмотр видеопотока номера комнаты |

**Возвращаемое значение:** void

## Определение типа

| Тип | Описание |
| --- | --- |
| [LayoutMode](https://www.tencentcloud.com/document/product/647/71717#9054f6cd-8773-447d-9139-3a65d2e9a42f) | Режим макета при подключении |
| [CoHostUser](https://www.tencentcloud.com/document/product/647/71717#c6cb7126-6f5a-40d7-af7d-1dbf39971e27) | Данные подключенного пользователя |
| [BattleUserWidgetModel](https://www.tencentcloud.com/document/product/647/71717#c0172cf5-a08d-4749-b91f-baab3b1a8566) | Данные местоположения представления пользователя PK |
| [BattleRequestCallback](https://www.tencentcloud.com/document/product/647/71717#c6cb7126-6f5a-40d7-af7d-1dbf39971e27) | Обратный вызов результата запроса битвы |
| [CoGuestWidgetBuilder](https://www.tencentcloud.com/document/product/647/71717#2059fa21-01e7-4767-a658-f813872e6de1) | Конструктор элемента управления представлением для прямой совместной трансляции |
| [CoHostWidgetBuilder](https://www.tencentcloud.com/document/product/647/71717#5bd38bde-fe02-401a-b32e-b65fc5c12c92) | Конструктор элемента управления представлением для подключения |
| [BattleWidgetBuilder](https://www.tencentcloud.com/document/product/647/71717#a532d664-4ce5-4018-afe9-8ed4bf15ee9c) | Конструктор элемента управления представлением видео хоста при PK |
| [BattleContainerWidgetBuilder](https://www.tencentcloud.com/document/product/647/71717#0310762a-6c8a-4c27-a600-b60fad1ac6c3) | Конструктор элемента управления полноэкранным представлением для PK |
| [VideoWidgetBuilder](https://www.tencentcloud.com/document/product/647/71717#c80fba60-cd47-4c93-afbe-64caf4428951) | Конструктор пользовательского элемента управления представлением |
| [OnConnectedUsersUpdated](https://www.tencentcloud.com/document/product/647/71717#92c1c3a0-a443-409f-8387-d9a919bc126a) | Обратный вызов для изменений в списке пользователей при подключении микрофона |
| [OnUserConnectionRequest](https://www.tencentcloud.com/document/product/647/71717#27bbd67b-3219-4eab-bc33-6cfe2fbf22d8) | Обратный вызов для полученного запроса на подключение микрофона |
| [OnUserConnectionCancelled](https://www.tencentcloud.com/document/product/647/71717#599f86a6-6279-

---
*Источник (EN): [livecorewidget.md](./livecorewidget.md)*
