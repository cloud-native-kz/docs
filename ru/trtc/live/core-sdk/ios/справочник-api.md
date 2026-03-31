# Справочник API

**AtomicXCore SDK** — это API нового поколения от компании **TRTC**, специально разработанный для прямого видеовещания и голосовых чат-румов. Этот набор API позволяет быстро разрабатывать пользовательские интерфейсы и поддерживает комплексные функции, включая управление комнатами, управление участниками, контроль мест вещания, базовые эффекты красоты и многое другое. Построенный на базе SDK TRTC, AtomicXCore обеспечивает сверхнизкую задержку и высокое качество аудио и видео. На этой странице приводится полный справочник по всем интерфейсам **AtomicXCore SDK API**, организованным по функциональным модулям.

## LoginStore

**Аутентификация пользователя и управление входом**

**Основные возможности:** Предоставляет аутентификацию пользователя, управляет состоянием входа, хранит профили пользователей и доставляет необходимые услуги аутентификации.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [loginUserInfo](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/loginstate/loginuserinfo) | Информация о текущем вошедшем в систему пользователе. |
| [loginStatus](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/loginstate/loginstatus) | Текущий статус входа. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [login(sdkAppID:userID:userSig:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/loginstore/login(sdkappid:userid:usersig:completion:)) | Аутентификация и вход пользователя в систему. |
| [logout(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/loginstore/logout(completion:)) | Выход текущего пользователя из системы. |
| [setSelfInfo(userProfile:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/loginstore/setselfinfo(userprofile:completion:)) | Обновление информации профиля пользователя. |

## LiveListStore

**Управление списком прямых трансляций**

- **Основные возможности**: Управление полным жизненным циклом комнаты прямой трансляции, включая создание, присоединение, выход и завершение, охватывая все основные бизнес-процессы.
- **Технические особенности**: Поддержка постраничной загрузки, синхронизация статуса в реальном времени, динамическое обновление информации о прямых трансляциях, использование реактивного управления данными (Combine) для синхронизации пользовательского интерфейса и состояния данных.
- **Сценарии использования**: Отображение списка комнат прямых трансляций, создание комнаты, управление статусом прямой трансляции, статистика данных прямой трансляции и другие основные сценарии потокового вещания.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [liveList](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststate/livelist) | Данные списка комнат прямых трансляций. |
| [liveListCursor](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststate/livelistcursor) | Курсор для постраничной загрузки комнат прямых трансляций. |
| [currentLive](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststate/currentlive) | Информация о текущей комнате прямой трансляции. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [fetchLiveList(cursor:count:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/fetchlivelist(cursor:count:completion:)) | Получить список комнат прямых трансляций. |
| [createLive(_:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/createlive(_:completion:)) | Создать новую комнату прямой трансляции. |
| [joinLive(liveID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/joinlive(liveid:completion:)) | Присоединиться к существующей комнате прямой трансляции. |
| [leaveLive(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/leavelive(completion:)) | Выйти из текущей комнаты прямой трансляции. |
| [endLive(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/endlive(completion:)) | Завершить трансляцию. |
| [updateLiveInfo(_:modifyFlag:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/updateliveinfo(_:modifyflag:completion:)) | Обновить информацию комнаты прямой трансляции. |
| [queryMetaData](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/querymetadata(keys:completion:)) | Запросить пользовательские метаданные. |
| [updateLiveMetaData](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveliststore/updatelivemetadata(_:completion:)) | Обновить пользовательские метаданные комнаты прямой трансляции. |

## LiveSeatStore

**Управление местами в комнате прямой трансляции**

- **Основные возможности:** Предоставляет контроль мест для сценариев совместного вещания нескольких пользователей, поддерживая расширенное управление статусом мест и контроль аудио/видео устройств.
- **Технические особенности:** Построено на WebRTC, поддерживает управление многопотоковым аудио/видео, блокировку мест, контроль устройств и управление правами доступа.
- **Сценарии использования:** Совместное вещание нескольких пользователей, PK хостов, интерактивные игры, онлайн-образование, прямое видеовещание конференций и другие сценарии многопользовательского взаимодействия в прямом эфире.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [seatList](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstate/seatlist) | Список мест в комнате прямой трансляции. |
| [canvas](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstate/canvas) | Информация о холсте для макета видео. |
| [speakingUsers](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstate/speakingusers) | Список пользователей, в настоящий момент говорящих. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [takeSeat(seatIndex:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/takeseat(seatindex:completion:)) | Занять место (присоединиться как со-ведущий). |
| [leaveSeat(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/leaveseat(completion:)) | Покинуть место (выйти из роли со-ведущего). |
| [muteMicrophone()](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/mutemicrophone()) | Отключить микрофон. |
| [unmuteMicrophone(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/unmutemicrophone(completion:)) | Включить микрофон. |
| [kickUserOutOfSeat(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/kickuseroutofseat(userid:completion:)) | Удалить пользователя с места. |
| [moveUserToSeat(userID:targetIndex:policy:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/moveusertoseat(userid:targetindex:policy:completion:)) | Переместить пользователя на указанное место. |
| [lockSeat(seatIndex:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/lockseat(seatindex:completion:)) | Заблокировать место. |
| [unlockSeat(seatIndex:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/unlockseat(seatindex:completion:)) | Разблокировать место. |
| [openRemoteCamera(userID:policy:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/openremotecamera(userid:policy:completion:)) | Включить камеру удаленного пользователя. |
| [closeRemoteCamera(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/closeremotecamera(userid:completion:)) | Отключить камеру удаленного пользователя. |
| [openRemoteMicrophone(userID:policy:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/openremotemicrophone(userid:policy:completion:)) | Включить микрофон удаленного пользователя. |
| [closeRemoteMicrophone(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveseatstore/closeremotemicrophone(userid:completion:)) | Отключить микрофон удаленного пользователя. |

## LiveAudienceStore

**Управление аудиторией комнаты прямой трансляции**

- **Основные возможности:** Управление списком аудитории, контроль прав доступа аудитории, назначение администраторов и поддержание порядка в комнате прямой трансляции.
- **Технические особенности:** Предоставление обновлений списка аудитории в реальном времени, иерархическое управление правами доступа, пакетные операции и расширенные функции модерации.
- **Сценарии использования:** Управление аудиторией, контроль прав доступа, модерация комнаты прямой трансляции, взаимодействие с аудиторией и другие сценарии потокового вещания.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [audienceList](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestate/audiencelist) | Список членов аудитории в комнате прямой трансляции. |
| [audienceCount](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestate/audiencecount) | Количество членов аудитории. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [fetchAudienceList(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestore/fetchaudiencelist(completion:)) | Получить список аудитории. |
| [setAdministrator(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestore/setadministrator(userid:completion:)) | Назначить права администратора. |
| [revokeAdministrator(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestore/revokeadministrator(userid:completion:)) | Отозвать права администратора. |
| [kickUserOutOfRoom(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestore/kickuseroutofroom(userid:completion:)) | Удалить пользователя из комнаты. |
| [disableSendMessage(userID:isDisable:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/liveaudiencestore/disablesendmessage(userid:isdisable:completion:)) | Запретить пользователю отправлять сообщения. |

## DeviceStore

**Управление состоянием устройства**

- **Основные возможности:** Контроль аудио/видео устройств, таких как камера и микрофон, мониторинг состояния устройства и проверка прав доступа.
- **Технические особенности:** Поддержка управления несколькими устройствами, мониторинг состояния устройства в реальном времени, динамическая проверка прав доступа и автоматическое восстановление устройства.
- **Сценарии использования:** Управление устройствами, контроль прав доступа, захват аудио/видео, обработка отказов устройств и другие базовые технические сценарии.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [microphoneStatus](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/microphonestatus) | Статус включения микрофона. |
| [microphoneLastError](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/microphonelasterror) | Последняя ошибка микрофона. |
| [captureVolume](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/capturevolume) | Громкость захвата микрофона (0-100). |
| [currentMicVolume](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/currentmicvolume) | Текущая громкость микрофона (0-100). |
| [outputVolume](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/outputvolume) | Громкость вывода аудио (0-100). |
| [cameraStatus](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/camerastatus) | Статус включения камеры. |
| [cameraLastError](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/cameralasterror) | Последняя ошибка камеры. |
| [isFrontCamera](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/isfrontcamera) | Указывает, используется ли передняя камера. |
| [localMirrorType](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/localmirrortype) | Тип зеркального отображения локального видео. |
| [localVideoQuality](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/localvideoquality) | Параметры качества локального видео. |
| [currentAudioRoute](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/currentaudioroute) | Текущий маршрут вывода аудио (динамик или наушники). |
| [screenStatus](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/screenstatus) | Статус общего доступа экрана. |
| [networkInfo](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestate/networkinfo) | Информация о текущей сети. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [openLocalMicrophone(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore/openlocalmicrophone(completion:)) | Включить локальный микрофон. |
| [closeLocalMicrophone()](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore/closelocalmicrophone()) | Отключить локальный микрофон. |
| [setCaptureVolume(volume:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore/setcapturevolume(volume:)) | Установить громкость захвата микрофона. |
| [setOutputVolume(_:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore/setoutputvolume(_:)) | Установить громкость вывода аудио. |
| [openLocalCamera(isFront:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/devicestore/openlocalcamera(isfront:completion:)) | Включить локальную камеру. |

## CoGuestStore

**Управление гостями со-ведущих**

- **Основные возможности:** Управление взаимодействием со-ведущих между аудиторией и ведущим, включая рабочие процессы подачи заявки, приглашения, принятия и отклонения.
- **Технические особенности:** Использование технологии аудио/видео в реальном времени, поддержка синхронизации статуса со-ведущего в реальном времени, адаптивное качество аудио/видео и мониторинг сети.
- **Сценарии использования:** Совместное вещание аудитории, интерактивные вопросы и ответы, онлайн-караоке, трансляция игр и другие сценарии участия аудитории.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [connected](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststate/connected) | Список подключенных гостей со-ведущих. |
| [invitees](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststate/invitees) | Список пользователей, приглашенных на место со-ведущего. |
| [applicants](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststate/applicants) | Список пользователей, подающих заявку на место со-ведущего. |
| [candidates](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststate/candidates) | Список кандидатов, доступных для приглашения на место со-ведущего. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [applyForSeat(seatIndex:timeout:extraInfo:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/applyforseat(seatindex:timeout:extrainfo:completion:)) | Подать заявку на место со-ведущего. |
| [cancelApplication(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/cancelapplication(completion:)) | Отменить заявку на место со-ведущего. |
| [acceptApplication(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/acceptapplication(userid:completion:)) | Принять заявку на место со-ведущего. |
| [rejectApplication(userID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/rejectapplication(userid:completion:)) | Отклонить заявку на место со-ведущего. |
| [inviteToSeat(userID:seatIndex:timeout:extraInfo:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/invitetoseat(userid:seatindex:timeout:extrainfo:completion:)) | Пригласить пользователя на место со-ведущего. |
| [cancelInvitation(inviteeID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/cancelinvitation(inviteeid:completion:)) | Отменить приглашение на место со-ведущего. |
| [acceptInvitation(inviterID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/acceptinvitation(inviterid:completion:)) | Принять приглашение на место со-ведущего. |
| [rejectInvitation(inviterID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/rejectinvitation(inviterid:completion:)) | Отклонить приглашение на место со-ведущего. |
| [disConnect(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cogueststore/disconnect(completion:)) | Отключиться от со-ведущего. |

## CoHostStore

**Управление подключением ведущего**

- **Основные возможности:** Включить подключения ведущий-ведущий, включая приглашения, запросы подключения, управление статусом и взаимодействие ведущих.
- **Технические особенности:** Поддержка синхронизации аудио/видео нескольких ведущих, отображение картинка в картинке и оптимизация качества аудио/видео для беспрепятственного сотрудничества ведущих.
- **Сценарии использования:** PK ведущих, совместное потоковое вещание, кроссплатформенное со-ведущее вещание, взаимодействие ведущих и расширенные сценарии прямого видеовещания.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [connected](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststate/connected) | Список подключенных ведущих. |
| [invitees](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststate/invitees) | Список ведущих, приглашенных на подключение. |
| [applicant](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststate/applicant) | Ведущий, в настоящий момент подающий заявку на подключение. |
| [coHostStatus](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststate/cohoststatus) | Текущий статус подключения ведущего. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [requestHostConnection(targetHost:layoutTemplate:timeout:extraInfo:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore/requesthostconnection(targethost:layouttemplate:timeout:extrainfo:completion:)) | Запросить подключение ведущий-ведущий. |
| [cancelHostConnection(toHostLiveID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore/cancelhostconnection(tohostliveid:completion:)) | Отменить запрос подключения ведущего. |
| [acceptHostConnection(fromHostLiveID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore/accepthostconnection(fromhostliveid:completion:)) | Принять запрос подключения ведущего. |
| [rejectHostConnection(fromHostLiveID:completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore/rejecthostconnection(fromhostliveid:completion:)) | Отклонить запрос подключения ведущего. |
| [exitHostConnection(completion:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/cohoststore/exithostconnection(completion:)) | Выйти из подключения ведущего. |

## AudioEffectStore

**Обработка звуковых эффектов**

- **Основные возможности:** Предоставляет продвинутые звуковые эффекты, включая изменение голоса, реверберацию и мониторинг в наушниках, с регулировкой звука в реальном времени.
- **Технические особенности:** На базе алгоритмов звука от Tencent Ethereal Lab, поддерживает звуковые эффекты в реальном времени, передачу с низкой задержкой и оптимизацию качества звука.
- **Сценарии использования:** Трансляция с изменением голоса, караоке, развлекательные аудиоэффекты, профессиональные звуковые эффекты и другие сценарии обработки звука.

**Реактивные данные**

| **Список данных** | **Описание** |
| --- | --- |
| [isEarMonitorOpened](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstate/isearmonitoropened) | Статус мониторинга в наушниках (вкл/выкл). |
| [earMonitorVolume](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstate/earmonitorvolume) | Уровень громкости мониторинга в наушниках. |
| [audioChangerType](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstate/audiochangertype) | Текущий эффект изменения голоса. |
| [audioReverbType](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstate/audioreverbtype) | Текущий эффект реверберации. |

**Функции API**

| **Список функций** | **Описание** |
| --- | --- |
| [setAudioChangerType(type:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstore/setaudiochangertype(type:)) | Установить эффект изменения голоса. |
| [setAudioReverbType(type:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstore/setaudioreverbtype(type:)) | Установить эффект реверберации. |
| [setVoiceEarMonitorEnable(enable:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstore/setvoiceearmonitorenable(enable:)) | Включить или отключить мониторинг в наушниках. |
| [setVoiceEarMonitorVolume(volume:)](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/audioeffectstore/setvoiceearmonitorvolume(volume:)) | Установить громкость мониторинга в науш

---
*Источник (EN): [api-reference.md](справочник-api.md)*
