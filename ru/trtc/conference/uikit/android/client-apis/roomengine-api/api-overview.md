# Обзор API

**ОБЗОР API**

## Обратный вызов события ошибки.

| FuncList | DESC |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/54863#2db3f881372c598e3e647f3b17915369) | Обратный вызов события ошибки. |

## Обратный вызов события статуса входа.

| FuncList | DESC |
| --- | --- |
| [onKickedOffLine](https://www.tencentcloud.com/document/product/647/54863#5dfa1251a6787bde3f2f1d1a4b1bab88) | Текущий пользователь был отключен. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/54863#4309a1386c7b4635777bb8520b0c44fc) | Подпись текущего пользователя истекла. |

## Обратный вызов события в комнате.

| FuncList | DESC |
| --- | --- |
| [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54863#97fc563cec36fcde1bb0bc1b212b5c4e) | Имя комнаты изменилось. |
| [onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/54863#15f469022d454f95f53372a83157fbbc) | Статус отключения открытия микрофона изменился для всех пользователей. |
| [onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/54863#6bc81e3152578d22f10f45780fa7cb77) | Статус отключения открытия камеры изменился для всех пользователей. |
| [onScreenShareForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54863#d6f2fb6b5936b7313bf9e36aa75aef9d) | Статус отключения открытия общего доступа к экрану изменился для всех пользователей. |
| [onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54863#8d2f050ec369f72915aa26991c04399b) | Статус отключения отправки сообщений изменился для всех пользователей. |
| [onRoomDismissed](https://www.tencentcloud.com/document/product/647/54863#087189eff55afc545eaa7fc58eaa2622) | Комната была закрыта. |
| [onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/54863#216fe07cfda9d5b3736e368c0eef69c2) | Текущий пользователь был отключен от комнаты. |
| [onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/54863#dd614e13a79128f06065469914b9a797) | Режим мест в комнате изменился. |
| [onRoomUserCountChanged](https://www.tencentcloud.com/document/product/647/54863#b1ce0f40db4b25f53d14ca03d2902846) | Количество пользователей в комнате изменилось. |
| [onRoomMetadataChanged](https://www.tencentcloud.com/document/product/647/54863#bcc8d33dab3ea6791703f3755bd5986b) | Метаданные комнаты (ключ-значение) изменились. |

## Обратный вызов события пользователя в комнате.

| FuncList | DESC |
| --- | --- |
| [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54863#823d44ecd328c1436a8d7e324c5654b1) | Удаленный пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54863#464debb75790e0f51f4d1690fa4e4450) | Удаленный пользователь вышел из комнаты. |
| [onUserInfoChanged](https://www.tencentcloud.com/document/product/647/54863#9df3bd61a4a7bfb3a508d114cbc99e7d) | Информация пользователя в комнате изменилась. |
| [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54863#1b5f1be3b9eacef43456b28a335bde63) | Статус видеопотока пользователя изменился. |
| [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54863#0d385087f48c9f2d85d650f492bacb9d) | Статус аудиопотока пользователя изменился. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54863#b0dfa9b3b96e9704c57c81f4f4e3c35a) | Громкость голоса пользователя изменилась. |
| [onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/54863#493bc419ce28818107f146e7f1563893) | Статус отключения отправки сообщений изменился для пользователя. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/54863#13f898da65ec4ad64994746ac417fbc1) | Состояние сети пользователя изменилось. |
| [onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/54863#bdd10647f4a557c8225bc897047ad3db) | Общий доступ к экрану остановлен. |
| [onUserVideoSizeChanged](https://www.tencentcloud.com/document/product/647/54863#a8f343f64a1c508ccfc9fe547e22e687) | Размер видео пользователя изменился. |

## Обратный вызов события места в комнате.

| FuncList | DESC |
| --- | --- |
| [onSeatListChanged](https://www.tencentcloud.com/document/product/647/54863#d544966ec2d49b6f777c2474c0ad0d91) | Список мест изменился. |
| [onKickedOffSeat](https://www.tencentcloud.com/document/product/647/54863#4e11a93aedd2ef4b75a7bc5f9a925032) | Пользователь был отключен с места. |

## Обратный вызов события запроса.

| FuncList | DESC |
| --- | --- |
| [onRequestReceived](https://www.tencentcloud.com/document/product/647/54863#51c9deaee5b33b0ef9f6d5223880c667) | Получено сообщение запроса. |
| [onRequestCancelled](https://www.tencentcloud.com/document/product/647/54863#635b121d6722a2a7c7a69bcf1bc4981a) | Получен отмененный запрос. |
| [onRequestProcessed](https://www.tencentcloud.com/document/product/647/54863#bee4b3bdf3bee6c00ec58801b882ceca) | Получен запрос, обработанный другим администратором/владельцем. |
| [onReceiveTextMessage](https://www.tencentcloud.com/document/product/647/54863#386f4c4ff37a699303b09b64bd051b99) | Получено текстовое сообщение |

## События сообщений в комнате

| FuncList | DESC |
| --- | --- |
| [onRequestReceived](https://www.tencentcloud.com/document/product/647/54863#51c9deaee5b33b0ef9f6d5223880c667) | Получено сообщение запроса. |
| [onReceiveTextMessage](https://www.tencentcloud.com/document/product/647/54863#386f4c4ff37a699303b09b64bd051b99) | Получено текстовое сообщение |
| [onReceiveCustomMessage](https://www.tencentcloud.com/document/product/647/54863#5abdba4e2d80e39bbc9a268e4fd07791) | Получено пользовательское сообщение |

## Создание экземпляров и обратный вызов события.

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/54864#16cf67c8716b1c79b762d19e4ab99008) | Создать экземпляр TUIRoomEngine (паттерн singleton). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/54864#56ce73cf1f0b6bf6492c81d308ec029d) | Уничтожить экземпляр TUIRoomEngine (паттерн singleton). |
| [login](https://www.tencentcloud.com/document/product/647/54864#e91313128572e17f2397f7be8edd93cf) | После создания экземпляра TUIRoomEngine вы должны войти с использованием sdkAppId, userId и userSig, чтобы вы могли вызывать экземпляр TUIRoomEngine и другие функции. |
| [logout](https://www.tencentcloud.com/document/product/647/54864#45756ace1ef6c82297eee3fac5cd8667) | Выйти из аккаунта. Если вы находитесь в комнате, будут выполнены активные операции выхода из комнаты и уничтожения ресурсов. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54864#bc3705389df676bb8e8cb68942dd820f) | Обновить имя пользователя и аватар для вошедшего пользователя. |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54864#946bae7d91f5073f8044633a79a3c227) | Вернуть базовую информацию вошедшего пользователя, включая никнейм и аватар. |
| [addObserver](https://www.tencentcloud.com/document/product/647/54864#aa9e2a751854badf8d300deef59680b9) | Установить наблюдатель события. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/54864#a66b02c83a4371533c8076e9715d13b8) | Удалить наблюдатель события. |

## API комнаты.

| FuncList | DESC |
| --- | --- |
| [createRoom](https://www.tencentcloud.com/document/product/647/54864#911bbef4c82371be741fa4c6c0693907) | Создать комнату. |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/54864#9141c0291abba473fe8daeb75e3e052c) | Закрыть комнату. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54864#35fdf16804f2627fec75cdce28ffc6cc) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/54864#380786b98d56b95daf683fa4d68af388) | Выйти из комнаты. |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/54864#592e4c141886cc8b8666cf8dfefc3a8f) | Получить информацию о комнате. |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/54864#d970bfb9100d587e0d008db312b5bc5b) | Обновить имя комнаты (только для администраторов или владельца комнаты). |
| [updateRoomSeatModeByAdmin](https://www.tencentcloud.com/document/product/647/54864#07121319d8ae42ebccb1761dcbe508a4) | Обновить режим мест в комнате (только для администраторов или владельца комнаты). |
| [updateRoomPasswordByAdmin](https://www.tencentcloud.com/document/product/647/54864#cac0a265de041de6d6e57aa57d705ad6) | Обновить пароль комнаты (только для администраторов или владельца комнаты). |
| [getRoomMetadata](https://www.tencentcloud.com/document/product/647/54864#4bf28fcd8a1146b0662779f3094a509e) | Получить метаданные комнаты. |
| [setRoomMetadataByAdmin](https://www.tencentcloud.com/document/product/647/54864#e774ac4968fa3eef64f36571ae2afe42) | Установить метаданные комнаты, если ключ уже существует, обновить его значение, если нет, добавить ключ. |

## Рендеринг локального просмотра пользователя, управление видео.

| FuncList | DESC |
| --- | --- |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/54864#98362c835e4499225b7f36ad9336d924) | Установить локальную камеру для предпросмотра представления. |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/54864#67c926e68b2bc30b9e20e0a0c4745bdf) | Открыть локальную камеру. |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/54864#ef8016748e2d62b77b933cbbc0bc70d7) | Закрыть локальную камеру. |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/54864#899becc4c8470f2036a8e53131814471) | Начать публикацию локального видеопотока, включено по умолчанию. |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/54864#672b82fcec8a33f5f4c2009321012adc) | Остановить публикацию локального видеопотока. |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/54864#ea061bff081ab6fb25c9d23efbb659b3) | Обновить качество кодирования видео. |
| [updateVideoQualityEx](https://www.tencentcloud.com/document/product/647/54864#79bd53687be4c329a1674d28be1ce907) | Установить параметры кодирования видео. |
| [setVideoResolutionMode](https://www.tencentcloud.com/document/product/647/54864#a995efd41a996d7c0b09a3efb5ff5df1) | Установить режим разрешения видео (горизонтальное или вертикальное разрешение). |
| [setLocalVideoMuteImage](https://www.tencentcloud.com/document/product/647/54864#b8375cb87e8315e878fcaf6b12c12c5b) | Установить изображение-заменитель для локального видео во время паузы. |
| [enableGravitySensor](https://www.tencentcloud.com/document/product/647/54864#69775a6d4050ab5f60bdccedf14e9182) | Включить режим датчика гравитации. (только доступно на мобильных ОС и при захвате камеры внутри SDK). |
| [startScreenSharing](https://www.tencentcloud.com/document/product/647/54864#cc949f99d6a39e2bcf4723b664fe2d74) | Начать общий доступ к экрану (только доступно на мобильных ОС). |
| [stopScreenSharing](https://www.tencentcloud.com/document/product/647/54864#9c5fa0c202a0f5b24fed30ddf9e62939) | Остановить общий доступ к экрану. |

## Управление локальным аудио пользователя.

| FuncList | DESC |
| --- | --- |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/54864#0e9b0f5598d305831ddb19ece07f1b91) | Открыть локальный микрофон. |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/54864#f677ac0fc0aa1efcd27121054699bfdc) | Закрыть локальный микрофон. |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/54864#778e31acbb656244cffdb4450ba0c156) | Обновить качество кодирования аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/54864#80693da4a3b18e07d92a802485f6334e) | Приостановить публикацию локального аудиопотока. |
| [unmuteLocalAudio](https://www.tencentcloud.com/document/product/647/54864#2a622d95aa2f7305de666cbec7109d77) | Возобновить публикацию локального аудиопотока. |
| [enableSystemAudioSharing](https://www.tencentcloud.com/document/product/647/54864#da0b9688d75cd77f51984e71566fab47) | Включить общий доступ к системному аудио |

## Рендеринг удаленного просмотра пользователя и управление видео.

| FuncList | DESC |
| --- | --- |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/54864#0e6f5fe07c0f268923e502a3a2be76c1) | Установить представление рендеринга для удаленного пользователя. |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54864#72d1726923e949d2c443dd96aa4deeca) | Начать воспроизведение видеопотока удаленного пользователя. |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54864#4d251840dd060f6ee45f3d41ad7a6c84) | Остановить воспроизведение видеопотока удаленного пользователя. |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/54864#2184de7077cf5dc9f3165329efbf43b5) | Отключить звук аудиопотока удаленного пользователя. |

## Информация о пользователе в комнате.

| FuncList | DESC |
| --- | --- |
| [getUserList](https://www.tencentcloud.com/document/product/647/54864#699fe77c2784c5d75f05078d5add27fb) | Получить список пользователей в комнате. |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/54864#6cd5c36b39754b71ad5cce7bfd2ff4b4) | Получить информацию о пользователе. |

## Управление пользователями в комнате.

| FuncList | DESC |
| --- | --- |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/54864#f0cf468f4a2fa73a73f82e60329ae649) | Изменить роль пользователя (только для администраторов или владельца комнаты). |
| [changeUserNameCard](https://www.tencentcloud.com/document/product/647/54864#33b8996e2230421dfb1a9c3bc00ecdf7) | Изменить никнейм пользователя в комнате (только администраторы или владельцы комнаты могут изменять всех пользователей, пользователи могут изменять только себя). |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/54864#258101fd02fe373bb682f479d15fc059) | Отключить удаленного пользователя из комнаты (только для администраторов или владельца комнаты). |
| [addCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/54864#a1345a3a776cab7c63c0e073b4885481) | Добавить тег для пользователя (только для администраторов или владельца комнаты). |
| [removeCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/54864#045a6dc44d38e0d1ac8e282cd1d1676e) | Удалить тег для пользователя (только для владельца комнаты). |
| [getUserListByTag](https://www.tencentcloud.com/document/product/647/54864#c27be9df993987f57823fb7d0946722f) | Получить информацию о пользователе в комнате по тегу. |
| [setCustomInfoForUser](https://www.tencentcloud.com/document/product/647/54864#f8c95b9ae30880404583b6786a3e4789) | Установить пользовательскую информацию для пользователей комнаты. |

## Управление речью пользователя в комнате.

| FuncList | DESC |
| --- | --- |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/54864#1ecce7f3cdb7dbb6f35fbaa3cc741122) | Владелец или администратор контролируют, могут ли все пользователи открывать устройство. Например: всем пользователям запрещено открывать микрофон (только доступно в сценарии конференции). |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54864#590f32d6fe85c2fc80c339937aac9cdc) | Запросить удаленного пользователя открыть медиа-устройство (только для администраторов или владельца комнаты). |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54864#510e6569a496ebad2e04bde91326eb60) | Закрыть медиа-устройства удаленного пользователя (только для администраторов или владельца комнаты). |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/54864#4d4e5f3bc13e611768a401b4c3db962f) | Подать заявку на открытие локального медиа-устройства (доступно обычным пользователям). |

## Управление местами в комнате.

| FuncList | DESC |
| --- | --- |
| [getSeatList](https://www.tencentcloud.com/document/product/647/54864#7820648092d091e37560ce0593879fc7) | Получить список мест. |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/54864#81044cd0b188305f7227e3863c0e482f) | Заблокировать место (только для администраторов или владельца комнаты). |
| [takeSeat](https://www.tencentcloud.com/document/product/647/54864#6eee934af96d5538e066a543c637e0cd) | Занять место. |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/54864#84e97d04aa3dc31eda5d6b1bdeb4c34d) | Покинуть место. |
| [moveToSeat](https://www.tencentcloud.com/document/product/647/54864#60d07dda176d554ffd84e0cf3e373262) | Переместиться на место. |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/54864#85fcac236a372109a330eb0c5e3f0a0b) | Пригласить пользователя занять место (только для администраторов или владельца комнаты). |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/54864#f878dca93c7266e7a132485ba1a00c4d) | Отключить пользователя с места (только для администраторов или владельца комнаты). |
| [getSeatApplicationList](https://www.tencentcloud.com/document/product/647/54864#54d31a649216d220311f8fcf8f905404) | Получить список запросов пользователей, которые хотят занять место в комнате (только для администраторов или владельца комнаты). |

## Сообщение.

| FuncList | DESC |
| --- | --- |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/54864#1a14651e5e06305956f7e8dd8c29b821) | Отключить возможность удаленных пользователей отправлять сообщения (только для администраторов или владельца комнаты). |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/54864#5f4a70034d79062967c860559af11b21) | Отключить возможность всех пользователей отправлять сообщения (только для администраторов или владельца комнаты). |
| [sendTextMessage](https://www.tencentcloud.com/document/product/647/54864#b642e3d2cee3cacc9e7c6f47af571314) | Отправить текстовое сообщение |
| [sendCustomMessage](https://www.tencentcloud.com/document/product/647/54864#7d14723294200fd5aa0c3853884fc97f) | Отправить пользовательское сообщение |

## Управление запросами.

| FuncList | DESC |
| --- | --- |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/54864#3271224bcd640ef9a347492b18bed14b) | Отменить запрос. |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/54864#ca9c83c643f5bd6c26dd23ec34639660) | Ответить на запрос. |

## Расширенные возможности.

| FuncList | DESC |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54864#393689f458433968d8dcc9d91635d71b) | Получить объект экземпляра TRTC. |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/54864#356c9ac2d40d703ae8075ec6d99719b3) | Установить уровень красоты. |
| [setWhitenessLevel](https://www.tencentcloud.com/document/product/647/54864#7df1e01587684fba1d0a5766334703b3) | Установить уровень отбеливания. |
| [getExtension](https://www.tencentcloud.com/document/product/647/54864#5ad5ce957d19bef36541d4eb11a1051e) | Получить расширение. |
| [getMediaDeviceManager](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21) | Получить класс управления устройством. |
| [getLiveConnectionManager](https://www.tencentcloud.com/document/product/647/54864#fe288b50da697505b5ab87a35bed950e) | Получить класс управления живым подключением. |
| [getLiveBattleManager](https://www.tencentcloud.com/document/product/647/54864#5d671512de7e22b0507211255a9c123f) | Получить класс управления живым боем. |

## Отладка.

| FuncList | DESC |
| --- | --- |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/54864#781a86cef929d0e20b8721a3e17b3726) | Вызвать экспериментальные API. |


---
*Источник: [https://trtc.io/document/54861](https://trtc.io/document/54861)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*
