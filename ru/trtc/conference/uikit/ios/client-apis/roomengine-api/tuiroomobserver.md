# TUIRoomObserver

**TUIRoomObserver**

## TUIRoomObserver

| FuncList | DESC |
| --- | --- |
| [onError:message:](https://www.tencentcloud.com/document/product/647/54854#e2d2a8b13e80bbe60e2467739f0a0316) | Обратный вызов события ошибки. |
| [onKickedOffLine:](https://www.tencentcloud.com/document/product/647/54854#b0238d7b1fa86af2c540ec313dba8e6b) | Текущий пользователь был отключен. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/54854#7b8df3f701ffd641b11047e27094d8db) | Подпись текущего пользователя истекла. |
| [onRoomNameChanged:roomName:](https://www.tencentcloud.com/document/product/647/54854#14f6f031aedb2aef37640bd8d52b512d) | Имя комнаты было изменено. |
| [onAllUserMicrophoneDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#3ec4485cdec9612c161c8a3211b2fb28) | Статус отключения открытия микрофона изменился для всех пользователей. |
| [onAllUserCameraDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#55a547bc323badf7599db85f13c6b286) | Статус отключения открытия камеры изменился для всех пользователей. |
| [onScreenShareForAllUserDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#fe6861c09539278fb9440da696c4d028) | Статус отключения открытия общей экрана изменился для всех пользователей. |
| [onSendMessageForAllUserDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#b64a6a83036eb91c14d381c1feca555b) | Статус отключения отправки сообщений изменился для всех пользователей. |
| [onRoomDismissed:reason:](https://www.tencentcloud.com/document/product/647/54854#e3741060867444c54121e60eb54f989c) | Комната была закрыта. |
| [onKickedOutOfRoom:reason:message:](https://www.tencentcloud.com/document/product/647/54854#bbebfbd4e8b6c95b7852d1493f60bd4e) | Текущий пользователь был исключен из комнаты. |
| [onRoomSeatModeChanged:seatMode:](https://www.tencentcloud.com/document/product/647/54854#43c39ab0e5611de1f28bfe62e4e0077b) | Режим мест в комнате был изменен. |
| [onRoomUserCountChanged:userCount:](https://www.tencentcloud.com/document/product/647/54854#4c5cdb0b2676614586770fe9085576fe) | Количество пользователей в комнате изменилось. |
| [onRoomMetadataChanged:value:](https://www.tencentcloud.com/document/product/647/54854#f3151fab3ff4a34eed91d740e05c9d5f) | Значение ключа метаданных комнаты изменилось. |
| [onRemoteUserEnterRoom:userInfo:](https://www.tencentcloud.com/document/product/647/54854#64bc4ce1b62e5a15de963ecfb9225e98) | Удаленный пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom:userInfo:](https://www.tencentcloud.com/document/product/647/54854#16b0d80475c0d1f945024d5116074c66) | Удаленный пользователь покинул комнату. |
| [onUserInfoChanged:modifyFlag:](https://www.tencentcloud.com/document/product/647/54854#b5637d7d08d9811983db56c8dd28f051) | Информация пользователя в комнате изменилась. |
| [onUserVideoStateChanged:streamType:hasVideo:reason:](https://www.tencentcloud.com/document/product/647/54854#00c4eb2525cf2b404bb784d7731d95a8) | Статус видеопотока пользователя изменился. |
| [onUserAudioStateChanged:hasAudio:reason:](https://www.tencentcloud.com/document/product/647/54854#57eafbcdec43b9cacef68034b3087e45) | Статус аудиопотока пользователя изменился. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54854#65abb01367f2509a0457ba351efb1fe1) | Громкость голоса пользователя изменилась. |
| [onSendMessageForUserDisableChanged:userId:isDisable:](https://www.tencentcloud.com/document/product/647/54854#d1f497f96f9523b0d284992b90b22d26) | Статус отключения отправки сообщений для пользователя изменился. |
| [onUserNetworkQualityChanged:](https://www.tencentcloud.com/document/product/647/54854#1147aa1bf7e279740ad961bdbbd626bb) | Статус сетевого соединения пользователя изменился. |
| [onUserScreenCapturePaused:](https://www.tencentcloud.com/document/product/647/54854#73cb544fa8fd92b8a607a9298ce686ae) | Общая доступ экрана приостановлена. |
| [onUserScreenCaptureResumed:](https://www.tencentcloud.com/document/product/647/54854#48f8345803b57e6ec01593732ec756e7) | Общая доступ экрана возобновлена. |
| [onUserScreenCaptureStopped:](https://www.tencentcloud.com/document/product/647/54854#f6bae569cb7519e87904a735c61605da) | Общая доступ экрана остановлена. |
| [onUserVideoSizeChanged:userId:streamType:width:height:](https://www.tencentcloud.com/document/product/647/54854#850d2069ee734aa8537e9fe830f3591d) | Размер видео пользователя изменился. |
| [onSeatListChanged:seated:left:](https://www.tencentcloud.com/document/product/647/54854#31a13be6f374e28422eb363a518b235f) | Список мест изменился. |
| [onKickedOffSeat:operateUser:](https://www.tencentcloud.com/document/product/647/54854#bd26ee6b56090e87eb9409c47df09435) | Пользователь был исключен с места. |
| [onRequestReceived:](https://www.tencentcloud.com/document/product/647/54854#3697d1d038fd6f3ebe54ea33cd32e3df) | Получено сообщение запроса. |
| [onRequestCancelled:operateUser:](https://www.tencentcloud.com/document/product/647/54854#92b334084d0e34a0a3d4507e02acb850) | Получен отмененный запрос. |
| [onRequestProcessed:operateUser:](https://www.tencentcloud.com/document/product/647/54854#ca708aa561838272c90fa5e3e4eb41e7) | Получен запрос, обработанный другим администратором/владельцем. |
| [onReceiveTextMessage:](https://www.tencentcloud.com/document/product/647/54854#ac7c0d898f526f0f902a83c49afffd64) | Текстовое сообщение получено |
| [onReceiveCustomMessage:](https://www.tencentcloud.com/document/product/647/54854#a8574308a070707a877d1c699a9c3aba) | Пользовательское сообщение получено |
| [onDeviceChanged:type:state:](https://www.tencentcloud.com/document/product/647/54854#8bb5da23b114eee5d7422671ada72503) | Локальное устройство добавлено. |

## onError:message:

**onError:message:**

| - (void)onError: | ([TUIError](https://www.tencentcloud.com/document/product/647/64475#d41b099f14c721618a59bac76f0f456b))errorCode |
| --- | --- |
| message: | (NSString *)message |

#### Обратный вызов события ошибки.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Обратный вызов событий ошибок при входе в комнату или открытии устройства.

| Param | DESC |
| --- | --- |
| errorCode | Код ошибки. Дополнительные сведения см. в [TUIError](https://www.tencentcloud.com/document/product/647/64475#d41b099f14c721618a59bac76f0f456b). |
| message | Сообщение об ошибке. |

## onKickedOffLine:

**onKickedOffLine:**

| - (void)onKickedOffLine: | (NSString *)message |
| --- | --- |

#### Текущий пользователь был отключен.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается, когда пользователь отключается.

| Param | DESC |
| --- | --- |
| message | Описание отключения. |

## onUserSigExpired

**onUserSigExpired**

#### Подпись текущего пользователя истекла.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при истечении срока действия подписи пользователя.

## onRoomNameChanged:roomName:

**onRoomNameChanged:roomName:**

| - (void)onRoomNameChanged: | (NSString *)roomId |
| --- | --- |
| roomName: | (NSString *)roomName |

#### Имя комнаты было изменено.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при изменении имени комнаты.

| Param | DESC |
| --- | --- |
| roomId | ID комнаты. |
| roomName | Имя комнаты. |

## onAllUserMicrophoneDisableChanged:isDisable:

**onAllUserMicrophoneDisableChanged:isDisable:**

| - (void)onAllUserMicrophoneDisableChanged: | (NSString *)roomId |
| --- | --- |
| isDisable: | (BOOL)isDisable |

#### Статус отключения открытия микрофона изменился для всех пользователей.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить для пользователей открытие микрофона false: разрешить пользователям открытие микрофона. |
| roomId | ID комнаты. |

> **Примечание**Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)..Вызывается при изменении статуса отключения микрофона для всех пользователей.

## onAllUserCameraDisableChanged:isDisable:

**onAllUserCameraDisableChanged:isDisable:**

| - (void)onAllUserCameraDisableChanged: | (NSString *)roomId |
| --- | --- |
| isDisable: | (BOOL)isDisable |

#### Статус отключения открытия камеры изменился для всех пользователей.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить для пользователей открытие камеры false: разрешить пользователям открытие камеры. |
| roomId | ID комнаты. |

> **Примечание**Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)..Вызывается при изменении статуса отключения камеры для всех пользователей.

## onScreenShareForAllUserDisableChanged:isDisable:

**onScreenShareForAllUserDisableChanged:isDisable:**

| - (void)onScreenShareForAllUserDisableChanged: | (NSString *)roomId |
| --- | --- |
| isDisable: | (BOOL)isDisable |

#### Статус отключения открытия общей экрана изменился для всех пользователей.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить для пользователей открытие общей экрана false: разрешить пользователям открытие общей экрана. |
| roomId | ID комнаты. |

> **Примечание**Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)..Вызывается при изменении прав доступа для общей экрана для всех пользователей.

## onSendMessageForAllUserDisableChanged:isDisable:

**onSendMessageForAllUserDisableChanged:isDisable:**

| - (void)onSendMessageForAllUserDisableChanged: | (NSString *)roomId |
| --- | --- |
| isDisable: | (BOOL)isDisable |

#### Статус отключения отправки сообщений изменился для всех пользователей.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить отправку сообщений для пользователей false: разрешить отправку сообщений для пользователей. |
| roomId | ID комнаты. |

> **Примечание**Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)..Вызывается при изменении прав доступа для отправки сообщений для всех пользователей.

## onRoomDismissed:reason:

**onRoomDismissed:reason:**

| - (void)onRoomDismissed: | (NSString *)roomId |
| --- | --- |
| reason: | ([TUIRoomDismissedReason](https://www.tencentcloud.com/document/product/647/64477#9e97a16d20d331906cc0990099121355))reason |

#### Комната была закрыта.

| Param | DESC |
| --- | --- |
| reason | Причина закрытия комнаты. Дополнительные сведения см. в [TUIRoomDismissedReason](https://www.tencentcloud.com/document/product/647/64477#9e97a16d20d331906cc0990099121355). |
| roomId | ID комнаты. |

> **Примечание**Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)..Вызывается при закрытии комнаты.

## onKickedOutOfRoom:reason:message:

**onKickedOutOfRoom:reason:message:**

| - (void)onKickedOutOfRoom: | (NSString *)roomId |
| --- | --- |
| reason: | ([TUIKickedOutOfRoomReason](https://www.tencentcloud.com/document/product/647/64477#c6b3c5e07b71d50181b15edf97f384c8))reason |
| message: | (NSString *)message |

#### Текущий пользователь был исключен из комнаты.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при исключении пользователя из комнаты.

| Param | DESC |
| --- | --- |
| message | Описание исключения. |
| reason | Причина исключения. |
| roomId | ID комнаты. |

## onRoomSeatModeChanged:seatMode:

**onRoomSeatModeChanged:seatMode:**

| - (void)onRoomSeatModeChanged: | (NSString *)roomId |
| --- | --- |
| seatMode: | ([TUISeatMode](https://www.tencentcloud.com/document/product/647/64477#6e6fdc219cc838c9e3c5d622ab32c8f1))seatMode |

#### Режим мест в комнате был изменен.

| Param | DESC |
| --- | --- |
| roomId | : ID комнаты. |
| seatMode | : Режим мест. Дополнительные сведения см. в [TUISeatMode](https://www.tencentcloud.com/document/product/647/64477#6e6fdc219cc838c9e3c5d622ab32c8f1).#### [REMARK]Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).Вызывается при изменении режима мест комнаты. |

## onRoomUserCountChanged:userCount:

**onRoomUserCountChanged:userCount:**

| - (void)onRoomUserCountChanged: | (NSString *)roomId |
| --- | --- |
| userCount: | (NSInteger)userCount |

#### Количество пользователей в комнате изменилось.

| Param | DESC |
| --- | --- |
| roomId | ID комнаты. |
| userCount | Количество пользователей.#### [REMARK]Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).Вызывается при изменении количества пользователей в комнате. |

## onRoomMetadataChanged:value:

**onRoomMetadataChanged:value:**

| - (void)onRoomMetadataChanged: | (NSString *)key |
| --- | --- |
| value: | (NSString *)value |

#### Значение ключа метаданных комнаты изменилось.

| Param | DESC |
| --- | --- |
| key | Ключ метаданных комнаты. |
| value | Значение метаданных комнаты.#### [REMARK]Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).Вызывается при изменении пользовательской информации комнаты. |

## onRemoteUserEnterRoom:userInfo:

**onRemoteUserEnterRoom:userInfo:**

| - (void)onRemoteUserEnterRoom: | (NSString *)roomId |
| --- | --- |
| userInfo: | ([TUIUserInfo](https://www.tencentcloud.com/document/product/647/64477#f619c1d19040e033e9fa88e0946cc619) *)userInfo |

#### Удаленный пользователь вошел в комнату.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при входе удаленного пользователя в комнату.

| Param | DESC |
| --- | --- |
| roomId | ID комнаты. |
| userInfo | Информация о пользователе. Дополнительные сведения см. в [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64477#f619c1d19040e033e9fa88e0946cc619). |

## onRemoteUserLeaveRoom:userInfo:

**onRemoteUserLeaveRoom:userInfo:**

| - (void)onRemoteUserLeaveRoom: | (NSString *)roomId |
| --- | --- |
| userInfo: | ([TUIUserInfo](https://www.tencentcloud.com/document/product/647/64477#f619c1d19040e033e9fa88e0946cc619) *)userInfo |

#### Удаленный пользователь покинул комнату.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при выходе удаленного пользователя из комнаты.

| Param | DESC |
| --- | --- |
| roomId | ID комнаты. |
| userInfo | Информация о пользователе. Дополнительные сведения см. в [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64477#f619c1d19040e033e9fa88e0946cc619). |

## onUserInfoChanged:modifyFlag:

**onUserInfoChanged:modifyFlag:**

| - (void)onUserInfoChanged: | ([TUIUserInfo](https://www.tencentcloud.com/document/product/647/64477#f619c1d19040e033e9fa88e0946cc619) *)userInfo |
| --- | --- |
| modifyFlag: | (TUIUserInfoModifyFlag)modifyFlag |

#### Информация пользователя в комнате изменилась.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при изменении информации пользователя.

| Param | DESC |
| --- | --- |
| modifyFlag | Изменяемый параметр. Дополнительные сведения см. в TUIUserInfoModifyFlag. |
| userInfo | Информация о пользователе. Дополнительные сведения см. в [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64477#f619c1d19040e033e9fa88e0946cc619). |

## onUserVideoStateChanged:streamType:hasVideo:reason:

**onUserVideoStateChanged:streamType:hasVideo:reason:**

| - (void)onUserVideoStateChanged: | (NSString *)userId |
| --- | --- |
| streamType: | ([TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15))streamType |
| hasVideo: | (BOOL)hasVideo |
| reason: | ([TUIChangeReason](https://www.tencentcloud.com/document/product/647/64477#e076e8a54a50ddfea400e7eeeb5b3132))reason |

#### Статус видеопотока пользователя изменился.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при изменении статуса видео пользователя.

| Param | DESC |
| --- | --- |
| hasVideo | Наличие видеопотока у текущего пользователя. |
| reason | Причина изменения видеопотока: [TUIChangeReasonBySelf](https://www.tencentcloud.com/document/product/647/64477#e076e8a54a50ddfea400e7eeeb5b3132): Изменено самим пользователем [TUIChangeReasonByAdmin](https://www.tencentcloud.com/document/product/647/64477#e076e8a54a50ddfea400e7eeeb5b3132): Изменено администратором. |
| streamType | Тип видеопотока. Дополнительные сведения см. в [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15). |
| userId | ID пользователя. |

## onUserAudioStateChanged:hasAudio:reason:

**onUserAudioStateChanged:hasAudio:reason:**

| - (void)onUserAudioStateChanged: | (NSString *)userId |
| --- | --- |
| hasAudio: | (BOOL)hasAudio |
| reason: | ([TUIChangeReason](https://www.tencentcloud.com/document/product/647/64477#e076e8a54a50ddfea400e7eeeb5b3132))reason |

#### Статус аудиопотока пользователя изменился.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при изменении статуса аудио пользователя.

| Param | DESC |
| --- | --- |
| hasAudio | Наличие аудиопотока у текущего пользователя. |
| reason | Причина изменения видеопотока: [TUIChangeReasonBySelf](https://www.tencentcloud.com/document/product/647/64477#e076e8a54a50ddfea400e7eeeb5b3132): Изменено самим пользователем [TUIChangeReasonByAdmin](https://www.tencentcloud.com/document/product/647/64477#e076e8a54a50ddfea400e7eeeb5b3132): Изменено администратором. |
| userId | ID пользователя. |

## onUserVoiceVolumeChanged

**onUserVoiceVolumeChanged**

#### Громкость голоса пользователя изменилась.

Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

Вызывается при изменении громкости голоса пользователя.

| Param | DESC |
| --- | --- |
| volumeMap | : Словарь громкости пользователя, ключ: userId, значение: громкость всех говорящих пользователей, диапазон значений 0

---
*Источник (EN): [tuiroomobserver.md](./tuiroomobserver.md)*
