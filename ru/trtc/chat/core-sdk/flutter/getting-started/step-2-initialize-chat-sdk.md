# Шаг 2: Инициализация Chat SDK

## Описание функции

Вы **должны** инициализировать Chat SDK перед использованием его функций.

В большинстве сценариев Chat SDK требуется инициализировать только один раз в течение жизненного цикла приложения.

## Инициализация

Вы можете инициализировать SDK следующим образом:

1. Подготовьте `SDKAppID`.
2. Установите `LogLevelEnum`.
3. Установите слушатель событий SDK.
4. Вызовите `initSDK` для инициализации SDK.

Подробные шаги описаны ниже.

### Подготовка SDKAppID

Для выполнения инициализации вы должны иметь корректный

`SDKAppID`

.

`SDKAppID`

— это уникальный идентификатор, который служба Chat использует для идентификации учетной записи клиента. Рекомендуется применять новый

`SDKAppID`

для каждого независимого приложения, чтобы автоматически изолировать сообщения между

`SDKAppIDs`

.
Вы можете просмотреть все

`SDKAppIDs`

в

консоли Chat

или нажать

**Create Application**

для создания

`SDKAppID`

.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b9e1eeb0d95711efab2f5254007c27c5.png)

### Установка LogLevelEnum

Перед инициализацией SDK необходимо инициализировать объект `LogLevelEnum` ([Dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_log_level_enum/LogLevelEnum.html)), который используется для установки уровня логирования SDK.

#### Установка уровня логирования

Chat SDK поддерживает следующие уровни логирования:

| Уровень логирования | Вывод логов |
| --- | --- |
| LogLevelEnum.V2TIM_LOG_NONE | Логи не выводятся. |
| LogLevelEnum.V2TIM_LOG_DEBUG | Выводятся логи уровней DEBUG, INFO, WARNING и ERROR (уровни логирования по умолчанию). |
| LogLevelEnum.V2TIM_LOG_INFO | Выводятся логи уровней INFO, WARNING и ERROR. |
| LogLevelEnum.V2TIM_LOG_WARN | Выводятся логи уровней WARNING и ERROR. |
| LogLevelEnum.V2TIM_LOG_ERROR | Выводятся логи уровня ERROR. |

Правила хранения логов SDK следующие:

- Локальные логи Chat SDK хранятся по умолчанию в течение семи дней, и логи, созданные более семи дней назад, будут автоматически очищены при инициализации SDK.
- Для Android логи Chat SDK по умолчанию хранятся в каталоге `/sdcard/tencenet/imsdklogs/<App package name>` для версий ранее 4.8.50 и в каталоге `/sdcard/Android/data/<Package name>/files/log/tencent/imsdk` для версии 4.8.50 и позже.

Начиная с версии v4.7.1 для вывода логов Chat SDK используется модуль xlog из WeChat, который сжимает логи по умолчанию. Их необходимо распаковать с помощью скрипта Python.

- Для получения скрипта распаковки нажмите [Decode Log 27](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/tools/xlog_decoder_python27.py) (для Python 2.7) или [Decode Log 30](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/tools/xlog_decoder_python30.py) (для Python 3.0).
- В консоли Windows или Mac логи можно распаковать, выполнив следующую команду. После распаковки имена файлов заканчиваются на "xlog.log", и вы сможете открыть эти файлы в текстовом редакторе.

```
python decode_mars_nocrypt_log_file.py imsdk_yyyyMMdd.xlog
```

### Установка слушателя событий SDK

После инициализации SDK будет сообщать о таких событиях, как статус подключения и истечение билета входа через `V2TimSDKListener`.
Рекомендуется передать `V2TimSDKListener` ([Dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimSDKListener/V2TimSDKListener-class.html)) при вызове `initSDK`, чтобы добавить слушатель событий SDK и выполнить обработку логики в обратном вызове.

Обратные вызовы `V2TimSDKListener` следующие:

| Обратный вызов события | Описание события | Рекомендуемое действие |
| --- | --- | --- |
| onConnecting | SDK подключается к экземпляру CVM. | Отобразите статус "подключение" в пользовательском интерфейсе. |
| onConnectSuccess | SDK успешно подключился к экземпляру CVM. | - |
| onConnectFailed | Не удалось подключить SDK к экземпляру CVM. | Уведомите пользователя о том, что сетевое соединение в настоящее время недоступно. |
| onKickedOffline | Текущий пользователь отключен от сети. | Отобразите сообщение "Вы уже вошли на другом устройстве. Вы уверены, что хотите войти снова?" в пользовательском интерфейсе. |
| onUserSigExpired | Билет входа истек. | Войдите с новым `UserSig`. |
| onSelfInfoUpdated | Профиль текущего пользователя обновлен. | Обновите фотографию профиля и никнейм в пользовательском интерфейсе. |

> **Осторожность:** Если вы получите обратный вызов `onUserSigExpired`, UserSig, используемый вами для входа, истек. В этом случае необходимо использовать вновь выданный `UserSig` для входа. Если вы продолжите использовать истекший `UserSig`, Chat SDK войдет в бесконечный цикл входа.

### Вызов API инициализации

После выполнения вышеуказанных шагов вы можете вызвать `initSDK` ([Dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/initSDK.html)) для инициализации SDK.

Пример кода:

```
    // 1. Get the `SDKAppID` from the IM console.    int sdkAppID = 0;    // 2. Add the `V2TimSDKListener` event listener. `sdkListener` is the implementation class of `V2TimSDKListener`.    V2TimSDKListener sdkListener = V2TimSDKListener(      onConnectFailed: (int code, String error) {        // Connection failure callback function        // `code`: Error code        // `error`: Error message      },      onConnectSuccess: () {        // The SDK is successfully connected to the CVM instance      },      onConnecting: () {        // The SDK is connecting to the CVM instance      },      onKickedOffline: () {        // The current user is kicked offline: the SDK notifies the user on the UI, and the user can choose to call the login() function of V2TIMManager to log in again.      },      onSelfInfoUpdated: (V2TimUserFullInfo info) {        // The profile of the current user was updated        // `info`: information of the login user      },      onUserSigExpired: () {        // The ticket expires when the user is online: the user needs to generate a new userSig and call the login() function of V2TIMManager to log in again.      },      onUserStatusChanged: (List<V2TimUserStatus> userStatusList) {        // User status change notification        // `userStatusList`: list of users whose status changes        // Notification receiving: This callback will be triggered if a subscribed user status (including online status and custom status) changes.        // This callback will be triggered when a friend's status changes after notifications of friends' statuses are enabled in the IM console, even if the status has not been subscribed to.        // This callback will be sent to all the devices when an account is logged in on them and the custom status is changed on one of them.      },    );    // 3. Initialize the SDK    V2TimValueCallback<bool> initSDKRes =        await TencentImSDKPlugin.v2TIMManager.initSDK(      sdkAppID: sdkAppID, // SDKAppID      loglevel: LogLevelEnum.V2TIM_LOG_ALL, // Log registration level      listener: sdkListener, // Event listener    );    if (initSDKRes.code == 0) {      // Initialized successfully    }
```

// Отмена инициализации

Как правило, если жизненный цикл вашего приложения совпадает с жизненным циклом Chat SDK, вам не нужно отменять инициализацию Chat SDK перед выходом из приложения.

Однако вы можете отменить инициализацию Chat SDK в специальных случаях, например только после входа в определенный пользовательский интерфейс и более не используя его после выхода из пользовательского интерфейса.

Вы можете выполнить отмену инициализации, вызвав API отмены инициализации `unInitSDK` ([Dart](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/unInitSDK.html)).

Пример кода:

```
// Uninitialize the SDKTencentImSDKPlugin.v2TIMManager.unInitSDK();
```

## Часто задаваемые вопросы

### 1. Что делать, если при вызове функции входа или другого API возвращается код ошибки 6013 с описанием "not initialized"?

Вы должны инициализировать Chat SDK перед использованием функций входа, сообщений, групп, разговоров, цепочки отношений и профиля, а также сигнализации.


---
*Источник: [https://trtc.io/document/47966](https://trtc.io/document/47966)*

---
*Источник (EN): [step-2-initialize-chat-sdk.md](./step-2-initialize-chat-sdk.md)*
