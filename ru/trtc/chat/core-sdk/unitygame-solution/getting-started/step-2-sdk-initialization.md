# Шаг 2: инициализация SDK

## Обзор

Вы **должны** инициализировать Chat SDK перед использованием его функций.

В большинстве сценариев нужно инициализировать Chat SDK только один раз во время жизненного цикла приложения.

## Инициализация

Вы можете инициализировать SDK следующим образом:

1. Подготовьте `SDKAppID`.
2. Установите `SdkConfig`.
3. Установите слушатель событий SDK.
4. Вызовите [`Init`](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/Init.html) для инициализации SDK.

Подробные шаги описаны ниже.

### Подготовка SDKAppID

Для выполнения инициализации у вас должен быть правильный `SDKAppID`.
`SDKAppID` — это уникальный идентификатор, который служба Chat использует для идентификации учетной записи клиента. Рекомендуется запросить новый `SDKAppID` для каждого независимого приложения, чтобы автоматически изолировать сообщения между `SDKAppIDs`.
Вы можете просмотреть все `SDKAppIDs` в [консоли Chat](https://console.tencentcloud.com/im) или нажать **Create Application** для создания `SDKAppID`.

### Установка SdkConfig

Используется для настройки пути хранения журналов выполнения Chat и данных.

### sdk_config_config_file_path

Путь хранения локальных данных Chat.

> **Внимание** Приложение должно иметь права доступа на чтение и запись к этому пути.

### sdk_config_log_file_path

Это путь хранения журналов Chat.

> **Внимание** Приложение должно иметь права доступа на чтение и запись к этому пути.

### Вызов API инициализации

После выполнения вышеуказанных шагов вы можете вызвать [`Init`](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/Init.html) для инициализации SDK.

Пример кода:

```
namespace Com.Tencent.IM.Unity.UIKit{    public static void Init() {        string sdkappid = ""; // Get the `SDKAppID` from the IM console        SdkConfig sdkConfig = new SdkConfig();        sdkConfig.sdk_config_config_file_path = Application.persistentDataPath + "/TIM-Config";        sdkConfig.sdk_config_log_file_path = Application.persistentDataPath + "/TIM-Log";        TIMResult res = TencentIMSDK.Init(long.Parse(sdkappid), sdkConfig);    }}
```

### Регистрация слушателя глобальных событий SDK

После инициализации SDK будет выбрасывать события, такие как статус подключения и истечение срока действия билета входа, через [`NetworkStatusListenerCallback`](https://comm.qq.com/im/doc/unity/zh/callback/NetworkStatusListenerCallback.html), [`UserSigExpiredCallback`](https://comm.qq.com/im/doc/unity/zh/callback/UserSigExpiredCallback.html) и другие обратные вызовы.
Рекомендуется зарегистрировать слушатель глобальных событий сразу после вызова `initSDK` и выполнить обработку логики в таких обратных вызовах.

Обратные вызовы описаны ниже:

| Обратный вызов события | Описание |
| --- | --- |
| [RecvNewMsgCallback](https://comm.qq.com/im/doc/unity/zh/callback/RecvNewMsgCallback.html) | Обратный вызов для получения нового сообщения |
| [MsgReadedReceiptCallback](https://comm.qq.com/im/doc/unity/zh/callback/MsgReadedReceiptCallback.html) | Обратный вызов для подтверждения прочтения сообщения |
| [MsgRevokeCallback](https://comm.qq.com/im/doc/unity/zh/callback/MsgRevokeCallback.html) | Обратный вызов для отзыва сообщения |
| [MsgElemUploadProgressCallback](https://comm.qq.com/im/doc/unity/zh/callback/MsgElemUploadProgressCallback.html) | Обратный вызов для отслеживания прогресса загрузки элемента сообщения |
| [GroupTipsEventCallback](https://comm.qq.com/im/doc/unity/zh/callback/GroupTipsEventCallback.html) | Обратный вызов для системного сообщения группы |
| [GroupAttributeChangedCallback](https://comm.qq.com/im/doc/unity/zh/callback/GroupAttributeChangedCallback.html) | Обратный вызов для изменения атрибутов группы |
| [ConvTotalUnreadMessageCountChangedCallback](https://comm.qq.com/im/doc/unity/zh/callback/ConvTotalUnreadMessageCountChangedCallback.html) | Обратный вызов для изменения количества непрочитанных сообщений в беседе |
| [NetworkStatusListenerCallback](https://comm.qq.com/im/doc/unity/zh/callback/NetworkStatusListenerCallback.html) | Обратный вызов для отслеживания статуса подключения к сети |
| [KickedOfflineCallback](https://comm.qq.com/im/doc/unity/zh/callback/KickedOfflineCallback.html) | Обратный вызов для отключения в режиме «вне сети» |
| [UserSigExpiredCallback](https://comm.qq.com/im/doc/unity/zh/callback/UserSigExpiredCallback.html) | Обратный вызов для истечения срока действия билета |
| [OnAddFriendCallback](https://comm.qq.com/im/doc/unity/zh/callback/OnAddFriendCallback.html) | Обратный вызов для добавления друга |
| [OnDeleteFriendCallback](https://comm.qq.com/im/doc/unity/zh/callback/OnDeleteFriendCallback.html) | Обратный вызов для удаления друга |
| [UpdateFriendProfileCallback](https://comm.qq.com/im/doc/unity/zh/callback/UpdateFriendProfileCallback.html) | Обратный вызов для обновления профиля друга |
| [FriendAddRequestCallback](https://comm.qq.com/im/doc/unity/zh/callback/FriendAddRequestCallback.html) | Обратный вызов для запроса добавления друга |
| [FriendApplicationListDeletedCallback](https://comm.qq.com/im/doc/unity/zh/callback/FriendApplicationListDeletedCallback.html) | Обратный вызов для удаления запроса добавления друга |
| [FriendApplicationListReadCallback](https://comm.qq.com/im/doc/unity/zh/callback/FriendApplicationListReadCallback.html) | Обратный вызов для чтения запроса добавления друга |
| [FriendBlackListAddedCallback](https://comm.qq.com/im/doc/unity/zh/callback/FriendBlackListAddedCallback.html) | Обратный вызов для добавления друга в черный список |
| [FriendBlackListDeletedCallback](https://comm.qq.com/im/doc/unity/zh/callback/FriendBlackListDeletedCallback.html) | Обратный вызов для удаления друга из черного списка |
| [LogCallback](https://comm.qq.com/im/doc/unity/zh/callback/LogCallback.html) | Обратный вызов логирования |
| [MsgUpdateCallback](https://comm.qq.com/im/doc/unity/zh/callback/MsgUpdateCallback.html) | Обратный вызов для обновления сообщения |
| [MsgGroupMessageReadMemberListCallback](https://comm.qq.com/im/doc/unity/zh/callback/MsgGroupMessageReadMemberListCallback.html) | Обратный вызов для получения списка участников группы, которые прочитали групповое сообщение |

> **Внимание** Если вы получите обратный вызов [`UserSigExpiredCallback`](https://comm.qq.com/im/doc/unity/zh/callback/UserSigExpiredCallback.html), это означает, что истек срок действия `UserSig`, используемый вами для входа. В этом случае необходимо использовать заново выданный `UserSig` для повторного входа. Если вы продолжите использовать истекший `UserSig`, Chat SDK войдет в бесконечный цикл входа.

// Деинициализация

Как правило, если жизненный цикл вашего приложения совпадает с жизненным циклом Chat SDK, вам не нужно деинициализировать Chat SDK перед выходом из приложения.

Однако в специальных случаях вы можете деинициализировать Chat SDK, например только после входа в определенный интерфейс и прекращения его использования при выходе из интерфейса.

Вы можете выполнить деинициализацию путем вызова API деинициализации [`unInit`](https://comm.qq.com/im/doc/unity/zh/api/IMSDKInit/Uninit.html).

Пример кода:

```
// Uninitialize the SDKTencentIMSDK.Uninit();
```

## Прочее

Используется для отображения результата, возвращаемого при вызове SDK. Когда `res` имеет значение `TIMResult.TIM_SUCC = 0`, вызов API выполнен успешно.

После успешной инициализации SDK добавьте необходимые слушатели, чтобы не пропустить сообщения.

## Часто задаваемые вопросы

### 1. Вы должны инициализировать Chat SDK перед использованием входа, сообщений, групп, бесед, цепочек отношений и профилей, а также функций сигнализации.


---
*Источник: [https://trtc.io/document/48570](https://trtc.io/document/48570)*

---
*Источник (EN): [step-2-sdk-initialization.md](./step-2-sdk-initialization.md)*
