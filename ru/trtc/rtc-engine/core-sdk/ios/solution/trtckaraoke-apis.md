# API TRTCKaraoke

`TRTCKaraokeRoom` основан на Tencent Real-Time Communication (TRTC) и Tencent Cloud Chat. С TRTCKaraoke:

- Пользователь может создать комнату караоке и стать спикером или войти в комнату караоке в качестве слушателя.
- Владелец комнаты может управлять заявками на песни, а также удалять спикера со своего места.
- Владелец комнаты также может заблокировать место. Слушатели не могут запросить заблокированное место.
- Слушатель может стать спикером, чтобы запросить и спеть песни. Спикер также может стать слушателем.
- Все пользователи могут отправлять подарки, текстовые сообщения и пользовательские сообщения. Пользовательские сообщения можно использовать для отправки комментариев на экран и лайков.

> **Примечание** Все компоненты TUIKit основаны на двух базовых сервисах PaaS Tencent Cloud, а именно на [TRTC](https://intl.cloud.tencent.com/document/product/647/35078) и [Chat](https://intl.cloud.tencent.com/document/product/1047/35448). При активации TRTC пробная версия Chat SDK (поддерживающая до 100 DAU) активируется автоматически. Подробные сведения о выставлении счетов для Chat см. в разделе [Цены](https://intl.cloud.tencent.com/document/product/1047/34350).

`TRTCKaraokeRoom` — это класс с открытым исходным кодом, зависящий от двух закрытых SDK Tencent Cloud. Для получения информации о конкретном процессе реализации см. [Karaoke (iOS)](https://intl.cloud.tencent.com/document/product/647/41942).

- [TRTC SDK](/document/product/647/35078) используется в качестве компонента низкозадержного аудиочата.
- Функция `AVChatRoom` в [Chat SDK](https://intl.cloud.tencent.com/document/product/1047) используется для реализации чат-комнат. API атрибутов IM используются для сохранения информации о комнате, такой как список мест, а сигнализация приглашения используется для отправки запросов на выступление или приглашения других для выступления.

## Обзор API `TRTCKaraokeRoom`

### API базовых SDK

### API комнаты

| API | Описание |
| --- | --- |
| [createRoom](#createroom) | Создает комнату (вызывается владельцем комнаты). Если комната не существует, система автоматически создаст комнату. |
| [destroyRoom](#destroyroom) | Завершает комнату (вызывается владельцем комнаты). |
| [enterRoom](#enterroom) | Входит в комнату (вызывается слушателем). |
| [exitRoom](#exitroom) | Выходит из комнаты (вызывается слушателем). |
| [getRoomInfoList](#getroominfolist) | Получает сведения о списке комнат. |
| [getUserInfoList](#getuserinfolist) | Получает информацию пользователя указанного `userId`. Если значение равно `nil`, получается информация всех пользователей в комнате. |

### API воспроизведения музыки

| API | Описание |
| --- | --- |
| [startPlayMusic](#startplaymusic) | Начинает воспроизведение музыки. |
| [stopPlayMusic](#stopplaymusic) | Останавливает воспроизведение музыки. |
| [pausePlayMusic](#pauseplaymusic) | Пауза музыки. |
| [resumePlayMusic](#resumeplaymusic) | Возобновляет воспроизведение музыки. |

### API управления местами

| API | Описание |
| --- | --- |
| [enterSeat](#enterseat) | Становится спикером (вызывается владельцем комнаты или слушателем). |
| [leaveSeat](#leaveseat) | Становится слушателем (вызывается спикером). |
| [pickSeat](#pickseat) | Помещает пользователя на место (вызывается владельцем комнаты). |
| [kickSeat](#kickseat) | Удаляет спикера (вызывается владельцем комнаты). |
| [muteSeat](#muteseat) | Отключает/включает звук места (вызывается владельцем комнаты). |
| [closeSeat](#closeseat) | Блокирует/разблокирует место (вызывается владельцем комнаты). |

### API локального аудио

| API | Описание |
| --- | --- |
| [startMicrophone](#startmicrophone) | Начинает захват микрофона. |
| [stopMicrophone](#stopmicrophone) | Останавливает захват микрофона. |
| [setAudioQuality](#setaudioquality) | Устанавливает качество звука. |
| [muteLocalAudio](#mutelocalaudio) | Отключает/включает локальный звук. |
| [setSpeaker](#setspeaker) | Устанавливает, воспроизводится ли звук с динамика или наушников устройства. |
| [setAudioCaptureVolume](#setaudiocapturevolume) | Устанавливает громкость захвата микрофона. |
| [setAudioPlayoutVolume](#setaudioplayoutvolume) | Устанавливает громкость воспроизведения. |
| [setVoiceEarMonitorEnable](#setvoiceearmonitorenable) | Включает/отключает мониторинг в наушниках. |

### API удаленного аудио

| API | Описание |
| --- | --- |
| [muteRemoteAudio](#muteremoteaudio) | Отключает/включает звук указанного участника. |
| [muteAllRemoteAudio](#muteallremoteaudio) | Отключает/включает звук всех участников. |

### API фоновой музыки и звуковых эффектов

| API | Описание |
| --- | --- |
| [getAudioEffectManager](#getaudioeffectmanager) | Получает объект управления фоновой музыкой и звуковыми эффектами [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__android.html#interfacecom_1_1tencent_1_1liteav_1_1audio_1_1TXAudioEffectManager). |

### API отправки сообщений

| API | Описание |
| --- | --- |
| [sendRoomTextMsg](#sendroomtextmsg) | Транслирует текстовое сообщение чата в комнате. Этот API обычно используется для комментариев на экране. |
| [sendRoomCustomMsg](#sendroomcustommsg) | Отправляет пользовательское текстовое сообщение чата. |

### API сигнализации приглашения

| API | Описание |
| --- | --- |
| [sendInvitation](#sendinvitation) | Отправляет приглашение. |
| [acceptInvitation](#acceptinvitation) | Принимает приглашение. |
| [rejectInvitation](#rejectinvitation) | Отклоняет приглашение. |
| [cancelInvitation](#cancelinvitation) | Отменяет приглашение. |

## Обзор API `TRTCKaraokeRoomDelegate`

### Обратные вызовы обычных событий

### API обратных вызовов событий комнаты

| API | Описание |
| --- | --- |
| [onRoomDestroy](#onroomdestroy) | Комната была завершена. |
| [onRoomInfoChange](#onroominfochange) | Информация комнаты изменилась. |
| [onUserVolumeUpdate](#onuservolumeupdate) | Громкость пользователя |

### API обратных вызовов изменения списка мест

| API | Описание |
| --- | --- |
| [onSeatListChange](#onseatlistchange) | Все изменения мест. |
| [onAnchorEnterSeat](#onanchorenterseat) | Пользователь стал спикером или был сделан спикером владельцем комнаты. |
| [onAnchorLeaveSeat](#onanchorleaveseat) | Пользователь стал слушателем или был сделан слушателем владельцем комнаты. |
| [onSeatMute](#onseatmute) | Владелец комнаты отключил звук места. |
| [onUserMicrophoneMute](#onusermicrophonemute) | Отключен ли микрофон пользователя |
| [onSeatClose](#onseatclose) | Владелец комнаты заблокировал место. |

### API обратных вызовов для входа/выхода слушателя из комнаты

| API | Описание |
| --- | --- |
| [onAudienceEnter](#onaudienceenter) | Слушатель вошел в комнату. |
| [onAudienceExit](#onaudienceexit) | Слушатель покинул комнату. |

### API обратных вызовов событий сообщений

| API | Описание |
| --- | --- |
| [onRecvRoomTextMsg](#onrecvroomtextmsg) | Получено текстовое сообщение чата. |
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | Получено пользовательское сообщение. |

### API обратных вызовов событий сигнализации

| API | Описание |
| --- | --- |
| [onReceiveNewInvitation](#onreceivenewinvitation) | Получение приглашения. |
| [onInviteeAccepted](#oninviteeaccepted) | Приглашение принято приглашаемым. |
| [onInviteeRejected](#oninviteerejected) | Приглашение отклонено приглашаемым. |
| [onInvitationCancelled](#oninvitationcancelled) | Приглашение отменено приглашающим. |

### API обратных вызовов событий музыки

| API | Описание |
| --- | --- |
| [onMusicProgressUpdate](#onmusicprogressupdate) | Прогресс воспроизведения музыки. |
| [onMusicPrepareToPlay](#onmusicpreparetoplay) | Воспроизведение музыки готово. |
| [onMusicCompletePlaying](#onmusiccompleteplaying) | Воспроизведение музыки завершено. |

## API базовых SDK

### sharedInstance

```
/*** Получить объект-одиночку `TRTCKaraokeRoom`** - возвращает: экземпляр `TRTCKaraokeRoom`* - примечание: Для завершения объекта-одиночки вызовите {@link TRTCKaraokeRoom#destroySharedInstance()}.*/+ (instancetype)sharedInstance NS_SWIFT_NAME(shared());
```

### destroySharedInstance

Этот API используется для завершения объекта-одиночки [TRTCKaraokeRoom](https://intl.cloud.tencent.com/document/product/647/41940).

> **Примечание** После завершения экземпляра кэшированный снаружи экземпляр `TRTCKaraokeRoom` больше не может использоваться. Вам нужно вызвать [sharedInstance](#sharedInstance) еще раз, чтобы получить новый экземпляр.

```
/*** Завершить объект-одиночку `TRTCKaraokeRoom`** - примечание: После завершения экземпляра кэшированный снаружи экземпляр `TRTCKaraokeRoom` больше не может использоваться. Вам нужно вызвать {@link TRTCKaraokeRoom#sharedInstance()} еще раз, чтобы получить новый экземпляр.*/+ (void)destroySharedInstance NS_SWIFT_NAME(destroyShared());
```

### setDelegate

Этот API используется для установки обратных вызовов событий [TRTCKaraokeRoom](https://intl.cloud.tencent.com/document/product/647/41940). Вы можете использовать `TRTCKaraokeRoomDelegate` для получения различных уведомлений о состоянии [TRTCKaraokeRoom](https://intl.cloud.tencent.com/document/product/647/41940).

```
/*** Установить обратные вызовы событий компонента* * Вы можете использовать `TRTCKaraokeRoomDelegate` для получения различных уведомлений о состоянии `TRTCKaraokeRoom`.** - параметр delegate API обратного вызова* - примечание: Обратные вызовы в `TRTCKaraokeRoom` по умолчанию отправляются вам в основную очередь. Если вам нужно указать очередь для обратных вызовов событий, используйте {@link TRTCKaraokeRoom#setDelegateQueue(queue)}.*/- (void)setDelegate:(id<TRTCKaraokeRoomDelegate>)delegate NS_SWIFT_NAME(setDelegate(delegate:));
```

> **Примечание** `setDelegate` — это обратный вызов делегата `TRTCKaraokeRoom`.

### setDelegateQueue

Этот API используется для установки очереди потока для обратных вызовов событий. По умолчанию используется главный поток (MainQueue).

```
/*** Установить очередь для обратных вызовов событий** - параметр queue. Уведомления о состоянии `TRTCKaraokeRoom` будут отправлены в указанную вами очередь.*/- (void)setDelegateQueue:(dispatch_queue_t)queue NS_SWIFT_NAME(setDelegateQueue(queue:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| queue | dispatch_queue_t | Уведомления о состоянии `TRTCKaraokeRoom` отправляются в указанную вами очередь потока. |

### login

Вход

```
- (void)login:(int)sdkAppID       userId:(NSString *)userId      userSig:(NSString *)userSig     callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(login(sdkAppID:userId:userSig:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| sdkAppId | int | Вы можете просмотреть `SDKAppID` через [Управление приложением](https://console.tencentcloud.com/trtc/app) > **Информация приложения** в консоли TRTC. |
| userId | String | ID текущего пользователя, это строка, которая может содержать только буквы (a-z и A-Z), цифры (0-9), дефисы (-) и подчеркивания (_). |
| userSig | String | Фирменная подпись безопасности Tencent Cloud. Для получения информации о том, как вычислить и использовать ее, см. [Часто задаваемые вопросы > UserSig](https://intl.cloud.tencent.com/document/product/647/35166). |
| callback | ActionCallback | Обратный вызов для входа. Код `0` означает, что вход успешен. |

### logout

Выход

```
- (void)logout:(ActionCallback _Nullable)callback NS_SWIFT_NAME(logout(callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для выхода. Код `0` означает, что выход успешен. |

### setSelfProfile

Этот API используется для установки профиля.

```
- (void)setSelfProfile:(NSString *)userName avatarURL:(NSString *)avatarURL callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(setSelfProfile(userName:avatarURL:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userName | String | Имя пользователя. |
| avatar | String | Адрес фотографии профиля. |
| callback | ActionCallback | Обратный вызов для конфигурации профиля. Код `0` означает, что операция успешна. |

## API комнаты

### createRoom

Этот API используется для создания комнаты (вызывается владельцем комнаты).

```
- (void)createRoom:(int)roomID roomParam:(RoomParam *)roomParam callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(createRoom(roomID:roomParam:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | int | ID комнаты. Вам нужно назначить и управлять ID комнат централизованно. Несколько значений `roomID` можно объединить в список комнат. В настоящее время Tencent Cloud не предоставляет услуги управления списками комнат. Пожалуйста, управляйте своими собственными списками комнат. |
| roomParam | TRTCCreateRoomParam | Информация о комнате, такая как название комнаты, информация о списке мест и информация о обложке. Для управления местами вы должны ввести количество мест в комнате. |
| callback | ActionCallback | Обратный вызов для создания комнаты. Код 0 означает, что операция успешна. |

Процесс создания комнаты караоке и становления спикером выглядит следующим образом:

1. Пользователь вызывает `createRoom` для создания комнаты караоке, передав атрибуты комнаты (например, ID комнаты, требуется ли разрешение владельца комнаты для слушателей, чтобы говорить, количество мест).
2. После создания комнаты пользователь вызывает `enterSeat`, чтобы стать спикером.
3. Пользователь получит уведомление `onSeatListChanget` об изменении списка мест и может обновить это изменение в UI.
4. Пользователь также получит уведомление `onAnchorEnterSeat` о том, что кто-то стал спикером, и захват микрофона будет включен автоматически.

### destroyRoom

Этот API используется для завершения комнаты (вызывается владельцем комнаты).

```
- (void)destroyRoom:(ActionCallback _Nullable)callback NS_SWIFT_NAME(destroyRoom(callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для завершения комнаты. Код `0` означает, что операция успешна. |

### enterRoom

Этот API используется для входа в комнату (вызывается слушателем).

```
- (void)enterRoom:(NSInteger)roomID callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(enterRoom(roomID:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | int | ID комнаты. |
| callback | ActionCallback | Обратный вызов для входа в комнату. Код `0` означает, что операция успешна. |

Процесс входа в комнату в качестве слушателя выглядит следующим образом:

1. Пользователь получает последний список комнат караоке с вашего сервера. Список может содержать `roomId` и информацию о комнате нескольких комнат караоке.
2. Пользователь выбирает комнату и входит в комнату, вызвав `enterRoom` с переданным ID комнаты.
3. После входа в комнату пользователь получает уведомление `onRoomInfoChange` об изменении атрибута комнаты от компонента. Атрибуты могут быть записаны, и соответствующие изменения могут быть внесены в UI, включая название комнаты, требуется ли разрешение владельца комнаты для слушателей на выступление и т. д.
4. Пользователь получит уведомление `onSeatListChange` об изменении списка мест и сможет обновить это изменение в UI.
5. Пользователь также получит уведомление `onAnchorEnterSeat` о том, что кто-то стал спикером.

### exitRoom

Выход из комнаты

```
- (void)exitRoom:(ActionCallback _Nullable)callback NS_SWIFT_NAME(exitRoom(callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для выхода из комнаты. Код `0` означает, что операция успешна. |

### getRoomInfoList

Этот API используется для получения сведений о списке комнат. Название комнаты и обложка устанавливаются владельцем комнаты через `roomInfo` при вызове `createRoom()`.

> **Примечание** Вам не нужен этот API, если список комнат и информация о комнате управляются на вашем сервере.

```
- (void)getRoomInfoList:(NSArray<NSNumber *> *)roomIdList callback:(KaraokeInfoCallback _Nullable)callback NS_SWIFT_NAME(getRoomInfoList(roomIdList:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomIdList | List<Integer> | Список ID комнат. |
| callback | RoomInfoCallback | Обратный вызов подробностей комнаты. |

### getUserInfoList

Этот API используется для получения информации о конкретных пользователях (`userId`).

```
- (void)getUserInfoList:(NSArray<NSString *> * _Nullable)userIDList callback:(KaraokeUserListCallback _Nullable)callback NS_SWIFT_NAME(getUserInfoList(userIDList:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | ID пользователей для запроса. Если этот параметр равен `null`, запрашивается информация всех пользователей в комнате. |
| userlistcallback | UserListCallback | Обратный вызов подробностей пользователя. |

## API воспроизведения музыки

### startPlayMusic

Этот API используется для воспроизведения музыки (вызывается после того, как вы становитесь спикером).

> **Примечание** После начала воспроизведения музыки вы получите уведомление `onMusicPrepareToPlay`. Во время воспроизведения музыки все члены в комнате будут постоянно получать уведомление `onMusicProgressUpdate`. После остановки воспроизведения музыки вы получите уведомление `onMusicCompletePlaying`.

```
- (void)startPlayMusic:(int32_t)musicID originalUrl:(NSString *)originalUrl accompanyUrl:(NSString *)backingUrl NS_SWIFT_NAME(startPlayMusic(musicID:originalUrl:accompanyUrl:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| musicID | int32_t | ID музыки. |
| originalUrl | String | Абсолютный путь вокального трека. |
| accompanyUrl | String | Абсолютный путь инструментального трека. |

После вызова этого API воспроизводимая песня остановится.

### stopPlayMusic

Этот API используется для остановки музыки (вызывается во время воспроизведения музыки).

> **Примечание** После остановки воспроизведения музыки вы получите уведомление `onMusicCompletePlaying`.

```
- (void)stopPlayMusic NS_SWIFT_NAME(stopPlayMusic());
```

### pausePlayMusic

Этот API используется для паузы музыки (вызывается во время воспроизведения музыки).

> **Примечание** Уведомление `onMusicProgressUpdate` будет приостановлено. Вы не получите уведомление `onMusicCompletePlaying`.

```
- (void)pausePlayMusic NS_SWIFT_NAME(pausePlayMusic());
```

### resumePlayMusic

Этот API используется для возобновления музыки (вызывается после паузы воспроизведения музыки).

> **Примечание** Вы не получите уведомление `onMusicPrepareToPlay`.

```
- (void)resumePlayMusic NS_SWIFT_NAME(resumePlayMusic());
```

## API управления местами

### enterSeat

Этот API используется для становления спикером (вызывается владельцем комнаты или слушателем).

> **Примечание** После того, как пользователь становится спикером, все члены в комнате получат уведомление `onSeatListChange` и уведомление `onAnchorEnterSeat`.

```
- (void)enterSeat:(NSInteger)seatIndex callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(enterSeat(seatIndex:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места, которое нужно занять. |
| callback | ActionCallback | Обратный вызов для операции. |

Вызов этого API немедленно изменит список мест. В случаях, когда слушателям требуется разрешение владельца комнаты для занятия места, вы можете сначала вызвать `sendInvitation` для отправки запроса и, после получения `onInvitationAccept`, вызвать этот API.

### leaveSeat

Этот API используется для становления слушателем (вызывается спикером).

> **Примечание** После того, как спикер становится слушателем, все члены в комнате получат уведомление `onSeatListChange` и уведомление `onAnchorLeaveSeat`.

```
- (void)leaveSeat:(ActionCallback _Nullable)callback NS_SWIFT_NAME(leaveSeat(callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для операции. |

### pickSeat

Этот API используется для помещения пользователя на место (вызывается владельцем комнаты).

> **Примечание** После того, как владелец комнаты сделает кого-то спикером, все члены в комнате получат уведомление `onSeatListChange` и уведомление `onAnchorEnterSeat`.

```
- (void)pickSeat:(NSInteger)seatIndex userId:(NSString *)userId callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(pickSeat(seatIndex:userId:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места для размещения слушателя. |
| userId | String | ID пользователя. |
| callback | ActionCallback | Обратный вызов для операции. |

Вызов этого API немедленно изменит список мест. В случаях, когда владельцу комнаты требуется разрешение слушателей на то, чтобы сделать их спикерами, вы можете сначала вызвать `sendInvitation` для отправки запроса и, после получения `onInvitationAccept`, вызвать `pickSeat`.

### kickSeat

Этот API используется для удаления спикера (вызывается владельцем комнаты).

> **Примечание** После удаления спикера со своего места все члены в комнате получат уведомление `onSeatListChange` и уведомление `onAnchorLeaveSeat`.

```
- (void)kickSeat:(NSInteger)seatIndex callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(kickSeat(seatIndex:callback:));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места для удаления спикера. |

---
*Источник (EN): [trtckaraoke-apis.md](./trtckaraoke-apis.md)*
