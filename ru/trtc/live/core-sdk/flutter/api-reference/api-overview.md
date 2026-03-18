# Обзор API

## Обзор

TUIRoomEngine ([rtc_room_engine](https://pub.dev/packages/rtc_room_engine)) — это компонент, разработанный для сценариев, включающих **корпоративные встречи, вебинары, онлайн-образование** и т. д., поддерживающий многопользовательские аудио- и видеоконфокусы. Он предоставляет функции управления комнатой, многопользовательское взаимодействие через TRTC, управление участниками, общий доступ к экрану и другие функции контроля встреч, а также поддерживает различные качества видео, включая стандартное, высокое и ультравысокое разрешение. Путём интеграции этого компонента вы можете добавить в своё приложение функции многопользовательских аудио- и видеоконфокусов.

### **Метод интеграции:**

В файле `pubspec.yaml` вашего проекта добавьте следующий код для интеграции TUIRoomEngine:

```
dependencies:       rtc_room_engine: latest version
```

Выполните следующую команду для установки компонента:

```
flutter pub get
```

## Список API TUIRoomEngine

API TUIRoomEngine — это интерфейс без UI для многопользовательских аудио- и видеокомнат. Вы можете использовать эти API для выполнения пользовательской инкапсуляции в соответствии с вашими потребностями.

TUIRoomEngine

### Основные методы TUIRoomEngine

| API | Описание |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/67263#sharedInstance) | Создать экземпляр TUIRoomEngine. |
| [destroyISharedinstance](https://www.tencentcloud.com/document/product/647/67263#a3b428a8-fc46-4927-abcb-642cfed08e0f) | Уничтожить экземпляр TUIRoomEngine. |
| [login](https://www.tencentcloud.com/document/product/647/67263#login) | Интерфейс входа, необходимо сначала инициализировать информацию пользователя для входа в комнату и выполнения ряда операций. |
| [logout](https://www.tencentcloud.com/document/product/647/67263#4955bdc1-5a79-4eb4-8f86-2fb73923bcb8) | Интерфейс выхода, включающий активное покидание комнаты и освобождение ресурсов. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/67263#setSelfInfo) | Установить имя пользователя и аватар локального пользователя. |
| [setLoginUserInfo](https://www.tencentcloud.com/document/product/647/67263#setLoginUserInfo) | Установить информацию о пользователе, вошедшем в систему. |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/67263#getSelfInfo) | Получить базовую информацию локального пользователя, вошедшего в систему. |
| [addObserver](https://www.tencentcloud.com/document/product/647/67263#addObserver) | Установить обратные вызовы событий. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/67263#removeObserver) | Удалить обратные вызовы событий. |

### Активный интерфейс, связанный с комнатой

| API | Описание |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/67263#createRoom) | Создать комнату. |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/67263#destroyRoom) | Распустить комнату. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/67263#enterRoom) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/67263#exitRoom) | Покинуть комнату. |
| [connectOtherRoom](https://www.tencentcloud.com/document/product/647/67263#connectOtherRoom) | Подключиться к другим комнатам. |
| [disconnectOtherRoom](https://www.tencentcloud.com/document/product/647/67263#disconnectOtherRoom) | Отключиться от других комнат. |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/67263#fetchRoomInfo) | Получить информацию о комнате. |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/67263#updateRoomNameByAdmin) | Обновить имя комнаты (могут вызывать только администраторы или владельцы группы). |
| [updateRoomSeatModeByAdmin](https://www.tencentcloud.com/document/product/647/67263#updateRoomSeatModeByAdmin) | Установить режим управления комнатой (могут вызывать только администраторы или владельцы группы). |

### Визуализация локального пользователя, управление видео

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/67263#setLocalVideoView) | Установить элемент управления для визуализации видео локального пользователя. |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/67263#openLocalCamera) | Включить локальную камеру. |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/67263#closeLocalCamera) | Выключить локальную камеру. |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/67263#updateVideoQuality) | Обновить параметры качества кодирования локального видео. |
| [updateVideoQualityEx](https://www.tencentcloud.com/document/product/647/67263#updateVideoQualityEx) | Установить параметры кодирования для видеокодека |
| [setVideoResolutionMode](https://www.tencentcloud.com/document/product/647/67263#setVideoResolutionMode) | Установить режим разрешения для видеокодека |
| [enableGravitySensor](https://www.tencentcloud.com/document/product/647/67263#enableGravitySensor) | Включить режим датчика гравитации |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/67263#startPushLocalVideo) | Начать передачу локального видео. |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/67263#stopPushLocalVideo) | Остановить передачу локального видео. |
| [startScreenSharing](https://www.tencentcloud.com/document/product/647/67263#startScreenSharing) | Начать общий доступ к экрану |
| [stopScreenSharing](https://www.tencentcloud.com/document/product/647/67263#stopScreenSharing) | Завершить общий доступ к экрану |

### Управление локальным аудио пользователя

| API | Описание |
| --- | --- |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/67263#openLocalMicrophone) | Включить локальный микрофон. |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/67263#closeLocalMicrophone) | Отключить локальный микрофон. |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/67263#updateAudioQuality) | Обновить параметры качества кодирования локального аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/67263#startPushLocalAudio) | Остановить передачу локального аудио. |
| [unMuteLocalAudio](https://www.tencentcloud.com/document/product/647/67263#stopPushLocalAudio) | Начать передачу локального аудио. |

### Визуализация удалённого пользователя, управление видео

| API | Описание |
| --- | --- |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/67263#setRemoteVideoView) | Установить элемент управления для визуализации видео удалённого пользователя. |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/67263#124ff5a0-beaa-4d55-b30d-9703290ab5c7) | Начать воспроизведение видео удалённого пользователя. |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/67263# stopPlayRemoteVideo) | Остановить воспроизведение видео удалённого пользователя. |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/67263#muteRemoteAudioStream) | Отключить звук удалённого пользователя. |

### Информация о пользователе внутри комнаты

| API | Описание |
| --- | --- |
| [getUserList](https://www.tencentcloud.com/document/product/647/67263#getUserList) | Получить список участников внутри комнаты. |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/67263#getUserInfo) | Получить информацию об участнике. |

### Управление пользователями в комнате

| API | Описание |
| --- | --- |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/67263#changeUserRole) | Изменить роль пользователя (могут вызывать только администраторы или владельцы группы). |
| [changeUserNameCard](https://www.tencentcloud.com/document/product/647/67263#changeUserNameCard) | Изменить никнейм пользователя. |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/67263#kickRemoteUserOutOfRoom) | Удалить удалённого пользователя из комнаты (могут вызывать только администраторы или владельцы группы). |
| [addCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/67263#addCategoryTagForUsers) | Добавить метку пользователю (могут вызывать только владельцы) |
| [removeCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/67263#removeCategoryTagForUsers) | Удалить метку у пользователя (могут вызывать только владельцы) |
| [getUserListByTag](https://www.tencentcloud.com/document/product/647/67263#getUserListByTag) | Получить информацию о пользователях в комнате по меткам |
| [setCustomInfoForUser](https://www.tencentcloud.com/document/product/647/67263#setCustomInfoForUser) | Установить пользовательскую информацию для участников в комнате |

### Управление говорением пользователя в комнате

| API | Описание |
| --- | --- |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/67263#disableDeviceForAllUserByAdmin) | Контролировать, могут ли все пользователи в текущей комнате включать устройства захвата аудиопотока, видеопотока. Например: запретить всем включать микрофон, камеру или общий доступ к экрану (в настоящее время доступно только в сценариях встреч, могут вызывать только администраторы или владельцы группы). |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/67263#63833efa-43b7-4e56-81dc-4417774b1b07) | Запросить у удалённого пользователя включение устройств мультимедиа (могут вызывать только администраторы или владельцы группы). |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/67263#closeRemoteDeviceByAdmin) | Отключить устройства мультимедиа удалённого пользователя (могут вызывать только администраторы или владельцы группы). |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/67263#applyToAdminToOpenLocalDevice) | Запросить включение локальных устройств мультимедиа (доступно обычным пользователям). |

### Управление позициями микрофона внутри комнат

| API | Описание |
| --- | --- |
| [setMaxSeatCount](https://www.tencentcloud.com/document/product/647/67263#setMaxSeatCount) | Установить максимальное количество микрофонов (можно установить только перед входом или созданием комнаты). |
| [getSeatList](https://www.tencentcloud.com/document/product/647/67263#getSeatList) | Получить список позиций микрофона. |
| [getSeatApplicationList](https://www.tencentcloud.com/document/product/647/67263#getSeatApplicationList) | Ведущий/администратор получает список запросов пользователей, применяющихся к микрофону в комнате. |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/67263#lockSeatByAdmin) | Заблокировать позицию микрофона (могут вызывать только администраторы или владельцы группы, включая блокировку позиции, блокировку статуса аудио и блокировку статуса видео). |
| [takeSeat](https://www.tencentcloud.com/document/product/647/67263#takeSeat) | Применить для присоединения к микрофону (нет необходимости в применении в режиме свободного говорения). |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/67263#leaveSeat) | Применить для отхода от микрофона (нет необходимости в применении в режиме свободного говорения). |
| [moveToSeat](https://www.tencentcloud.com/document/product/647/67263#moveToSeat) | Отключить микрофон |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/67263#takeUserOnSeatByAdmin) | Ведущий/администратор приглашает пользователей на сцену. |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/67263#kickUserOffSeatByAdmin) | Ведущий/администратор удаляет пользователей с микрофона. |

### Управление сигнализацией

| API | Описание |
| --- | --- |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/67263#cancelRequest) | Отменить запрос. |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/67263#responseRemoteRequest) | Ответить на запрос. |

### Отправка сообщения

| API | Описание |
| --- | --- |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/67263#disableSendingMessageByAdmin) | Отключить возможность удалённого пользователя отправлять текстовые сообщения (могут вызывать только администраторы или владельцы группы). |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/67263#disableSendingMessageForAllUser) | Отключить возможность всех пользователей отправлять текстовые сообщения (могут вызывать только администраторы или владельцы группы). |

### Дополнительные функции

| API | Описание |
| --- | --- |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/67263#setBeautyLevel) | Установить уровень эффекта фильтра красоты |
| [setWhitenessLevel](https://www.tencentcloud.com/document/product/647/67263#setWhitenessLevel) | Установить уровень эффекта фильтра отбеливания |
| [getExtension](https://www.tencentcloud.com/document/product/647/67263#getExtension) | Получить плагины |
| [getMediaDeviceManager](https://www.tencentcloud.com/document/product/647/67263#getMediaDeviceManager) | Получить класс управления устройствами |

### Связано с отладкой

| API | Описание |
| --- | --- |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/67263#callExperimentalAPI) | Вызывает экспериментальный API. |

## Событие обратного вызова TUIRoomObserver

TUIRoomObserver — это класс события обратного вызова, соответствующий TUIRoomEngine. Вы можете использовать этот обратный вызов для прослушивания нужных вам событий.

TUIRoomObserver

## TUIRoomObserver

### Обратный вызов ошибки

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/67262#onError) | Обратный вызов события ошибки |

### Обратный вызов события статуса входа

| API | Описание |
| --- | --- |
| [onKickedOffLine](https://www.tencentcloud.com/document/product/647/67262#onKickedOffLine) | Отключено другим клиентом при входе терминала. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/67262#onUserSigExpired) | Событие истечения срока действия учётных данных пользователя. |

### Обратный вызов события комнаты

| API | Описание |
| --- | --- |
| [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/67262#onRoomNameChanged) | Событие изменения имени комнаты. |
| [onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/67262#0343c6f5-0de0-4d03-ac6c-c4796f9b6434) | Событие отключения микрофонов всех пользователей в комнате. |
| [onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/67262#802c03d5-7144-428a-b332-51e63793e5db) | Событие отключения камер всех пользователей в комнате. |
| [onScreenShareForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/67262#onScreenShareForAllUserDisableChanged) | Событие отключения общего доступа к экрану всех пользователей в комнате. |
| [onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/67262#40a909c8-b39c-412d-aa58-e038e77ba856) | Событие отключения возможности отправки текстовых сообщений всеми пользователями в комнате. |
| [onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/67262#onKickedOutOfRoom) | Событие удаления из комнаты. |
| [onRoomDismissed](https://www.tencentcloud.com/document/product/647/67262#onRoomDismissed) | Событие распуска комнаты. |
| [onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/67262#onRoomSeatModeChanged) | Изменение режима микрофона комнаты |
| [onRoomUserCountChanged](https://www.tencentcloud.com/document/product/647/67262#7c8a0a9e-1f60-4e14-8a11-fa72dc7221e4) | Изменилось количество пользователей в комнате |

### Обратный вызов события пользователя внутри комнаты

| API | Описание |
| --- | --- |
| [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/67262#onRemoteUserEnterRoom) | Событие входа удалённого пользователя в комнату. |
| [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/67262#onRemoteUserLeaveRoom) | Событие выхода удалённого пользователя из комнаты. |
| [onUserRoleChanged](https://www.tencentcloud.com/document/product/647/67262#onUserRoleChanged) | Событие изменения роли пользователя. |
| [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/67262#onUserVideoStateChanged) | Событие изменения статуса видео пользователя. |
| [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/67262#onUserAudioStateChanged) | Событие изменения статуса аудио пользователя |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/67262#onUserVoiceVolumeChanged) | Событие изменения громкости голоса пользователя. |
| [onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/67262#onSendMessageForUserDisableChanged) | Событие изменения возможности отправки текстового сообщения пользователем. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/67262#onUserNetworkQualityChanged) | Событие изменения статуса сети пользователя. |
| [onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/67262#onUserScreenCaptureStopped) | Общий доступ к экрану завершён. |

### Обратный вызов события позиции микрофона комнаты

| API | Описание |
| --- | --- |
| [onRoomMaxSeatCountChanged](https://www.tencentcloud.com/document/product/647/67262#onRoomMaxSeatCountChanged) | Событие изменения максимального количества микрофонов в комнате (только в комнатах типа встреча). |
| [onSeatListChanged](https://www.tencentcloud.com/document/product/647/67262#onSeatListChanged) | Событие изменения списка позиций микрофона. |
| [onKickedOffSeat](https://www.tencentcloud.com/document/product/647/67262#4c91dcc7-f9ed-4e50-8948-763b420b0662) | Событие удаления пользователя с микрофона получено. |

### Обратный вызов события сигнализации запроса

| API | Описание |
| --- | --- |
| [onRequestReceived](https://www.tencentcloud.com/document/product/647/67262# onRequestReceived) | Событие получения сообщения запроса. |
| [onRequestCancelled](https://www.tencentcloud.com/document/product/647/67262#510d9829-0e77-421f-abd5-4323d8bb456c) | Событие получения отмены запроса. |
| [onRequestProcessed](https://www.tencentcloud.com/document/product/647/67262#onRequestProcessed) | Событие получения запроса, обработанного другим администратором/владельцем |


---
*Источник: [https://trtc.io/document/67264](https://trtc.io/document/67264)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*
