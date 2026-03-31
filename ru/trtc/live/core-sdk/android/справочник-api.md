# Справочник API

AtomicXCore SDK — это SDK следующего поколения TRTC на основе сценариев, предназначенный для приложений прямых трансляций и комнат голосовых чатов. Он позволяет быстро создавать пользовательские интерфейсы с минимальными усилиями.

SDK предлагает полный набор функций, включая управление комнатами, совместное использование экрана, управление участниками, управление микрофонными местами и встроенные фильтры красоты. Построенный на основе TRTC, он обеспечивает сверхнизкую задержку и высокое качество звука и видео.

На этой странице приводится полный справочник всех API **AtomicXCore SDK** (Android), организованный по функциональным модулям.

## LoginStore

Модуль аутентификации пользователей и управления входом в систему

**Основные функции:** Отвечает за аутентификацию пользователей, управление статусом входа, ведение информации о пользователе и другие базовые услуги аутентификации.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [loginUserInfo](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.login/-login-state/login-user-info.html) | Информация о текущем авторизованном пользователе. |
| [loginStatus](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.login/-login-state/login-status.html) | Текущий статус входа. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [login](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.login/-login-store/login.html) | Метод входа в систему. |
| [logout](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.login/-login-store/logout.html) | Метод выхода из системы. |
| [setSelfInfo](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.login/-login-store/set-self-info.html) | Установить информацию о пользователе. |
| [addLoginListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.login/-login-store/add-login-listener.html) | Добавить прослушиватель событий обратного вызова входа. |
| [removeLoginListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.login/-login-store/remove-login-listener.html) | Удалить прослушиватель событий обратного вызова входа. |

## LiveListStore

Модуль управления списком трансляций

- Основные функции: Управляет полным жизненным циклом комнат прямых трансляций, включая создание, присоединение, выход и основные бизнес-процессы.
- Технические возможности:
  - Поддерживает загрузку по страницам, синхронизацию статуса в реальном времени и динамические обновления информации о трансляции.
  - Реализует реактивное управление данными с использованием Kotlin Flow для обеспечения беспроблемной синхронизации между состояниями пользовательского интерфейса и данных.
- Преимущества: Предоставляет необходимые возможности управления комнатами прямых трансляций для платформ прямого вещания, обрабатывает высокопроизводительные сценарии в большом масштабе и служит основной инфраструктурой для услуг прямого вещания.
- Варианты использования: Отображение списка прямых трансляций, создание комнаты, управление статусом трансляции и аналитика трансляций.

**Реактивные данные**

| Список данных | Описание |
| --- | --- |
| [liveList](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-state/live-list.html) | Данные списка прямых трансляций. |
| [liveListCursor](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-state/live-list-cursor.html) | Курсор списка прямых трансляций, используется для загрузки по страницам. |
| [currentLive](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-state/current-live.html) | Информация о текущей прямой трансляции. |

**Функции API**

| Список функций | Описание |
| --- | --- |
| [fetchLiveList](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/fetch-live-list.html) | Получить список прямых трансляций. |
| [fetchLiveInfo](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/fetch-live-info.html) | Получить информацию о комнате прямой трансляции на основе идентификатора комнаты прямой трансляции. |
| [createLive](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/create-live.html) | Создать комнату прямой трансляции. |
| [joinLive](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/join-live.html) | Присоединиться к комнате прямой трансляции. |
| [leaveLive](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/leave-live.html) | Покинуть комнату прямой трансляции. |
| [endLive](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/end-live.html) | Завершить прямую трансляцию. |
| [updateLiveInfo](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/update-live-info.html) | Обновить информацию о прямой трансляции. |
| [addLiveListListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/add-live-list-listener.html) | Добавить прослушиватель событий списка прямых трансляций. |
| [removeLiveListListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/remove-live-list-listener.html) | Удалить прослушиватель событий списка прямых трансляций. |

## LiveSeatStore

Модуль управления микрофонными местами

- Основные функции: Включает управление местами в многопользовательских сценариях голосовых чатов, поддерживая сложное управление состоянием мест и управление устройствами аудио/видео.
- Технические возможности:
  - Построено на технологии WebRTC с возможностью управления несколькими потоками
  - Поддерживает блокировку и разблокировку мест
  - Предоставляет управление устройствами аудио/видео
  - Реализует управление разрешениями на основе ролей
- Преимущества: Предоставляет необходимую технологическую инфраструктуру для интерактивной прямой трансляции, включая различные сценарии взаимодействия, такие как совместное вещание, боевые действия якорей (PK) и многопользовательские взаимодействия.
- Варианты использования: Многопользовательские сценарии взаимодействия аудио/видео, включая совместное вещание, конкурсы якорей, интерактивные игры, онлайн-образование и прямые конференции.

**Реактивные данные**

| Список данных | Описание |
| --- | --- |
| [seatList](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-state/seat-list.html) | Список мест. |
| [canvas](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-state/canvas.html) | Информация о холсте. |
| [speakingUsers](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-state/speaking-users.html) | Список пользователей, которые в данный момент говорят. |
| [avStatistics](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-state/av-statistics.html) | Статистика аудио/видео. |

**Функции API**

| Список функций | Описание |
| --- | --- |
| [takeSeat](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/take-seat.html) | Пользователь присоединяется на сцену. |
| [leaveSeat](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/leave-seat.html) | Отключение микрофона пользователя. |
| [muteMicrophone](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/mute-microphone.html) | Отключить микрофон. |
| [unmuteMicrophone](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/unmute-microphone.html) | Включить микрофон. |
| [kickUserOutOfSeat](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/kick-user-out-of-seat.html) | Выгнать пользователя. |
| [moveUserToSeat](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/move-user-to-seat.html) | Переместить пользователя на сцену. |
| [lockSeat](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/lock-seat.html) | Заблокировать место. |
| [unlockSeat](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/unlock-seat.html) | Разблокировать микрофон. |
| [openRemoteCamera](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/open-remote-camera.html) | Включить камеру удаленного пользователя. |
| [closeRemoteCamera](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/close-remote-camera.html) | Отключить камеру удаленного пользователя. |
| [openRemoteMicrophone](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/open-remote-microphone.html) | Включить микрофон удаленного пользователя. |
| [closeRemoteMicrophone](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/close-remote-microphone.html) | Отключить микрофон удаленного пользователя. |
| [addLiveSeatEventListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/add-live-seat-event-listener.html) | Добавить прослушиватель событий микрофонного места. |
| [removeLiveSeatEventListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-seat-store/remove-live-seat-event-listener.html) | Удалить прослушиватель событий микрофонного места. |

## LiveAudienceStore

Модуль управления аудиторией прямой трансляции

- Основные функции: Управляет списками аудитории в комнатах прямых трансляций с контролем разрешений, конфигурацией администраторов и инструментами модерации для поддержания порядка в комнате.
- Технические возможности:
  - Обновления списка аудитории в реальном времени
  - Иерархическое управление разрешениями
  - Поддержка массовых операций
  - Расширенные инструменты модерации
- Преимущества: Предоставляет комплексные решения для управления аудиторией на платформах прямого вещания, обеспечивая беспроблемную модерацию в большом масштабе.
- Варианты использования: Управление списком аудитории, управление разрешениями, модерация комнаты и управление взаимодействием с аудиторией.

**Реактивные данные**

| Список данных | Описание |
| --- | --- |
| [audienceList](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-state/audience-list.html) | Список аудитории комнаты прямой трансляции. |
| [audienceCount](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-state/audience-count.html) | Размер аудитории комнаты прямой трансляции. |
| [messageBannedUserList](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-state/message-banned-user-list.html) | Список пользователей с отключенным звуком. |

**Функции API**

| Список функций | Описание |
| --- | --- |
| [fetchAudienceList](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-store/fetch-audience-list.html) | Получить список аудитории. |
| [setAdministrator](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-store/set-administrator.html) | Установить администратора. |
| [revokeAdministrator](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-store/revoke-administrator.html) | Отозвать администратора. |
| [kickUserOutOfRoom](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-store/kick-user-out-of-room.html) | Выгнать пользователя из комнаты. |
| [disableSendMessage](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-store/disable-send-message.html) | Отключить отправку сообщений. |
| [addAudienceListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-store/add-live-audience-listener.html) | Добавить прослушиватель аудитории. |
| [removeAudienceListener](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-audience-store/remove-live-audience-listener.html) | Удалить прослушиватель аудитории. |

## DeviceStore

Модуль управления состоянием устройства

- Основные функции: Управление управлением камерами, микрофонами и другими устройствами аудио/видео, предоставление мониторинга состояния устройства, проверки разрешений и других основных услуг устройства.
- Технические возможности: Поддерживает расширенные функции, такие как управление несколькими устройствами, мониторинг состояния в реальном времени, динамическая проверка разрешений и автоматическое восстановление после сбоев.
- Преимущества: Обеспечивают стабильность устройства для системы прямой трансляции, гарантируют надежность захвата аудио и видео и удобство работы пользователя.
- Варианты использования: Базовые технические сценарии, такие как управление устройством, управление разрешениями, захват аудио и видео и обработка отказов устройства.

**Реактивные данные**

| Список данных | Описание |
| --- | --- |
| [microphoneStatus](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/microphone-status.html) | Состояние включения микрофона. |
| [microphoneLastError](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/microphone-last-error.html) | Статус последней ошибки микрофона. |
| [captureVolume](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/capture-volume.html) | Громкость захвата звука (0–100). |
| [currentMicVolume](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/current-mic-volume.html) | Текущая громкость микрофона (0–100). |
| [outputVolume](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/output-volume.html) | Громкость вывода звука (0–100). |
| [cameraStatus](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/camera-status.html) | Состояние включения камеры. |
| [cameraLastError](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/camera-last-error.html) | Статус последней ошибки камеры. |
| [isFrontCamera](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/is-front-camera.html) | Является ли камера фронтальной. |
| [localMirrorType](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/local-mirror-type.html) | Тип локального изображения. |
| [localVideoQuality](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/local-video-quality.html) | Параметры локального качества видео. |
| [currentAudioRoute](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/current-audio-route.html) | Текущий маршрут вывода звука (динамик/наушники). |
| [screenStatus](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/screen-status.html) | Состояние совместного использования экрана. |
| [networkInfo](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-state/network-info.html) | Состояние информации о сети. |

**Функции API**

| Список функций | Описание |
| --- | --- |
| [openLocalMicrophone](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/open-local-microphone.html) | Включить локальный микрофон. |
| [closeLocalMicrophone](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/close-local-microphone.html) | Отключить локальный микрофон. |
| [setCaptureVolume](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/set-capture-volume.html) | Установить громкость захвата. |
| [setOutputVolume](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/set-output-volume.html) | Установить громкость вывода. |
| [setAudioRoute](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/set-audio-route.html) | Установить маршрут вывода звука. |
| [startCameraTest](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/start-camera-test.html) | Предпросмотр фронтальной камеры, видео предпросмотр будет отображено на параметре cameraView. |
| [stopCameraTest](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/stop-camera-test.html) | Остановить предпросмотр камеры. |
| [openLocalCamera](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/open-local-camera.html) | Включить локальную камеру. |
| [closeLocalCamera](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/close-local-camera.html) | Выключить локальную камеру. |
| [switchCamera](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/switch-camera.html) | Переключить каме

---
*Источник (EN): [api-reference.md](справочник-api.md)*
