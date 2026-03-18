# Быстрая интеграция

## Обзор

TUIKaraoke — это компонент UI для аудио/видео на основе открытого исходного кода, который вы можете интегрировать в свой проект, чтобы добавить в приложение онлайн-караоке, управление местами, дарение/получение подарков, текстовый чат и другие функции TRTC. TUIKaraoke требует всего несколько строк кода и также поддерживает платформу Android. Его основные функции показаны ниже:

> **Примечание** Все компоненты TUIKit основаны на двух базовых сервисах PaaS Tencent Cloud, а именно на [TRTC](https://intl.cloud.tencent.com/document/product/647/35078) и [Chat](https://intl.cloud.tencent.com/document/product/1047/35448). При активации TRTC пробная версия Chat SDK (поддерживающая до 100 DAU) также активируется автоматически. Подробнее о выставлении счетов за Chat см. в разделе [Pricing](https://intl.cloud.tencent.com/document/product/1047/34350).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/efa3bd2d38bd11edb1de525400c56988.png)

## Интеграция

### Шаг 1. Загрузка и импорт компонента `TUIKaraoke`

Перейдите на [GitHub](https://github.com/tencentyun/TUIKaraoke), клонируйте или загрузите код, скопируйте папки `Source`, `Resources` и `TXAppBasic`, а также файл `TUIKaraoke.podspec` из директории `iOS` в ваш проект и выполните следующие операции импорта:

- Добавьте следующие команды импорта в ваш `Podfile`:

```
pod 'TUIKaraoke', :path => "./", :subspecs => ["TRTC"]pod 'TXLiteAVSDK_TRTC'pod 'TXAppBasic', :path => "TXAppBasic/"
```

- Откройте Terminal и выполните следующую команду установки в директории `Podfile`:

```
pod install
```

### Шаг 2. Конфигурация разрешений

Сконфигурируйте запросы разрешений для приложения в файле `info.plist` вашего проекта. SDK требуют следующих разрешений (на iOS доступ к микрофону должен запрашиваться во время выполнения):

```
 <key>NSMicrophoneUsageDescription</key>    <string>`TUIKaraoke` требует доступ к вашему микрофону.</string>
```

### Шаг 3. Инициализация и вход в компонент

Дополнительные сведения о соответствующих API см. в разделе [TRTCKaraoke (iOS)](https://intl.cloud.tencent.com/document/product/647/41942).

```
  // 1. Инициализация  let karaokeRoom = TRTCKaraokeRoom.shared()  karaokeRoom.setDelegate(delegate: self)  // 2. Вход  karaokeRoom.login(SDKAppID: Int32(SDKAppID), UserId: UserId, UserSig: ProfileManager.shared.curUserSig()) { code, message in        if code == 0 {            // Вход выполнен        }  }
```

**Описание параметров:**

- **SDKAppID**: **ID приложения TRTC**. Если вы еще не активировали TRTC, войдите в [консоль TRTC](https://console.tencentcloud.com/trtc/app), создайте приложение TRTC, нажмите **Application Info**, информация `SDKAppID` отображается на рисунке ниже:
![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/415d3224b5d011eeb2a1525400170219.png)
- **SecretKey**: **Ключ приложения TRTC**. Каждому `SDKAppID` соответствует ключ. Вы можете просмотреть ключ приложения на странице [Application Management](https://console.tencentcloud.com/trtc/app) консоли TRTC.
- **userId**: ID текущего пользователя, это пользовательская строка, которая может содержать до 32 байт букв и цифр (специальные символы не поддерживаются).
- **userSig**: Защитная подпись безопасности, вычисленная на основе `SDKAppID`, `userId` и `Secretkey`. Вы можете щелкнуть [здесь](https://console.trtc.io/usersig), чтобы напрямую создать отладочный `userSig` онлайн. Дополнительные сведения см. в разделе [UserSig](https://intl.cloud.tencent.com/document/product/647/35166).

### Шаг 4. Реализация сценария онлайн-караоке

1. **Владелец комнаты создает комнату через**[TUIKaraoke.createRoom](https://intl.cloud.tencent.com/document/product/647/41942).

```
int roomId = "ID комнаты";let param = RoomParam.init()param.roomName = "Название комнаты";param.needRequest = false; // Требуется ли разрешение для того, чтобы слушатели могли говорить.param.seatCount = 8;       // Количество мест в комнате. Установите значение `8`.param.coverUrl = "URL изображения обложки комнаты";karaokeRoom.createRoom(roomID: Int32(roomInfo.roomID), roomParam: param) { [weak self] (code, message) in guard let `self` = self else { return } if code == 0 {     // Комната успешно создана }}
```

2. **Слушатель входит в комнату через**[TUIKaraoke.enterRoom](https://intl.cloud.tencent.com/document/product/647/41942).

```
karaokeRoom.enterRoom(roomID: roomInfo.roomID) { [weak self] (code, message) in guard let `self` = self else { return } if code == 0 {     // Вход в комнату выполнен успешно }}
```

3. **Слушатель включает свой микрофон через**[TUIKaraoke.enterSeat](https://intl.cloud.tencent.com/document/product/647/41942).

```
// 1. Слушатель вызывает API для включения микрофонаint seatIndex = 1; karaokeRoom.enterSeat(seatIndex: seatIndex) { [weak self] (code, message) in guard let `self` = self else { return } if code == 0 {     // Микрофон успешно включен }}// 2. Слушатель получает обратный вызов `onSeatListChange` и обновляет список мест.func onSeatListChange(seatInfoList: [SeatInfo]) {}
```

> **Примечание** Вы можете реализовать другие операции управления местами согласно инструкциям в разделе [TRTCKaraoke (iOS)](https://intl.cloud.tencent.com/document/product/647/41942) или со ссылкой на [демо-проект TUIKaraoke](https://github.com/tencentyun/TUIKaraoke/).

4. **Воспроизведение песен и опробование сценария караоке**
Вы можете получить ID музыки и URL для воспроизведения песни. Дополнительные сведения см. в разделе [Music Playback APIs](https://www.tencentcloud.com/document/product/647/41942#music-playback-apis2).

```
// Воспроизведение музыкиkaraokeRoom.startPlayMusic(musicID: musicID, originalUrl: muscicLocalPath, accompanyUrl: accompanyLocalPath);// Остановка музыкиkaraokeRoom.stopPlayMusic();
```

После завершения предыдущих шагов вы можете реализовать базовые функции караоке. Если вашему бизнесу требуются дополнительные функции, такие как чат и дарение подарков, вы можете интегрировать следующие возможности:

### Шаг 5. Добавление функции текстового чата (опционально)

Если вы хотите реализовать функцию текстового чата между ораторами и слушателями, реализуйте отправку/получение сообщений следующим образом:
Дополнительные сведения о соответствующих API см. в разделе [sendRoomTextMsg](https://intl.cloud.tencent.com/document/product/647/41942#sendroomtextmsg).

```
// Отправитель: отправляет текстовые сообщения чатаkaraokeRoom.sendRoomTextMsg(message: message) { [weak self] (code, message) in    if code == 0 {        // Успешно отправлено    }}// Получатель: прослушивает текстовые сообщения чатаkaraokeRoom.setDelegate(delegate: self)func onRecvRoomTextMsg(message: String, userInfo: UserInfo) {    debugPrint("Получено сообщение от " + userInfo.userName + ": " + message)}
```

### Шаг 6. Добавление функции дарения подарков (опционально)

Вы можете реализовать дарение, получение и отображение подарков следующим образом:

```
// Отправитель: настройте `IMCMD_GIFT` для различия между сообщениями о подарках.karaokeRoom.sendRoomCustomMsg(cmd: kSendGiftCmd, message: message) { code, msg in    if (code == 0) {        // Успешно отправлено    }}// Получатель: прослушивает сообщения о подарках.karaokeRoom.setDelegate(delegate: self)func onRecvRoomCustomMsg(cmd: String, message: String, userInfo: UserInfo) {    if cmd == kSendGiftCmd {        debugPrint("Получено подарок от " + userInfo.userName + ": " + message)    }}
```

## Часто задаваемые вопросы

### Поддерживает ли компонент `TUIKaraoke` функции звуковых эффектов, такие как изменение голоса, изменение тональности и реверберация?

Да. Дополнительные сведения см. в [демо-проекте TUIKaraoke](https://github.com/tencentyun/TUIKaraoke/blob/main/iOS/Source/ui/TRTCKTVViewController/SubViews/TRTCKaraokeSoundEffectAlert.swift).

> **Примечание** Если у вас есть предложения или отзывы, пожалуйста, свяжитесь с нами по адресу colleenyu@tencent.com.


---
*Источник: [https://trtc.io/document/41940](https://trtc.io/document/41940)*

---
*Источник (EN): [quick-integration.md](./quick-integration.md)*
