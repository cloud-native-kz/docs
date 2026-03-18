# TUIRoomObserver

**TUIRoomObserver**

| FuncList | DESC |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/54863#2db3f881372c598e3e647f3b17915369) | Обратный вызов события ошибки. |
| [onKickedOffLine](https://www.tencentcloud.com/document/product/647/54863#5dfa1251a6787bde3f2f1d1a4b1bab88) | Текущий пользователь был отключен от сети. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/54863#4309a1386c7b4635777bb8520b0c44fc) | Сигнатура текущего пользователя истекла. |
| [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54863#97fc563cec36fcde1bb0bc1b212b5c4e) | Имя комнаты было изменено. |
| [onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/54863#15f469022d454f95f53372a83157fbbc) | Статус отключения микрофона для всех пользователей изменился. |
| [onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/54863#6bc81e3152578d22f10f45780fa7cb77) | Статус отключения камеры для всех пользователей изменился. |
| [onScreenShareForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54863#d6f2fb6b5936b7313bf9e36aa75aef9d) | Статус отключения совместного использования экрана для всех пользователей изменился. |
| [onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54863#8d2f050ec369f72915aa26991c04399b) | Статус отключения отправки сообщений для всех пользователей изменился. |
| [onRoomDismissed](https://www.tencentcloud.com/document/product/647/54863#087189eff55afc545eaa7fc58eaa2622) | Комната была закрыта. |
| [onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/54863#216fe07cfda9d5b3736e368c0eef69c2) | Текущий пользователь был исключен из комнаты. |
| [onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/54863#dd614e13a79128f06065469914b9a797) | Режим рассадки в комнате изменился. |
| [onRoomUserCountChanged](https://www.tencentcloud.com/document/product/647/54863#b1ce0f40db4b25f53d14ca03d2902846) | Количество пользователей в комнате изменилось. |
| [onRoomMetadataChanged](https://www.tencentcloud.com/document/product/647/54863#bcc8d33dab3ea6791703f3755bd5986b) | Ключ-значение метаданных комнаты изменилось. |
| [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54863#823d44ecd328c1436a8d7e324c5654b1) | Удаленный пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54863#464debb75790e0f51f4d1690fa4e4450) | Удаленный пользователь покинул комнату. |
| [onUserInfoChanged](https://www.tencentcloud.com/document/product/647/54863#9df3bd61a4a7bfb3a508d114cbc99e7d) | Информация пользователя в комнате изменилась. |
| [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54863#1b5f1be3b9eacef43456b28a335bde63) | Статус видеопотока пользователя изменился. |
| [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54863#0d385087f48c9f2d85d650f492bacb9d) | Статус аудиопотока пользователя изменился. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54863#b0dfa9b3b96e9704c57c81f4f4e3c35a) | Громкость голоса пользователя изменилась. |
| [onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/54863#493bc419ce28818107f146e7f1563893) | Статус отключения отправки сообщений для пользователя изменился. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/54863#13f898da65ec4ad64994746ac417fbc1) | Статус сети пользователя изменился. |
| [onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/54863#bdd10647f4a557c8225bc897047ad3db) | Совместное использование экрана было остановлено. |
| [onUserVideoSizeChanged](https://www.tencentcloud.com/document/product/647/54863#a8f343f64a1c508ccfc9fe547e22e687) | Размер видео пользователя изменился. |
| [onSeatListChanged](https://www.tencentcloud.com/document/product/647/54863#d544966ec2d49b6f777c2474c0ad0d91) | Список мест изменился. |
| [onKickedOffSeat](https://www.tencentcloud.com/document/product/647/54863#4e11a93aedd2ef4b75a7bc5f9a925032) | Пользователь был выведен с места. |
| [onRequestReceived](https://www.tencentcloud.com/document/product/647/54863#51c9deaee5b33b0ef9f6d5223880c667) | Получено сообщение запроса. |
| [onRequestCancelled](https://www.tencentcloud.com/document/product/647/54863#635b121d6722a2a7c7a69bcf1bc4981a) | Получен отмененный запрос. |
| [onRequestProcessed](https://www.tencentcloud.com/document/product/647/54863#bee4b3bdf3bee6c00ec58801b882ceca) | Получен запрос на обработку другим администратором/владельцем. |
| [onReceiveTextMessage](https://www.tencentcloud.com/document/product/647/54863#386f4c4ff37a699303b09b64bd051b99) | Текстовое сообщение получено |
| [onReceiveCustomMessage](https://www.tencentcloud.com/document/product/647/54863#5abdba4e2d80e39bbc9a268e4fd07791) | Пользовательское сообщение получено |

## onError

**onError**

| void onError | (TUICommonDefine.[Error](https://www.tencentcloud.com/document/product/647/54863#2db3f881372c598e3e647f3b17915369) errorCode |
| --- | --- |
|  | String message) |

#### Обратный вызов события ошибки.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Обратный вызов событий ошибок при входе в комнату или открытии устройства.

| Param | DESC |
| --- | --- |
| errorCode | Код ошибки. Подробнее см. [Error](https://www.tencentcloud.com/document/product/647/54863#2db3f881372c598e3e647f3b17915369). |
| message | Сообщение об ошибке. |

## onKickedOffLine

**onKickedOffLine**

| void onKickedOffLine | (String message) |
| --- | --- |

#### Текущий пользователь был отключен от сети.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается, когда пользователь отключен от сети.

| Param | DESC |
| --- | --- |
| message | Описание отключения. |

## onUserSigExpired

**onUserSigExpired**

#### Сигнатура текущего пользователя истекла.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается, когда сигнатура пользователя истекает.

## onRoomNameChanged

**onRoomNameChanged**

| void onRoomNameChanged | (String roomId |
| --- | --- |
|  | String roomName) |

#### Имя комнаты было изменено.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается при изменении имени комнаты.

| Param | DESC |
| --- | --- |
| roomId | Идентификатор комнаты. |
| roomName | Имя комнаты. |

## onAllUserMicrophoneDisableChanged

**onAllUserMicrophoneDisableChanged**

| void onAllUserMicrophoneDisableChanged | (String roomId |
| --- | --- |
|  | boolean isDisable) |

#### Статус отключения микрофона для всех пользователей изменился.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить микрофон для пользователей false: разрешить открывать микрофон пользователям. |
| roomId | Идентификатор комнаты. |

> **Note**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)..Вызывается при изменении статуса отключения микрофона для всех пользователей.

## onAllUserCameraDisableChanged

**onAllUserCameraDisableChanged**

| void onAllUserCameraDisableChanged | (String roomId |
| --- | --- |
|  | boolean isDisable) |

#### Статус отключения камеры для всех пользователей изменился.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить камеру для пользователей false: разрешить открывать камеру пользователям. |
| roomId | Идентификатор комнаты. |

> **Note**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)..Вызывается при изменении статуса отключения камеры для всех пользователей.

## onScreenShareForAllUserDisableChanged

**onScreenShareForAllUserDisableChanged**

| void onScreenShareForAllUserDisableChanged | (String roomId |
| --- | --- |
|  | boolean isDisable) |

#### Статус отключения совместного использования экрана для всех пользователей изменился.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить совместное использование экрана для пользователей false: разрешить совместное использование экрана пользователями. |
| roomId | Идентификатор комнаты. |

> **Note**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)..Вызывается при изменении прав совместного использования экрана для всех пользователей.

## onSendMessageForAllUserDisableChanged

**onSendMessageForAllUserDisableChanged**

| void onSendMessageForAllUserDisableChanged | (String roomId |
| --- | --- |
|  | boolean isDisable) |

#### Статус отключения отправки сообщений для всех пользователей изменился.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить отправку сообщений для пользователей false: разрешить отправку сообщений пользователями. |
| roomId | Идентификатор комнаты. |

> **Note**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)..Вызывается при изменении прав отправки сообщений для всех пользователей.

## onRoomDismissed

**onRoomDismissed**

| void onRoomDismissed | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[RoomDismissedReason](https://www.tencentcloud.com/document/product/647/64481#5f24e5d31bd068c0cfb09a71f1a3dd1b) reason) |

#### Комната была закрыта.

| Param | DESC |
| --- | --- |
| reason | Причина закрытия комнаты. Подробнее см. [RoomDismissedReason](https://www.tencentcloud.com/document/product/647/64481#5f24e5d31bd068c0cfb09a71f1a3dd1b). |
| roomId | Идентификатор комнаты. |

> **Note**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)..Вызывается при закрытии комнаты.

## onKickedOutOfRoom

**onKickedOutOfRoom**

| void onKickedOutOfRoom | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[KickedOutOfRoomReason](https://www.tencentcloud.com/document/product/647/64481#0146a10db3e3c88e5e3a3649ef4b8269) reason |
|  | String message) |

#### Текущий пользователь был исключен из комнаты.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается, когда пользователь исключен из комнаты.

| Param | DESC |
| --- | --- |
| message | Описание исключения. |
| reason | Причина исключения. |
| roomId | Идентификатор комнаты. |

## onRoomSeatModeChanged

**onRoomSeatModeChanged**

| void onRoomSeatModeChanged | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[SeatMode](https://www.tencentcloud.com/document/product/647/54863#dd614e13a79128f06065469914b9a797) seatMode) |

#### Режим рассадки в комнате изменился.

| Param | DESC |
| --- | --- |
| roomId | : Идентификатор комнаты. |
| seatMode | : Режим рассадки. Подробнее см. [TUISeatMode](https://www.tencentcloud.com/document/product/647/64481#908781531506c53abbfa1db07153d7c1).#### [REMARK]Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).Вызывается при изменении режима рассадки комнаты. |

## onRoomUserCountChanged

**onRoomUserCountChanged**

| void onRoomUserCountChanged | (String roomId |
| --- | --- |
|  | int userCount) |

#### Количество пользователей в комнате изменилось.

| Param | DESC |
| --- | --- |
| roomId | Идентификатор комнаты. |
| userCount | Количество пользователей.#### [REMARK]Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).Вызывается при изменении количества пользователей в комнате. |

## onRoomMetadataChanged

**onRoomMetadataChanged**

| void onRoomMetadataChanged | (String key |
| --- | --- |
|  | String value) |

#### Ключ-значение метаданных комнаты изменилось.

| Param | DESC |
| --- | --- |
| key | Ключ метаданных комнаты. |
| value | Значение метаданных комнаты.#### [REMARK]Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).Вызывается при изменении пользовательской информации комнаты. |

## onRemoteUserEnterRoom

**onRemoteUserEnterRoom**

| void onRemoteUserEnterRoom | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[UserInfo](https://www.tencentcloud.com/document/product/647/54863#9df3bd61a4a7bfb3a508d114cbc99e7d) userInfo) |

#### Удаленный пользователь вошел в комнату.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается, когда удаленный пользователь входит в комнату.

| Param | DESC |
| --- | --- |
| roomId | Идентификатор комнаты. |
| userInfo | Информация о пользователе. Подробнее см. [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64481#bc8ea9058aacb64d01afa686523dbdaa). |

## onRemoteUserLeaveRoom

**onRemoteUserLeaveRoom**

| void onRemoteUserLeaveRoom | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[UserInfo](https://www.tencentcloud.com/document/product/647/54863#9df3bd61a4a7bfb3a508d114cbc99e7d) userInfo) |

#### Удаленный пользователь покинул комнату.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается, когда удаленный пользователь покидает комнату.

| Param | DESC |
| --- | --- |
| roomId | Идентификатор комнаты. |
| userInfo | Информация о пользователе. Подробнее см. [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64481#bc8ea9058aacb64d01afa686523dbdaa). |

## onUserInfoChanged

**onUserInfoChanged**

| void onUserInfoChanged | (TUIRoomDefine.[UserInfo](https://www.tencentcloud.com/document/product/647/54863#9df3bd61a4a7bfb3a508d114cbc99e7d) userInfo |
| --- | --- |
|  | List<TUIRoomDefine.[UserInfoModifyFlag](https://www.tencentcloud.com/document/product/647/64481#25ce7d8fe7ae9d0fb7baecd643a3da03)> modifyFlag) |

#### Информация пользователя в комнате изменилась.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается при изменении информации пользователя.

| Param | DESC |
| --- | --- |
| modifyFlag | Модифицируемый параметр. Подробнее см. [UserInfoModifyFlag](https://www.tencentcloud.com/document/product/647/64481#25ce7d8fe7ae9d0fb7baecd643a3da03). |
| userInfo | Информация о пользователе. Подробнее см. [TUIUserInfo](https://www.tencentcloud.com/document/product/647/64481#bc8ea9058aacb64d01afa686523dbdaa). |

## onUserVideoStateChanged

**onUserVideoStateChanged**

| void onUserVideoStateChanged | (String userId |
| --- | --- |
|  | TUIRoomDefine.[VideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0) streamType |
|  | boolean hasVideo |
|  | TUIRoomDefine.[ChangeReason](https://www.tencentcloud.com/document/product/647/64481#4cc7da84ae9c0e2e9a207631c66d29c2) reason) |

#### Статус видеопотока пользователя изменился.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается при изменении статуса видео пользователя.

| Param | DESC |
| --- | --- |
| hasVideo | Наличие видеопотока у текущего пользователя. |
| reason | Причина изменения видеопотока: [BY_SELF](https://www.tencentcloud.com/document/product/647/64481#4cc7da84ae9c0e2e9a207631c66d29c2): Изменено самим пользователем [BY_ADMIN](https://www.tencentcloud.com/document/product/647/64481#4cc7da84ae9c0e2e9a207631c66d29c2): Изменено администратором. |
| streamType | Тип видеопотока. Подробнее см. [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0). |
| userId | Идентификатор пользователя. |

## onUserAudioStateChanged

**onUserAudioStateChanged**

| void onUserAudioStateChanged | (String userId |
| --- | --- |
|  | boolean hasAudio |
|  | TUIRoomDefine.[ChangeReason](https://www.tencentcloud.com/document/product/647/64481#4cc7da84ae9c0e2e9a207631c66d29c2) reason) |

#### Статус аудиопотока пользователя изменился.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается при изменении статуса аудио пользователя.

| Param | DESC |
| --- | --- |
| hasAudio | Наличие аудиопотока у текущего пользователя. |
| reason | Причина изменения видеопотока: [BY_SELF](https://www.tencentcloud.com/document/product/647/64481#4cc7da84ae9c0e2e9a207631c66d29c2): Изменено самим пользователем [BY_ADMIN](https://www.tencentcloud.com/document/product/647/64481#4cc7da84ae9c0e2e9a207631c66d29c2): Изменено администратором. |
| userId | Идентификатор пользователя. |

## onUserVoiceVolumeChanged

**onUserVoiceVolumeChanged**

| void onUserVoiceVolumeChanged | (Map<String, Integer> volumeMap) |
| --- | --- |

#### Громкость голоса пользователя изменилась.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается при изменении громкости голоса пользователя.

| Param | DESC |
| --- | --- |
| volumeMap | : Словарь громкостей пользователей ключ: userId, значение: громкость всех говорящих пользователей, диапазон значений 0 - 100. |

## onSendMessageForUserDisableChanged

**onSendMessageForUserDisableChanged**

| void onSendMessageForUserDisableChanged | (String roomId |
| --- | --- |
|  | String userId |
|  | boolean isDisable) |

#### Статус отключения отправки сообщений для пользователя изменился.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

Вызывается при изменении прав отправки сообщений пользователем.

| Param | DESC |
| --- | --- |
| isDisable | true: отключить отправку сообщений для пользователя false: разрешить отправку сообщений пользователю. |
| userId | Идентификатор пользователя. |

## onUserNetworkQualityChanged

**onUserNetworkQualityChanged**

| void onUserNetworkQualityChanged | (Map<String, TUICommonDefine.[NetworkInfo](https://www.tencentcloud.com/document/product/647/64480#f05ccf0cb4317161e0b13fc79fcf0ceb)> networkMap) |
| --- | --- |

#### Статус сети пользователя изменился.

Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/

---
*Источник (EN): [tuiroomobserver.md](./tuiroomobserver.md)*
