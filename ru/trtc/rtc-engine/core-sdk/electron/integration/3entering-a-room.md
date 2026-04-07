# 3. Вход в комнату

Этот документ описывает, как войти в комнату TRTC. Только после входа в комнату аудио/видео пользователь может подписаться на аудио/видео потоки других пользователей в комнате или опубликовать свои собственные аудио/видео потоки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/34552cda37fc11ed8088525400463ef7.png)

## Руководство вызова

### Шаг 1. Импортируйте SDK

Импортируйте SDK в соответствии с инструкциями в [Electron](https://intl.cloud.tencent.com/document/product/647/35097).

### Шаг 2. Создайте экземпляр SDK

```
import TRTCCloud from 'trtc-electron-sdk';const rtcCloud = new TRTCCloud();
```

### Шаг 3. Слушайте события SDK

```
function onError(errCode, errMsg) {  // For information on the error codes, see https://intl.cloud.tencent.com/document/product/647/35124#error-codes  console.log(errCode, errMsg);}function onWarning(warningCode, warningMsg) {  // For information on the warning codes, see https://intl.cloud.tencent.com/document/product/647/35124#warning-codes  console.log(warningCode, warningMsg);}rtcCloud.on('onError', onError);rtcCloud.on('onWarning', onWarning);
```

### Шаг 4. Соберите параметр входа в комнату `TRTCParams`

#### Параметр 1: TRTCAppScene

Этот параметр используется для указания того, является ли сценарий вашего приложения **трансляцией в прямом эфире** или **общением в реальном времени**.

- Для **вызовов в реальном времени** установите параметр на `TRTCAppSceneVideoCall` (видеозвонок) или `TRTCAppSceneAudioCall` (аудиозвонок). Этот режим подходит для общения один-на-один через аудио/видео или онлайн-встреч с участием до 300 человек.
- Для **трансляции в прямом эфире** установите параметр на `TRTCAppSceneLIVE` (видеотрансляция) или `TRTCAppSceneVoiceChatRoom` (аудиотрансляция). Этот режим подходит для трансляции до 100 000 пользователей. Убедитесь, что вы указали поле **role** (допустимые значения: **anchor**, **audience**) в `TRTCParams`, если вы используете этот режим.

#### Параметр 2: TRTCParams

`TRTCParams` состоит из множества полей; однако обычно вам нужно обращать внимание только на следующие поля:

| Параметр | Описание | Замечания | Тип данных | Пример значения |
| --- | --- | --- | --- | --- |
| SDKAppID | ID приложения | Вы можете просмотреть ID приложения в [консоли TRTC](https://console.tencentcloud.com/trtc/app). Если у вас еще нет приложения, нажмите **Create application** для создания. | Number | 1400000123 |
| userId | ID пользователя | Может содержать только буквы, цифры, подчеркивания и дефисы. В TRTC пользователь не может использовать один и тот же ID пользователя для входа в одну и ту же комнату на двух разных устройствах одновременно. | String | `denny` или `123321` |
| userSig | Билет аутентификации, необходимый для входа в комнату | `userSig` рассчитывается на основе `userId` и `SDKAppID`. Метод расчета см. в [UserSig](https://intl.cloud.tencent.com/document/product/647/35166). | String | eJyrVareCeYrSy1SslI... |
| roomId | ID комнаты | Числовой ID комнаты. Если вы хотите использовать строковые ID комнат, укажите **strRoomId**. Не используйте `strRoomId` и `roomId` одновременно. | Number | 29834 |
| strRoomId | ID комнаты | Строковый ID комнаты. Не используйте `strRoomId` и `roomId` одновременно. Значения `"123"` и `123` рассматриваются бэкендом TRTC как разные комнаты. | String | "29834" |
| role | Роль | Есть две роли: якорь и аудитория. Это поле требуется только в том случае, если `TRTCAppScene` установлен на сценарии прямой трансляции `TRTCAppSceneLIVE` или `TRTCAppSceneVoiceChatRoom`. | Enumeration | `TRTCRoleAnchor` или `TRTCRoleAudience` |

> **Примечание**: В TRTC пользователь не может использовать один и тот же `userId` для входа в одну и ту же комнату на двух разных устройствах одновременно; в противном случае произойдет конфликт. Значение `appScene` должно быть одинаковым на каждом клиенте. Несогласованное `appScene` может привести к непредвиденным проблемам.

### Шаг 5. Войдите в комнату (`enterRoom`)

```
import { TRTCParams, TRTCRoleType, TRTCAppScene } from 'trtc-electron-sdk';const param = new TRTCParams();param.sdkAppId = 1400000123;param.userId = "denny";  param.roomId = 123321;param.userSig = "xxx";param.role = TRTCRoleType.TRTCRoleAnchor;// If your scenario is live streaming, set the application scenario to `TRTC_APP_SCENE_LIVE`rtcCloud.enterRoom(param, TRTCAppScene.TRTCAppSceneLIVE);
```

**Обратные вызовы:**

- Если вход в комнату выполнен успешно, SDK вызовет обратный вызов события `onEnterRoom(result)`, и значение `result` будет больше 0, указывая время в миллисекундах, затраченное на вход в комнату.
- Если вход в комнату не удался, SDK также вызовет обратный вызов события `onEnterRoom(result)`, но значение `result` будет отрицательным числом, указывающим код ошибки при неудачном входе в комнату.

```
function onEnterRoom(result) {  // For details about `onEnterRoom`, see https://web.sdk.qcloud.com/trtc/electron/doc/en/trtc_electron_sdk/TRTCCallback.html#event:onEnterRoom  if (result > 0) {    console.log('Enter room succeed');  } else {    // For room entry error codes, see https://intl.cloud.tencent.com/document/product/647/35124    console.log('Enter room failed');  }}rtcCloud.on('onEnterRoom', onEnterRoom);
```


---
*Источник: [https://trtc.io/document/48049](https://trtc.io/document/48049)*

---
*Источник (EN): [3entering-a-room.md](./3entering-a-room.md)*
