# Шаг 3: Вход и выход

## Обзор

После инициализации Chat SDK необходимо вызвать API входа SDK для аутентификации вашей учетной записи, чтобы получить разрешения на использование сообщений, диалогов и других функций.

> **Осторожно:** Только API получения диалога может быть вызван сразу после вызова API входа, а другие API могут быть вызваны только после успешного входа в SDK. Поэтому **убедитесь, что вы успешно вошли в систему** перед использованием других функций; в противном случае эти функции могут работать ненормально или быть недоступны.

## Вход

Вам не нужно регистрироваться при первом входе, так как вы будете автоматически зарегистрированы в случае успешного входа.
Вы можете вызвать API `login` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/login.html)) для входа.

Ключевые параметры API `login`:

| Параметр | Описание | Примечания |
| --- | --- | --- |
| UserID | Уникальный идентификатор пользователя | Может содержать до 32 байт букв (a-z и A-Z), цифр (0-9), подчеркиваний (_) и дефисов (-). |
| UserSig | Билет входа. | Вычисляется вашим сервером приложения в целях безопасности. Для получения дополнительной информации о методе расчета см. [Генерирование UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |

Вы можете вызвать API `login` в следующих сценариях:

- Когда вы используете функции Chat SDK впервые после запуска приложения.
- Срок действия билета истёк перед входом: обратный вызов API `login` возвращает ошибку `ERR_USER_SIG_EXPIRED` (6206) или `ERR_SVR_ACCOUNT_USERSIG_EXPIRED` (70001), и вам необходимо сгенерировать новый userSig и войти снова.
- Срок действия билета истёк при попытке входа в сеть: Вы можете получить обратный вызов `onUserSigExpired` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimSDKListener/V2TimSDKListener/onUserSigExpired.html)) при входе в сеть. В этом случае вам необходимо сгенерировать новый `userSig` и войти снова.
- Пользователь отключен от сети: Когда пользователь отключен от сети, Chat SDK уведомляет вас через обратный вызов `onKickedOffline` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimSDKListener/V2TimSDKListener/onKickedOffline.html)). В этом случае вы можете предупредить пользователя и вызвать `login` для входа снова.

Вам не нужно вызывать API `login` в следующих сценариях:

- Когда ваше сетевое соединение разорвано, а затем восстановлено. В этом случае SDK автоматически выходит в сеть.
- Когда уже запущен процесс входа. В этом случае повторный вход не требуется.

> **Примечание:** После вызова API Chat SDK и успешного входа начнется расчет DAU; поэтому вызывайте API входа по мере необходимости, чтобы избежать высокого DAU. Вы не можете одновременно войти в несколько учетных записей Chat SDK одного приложения; в противном случае в сети будет только последняя введенная учетная запись.

Пример кода:

```
String userID = "your user id";String userSig = "userSig from your server";V2TimCallback res = await TencentImSDKPlugin.v2TIMManager.login(userID: userID, userSig: userSig);if(res.code == 0){    // Logic for successful login}else{     // Logic for failed login}
```

### Получение пользователя, вошедшего в систему

После успешного входа вызовите API `getLoginUser` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getLoginUser.html)) для получения `UserID`.
Если вход не удался, `UserID` будет пустым.

Пример кода:

```
    // After successful login,    // call `getLoginUser` to get the `UserID`.    V2TimValueCallback<String> getLoginUserRes =        await TencentImSDKPlugin.v2TIMManager.getLoginUser();    if (getLoginUserRes.code == 0) {      // Obtained successfully      getLoginUserRes.data; // `getLoginUserRes.data` gets the `UserID` of the login user    }
```

### Получение статуса входа

Вызовите API `getLoginStatus` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/getLoginStatus.html)) для получения статуса входа. Если пользователь вошел в систему или входит в систему, не вызывайте API входа часто. Chat SDK поддерживает следующие статусы входа:

| Статус входа | Описание |
| --- | --- |
| V2TIM_STATUS_LOGINED (1) | Вошел в систему |
| V2TIM_STATUS_LOGINING (2) | Вход в систему |
| V2TIM_STATUS_LOGOUT (3) | Не вошел в систему |

Пример кода:

```
    // After successful login,    // call `getLoginStatus` to get the status of the login user.    V2TimValueCallback<int> getLoginStatusRes =        await TencentImSDKPlugin.v2TIMManager.getLoginStatus();    if (getLoginStatusRes.code == 0) {      int? status = getLoginStatusRes.data; // `getLoginStatusRes.data` gets the user's login status value.      if (status == 1) {        // Logged in      } else if (status == 2) {        // Logging in      } else if (status == 3) {        // Not logged in      }    }
```

## Вход с нескольких клиентов и отключение

Вы можете настроить политики входа с нескольких клиентов для Chat SDK в консоли Tencent Cloud.
Существует несколько политик входа с нескольких клиентов, таких как **пользователь может одновременно находиться в сети на мобильной, настольной платформе и веб-платформе** или **пользователь может одновременно находиться в сети на всех платформах**.
Соответствующие конфигурации см. в разделе [Параметры входа](https://intl.cloud.tencent.com/document/product/1047/34419).

Вы можете настроить **максимальное количество экземпляров входа на одного пользователя на одну платформу** для Chat SDK в консоли Tencent Cloud, то есть максимальное количество экземпляров на одной платформе, которые могут одновременно находиться в сети.

Эта функция доступна только для Pro, Pro Plus или Enterprise версий. Пользователь может одновременно находиться в сети на максимум десяти клиентов на веб-платформе или на максимум трех клиентах на платформах Android, iPhone, iPad, Windows или macOS (максимальное количество клиентов, которые могут одновременно находиться в сети на Flutter, зависит от фактического результата компиляции).

Соответствующие конфигурации см. в разделе [Параметры входа](https://intl.cloud.tencent.com/document/product/1047/34419).

При вызове API `login` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/login.html)) для входа, если лимит, установленный политикой входа с нескольких клиентов для вашей учетной записи, превышен, новый вошедший экземпляр отключит более ранний.

Отключенный экземпляр получит обратный вызов `onKickedOffline` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/enum_V2TimSDKListener/V2TimSDKListener/onKickedOffline.html)).

## Выход

Как правило, если жизненный цикл вашего приложения совпадает с жизненным циклом Chat SDK, перед выходом из приложения нет необходимости выходить из системы.
В особых случаях, например, если вы используете Chat SDK только после входа в определенный интерфейс и больше не используете его после выхода из интерфейса, вы можете вызвать API `logout` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/logout.html)) для выхода из SDK, после чего вы больше не будете получать новые сообщения. Обратите внимание, что в этом случае вам также необходимо вызвать `unInitSDK` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/unInitSDK.html)) после выхода для отмены инициализации SDK.

Пример кода:

```
V2TimCallback logoutRes = await TencentImSDKPlugin.v2TIMManager.logout();if(logoutRes.code == 0){}
```

## Переключение учетной записи

Вызовите `login` ([подробнее](https://pub.dev/documentation/tencent_cloud_chat_sdk/latest/manager_v2_tim_manager/V2TIMManager/login.html)) для переключения между учетными записями в приложении.

Например, чтобы переключить вошедшего пользователя с `alice` на `bob`, просто войдите под учетной записью bob. Вам не нужно явно вызывать `logout alice`, так как эта операция будет обработана автоматически внутри Chat SDK.


---
*Источник: [https://trtc.io/document/47969](https://trtc.io/document/47969)*

---
*Источник (EN): [step-3-login-and-logout.md](./step-3-login-and-logout.md)*
