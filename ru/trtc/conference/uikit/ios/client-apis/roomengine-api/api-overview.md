# Обзор API

**ОБЗОР API**

## Создание экземпляров и обратный вызов события.

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/54855#7591fdc3a0ca12c99ae6e02bd406ed17) | Создать экземпляр TUIRoomEngine (паттерн singleton). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/54855#665e37566fe89fb0abeb66ef2fc3d5db) | Уничтожить экземпляр TUIRoomEngine (паттерн singleton). |
| [loginWithSDKAppId:userId:userSig:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#fb5d593fb688c5e26a700db98250e6dd) | После создания экземпляра TUIRoomEngine необходимо выполнить вход с помощью sdkAppId, userId и userSig, затем можно вызывать экземпляр TUIRoomEngine и другие функции. |
| [logout:onError:](https://www.tencentcloud.com/document/product/647/54855#509b68f796961e5de754932fb21aa50a) | Выход из учетной записи. Если вы находитесь в комнате, будут выполнены операции активного выхода из комнаты и освобождения ресурсов. |
| [setSelfInfoWithUserName:avatarUrl:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#0cf77ae0514c515dc5be4203a6d44f34) | Обновить имя пользователя и аватар для вошедшего в систему пользователя. |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54855#55196a0862d9231f772d05263e703cb2) | Возвращает основную информацию вошедшего в систему пользователя, включая ник и аватар. |
| [setSelfInfo:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#b3121cde5287dbe110376617320fad58) | Обновить основную информацию пользователя для вошедшего в систему пользователя. |
| [addObserver:](https://www.tencentcloud.com/document/product/647/54855#b272afc5ebfd02ef90e7e8dc599a4b82) | Установить наблюдатель события. |
| [removeObserver:](https://www.tencentcloud.com/document/product/647/54855#34e77ed104d979192e355dbb31e84fbf) | Удалить наблюдатель события. |

## API комнаты.

| FuncList | DESC |
| --- | --- |
| [createRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#4d0e7ddf563f6245a1d812b0690a5eea) | Создать комнату. |
| [destroyRoom:onError:](https://www.tencentcloud.com/document/product/647/54855#31650ce63622900078ee2f81c23e4454) | Закрыть комнату. |
| [enterRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#e76b632b17a47f9254f32d2f5ed96222) | Войти в комнату. |
| [enterRoom:roomType:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#c14956bfcb56cb3759b498050631331a) | Войти в комнату. |
| [enterRoom:roomType:options:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#3e5f7fdc1c30135d17bd4464609d99e4) | Войти в комнату. |
| [exitRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#cb2aa94c3b2e1d926793eb7aaab410e8) | Выйти из комнаты. |
| [fetchRoomInfo:onError:](https://www.tencentcloud.com/document/product/647/54855#f6d4167648189c5290b711062c74e8fd) | Получить информацию о комнате. |
| [fetchRoomInfo:roomType:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#26f5a1529c27553cce6c56d942c80ad0) | Получить информацию об указанной комнате. |
| [updateRoomNameByAdmin:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#bc6afcb38590615a5df7600df29367ba) | Обновить имя комнаты (поддерживается только администраторами или владельцем комнаты). |
| [updateRoomSeatModeByAdmin:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#d06444a359611753052ac864c5b611e9) | Обновить режим мест в комнате (поддерживается только администраторами или владельцем комнаты). |
| [updateRoomPasswordByAdmin:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#8a55267d6730bb708d531581746fa966) | Обновить пароль комнаты (поддерживается только администраторами или владельцем комнаты). |
| [getRoomMetadata:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#f7eb8d8350b755920accc62b1b7e4397) | Получить метаданные комнаты. |
| [setRoomMetadataByAdmin](https://www.tencentcloud.com/document/product/647/54855#fba0ca6c5bae1858bcf81734036248cc) | Установить метаданные комнаты, если ключ уже существует, обновить его значение, если нет, добавить ключ. |

## Отрисовка локального представления пользователя и управление видео.

| FuncList | DESC |
| --- | --- |
| [setLocalVideoView:](https://www.tencentcloud.com/document/product/647/54855#55a67c65f1344a3339ee151b807d24ab) | Установить локальную камеру для предпросмотра представления отрисовки. |
| [openLocalCamera:quality:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#f72c16229f46ba7b28b0d9849ac98826) | Открыть локальную камеру. |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/54855#ff4537fd911678280a013b61005345ed) | Закрыть локальную камеру. |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/54855#b178202f1acaedf7f1088ce109d3f963) | Начать публикацию локального видеопотока, включено по умолчанию. |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/54855#4500cae058442aa6cf0660899c590b9d) | Остановить публикацию локального видеопотока. |
| [updateVideoQuality:](https://www.tencentcloud.com/document/product/647/54855#486a72e802a93ad219ac70b2f987ff2d) | Обновить качество кодирования видео. |
| [updateVideoQualityEx:params:](https://www.tencentcloud.com/document/product/647/54855#bf634578e3304a18894e04560468c20f) | Установить параметры кодирования видео. |
| [setVideoResolutionMode:resolutionMode:](https://www.tencentcloud.com/document/product/647/54855#60c1bc35ad2ebbe4b19198bc16ea2865) | Установить режим разрешения видео (горизонтальное разрешение или вертикальное разрешение). |
| [setLocalVideoMuteImage:](https://www.tencentcloud.com/document/product/647/54855#0fdb2eda054cdf1d2b7c74268d16c62a) | Установить замещающее изображение для локального видео при паузе. |
| [enableGravitySensor:](https://www.tencentcloud.com/document/product/647/54855#e43024d3910ad9ec7001aa44bc8275af) | Включить режим определения гравитации. (доступно только на мобильных ОС и в сценах захвата камеры внутри SDK). |
| [startScreenCaptureByReplaykit:](https://www.tencentcloud.com/document/product/647/54855#fe00b96dd343d6975b4350efc157d5c8) | Начать совместное использование экрана (доступно только на мобильных ОС). |
| [startScreenCapture:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#f0c5bef34ea01c7a57f75905a116b310) | Начать совместное использование экрана (доступно только на Mac OS). |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/54855#0fa4aee168037d922e21047913bb8382) | Остановить совместное использование экрана. |
| [getScreenCaptureSources](https://www.tencentcloud.com/document/product/647/54855#45bab04fe4f34e65db53282904eab4db) | Получить общедоступные экраны и окна (доступно только на Mac OS) |
| [selectScreenCaptureTarget:](https://www.tencentcloud.com/document/product/647/54855#fe760c4f87bf7d13e878f0085bdb06e9) | Выбрать экран или окна для совместного использования (доступно только на Mac OS) |

## Управление локальным аудио пользователя.

| FuncList | DESC |
| --- | --- |
| [openLocalMicrophone:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#0d61ecfc837ff6d44e5a5c3d0faee8b3) | Открыть локальный микрофон. |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/54855#6a5f4544cf81d483a4dba368545f94b9) | Закрыть локальный микрофон. |
| [updateAudioQuality:](https://www.tencentcloud.com/document/product/647/54855#8b1839388fa8e799f0ae35c49a3f2911) | Обновить качество кодирования аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/54855#c64198c0a04341cac736e4104ebdf0bd) | Приостановить публикацию локального аудиопотока. |
| [unmuteLocalAudio:onError:](https://www.tencentcloud.com/document/product/647/54855#14f97e6ab0e879b699ab0e37b485eba4) | Возобновить публикацию локального аудиопотока. |
| [enableSystemAudioSharing:](https://www.tencentcloud.com/document/product/647/54855#25c0877abd6134e2522eafe7c4de65f9) | Включить совместное использование системного аудио |

## Отрисовка представления удаленного пользователя и управление видео.

| FuncList | DESC |
| --- | --- |
| [setRemoteVideoView:streamType:view:](https://www.tencentcloud.com/document/product/647/54855#e3a3d88e04a1f569e6dcb68d91cce59a) | Установить представление отрисовки для удаленного пользователя. |
| [startPlayRemoteVideo:streamType:onPlaying:onLoading:onError:](https://www.tencentcloud.com/document/product/647/54855#989232414785216d37587684becbb483) | Начать воспроизведение видеопотока удаленного пользователя. |
| [stopPlayRemoteVideo:streamType:](https://www.tencentcloud.com/document/product/647/54855#5500e4b4d12b3d56faee3eb725b00f1a) | Остановить воспроизведение видеопотока удаленного пользователя. |
| [muteRemoteAudioStream:isMute:](https://www.tencentcloud.com/document/product/647/54855#b78726b72ddf579f240da34884b2c609) | Отключить аудиопоток удаленного пользователя. |

## Информация пользователя в комнате.

| FuncList | DESC |
| --- | --- |
| [getUserList:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#1e4f7da192b0128754ba6e9f385bed8d) | Получить список пользователей в комнате. |
| [getUserInfo:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#ec236cd0d12ab2fce2ca5621f668ab5d) | Получить информацию о пользователе. |

## Управление пользователями в комнате.

| FuncList | DESC |
| --- | --- |
| [changeUserRole:role:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#17f8c2dc10f266cbc78d3b1812f95240) | Изменить роль пользователя (поддерживается только администраторами или владельцем комнаты). |
| [changeUserNameCard:nameCard:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#b1ea3d2360a2c0889ffc5cf382fb9da2) | Изменить ник пользователя в комнате (администраторы или владелец комнаты могут изменять всех пользователей, пользователи могут изменять только себя). |
| [kickRemoteUserOutOfRoom:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#fa4bd9852c77cf5f5b7be203fe6dbb22) | Исключить удаленного пользователя из комнаты (поддерживается только администраторами или владельцем комнаты). |
| [addCategoryTagForUsers:userList:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#619bec5e8dcb6619488732a8a9effaae) | Добавить тег для пользователя (поддерживается только администраторами или владельцем комнаты). |
| [removeCategoryTagForUsers:userList:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#6e3ba5a485a91fc43757891c4dc99d27) | Удалить тег для пользователя (поддерживается только владельцем комнаты). |
| [getUserListByTag:nextSequence:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#333966765d152e41f549157cc2ab7071) | Получить информацию о пользователях в комнате по тегу. |
| [setCustomInfoForUser:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#56222c867961904dc8769ad714bba5fe) | Установить пользовательскую информацию для пользователей комнаты. |

## Управление речью пользователя в комнате.

| FuncList | DESC |
| --- | --- |
| [disableDeviceForAllUserByAdmin:isDisable:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#8f96b729c8a9948c9cf7d2ebfd6ff48f) | Владелец или администратор контролируют, могут ли все пользователи открывать устройство. Например: всем пользователям запрещено открывать микрофон (доступно только в сценарии конференции). |
| [openRemoteDeviceByAdmin:device:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#5efa632932881735e551ff016402160b) | Запросить у удаленного пользователя открыть медиаустройство (поддерживается только администраторами или владельцем комнаты). |
| [closeRemoteDeviceByAdmin:device:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#780489248cb022a5495812a6eb072317) | Закрыть медиаустройства удаленного пользователя (поддерживается только администраторами или владельцем комнаты). |
| [applyToAdminToOpenLocalDevice:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#4993a64e14a999449612351df8a574c6) | Подать заявку на открытие локального медиаустройства (доступно обычным пользователям). |

## Управление местами в комнате.

| FuncList | DESC |
| --- | --- |
| [getSeatList:onError:](https://www.tencentcloud.com/document/product/647/54855#9a8217b0951913d5c24a3418cd5f452d) | Получить список мест. |
| [lockSeatByAdmin:lockMode:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#df1f081b00d3640cd6173899e788d9bf) | Заблокировать место (поддерживается только администраторами или владельцем комнаты). |
| [takeSeat:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#b7dec60a76be6d9a9b63093319301943) | Занять место. |
| [leaveSeat:onError:](https://www.tencentcloud.com/document/product/647/54855#f301d65082c9fe6e54df6f74522df36d) | Покинуть место. |
| [moveToSeat:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#17c6072ee712ee80751eb30a5815ff1b) | Переместиться на место. |
| [takeUserOnSeatByAdmin:userId:timeout:onAccepted:onRejected:onCancelled:onTimeout:onError:](https://www.tencentcloud.com/document/product/647/54855#060623f0395a1416baf48ebd80c598f1) | Пригласить пользователя занять место (поддерживается только администраторами или владельцем комнаты). |
| [kickUserOffSeatByAdmin:userId:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#4fc6a6c9e386a7a0d9dda3a6a0aade6f) | Выгнать пользователя с места (поддерживается только администраторами или владельцем комнаты). |
| [getSeatApplicationList:onError:](https://www.tencentcloud.com/document/product/647/54855#318ba4689ead5ec4214664f23c92a6e3) | Получить список запросов пользователей, которые хотят занять место в комнате (поддерживается только администраторами или владельцем комнаты). |

## Сообщение.

| FuncList | DESC |
| --- | --- |
| [disableSendingMessageByAdmin:isDisable:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#99f76e01022ed98bcb8759320810d85b) | Отключить возможность удаленных пользователей отправлять сообщения (поддерживается только администраторами или владельцем комнаты). |
| [disableSendingMessageForAllUser:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#88f96a71fd0ee8c59ab3cdecd0930551) | Отключить возможность всех пользователей отправлять сообщения (поддерживается только администраторами или владельцем комнаты). |
| [sendTextMessage:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#2211c4227dfecaf8a1a0448d943599d2) | Отправить текстовое сообщение |
| [sendCustomMessage:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#a6092b6681c81429033efd93161b415e) | Отправить пользовательское сообщение |

## Управление запросами.

| FuncList | DESC |
| --- | --- |
| [cancelRequest:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#17ba27cad02e54757cdd41e442ddfbbc) | Отменить запрос. |
| [responseRemoteRequest:agree:onSuccess:onError:](https://www.tencentcloud.com/document/product/647/54855#10789c19d23dec9a25d6c8bfab407f23) | Ответить на запрос. |

## Расширенные функции.

| FuncList | DESC |
| --- | --- |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54855#d3c48e3c9d0f371386ca7b0589ef4c88) | Получить объект экземпляра TRTC. |
| [setBeautyLevel:beautyLevel:](https://www.tencentcloud.com/document/product/647/54855#4c6d4893dba79b7e4a41a001eaea1534) | Установить уровень красоты. |
| [setWhitenessLevel:](https://www.tencentcloud.com/document/product/647/54855#ba29ed099d81a69fc300a82caebb8fde) | Установить уровень отбеливания. |
| [getExtension:](https://www.tencentcloud.com/document/product/647/54855#b99da8d3a9d62547dd23c56e0b4436c0) | Получить расширение. |
| [getMediaDeviceManager](https://www.tencentcloud.com/document/product/647/54855#c6483c3f80f639d0eb3fd076f02872d6) | Получить класс управления устройствами. |
| [getLiveConnectionManager](https://www.tencentcloud.com/document/product/647/54855#fdb1665975863e593233d97715af0dc5) | Получить класс управления прямой трансляцией. |
| [getLiveBattleManager](https://www.tencentcloud.com/document/product/647/54855#0a32a3590a6ae1e2776d80e5eb3040e1) | Получить класс управления боевой прямой трансляцией. |

## Отладка связанных.

| FuncList | DESC |
| --- | --- |
| [callExperimentalAPI:callback:](https://www.tencentcloud.com/document/product/647/54855#91021955c4aadb7dfcbff8f0376f0106) | Вызвать экспериментальные API. |

## Обратный вызов события ошибки.

| FuncList | DESC |
| --- | --- |
| [onError:message:](https://www.tencentcloud.com/document/product/647/54854#e2d2a8b13e80bbe60e2467739f0a0316) | Обратный вызов события ошибки. |

## Обратный вызов события статуса входа.

| FuncList | DESC |
| --- | --- |
| [onKickedOffLine:](https://www.tencentcloud.com/document/product/647/54854#b0238d7b1fa86af2c540ec313dba8e6b) | Текущий пользователь был отключен в сети. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/54854#7b8df3f701ffd641b11047e27094d8db) | Сигнатура текущего пользователя истекла. |

## Обратный вызов события в комнате.

| FuncList | DESC |
| --- | --- |
| [onRoomNameChanged:roomName:](https://www.tencentcloud.com/document/product/647/54854#14f6f031aedb2aef37640bd8d52b512d) | Имя комнаты изменилось. |
| [onAllUserMicrophoneDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#3ec4485cdec9612c161c8a3211b2fb28) | Статус отключения открытия микрофона изменился для всех пользователей. |
| [onAllUserCameraDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#55a547bc323badf7599db85f13c6b286) | Статус отключения открытия камеры изменился для всех пользователей. |
| [onScreenShareForAllUserDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#fe6861c09539278fb9440da696c4d028) | Статус отключения открытия совместного использования экрана изменился для всех пользователей. |
| [onSendMessageForAllUserDisableChanged:isDisable:](https://www.tencentcloud.com/document/product/647/54854#b64a6a83036eb91c14d381c1feca555b) | Статус отключения отправки сообщения изменился для всех пользователей. |
| [onRoomDismissed:reason:](https://www.tencentcloud.com/document/product/647/54854#e3741060867444c54121e60eb54f989c) | Комната была закрыта. |
| [onKickedOutOfRoom:reason:message:](https://www.tencentcloud.com/document/product/647/54854#bbebfbd4e8b6c95b7852d1493f60bd4e) | Текущий пользователь был исключен из комнаты. |
| [onRoomSeatModeChanged:seatMode:](https://www.tencentcloud.com/document/product/647/54854#43c39ab0e5611de1f28bfe62e4e0077b) | Режим мест в комнате изменился. |
| [onRoomUserCountChanged:userCount:](https://www.tencentcloud.com/document/product/647/54854#4c5cdb0b2676614586770fe9085576fe) | Количество пользователей в комнате изменилось. |
| [onRoomMetadataChanged:value:](https://www.tencentcloud.com/document/product/647/54854#f3151fab3ff4a34eed91d740e05c9d5f) | Значение ключа метаданных комнаты изменилось. |

## Обратный вызов события пользователя в комнате.

| FuncList | DESC |
| --- | --- |
| [onRemoteUserEnterRoom:userInfo:](https://www.tencentcloud.com/document/product/647/54854#64bc4ce1b62e5a15de963ecfb9225e98) | Удаленный пользователь вошел в комнату. |
| [onRemoteUserLeaveRoom:userInfo:](https://www.tencentcloud.com/document/product/647/54854#16b0d80475c0d1f945024d5116074c66) | Удаленный пользователь покинул комнату. |
| [onUserInfoChanged:modifyFlag:](https://www.tencentcloud.com/document/product/647/54854#b5637d7d08d9811983db56c8dd28f051) | Информация пользователя в комнате изменилась. |
| [onUserVideoStateChanged:streamType:hasVideo:reason:](https://www.tencentcloud.com/document/product/647/54854#00c4eb2525cf2b404bb784d7731d95a8) | Статус наличия видеопотока у пользователя изменился. |
| [onUserAudioStateChanged:hasAudio:reason:](https://www.tencentcloud.com/document/product/647/54854#57eafbcdec43b9cacef68034b3087e45) | Статус наличия аудиопотока у пользователя изменился. |
| [onUserVoiceVolumeChanged](https://www.ten

---
*Источник (EN): [api-overview.md](./api-overview.md)*
