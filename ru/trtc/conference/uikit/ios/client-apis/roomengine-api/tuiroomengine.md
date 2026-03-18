# TUIRoomEngine

Авторское право (c) 2024 Tencent. Все права защищены.

Модуль:   TUIRoomEngine @ TUIKitEngine.

Функция: Основные API-функции TUIRoomEngine.

Версия: 3.2

**TUIRoomEngine**

## TUIRoomEngine

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/54855#7591fdc3a0ca12c99ae6e02bd406ed17) | Создать экземпляр TUIRoomEngine (паттерн singleton). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/54855#665e37566fe89fb0abeb66ef2fc3d5db) | Уничтожить экземпляр TUIRoomEngine (паттерн singleton). |
| [loginWithSDKAppId:userId:userSig:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#fb5d593fb688c5e26a700db98250e6dd) | После создания экземпляра TUIRoomEngine необходимо выполнить вход с помощью sdkAppId, userId и userSig, затем можно вызывать методы экземпляра TUIRoomEngine и другие функции. |
| [logout:onError:](https://www.tencentcloud.com/document/product/647/54855#509b68f796961e5de754932fb21aa50a) | Выход из учетной записи. Если вы находитесь в комнате, произойдут активные операции выхода из комнаты и освобождения ресурсов. |
| [setSelfInfoWithUserName:avatarUrl:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#0cf77ae0514c515dc5be4203a6d44f34) | Обновить имя пользователя и аватар для авторизованного пользователя. |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54855#55196a0862d9231f772d05263e703cb2) | Вернуть основную информацию авторизованного пользователя, включая никнейм и аватар. |
| [setSelfInfo:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#b3121cde5287dbe110376617320fad58) | Обновить основную информацию пользователя для авторизованного пользователя. |
| [addObserver:](https://www.tencentcloud.com/document/product/647/54855#b272afc5ebfd02ef90e7e8dc599a4b82) | Установить наблюдатель событий. |
| [removeObserver:](https://www.tencentcloud.com/document/product/647/54855#34e77ed104d979192e355dbb31e84fbf) | Удалить наблюдатель событий. |
| [createRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#4d0e7ddf563f6245a1d812b0690a5eea) | Создать комнату. |
| [destroyRoom:onError:](https://www.tencentcloud.com/document/product/647/54855#31650ce63622900078ee2f81c23e4454) | Закрыть комнату. |
| [enterRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#e76b632b17a47f9254f32d2f5ed96222) | Войти в комнату. |
| [enterRoom:roomType:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#c14956bfcb56cb3759b498050631331a) | Войти в комнату. |
| [enterRoom:roomType:options:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#3e5f7fdc1c30135d17bd4464609d99e4) | Войти в комнату. |
| [exitRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#cb2aa94c3b2e1d926793eb7aaab410e8) | Выйти из комнаты. |
| [fetchRoomInfo:onError:](https://www.tencentcloud.com/document/product/647/54855#f6d4167648189c5290b711062c74e8fd) | Получить информацию о комнате. |
| [fetchRoomInfo:roomType:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#26f5a1529c27553cce6c56d942c80ad0) | Получить информацию об указанной комнате. |
| [updateRoomNameByAdmin:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#bc6afcb38590615a5df7600df29367ba) | Обновить название комнаты (только для администраторов или владельца комнаты). |
| [updateRoomSeatModeByAdmin:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#d06444a359611753052ac864c5b611e9) | Обновить режим мест в комнате (только для администраторов или владельца комнаты). |
| [updateRoomPasswordByAdmin:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#8a55267d6730bb708d531581746fa966) | Обновить пароль комнаты (только для администраторов или владельца комнаты). |
| [getRoomMetadata:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#f7eb8d8350b755920accc62b1b7e4397) | Получить метаданные комнаты. |
| [setRoomMetadataByAdmin](https://www.tencentcloud.com/document/product/647/54855#fba0ca6c5bae1858bcf81734036248cc) | Установить метаданные комнаты, если ключ уже существует, обновить его значение, если нет, добавить ключ. |
| [setLocalVideoView:](https://www.tencentcloud.com/document/product/647/54855#55a67c65f1344a3339ee151b807d24ab) | Установить локальную камеру для предпросмотра в окне рендеринга. |
| [openLocalCamera:quality:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#f72c16229f46ba7b28b0d9849ac98826) | Открыть локальную камеру. |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/54855#ff4537fd911678280a013b61005345ed) | Закрыть локальную камеру. |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/54855#b178202f1acaedf7f1088ce109d3f963) | Начать публикацию локального видеопотока, включено по умолчанию. |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/54855#4500cae058442aa6cf0660899c590b9d) | Остановить публикацию локального видеопотока. |
| [updateVideoQuality:](https://www.tencentcloud.com/document/product/647/54855#486a72e802a93ad219ac70b2f987ff2d) | Обновить качество кодирования видео. |
| [updateVideoQualityEx:params:](https://www.tencentcloud.com/document/product/647/54855#bf634578e3304a18894e04560468c20f) | Установить параметры кодирования видео. |
| [setVideoResolutionMode:resolutionMode:](https://www.tencentcloud.com/document/product/647/54855#60c1bc35ad2ebbe4b19198bc16ea2865) | Установить режим разрешения видео (горизонтальное разрешение или вертикальное разрешение). |
| [setLocalVideoMuteImage:](https://www.tencentcloud.com/document/product/647/54855#0fdb2eda054cdf1d2b7c74268d16c62a) | Установить подменное изображение для локального видео при паузе. |
| [enableGravitySensor:](https://www.tencentcloud.com/document/product/647/54855#e43024d3910ad9ec7001aa44bc8275af) | Включить режим датчика гравитации. (доступно только на мобильных ОС и при захвате камеры внутри SDK). |
| [startScreenCaptureByReplaykit:](https://www.tencentcloud.com/document/product/647/54855#fe00b96dd343d6975b4350efc157d5c8) | Начать общий доступ к экрану (доступно только на мобильных ОС). |
| [startScreenCapture:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#f0c5bef34ea01c7a57f75905a116b310) | Начать общий доступ к экрану (доступно только на Mac OS). |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/54855#0fa4aee168037d922e21047913bb8382) | Остановить общий доступ к экрану. |
| [getScreenCaptureSources](https://www.tencentcloud.com/document/product/647/54855#45bab04fe4f34e65db53282904eab4db) | Получить список доступных экранов и окон для общего доступа (доступно только на Mac OS) |
| [selectScreenCaptureTarget:](https://www.tencentcloud.com/document/product/647/54855#fe760c4f87bf7d13e878f0085bdb06e9) | Выбрать экран или окна для общего доступа (доступно только на Mac OS) |
| [openLocalMicrophone:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#0d61ecfc837ff6d44e5a5c3d0faee8b3) | Открыть локальный микрофон. |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/54855#6a5f4544cf81d483a4dba368545f94b9) | Закрыть локальный микрофон. |
| [updateAudioQuality:](https://www.tencentcloud.com/document/product/647/54855#8b1839388fa8e799f0ae35c49a3f2911) | Обновить качество кодирования аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/54855#c64198c0a04341cac736e4104ebdf0bd) | Приостановить публикацию локального аудиопотока. |
| [unmuteLocalAudio:onError:](https://www.tencentcloud.com/document/product/647/54855#14f97e6ab0e879b699ab0e37b485eba4) | Возобновить публикацию локального аудиопотока. |
| [enableSystemAudioSharing:](https://www.tencentcloud.com/document/product/647/54855#25c0877abd6134e2522eafe7c4de65f9) | Включить общий доступ к системному звуку |
| [setRemoteVideoView:streamType:view:](https://www.tencentcloud.com/document/product/647/54855#e3a3d88e04a1f569e6dcb68d91cce59a) | Установить окно рендеринга для удаленного пользователя. |
| [startPlayRemoteVideo:streamType:onPlaying:onLoading:onError:](https://www.tencentcloud.com/document/product/647/54855#989232414785216d37587684becbb483) | Начать воспроизведение видеопотока удаленного пользователя. |
| [stopPlayRemoteVideo:streamType:](https://www.tencentcloud.com/document/product/647/54855#5500e4b4d12b3d56faee3eb725b00f1a) | Остановить воспроизведение видеопотока удаленного пользователя. |
| [muteRemoteAudioStream:isMute:](https://www.tencentcloud.com/document/product/647/54855#b78726b72ddf579f240da34884b2c609) | Отключить звук аудиопотока удаленного пользователя. |
| [getUserList:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#1e4f7da192b0128754ba6e9f385bed8d) | Получить список пользователей в комнате. |
| [getUserInfo:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#ec236cd0d12ab2fce2ca5621f668ab5d) | Получить информацию о пользователе. |
| [changeUserRole:role:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#17f8c2dc10f266cbc78d3b1812f95240) | Изменить роль пользователя (только для администраторов или владельца комнаты). |
| [changeUserNameCard:nameCard:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#b1ea3d2360a2c0889ffc5cf382fb9da2) | Изменить никнейм пользователя в комнате (только администраторы или владелец комнаты могут изменить для всех пользователей, пользователь может изменить только свой). |
| [kickRemoteUserOutOfRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#fa4bd9852c77cf5f5b7be203fe6dbb22) | Исключить удаленного пользователя из комнаты (только для администраторов или владельца комнаты). |
| [addCategoryTagForUsers:userList:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#619bec5e8dcb6619488732a8a9effaae) | Добавить метку для пользователя (только для администраторов или владельца комнаты). |
| [removeCategoryTagForUsers:userList:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#6e3ba5a485a91fc43757891c4dc99d27) | Удалить метку для пользователя (только для владельца комнаты). |
| [getUserListByTag:nextSequence:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#333966765d152e41f549157cc2ab7071) | Получить информацию о пользователях в комнате на основе метки. |
| [setCustomInfoForUser:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#56222c867961904dc8769ad714bba5fe) | Установить пользовательскую информацию для пользователей комнаты. |
| [disableDeviceForAllUserByAdmin:isDisable:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#8f96b729c8a9948c9cf7d2ebfd6ff48f) | Владелец или администратор контролирует, могут ли все пользователи открывать устройства. Например: всем пользователям запрещено открывать микрофон (доступно только в сценарии конференции). |
| [openRemoteDeviceByAdmin:device:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#5efa632932881735e551ff016402160b) | Запросить у удаленного пользователя открыть медиа-устройство (только для администраторов или владельца комнаты). |
| [closeRemoteDeviceByAdmin:device:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#780489248cb022a5495812a6eb072317) | Закрыть медиа-устройства удаленного пользователя (только для администраторов или владельца комнаты). |
| [applyToAdminToOpenLocalDevice:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#4993a64e14a999449612351df8a574c6) | Запросить разрешение на открытие локального медиа-устройства (доступно обычным пользователям). |
| [getSeatList:onError:](https://www.tencentcloud.com/document/product/647/54855#9a8217b0951913d5c24a3418cd5f452d) | Получить список мест. |
| [lockSeatByAdmin:lockMode:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#df1f081b00d3640cd6173899e788d9bf) | Заблокировать место (только для администраторов или владельца комнаты). |
| [takeSeat:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#b7dec60a76be6d9a9b63093319301943) | Занять место. |
| [leaveSeat:onError:](https://www.tencentcloud.com/document/product/647/54855#f301d65082c9fe6e54df6f74522df36d) | Покинуть место. |
| [moveToSeat:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#17c6072ee712ee80751eb30a5815ff1b) | Переместиться на место. |
| [takeUserOnSeatByAdmin:userId:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#060623f0395a1416baf48ebd80c598f1) | Пригласить пользователя занять место (только для администраторов или владельца комнаты). |
| [kickUserOffSeatByAdmin:userId:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#4fc6a6c9e386a7a0d9dda3a6a0aade6f) | Исключить пользователя со своего места (только для администраторов или владельца комнаты). |
| [getSeatApplicationList:onError:](https://www.tencentcloud.com/document/product/647/54855#318ba4689ead5ec4214664f23c92a6e3) | Получить список заявок от пользователей, которые хотят занять место в комнате (только для администраторов или владельца комнаты). |
| [disableSendingMessageByAdmin:isDisable:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#99f76e01022ed98bcb8759320810d85b) | Отключить возможность удаленных пользователей отправлять сообщения (только для администраторов или владельца комнаты). |
| [disableSendingMessageForAllUser:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#88f96a71fd0ee8c59ab3cdecd0930551) | Отключить возможность всех пользователей отправлять сообщения (только для администраторов или владельца комнаты). |
| [sendTextMessage:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#2211c4227dfecaf8a1a0448d943599d2) | Отправить текстовое сообщение |
| [sendCustomMessage:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#a6092b6681c81429033efd93161b415e) | Отправить пользовательское сообщение |
| [cancelRequest:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#17ba27cad02e54757cdd41e442ddfbbc) | Отменить запрос. |
| [responseRemoteRequest:agree:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#10789c19d23dec9a25d6c8bfab407f23) | Ответить на запрос. |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54855#d3c48e3c9d0f371386ca7b0589ef4c88) | Получить объект экземпляра TRTC. |
| [setBeautyLevel:beautyLevel:](https://www.tencentcloud.com/document/product/647/54855#4c6d4893dba79b7e4a41a001eaea1534) | Установить уровень красоты. |
| [setWhitenessLevel:](https://www.tencentcloud.com/document/product/647/54855#ba29ed099d81a69fc300a82caebb8fde) | Установить уровень отбеливания. |
| [getExtension:](https://www.tencentcloud.com/document/product/647/54855#b99da8d3a9d62547dd23c56e0b4436c0) | Получить расширение. |
| [getMediaDeviceManager](https://www.tencentcloud.com/document/product/647/54855#c6483c3f80f639d0eb3fd076f02872d6) | Получить класс управления устройствами. |
| [getLiveConnectionManager](https://www.tencentcloud.com/document/product/647/54855#fdb1665975863e593233d97715af0dc5) | Получить класс управления live-соединением. |
| [getLiveBattleManager](https://www.tencentcloud.com/document/product/647/54855#0a32a3590a6ae1e2776d80e5eb3040e1) | Получить класс управления live-баттлом. |
| [callExperimentalAPI:callback:](https://www.tencentcloud.com/document/product/647/54855#91021955c4aadb7dfcbff8f0376f0106) | Вызвать экспериментальные API. |

## sharedInstance

**sharedInstance**

#### Создать экземпляр TUIRoomEngine (паттерн singleton).

Описание:

- Создает и возвращает глобальный общий экземпляр TUIRoomEngine (паттерн singleton).
- Поддерживает типы комнат конференции и прямой трансляции ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) & [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).
- Использование паттерна singleton избегает создания дублирующихся экземпляров движка и экономит ресурсы.

Возвращаемое значение:

- Возвращает указатель на экземпляр singleton TUIRoomEngine.

```
// Пример использования в Objective-C:TUIRoomEngine *engine = [TUIRoomEngine sharedInstance];// Пример использования в Swift:let engine = TUIRoomEngine.sharedInstance()
```

> **Примечание** Многократные вызовы вернут один и тот же экземпляр.

## destroySharedInstance

**destroySharedInstance**

#### Уничтожить экземпляр TUIRoomEngine (паттерн singleton).

Описание:

- Чтобы избежать неизвестных исключений после уничтожения экземпляра singleton, не рекомендуется вызывать этот интерфейс во время выполнения программы.
- Уничтожает глобальный общий экземпляр TUIRoomEngine.
- Освобождает все ресурсы, занятые движком.
- Необходимо заново получить sharedInstance при использовании после вызова этого метода.

```
// Пример использования в Objective-C:[TUIRoomEngine destroySharedInstance];// Пример использования в Swift:TUIRoomEngine.destroySharedInstance()
```

> **Примечание** Убедитесь, что все комнаты закрыты перед вызовом этого метода. Все функциональности движка будут недоступны после вызова этого метода. Применимо к типам комнат конференции и прямой трансляции ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) & [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).

## loginWithSDKAppId:userId:userSig:onSuccess:onError:

**loginWithSDKAppId:userId:userSig:onSuccess:onError:**

| + (void)loginWithSDKAppId: | (NSInteger)sdkAppId |
| --- | --- |
| userId: | (NSString *)userId |
| userSig: | (NSString *)userSig |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### После создания экземпляра TUIRoomEngine необходимо выполнить вход с помощью sdkAppId, userId и userSig, затем можно вызывать методы экземпляра TUIRoomEngine и другие функции.

Описание:

- Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).
- Если пользователь исключен в режиме онлайн, SDK уведомит вас через обратный вызов [onKickedOffLine](https://www.tencentcloud.com/document/product/647/54854#b0238d7b1fa86af2c540ec313dba8e6b) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

```
// Пример использования в Objective-C:[TUIRoomEngine loginWithSDKAppId:1400000001                           userId:@"user123"                          userSig:@"xxxxxx"                        onSuccess:^{                           // Обработка успешного входа                        }                          onError:^(int code, NSString *message) {                           // Обработка ошибки входа                       }];// Пример использования в Swift:TUIRoomEngine.login(sdkAppId: 1400000001,                      userId: "user123",                     userSig: "xxxxxx",                   onSuccess: {                          // Обработка успешного входа                    },                     onError: { code, message in                          // Обработка ошибки входа                  })
```

Параметры:

| Param | DESC |
| --- | --- |
| sdkAppId | Идентификатор приложения. Вы можете просмотреть SDKAppId, создав приложение в консоли TRTC [Console](https://console.trtc.io/). |
| userId | ID пользователя, уникальный идентификатор, используемый Tencent Cloud для различения пользователей. |
| userSig | Подпись пользователя, разработанная Tencent Cloud на основе UserId, используется для доступа к услугам Tencent Cloud. Более подробно см. [UserSig](https://trtc.io/document/35166). |

> **Примечание** Необходимо вызвать этот интерфейс для успешного входа перед выполнением других операций. UserId под одним SDKAppId должен быть уникальным. userSig должен быть создан вашим сервером приложений.

## logout:onError:

**logout:onError:**

| + (void)logout: | (TUISuccessBlock)onSuccess |
| --- | --- |
| onError: | (TUIErrorBlock)onError |

#### Выход из учетной записи. Если вы находитесь в комнате, произойдут активные операции выхода из комнаты и освобождения ресурсов.

Описание:

- Активно выполняет выход из текущего статуса входа.
- Освобождает все ресурсы, занятые движком.
- Автоматически выполняет операцию выхода из комнаты

## destroyRoom:onError:

**destroyRoom:onError:**

| - (void)destroyRoom: | (TUISuccessBlock)onSuccess |
| --- | --- |
| onError: | (TUIErrorBlock)onError |

#### Закрыть комнату.

Описание:

- Закрывает текущую комнату, в которой находится пользователь.
- Все участники будут принудительно удалены после закрытия комнаты.
- Поддерживает оба типа комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] destroyRoom:^{    NSLog(@"Room dismissed successfully");} onError:^(TUIError code, NSString * _Nonnull message) {    NSLog(@"Failed to dismiss room: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().destroyRoom {    print("Room dismissed successfully")} onError: { code, message in    print("Failed to dismiss room: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, обратный вызов при ошибке содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов при успехе. |

> **Примечание** Только владелец комнаты может вызвать этот интерфейс. После закрытия комнаты SDK уведомит пользователей в комнате через обратный вызов [onRoomDismissed](https://www.tencentcloud.com/document/product/647/54854#e3741060867444c54121e60eb54f989c) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa). Убедитесь, что все операции в комнате завершены перед вызовом этого интерфейса. Закрытую комнату восстановить нельзя, для продолжения работы необходимо создать новую комнату.

## enterRoom:onSuccess:onError:

**enterRoom:onSuccess:onError:**

| - (void)enterRoom: | (NSString *)roomId |
| --- | --- |
| onSuccess: | (TUIRoomInfoBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Войти в комнату.

Описание:

- Этот интерфейс будет устаревшим в будущих версиях и не рекомендуется для использования.
- Для входа в комнаты рекомендуется использовать один из следующих методов:

` 2.4 enterRoom(String roomId, TUIRoomDefine.RoomType roomType ` или ` 2.5 enterRoom(String roomId, TUIRoomDefine.RoomType roomType, TUIRoomDefine.EnterRoomOptions ` интерфейс.

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] enterRoom:@"roomId123" onSuccess:^(TUIRoomInfo * _Nullable roomInfo) {    NSLog(@"Enter room successfully");} onError:^(TUIError code, NSString * _Nonnull message) {    NSLog(@"Failed to enter room: %@", message);}];// Swift ExampleTUIRoomEngine.sharedInstance().enterRoom("roomId123") { roomInfo in  print("Enter room successfully")} onError: { code, message in  print("Failed to enter room: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, обратный вызов при ошибке содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов при успехе. |
| roomId | ID комнаты. |

> **Примечание** Одно устройство может одновременно находиться в 1 комнате. При превышении лимита самая старая комната будет закрыта автоматически. Если один и тот же аккаунт авторизован на нескольких устройствах, только 1 устройство может находиться в конференц-комнате с одним и тем же ID. Другие устройства, пытающиеся войти, вытеснят ранее подключённое устройство. После входа в комнату SDK уведомит пользователей в комнате через обратный вызов [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54854#64bc4ce1b62e5a15de963ecfb9225e98) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## enterRoom:roomType:onSuccess:onError:

**enterRoom:roomType:onSuccess:onError:**

| - (void)enterRoom: | (NSString *)roomId |
| --- | --- |
| roomType: | ([TUIRoomType](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248))roomType |
| onSuccess: | (TUIRoomInfoBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Войти в комнату.

Описание:

- Входит в указанную комнату, поддерживает два типа комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] enterRoom:@"roomId123"                                 roomType:TUIRoomTypeConference                                onSuccess:^(TUIRoomInfo * _Nullable roomInfo) {    NSLog(@"Enter room successfully");} onError:^(TUIError code, NSString * _Nonnull message) {    NSLog(@"Failed to enter room: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().enterRoom("roomId123", roomType: .conference) { roomInfo in    print("Enter room successfully")} onError: { code, message in    print("Failed to enter room: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, обратный вызов при ошибке содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов при успехе. |
| roomId | ID комнаты, должен быть уникальным. |
| roomType | Тип комнаты (конференция/трансляция). |

> **Примечание** Одно устройство может одновременно находиться в 1 конференц-комнате или 3 комнатах трансляции. При превышении лимита самая старая комната будет закрыта автоматически. Если один и тот же аккаунт авторизован на нескольких устройствах, только 1 устройство может находиться в конференц-комнате с одним и тем же ID. Другие устройства, пытающиеся войти, вытеснят ранее подключённое устройство. После входа в комнату SDK уведомит пользователей в комнате через обратный вызов [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54854#64bc4ce1b62e5a15de963ecfb9225e98) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## enterRoom:roomType:options:onSuccess:onError:

**enterRoom:roomType:options:onSuccess:onError:**

| - (void)enterRoom: | (NSString *)roomId |
| --- | --- |
| roomType: | ([TUIRoomType](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248))roomType |
| options: | ([TUIEnterRoomOptions](https://www.tencentcloud.com/document/product/647/64477#16f3cb3850bd70aecb0bd6f007955a13) *)options |
| onSuccess: | (TUIRoomInfoBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Войти в комнату.

Описание:

- Входит в указанную комнату, поддерживает два типа комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).
- Поддерживает передачу дополнительных параметров входа в комнату через options, таких как пароль комнаты и т.д.

```
// Objective-C Usage example:TUIEnterRoomOptions *options = [[TUIEnterRoomOptions alloc] init];options.password = @"***";[[TUIRoomEngine sharedInstance] enterRoom:@"roomId123"                                 roomType:TUIRoomTypeConference                                  options:options                                onSuccess:^(TUIRoomInfo * _Nullable roomInfo) {    NSLog(@"Enter room successfully");} onError:^(TUIError code, NSString * _Nonnull message) {    NSLog(@"Failed to enter room: %@", message);}];// Swift Usage example:let options = TUIEnterRoomOptions()options.password = "***"TUIRoomEngine.sharedInstance().enterRoom("roomId123",                                         roomType: .conference,                                          options: options) { roomInfo in    print("Enter room successfully")} onError: { code, message in    print("Failed to enter room: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, обратный вызов при ошибке содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов при успехе. |
| options | Параметры входа в комнату, тип ([TUIEnterRoomOptions](https://www.tencentcloud.com/document/product/647/64477#16f3cb3850bd70aecb0bd6f007955a13)). |
| roomId | ID комнаты. |
| roomType | Тип комнаты. |

> **Примечание** Одно устройство может одновременно находиться в 1 конференц-комнате или 3 комнатах трансляции. При превышении лимита самая старая комната будет закрыта автоматически. Если один и тот же аккаунт авторизован на нескольких устройствах, только 1 устройство может находиться в конференц-комнате с одним и тем же ID. Другие устройства, пытающиеся войти, вытеснят ранее подключённое устройство. После входа в комнату SDK уведомит пользователей в комнате через обратный вызов [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54854#64bc4ce1b62e5a15de963ecfb9225e98) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## exitRoom:onSuccess:onError:

**exitRoom:onSuccess:onError:**

| - (void)exitRoom: | (BOOL)syncWaiting |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Выйти из комнаты.

Описание:

- Выходит из текущей комнаты.
- Этот метод поддерживает оба типа комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).
- Все потоки аудио/видео автоматически остановят трансляцию после выхода из комнаты.

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] exitRoom:YES onSuccess:^{    NSLog(@"Exit room successfully");} onError:^(TUIError code, NSString * _Nonnull message) {    NSLog(@"Failed to exit room: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().exitRoom(syncWaiting: true) {  print("Exit room successfully")} onError: { code, message in  print("Failed to exit room: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, обратный вызов при ошибке содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов при успехе. |
| syncWaiting | Ждать ли синхронно возврата интерфейса. |

> **Примечание** После выхода из комнаты SDK уведомит пользователей в комнате через обратный вызов [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54854#16b0d80475c0d1f945024d5116074c66) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## fetchRoomInfo:onError:

**fetchRoomInfo:onError:**

| - (void)fetchRoomInfo: | (TUIRoomInfoBlock)onSuccess |
| --- | --- |
| onError: | (TUIErrorBlock)onError |

#### Получить информацию о комнате.

Описание:

- Получает подробную информацию о текущей комнате, включая ID комнаты, имя комнаты, тип комнаты и т.д.
- Поддерживает оба типа комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] fetchRoomInfo:^(TUIRoomInfo * _Nullable roomInfo) {    NSLog(@"Get room info successfully: %@", roomInfo);} onError:^(TUIError code, NSString * _Nonnull message) {    NSLog(@"Failed to get room info: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().fetchRoomInfo { roomInfo in    print("Get room info successfully: \\(roomInfo)")} onError: { code, message in    print("Failed to get room info: \\(message)")}
```

Параметры:

- @param onSuccess(iOS) Обратный вызов при успешном получении информации о комнате, содержит информацию о комнате $TUIRoomInfo.
- @param onError(iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение).
- @param callback(Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, при успехе возвращает информацию о комнате $TUIRoomInfo, при ошибке возвращает код ошибки и сообщение.

> **Примечание** Должен быть вызван после входа в комнату. Возвращённая информация о комнате включает основную конфигурацию и текущее состояние. Возвращает ошибку, если пользователь в настоящий момент не находится ни в какой комнате.

## fetchRoomInfo:roomType:onSuccess:onError:

**fetchRoomInfo:roomType:onSuccess:onError:**

| - (void)fetchRoomInfo: | (NSString*)roomId |
| --- | --- |
| roomType: | ([TUIRoomType](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248))roomType |
| onSuccess: | (TUIRoomInfoBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Получить информацию об указанной комнате.

Описание:

- Получает подробную информацию об указанной комнате, включая ID комнаты, имя комнаты, тип комнаты и т.д.
- Применимо для обоих типов комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] fetchRoomInfo:@"room123"                                      roomType:TUIRoomTypeConference                                    onSuccess:^(TUIRoomInfo *roomInfo) {    NSLog(@"Room info fetched successfully: %@", roomInfo);} onError:^(TUIError code, NSString *message) {    NSLog(@"Failed to fetch room info: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().fetchRoomInfo(roomId: "room123", roomType: .conference) { roomInfo in    print("Room info fetched successfully: \\(roomInfo)")} onError: { code, message in    print("Failed to fetch room info: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, при успехе возвращает информацию о комнате $TUIRoomInfo, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке, включает код ошибки и сообщение. |
| onSuccess | (iOS) Обратный вызов при успехе, возвращает объект информации о комнате. |
| roomId | ID комнаты для запроса. |
| roomType | Тип комнаты (конференция/трансляция). |

> **Примечание** Может быть вызван перед входом в комнату для запроса основной информации о комнате. Возвращённая информация о комнате включает основную конфигурацию и текущее состояние. Возвращает ошибку ROOM_ERROR_NOT_FOUND(1001), если комната не существует.

## updateRoomNameByAdmin:onSuccess:onError:

**updateRoomNameByAdmin:onSuccess:onError:**

| - (void)updateRoomNameByAdmin: | (NSString *)roomName |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Обновить имя комнаты (только для администраторов или владельца комнаты).

Описание:

- Изменяет имя текущей комнаты, применимо для обоих типов комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).
- После обновления имени комнаты SDK уведомит всех пользователей в комнате через обратный вызов [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54854#14f6f031aedb2aef37640bd8d52b512d) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] updateRoomNameByAdmin:@"New Room" onSuccess:^{  NSLog(@"Room name updated successfully");} onError:^(TUIError code, NSString *message) {  NSLog(@"Failed to update room name: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().updateRoomNameByAdmin("New Room") {    print("Room name updated successfully")} onError: { code, message in    print("Failed to update room name: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов при успехе. |
| roomName | Новое имя комнаты. |

> **Примечание** Только администраторы или владельцы комнаты могут вызвать этот интерфейс. После успешного изменения все пользователи в комнате получат обратный вызов [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54854#14f6f031aedb2aef37640bd8d52b512d). Возвращает код ошибки, если имя комнаты содержит недопустимые символы или превышает лимит длины.

## updateRoomSeatModeByAdmin:onSuccess:onError:

**updateRoomSeatModeByAdmin:onSuccess:onError:**

| - (void)updateRoomSeatModeByAdmin: | ([TUISeatMode](https://www.tencentcloud.com/document/product/647/64477#6e6fdc219cc838c9e3c5d622ab32c8f1))seatMode |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Обновить режим размещения мест в комнате (только для администраторов или владельца комнаты).

Описание:

- Изменяет режим управления местами в комнате, поддерживает режимы свободного захвата места и захвата с одобрением.
- Применимо для обоих типов комнат: конференция и трансляция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).
- После обновления режима размещения мест SDK уведомит всех пользователей в комнате через обратный вызов [onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/54854#43c39ab0e5611de1f28bfe62e4e0077b) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] updateRoomSeatModeByAdmin:TUISeatModeApplyToTake onSuccess:^{  NSLog(@"Room seat mode updated successfully");} onError:^(TUIError code, NSString *message) {  NSLog(@"Failed to update room seat mode: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().updateRoomSeatModeByAdmin(.applyToTake) {    print("Room seat mode updated successfully")} onError: { code, message in    print("Failed to update room seat mode: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов при успехе. |
| seatMode | Режим размещения мест [TUISeatModeFreeToTake](https://www.tencentcloud.com/document/product/647/64477#6e6fdc219cc838c9e3c5d622ab32c8f1): режим свободного захвата места, зрители могут занять место без заявки. [TUISeatModeApplyToTake](https://www.tencentcloud.com/document/product/647/64477#6e6fdc219cc838c9e3c5d622ab32c8f1): режим захвата с одобрением, зрители должны получить одобрение администратора/владельца для занятия места. |

> **Примечание** Только администраторы или владельцы комнаты могут вызвать этот интерфейс. После изменения режима все пользователи в комнате получат обратный вызов [onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/54854#43c39ab0e5611de1f28bfe62e4e0077b). Режим свободного захвата места подходит для интерактивных сценариев, режим захвата с одобрением подходит для сценариев, требующих контроля выступления.

## updateRoomPasswordByAdmin:onSuccess:onError:

**updateRoomPasswordByAdmin:onSuccess:onError:**

| - (void)updateRoomPasswordByAdmin: | (NSString *)password |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Обновить пароль комнаты (только для администраторов или владельца комнаты).

Описание:

- Изменяет пароль доступа к текущей комнате, применимо только для типа комнаты конференция ([TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248)).
- После обновления пароля новые пользователи, входящие в комнату, должны будут предоставить новый пароль.

```
// Objective-C Usage example:[[TUIRoomEngine sharedInstance] updateRoomPasswordByAdmin:@"NewPassword" onSuccess:^{  NSLog(@"Room password updated successfully");} onError:^(TUIError code, NSString *message) {  NSLog(@"Failed to update room password: %@", message);}];// Swift Usage example:TUIRoomEngine.sharedInstance().updateRoomPasswordByAdmin("NewPassword") {  print("Room password updated successfully")} onError: { code, message in  print("Failed to update room password: \\(message)")}
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android) Обратный вызов интерфейса для уведомления об успехе или ошибке вызова, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов при ошибке (содержит код ошибки и

## setVideoResolutionMode:resolutionMode:

**setVideoResolutionMode:resolutionMode:**

| - (void)setVideoResolutionMode: | ([TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15))streamType |
| --- | --- |
| resolutionMode: | ([TUIResolutionMode](https://www.tencentcloud.com/document/product/647/64477#281ffe18a1c82b67e026189153cadcd3))resolutionMode |

#### Установить режим разрешения видео (горизонтальное или вертикальное разрешение).

| Параметр | Описание |
| --- | --- |
| resolutionMode | Режим разрешения. Дополнительные сведения см. в [TUIResolutionMode](https://www.tencentcloud.com/document/product/647/64477#281ffe18a1c82b67e026189153cadcd3). |
| streamType | Тип видеопотока. Дополнительные сведения см. в [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15). |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## setLocalVideoMuteImage:

**setLocalVideoMuteImage:**

| - (void)setLocalVideoMuteImage: | (nullable TUIImage *)image |
| --- | --- |

#### Установить изображение-заменитель для локального видео при паузе.

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). Установка изображения-заменителя поддерживается только для трансляции после вызова stopPushLocalVideo; не поддерживается после вызова closeLocalCamera. @param image Изображение-заменитель.

## enableGravitySensor:

**enableGravitySensor:**

| - (void)enableGravitySensor: | (BOOL)enable |
| --- | --- |

#### Включить режим определения ориентации по датчику гравитации. (доступно только на мобильных ОС и при захвате видео с камеры внутри SDK).

| Параметр | Описание |
| --- | --- |
| enable | YES: включить NO: отключить. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После включения определения ориентации по датчику гравитации, если устройство на стороне захвата поворачивается, изображения на стороне захвата и для зрителей будут отрендерены соответствующим образом, чтобы гарантировать, что изображение в поле зрения всегда ориентировано вверх.

## startScreenCaptureByReplaykit:

**startScreenCaptureByReplaykit:**

| - (void)startScreenCaptureByReplaykit: | (NSString *)appGroup |
| --- | --- |

#### Начать демонстрацию экрана (доступно только на мобильных ОС).

После начала демонстрации экрана SDK уведомляет пользователей в комнате через обратный вызов [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54854#00c4eb2525cf2b404bb784d7731d95a8) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## startScreenCapture:onSuccess:onError:

**startScreenCapture:onSuccess:onError:**

| - (void)startScreenCapture: | (TUIVideoView *)view |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Начать демонстрацию экрана (доступно только на Mac OS).

| Параметр | Описание |
| --- | --- |
| view | Представление для отрендеринга может быть установлено в значение null, что означает отсутствие локального предпросмотра экрана. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После начала демонстрации экрана SDK уведомляет пользователей в комнате через обратный вызов [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54854#00c4eb2525cf2b404bb784d7731d95a8) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa). API может захватывать содержимое экрана всей Mac OS или захватывать и совместно использовать содержимое выбранного вами окна.

## stopScreenCapture

**stopScreenCapture**

#### Остановить демонстрацию экрана.

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После завершения демонстрации экрана SDK уведомляет пользователей в комнате через обратный вызов [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54854#00c4eb2525cf2b404bb784d7731d95a8) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa) и также уведомляет вас через обратный вызов [onUserScreenCaptureStopped](https://www.tencentcloud.com/document/product/647/54854#f6bae569cb7519e87904a735c61605da).

## getScreenCaptureSources

**getScreenCaptureSources**

#### Получить список доступных экранов и окон для демонстрации (доступно только на Mac OS)

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). Пользователь может использовать API для выбора экрана и окна для демонстрации. Через API вы можете запросить идентификатор, имя и миниатюру окна, доступного для демонстрации в текущей системе.

#### Описание возвращаемого значения:

Список окон, включая экраны.

## selectScreenCaptureTarget:

**selectScreenCaptureTarget:**

| - (void)selectScreenCaptureTarget: | (NSString *)targetId |
| --- | --- |

#### Выбрать экран или окно для демонстрации (доступно только на Mac OS)

| Параметр | Описание |
| --- | --- |
| targetId | Выбранный источник для демонстрации. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После получения экрана и окна для демонстрации через getScreenCaptureSources вы можете вызвать API для выбора целевого экрана или окна. Во время демонстрации экрана вы также можете вызвать API для изменения целевого источника демонстрации.

## openLocalMicrophone:onSuccess:onError:

**openLocalMicrophone:onSuccess:onError:**

| - (void)openLocalMicrophone: | ([TUIAudioQuality](https://www.tencentcloud.com/document/product/647/64477#8a3a133f95f1c0d4e341943ffb7765b4))quality |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Открыть локальный микрофон.

| Параметр | Описание |
| --- | --- |
| quality | Качество звука. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После открытия локального микрофона в комнате SDK уведомляет пользователей в комнате через обратный вызов [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54854#57eafbcdec43b9cacef68034b3087e45) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## closeLocalMicrophone

**closeLocalMicrophone**

#### Закрыть локальный микрофон.

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После закрытия локального микрофона в комнате SDK уведомляет пользователей в комнате через обратный вызов [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54854#57eafbcdec43b9cacef68034b3087e45) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## updateAudioQuality:

**updateAudioQuality:**

| - (void)updateAudioQuality: | ([TUIAudioQuality](https://www.tencentcloud.com/document/product/647/64477#8a3a133f95f1c0d4e341943ffb7765b4))quality |
| --- | --- |

#### Обновить качество кодирования звука.

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## muteLocalAudio

**muteLocalAudio**

#### Приостановить трансляцию локального аудиопотока.

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). Если вы открыли микрофон и вызовите API для приостановки трансляции локального аудиопотока, SDK уведомит пользователей в комнате через обратный вызов [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54854#57eafbcdec43b9cacef68034b3087e45) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## unmuteLocalAudio:onError:

**unmuteLocalAudio:onError:**

| - (void)unmuteLocalAudio: | (TUISuccessBlock)onSuccess |
| --- | --- |
| onError: | (TUIErrorBlock)onError |

#### Возобновить трансляцию локального аудиопотока.

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). Если вы открыли микрофон и вызовите API для возобновления трансляции локального аудиопотока, SDK уведомит пользователей в комнате через обратный вызов [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54854#57eafbcdec43b9cacef68034b3087e45) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## enableSystemAudioSharing:

**enableSystemAudioSharing:**

| - (void)enableSystemAudioSharing: | (BOOL)enable |
| --- | --- |

#### Включить демонстрацию системного звука

Этот API захватывает данные системного звука с вашего устройства и смешивает их с текущим аудиопотоком SDK. Это гарантирует, что другие пользователи в комнате услышат звук, воспроизводимый другим приложением.

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). Android: Сначала необходимо использовать этот интерфейс для включения захвата системного звука, и он будет работать только при вызове startScreenCapture для включения демонстрации экрана.

## setRemoteVideoView:streamType:view:

**setRemoteVideoView:streamType:view:**

| - (void)setRemoteVideoView: | (NSString *)userId |
| --- | --- |
| streamType: | ([TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15))streamType |
| view: | (TUIVideoView *__nullable)view |

#### Установить представление для отрендеринга видео удаленного пользователя.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока. Дополнительные сведения см. в [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15). |
| userId | Идентификатор удаленного пользователя. |
| view | Представление для отрендеринга. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## startPlayRemoteVideo:streamType:onPlaying:onLoading:onError:

**startPlayRemoteVideo:streamType:onPlaying:onLoading:onError:**

| - (void)startPlayRemoteVideo: | (NSString *)userId |
| --- | --- |
| streamType: | ([TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15))streamType |
| onPlaying: | (TUIPlayOnPlayingBlock)onPlaying |
| onLoading: | (TUIPlayOnLoadingBlock)onLoading |
| onError: | (TUIPlayOnErrorBlock)onError |

#### Начать воспроизведение видеопотока удаленного пользователя.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока. Дополнительные сведения см. в [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15). |
| userId | Идентификатор пользователя. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## stopPlayRemoteVideo:streamType:

**stopPlayRemoteVideo:streamType:**

| - (void)stopPlayRemoteVideo: | (NSString *)userId |
| --- | --- |
| streamType: | ([TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15))streamType |

#### Остановить воспроизведение видеопотока удаленного пользователя.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока. Дополнительные сведения см. в [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/64477#ca0c0e583eff1fbc8e326f6802b59f15). |
| userId | Идентификатор пользователя. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## muteRemoteAudioStream:isMute:

**muteRemoteAudioStream:isMute:**

| - (void)muteRemoteAudioStream: | (NSString *)userId |
| --- | --- |
| isMute: | (BOOL)isMute |

#### Отключить аудиопоток удаленного пользователя.

| Параметр | Описание |
| --- | --- |
| isMute | true: приостановить получение аудиопотока удаленного пользователя, false: возобновить получение аудиопотока удаленного пользователя. |
| userId | Идентификатор пользователя. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## getUserList:onSuccess:onError:

**getUserList:onSuccess:onError:**

| - (void)getUserList: | (NSInteger)nextSequence |
| --- | --- |
| onSuccess: | (TUIUserListResponseBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Получить список пользователей в комнате.

| Параметр | Описание |
| --- | --- |
| nextSequence | Для первого запроса укажите 0, если возвращаемые данные обратного вызова не равны нулю, требуется постраничный просмотр, продолжайте операцию до значения 0. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## getUserInfo:onSuccess:onError:

**getUserInfo:onSuccess:onError:**

| - (void)getUserInfo: | (NSString *)userId |
| --- | --- |
| onSuccess: | (TUIUserInfoBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Получить информацию о пользователе.

| Параметр | Описание |
| --- | --- |
| userId | Идентификатор пользователя. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## changeUserRole:role:onSuccess:onError:

**changeUserRole:role:onSuccess:onError:**

| - (void)changeUserRole: | (NSString *)userId |
| --- | --- |
| role: | ([TUIRole](https://www.tencentcloud.com/document/product/647/64477#246382de7328bdcc5fe6680365be6234))role |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Изменить роль пользователя (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| role | Роль пользователя. Дополнительные сведения см. в [TUIRole](https://www.tencentcloud.com/document/product/647/64477#246382de7328bdcc5fe6680365be6234). |
| userId | Идентификатор пользователя. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После изменения роли пользователя SDK уведомит пользователей в комнате через обратный вызов [onUserInfoChanged](https://www.tencentcloud.com/document/product/647/54854#b5637d7d08d9811983db56c8dd28f051) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## changeUserNameCard:nameCard:onSuccess:onError:

**changeUserNameCard:nameCard:onSuccess:onError:**

| - (void)changeUserNameCard: | (NSString *)userId |
| --- | --- |
| nameCard: | (NSString *)nameCard |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Изменить никнейм пользователя в комнате (администраторы и владельцы комнат могут менять для всех пользователей, пользователи могут менять только свой).

| Параметр | Описание |
| --- | --- |
| nameCard | Устанавливаемый никнейм пользователя, максимум 32 байта |
| userId | Идентификатор пользователя для изменения. |

> **Примечание**: Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После изменения никнейма пользователя SDK уведомит пользователей в комнате через обратный вызов [onUserInfoChanged](https://www.tencentcloud.com/document/product/647/54854#b5637d7d08d9811983db56c8dd28f051) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## kickRemoteUserOutOfRoom:onSuccess:onError:

**kickRemoteUserOutOfRoom:onSuccess:onError:**

| - (void)kickRemoteUserOutOfRoom: | (NSString *)userId |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Удалить удаленного пользователя из комнаты (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| userId | Идентификатор пользователя. |

> **Примечание**: Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После удаления пользователя из комнаты SDK уведомляет удаленного пользователя через обратный вызов [onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/54854#bbebfbd4e8b6c95b7852d1493f60bd4e) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa) и уведомляет пользователей в комнате через [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54854#16b0d80475c0d1f945024d5116074c66).

## addCategoryTagForUsers:userList:onSuccess:onError:

**addCategoryTagForUsers:userList:onSuccess:onError:**

| - (void)addCategoryTagForUsers: | (NSInteger)tag |
| --- | --- |
| userList: | (NSArray<NSString *> *)userList |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Добавить тег для пользователя (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| tag | Целое число, рекомендуется, чтобы это значение было больше или равно 1000, вы можете использовать пользовательское значение. |
| userList | Список пользователей. |

> **Примечание**: Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## removeCategoryTagForUsers:userList:onSuccess:onError:

**removeCategoryTagForUsers:userList:onSuccess:onError:**

| - (void)removeCategoryTagForUsers: | (NSInteger)tag |
| --- | --- |
| userList: | (NSArray<NSString *> *)userList |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Удалить тег для пользователя (поддерживается только для владельца комн

## takeSeat:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:

**takeSeat:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:**

| - (TUIRequest *)takeSeat: | (NSInteger)seatIndex |
| --- | --- |
| timeout: | (NSTimeInterval)timeout |
| onAccepted: | (TUIRequestAcceptedBlock)onAccepted |
| onRejected: | (TUIRequestRejectedBlock)onRejected |
| onCancelled: | (TUIRequestCancelledBlock)onCancelled |
| onTimeout: | (TUIRequestTimeoutBlock)onTimeout |
| onError: | (TUIRequestErrorBlock)onError |

#### Занять место.

| Param | DESC |
| --- | --- |
| seatIndex | Индекс места. Если место не включено или последовательность мест не требуется, просто заполните -1. |
| timeout | Время ожидания в секундах. Если установлено значение 0, SDK не будет выполнять обнаружение тайм-аута и не будет вызывать обратный вызов тайм-аута. |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). Пользователь может публиковать аудио/видео поток после занятия места, если isSeatEnable имеет значение true. После успешного занятия места SDK уведомит пользователей в комнате через $onSeatListChanged$ в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa). Когда [TUISeatMode](https://www.tencentcloud.com/document/product/647/64477#6e6fdc219cc838c9e3c5d622ab32c8f1) — ApplyToTake, операция занятия места требует одобрения владельца или администратора. Когда [TUISeatMode](https://www.tencentcloud.com/document/product/647/64477#6e6fdc219cc838c9e3c5d622ab32c8f1) — FreeToTake, вы можете свободно занять место.

#### Описание возврата:

TUIRequest Тело запроса.

## leaveSeat:onError:

**leaveSeat:onError:**

| - (void)leaveSeat: | (TUISuccessBlock)onSuccess |
| --- | --- |
| onError: | (TUIErrorBlock)onError |

#### Покинуть место.

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). Пользователь не может публиковать аудио/видео поток после покидания места, если isSeatEnable имеет значение true. После успешного покидания места SDK уведомит пользователей в комнате через [onSeatListChanged](https://www.tencentcloud.com/document/product/647/54854#31a13be6f374e28422eb363a518b235f) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## moveToSeat:onSuccess:onError:

**moveToSeat:onSuccess:onError:**

| - (void)moveToSeat: | (NSInteger)targetSeatIndex |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Переместиться на место.

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После успешного перемещения на место SDK уведомит пользователей в комнате через [onSeatListChanged](https://www.tencentcloud.com/document/product/647/54854#31a13be6f374e28422eb363a518b235f) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## takeUserOnSeatByAdmin:userId:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:

**takeUserOnSeatByAdmin:userId:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:**

| - (TUIRequest *)takeUserOnSeatByAdmin: | (NSInteger)seatIndex |
| --- | --- |
| userId: | (NSString *)userId |
| timeout: | (NSTimeInterval)timeout |
| onAccepted: | (TUIRequestAcceptedBlock)onAccepted |
| onRejected: | (TUIRequestRejectedBlock)onRejected |
| onCancelled: | (TUIRequestCancelledBlock)onCancelled |
| onTimeout: | (TUIRequestTimeoutBlock)onTimeout |
| onError: | (TUIRequestErrorBlock)onError |

#### Пригласить пользователя занять место (только для администраторов или владельца комнаты).

| Param | DESC |
| --- | --- |
| seatIndex | Индекс места. |
| timeout | Время ожидания в секундах. Если установлено значение 0, SDK не будет выполнять обнаружение тайм-аута и не будет вызывать обратный вызов тайм-аута. |
| userId | ID пользователя. |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После успешного вызова API SDK уведомит приглашённого пользователя через [onRequestReceived](https://www.tencentcloud.com/document/product/647/54854#3697d1d038fd6f3ebe54ea33cd32e3df) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

#### Описание возврата:

TUIRequest: Тело запроса.

## kickUserOffSeatByAdmin:userId:onSuccess:onError:

**kickUserOffSeatByAdmin:userId:onSuccess:onError:**

| - (void)kickUserOffSeatByAdmin: | (NSInteger)seatIndex |
| --- | --- |
| userId: | (NSString *)userId |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Исключить пользователя с места (только для администраторов или владельца комнаты).

| Param | DESC |
| --- | --- |
| seatIndex | Индекс места. Если место не включено и последовательность мест не требуется, просто заполните -1. |
| userId | ID пользователя. |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После успешного вызова API SDK уведомит пользователей в комнате через [onSeatListChanged](https://www.tencentcloud.com/document/product/647/54854#31a13be6f374e28422eb363a518b235f) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## getSeatApplicationList:onError:

**getSeatApplicationList:onError:**

| - (void)getSeatApplicationList: | (TUIRequestListResponseBlock)onSuccess |
| --- | --- |
| onError: | (TUIErrorBlock)onError |

#### Получить список запросов пользователей, которые хотят занять место в комнате (только для администраторов или владельца комнаты).

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## disableSendingMessageByAdmin:isDisable:onSuccess:onError:

**disableSendingMessageByAdmin:isDisable:onSuccess:onError:**

| - (void)disableSendingMessageByAdmin: | (NSString *)userId |
| --- | --- |
| isDisable: | (BOOL)isDisable |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Отключить возможность удалённых пользователей отправлять сообщения (только для администраторов или владельца комнаты).

| Param | DESC |
| --- | --- |
| isDisable | true: запретить пользователю отправлять сообщение, false: разрешить пользователю отправлять сообщение. |
| userId | ID пользователя. |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После отключения возможности удалённых пользователей отправлять сообщения SDK уведомит отключённого пользователя через [onSendMessageForUserDisableChanged](https://www.tencentcloud.com/document/product/647/54854#d1f497f96f9523b0d284992b90b22d26) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## disableSendingMessageForAllUser:onSuccess:onError:

**disableSendingMessageForAllUser:onSuccess:onError:**

| - (void)disableSendingMessageForAllUser: | (BOOL)isDisable |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Отключить возможность всех пользователей отправлять сообщения (только для администраторов или владельца комнаты).

| Param | DESC |
| --- | --- |
| isDisable | true: запретить всем пользователям отправлять сообщение, false: разрешить всем пользователям отправлять сообщение. |

> **Примечание** Функция поддерживает только тип комнаты [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После отключения возможности всех пользователей отправлять сообщения SDK уведомит пользователей в комнате через [onSendMessageForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54854#b64a6a83036eb91c14d381c1feca555b) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa).

## sendTextMessage:onSuccess:onError:

**sendTextMessage:onSuccess:onError:**

| - (void)sendTextMessage: | ([TUIRoomTextMessage](https://www.tencentcloud.com/document/product/647/64477#7e0dfeb925fa7e89ac4d1073c6e2a046) *)textMessage |
| --- | --- |
| onSuccess: | (TUISendTextMessageBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Отправить текстовое сообщение

| Param | DESC |
| --- | --- |
| onError | Обратный вызов ошибки. |
| onSuccess | Обратный вызов успеха. |
| textMessage | Объект сообщения. |

## sendCustomMessage:onSuccess:onError:

**sendCustomMessage:onSuccess:onError:**

| - (void)sendCustomMessage: | ([TUIRoomCustomMessage](https://www.tencentcloud.com/document/product/647/64477#2dbc71d1c436a27bf13d15a5d22e01d1) *)customMessage |
| --- | --- |
| onSuccess: | (TUISendCustomMessageBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Отправить пользовательское сообщение

| Param | DESC |
| --- | --- |
| customMessage | Объект сообщения. |
| onError | Обратный вызов ошибки. |
| onSuccess | Обратный вызов успеха. |

## cancelRequest:onSuccess:onError:

**cancelRequest:onSuccess:onError:**

| - (void)cancelRequest: | (NSString *)requestId |
| --- | --- |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Отменить запрос.

| Param | DESC |
| --- | --- |
| requestId | ID запроса (получить из отправленного запроса). |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). После отмены запроса SDK уведомит запрашиваемого пользователя через [onRequestCancelled](https://www.tencentcloud.com/document/product/647/54854#92b334084d0e34a0a3d4507e02acb850) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54854#6768cb2b92f818315a7d2ac8774f72fa). API можно использовать для отмены отправленного запроса.

## responseRemoteRequest:agree:onSuccess:onError:

**responseRemoteRequest:agree:onSuccess:onError:**

| - (void)responseRemoteRequest: | (NSString *)requestId |
| --- | --- |
| agree: | (BOOL)agree |
| onSuccess: | (TUISuccessBlock)onSuccess |
| onError: | (TUIErrorBlock)onError |

#### Ответить на запрос.

| Param | DESC |
| --- | --- |
| agree | YES: Согласиться с запросом, NO: Отклонить запрос. |
| requestId | ID запроса (получить из отправленного запроса или уведомления события OnRequestReceived). |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248). При получении запроса вы можете использовать этот API для ответа на полученный запрос.

## getTRTCCloud

**getTRTCCloud**

#### Получить объект экземпляра TRTC.

## setBeautyLevel:beautyLevel:

**setBeautyLevel:beautyLevel:**

| - (void)setBeautyLevel: | (NSInteger)beautyStyle |
| --- | --- |
| beautyLevel: | (float)beautyLevel |

#### Установить уровень красоты.

| Param | DESC |
| --- | --- |
| beautyLevel | Уровень красоты, диапазон значений 0–9; 0 означает отключение фильтра, а 9 означает наиболее очевидный эффект. |
| beautyStyle | Стиль красоты, значения следующие: 0: Гладкий, эффект сглаживания кожи более очевиден; 1: Естественный, эффект сглаживания кожи более естественный и сохраняются больше деталей лица; 2: Отличный, эффект сглаживания кожи находится между гладким и естественным, сохраняет больше деталей кожи, чем гладкий, и степень сглаживания кожи выше, чем естественный. |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## setWhitenessLevel:

**setWhitenessLevel:**

| - (void)setWhitenessLevel: | (float)whitenessLevel |
| --- | --- |

#### Установить уровень отбеливания.

| Param | DESC |
| --- | --- |
| whitenessLevel | Уровень отбеливания, диапазон 0–9; 0 означает отключение фильтра, а 9 означает наиболее очевидный эффект. |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## getExtension:

**getExtension:**

| - (id) getExtension: | ([TUIExtensionType](https://www.tencentcloud.com/document/product/647/64475#9d4c7f4d7226087edd7da128249f1de7))extensionType |
| --- | --- |

#### Получить расширение.

| Param | DESC |
| --- | --- |
| extensionType | Тип расширения. Более подробные сведения см. в [TUIExtensionType](https://www.tencentcloud.com/document/product/647/64475#9d4c7f4d7226087edd7da128249f1de7). |

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## getMediaDeviceManager

**getMediaDeviceManager**

#### Получить класс управления устройствами.

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## getLiveConnectionManager

**getLiveConnectionManager**

#### Получить класс управления подключением прямой трансляции.

> **Примечание** Функция поддерживает тип комнаты [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## getLiveBattleManager

**getLiveBattleManager**

#### Получить класс управления боевым режимом прямой трансляции.

> **Примечание** Функция поддерживает тип комнаты [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).

## callExperimentalAPI:callback:

**callExperimentalAPI:callback:**

| - (id)callExperimentalAPI: | (NSString *)jsonStr |
| --- | --- |
| callback: | (TUIExperimentalAPIResponseBlock)callback |

#### Вызвать экспериментальные API.

> **Примечание** Функция поддерживает типы комнат [TUIRoomTypeConference](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248) и [TUIRoomTypeLive](https://www.tencentcloud.com/document/product/647/64477#7f245d24537c126ff60fed533d974248).


---
*Источник: [https://trtc.io/document/54855](https://trtc.io/document/54855)*

---
*Источник (EN): [tuiroomengine.md](./tuiroomengine.md)*
