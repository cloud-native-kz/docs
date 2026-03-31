# TUIRoomEngine

## Введение в TUIRoomEngine

SDK TUIRoomEngine предоставляет функции управления комнатой, многопользовательскую связь Tencent Real-Time Communication, общий доступ к экрану, управление участниками, мгновенную передачу сообщений и другие функции.

**Способ установки:**

```
// Использование npmnpm i @tencentcloud/tuiroom-engine-electron --save// Использование pnpmpnpm i @tencentcloud/tuiroom-engine-electron --save// Использование yarnyarn add @tencentcloud/tuiroom-engine-electron
```

## API TUIRoomEngine

### **Статические методы TUIRoomEngine**

| API | Описание |
| --- | --- |
| [once](https://www.tencentcloud.com/document/product/647/54883#once) | **Прослушивание события готовности TUIRoomEngine. Примечание: все методы, кроме TUIRoomEngine.login, должны выполняться после прослушивания события готовности TUIRoomEngine и успешного выполнения метода TUIRoomEngine.login.** |
| [login](https://www.tencentcloud.com/document/product/647/54883#login) | Вход в TUIRoomEngine |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54883#setSelfInfo) | Установка базовой информации текущего пользователя (имя пользователя, аватар пользователя) |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54883#getSelfInfo) | Получение базовой информации текущего пользователя (имя пользователя, аватар пользователя) |
| [logout](https://www.tencentcloud.com/document/product/647/54883#logout) | Выход из TUIRoomEngine |

### **API управления комнатой roomEngine**

| API | Описание |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/54883#createRoom) | Создание комнаты |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54883#enterRoom) | Вход в комнату |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/54883#destroyRoom) | Удаление комнаты |
| [exitRoom](https://www.tencentcloud.com/document/product/647/54883#exitRoom) | Выход из комнаты |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/54883#fetchRoomInfo) | Получение данных комнаты |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/54883#updateRoomNameByAdmin) | Обновление имени (только владелец группы или администратор) |
| [updateRoomSpeechModeByAdmin](https://www.tencentcloud.com/document/product/647/54883#updateRoomSpeechModeByAdmin) | Обновление режима выступления (только владелец группы или администратор) |
| [getUserList](https://www.tencentcloud.com/document/product/647/54883#getUserList) | Получение списка пользователей |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/54883#getUserInfo) | Получение подробной информации о пользователе |

### **API аудио-видео roomEngine**

| API | Описание |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/54883#setLocalVideoView) | Установка позиции отрисовки локального потока |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/54883#openLocalCamera) | Захват видеопотока локальной камеры |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/54883#closeLocalCamera) | Закрытие локальной камеры |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/54883#openLocalMicrophone) | Включение локального микрофона |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/54883#closeLocalMicrophone) | Отключение локального микрофона |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/54883#updateVideoQuality) | Установка параметров локального видео |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/54883#updateAudioQuality) | Установка параметров локального аудио |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/54883#startPushLocalVideo) | Начало отправки локального видеопотока удаленно |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/54883#stopPushLocalVideo) | Остановка отправки локального видеопотока удаленно |
| [startPushLocalAudio](https://www.tencentcloud.com/document/product/647/54883#startPushLocalAudio) | Начало отправки локального аудиопотока удаленно |
| [stopPushLocalAudio](https://www.tencentcloud.com/document/product/647/54883#stopPushLocalAudio) | Остановка отправки локального аудиопотока удаленно |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/54883#setRemoteVideoView) | Установка области отрисовки удаленного потока |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54883#startPlayRemoteVideo) | Начало воспроизведения видеопотока удаленного пользователя |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54883#stopPlayRemoteVideo) | Остановка воспроизведения видеопотока удаленного пользователя |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/54883#muteRemoteAudioStream) | Остановка аудиопотока удаленного пользователя |

### **API управления участниками roomEngine**

| API | Описание |
| --- | --- |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54883#openRemoteDeviceByAdmin) | Запрос удаленного пользователя открыть медиаустройство |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/54883#applyToAdminToOpenLocalDevice) | Запрос участника к хосту на открытие устройства |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54883#closeRemoteDeviceByAdmin) | Закрытие медиаустройства удаленного пользователя |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/54883#cancelRequest) | Отмена отправленного запроса |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/54883#responseRemoteRequest) | Ответ на запрос удаленного пользователя |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/54883#changeUserRole) | Изменение роли пользователя |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/54883#kickRemoteUserOutOfRoom) | Исключение пользователя из комнаты |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/54883#disableDeviceForAllUserByAdmin) | Отключение/включение медиаустройства всех пользователей |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/54883#disableSendingMessageForAllUser) | Запрет/разрешение всем пользователям отправлять сообщения |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/54883#disableSendingMessageByAdmin) | Запрет/разрешение конкретному пользователю отправлять сообщения |

### **API общего доступа к экрану roomEngine**

| API | Описание |
| --- | --- |
| [startScreenSharingElectron](https://www.tencentcloud.com/document/product/647/54883#startScreenSharingElectron) | Начало общего доступа к экрану |
| [stopScreenSharingElectron](https://www.tencentcloud.com/document/product/647/54883#stopScreenSharingElectron) | Остановка общего доступа к экрану |
| [getScreenSharingTarget](https://www.tencentcloud.com/document/product/647/54883#getScreenSharingTarget) | Получение списка общего доступа к экрану |
| [selectScreenSharingTarget](https://www.tencentcloud.com/document/product/647/54883#selectScreenSharingTarget) | Переключение окна общего доступа к экрану |

### **API управления позициями микрофона roomEngine**

| API | Описание |
| --- | --- |
| [setMaxSeatCount](https://www.tencentcloud.com/document/product/647/54883#setMaxSeatCount) | Установка максимального количества позиций в комнате |
| [getSeatList](https://www.tencentcloud.com/document/product/647/54883#getSeatList) | Получение информации о позициях микрофона |
| [takeSeat](https://www.tencentcloud.com/document/product/647/54883#takeSeat) | Занятие позиции микрофона |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/54883#leaveSeat) | Освобождение позиции микрофона |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/54883#takeUserOnSeatByAdmin) | Приглашение других начать трансляцию (только хост и администратор комнаты) |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/54883#kickUserOffSeatByAdmin) | Удаление других с микрофона (только хост и администратор комнаты) |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/54883#lockSeatByAdmin) | Блокировка конкретной позиции микрофона (только хост и администратор комнаты) |

### **API отправки сообщений roomEngine**

| API | Описание |
| --- | --- |
| [sendTextMessage](https://www.tencentcloud.com/document/product/647/54883#sendTextMessage) | Отправка текстового сообщения |
| [sendCustomMessage](https://www.tencentcloud.com/document/product/647/54883#sendCustomMessage) | Отправка пользовательского сообщения |

### **API управления устройствами roomEngine**

| API | Описание |
| --- | --- |
| [getCameraDevicesList](https://www.tencentcloud.com/document/product/647/54883#getCameraDevicesList) | Получение списка устройств камеры |
| [getMicDevicesList](https://www.tencentcloud.com/document/product/647/54883#getMicDevicesList) | Получение списка устройств микрофона |
| [getSpeakerDevicesList](https://www.tencentcloud.com/document/product/647/54883#getSpeakerDevicesList) | Получение списка устройств динамика |
| [setCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54883#setCurrentCameraDevice) | Выбор используемой камеры |
| [setCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54883#setCurrentMicDevice) | Выбор используемого микрофона |
| [setCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54883#setCurrentSpeakerDevice) | Выбор используемого динамика |
| [getCurrentCameraDevice](https://www.tencentcloud.com/document/product/647/54883#getCurrentCameraDevice) | Получение текущей используемой камеры |
| [getCurrentMicDevice](https://www.tencentcloud.com/document/product/647/54883#getCurrentMicDevice) | Получение текущего используемого микрофона |
| [getCurrentSpeakerDevice](https://www.tencentcloud.com/document/product/647/54883#getCurrentSpeakerDevice) | Получение текущего используемого динамика |
| [startCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54883#startCameraDeviceTest) | Начало тестирования камеры |
| [stopCameraDeviceTest](https://www.tencentcloud.com/document/product/647/54883#stopCameraDeviceTest) | Остановка тестирования камеры |

### **API прослушивания событий roomEngine**

| API | Описание |
| --- | --- |
| [on](https://www.tencentcloud.com/document/product/647/54883#on) | Прослушивание [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54884) |
| [off](https://www.tencentcloud.com/document/product/647/54883#off) | Отмена прослушивания [TUIRoomEvents](https://www.tencentcloud.com/document/product/647/54884) |

### **Другие API roomEngine**

| API | Описание |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54883#getTRTCCloud) | Получение экземпляра trtcCloud |
| [getTIM](https://www.tencentcloud.com/document/product/647/54883#getTIM) | Получение экземпляра tim |

## Подробное описание API

### once

Мониторинг события готовности TUIRoomEngine

```
TUIRoomEngine.once('ready', () => {  const roomEngine = new TUIRoomEngine();    await TUIRoomEngine.init({    sdkAppId: 0,   // Заполните применяемый вами sdkAppId    userId: '',    // Заполните userId, соответствующий вашему бизнесу    userSig: '',   // Заполните userSig, рассчитанный сервером или локально  });    await roomEngine.createRoom({    roomId: '12345',   // Введите ваш ID комнаты, обратите внимание, что ID комнаты должен быть типом string    name: 'Test Room',     // Введите имя вашей комнаты, имя комнаты по умолчанию — roomId, максимум 30 байт    roomType: TUIRoomType.kGroup, // Установите тип комнаты на TUIRoomType.kGroup  });});
```

### login

> **Описание:** В версии v1.0.0 этот интерфейс называется TUIRoomEngine.init, пожалуйста, используйте TUIRoomEngine.login для входа в TUIRoomEngine в версиях v1.0.1 и выше.

Вы должны войти в TUIRoomEngine перед вызовом других методов TUIRoomEngine и его экземпляров.

```
// Вход в TUIRoomEngineawait TUIRoomEngine.login({ sdkAppId: 0,   // Заполните применяемый вами sdkAppId userId: '',    // Заполните userId, соответствующий вашему бизнесу userSig: '',   // Заполните userSig, рассчитанный сервером или локально});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| sdkAppId | number | Обязательный | - | После нажатия Application Management > Create Application в консоли Tencent Real-Time Communication вы можете получить информацию sdkAppId в Application Info. |
| userId | string | Обязательный | - | Рекомендуется ограничить длину ID пользователя до 32 байт, разрешены только латинские буквы верхнего и нижнего регистра (a-zA-Z), цифры (0-9), подчеркивания и дефисы. |
| userSig | string | Обязательный | - | Подпись UserSig. Пожалуйста, обратитесь к [информации о UserSig](https://www.tencentcloud.com/document/product/647/35166) для метода расчета userSig. |
| tim | TIM | Необязательный | - | Если вы хотите использовать дополнительные возможности Chat SDK при доступе к roomEngine, вы можете передать созданный экземпляр tim в TUIRoomEngine. Для метода создания экземпляра tim обратитесь к [TIM.create](https://web.sdk.qcloud.com/im/doc/zh-cn/TIM.html#.create). |

**Возвращает***Promise<void>*

### setSelfInfo

Установка базовой информации текущего пользователя (имя пользователя, аватар пользователя).

```
// Установка имени пользователя и аватара текущего пользователяawait TUIRoomEngine.setSelfInfo({ userName: '',     // Введите новое имя пользователя avatarUrl: '',    // Введите новый URL аватара});
```

**Параметры:**

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| userName | string | Обязательный | - | Имя пользователя |
| avatarUrl | string | Обязательный | - | Аватар пользователя |

**Возвращает***Promise<void>*

### **getSelfInfo**

Получение базовой информации текущего пользователя (имя пользователя, аватар пользователя).

```
// Получение имени пользователя и аватара текущего пользователяconst loginUserInfo = await TUIRoomEngine.getSelfInfo();
```

Возвращает*Promise<*[TUILoginUserInfo](https://www.tencentcloud.com/document/product/647/54886#TUILoginUserInfo)*> loginUserInfo*

### **logout**

> **Описание:** Интерфейс поддерживается с версии v1.0.1.

Выход из TUIRoomEngine

```
// Выход из TUIRoomEngineawait TUIRoomEngine.logout();
```

Возвращает*Promise<void>*

### createRoom

Хост создает комнату, вызов createRoom. Пользователь, вызывающий метод, становится владельцем комнаты. При создании комнаты вы можете установить ID комнаты, имя комнаты, тип комнаты, режим выступления, разрешить ли пользователям присоединяться и включать аудио и видео, отправлять сообщения и другие функции.

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({    roomId: '12345',   // Введите ваш ID комнаты, обратите внимание, что ID комнаты должен быть типом string    roomName: 'Test Room',     // Введите имя вашей комнаты, имя комнаты по умолчанию — roomId, максимальная длина 30 байт    roomType: TUIRoomType.kConference, // Установите тип комнаты на TUIRoomType.kConference    speechMode: TUISpeechMode.kFreeToSpeak, // Установите режим выступления на режим свободного выступления    isMicrophoneDisableForAllUser: false,  // Разрешить пользователям включать микрофон при присоединении к комнате    isCameraDisableForAllUser: false,  // Разрешить пользователям включать камеру при присоединении к комнате    isMessageDisableForAllUser: false,  // Разрешить пользователям отправлять сообщения при присоединении к комнате});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| roomId | string | Обязательный | - | ID комнаты, roomId имеет ограничение по длине в 64 байта и поддерживает только следующий набор символов: латинские буквы (a-zA-Z), цифры (0-9), пробел ! # $ % & ( ) + - : ; < = . > ? @ [ ] ^ _ { } \| ~ , |
| roomName | string | Необязательный | roomId | Имя комнаты, значение по умолчанию — roomId, не может быть пустой строкой |
| roomType | [TUIRoomType](https://www.tencentcloud.com/document/product/647/54886#TUIRoomType) | Необязательный | TUIRoomType.kConference | Тип комнаты. Для офисного сотрудничества, медицинских консультаций, удаленных конференций, образовательных сценариев roomType устанавливается на TUIRoomType.kConference. Для прямого эфира электронной коммерции, сценариев чат-комнаты roomType устанавливается на TUIRoomType.kLivingRoom |
| speechMode | TUISpeechMode | Необязательный | TUISpeechMode.kFreeToSpeak | Режим выступления в комнате. Для TUIRoomType.kConference (образовательные и конференц-сценарии): установите speechMode на TUISpeechMode.kFreeToSpeak, пользователи могут включить камеру и микрофон по умолчанию при входе в комнату. Установите speechMode на TUISpeechMode.kApplyToSpeak, пользователи не включают камеру и микрофон по умолчанию при входе в комнату и должны подать заявку хосту на включение камеры или микрофона. TUISpeechMode.kFreeToSpeak и TUISpeechMode.kApplyToSpeak режимы могут переключаться. Установите speechMode на TUISpeechMode.kSpeakAfterTakingSeat, пользователи должны вызвать интерфейс takeSeat для получения разрешения на включение камеры и микрофона после входа в комнату. Для TUIRoomType.kLivingRoom (сценарий прямого эфира): установите speechMode на TUISpeechMode.kFreeToSpeak, не требуется одобрение хоста для начала трансляции. Установите speechMode на TUISpeechMode.kSpeakAfterTakingSeat, требуется одобрение хоста для начала трансляции. TUISpeechMode.kFreeToSpeak и TUISpeechMode.kSpeakAfterTakingSeat режимы могут переключаться |
| isMicrophoneDisableForAllUser | boolean | Необязательный | false | Включение отключения всех по умолчанию, не включать отключение всех по умолчанию |
| isCameraDisableForAllUser | boolean | Необязательный | false | Включение отключения всех видео по умолчанию, не включать отключение всех видео по умолчанию |
| isMessageDisableForAllUser | boolean | Необязательный | false | Разрешить членам отправлять сообщения, по умолчанию не запрещать |
| maxSeatCount | number | Необязательный | - | Максимальное количество позиций микрофона. Для TUIRoomType.kConference (образовательные и конференц-сценарии) значение maxSeatCount не ограничено. Для TUIRoomType.kLivingRoom (сценарий прямого эфира) максимальный предел maxSeatCount составляет 16 |
| enableCDNStreaming | boolean | Необязательный | false | Включение потока CDN |
| cdnStreamDomain | string | Необязательный | '' | Домен отправки |

Возвращает*Promise<void>*

### enterRoom

Интерфейс входа в комнату.

```
const roomEngine = new TUIRoomEngine();const roomInfo = await roomEngine.enterRoom({    roomId: '12345',});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| roomId | string | Обязательный | - | ID комнаты |

**Возвращает***Promise<*[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/54886#TUIRoomInfo)*> roomInfo*

Этот интерфейс возвращает текущие данные комнаты

### destroyRoom

Интерфейс закрытия комнаты, комната должна быть закрыта владельцем комнаты, и после закрытия в нее больше нельзя будет входить.

```
const roomEngine = new TUIRoomEngine();await roomEngine.destroyRoom();
```

**Возвращает***Promise<void>*

### exitRoom

Интерфейс выхода из комнаты, пользователи могут выйти из комнаты через exitRoom после выполнения enterRoom.

```
const roomEngine = new TUIRoomEngine();await roomEngine.exitRoom();
```

**Возвращает***Promise<void>*

### fetchRoomInfo

Получение информации о комнате.

```
const roomEngine = new TUIRoomEngine();const roomInfo = roomEngine.fetchRoomInfo();
```

Возвращает*Promise<*[TUIRoomInfo](https://www.tencentcloud.com/document/product/647/54886#TUIRoomInfo)*> roomInfo*

### updateRoomNameByAdmin

Обновление имени текущей комнаты (только владелец группы или администратор могут вызвать).

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({ roomId: '12345' });await roomEngine.updateRoomNameByAdmin({ roomName: 'new name' });
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| roomName | string | Обязательный | - | Обновите имя комнаты, требование: roomName не должен быть пустой строкой |

**Возвращает***Promise<void>*

### updateRoomSpeechModeByAdmin

Обновление режима выступления в комнате (только владелец группы или администратор могут вызвать).

```
const roomEngine = new TUIRoomEngine();await roomEngine.createRoom({ roomId: '12345' });await roomEngine.updateRoomSpeechModeByAdmin({  speechMode: TUISpeechMode.kSpeakAfterTakingSeat  // Обновить на режим выступления после занятия позиции});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| speechMode | TUISpeechMode | Обязательный | - | Обновить режим выступления в комнате |

### getUserList

Получение списка пользователей в текущей комнате, обратите внимание, что максимальное количество извлекаемых этим интерфейсом списков пользователей составляет 100.

```
const roomEngine = new TUIRoomEngine();const userList = [];let result;do {  result = await globalProperties.roomEngine.getUserList();  userList.push(...result.userInfoList);} while (result.nextSequence !== 0)
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| nextSequence | number | Необязательный | 0 | Смещение, по умолчанию начинается с 0 для извлечения пользователей |

**Возвращает**ï¼*Promise<object>  result*

result.nextSequence — это смещение для следующего извлечения пользователей группы, если result.nextSequence равно 0, это означает, что все userList были извлечены

result.userInfoList — это список пользователей, извлеченный на этот раз

### getUserInfo

Получение подробной информации о пользователе.

```
const roomEngine = new TUIRoomEngine();const userList = [];const userInfo = await roomEngine.getUserInfo({    userId: 'user_12345',});
```

Параметры:

| Параметр | Тип | Описание | Значение по умолчанию | Значение |
| --- | --- | --- | --- | --- |
| userId | string | Обязательный | - | Получение подробной информации о пользователе в соответствии с userId |

**Возвращает**ï¼*Promise<*[TUIUserInfo](https://www.tencentcloud.com/document/product/647/54886#TUIUserInfo)*> userInfo*

Этот интерфейс возвращает информацию о пользователе указанного пользователя

---
*Источник (EN): [tuiroomengine.md](./tuiroomengine.md)*
