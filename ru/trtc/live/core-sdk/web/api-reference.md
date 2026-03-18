# Справочник API

**AtomicXCore SDK** — это API нового поколения от **TRTC**, специально разработанный для прямых трансляций, мгновенной обмена сообщениями, аудио/видео вызовов и голосовых чат-комнат. Этот набор API позволяет быстро разрабатывать пользовательские интерфейсы и поддерживает комплексные функции, включая управление комнатами, общий доступ к экрану, управление участниками, контроль мест, базовые эффекты красоты и многое другое. Построенный на основе TRTC SDK, AtomicXCore обеспечивает ультранизкую задержку и высокое качество аудио и видео. Эта страница содержит полный справочник всех интерфейсов **API AtomicXCore SDK**, организованный по функциональным модулям.

## LoginState

**Аутентификация пользователя и управление входом**

- **Основные функции:** Предоставляет основные функции аутентификации личности, включая вход пользователя, выход и управление личным профилем. Это формирует основу идентичности пользователя во всем приложении.
- **Технические особенности:** Поддержка нескольких методов входа, кеширование информации пользователя, сохранение состояния входа и надежная безопасность идентичности пользователя.
- **Сценарии использования:** Вход пользователя, проверка идентификации, управление профилем, контроль разрешений и другие основные сценарии аутентификации.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [loginUserInfo](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#loginUserInfo) | Информация текущего вошедшего пользователя. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [login](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#login) | Аутентификация и вход пользователя. |
| [setSelfInfo](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setSelfInfo) | Обновить информацию профиля пользователя. |
| [logout](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#logout) | Выход пользователя. |

## DeviceState

**Управление состоянием устройства**

- **Основные функции:** Управление устройствами аудио/видео, такими как камеры и микрофоны, мониторинг состояния устройства, проверка разрешений и предоставление основных услуг устройства.
- **Технические особенности:** Поддержка управления несколькими устройствами, мониторинг устройств в реальном времени, проверка разрешений в динамическом режиме и автоматическое восстановление при сбоях.
- **Сценарии использования:** Управление устройствами, контроль разрешений, захват аудио/видео, обработка сбоев устройства и другие основные сценарии.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [microphoneStatus](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#microphoneStatus) | Состояние микрофона. |
| [microphoneList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#microphoneList) | Список доступных устройств микрофона. |
| [currentMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#currentMicrophone) | Текущее выбранное устройство микрофона. |
| [microphoneLastError](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#microphoneLastError) | Информация о последней ошибке микрофона. |
| [captureVolume](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#captureVolume) | Уровень громкости захвата микрофона. |
| [currentMicVolume](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#currentMicVolume) | Текущая громкость микрофона. |
| [isMicrophoneTesting](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#isMicrophoneTesting) | Статус тестирования микрофона. |
| [testingMicVolume](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#testingMicVolume) | Громкость микрофона во время тестирования. |
| [cameraStatus](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#cameraStatus) | Состояние камеры. |
| [cameraList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#cameraList) | Список доступных устройств камеры. |
| [currentCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#currentCamera) | Текущее выбранное устройство камеры. |
| [cameraLastError](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#cameraLastError) | Информация о последней ошибке камеры. |
| [isCameraTesting](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#isCameraTesting) | Статус тестирования камеры. |
| [isCameraTestLoading](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#isCameraTestLoading) | Статус загрузки теста камеры. |
| [isFrontCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#isFrontCamera) | Указывает, используется ли фронтальная камера. |
| [localMirrorType](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#localMirrorType) | Тип локального зеркала видео. |
| [localVideoQuality](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#localVideoQuality) | Параметры качества локального видео. |
| [speakerList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#speakerList) | Список доступных устройств динамика. |
| [currentSpeaker](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#currentSpeaker) | Текущее выбранное устройство динамика. |
| [outputVolume](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#outputVolume) | Уровень громкости выхода динамика. |
| [currentAudioRoute](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#currentAudioRoute) | Текущий маршрут выхода аудио. |
| [isSpeakerTesting](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#isSpeakerTesting) | Статус тестирования динамика. |
| [screenStatus](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#screenStatus) | Статус общего доступа к экрану. |
| [networkInfo](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#networkInfo) | Информация о сетевом подключении. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [openLocalMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#openLocalMicrophone) | Включить локальный микрофон. |
| [closeLocalMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#closeLocalMicrophone) | Отключить локальный микрофон. |
| [muteLocalAudio](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#muteLocalAudio) | Отключить звук локального аудио. |
| [unmuteLocalAudio](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#unmuteLocalAudio) | Включить звук локального аудио. |
| [getMicrophoneList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#getMicrophoneList) | Получить список устройств микрофона. |
| [setCurrentMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setCurrentMicrophone) | Выбрать активное устройство микрофона. |
| [startMicrophoneTest](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#startMicrophoneTest) | Начать тестирование микрофона. |
| [setCaptureVolume](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setCaptureVolume) | Отрегулировать громкость захвата микрофона. |
| [setOutputVolume](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setOutputVolume) | Отрегулировать громкость выхода динамика. |
| [stopMicrophoneTest](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#stopMicrophoneTest) | Завершить тестирование микрофона. |
| [getSpeakerList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#getSpeakerList) | Получить список устройств динамика. |
| [setCurrentSpeaker](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setCurrentSpeaker) | Выбрать активное устройство динамика. |
| [setAudioRoute](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setAudioRoute) | Настроить маршрут выхода аудио. |
| [startSpeakerTest](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#startSpeakerTest) | Начать тестирование динамика. |
| [stopSpeakerTest](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#stopSpeakerTest) | Завершить тестирование динамика. |
| [openLocalCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#openLocalCamera) | Включить локальную камеру. |
| [closeLocalCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#closeLocalCamera) | Отключить локальную камеру. |
| [getCameraList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#getCameraList) | Получить список устройств камеры. |
| [setCurrentCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setCurrentCamera) | Выбрать активное устройство камеры. |
| [switchCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#switchCamera) | Переключаться между фронтальной и тыльной камерой. |
| [switchMirror](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#switchMirror) | Переключить режим зеркала видео. |
| [updateVideoQuality](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#updateVideoQuality) | Обновить параметры качества видео. |
| [startCameraDeviceTest](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#startCameraDeviceTest) | Начать тестирование устройства камеры. |
| [startScreenShare](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#startScreenShare) | Начать общий доступ к экрану. |
| [stopScreenShare](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#stopScreenShare) | Остановить общий доступ к экрану. |
| [stopCameraDeviceTest](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#stopCameraDeviceTest) | Завершить тестирование устройства камеры. |
| [screenCaptureStopped](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#screenCaptureStopped) | Обратный вызов при остановке общего доступа к экрану. |

## LiveListState

**Управление списком трансляций**

- **Основные функции:** Управление полным жизненным циклом комнат трансляций, включая создание, присоединение, выход, завершение и поддержка постраничной выборки и обновления списка комнат трансляций в реальном времени.
- **Технические особенности:** Постраничная загрузка, синхронизация состояния в реальном времени, динамические обновления информации о трансляции и реактивная привязка данных для синхронизации пользовательского интерфейса и состояния данных. Новые реактивные данные: liveList и liveListCursor, плюс API fetchLiveList.
- **Сценарии использования:** Отображение списков комнат трансляций, создание комнат трансляций, управление состоянием трансляции, аналитика трансляций и связанные бизнес-сценарии.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [currentLive](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#currentLive) | Информация о текущей комнате трансляции. |
| [liveList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#liveList) | Данные списка комнат трансляций, включая все комнаты трансляций. |
| [liveListCursor](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#liveListCursor) | Курсор постраничной выборки для получения следующей страницы данных комнаты трансляции. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [createLive](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#createLive) | Создать новую комнату трансляции. |
| [joinLive](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#joinLive) | Присоединиться к существующей комнате трансляции. |
| [leaveLive](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#leaveLive) | Выйти из текущей комнаты трансляции. |
| [endLive](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#endLive) | Завершить трансляцию. |
| [updateLiveInfo](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#updateLiveInfo) | Обновить информацию комнаты трансляции. |
| [queryMetaData](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#queryMetaData) | Запросить пользовательские метаданные. |
| [updateLiveMetaData](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#updateLiveMetaData) | Обновить пользовательские метаданные для комнаты трансляции. |
| [fetchLiveList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#fetchLiveList) | Получить список комнат трансляций. |

## LiveSeatState

**Управление местами в комнате трансляции**

- **Основные функции:** Предоставить управление местами для многопользовательского совещания, включая управление состоянием мест и управление устройствами аудио/видео — занятие места, выход с места, блокировка места и многое другое.
- **Технические особенности:** Построено на WebRTC, поддержка управления многопотоковым аудио/видео, блокировка мест, управление устройствами, управление разрешениями и передовые функции. Новые реактивные данные: seatList, canvas, speakingUsers, networkQualities и полные API операций мест.
- **Сценарии использования:** Многопользовательское совещание, боевые действия между хостами, интерактивные игры, онлайн-образование, трансляция конференций и другие многопользовательские сценарии взаимодействия.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [seatList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#seatList) | Список мест, включая статус и информацию о пользователе для всех мест. |
| [canvas](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#canvas) | Конфигурация холста для отображения видео и макета. |
| [speakingUsers](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#speakingUsers) | Список пользователей, которые в настоящее время говорят. |
| [networkQualities](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#networkQualities) | Информация о качестве сети для каждого пользователя. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [takeSeat](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#takeSeat) | Занять место (начать прямую трансляцию с микрофона). |
| [leaveSeat](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#leaveSeat) | Выйти с места (отключить микрофон). |
| [lockSeat](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#lockSeat) | Заблокировать место. |
| [unLockSeat](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#unLockSeat) | Разблокировать место. |
| [kickUserOutOfSeat](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#kickUserOutOfSeat) | Удалить пользователя с места. |
| [moveUserToSeat](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#moveUserToSeat) | Переместить пользователя на указанное место. |
| [openRemoteCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#openRemoteCamera) | Включить камеру удаленного пользователя. |
| [closeRemoteCamera](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#closeRemoteCamera) | Отключить камеру удаленного пользователя. |
| [openRemoteMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#openRemoteMicrophone) | Включить микрофон удаленного пользователя. |
| [closeRemoteMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#closeRemoteMicrophone) | Отключить микрофон удаленного пользователя. |
| [muteMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#muteMicrophone) | Отключить звук микрофона. |
| [unmuteMicrophone](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#unmuteMicrophone) | Включить звук микрофона. |
| [startPlayStream](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#startPlayStream) | Начать воспроизведение потока. |
| [stopPlayStream](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#stopPlayStream) | Остановить воспроизведение потока. |

## LiveAudienceState

**Управление аудиторией комнаты трансляции**

- **Основные функции:** Управление списком аудитории, контроль разрешений аудитории, назначение администраторов и поддержка модерации и статистики аудитории в реальном времени.
- **Технические особенности:** Обновления списка аудитории в реальном времени, иерархическое управление разрешениями, массовые операции, обеспечение порядка в комнате трансляции и оптимального взаимодействия пользователей. Новые реактивные данные: audienceList и audienceCount.
- **Сценарии использования:** Управление аудиторией, контроль разрешений, модерация комнаты трансляции, взаимодействие с аудиторией и связанные сценарии.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [audienceList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#audienceList) | Список аудитории, включая информацию о всех зрителях. |
| [audienceCount](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#audienceCount) | Общее количество аудитории. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [fetchAudienceList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#fetchAudienceList) | Получить список аудитории. |
| [setAdministrator](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#setAdministrator) | Назначить привилегии администратора. |
| [revokeAdministrator](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#revokeAdministrator) | Отозвать привилегии администратора. |
| [kickUserOutOfRoom](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#kickUserOutOfRoom) | Удалить пользователя из комнаты. |
| [disableSendMessage](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#disableSendMessage) | Отключить звук пользователя. |

## LiveMonitorState

**Управление мониторингом комнаты трансляции**

- **Основные функции:** Предоставить мониторинг комнат трансляций в реальном времени, включая отслеживание статуса трансляции, статистику данных, обнаружение аномалий и мониторинг нескольких комнат.
- **Технические особенности:** Сбор данных в реальном времени, многомерные метрики, интеллектуальное оповещение, обеспечение стабильности и надежности трансляции. Новые реактивные данные: monitorLiveInfoList и оптимизированные API мониторинга.
- **Сценарии использования:** Мониторинг качества трансляции, анализ производительности, оповещения об аномалиях, статистика данных и оперативное управление.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [monitorLiveInfoList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#monitorLiveInfoList) | Список сведений мониторируемых комнат трансляций. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [init](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#init) | Инициализировать мониторинг комнаты трансляции. |
| [getLiveList](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#getLiveList) | Получить список комнат трансляций. |
| [closeRoom](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#closeRoom) | Закрыть комнату трансляции. |
| [sendMessage](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#sendMessage) | Отправить сообщение. |
| [startPlay](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#startPlay) | Начать воспроизведение. |
| [stopPlay](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#stopPlay) | Остановить воспроизведение. |
| [muteLiveAudio](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#muteLiveAudio) | Отключить звук прямой трансляции. |

## CoGuestState

**Управление гостями-соведущими**

- **Основные функции:** Управление взаимодействиями между соведущими и аудиторией с хостом, включая применение, приглашение, принятие, отклонение и управление статусом соведущего.
- **Технические особенности:** Технология аудио/видео в реальном времени, синхронизация состояния, адаптивное качество, мониторинг сети. Новые реактивные данные: connected, invitees, applicants, candidates и API applyForSeat.
- **Сценарии использования:** Соведущая аудитория, интерактивные вопросы и ответы, онлайн-караоке, трансляция игр и другие сценарии участия аудитории.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [candidates](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#candidates) | Список потенциальных пользователей для приглашения в соведущие. |
| [connected](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#connected) | Список пользователей, которые в настоящее время являются соведущими. |
| [invitees](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#invitees) | Список пользователей, приглашенных в соведущие. |
| [applicants](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#applicants) | Список пользователей, подавших заявку на участие в соведущих. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [cancelApplication](https://web.sdk.qcloud.com/trtc/live/web/doc/zh/index.html#cancelApplication) | Отменить заявку на совед

---
*Источник (EN): [api-reference.md](./api-reference.md)*
