# LiveCoreView

## Обзор API

LiveCoreView — это фундаментальный элемент управления, разработанный для нашего UIKit видеотрансляции. Этот основной элемент управления предоставляет богатые API, такие как предпросмотр перед трансляцией, запуск видеотрансляции, остановка видеотрансляции, подключение к комнате трансляции с аудиторией и кросс-комнатное соединение с другими ведущими.

## Обзор API

| API | Описание |
| --- | --- |
| [LiveCoreView](https://www.tencentcloud.com/document/product/647/66145#d147f174-e55a-4ba2-bbaf-2792c9419650) | Создание объекта LiveCoreView, поддерживаются оба метода: создание через код и загрузка из XML. |
| [startCamera](https://www.tencentcloud.com/document/product/647/66145#c6f79ba4-2dc1-4d65-82b3-e52d3ef28f2f) | Запуск захвата видеокамеры и отображение захваченного видео на LiveCoreView. |
| [startMicrophone](https://www.tencentcloud.com/document/product/647/66145#1032095a-ba39-4820-aac9-6399f497ec6d) | Включение локального микрофона |
| [muteMicrophone](https://www.tencentcloud.com/document/product/647/66145#b866f4a7-1951-41b8-8629-dd613a030fd5) | Приостановка публикации локального аудиопотока |
| [stopCamera](https://www.tencentcloud.com/document/product/647/66145#61a3e2e3-2780-4f16-bdc4-9fae002c48e5) | Отключение локальной камеры |
| [stopMicrophone](https://www.tencentcloud.com/document/product/647/66145#c739e487-b83b-4a78-b432-3f84d867ffa2) | Отключение локального микрофона |
| [startLiveStream](https://www.tencentcloud.com/document/product/647/66145#fa10462e-e188-4879-9be5-2c2d6a222b6d) | Ведущий создаёт комнату трансляции и начинает трансляцию |
| [stopLiveStream](https://www.tencentcloud.com/document/product/647/66145#89f1f933-1771-4f4e-81af-5e0d38dce48e) | Ведущий останавливает трансляцию и уничтожает комнату |
| [joinLiveStream](https://www.tencentcloud.com/document/product/647/66145#8c23ef17-5f8a-4ddd-b803-f78bd3a18f17) | Зритель присоединяется к комнате трансляции ведущего |
| [leaveLiveStream](https://www.tencentcloud.com/document/product/647/66145#cdba89b2-1d72-4603-9077-c97d158e2fef) | Зритель покидает комнату трансляции ведущего |
| [requestIntraRoomConnection](https://www.tencentcloud.com/document/product/647/66145#db8d3b1f-26b4-4e79-896a-dc00cc32caac) | Зритель запрашивает соединение с ведущим |
| [cancelIntraRoomConnection](https://www.tencentcloud.com/document/product/647/66145#dedaef30-7e34-4d1d-87d3-7cad0c60a2d6) | Зритель отменяет запрос на соединение с ведущим |
| [respondIntraRoomConnection](https://www.tencentcloud.com/document/product/647/66145#00371c4a-dda3-4035-8bd2-318591fa7d0f) | Ведущий отвечает на запрос зрителя на соединение |
| [disconnectUser](https://www.tencentcloud.com/document/product/647/66145#c771b29e-ad6c-4cc6-beb6-10a0e2206b11) | Ведущий отключает подключённого зрителя |
| [terminateIntraRoomConnection](https://www.tencentcloud.com/document/product/647/66145#e8cad683-cd01-44ec-bf4b-4ce647f138fd) | Зритель самостоятельно прерывает соединение с ведущим |
| [requestCrossRoomConnection](https://www.tencentcloud.com/document/product/647/66145#fa324f97-fad6-45ac-ba1b-a85032038645) | Ведущий запрашивает соединение с другим ведущим в другой комнате |
| [cancelCrossRoomConnection](https://www.tencentcloud.com/document/product/647/66145#ff06ff0c-cd0f-4cc2-9491-e228c98eb569) | Ведущий отменяет запрос на соединение с другим ведущим в другой комнате |
| [respondToCrossRoomConnection](https://www.tencentcloud.com/document/product/647/66145#95b1d9e0-7929-4029-b55c-c914ab70bb18) | Ведущий отвечает на запрос на соединение |
| [terminateCrossRoomConnection](https://www.tencentcloud.com/document/product/647/66145#5630e92d-5e13-4c2b-b588-3d684046e828) | Ведущий прерывает соединение |
| [registerConnectionObserver](https://www.tencentcloud.com/document/product/647/66145#bc6933f2-783a-4059-8164-d4566dbebe06) | Регистрация обратного вызова события соединения |
| [unregisterConnectionObserver](https://www.tencentcloud.com/document/product/647/66145#b0de0bf4-56d2-4b8d-baa3-165e2dab8a3c) | Отмена регистрации обратного вызова события соединения |
| [setLayoutMode](https://www.tencentcloud.com/document/product/647/66145#c69ad7f9-71ab-4b3b-8529-8e1a10abebd1) | Установка режима разметки видеоэкрана подключённого ведущего |
| [setVideoViewAdapter](https://www.tencentcloud.com/document/product/647/66145#58713969-f561-4dd1-aa5d-f188888358dd) | Установка адаптера представлений для добавления виджетов на видеоэкран ведущего |

## Подробное описание API

### LiveCoreView

Создание экземпляра объекта LiveCoreView. Поддерживает оба метода: создание через код и загрузку из XML.

```
public LiveCoreView(Context context)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| context | Context | Объект контекста Android |

**Возвращаемое значение: LiveCoreView**

### startCamera

Запуск захвата видеокамеры и отображение захваченного видео на представлении LiveCoreView.

```
public void startCamera(boolean useFrontCamera, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| useFrontCamera | boolean | true: использовать фронтальную камеру, false: использовать задную камеру |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### startMicrophone

Включение локального микрофона.

```
void startMicrophone(ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### muteMicrophone

Приостановка публикации локального аудиопотока.

```
void muteMicrophone(boolean mute)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| mute | boolean | true: приостановить публикацию видеопотока, false: нормальная публикация видеопотока |

**Возвращаемое значение:**void

### stopCamera

Отключение локальной камеры.

```
void stopCamera()
```

**Параметры:**

**Возвращаемое значение:**void

### stopMicrophone

Отключение локального микрофона.

```
void stopMicrophone()
```

**Параметры:**

**Возвращаемое значение:**void

### startLiveStream

Ведущий создаёт комнату трансляции и начинает трансляцию.

```
void startLiveStream(RoomInfo roomInfo, GetRoomInfoCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomInfo | RoomInfo | Информация для создания комнаты трансляции |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### stopLiveStream

Ведущий останавливает трансляцию и уничтожает комнату.

```
void stopLiveStream(ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### joinLiveStream

Зритель присоединяется к комнате трансляции ведущего.

```
void joinLiveStream(String roomId, GetRoomInfoCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | ID комнаты трансляции |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### leaveLiveStream

Зритель покидает комнату трансляции ведущего.

```
void leaveLiveStream(ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### requestIntraRoomConnection

Зритель запрашивает соединение с ведущим.

```
void requestIntraRoomConnection(String userId, int timeout, boolean openCamera, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя. Если оставить пусто, представляет ID ведущего. |
| timeout | int | Время ожидания запроса в секундах. |
| openCamera | boolean | Включать ли камеру после успешного соединения с микрофоном. true: видео соединение, false: только аудио соединение. |
| callback | ActionCallback | Обратный вызов операции. |

**Возвращаемое значение:**void

### cancelIntraRoomConnection

Зритель отменяет запрос на соединение с ведущим.

```
void cancelIntraRoomConnection(String userId, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя, который отменяет соединение с микрофоном. Если оставить пусто, представляет ID ведущего. |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### respondIntraRoomConnection

Ведущий отвечает на запрос зрителя на соединение.

```
void respondIntraRoomConnection(String userId, boolean isAccepted, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя, отвечающего на запрос |
| isAccepted | isAccepted | Принять ли запрос на соединение с микрофоном. true: принять запрос, false: отклонить запрос |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### disconnectUser

Ведущий отключает подключённого зрителя.

```
void disconnectUser(String userId, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя, который должен быть отключен ведущим |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### terminateIntraRoomConnection

Зритель самостоятельно прерывает соединение с ведущим.

```
void terminateIntraRoomConnection()
```

**Параметры: нет**

**Возвращаемое значение:**void

### requestCrossRoomConnection

Ведущий запрашивает соединение с другим ведущим в другой комнате.

```
void requestCrossRoomConnection(String roomId, int timeout, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | ID комнаты для запроса кросс-комнатного соединения. |
| timeout | int | Время ожидания запроса в секундах. |
| callback | ActionCallback | Обратный вызов операции. |

**Возвращаемое значение:**void

### cancelCrossRoomConnection

Ведущий отменяет запрос на соединение с другим ведущим в другой комнате.

```
void cancelCrossRoomConnection(String roomId, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | ID комнаты для отмены соединения |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### respondToCrossRoomConnection

Ведущий отвечает на запрос на соединение.

```
void respondToCrossRoomConnection(String roomId, boolean isAccepted, ActionCallback callback)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | ID комнаты для ответа на запрос соединения |
| isAccepted | boolean | Согласиться ли на соединение, true: согласиться, false: отклонить |
| callback | ActionCallback | Обратный вызов операции |

**Возвращаемое значение:**void

### terminateCrossRoomConnection

Ведущий прерывает соединение.

```
void terminateCrossRoomConnection()
```

**Параметры: нет**

**Возвращаемое значение:**void

### registerConnectionObserver

Регистрация обратного вызова события соединения.

```
void registerConnectionObserver(ConnectionObserver observer)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| observer | [ConnectionObserver](https://www.tencentcloud.com/document/product/647/66145#d8860caf-d045-431b-becc-d4f8b4e152b1) | Объект обратного вызова для событий соединения |

**Возвращаемое значение:**void

### unregisterConnectionObserver

Отмена регистрации обратного вызова события соединения.

```
void unregisterConnectionObserver(ConnectionObserver observer)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| observer | [ConnectionObserver](https://www.tencentcloud.com/document/product/647/66145#d8860caf-d045-431b-becc-d4f8b4e152b1) | Объект обратного вызова для событий соединения |

**Возвращаемое значение:**void

### setLayoutMode

Установка режима разметки видеоэкрана подключённого ведущего.

```
void setLayoutMode(LayoutMode layoutModel, String layoutJson)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| layoutModel | [LayoutMode](https://www.tencentcloud.com/document/product/647/66145#9054f6cd-8773-447d-9139-3a65d2e9a42f) | Режим разметки во время соединения, поддерживаются сеточная разметка, разметка с плавающим окном и пользовательская разметка. |
| layoutJson | String | Строка JSON разметки |

**Возвращаемое значение:**void

### setVideoViewAdapter

Установка адаптера представлений для добавления виджетов на видеоэкран ведущего.

```
void setVideoViewAdapter(LiveCoreViewDefine.VideoViewAdapter viewAdapter)
```

**Параметры:**

| Параметр | Тип | Значение |
| --- | --- | --- |
| viewAdapter | [VideoViewAdapter](https://www.tencentcloud.com/document/product/647/66145#43c7b85d-9c84-4111-a3a3-b2c2e3271e17) | Адаптер представлений для добавления виджетов на видеоэкран ведущего |

**Возвращаемое значение:**void

## Определение типов

| Тип | Описание |
| --- | --- |
| [ConnectionObserver](https://www.tencentcloud.com/document/product/647/66145#d8860caf-d045-431b-becc-d4f8b4e152b1) | Установка событий обратного вызова для соединений основного элемента управления. |
| [LayoutMode](https://www.tencentcloud.com/document/product/647/66145#9054f6cd-8773-447d-9139-3a65d2e9a42f) | Режим разметки во время соединения, поддерживаются сеточная разметка, разметка с плавающим окном и пользовательская разметка. |
| [VideoViewAdapter](https://www.tencentcloud.com/document/product/647/66145#43c7b85d-9c84-4111-a3a3-b2c2e3271e17) | Интерфейс адаптера соединения представлений, который позволяет добавлять виджеты к каждому представлению аудио и видеопотока путём реализации этого интерфейса. |

### ConnectionObserver

| Тип | Описание |
| --- | --- |
| [onConnectedUsersUpdated](https://www.tencentcloud.com/document/product/647/66145#698b164e-c775-48f1-88b7-85ea8c18e94c) | Обратный вызов при изменении списка подключённых пользователей. |
| [onUserConnectionRequest](https://www.tencentcloud.com/document/product/647/66145#485a04e9-742d-4cbb-901d-cf1018cc71e5) | Обратный вызов при получении запроса на соединение. |
| [onUserConnectionCancelled](https://www.tencentcloud.com/document/product/647/66145#2b9086aa-a2d0-4cad-962e-b35e6e29dc95) | Обратный вызов при получении запроса на отмену соединения. |
| [onUserConnectionAccepted](https://www.tencentcloud.com/document/product/647/66145#51b2b526-d288-48b4-96bb-abb28bf03186) | Обратный вызов при одобрении запроса на соединение. |
| [onUserConnectionRejected](https://www.tencentcloud.com/document/product/647/66145#8f985ad2-a119-49d1-b66d-a775730a04bf) | Обратный вызов при отклонении запроса на соединение. |
| [onUserConnectionTimeout](https://www.tencentcloud.com/document/product/647/66145#0619d6ab-e8d0-4594-89a3-4c58b6a63659) | Обратный вызов при истечении времени ожидания запроса на соединение. |
| [onUserConnectionTerminated](https://www.tencentcloud.com/document/product/647/66145#c97e43b0-87e5-4cb1-8256-cb27613f1616) | Обратный вызов при отключении ведущим соединения с микрофоном этого зрителя. |
| [onUserConnectionExited](https://www.tencentcloud.com/document/product/647/66145#844be3c0-8638-4dce-aed6-01786eb8ab5d) | Обратный вызов при самостоятельном отключении зрителем. |
| [onConnectedRoomsUpdated](https://www.tencentcloud.com/document/product/647/66145#4c10617c-5a25-4e81-8d19-06608d28d82b) | Обратный вызов при изменении списка кросс-комнатных соединений. |
| [onCrossRoomConnectionRequest](https://www.tencentcloud.com/document/product/647/66145#2a1ef273-7b94-4cdf-b263-84bd0072914b) | Обратный вызов при получении запроса на кросс-комнатное соединение. |
| [onCrossRoomConnectionCancelled](https://www.tencentcloud.com/document/product/647/66145#e8e761fe-e391-4987-a90a-a1eeff2ea04c) | Обратный вызов при получении запроса на отмену кросс-комнатного соединения. |
| [onCrossRoomConnectionAccepted](https://www.tencentcloud.com/document/product/647/66145#10bfc883-124d-4cff-8f8f-2ac231c12b2a) | Полученный обратный вызов согласия на кросс-комнатное соединение |
| [onCrossRoomConnectionRejected](https://www.tencentcloud.com/document/product/647/66145#185047be-2bde-42aa-ac94-50b6ce3d4243) | Полученный обратный вызов отклонения кросс-комнатного соединения |
| [onCrossRoomConnectionTimeout](https://www.tencentcloud.com/document/product/647/66145#de5d609d-132a-4bb0-b73f-c93906a9035a) | Полученный обратный вызов истечения времени ожидания кросс-комнатного соединения. |
| [onCrossRoomConnectionExited](https://www.tencentcloud.com/document/product/647/66145#b8ab1647-b00e-4b9d-ac70-d069257a1c3f) | Полученный обратный вызов отключения кросс-комнатного соединения. |
| [onRoomDismissed](https://www.tencentcloud.com/document/product/647/66145#8aa11fb4-f463-4aa7-a581-f67239f57757) | Полученный обратный вызов при завершении комнаты. |

### LayoutMode

Режим разметки во время соединения

| Тип | Описание |
| --- | --- |
| GRID_LAYOUT | Сеточная разметка. |
| FLOAT_LAYOUT | Разметка с плавающим окном. |
| FREE_LAYOUT | Пользовательская разметка. |

### VideoViewAdapter

Интерфейс адаптера соединения представлений, который позволяет добавлять виджеты к каждому представлению аудио и видеопотока путём реализации этого интерфейса.

| API | Описание |
| --- | --- |
| [createCoGuestView](https://www.tencentcloud.com/document/product/647/66145#47d95d62-30bd-498f-b28d-1374aa6bc1aa) | Обратный вызов при создании представления для зрителя с соединением микрофона. Представление, созданное через этот API, будет отображаться на представлении зрителя с соединением. |
| [updateCoGuestView](https://www.tencentcloud.com/document/product/647/66145#23b3931d-345f-4193-82ed-f9ff8c9890cf) | Обратный вызов при обновлении представления зрителя с соединением. |
| [createCoHostView](https://www.tencentcloud.com/document/product/647/66145#a4508d98-522b-4cc6-83f3-e1d2e2ee8bda) | Обратный вызов при создании представления подключённого ведущего, представление, созданное через этот API, будет отображаться на представлении подключённого ведущего. |
| [updateCoHostView](https://www.tencentcloud.com/document/product/647/66145#283e2cca-68b0-48b4-92f6-cc15b40db7f2) | Обратный вызов при обновлении представления подключённого ведущего. |

## Подробное описание событий обратного вызова

### onConnectedUsersUpdated

Обратный вызов при изменении списка подключённых пользователей.

```
void onConnectedUsersUpdated(List<UserInfo> userList, List<UserInfo> joinList, List<UserInfo> leaveList);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userList | List<UserInfo> | Список подключённых пользователей |
| joinList | List<UserInfo> | Вновь подключённые пользователи |
| leaveList | List<UserInfo> | Пользователи, которые отключились |

**Возвращаемое значение:**void

### onUserConnectionRequest

Обратный вызов при получении запроса на соединение.

```
void onUserConnectionRequest(UserInfo inviterUser);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| inviterUser | UserInfo | Информация о пользователе, запрашивающем соединение |

**Возвращаемое значение:**void

### onUserConnectionCancelled

Обратный вызов при получении запроса на отмену соединения.

```
void onUserConnectionCancelled(UserInfo inviterUser);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| inviterUser | UserInfo | Информация о пользователе, отменяющем соединение |

**Возвращаемое значение:**void

### onUserConnectionAccepted

Обратный вызов при одобрении запроса на соединение.

```
void onUserConnectionAccepted(UserInfo userInfo);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация о пользователе, согласившемся на соединение с микрофоном |

**Возвращаемое значение:**void

### onUserConnectionRejected

Обратный вызов при отклонении запроса на соединение.

```
void onUserConnectionRejected(UserInfo userInfo);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация о пользователе, отклонившем соединение с микрофоном |

**Возвращаемое значение:**void

### onUserConnectionTimeout

Обратный вызов при истечении времени ожидания запроса на соединение.

```
void onUserConnectionTimeout(UserInfo userInfo);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация о пользователе, у которого истекло время ожидания запроса на соединение с микрофоном |

**Возвращаемое значение:**void

### onUserConnectionTerminated

Обратный вызов при отключении ведущим соединения с микрофоном этого зрителя.

```
vvoid onUserConnectionTerminated();
```

**Параметр: нет**

**Возвращаемое значение:**void

### onUserConnectionExited

Обратный вызов при отключении подключённого пользователя.

```
void onUserConnectionExited(UserInfo userInfo);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | UserInfo | Информация о пользователе |

**Возвращаемое значение:**void

### onConnectedRoomsUpdated

Обратный вызов при изменении списка подключённых комнат.

```
void onConnectedRoomsUpdated(List<RoomInfo> roomList);
```

---
*Источник (EN): [livecoreview.md](./livecoreview.md)*
