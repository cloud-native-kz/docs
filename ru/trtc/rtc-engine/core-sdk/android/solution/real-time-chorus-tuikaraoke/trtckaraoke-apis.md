# API TRTCKaraoke

`TRTCKaraokeRoom` включает следующие функции, которые основаны на Tencent Real-Time Communication (TRTC) и Tencent Cloud Chat.

- Пользователь может создать комнату караоке и стать спикером или войти в комнату караоке в качестве слушателя.
- Владелец комнаты может управлять запросами песен, а также удалять спикера с места.
- Владелец комнаты также может заблокировать место. Слушатель не может запросить доступ на заблокированное место, чтобы стать спикером.
- Слушатель может стать спикером для запроса и исполнения песен. Спикер также может стать слушателем.
- Все пользователи могут отправлять подарки и пользовательские сообщения чата. Пользовательские сообщения можно использовать для отправки комментариев на экране и лайков.

> **Примечание** Все компоненты TUIKit основаны на двух основных PaaS-сервисах Tencent Cloud, а именно [TRTC](https://intl.cloud.tencent.com/document/product/647/35078) и [Chat](https://intl.cloud.tencent.com/document/product/1047/35448). При активации TRTC пробная версия Chat SDK (поддерживающая до 100 DAU) активируется автоматически. Для получения дополнительной информации о выставлении счетов Chat см. [Тарифы](https://intl.cloud.tencent.com/document/product/1047/34350).

`TRTCKaraokeRoom` — это класс с открытым исходным кодом, который зависит от двух закрытых SDK Tencent Cloud. Конкретный процесс реализации см. в разделе [Караоке (Android)](https://intl.cloud.tencent.com/document/product/647/41941).

- [TRTC SDK](/document/product/647/35078) используется в качестве компонента аудиочата с низкой задержкой.
- Функция `AVChatRoom` [Chat SDK](https://intl.cloud.tencent.com/document/product/1047) используется для реализации чатов. API атрибутов Chat используются для сохранения информации о комнате, такой как список мест, а также сигнализация приглашений используется для отправки запросов на выступление или приглашения других к выступлению.

## Обзор API TRTCKaraokeRoom

### Основные API SDK

### API комнаты

| API | Описание |
| --- | --- |
| [createRoom](#createroom) | Создает комнату (вызывается владельцем комнаты). Если комната не существует, система автоматически создаст комнату. |
| [destroyRoom](#destroyroom) | Завершает работу комнаты (вызывается владельцем комнаты). |
| [enterRoom](#enterroom) | Входит в комнату (вызывается слушателем). |
| [exitRoom](#exitroom) | Выходит из комнаты (вызывается слушателем). |
| [getRoomInfoList](#getroominfolist) | Получает подробную информацию о списке комнат. |
| [getUserInfoList](#getuserinfolist) | Получает информацию о пользователе для указанного `userId`. Если значение равно `null`, получается информация всех пользователей в комнате. |

### API воспроизведения музыки

| API | Описание |
| --- | --- |
| [startPlayMusic](#startplaymusic) | Запускает музыку. |
| [stopPlayMusic](#stopplaymusic) | Останавливает музыку. |
| [pausePlayMusic](#pauseplaymusic) | Приостанавливает музыку. |
| [resumePlayMusic](#resumeplaymusic) | Возобновляет музыку. |

### API управления местами

| API | Описание |
| --- | --- |
| [enterSeat](#enterseat) | Становится спикером (вызывается владельцем комнаты или слушателем). |
| [leaveSeat](#leaveseat) | Становится слушателем (вызывается спикером). |
| [pickSeat](#pickseat) | Размещает пользователя на месте (вызывается владельцем комнаты). |
| [kickSeat](#kickseat) | Удаляет спикера (вызывается владельцем комнаты). |
| [muteSeat](#muteseat) | Отключает/включает звук на месте (вызывается владельцем комнаты). |
| [closeSeat](#closeseat) | Блокирует/разблокирует место (вызывается владельцем комнаты). |

### API локального аудио

| API | Описание |
| --- | --- |
| [startMicrophone](#startmicrophone) | Запускает захват с микрофона. |
| [stopMicrophone](#stopmicrophone) | Останавливает захват с микрофона. |
| [setAudioQuality](#setaudioquality) | Устанавливает качество аудио. |
| [muteLocalAudio](#mutelocalaudio) | Отключает/включает локальное аудио. |
| [setSpeaker](#setspeaker) | Устанавливает, использовать ли динамик устройства или приемник для воспроизведения аудио. |
| [setAudioCaptureVolume](#setaudiocapturevolume) | Устанавливает громкость захвата микрофона. |
| [setAudioPlayoutVolume](#setaudioplayoutvolume) | Устанавливает громкость воспроизведения. |
| [setVoiceEarMonitorEnable](#setvoiceearmonitorenable) | Включает/отключает мониторинг в наушниках. |

### API удаленного аудио

| API | Описание |
| --- | --- |
| [muteRemoteAudio](#muteremoteaudio) | Отключает/включает звук для указанного участника. |
| [muteAllRemoteAudio](#muteallremoteaudio) | Отключает/включает звук для всех участников. |

### API фоновой музыки и звуковых эффектов

| API | Описание |
| --- | --- |
| [getAudioEffectManager](#getaudioeffectmanager) | Получает объект управления фоновой музыкой и звуковыми эффектами [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__android.html#interfacecom_1_1tencent_1_1liteav_1_1audio_1_1TXAudioEffectManager). |

### API отправки сообщений

| API | Описание |
| --- | --- |
| [sendRoomTextMsg](#sendroomtextmsg) | Транслирует текстовое сообщение чата в комнате. Этот API обычно используется для комментариев на экране. |
| [sendRoomCustomMsg](#sendroomcustommsg) | Отправляет пользовательское текстовое сообщение. |

### API сигнализации приглашений

| API | Описание |
| --- | --- |
| [sendInvitation](#sendinvitation) | Отправляет приглашение. |
| [acceptInvitation](#acceptinvitation) | Принимает приглашение. |
| [rejectInvitation](#rejectinvitation) | Отклоняет приглашение. |
| [cancelInvitation](#cancelinvitation) | Отменяет приглашение. |

## Обзор API TRTCKaraokeRoomDelegate

### API обратного вызова общих событий

### API обратного вызова события комнаты

| API | Описание |
| --- | --- |
| [onRoomDestroy](#onroomdestroy) | Комната была завершена. |
| [onRoomInfoChange](#onroominfochange) | Информация о комнате изменилась. |
| [onUserVolumeUpdate](#onuservolumeupdate) | Громкость пользователя. |

### API обратного вызова изменения списка мест

| API | Описание |
| --- | --- |
| [onSeatListChange](#onseatlistchange) | Все изменения мест. |
| [onAnchorEnterSeat](#onanchorenterseat) | Пользователь стал спикером или был назначен спикером владельцем комнаты. |
| [onAnchorLeaveSeat](#onanchorleaveseat) | Пользователь стал слушателем или был назначен слушателем владельцем комнаты. |
| [onSeatMute](#onseatmute) | Владелец комнаты отключил звук на месте. |
| [onUserMicrophoneMute](#onusermicrophonemute) | Отключен ли микрофон пользователя. |
| [onSeatClose](#onseatclose) | Владелец комнаты заблокировал место. |

### API обратного вызова входа/выхода слушателя из комнаты

| API | Описание |
| --- | --- |
| [onAudienceEnter](#onaudienceenter) | Слушатель вошел в комнату. |
| [onAudienceExit](#onaudienceexit) | Слушатель вышел из комнаты. |

### API обратного вызова события сообщения

| API | Описание |
| --- | --- |
| [onRecvRoomTextMsg](#onrecvroomtextmsg) | Получено текстовое сообщение чата. |
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | Получено пользовательское сообщение. |

## API обратного вызова события сигнализации

| API | Описание |
| --- | --- |
| [onReceiveNewInvitation](#onreceivenewinvitation) | Получение приглашения. |
| [onInviteeAccepted](#oninviteeaccepted) | Приглашение принято приглашенным. |
| [onInviteeRejected](#oninviteerejected) | Приглашение отклонено приглашенным. |
| [onInvitationCancelled](#oninvitationcancelled) | Приглашающий отменил приглашение. |

### API обратного вызова события песни

| API | Описание |
| --- | --- |
| [onMusicProgressUpdate](#onmusicprogressupdate) | Прогресс воспроизведения музыки. |
| [onMusicPrepareToPlay](#onmusicpreparetoplay) | Музыка готова к воспроизведению. |
| [onMusicCompletePlaying](#onmusiccompleteplaying) | Воспроизведение музыки завершено. |

## Основные API SDK

### sharedInstance

```
 public static synchronized TRTCKaraokeRoom sharedInstance(Context context);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| context | Context | Контекст Android, который будет преобразован в `ApplicationContext` для вызова системных API. |

### destroySharedInstance

Этот API используется для завершения работы объекта-одиночки [TRTCKaraokeRoom](https://intl.cloud.tencent.com/document/product/647/41941).

> **Примечание** После завершения работы экземпляра кэшированный снаружи экземпляр `TRTCKaraokeRoom` больше нельзя использовать. Вам нужно вызвать [sharedInstance](#sharedInstance) еще раз, чтобы получить новый экземпляр.

```
public static void destroySharedInstance();
```

### setDelegate

Этот API используется для установки обратных вызовов событий [TRTCKaraokeRoom](https://intl.cloud.tencent.com/document/product/647/41941). Вы можете использовать `TRTCKaraokeRoomDelegate` для получения различных уведомлений о состоянии [TRTCKaraokeRoom](https://intl.cloud.tencent.com/document/product/647/41941).

```
public abstract void setDelegate(TRTCKaraokeRoomDelegate delegate);
```

> **Примечание** `setDelegate` — это делегат обратного вызова `TRTCKaraokeRoom`.

### setDelegateHandler

Этот API используется для установки потока, где находятся обратные вызовы событий.

```
public abstract void setDelegateHandler(Handler handler);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| handler | Handler | Уведомления о состоянии `TRTCKaraokeRoom` отправляются в поток обработчика, который вы указываете. |

### login

Вход

```
public abstract void login(int sdkAppId, String userId, String userSig,TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| sdkAppId | int | Вы можете просмотреть `SDKAppID` через [Application Management](https://console.tencentcloud.com/trtc/app) > **Application Info** в консоли TRTC. |
| userId | String | ID текущего пользователя, который представляет собой строку, содержащую только буквы (a-z и A-Z), цифры (0-9), дефисы (-) и подчеркивания (_). |
| userSig | String | Запатентованная подпись безопасности Tencent Cloud. Для получения информации о том, как ее вычислить и использовать, см. [Часто задаваемые вопросы > UserSig](https://intl.cloud.tencent.com/document/product/647/35166). |
| callback | ActionCallback | Обратный вызов для входа. Код равен `0`, если вход выполнен успешно. |

### logout

Выход

```
public abstract void logout(TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для выхода. Код равен `0`, если выход выполнен успешно. |

### setSelfProfile

Этот API используется для установки профиля.

```
public abstract void setSelfProfile(String userName, String avatarURL, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userName | String | Имя пользователя. |
| avatar | String | Адрес фотографии профиля. |
| callback | ActionCallback | Обратный вызов для конфигурации профиля. Код равен `0`, если операция выполнена успешно. |

## API комнаты

### createRoom

Этот API используется для создания комнаты (вызывается владельцем комнаты).

```
public abstract void createRoom(int roomId, TRTCKaraokeRoomDef.RoomParam roomParam, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | int | ID комнаты. Вам необходимо централизованно назначать и управлять ID комнат. Несколько значений `roomID` могут быть объединены в список комнат караоке. В настоящее время Tencent Cloud не предоставляет услуги управления списками комнат караоке. Пожалуйста, управляйте своими собственными списками комнат. |
| roomParam | TRTCCreateRoomParam | Информация о комнате, такая как имя комнаты, информация о списке мест и информация об обложке. Для управления местами вы должны ввести количество мест в комнате. |
| callback | ActionCallback | Обратный вызов для создания комнаты. Код равен `0`, если операция выполнена успешно. |

Процесс создания комнаты караоке и становления спикером выглядит следующим образом:

1. Пользователь вызывает `createRoom` для создания комнаты караоке, передав атрибуты комнаты (т.е. ID комнаты, требуется ли разрешение владельца комнаты слушателям для выступления, количество мест).
2. После создания комнаты пользователь вызывает `enterSeat` для того, чтобы стать спикером.
3. Пользователь получит уведомление `onSeatListChanget` об изменении списка мест и может обновить изменение в UI.
4. Пользователь также получит уведомление `onAnchorEnterSeat` о том, что кто-то стал спикером, и захват микрофона будет включен автоматически.

### destroyRoom

Этот API используется для завершения работы комнаты (вызывается владельцем комнаты).

```
public abstract void destroyRoom(TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для завершения работы комнаты. Код равен `0`, если операция выполнена успешно. |

### enterRoom

Этот API используется для входа в комнату (вызывается слушателем).

```
public abstract void enterRoom(int roomId, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | int | ID комнаты. |
| callback | ActionCallback | Обратный вызов для входа в комнату. Код равен `0`, если операция выполнена успешно. |

Процесс входа в комнату в качестве слушателя выглядит следующим образом:

1. Пользователь получает последний список комнат караоке с вашего сервера. Список может содержать `roomId` и информацию о комнате нескольких комнат караоке.
2. Пользователь выбирает комнату и входит в комнату, вызвав `enterRoom` с переданным ID комнаты.
3. После входа в комнату пользователь получает уведомление `onRoomInfoChange` об изменении атрибутов комнаты от компонента. Атрибуты можно записать и внести соответствующие изменения в UI, включая имя комнаты, требуется ли разрешение владельца комнаты слушателям для выступления и т.д.
4. Пользователь получит уведомление `onSeatListChange` об изменении списка мест и может обновить изменение в UI.
5. Пользователь также получит уведомление `onAnchorEnterSeat` о том, что кто-то стал спикером.

### exitRoom

Выход из комнаты

```
public abstract void exitRoom(TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для выхода из комнаты. Код равен `0`, если операция выполнена успешно. |

### getRoomInfoList

Этот API используется для получения подробной информации о списке комнат. Имя комнаты и обложка устанавливаются владельцем комнаты через `roomInfo` при вызове `createRoom()`.

> **Примечание** Вам не нужен этот API, если список комнат и информация о комнате управляются на вашем сервере.

```
public abstract void getRoomInfoList(List<Integer> roomIdList, TRTCKaraokeRoomCallback.RoomInfoCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomIdList | List<Integer> | Список ID комнат. |
| callback | RoomInfoCallback | Обратный вызов подробной информации о комнате. |

### getUserInfoList

Этот API используется для получения информации о пользователе для указанного `userId`.

```
public abstract void getUserInfoList(List<String> userIdList, TRTCKaraokeRoomCallback.UserListCallback userlistcallback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | ID пользователей для запроса. Если этот параметр равен `null`, запрашивается информация всех пользователей в комнате. |
| userlistcallback | UserListCallback | Обратный вызов подробной информации о пользователе. |

## API воспроизведения музыки

### startPlayMusic

Этот API используется для воспроизведения музыки (вызывается после того, как вы стали спикером).

> **Примечание** После начала воспроизведения музыки вы получите уведомление `onMusicPrepareToPlay`. Во время воспроизведения музыки все участники комнаты будут постоянно получать уведомление `onMusicProgressUpdate`. После прекращения воспроизведения музыки вы получите уведомление `onMusicCompletePlaying`.

```
public abstract void startPlayMusic(int musicID, String originalUrl, String accompanyUrl);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| musicID | int | ID музыки. |
| originalUrl | String | Абсолютный путь вокальной дорожки. |
| accompanyUrl | String | Абсолютный путь инструментальной дорожки. |

После вызова этого API текущая воспроизводимая песня остановится.

### stopPlayMusic

Этот API используется для остановки музыки (вызывается во время воспроизведения музыки).

> **Примечание** После прекращения воспроизведения музыки вы получите уведомление `onMusicCompletePlaying`.

```
public abstract void stopPlayMusic();
```

### pausePlayMusic

Этот API используется для приостановки музыки (вызывается во время воспроизведения музыки).

> **Примечание** Уведомление `onMusicProgressUpdate` будет приостановлено. Вы не получите уведомление `onMusicCompletePlaying`.

```
public abstract void pausePlayMusic();
```

### resumePlayMusic

Этот API используется для возобновления музыки (вызывается после приостановки воспроизведения музыки).

> **Примечание** Вы не получите уведомление `onMusicPrepareToPlay`.

```
public abstract void resumePlayMusic();
```

## API управления местами

### enterSeat

Этот API используется для того, чтобы стать спикером (вызывается владельцем комнаты или слушателем).

> **Примечание** После того как пользователь станет спикером, все пользователи в комнате получат уведомление `onSeatListChange` и уведомление `onAnchorEnterSeat`.

```
public abstract void enterSeat(int seatIndex, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места для занятия. |
| callback | ActionCallback | Обратный вызов для операции. |

Вызов этого API немедленно изменит список мест. В случаях, когда слушателям требуется разрешение владельца комнаты для того, чтобы занять место, вы можете сначала вызвать `sendInvitation` для отправки запроса и, после получения `onInvitationAccept`, вызвать этот API.

### leaveSeat

Этот API используется для того, чтобы стать слушателем (вызывается спикером).

> **Примечание** После того как спикер станет слушателем, все участники комнаты получат уведомление `onSeatListChange` и уведомление `onAnchorLeaveSeat`.

```
public abstract void leaveSeat(TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callback | ActionCallback | Обратный вызов для операции. |

### pickSeat

Этот API используется для размещения пользователя на месте (вызывается владельцем комнаты).

> **Примечание** После того как владелец комнаты назначит кого-то спикером, все участники комнаты получат уведомление `onSeatListChange` и уведомление `onAnchorEnterSeat`.

```
public abstract void pickSeat(int seatIndex, String userId, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места для размещения слушателя. |
| userId | String | ID пользователя. |
| callback | ActionCallback | Обратный вызов для операции. |

Вызов этого API немедленно изменит список мест. В случаях, когда владельцу комнаты требуется разрешение слушателей для того, чтобы назначить их спикерами, вы можете сначала вызвать `sendInvitation` для отправки запроса и, после получения `onInvitationAccept`, вызвать `pickSeat`.

### kickSeat

Этот API используется для удаления спикера (вызывается владельцем комнаты).

> **Примечание** После того как спикер удален с места, все участники комнаты получат уведомление `onSeatListChange` и уведомление `onAnchorLeaveSeat`.

```
public abstract void kickSeat(int seatIndex, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места для удаления спикера. |
| callback | ActionCallback | Обратный вызов для операции. |

Вызов этого API немедленно изменит список мест.

### muteSeat

Этот API используется для отключения/включения звука на месте (вызывается владельцем комнаты).

> **Примечание** После отключения/включения звука на месте все участники комнаты получат уведомление `onSeatListChange` и уведомление `onSeatMute`.

```
public abstract void muteSeat(int seatIndex, boolean isMute, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места для отключения/включения звука. |
| isMute | boolean | `true`: отключить звук; `false`: включить звук |
| callback | ActionCallback | Обратный вызов для операции. |

Вызов этого API немедленно изменит список мест. Спикер на месте, указанном `seatIndex`, вызовет `muteAudio` для отключения/включения звука своего аудио.

### closeSeat

Этот API используется для блокировки/разблокировки места (вызывается владельцем комнаты).

> **Примечание** После блокировки/разблокировки места все участники комнаты получат уведомление `onSeatListChange` и уведомление `onSeatClose`.

```
public abstract void closeSeat(int seatIndex, boolean isClose, TRTCKaraokeRoomCallback.ActionCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места для блокировки/разблокировки. |
| isClose | boolean | `true`: заблокировать; `false`: разблокировать |
| callback | ActionCallback | Обратный вызов для операции. |

Вызов этого API немедленно изменит список мест. Спикер на месте, указанном `seatIndex`, выйдет с места.

## API локального аудио

### startMicrophone

Этот API используется для запуска захвата с микрофона.

---
*Источник (EN): [trtckaraoke-apis.md](./trtckaraoke-apis.md)*
