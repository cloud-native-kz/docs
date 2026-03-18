# TUIRoomEngine

## Введение в TUIRoomEngine

SDK TUIRoomEngine предоставляет управление комнатой, многопользовательское взаимодействие через Tencent Real-Time Communication, совместное использование экрана, управление участниками, мгновенные сообщения и другие возможности.

**Метод установки:**

```
// Используйте npmnpm i @tencentcloud/tuiroom-engine-js --save// Используйте pnpmpnpm i @tencentcloud/tuiroom-engine-js --save// Используйте yarnyarn add @tencentcloud/tuiroom-engine-js
```

## API TUIRoomEngine

### **Статические методы TUIRoomEngine**

| API | Описание |
| --- | --- |
| [once](https://www.tencentcloud.com/document/product/647/54878#once) | **Прослушивание события готовности TUIRoomEngine.****Примечание: все методы, кроме TUIRoomEngine.login, должны выполняться после прослушивания события готовности TUIRoomEngine и успешного выполнения метода TUIRoomEngine.login.** |
| [login](https://www.tencentcloud.com/document/product/647/54878#login) | Вход в TUIRoomEngine |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54878#setSelfInfo) | Установка основной информации текущего пользователя (имя пользователя, аватар пользователя) |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54878#getSelfInfo) | Получение основной информации текущего пользователя (имя пользователя, аватар пользователя) |
| [logout](https://www.tencentcloud.com/document/product/647/54878#logout) | Выход из TUIRoomEngine |

### **API управления комнатой roomEngine**

| API | Описание |
| --- | --- |
| [createRoom](#createRoom) | Создание комнаты |
| [enterRoom](#enterRoom) | Вход в комнату |
| [destroyRoom](#destroyRoom) | Удаление комнаты |
| [exitRoom](#exitRoom) | Выход из комнаты |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/54878#fetchRoomInfo) | Получение данных комнаты |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/54878#updateRoomNameByAdmin) | Обновление имени (только для владельца группы или администратора) |
| [updateRoomSpeechModeByAdmin](https://www.tencentcloud.com/document/product/647/54878#updateRoomSpeechModeByAdmin) | Обновление режима выступления (только для владельца группы или администратора) |
| [getUserList](#getUserList) | Получение списка пользователей |
| [getUserInfo](#getUserInfo) | Получение информации о пользователе |

### **API видеоконференции roomEngine**

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/54878#setLocalVideoView) | Установка позиции отрисовки локального потока |
| [openLocalCamera](#openLocalCamera) | Захват видеопотока локальной камеры |
| [closeLocalCamera](#closeLocalCamera) | Закрытие локальной камеры |
| [openLocalMicrophone](#openLocalMicrophone) | Включение локального микрофона |
| [closeLocalMicrophone](#closeLocalMicrophone) | Выключение локального микрофона |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/54878#updateVideoQuality) | Установка параметров локального видео |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/54878#updateAudioQuality) | Установка параметров локального аудио |
| [startScreenSharing](https://www.tencentcloud.com/document/product/647/54878#startScreenSharing) | Начало совместного использования экрана |
| [stopScreenSharing](https://www.tencentcloud.com/document/product/647/54878#stopScreenSharing) | Остановка совместного использования экрана |
| [startPushLocalVideo](#startPushLocalVideo) | Начало отправки локального видеопотока удаленному пользователю |
| [stopPushLocalVideo](#stopPushLocalVideo) | Остановка отправки локального видеопотока удаленному пользователю |
| [startPushLocalAudio](#startPushLocalAudio) | Начало отправки локального аудиопотока удаленному пользователю |
| [stopPushLocalAudio](#stopPushLocalAudio) | Остановка отправки локального аудиопотока удаленному пользователю |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/54878#setRemoteVideoView) | Установка области отрисовки удаленного потока |
| [startPlayRemoteVideo](#startPlayRemoteVideo) | Начало воспроизведения видеопотока удаленного пользователя |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54878#stopPlayRemoteVideo) | Остановка воспроизведения видеопотока удаленного пользователя |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/54878#muteRemoteAudioStream) | Остановка аудиопотока удаленного пользователя |

### **API управления участниками roomEngine**

| API | Описание |
| --- | --- |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54878#openRemoteDeviceByAdmin) | Запрос удаленному пользователю на открытие устройства |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/54878#applyToAdminToOpenLocalDevice) | Участник просит хоста открыть устройство |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54878#closeRemoteDeviceByAdmin) | Закрытие устройства удаленного пользователя |
| [cancelRequest](#cancelRequest) | Отмена отправленного запроса |
| [responseRemoteRequest](#responseRemoteRequest) | Ответ на запрос удаленного пользователя |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/54878#changeUserRole) | Изменение роли пользователя |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/54878#kickRemoteUserOutOfRoom) | Исключение пользователя из комнаты |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/54878#disableDeviceForAllUserByAdmin) | Отключение/включение устройства для всех пользователей |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/54878#disableSendingMessageForAllUser) | Запрещение/разрешение всем пользователям отправлять сообщения |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/54878#disableSendingMessageByAdmin) | Запрещение/разрешение конкретному пользователю отправлять сообщения |

### **API управления позициями микрофона roomEngine**

| API | Описание |
| --- | --- |
| [setMaxSeatCount](https://www.tencentcloud.com/document/product/647/54878#setMaxSeatCount) | Установка максимального количества мест в комнате |
| [getSeatList](#getSeatList) | Получение информации о позициях микрофона |
| [takeSeat](#takeSeat) | Занятие позиции микрофона |
| [leaveSeat](#leaveSeat) | Освобождение позиции микрофона |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/54878#takeUserOnSeatByAdmin) | Приглашение других включить трансляцию (только хост и администратор) |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/54878#kickUserOffSeatByAdmin) | Отключение других от микрофона (только хост и администратор) |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/54878#lockSeatByAdmin) | Блокировка конкретной позиции микрофона (только хост и администратор) |

### **API отправки сообщений roomEngine**

| API | Описание |
| --- | --- |
| [sendTextMessage](https://www.tencentcloud.com/document/product/647/54878#sendTextMessage) | Отправка текстового сообщения |
| [sendCustomMessage](https://www.tencentcloud.com/document/product/647/54878#sendCustomMessage) | Отправка пользовательского сообщения |

### **API управления устройствами roomEngine**

| API | Описание |
| --- | --- |
| [getCameraDevicesList](https://www.tencentcloud.com/document/product/647/54878#getCameraDevicesList) | Получение списка устройств камеры |
| [getMicDevicesList](https://www.tencentcloud.com/document/product/647/54878#getMicDevicesList) | Получение списка устройств микрофона |
| [getSpeakerDevicesList](https://www.tencentcloud.com/document/product/647/54878#getSpeakerDevicesList) | Получение списка устройств динамика |
| [setCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54878#setCurrentCameraDevice) | Установка используемой камеры |
| [setCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54878#setCurrentMicDevice) | Установка используемого микрофона |
| [setCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54878#setCurrentSpeakerDevice) | Установка используемого динамика |
| [getCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54878#getCurrentCameraDevice) | Получение текущей используемой камеры |
| [getCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54878#getCurrentMicDevice) | Получение текущего используемого микрофона |
| [getCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54878#getCurrentSpeakerDevice) | Получение текущего используемого динамика |
| [startCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54878#startCameraDeviceTest) | Начало теста камеры |
| [stopCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54878#stopCameraDeviceTest) | Остановка теста камеры |

### **API прослушивания событий roomEngine**

| API | Описание |
| --- | --- |
| [on](https://www.tencentcloud.com/document/product/647/54878#on) | Прослушивание событий [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54879#) |
| [off](https://www.tencentcloud.com/document/product/647/54878#off) | Отмена прослушивания событий [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54879#) |

### **Другой API roomEngine**

| API | Описание |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54878#getTRTCCloud) | Получение экземпляра trtcCloud |
| [getTIM](https://www.tencentcloud.com/document/product/647/54878#getTIM) | Получение экземпляра tim |

## Подробное описание API

### once

Мониторинг события готовности TUIRoomEngine

```
TUIRoomEngine.once('ready', () => {  const roomEngine = new TUIRoomEngine();    await TUIRoomEngine.login({    sdkAppId: 0,   // Заполните примененный вами sdkAppId    userId: '',    // Заполните userId, соответствующий вашему приложению    userSig: '',   // Заполните userSig, рассчитанный на сервере или локально  });    await roomEngine.createRoom({    roomId: '12345',   // Введите идентификатор комнаты, обратите внимание, что идентификатор комнаты должен быть строкового типа    name: 'Test Room',     // Введите имя комнаты, имя комнаты по умолчанию - это roomId, максимум 30 байт    roomType: TUIRoomType.kGroup, // Установите тип комнаты на TUIRoomType.kGroup  });});
```

### login

> **Описание:**В версии v1.0.0 этот интерфейс называется TUIRoomEngine.init, используйте TUIRoomEngine.login для входа в TUIRoomEngine в версии v1.0.1 и выше.

Вы должны войти в TUIRoomEngine перед тем, как вызывать другие методы TUIRoomEngine и его экземпляров.

```
// Вход в TUIRoomEngineawait TUIRoomEngine.login({ sdkAppId: 0,   // Заполните примененный вами sdkAppId userId: '',    // Заполните userId, соответствующий вашему приложению userSig: '',   // Заполните userSig, рассчитанный на сервере или локально});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| sdkAppId | number | Требуется | - | После нажатия на Application Management > Create Application в консоли Tencent Real-Time Communication вы сможете получить информацию sdkAppId в Application Info. |
| userId | string | Требуется | - | Рекомендуется ограничить длину userId до 32 байт, разрешены только прописные и строчные английские буквы (a-zA-Z), цифры (0-9), подчеркивания и дефисы. |
| userSig | string | Требуется | - | Подпись UserSigПожалуйста, обратитесь к [документации по UserSig](https://www.tencentcloud.com/document/product/647/35166) для метода расчета userSig. |
| tim | TIM | Не требуется | - | Если вы хотите использовать дополнительные возможности Chat SDK при доступе к roomEngine, вы можете передать созданный экземпляр tim в TUIRoomEngine. Способ создания экземпляра tim см. в [TIM.create](https://web.sdk.qcloud.com/im/doc/zh-cn/TIM.html#.create). |

Возвращает*Promise<void>*

### setSelfInfo

Установка основной информации текущего пользователя (имя пользователя, аватар пользователя)

```
// Установка имени пользователя и аватара текущего пользователяawait TUIRoomEngine.setSelfInfo({ userName: '',     // Введите новое имя пользователя avatarUrl: '',    // Введите новый URL аватара});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| userName | string | Требуется | - | Имя пользователя |
| avatarUrl | string | Требуется | - | Аватар пользователя |

Возвращает*Promise<void>*

### **getSelfInfo**

Получение основной информации текущего пользователя (имя пользователя, аватар пользователя)

```
// Получение имени пользователя и аватара текущего пользователяconst loginUserInfo = await TUIRoomEngine.getSelfInfo();
```

Возвращает*Promise<*[TUILoginUserInfo](https://www.tencentcloud.com/document/product/647/54876#6dd99cf1-05fd-4ef5-a4b9-d56f2b9f20ea)*> loginUserInfo*

### **logout**

> **Описание:**Интерфейс поддерживается с версии v1.0.1.

Выход из TUIRoomEngine

```
// Выход из TUIRoomEngineawait TUIRoomEngine.logout();
```

Возвращает*Promise<void>*

### createRoom

Хост создает комнату. При вызове createRoom пользователь становится владельцем комнаты. При создании комнаты вы можете установить идентификатор комнаты, имя комнаты, тип комнаты, режим выступления, разрешить ли пользователям присоединяться и включать аудио и видео, отправлять сообщения и другие функции.

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({    roomId: '12345',   // Введите идентификатор комнаты, обратите внимание, что он должен быть строкового типа    roomName: 'Test Room',     // Введите имя комнаты, имя по умолчанию - это roomId, максимальная длина 30 байт    roomType: TUIRoomType.kConference, // Установите тип комнаты на TUIRoomType.kConference    speechMode: TUISpeechMode.kFreeToSpeak, // Установите режим выступления на режим свободного выступления    isMicrophoneDisableForAllUser: false,  // Разрешить пользователям включать микрофон при входе в комнату    isCameraDisableForAllUser: false,  // Разрешить пользователям включать камеру при входе в комнату    isMessageDisableForAllUser: false,  // Разрешить пользователям отправлять сообщения при входе в комнату});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| roomId | string | Требуется | - | Идентификатор комнаты, roomId имеет ограничение длины 64 байта и поддерживает только следующие наборы символов: английские буквы (a-zA-Z), цифры (0-9), пробел ! # $ % & ( ) + - : ; < = . > ? @ [ ] ^ _ { } \| ~ , |
| roomName | string | Необязательно | roomId | Имя комнаты, значение по умолчанию - roomId, не может быть пустой строкой |
| roomType | [TUIRoomType](https://www.tencentcloud.com/document/product/647/54876#d149b153-35ff-4cab-84cb-c8d0009e179f) | Необязательно | TUIRoomType.kConference | Тип комнатыДля офисного сотрудничества, медицинских консультаций, удаленных конференций, образовательных сценариев roomType установите на TUIRoomType.kConferenceДля электронной торговли, прямых трансляций, чатов-комнат roomType установите на TUIRoomType.kLivingRoom |
| speechMode | [TUISpeechMode](https://www.tencentcloud.com/document/product/647/54876#TUISpeechMode) | Необязательно | TUISpeechMode.kFreeToSpeak | Режим выступления в комнатеДля TUIRoomType.kConference (образование и конференции): Установите speechMode на TUISpeechMode.kFreeToSpeak, пользователи могут по умолчанию включать камеру и микрофон при входе в комнату. Установите speechMode на TUISpeechMode.kApplyToSpeak, пользователи не включают по умолчанию камеру и микрофон при входе в комнату и должны попросить хоста разрешить включить камеру или микрофон. Режимы TUISpeechMode.kFreeToSpeak и TUISpeechMode.kApplyToSpeak можно переключать. Установите speechMode на TUISpeechMode.kSpeakAfterTakingSeat, пользователи должны вызвать интерфейс takeSeat для получения разрешения на включение камеры и микрофона после входа в комнату. Для TUIRoomType.kLivingRoom (сценарий прямой трансляции): Установите speechMode на TUISpeechMode.kFreeToSpeak, не требуется одобрения хоста для начала трансляции. Установите speechMode на TUISpeechMode.kSpeakAfterTakingSeat, требуется одобрение хоста для начала трансляции. Режимы TUISpeechMode.kFreeToSpeak и TUISpeechMode.kSpeakAfterTakingSeat можно переключать |
| isMicrophoneDisableForAllUser | boolean | Необязательно | false | Включить отключение для всех по умолчанию, не включать отключение для всех по умолчанию |
| isCameraDisableForAllUser | boolean | Необязательно | false | Включить отключение отрисовки для всех по умолчанию, не включать отключение отрисовки для всех по умолчанию |
| isMessageDisableForAllUser | boolean | Необязательно | false | Разрешить членам отправлять сообщения, по умолчанию не запрещено |
| maxSeatCount | number | Необязательно | - | Максимальное количество позиций микрофона. Для TUIRoomType.kConference (образование и конференции) значение maxSeatCount не ограничено. Для TUIRoomType.kLivingRoom (сценарий прямой трансляции) максимальный предел maxSeatCount составляет 16 |
| enableCDNStreaming | boolean | Необязательно | false | Включить трансляцию через CDN |
| cdnStreamDomain | string | Необязательно | '' | Домен отправки |

Возвращает*Promise<void>*

### enterRoom

Интерфейс входа в комнату

```
const roomEngine = new TUIRoomEngine();const roomInfo = await roomEngine.enterRoom({    roomId: '12345',});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| roomId | string | Требуется | - | Идентификатор комнаты |

ВозвращаетPromise<[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/54876#f8ed1be9-08fe-42ac-8ebc-5bbe11e6af10)> roomInfo

Этот интерфейс возвращает текущие данные комнаты

### destroyRoom

Интерфейс закрытия комнаты, комната должна быть закрыта владельцем, и после закрытия в комнату нельзя входить.

```
const roomEngine = new TUIRoomEngine();await roomEngine.destroyRoom();
```

Возвращает*Promise<void>*

### exitRoom

Интерфейс выхода из комнаты, пользователи могут выйти из комнаты через exitRoom после выполнения enterRoom.

```
const roomEngine = new TUIRoomEngine();await roomEngine.exitRoom();
```

Возвращает*Promise<void>*

### fetchRoomInfo

Получение информации о комнате

```
const roomEngine = new TUIRoomEngine();const roomInfo = roomEngine.fetchRoomInfo();
```

Возвращает*Promise<*[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/54876#f8ed1be9-08fe-42ac-8ebc-5bbe11e6af10)*> roomInfo*

### updateRoomNameByAdmin

Обновление имени текущей комнаты (только владелец группы или администратор могут вызвать)

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({ roomId: '12345' });await roomEngine.updateRoomNameByAdmin({ roomName: 'NewName' });
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| roomName | string | Требуется | - | Обновить имя комнаты, требование состоит в том, что roomName не должно быть пустой строкой |

### updateRoomSpeechModeByAdmin

Обновление режима выступления комнаты (только владелец группы или администратор могут вызвать)

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({ roomId: '12345' });await roomEngine.updateRoomSpeechModeByAdmin({  speechMode: TUISpeechMode.kSpeakAfterTakingSeat  // Обновить на режим выступления при занятии места});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| speechMode | TUISpeechMode | Требуется | - | Обновить режим выступления комнаты |

### getUserList

Получение списка пользователей текущей комнаты, обратите внимание, что максимальное количество пользователей, полученное этим интерфейсом, составляет 100

```
const roomEngine = new TUIRoomEngine();const userList = [];let result;do {  result = await globalProperties.roomEngine.getUserList();  userList.push(...result.userInfoList);} while (result.nextSequence !== 0)
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| nextSequence | number | Необязательно | 0 | Смещение, по умолчанию начинается с 0 |

Возвращает*Promise<Array> result*

result.nextSequence - это смещение для получения пользователей группы в следующий раз; если result.nextSequence равно 0, это означает, что все userList получены

result.userInfoList - это userList, полученный на этот раз

### getUserInfo

Получение подробной информации о пользователе

```
const roomEngine = new TUIRoomEngine();const userList = [];const userInfo = await roomEngine.getUserInfo({    userId: 'user_12345',});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| userId | string | Требуется | - | Получить подробную информацию пользователя согласно userId |

Возвращает*Promise<Array<*[TUIUserInfo](https://www.tencentcloud.com/document/product/647/54876#6dd99cf1-05fd-4ef5-a4b9-d56f2b9f20ea)*>> userInfoList*

Этот интерфейс возвращает информацию о пользователе указанного пользователя

### setLocalVideoView

Установка позиции отрисовки локального потока

```
const roomEngine = new TUIRoomEngine();    // Установить область воспроизведения локального видеопотока камеры в div-элемент с id 'preview-camera'await roomEngine.setLocalVideoView({  streamType: TUIVideoStreamType.kCameraStream,  view: 'preview-camera',});    // Установить область воспроизведения локального видеопотока общей экран в div-элемент с id 'preview-screen'await roomEngine.setLocalVideoView({  streamType: TUIVideoStreamType.kScreenStream,  view: 'preview-screen',});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| streamType | [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/54876#d129c5f7-80b8-4768-9394-e22b9af3f868) | Требуется | - | Тип локального потока |
| view | string | Требуется | - | Идентификатор div-элемента, соответствующий streamType |

Возвращает*Promise<void>*

### openLocalCamera

Открытие локальной камеры и начало захвата видеопотока

```
const roomEngine = new TUIRoomEngine();await roomEngine.setLocalVideoView({  streamType: TUIVideoStreamType.kCameraStream,  view: 'preview-camera',});await roomEngine.openLocalCamera();
```

Возвращает*Promise<void>*

### closeLocalCamera

Закрытие локальной камеры

```
const roomEngine = new TUIRoomEngine();await roomEngine.closeLocalCamera();
```

Возвращает*Promise<void>*

### openLocalMicrophone

Открытие локального микрофона

---
*Источник (EN): [tuiroomengine.md](./tuiroomengine.md)*
