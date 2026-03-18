# Обзор API

## Обзор

TUIRoomEngine ([rtc_room_engine](https://pub.dev/packages/rtc_room_engine)) — это компонент, разработанный для сценариев корпоративных встреч, вебинаров, онлайн-обучения и т. д., поддерживающий многопользовательские аудио и видеоконференции. Он предоставляет функции управления комнатой, многопользовательское взаимодействие TRTC, управление участниками, общий доступ к экрану и другие функции управления встречами, а также поддерживает различные качества видео, включая стандартное, высокое и сверхвысокое разрешение. Интегрировав этот компонент, вы можете добавить функции многопользовательского аудио и видеообщения в вашу приложение.

### **Метод интеграции:**

В `pubspec.yaml` вашего проекта добавьте следующий код для интеграции TUIRoomEngine:

```
dependencies:       rtc_room_engine: latest version
```

Выполните следующую команду для установки компонента:

```
flutter pub get
```

## Список API TUIRoomEngine

API TUIRoomEngine — это интерфейс без пользовательского интерфейса компонента аудио-видео вызовов. Вы можете использовать этот набор API для настраиваемой упаковки в соответствии с вашими потребностями.

TUIRoomEngine

### Основные методы TUIRoomEngine

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/57514#createInstance) | Создать экземпляр TUIRoomEngine |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/57514#destroyInstance) | Уничтожить экземпляр TUIRoomEngine |
| [login](https://www.tencentcloud.com/document/product/647/57514#login) | Интерфейс входа, необходимо инициализировать информацию пользователя перед входом в комнату и выполнением серии операций. |
| [logout](https://www.tencentcloud.com/document/product/647/57514#logout) | Интерфейс выхода, активно выйти из комнаты, уничтожить ресурсы |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/57514#setSelfInfo) | Установить имя и аватар локального пользователя |
| [setLoginUserInfo](https://www.tencentcloud.com/document/product/647/57514#setLoginUserInfo) | Установить информацию пользователя входа |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/57514#getSelfInfo) | Получить основную информацию локального пользователя |
| [addObserver](https://www.tencentcloud.com/document/product/647/57514#addObserver) | Установить обратный вызов события |
| [removeObserver](https://www.tencentcloud.com/document/product/647/57514#removeObserver) | Удалить обратный вызов события |

### Интерфейс активной операции, связанный с комнатой

| API | Описание |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/57514#createRoom) | Создать комнату |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/57514#destroyRoom) | Закрыть комнату |
| [enterRoom](https://www.tencentcloud.com/document/product/647/57514#enterRoom) | Вход в комнату |
| [exitRoom](https://www.tencentcloud.com/document/product/647/57514#exitRoom) | Выход из комнаты |
| [connectOtherRoom](https://www.tencentcloud.com/document/product/647/57514#connectOtherRoom) | Подключиться к другой комнате |
| [disconnectOtherRoom](https://www.tencentcloud.com/document/product/647/57514#disconnectOtherRoom) | Отключиться от другой комнаты |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/57514#fetchRoomInfo) | Получить данные комнаты |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/57514#updateRoomNameByAdmin) | Обновить имя комнаты |
| [updateRoomSpeechModeByAdmin](https://www.tencentcloud.com/document/product/647/57514#updateRoomSpeechModeByAdmin) | Установить режим управления комнатой (только администратор или владелец группы могут вызвать) |

### Отображение представления локального пользователя, управление видео

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/57514#setLocalVideoView) | Установить элемент управления представлением для отображения видео локального пользователя |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/57514#openLocalCamera) | Открыть локальную камеру |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/57514#closeLocalCamera) | Закрыть локальную камеру |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/57514#updateVideoQuality) | Обновить параметры качества локального видеокодека |
| [updateVideoQualityEx](https://www.tencentcloud.com/document/product/647/57514#updateVideoQualityEx) | Установить параметры кодирования видеокодера |
| [setVideoResolutionMode](https://www.tencentcloud.com/document/product/647/57514#setVideoResolutionMode) | Установить режим разрешения видеокодера |
| [enableGravitySensor](https://www.tencentcloud.com/document/product/647/57514#enableGravitySensor) | Включить датчик гравитации |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/57514#startPushLocalVideo) | Начать передачу локального видео |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/57514#stopPushLocalVideo) | Остановить передачу локального видео |
| [startScreenSharing](https://www.tencentcloud.com/document/product/647/57514#startScreenSharing) | Начать общий доступ к экрану |
| [stopScreenSharing](https://www.tencentcloud.com/document/product/647/57514#stopScreenSharing) | Остановить общий доступ к экрану |

### Управление звуком локального пользователя

| API | Описание |
| --- | --- |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/57514#openLocalMicrophone) | Открыть локальный микрофон |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/57514#closeLocalMicrophone) | Закрыть локальный микрофон |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/57514#updateAudioQuality) | Обновить параметры качества локального аудиокодека |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/57514#muteLocalAudio) | Отключить звук локального аудио |
| [unMuteLocalAudio](https://www.tencentcloud.com/document/product/647/57514#unMuteLocalAudio) | Включить звук локального аудио |

### Отображение представления удаленного пользователя, управление видео

| API | Описание |
| --- | --- |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/57514#setRemoteVideoView) | Установить элемент управления представлением для отображения видео удаленного пользователя |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/57514#startPlayRemoteVideo) | Начать воспроизведение видео удаленного пользователя |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/57514#stopPlayRemoteVideo) | Остановить воспроизведение видео удаленного пользователя |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/57514#muteRemoteAudioStream) | Отключить звук удаленного пользователя |

### Информация о пользователях комнаты

| API | Описание |
| --- | --- |
| [getUserList](https://www.tencentcloud.com/document/product/647/57514#getUserList) | Получить список участников в комнате |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/57514#getUserInfo) | Получить информацию о участнике |

### Управление пользователями комнаты

| API | Описание |
| --- | --- |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/57514#changeUserRole) | Изменить роль пользователя (только администратор или владелец группы могут вызвать) |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/57514#kickRemoteUserOutOfRoom) | Исключить удаленного пользователя из комнаты (только администратор или владелец группы могут вызвать) |
| [addCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/57514#addCategoryTagForUsers) | Добавить теги категорий пользователям (только администратор или владелец группы могут вызвать) |
| [removeCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/57514#removeCategoryTagForUsers) | Удалить теги категорий пользователей (только администратор или владелец группы могут вызвать) |
| [getUserListByTag](https://www.tencentcloud.com/document/product/647/57514#getUserListByTag) | Получить информацию о пользователях в комнате на основе тегов |

### Управление речью в комнате

| API | Описание |
| --- | --- |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/57514#disableDeviceForAllUserByAdmin) | Управлять статусом разрешения на открытие всеми пользователями в текущей комнате устройств захвата аудио и видео потоков, таких как: запретить всем включать микрофон, запретить всем включать камеру, запретить всем включать общий доступ к экрану (в настоящее время доступно только в сценариях встреч и только администраторы или владельцы групп могут вызывать). |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/57514#openRemoteDeviceByAdmin) | Запросить у удаленного пользователя открыть медиаустройство (только администратор или владелец группы могут вызвать) |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/57514#closeRemoteDeviceByAdmin) | Закрыть медиаустройство удаленного пользователя (только администратор или владелец группы могут вызвать) |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/57514#applyToAdminToOpenLocalDevice) | Запросить открытие локального медиаустройства (доступно для обычных пользователей) |

### Управление местами микрофона в комнате

| API | Описание |
| --- | --- |
| [setMaxSeatCount](https://www.tencentcloud.com/document/product/647/57514#setMaxSeatCount) | Установить максимальное количество мест микрофона (поддерживается только при входе и создании комнаты) |
| [getSeatList](https://www.tencentcloud.com/document/product/647/57514#getSeatList) | Получить список мест микрофона |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/57514#lockSeatByAdmin) | Заблокировать место микрофона (включая блокировку позиции, блокировку состояния звука, блокировку состояния видео) |
| [takeSeat](https://www.tencentcloud.com/document/product/647/57514#takeSeat) | Подать заявку на трансляцию (не требуется в режиме свободной речи) |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/57514#leaveSeat) | Подать заявку на выход из трансляции (не требуется в режиме свободной речи) |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/57514#takeUserOnSeatByAdmin) | Хост/администратор приглашает пользователя на трансляцию |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/57514#kickUserOffSeatByAdmin) | Хост/администратор исключает пользователя с места микрофона |

### Управление сигнализацией

| API | Описание |
| --- | --- |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/57514#cancelRequest) | Отменить запрос |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/57514#responseRemoteRequest) | Ответить на запрос |

### Отправка сообщения

| API | Описание |
| --- | --- |
| [sendTextMessage](https://www.tencentcloud.com/document/product/647/57514#sendTextMessage) | Отправить текстовое сообщение |
| [sendCustomMessage](https://www.tencentcloud.com/document/product/647/57514#sendCustomMessage) | Отправить пользовательское сообщение |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/57514#disableSendingMessageByAdmin) | Отключить возможность отправки текстовых сообщений удаленным пользователем (только администратор или владелец группы могут вызвать) |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/57514#disableSendingMessageForAllUser) | Отключить возможность отправки текстовых сообщений всеми пользователями (только администратор или владелец группы могут вызвать) Расширенные функции: получить экземпляр TRTC |

### Расширенные функции

| API | Описание |
| --- | --- |
| [switchCamera](https://www.tencentcloud.com/document/product/647/57514#switchCamera) | Переключить переднюю/заднюю камеру |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/57514#setBeautyLevel) | Установить уровень красоты |
| [setWhitenessLevel](https://www.tencentcloud.com/document/product/647/57514#setWhitenessLevel) | Установить уровень белизны |

### Связанное с отладкой

| API | Описание |
| --- | --- |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/57514#callExperimentalAPI) | Вызвать экспериментальный api |

## Событие обратного вызова TUIRoomObserver

TUIRoomObserver — это класс события обратного вызова, соответствующий TUIRoomEngine. Вы можете следить за событиями обратного вызова, которые вам нужны, через этот обратный вызов.

TUIRoomObserver

## TUIRoomObserver

### Обратный вызов ошибки

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/57513#onError) | Событие обратного вызова ошибки |

### Обратный вызов события состояния входа

| API | Описание |
| --- | --- |
| [onKickedOffLine](https://www.tencentcloud.com/document/product/647/57513#onKickedOffLine) | Событие исключения пользователя в режиме "вне сети" |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/57513#onUserSigExpired) | Событие истечения срока действия учетных данных пользователя |

### Обратный вызов события комнаты

| API | Описание |
| --- | --- |
| [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/57513#onRoomNameChanged) | Событие изменения имени комнаты |
| [onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/57513#onAllUserMicrophoneDisableChanged) | Событие отключения микрофонов всех пользователей в комнате |
| [onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/57513#onAllUserCameraDisableChanged) | Событие отключения камер всех пользователей в комнате |
| [onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/57513#onSendMessageForAllUserDisableChanged) | Событие отключения отправки текстовых сообщений всеми пользователями в комнате |
| [onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/57513#onKickedOutOfRoom) | Событие закрытия комнаты |
| [onRoomDismissed](https://www.tencentcloud.com/document/product/647/57513#onRoomDismissed) | Событие исключения из комнаты |
| [onRoomSpeechModeChanged](https://www.tencentcloud.com/document/product/647/57513#onRoomSpeechModeChanged) | Изменение режима управления микрофоном в комнате |

### Обратный вызов события пользователя комнаты

| API | Описание |
| --- | --- |
| [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/57513#onRemoteUserEnterRoom) | Событие входа удаленного пользователя в комнату |
| [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/57513#onRemoteUserLeaveRoom) | Событие выхода удаленного пользователя из комнаты |
| [onUserRoleChanged](https://www.tencentcloud.com/document/product/647/57513#onUserRoleChanged) | Событие изменения роли пользователя |
| [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/57513#onUserVideoStateChanged) | Событие изменения состояния видео пользователя |
| [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/57513#onUserAudioStateChanged) | Событие изменения состояния аудио пользователя |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/57513#onUserVoiceVolumeChanged) | Событие изменения громкости пользователя |
| [onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/57513#onSendMessageForUserDisableChanged) | Событие изменения способности отправки текстовых сообщений пользователем |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/57513#onUserNetworkQualityChanged) | Событие изменения состояния сети пользователя |
| [onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/57513#onUserScreenCaptureStopped) | Событие завершения общего доступа к экрану |

### Обратный вызов события места микрофона в комнате

| API | Описание |
| --- | --- |
| [onRoomMaxSeatCountChanged](https://www.tencentcloud.com/document/product/647/57513#onRoomMaxSeatCountChanged) | Событие изменения максимального количества мест микрофона в комнате (эффективно только в комнатах типа конференции) |
| [onSeatListChanged](https://www.tencentcloud.com/document/product/647/57513#onSeatListChanged) | Событие изменения списка мест микрофона |
| [onKickedOffSeat](https://www.tencentcloud.com/document/product/647/57513#onKickedOffSeat) | Получено событие исключения пользователя с места микрофона |

### Обратный вызов события сигнализации запроса

| API | Описание |
| --- | --- |
| [onRequestReceived](https://www.tencentcloud.com/document/product/647/57513#onRequestReceived) | Событие получения сообщения запроса |
| [onRequestCancelled](https://www.tencentcloud.com/document/product/647/57513#onRequestCancelled) | Событие получения отмены запроса |

### Обратный вызов события сообщения комнаты

| API | Описание |
| --- | --- |
| [onReceiveTextMessage](https://www.tencentcloud.com/document/product/647/57513#onReceiveTextMessage) | Событие получения обычного текстового сообщения |
| [onReceiveCustomMessage](https://www.tencentcloud.com/document/product/647/57513#onReceiveCustomMessage) | Событие получения пользовательского сообщения |


---
*Источник: [https://trtc.io/document/57512](https://trtc.io/document/57512)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*
