# TUIRoomEngine

© 2024 Tencent. Все права защищены.

Модуль: TUIRoomEngine @ TUIKitEngine.

Функция: API-интерфейсы основных функций TUIRoomEngine.

Версия: 3.2

**TUIRoomEngine**

## TUIRoomEngine

| FuncList | DESC |
| --- | --- |
| [sharedInstance](https://www.tencentcloud.com/document/product/647/54864#16cf67c8716b1c79b762d19e4ab99008) | Создать экземпляр TUIRoomEngine (паттерн одиночка). |
| [destroySharedInstance](https://www.tencentcloud.com/document/product/647/54864#56ce73cf1f0b6bf6492c81d308ec029d) | Уничтожить экземпляр TUIRoomEngine (паттерн одиночка). |
| [login](https://www.tencentcloud.com/document/product/647/54864#e91313128572e17f2397f7be8edd93cf) | После создания экземпляра TUIRoomEngine следует выполнить вход с использованием sdkAppId, userId и userSig, после чего можно вызывать экземпляр TUIRoomEngine и другие функции. |
| [logout](https://www.tencentcloud.com/document/product/647/54864#45756ace1ef6c82297eee3fac5cd8667) | Выход из учетной записи. Если вы находитесь в комнате, будут выполнены операции активного выхода из комнаты и освобождения ресурсов. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54864#bc3705389df676bb8e8cb68942dd820f) | Обновить имя пользователя и аватар для авторизованного пользователя. |
| [getSelfInfo](https://www.tencentcloud.com/document/product/647/54864#946bae7d91f5073f8044633a79a3c227) | Возвращает основную информацию авторизованного пользователя, включая псевдоним и аватар. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54864#effe69c548ae164bc3c1771de6706844) | Обновить основную информацию пользователя для авторизованного пользователя. |
| [addObserver](https://www.tencentcloud.com/document/product/647/54864#aa9e2a751854badf8d300deef59680b9) | Установить наблюдателя событий. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/54864#a66b02c83a4371533c8076e9715d13b8) | Удалить наблюдателя событий. |
| [createRoom](https://www.tencentcloud.com/document/product/647/54864#911bbef4c82371be741fa4c6c0693907) | Создать комнату. |
| [destroyRoom](https://www.tencentcloud.com/document/product/647/54864#9141c0291abba473fe8daeb75e3e052c) | Закрыть комнату. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54864#35fdf16804f2627fec75cdce28ffc6cc) | Войти в комнату. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54864#0b76c433d07df7aa3dfc9248c79d391e) | Войти в комнату. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54864#7d887cfe0029482a872a8bef2c90b29a) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/54864#380786b98d56b95daf683fa4d68af388) | Выйти из комнаты. |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/54864#592e4c141886cc8b8666cf8dfefc3a8f) | Получить информацию о комнате. |
| [fetchRoomInfo](https://www.tencentcloud.com/document/product/647/54864#3921f8c55dda7ecb9ae16ec0dcc7ac32) | Получить информацию об указанной комнате. |
| [updateRoomNameByAdmin](https://www.tencentcloud.com/document/product/647/54864#d970bfb9100d587e0d008db312b5bc5b) | Обновить имя комнаты (поддерживается только для администраторов или владельца комнаты). |
| [updateRoomSeatModeByAdmin](https://www.tencentcloud.com/document/product/647/54864#07121319d8ae42ebccb1761dcbe508a4) | Обновить режим мест в комнате (поддерживается только для администраторов или владельца комнаты). |
| [updateRoomPasswordByAdmin](https://www.tencentcloud.com/document/product/647/54864#cac0a265de041de6d6e57aa57d705ad6) | Обновить пароль комнаты (поддерживается только для администраторов или владельца комнаты). |
| [getRoomMetadata](https://www.tencentcloud.com/document/product/647/54864#4bf28fcd8a1146b0662779f3094a509e) | Получить метаданные комнаты. |
| [setRoomMetadataByAdmin](https://www.tencentcloud.com/document/product/647/54864#e774ac4968fa3eef64f36571ae2afe42) | Установить метаданные комнаты, если ключ уже существует, обновить его значение; если нет, добавить ключ. |
| [setLocalVideoView](https://www.tencentcloud.com/document/product/647/54864#98362c835e4499225b7f36ad9336d924) | Установить локальную камеру для предпросмотра видеопотока отображения. |
| [openLocalCamera](https://www.tencentcloud.com/document/product/647/54864#67c926e68b2bc30b9e20e0a0c4745bdf) | Открыть локальную камеру. |
| [closeLocalCamera](https://www.tencentcloud.com/document/product/647/54864#ef8016748e2d62b77b933cbbc0bc70d7) | Закрыть локальную камеру. |
| [startPushLocalVideo](https://www.tencentcloud.com/document/product/647/54864#899becc4c8470f2036a8e53131814471) | Начать публикацию локального видеопотока, включено по умолчанию. |
| [stopPushLocalVideo](https://www.tencentcloud.com/document/product/647/54864#672b82fcec8a33f5f4c2009321012adc) | Остановить публикацию локального видеопотока. |
| [updateVideoQuality](https://www.tencentcloud.com/document/product/647/54864#ea061bff081ab6fb25c9d23efbb659b3) | Обновить качество кодирования видео. |
| [updateVideoQualityEx](https://www.tencentcloud.com/document/product/647/54864#79bd53687be4c329a1674d28be1ce907) | Установить параметры кодирования видео. |
| [setVideoResolutionMode](https://www.tencentcloud.com/document/product/647/54864#a995efd41a996d7c0b09a3efb5ff5df1) | Установить режим разрешения видео (горизонтальное или вертикальное разрешение). |
| [setLocalVideoMuteImage](https://www.tencentcloud.com/document/product/647/54864#b8375cb87e8315e878fcaf6b12c12c5b) | Установить замещающее изображение для локального видео при паузе. |
| [enableGravitySensor](https://www.tencentcloud.com/document/product/647/54864#69775a6d4050ab5f60bdccedf14e9182) | Включить режим датчика гравитации. (доступно только на мобильных ОС и при захвате камеры внутри SDK). |
| [startScreenSharing](https://www.tencentcloud.com/document/product/647/54864#cc949f99d6a39e2bcf4723b664fe2d74) | Начать общий доступ к экрану (доступно только на мобильных ОС). |
| [stopScreenSharing](https://www.tencentcloud.com/document/product/647/54864#9c5fa0c202a0f5b24fed30ddf9e62939) | Остановить общий доступ к экрану. |
| [openLocalMicrophone](https://www.tencentcloud.com/document/product/647/54864#0e9b0f5598d305831ddb19ece07f1b91) | Открыть локальный микрофон. |
| [closeLocalMicrophone](https://www.tencentcloud.com/document/product/647/54864#f677ac0fc0aa1efcd27121054699bfdc) | Закрыть локальный микрофон. |
| [updateAudioQuality](https://www.tencentcloud.com/document/product/647/54864#778e31acbb656244cffdb4450ba0c156) | Обновить качество кодирования аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/54864#80693da4a3b18e07d92a802485f6334e) | Приостановить публикацию локального аудиопотока. |
| [unmuteLocalAudio](https://www.tencentcloud.com/document/product/647/54864#2a622d95aa2f7305de666cbec7109d77) | Возобновить публикацию локального аудиопотока. |
| [enableSystemAudioSharing](https://www.tencentcloud.com/document/product/647/54864#da0b9688d75cd77f51984e71566fab47) | Включить общий доступ к системному аудио |
| [setRemoteVideoView](https://www.tencentcloud.com/document/product/647/54864#0e6f5fe07c0f268923e502a3a2be76c1) | Установить представление отображения для удаленного пользователя. |
| [startPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54864#72d1726923e949d2c443dd96aa4deeca) | Начать воспроизведение видеопотока удаленного пользователя. |
| [stopPlayRemoteVideo](https://www.tencentcloud.com/document/product/647/54864#4d251840dd060f6ee45f3d41ad7a6c84) | Остановить воспроизведение видеопотока удаленного пользователя. |
| [muteRemoteAudioStream](https://www.tencentcloud.com/document/product/647/54864#2184de7077cf5dc9f3165329efbf43b5) | Отключить звук аудиопотока удаленного пользователя. |
| [getUserList](https://www.tencentcloud.com/document/product/647/54864#699fe77c2784c5d75f05078d5add27fb) | Получить список пользователей в комнате. |
| [getUserInfo](https://www.tencentcloud.com/document/product/647/54864#6cd5c36b39754b71ad5cce7bfd2ff4b4) | Получить информацию о пользователе. |
| [changeUserRole](https://www.tencentcloud.com/document/product/647/54864#f0cf468f4a2fa73a73f82e60329ae649) | Изменить роль пользователя (поддерживается только для администраторов или владельца комнаты). |
| [changeUserNameCard](https://www.tencentcloud.com/document/product/647/54864#33b8996e2230421dfb1a9c3bc00ecdf7) | Изменить псевдоним пользователя в комнате (только администраторы или владелец комнаты могут изменять для всех пользователей, пользователь может изменять только для себя). |
| [kickRemoteUserOutOfRoom](https://www.tencentcloud.com/document/product/647/54864#258101fd02fe373bb682f479d15fc059) | Исключить удаленного пользователя из комнаты (поддерживается только для администраторов или владельца комнаты). |
| [addCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/54864#a1345a3a776cab7c63c0e073b4885481) | Добавить тег для пользователя (поддерживается только для администраторов или владельца комнаты). |
| [removeCategoryTagForUsers](https://www.tencentcloud.com/document/product/647/54864#045a6dc44d38e0d1ac8e282cd1d1676e) | Удалить тег для пользователя (поддерживается только для владельца комнаты). |
| [getUserListByTag](https://www.tencentcloud.com/document/product/647/54864#c27be9df993987f57823fb7d0946722f) | Получить информацию о пользователях в комнате на основе тега. |
| [setCustomInfoForUser](https://www.tencentcloud.com/document/product/647/54864#f8c95b9ae30880404583b6786a3e4789) | Установить пользовательскую информацию для пользователей комнаты. |
| [disableDeviceForAllUserByAdmin](https://www.tencentcloud.com/document/product/647/54864#1ecce7f3cdb7dbb6f35fbaa3cc741122) | Владелец или администратор контролирует, могут ли все пользователи открывать устройства. Например: всем пользователям запрещено открывать микрофон (доступно только в сценарии конференции). |
| [openRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54864#590f32d6fe85c2fc80c339937aac9cdc) | Запросить удаленного пользователя открыть медиа-устройство (поддерживается только для администраторов или владельца комнаты). |
| [closeRemoteDeviceByAdmin](https://www.tencentcloud.com/document/product/647/54864#510e6569a496ebad2e04bde91326eb60) | Закрыть медиа-устройства удаленного пользователя (поддерживается только для администраторов или владельца комнаты). |
| [applyToAdminToOpenLocalDevice](https://www.tencentcloud.com/document/product/647/54864#4d4e5f3bc13e611768a401b4c3db962f) | Запросить открытие локального медиа-устройства (доступно для обычных пользователей). |
| [getSeatList](https://www.tencentcloud.com/document/product/647/54864#7820648092d091e37560ce0593879fc7) | Получить список мест. |
| [lockSeatByAdmin](https://www.tencentcloud.com/document/product/647/54864#81044cd0b188305f7227e3863c0e482f) | Заблокировать место (поддерживается только для администраторов или владельца комнаты). |
| [takeSeat](https://www.tencentcloud.com/document/product/647/54864#6eee934af96d5538e066a543c637e0cd) | Занять место. |
| [leaveSeat](https://www.tencentcloud.com/document/product/647/54864#84e97d04aa3dc31eda5d6b1bdeb4c34d) | Освободить место. |
| [moveToSeat](https://www.tencentcloud.com/document/product/647/54864#60d07dda176d554ffd84e0cf3e373262) | Перейти на место. |
| [takeUserOnSeatByAdmin](https://www.tencentcloud.com/document/product/647/54864#85fcac236a372109a330eb0c5e3f0a0b) | Пригласить пользователя занять место (поддерживается только для администраторов или владельца комнаты). |
| [kickUserOffSeatByAdmin](https://www.tencentcloud.com/document/product/647/54864#f878dca93c7266e7a132485ba1a00c4d) | Заставить пользователя покинуть место (поддерживается только для администраторов или владельца комнаты). |
| [getSeatApplicationList](https://www.tencentcloud.com/document/product/647/54864#54d31a649216d220311f8fcf8f905404) | Получить список запросов пользователей, которые хотят занять место в комнате (поддерживается только для администраторов или владельца комнаты). |
| [disableSendingMessageByAdmin](https://www.tencentcloud.com/document/product/647/54864#1a14651e5e06305956f7e8dd8c29b821) | Отключить способность удаленных пользователей отправлять сообщения (поддерживается только для администраторов или владельца комнаты). |
| [disableSendingMessageForAllUser](https://www.tencentcloud.com/document/product/647/54864#5f4a70034d79062967c860559af11b21) | Отключить способность всех пользователей отправлять сообщения (поддерживается только для администраторов или владельца комнаты). |
| [sendTextMessage](https://www.tencentcloud.com/document/product/647/54864#b642e3d2cee3cacc9e7c6f47af571314) | Отправить текстовое сообщение |
| [sendCustomMessage](https://www.tencentcloud.com/document/product/647/54864#7d14723294200fd5aa0c3853884fc97f) | Отправить пользовательское сообщение |
| [cancelRequest](https://www.tencentcloud.com/document/product/647/54864#3271224bcd640ef9a347492b18bed14b) | Отменить запрос. |
| [responseRemoteRequest](https://www.tencentcloud.com/document/product/647/54864#ca9c83c643f5bd6c26dd23ec34639660) | Ответить на запрос. |
| [getTRTCCloud](https://www.tencentcloud.com/document/product/647/54864#393689f458433968d8dcc9d91635d71b) | Получить объект экземпляра TRTC. |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/54864#356c9ac2d40d703ae8075ec6d99719b3) | Установить уровень красоты. |
| [setWhitenessLevel](https://www.tencentcloud.com/document/product/647/54864#7df1e01587684fba1d0a5766334703b3) | Установить уровень отбеливания. |
| [getExtension](https://www.tencentcloud.com/document/product/647/54864#5ad5ce957d19bef36541d4eb11a1051e) | Получить расширение. |
| [getMediaDeviceManager](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21) | Получить класс управления устройствами. |
| [getLiveConnectionManager](https://www.tencentcloud.com/document/product/647/54864#fe288b50da697505b5ab87a35bed950e) | Получить класс управления живыми соединениями. |
| [getLiveBattleManager](https://www.tencentcloud.com/document/product/647/54864#5d671512de7e22b0507211255a9c123f) | Получить класс управления живыми сражениями. |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/54864#781a86cef929d0e20b8721a3e17b3726) | Вызвать экспериментальные API. |

## sharedInstance

**sharedInstance**

#### Создать экземпляр TUIRoomEngine (паттерн одиночка).

Описание:

- Создает и возвращает глобальный общий экземпляр TUIRoomEngine (паттерн одиночка).
- Поддерживает типы комнат конференции и прямого эфира ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).
- Использование паттерна одиночка предотвращает создание дублирующихся экземпляров двигателя и экономит ресурсы.

Возвращаемое значение:

- Возвращает указатель на единственный экземпляр TUIRoomEngine.

```
// Пример использования на Java:TUIRoomEngine engine = TUIRoomEngine.sharedInstance();
```

> **Примечание** Несколько вызовов вернут один и тот же экземпляр.

## destroySharedInstance

**destroySharedInstance**

#### Уничтожить экземпляр TUIRoomEngine (паттерн одиночка).

Описание:

- Чтобы избежать неизвестных исключений после уничтожения единственного экземпляра, не рекомендуется вызывать этот интерфейс во время выполнения программы.
- Уничтожает глобальный общий экземпляр TUIRoomEngine.
- Освобождает все ресурсы, используемые двигателем.
- Если впоследствии требуется использование, необходимо повторно получить sharedInstance.

```
// Пример использования на Java:TUIRoomEngine.destroySharedInstance();
```

> **Примечание** Убедитесь, что все комнаты закрыты перед вызовом этого метода. Все функции двигателя будут недоступны после вызова этого метода. Применимо к типам комнат конференции и прямого эфира ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)) .

## login

**login**

| void login | (Context context |
| --- | --- |
|  | int sdkAppId |
|  | String userId |
|  | String userSig |
|  | TUIRoomDefine.ActionCallback callback) |

#### После создания экземпляра TUIRoomEngine следует выполнить вход с использованием sdkAppId, userId и userSig, после чего можно вызывать экземпляр TUIRoomEngine и другие функции.

Описание:

- Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).
- Если пользователь будет исключен из системы во время входа, SDK уведомит об этом через обратный вызов [onKickedOffLine](https://www.tencentcloud.com/document/product/647/54863#5dfa1251a6787bde3f2f1d1a4b1bab88) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

```
// Пример использования на Java:TUIRoomEngine.login(context, 1400000001, "user123", "xxxxxx",     new TUIRoomDefine.ActionCallback() {        @Override        public void onSuccess() {            // Обработка успешного входа         }        @Override        public void onError(int errorCode, String errorMessage) {            // Обработка ошибки входа         }    });
```

Параметры:

| Param | DESC |
| --- | --- |
| sdkAppId | Application ID. Вы можете найти SDKAppId, создав приложение в [консоли](https://console.trtc.io/) TRTC. |
| userId | User ID, уникальный идентификатор, используемый Tencent Cloud для различения пользователей. |
| userSig | Подпись пользователя, разработанная Tencent Cloud на основе UserId, используется для доступа к сервисам Tencent Cloud. Более подробно см. [UserSig](https://trtc.io/document/35166). |

> **Примечание** Вы должны успешно вызвать этот интерфейс для входа перед выполнением других операций. userId с одним и тем же SDKAppId должен быть уникальным. userSig необходимо генерировать на сервере вашего бизнеса.

## logout

**logout**

| void logout | (TUIRoomDefine.ActionCallback callback) |
| --- | --- |

#### Выход из учетной записи. Если вы находитесь в комнате, будут выполнены операции активного выхода из комнаты и освобождения ресурсов.

Описание:

- Активно выполняет выход из текущего статуса входа.
- Освобождает все ресурсы, используемые двигателем.
- Автоматически выполняет операцию выхода из комнаты, если пользователь находится в комнате.
- Для последующего использования требуется повторный вызов интерфейса входа.

```
// Пример использования на Java:TUIRoomEngine.logout(new TUIRoomDefine.ActionCallback() {    @Override    public void onSuccess() {        // Обработка успешного выхода    }    @Override    public void onError(int errorCode, String errorMessage) {        // Обработка ошибки выхода    }});
```

Параметры:

| Param | DESC |
| --- | --- |
| onError | Обратный вызов при неудачном выходе, включающий код ошибки и сообщение. |
| onSuccess | Обратный вызов при успешном выходе. |

> **Примечание** Убедитесь, что все необходимые операции очистки завершены перед вызовом этого метода. Все функции двигателя будут недоступны после вызова этого метода. Применимо к типам комнат конференции и прямого эфира ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)). Если выход не выполняется из-за проблем с сетью, рекомендуется повторить попытку или предложить пользователю проверить подключение к сети.

## setSelfInfo

**setSelfInfo**

| void setSelfInfo | (String userName |
| --- | --- |
|  | String avatarURL |
|  | TUIRoomDefine.ActionCallback callback) |

#### Обновить имя пользователя и аватар для авторизованного пользователя.

Описание:

- Устанавливает псевдоним и URL аватара локального пользователя.
- Измененная информация будет синхронизирована с другими пользователями в комнате.
- Применимо к типам комнат конференции и прямого эфира (TUIRoomTypeConference & TUIRoomTypeLive).

```
// Пример использования на Java:TUIRoomEngine.setSelfInfo("John", "https://avatar.url",      new TUIRoomDefine.ActionCallback() {         @Override         public void onSuccess() {             // Обработка успеха         }         @Override         public void onError(int errorCode, String errorMessage) {            // Обработка ошибки         }     });
```

Параметры:

| Param | DESC |
| --- | --- |
| avatarURL | Адрес URL аватара пользователя. |
| onError | Обратный вызов при неудачной операции, включающий код ошибки и сообщение. |
| onSuccess | Обратный вызов при успешной операции. |
| userName | Псевдоним пользователя. |

> **Примечание** URL аватара должен быть действительным и доступным адресом. Изменения псевдонима и аватара могут синхронизироваться

## enterRoom

**enterRoom**

| void enterRoom | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[RoomType](https://www.tencentcloud.com/document/product/647/64481#2c5219ee9c5bec4ecd3d78c97c6a3dfc) roomType |
|  | TUIRoomDefine.GetRoomInfoCallback callback) |

#### Войти в комнату.

Описание:

- Вход в указанную комнату с поддержкой двух типов комнат: конференция и прямая трансляция ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).

```
TUIRoomEngine.sharedInstance().enterRoom("room123",        TUIRoomDefine.RoomType.CONFERENCE,        new TUIRoomDefine.GetRoomInfoCallback() {    @Override    public void onSuccess(TUIRoomDefine.RoomInfo roomInfo) {        Log.d("TAG", "Enter room successfully");    }    @Override    public void onError(TUICommonDefine.Error error, String message) {        Log.e("TAG", "Failed to enter room: " + message);    }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, обратный вызов ошибки содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов ошибки (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов успеха. |
| roomId | Идентификатор комнаты, должен быть уникальным. |
| roomType | Тип комнаты (конференция/прямая трансляция). |

> **Примечание** Одно устройство может одновременно присоединиться к 1 конференц-комнате или 3 комнатам прямой трансляции. При превышении лимита самая ранняя присоединённая комната будет автоматически закрыта. Для одного аккаунта, залогиненного на нескольких устройствах, только 1 устройство может присоединиться к конференц-комнате с одинаковым ID. Другие устройства, пытающиеся присоединиться, выкинут ранее присоединённое устройство. После входа в комнату SDK уведомит пользователей в комнате через обратный вызов [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54863#823d44ecd328c1436a8d7e324c5654b1) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## enterRoom

**enterRoom**

| void enterRoom | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[RoomType](https://www.tencentcloud.com/document/product/647/64481#2c5219ee9c5bec4ecd3d78c97c6a3dfc) roomType |
|  | TUIRoomDefine.[EnterRoomOptions](https://www.tencentcloud.com/document/product/647/64481#cfb4029060d688617dbafedfa6cee5f6) options |
|  | TUIRoomDefine.GetRoomInfoCallback callback) |

#### Войти в комнату.

Описание:

- Вход в указанную комнату с поддержкой двух типов комнат: конференция и прямая трансляция ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).
- Поддерживает передачу дополнительных параметров входа в комнату через options, такие как пароль комнаты и т.д.

```
// Java Usage example:TUIRoomDefine.EnterRoomOptions options = new TUIRoomDefine.EnterRoomOptions();options.password = "***";TUIRoomEngine.sharedInstance().enterRoom("room123",     TUIRoomDefine.RoomType.CONFERENCE,     options,    new TUIRoomDefine.GetRoomInfoCallback() {        @Override        public void onSuccess(TUIRoomDefine.RoomInfo roomInfo) {            Log.d("TAG", "Enter room successfully");        }        @Override        public void onError(TUICommonDefine.Error error, String message) {            Log.e("TAG", "Failed to enter room: " + message);        }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, обратный вызов ошибки содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов ошибки (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов успеха. |
| options | Параметры входа в комнату, тип ([TUIEnterRoomOptions](https://www.tencentcloud.com/document/product/647/64481#cfb4029060d688617dbafedfa6cee5f6)). |
| roomId | Идентификатор комнаты. |
| roomType | Тип комнаты. |

> **Примечание** Одно устройство может одновременно присоединиться к 1 конференц-комнате или 3 комнатам прямой трансляции. При превышении лимита самая ранняя присоединённая комната будет автоматически закрыта. Для одного аккаунта, залогиненного на нескольких устройствах, только 1 устройство может присоединиться к конференц-комнате с одинаковым ID. Другие устройства, пытающиеся присоединиться, выкинут ранее присоединённое устройство. После входа в комнату SDK уведомит пользователей в комнате через обратный вызов [onRemoteUserEnterRoom](https://www.tencentcloud.com/document/product/647/54863#823d44ecd328c1436a8d7e324c5654b1) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## exitRoom

**exitRoom**

| void exitRoom | (boolean syncWaiting |
| --- | --- |
|  | TUIRoomDefine.ActionCallback callback) |

#### Выйти из комнаты.

Описание:

- Выход из текущей комнаты.
- Эта функция поддерживает оба типа комнат: конференция и прямая трансляция ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).
- Все потоки аудио/видео автоматически прекратят трансляцию после выхода.

```
// Java Usage example:TUIRoomEngine.sharedInstance().exitRoom(true, new TUIRoomDefine.ActionCallback() {  @Override  public void onSuccess() {    Log.d("TAG", "Exit room successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to exit room: " + message);  }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, обратный вызов ошибки содержит код ошибки и сообщение. |
| onError | (iOS) Обратный вызов ошибки (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов успеха. |
| syncWaiting | Ожидать ли синхронно возврата интерфейса. |

> **Примечание** После выхода из комнаты SDK уведомит пользователей в комнате через обратный вызов [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54863#464debb75790e0f51f4d1690fa4e4450) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## fetchRoomInfo

**fetchRoomInfo**

| void fetchRoomInfo | (TUIRoomDefine.GetRoomInfoCallback callback) |
| --- | --- |

#### Получить информацию о комнате.

Описание:

- Получить подробную информацию о текущей комнате, включая ID комнаты, имя комнаты, тип комнаты и т.д.
- Поддерживает оба типа комнат: конференция и прямая трансляция ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).

```
// Java Usage example:TUIRoomEngine.sharedInstance().fetchRoomInfo(new TUIRoomDefine.GetRoomInfoCallback() {  @Override  public void onSuccess(TUIRoomDefine.RoomInfo roomInfo) {    Log.d("TAG", "Get room info successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to get room info: " + message);  }});
```

Параметры:

- @param onSuccess(iOS) Обратный вызов при успешном получении информации о комнате, содержит информацию о комнате $TUIRoomInfo.
- @param onError(iOS) Обратный вызов ошибки (содержит код ошибки и сообщение).
- @param callback(Android/Win) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, при успехе возвращает информацию о комнате $TUIRoomInfo, при ошибке возвращает код ошибки и сообщение.

> **Примечание** Должна быть вызвана после входа в комнату. Возвращаемая информация о комнате включает базовую конфигурацию и текущее состояние. Возвращает ошибку, если вы не находитесь ни в какой комнате.

## fetchRoomInfo

**fetchRoomInfo**

| void fetchRoomInfo | (String roomId |
| --- | --- |
|  | TUIRoomDefine.[RoomType](https://www.tencentcloud.com/document/product/647/64481#2c5219ee9c5bec4ecd3d78c97c6a3dfc) roomType |
|  | TUIRoomDefine.GetRoomInfoCallback callback) |

#### Получить информацию о конкретной комнате.

Описание:

- Получить подробную информацию о конкретной комнате, включая ID комнаты, имя комнаты, тип комнаты и т.д.
- Применимо к обоим типам комнат: конференция и прямая трансляция ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).

```
// Java Usage example:TUIRoomEngine.sharedInstance().fetchRoomInfo("room123", TUIRoomDefine.RoomType.CONFERENCE, new TUIRoomDefine.GetRoomInfoCallback() {  @Override  public void onSuccess(TUIRoomDefine.RoomInfo roomInfo) {    Log.d("TAG", "Room info fetched successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to fetch room info: " + message);  }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, при успехе возвращает информацию о комнате $TUIRoomInfo, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов ошибки, содержит код ошибки и сообщение. |
| onSuccess | (iOS) Обратный вызов успеха, возвращает объект информации о комнате. |
| roomId | Идентификатор комнаты для запроса. |
| roomType | Тип комнаты (конференция/прямая трансляция). |

> **Примечание** Может быть вызвана перед входом в комнату для запроса базовой информации о комнате. Возвращаемая информация о комнате включает базовую конфигурацию и текущее состояние. Возвращает ошибку ROOM_ERROR_NOT_FOUND(1001), если комната не существует.

## updateRoomNameByAdmin

**updateRoomNameByAdmin**

| void updateRoomNameByAdmin | (String roomName |
| --- | --- |
|  | TUIRoomDefine.ActionCallback callback) |

#### Обновить имя комнаты (только для администраторов или владельца комнаты).

Описание:

- Изменить имя текущей комнаты, применимо к обоим типам комнат: конференция и прямая трансляция ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).
- После обновления имени комнаты SDK уведомит всех пользователей в комнате через обратный вызов [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54863#97fc563cec36fcde1bb0bc1b212b5c4e) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

```
// Java Usage example:TUIRoomEngine.sharedInstance().updateRoomNameByAdmin("New Room", new TUIRoomDefine.ActionCallback() {  @Override  public void onSuccess() {    Log.d("TAG", "Room name updated successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to update room name: " + message);  }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов ошибки (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов успеха. |
| roomName | Новое имя комнаты. |

> **Примечание** Только администраторы или владельцы комнаты могут вызывать этот интерфейс. После успешного изменения все пользователи в комнате получат обратный вызов [onRoomNameChanged](https://www.tencentcloud.com/document/product/647/54863#97fc563cec36fcde1bb0bc1b212b5c4e). Возвращает код ошибки, если имя комнаты содержит недопустимые символы или превышает ограничение длины.

## updateRoomSeatModeByAdmin

**updateRoomSeatModeByAdmin**

| void updateRoomSeatModeByAdmin | (TUIRoomDefine.[SeatMode](https://www.tencentcloud.com/document/product/647/54864#07121319d8ae42ebccb1761dcbe508a4) seatMode |
| --- | --- |
|  | TUIRoomDefine.ActionCallback callback) |

#### Обновить режим мест в комнате (только для администраторов или владельца комнаты).

Описание:

- Изменить режим управления местами в комнате, поддерживая режимы свободного захвата и необходимости одобрения.
- Применимо к обоим типам комнат: конференция и прямая трансляция ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) & [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).
- После обновления режима мест SDK уведомит всех пользователей в комнате через обратный вызов [onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/54863#dd614e13a79128f06065469914b9a797) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

```
// Java Usage example:TUIRoomEngine.sharedInstance().updateRoomSeatModeByAdmin(TUIRoomDefine.SeatMode.APPLY_TO_TAKE, new TUIRoomDefine.ActionCallback() {  @Override  public void onSuccess() {    Log.d("TAG", "Room seat mode updated successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to update room seat mode: " + error + ", " + message);  }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android/Win) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов ошибки (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов успеха. |
| seatMode | Режим мест [FREE_TO_TAKE](https://www.tencentcloud.com/document/product/647/64481#908781531506c53abbfa1db07153d7c1): режим свободного захвата, аудитория может захватить место без заявки.[APPLY_TO_TAKE](https://www.tencentcloud.com/document/product/647/64481#908781531506c53abbfa1db07153d7c1): режим необходимости одобрения, аудитория нуждается в одобрении администратора/владельца для захвата места. |

> **Примечание** Только администраторы или владельцы комнаты могут вызывать этот интерфейс. После изменения режима все пользователи в комнате получат обратный вызов [onRoomSeatModeChanged](https://www.tencentcloud.com/document/product/647/54863#dd614e13a79128f06065469914b9a797). Режим свободного захвата подходит для интерактивных сценариев, режим необходимости одобрения подходит для сценариев, требующих контроля разговора.

## updateRoomPasswordByAdmin

**updateRoomPasswordByAdmin**

| void updateRoomPasswordByAdmin | (String password |
| --- | --- |
|  | TUIRoomDefine.ActionCallback callback) |

#### Обновить пароль комнаты (только для администраторов или владельца комнаты).

Описание:

- Изменить пароль доступа к текущей комнате, применимо только к типу конференц-комнаты ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).
- После обновления пароля новые пользователи, присоединяющиеся к комнате, должны будут предоставить новый пароль.

```
// Java Usage example:TUIRoomEngine.sharedInstance().updateRoomPasswordByAdmin("NewPassword", new TUIRoomDefine.ActionCallback() {  @Override  public void onSuccess() {    Log.d("TAG", "Room password updated successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to update room password: " + message);  }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, при ошибке возвращает код ошибки и сообщение. |
| onError | (iOS) Обратный вызов ошибки (содержит код ошибки и сообщение). |
| onSuccess | (iOS) Обратный вызов успеха. |
| password | Новый пароль комнаты, рекомендуемая длина 8-16 символов, может включать буквы, цифры и специальные символы. |

> **Примечание** Только администраторы или владельцы комнаты могут вызывать этот интерфейс. Изменение пароля не влияет на пользователей, уже находящихся в комнате. Только типы конференц-комнаты ([CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)), не поддерживается для типа прямой трансляции ([LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).

## getRoomMetadata

**getRoomMetadata**

| void getRoomMetadata | (List<String> keys |
| --- | --- |
|  | TUIRoomDefine.GetRoomMetadataCallback callback) |

#### Получить метаданные комнаты.

Описание:

- Получить пользовательские пары ключ-значение метаданных комнаты, которые были установлены при создании комнаты или администраторами.
- Применимо только к типу комнаты прямой трансляции ([LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).

```
// Java Usage example:List<String> keys = Arrays.asList("key1", "key2");TUIRoomEngine.sharedInstance().getRoomMetadata(keys, new TUIRoomDefine.GetRoomMetadataCallback() {  @Override  public void onSuccess(HashMap<String, String> metadata) {    Log.d("TAG", "Room metadata fetched successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to fetch room metadata: " + message);  }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, при ошибке возвращает код ошибки и сообщение.Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, обратный вызов ошибки содержит код ошибки и сообщение. |
| keys | Список ключей метаданных для запроса. Передайте пустой список для получения всех метаданных. |
| onError | (iOS) Обратный вызов ошибки, содержит код ошибки и сообщение. |
| onSuccess | (iOS) Обратный вызов успеха, возвращает словарь метаданных. |

> **Примечание** Только тип комнаты прямой трансляции ([LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)) поддерживает эту функцию. Возвращаемые метаданные представлены в формате пар ключ-значение, со строковыми значениями. Пользователь должен находиться в комнате для вызова этого интерфейса.

## setRoomMetadataByAdmin

**setRoomMetadataByAdmin**

| void setRoomMetadataByAdmin | (HashMap<String, String> metadata |
| --- | --- |
|  | TUIRoomDefine.ActionCallback callback) |

#### Установить метаданные комнаты, если ключ уже существует, обновить его значение, если нет, добавить ключ.

Описание:

- Установить или обновить пользовательские пары ключ-значение метаданных комнаты, применимо только к типу комнаты прямой трансляции ([LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).
- Если указанный ключ существует, его значение будет обновлено; если нет, будет добавлена новая пара ключ-значение.
- После обновления метаданных SDK уведомит всех пользователей в комнате через обратный вызов [onRoomMetadataChanged](https://www.tencentcloud.com/document/product/647/54863#bcc8d33dab3ea6791703f3755bd5986b) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

```
// Java Usage example:HashMap<String, String> metadata = new HashMap<>();metadata.put("key1", "value1");metadata.put("key2", "value2");TUIRoomEngine.sharedInstance().setRoomMetadataByAdmin(metadata, new TUIRoomDefine.ActionCallback() {  @Override  public void onSuccess() {    Log.d("TAG", "Room metadata updated successfully");  }  @Override  public void onError(TUICommonDefine.Error error, String message) {    Log.e("TAG", "Failed to update room metadata: " + message);  }});
```

Параметры:

| Параметр | Описание |
| --- | --- |
| callback | (Android) Обратный вызов интерфейса для уведомления об успехе или неудаче вызова, обратный вызов ошибки содержит код ошибки и сообщение. |
| metadata | Пользовательские пары ключ-значение метаданных для установки, оба ключа и значения должны быть строками |
| onError | (iOS) Обратный вызов ошибки (содержит код ошибки и сообщение) |
| onSuccess | (iOS) Обратный вызов успеха |

> **Примечание** Только администраторы или владельцы комнаты могут вызывать этот интерфейс. После обновления метаданных все пользователи в комнате получат обратный вызов [onRoomMetadataChanged](https://www.tencentcloud.com/document/product/647/54863#bcc8d33dab3ea6791703f3755bd5986b). Длина ключа не может превышать 50 байт, длина значения не может превышать 200 байт. Только тип комнаты прямой трансляции ([LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db)).

## setLocalVideoView

**setLocalVideoView**

| void setLocalVideoView | (TUIVideoView view) |
| --- | --- |

#### Установить вид рендеринга предпросмотра локальной камеры.

| Параметр | Описание |
| --- | --- |
| view | Вид рендеринга. |

> **Примечание** Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## openLocalCamera

**openLocalCamera**

| void openLocalCamera | (boolean isFront |

## muteLocalAudio

**muteLocalAudio**

#### Приостановить публикацию локального аудиопотока.

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).Если вы открыли микрофон и вызвали API для приостановки публикации локального аудиопотока, SDK уведомит пользователей в комнате через обратный вызов [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54863#0d385087f48c9f2d85d650f492bacb9d) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## unmuteLocalAudio

**unmuteLocalAudio**

| void unmuteLocalAudio | (TUIRoomDefine.ActionCallback callback) |
| --- | --- |

#### Возобновить публикацию локального аудиопотока.

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).Если вы открыли микрофон и вызвали API для возобновления публикации локального аудиопотока, SDK уведомит пользователей в комнате через обратный вызов [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54863#0d385087f48c9f2d85d650f492bacb9d) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## enableSystemAudioSharing

**enableSystemAudioSharing**

| void enableSystemAudioSharing | (boolean enable) |
| --- | --- |

#### Включить совместное использование системного звука

Этот API захватывает данные системного звука с вашего устройства и смешивает их с текущим аудиопотоком SDK. Это гарантирует, что другие пользователи в комнате услышат аудио, воспроизводимое другим приложением.

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).Android: вам нужно сначала использовать этот интерфейс для включения захвата системного звука, и это вступит в силу только при вызове startScreenCapture для включения общего доступа к экрану.

## setRemoteVideoView

**setRemoteVideoView**

| void setRemoteVideoView | (String userId |
| --- | --- |
|  | TUIRoomDefine.[VideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0) streamType |
|  | TUIVideoView view) |

#### Установить представление рендеринга для удалённого пользователя.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока. Подробнее см. [VideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0). |
| userId | ID удалённого пользователя. |
| view | Представление рендеринга. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## startPlayRemoteVideo

**startPlayRemoteVideo**

| void startPlayRemoteVideo | (String userId |
| --- | --- |
|  | TUIRoomDefine.[VideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0) streamType |
|  | TUIRoomDefine.PlayCallback callback) |

#### Начать воспроизведение видеопотока удалённого пользователя.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока. Подробнее см. [VideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0). |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## stopPlayRemoteVideo

**stopPlayRemoteVideo**

| void stopPlayRemoteVideo | (String userId |
| --- | --- |
|  | TUIRoomDefine.[VideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0) streamType) |

#### Остановить воспроизведение видеопотока удалённого пользователя.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока. Подробнее см. [VideoStreamType](https://www.tencentcloud.com/document/product/647/64481#ea56a503f0706f2dc1d93ea018bddbe0). |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## muteRemoteAudioStream

**muteRemoteAudioStream**

| void muteRemoteAudioStream | (String userId |
| --- | --- |
|  | boolean isMute) |

#### Отключить аудиопоток удалённого пользователя.

| Параметр | Описание |
| --- | --- |
| isMute | true: приостановить получение аудиопотока удалённого пользователя, false: возобновить получение аудиопотока удалённого пользователя. |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## getUserList

**getUserList**

| void getUserList | (long nextSequence |
| --- | --- |
|  | TUIRoomDefine.GetUserListCallback callback) |

#### Получить список пользователей в комнате.

| Параметр | Описание |
| --- | --- |
| nextSequence | Для первого запроса указать 0, если возвращённые данные обратного вызова не равны нулю, необходимо выполнить разбиение по страницам, продолжайте операцию до достижения нулевого значения. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## getUserInfo

**getUserInfo**

| void getUserInfo | (String userId |
| --- | --- |
|  | TUIRoomDefine.GetUserInfoCallback callback) |

#### Получить информацию о пользователе.

| Параметр | Описание |
| --- | --- |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## changeUserRole

**changeUserRole**

| void changeUserRole | (String userId |
| --- | --- |
|  | TUIRoomDefine.[Role](https://www.tencentcloud.com/document/product/647/54864#f0cf468f4a2fa73a73f82e60329ae649) role |
|  | TUIRoomDefine.ActionCallback callback) |

#### Изменить роль пользователя (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| role | Роль пользователя. Подробнее см. [Role](https://www.tencentcloud.com/document/product/647/54864#f0cf468f4a2fa73a73f82e60329ae649). |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).После изменения роли пользователя SDK уведомит пользователей в комнате через обратный вызов [onUserInfoChanged](https://www.tencentcloud.com/document/product/647/54863#9df3bd61a4a7bfb3a508d114cbc99e7d) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## changeUserNameCard

**changeUserNameCard**

| void changeUserNameCard | (String userId |
| --- | --- |
|  | String nameCard |
|  | TUIRoomDefine.ActionCallback callback) |

#### Изменить прозвище пользователя в комнате (администраторы и владелец комнаты могут изменять прозвище для всех пользователей, обычные пользователи могут изменять только своё прозвище).

| Параметр | Описание |
| --- | --- |
| nameCard | Прозвище пользователя для установки, максимум 32 байта |
| userId | ID пользователя для изменения. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).После изменения прозвища пользователя SDK уведомит пользователей в комнате через обратный вызов [onUserInfoChanged](https://www.tencentcloud.com/document/product/647/54863#9df3bd61a4a7bfb3a508d114cbc99e7d) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## kickRemoteUserOutOfRoom

**kickRemoteUserOutOfRoom**

| void kickRemoteUserOutOfRoom | (String userId |
| --- | --- |
|  | TUIRoomDefine.ActionCallback callback) |

#### Удалить удалённого пользователя из комнаты (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).После удаления удалённого пользователя из комнаты SDK уведомит удалённого пользователя через обратный вызов [onKickedOutOfRoom](https://www.tencentcloud.com/document/product/647/54863#216fe07cfda9d5b3736e368c0eef69c2) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a) и уведомит пользователей в комнате через [onRemoteUserLeaveRoom](https://www.tencentcloud.com/document/product/647/54863#464debb75790e0f51f4d1690fa4e4450).

## addCategoryTagForUsers

**addCategoryTagForUsers**

| void addCategoryTagForUsers | (int tag |
| --- | --- |
|  | List<String> userList |
|  | TUIRoomDefine.ActionCallback callback) |

#### Добавить тег для пользователя (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| tag | Целочисленный тип, рекомендуется, чтобы это значение было больше или равно 1000, вы можете настроить его. |
| userList | Список пользователей. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## removeCategoryTagForUsers

**removeCategoryTagForUsers**

| void removeCategoryTagForUsers | (int tag |
| --- | --- |
|  | List<String> userList |
|  | TUIRoomDefine.ActionCallback callback) |

#### Удалить тег для пользователя (поддерживается только для владельца комнаты).

| Параметр | Описание |
| --- | --- |
| tag | Целочисленный тип, рекомендуется, чтобы это значение было больше или равно 1000, вы можете настроить его. |
| userList | Список пользователей. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## getUserListByTag

**getUserListByTag**

| void getUserListByTag | (int tag |
| --- | --- |
|  | long nextSequence |
|  | TUIRoomDefine.GetUserListCallback callback) |

#### Получить информацию о пользователе в комнате на основе тега.

| Параметр | Описание |
| --- | --- |
| nextSequence | Для первого запроса указать 0, если возвращённые данные обратного вызова не равны нулю, необходимо выполнить разбиение по страницам, продолжайте операцию до достижения нулевого значения. |
| tag | Целочисленный тип, рекомендуется, чтобы это значение было больше или равно 1000, вы можете настроить его. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## setCustomInfoForUser

**setCustomInfoForUser**

| void setCustomInfoForUser | (String userId |
| --- | --- |
|  | HashMap<String |
|  | byte[]> customInfo |
|  | TUIRoomDefine.ActionCallback callback) |

#### Установить пользовательскую информацию для пользователей комнаты.

| Параметр | Описание |
| --- | --- |
| customInfo | Пользовательская информация. |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## disableDeviceForAllUserByAdmin

**disableDeviceForAllUserByAdmin**

| void disableDeviceForAllUserByAdmin | (TUIRoomDefine.[MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21) device |
| --- | --- |
|  | boolean isDisable |
|  | TUIRoomDefine.ActionCallback callback) |

#### Владелец или администратор управляют тем, могут ли все пользователи открывать устройство. Например: все пользователи запрещены открывать микрофон (доступно только в сценарии конференции).

| Параметр | Описание |
| --- | --- |
| device | Устройство. Подробнее см.: [MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21). |
| isDisable | true: запретить пользователям открывать устройство, false: разрешить пользователям открывать устройство. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).После успешного вызова API:если тип устройства [MICROPHONE](https://www.tencentcloud.com/document/product/647/64480#726ca9fc63ac2f58472dd54daa6b022f), SDK уведомит пользователей в комнате через [onAllUserMicrophoneDisableChanged](https://www.tencentcloud.com/document/product/647/54863#15f469022d454f95f53372a83157fbbc) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).если тип устройства [CAMERA](https://www.tencentcloud.com/document/product/647/64480#726ca9fc63ac2f58472dd54daa6b022f), SDK уведомит пользователей в комнате через [onAllUserCameraDisableChanged](https://www.tencentcloud.com/document/product/647/54863#6bc81e3152578d22f10f45780fa7cb77) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).если тип устройства [SCREEN_SHARING](https://www.tencentcloud.com/document/product/647/64480#726ca9fc63ac2f58472dd54daa6b022f), SDK уведомит пользователей в комнате через [onScreenShareForAllUserDisableChanged](https://www.tencentcloud.com/document/product/647/54863#d6f2fb6b5936b7313bf9e36aa75aef9d) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## openRemoteDeviceByAdmin

**openRemoteDeviceByAdmin**

| Request openRemoteDeviceByAdmin | (String userId |
| --- | --- |
|  | TUIRoomDefine.[MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21) device |
|  | int timeout |
|  | TUIRoomDefine.RequestCallback callback) |

#### Запросить у удалённого пользователя открыть медиа-устройство (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| device | Медиа-устройство. Подробнее см.: [MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21). |
| timeout | Время ожидания в секундах. Если установлено значение 0, SDK не выполнит обнаружение тайм-аута и не вызовет обратный вызов тайм-аута. |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).После вызова API SDK уведомит запрашиваемого пользователя через [onRequestReceived](https://www.tencentcloud.com/document/product/647/54863#51c9deaee5b33b0ef9f6d5223880c667) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

#### Описание возвращаемого значения:

TUIRequest Тело запроса.

## closeRemoteDeviceByAdmin

**closeRemoteDeviceByAdmin**

| void closeRemoteDeviceByAdmin | (String userId |
| --- | --- |
|  | TUIRoomDefine.[MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21) device |
|  | TUIRoomDefine.ActionCallback callback) |

#### Закрыть медиа-устройства удалённого пользователя (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| device | Медиа-устройство. Подробнее см.: [MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21). |
| userId | ID пользователя. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).После успешного вызова API:если тип устройства [MICROPHONE](https://www.tencentcloud.com/document/product/647/64480#726ca9fc63ac2f58472dd54daa6b022f), SDK уведомит пользователей в комнате через [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/54863#0d385087f48c9f2d85d650f492bacb9d) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).если тип устройства [CAMERA](https://www.tencentcloud.com/document/product/647/64480#726ca9fc63ac2f58472dd54daa6b022f) или [SCREEN_SHARING](https://www.tencentcloud.com/document/product/647/64480#726ca9fc63ac2f58472dd54daa6b022f), SDK уведомит пользователей в комнате через [onUserVideoStateChanged](https://www.tencentcloud.com/document/product/647/54863#1b5f1be3b9eacef43456b28a335bde63) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

## applyToAdminToOpenLocalDevice

**applyToAdminToOpenLocalDevice**

| Request applyToAdminToOpenLocalDevice | (TUIRoomDefine.[MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21) device |
| --- | --- |
|  | int timeout |
|  | TUIRoomDefine.RequestCallback callback) |

#### Подать заявку на открытие локального медиа-устройства (доступно для обычных пользователей).

| Параметр | Описание |
| --- | --- |
| device | Медиа-устройство. Подробнее см.:[MediaDevice](https://www.tencentcloud.com/document/product/647/54864#63940a3d4b6af78eee8e77087330ff21). |
| timeout | Время ожидания в секундах. Если установлено значение 0, SDK не выполнит обнаружение тайм-аута и не вызовет обратный вызов тайм-аута. |

> **Примечание**Функция поддерживает только тип комнаты [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).После успешного вызова API SDK уведомит запрашиваемого пользователя через [onRequestReceived](https://www.tencentcloud.com/document/product/647/54863#51c9deaee5b33b0ef9f6d5223880c667) в [TUIRoomObserver](https://www.tencentcloud.com/document/product/647/54863#813244772a459c655a423eec84ae8f9a).

#### Описание возвращаемого значения:

TUIRequest: Тело запроса.

## getSeatList

**getSeatList**

| void getSeatList | (TUIRoomDefine.GetSeatListCallback callback) |
| --- | --- |

#### Получить список мест.

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## lockSeatByAdmin

**lockSeatByAdmin**

| void lockSeatByAdmin | (int seatIndex |
| --- | --- |
|  | TUIRoomDefine.[SeatLockParams](https://www.tencentcloud.com/document/product/647/64481#80795bda03a58adbe30293d3de33b99c) lockParams |
|  | TUIRoomDefine.ActionCallback callback) |

#### Заблокировать место (поддерживается только для администраторов или владельца комнаты).

| Параметр | Описание |
| --- | --- |
| lockParams | Параметр блокировки места. Подробнее см.: $TUISeatLockParam$. |
| seatIndex | Индекс места. |

> **Примечание**Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).Если lockParams является lockSeat, это означает, что текущее место не может быть занято никаким пользователем, и пользователь будет удалён, если место было занято.Если lockParams является lockVideo/lockAudio, это означает, что текущее место не может публиковать видео/аудиопоток.

## takeSeat

**takeSeat**

| Request takeSeat | (int seatIndex |
| --- | --- |
|  | int timeout |
|  | TUIRoomDefine.RequestCallback callback) |

#### Занять место.

| Параметр | Описание |
| --- | --- |
| seatIndex | Индекс места. Если место не включено или последовательность мест не имеет значения, просто укажите -1. |
| timeout | Время ожидания в секундах. Если установлено значение 0, SDK не выполнит обнаружение тайм-аута и не вызовет обратный вызов тайм-аута. |

> **Примечание**Функция поддерживает тип

## setWhitenessLevel

**setWhitenessLevel**

| void setWhitenessLevel | (float whitenessLevel) |
| --- | --- |

#### Установить уровень отбеливания.

| Param | DESC |
| --- | --- |
| whitenessLevel | Уровень отбеливания в диапазоне от 0 до 9; 0 означает отключение фильтра, а 9 означает наиболее очевидный эффект. |

> **Note** Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## getExtension

**getExtension**

| Object getExtension | (TUICommonDefine.[ExtensionType](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) extensionType) |
| --- | --- |

#### Получить расширение.

| Param | DESC |
| --- | --- |
| extensionType | Тип расширения. Дополнительные сведения см. в разделе [TUIExtensionType](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db). |

> **Note** Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## getMediaDeviceManager

**getMediaDeviceManager**

#### Получить класс управления устройствами.

> **Note** Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## getLiveConnectionManager

**getLiveConnectionManager**

#### Получить класс управления прямыми трансляциями.

> **Note** Функция поддерживает тип комнаты [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## getLiveBattleManager

**getLiveBattleManager**

#### Получить класс управления боевыми событиями прямой трансляции.

> **Note** Функция поддерживает тип комнаты [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).

## callExperimentalAPI

**callExperimentalAPI**

| Object callExperimentalAPI | (String jsonStr |
| --- | --- |
|  | TUIRoomDefine.ExperimentalAPIResponseCallback callback) |

#### Вызвать экспериментальные API.

> **Note** Функция поддерживает типы комнат [CONFERENCE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db) и [LIVE](https://www.tencentcloud.com/document/product/647/64480#16f14b26fa9a9f11bc07ef5be5db48db).


---
*Source: [https://trtc.io/document/54864](https://trtc.io/document/54864)*

---
*Источник (EN): [tuiroomengine.md](./tuiroomengine.md)*
