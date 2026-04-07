# Шаг 3: Вход и выход

## Описание функции

После инициализации SDK необходимо вызвать API входа SDK для аутентификации учетной записи и получения прав доступа для использования функций сообщений, бесед и других возможностей.

> **Примечание:** Все API функций SDK можно вызывать только после успешного входа, за исключением API для получения списка бесед и загрузки исторических сообщений. Поэтому **убедитесь, что вы успешно вошли в систему** перед использованием других функций. Вы можете вызывать API для получения списка бесед и загрузки исторических сообщений даже в случае сбоя входа. В этом случае будут возвращены локально кэшированные список бесед и исторические сообщения, которые можно отобразить при отсутствии сетевого подключения.

## Вход в систему

Ваш первый вход в учетную запись Chat не требует регистрации, поскольку Chat автоматически зарегистрирует учетную запись после обнаружения использования новой учетной записи. Вы можете вызвать API `login` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a73fc0e14c5f2f5fc06a80081479fb416) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.login(userid:usersig:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a38c42943046acdaf615915c9422af07c) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a6a9c19be21327ace77ab75657d2944b3)) для входа в систему.

Ключевые параметры API `login` выглядят следующим образом:

| Параметр | Определение | Описание |
| --- | --- | --- |
| UserID | Уникальный ID пользователя | Может содержать до 32 байт букв (a-z и A-Z), цифр (0-9), подчеркиваний (_) и дефисов (-). |
| UserSig | Токен входа | Вычисляется вашим сервером приложения для обеспечения безопасности. Подробнее см. [Генерация UserSig](https://intl.cloud.tencent.com/document/product/1047/34385). |

API `login` можно вызывать в следующих сценариях:

- Вы используете функции SDK впервые после запуска приложения.
- Ваш токен истекает при входе: Обратный вызов API `login` возвращает код ошибки `ERR_USER_SIG_EXPIRED (6206)` или `ERR_SVR_ACCOUNT_USERSIG_EXPIRED (70001)`. В этом случае вам необходимо сгенерировать новый `userSig` для повторного входа.
- Ваш токен истекает, когда пользователь находится в сети: Вы можете получить обратный вызов `onUserSigExpired` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKListener.html#a55a5d5ee490850d28b7b8a17868c4833) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMSDKListener.html#v2timsdklistener.onusersigexpired()) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMSDKListener-p.html#a55a5d5ee490850d28b7b8a17868c4833) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMSDKListener.html#a65e7f5c8eb4c87df150048a969315e8e)), когда пользователи находятся в сети. В этом случае вам необходимо сгенерировать новый `userSig` для повторного входа.
- Пользователь был отключен: При отключении пользователя SDK уведомит вас через обратный вызов `onKickedOffline` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKListener.html#a0f56352869133d50d43c060448e208e7) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMSDKListener.html#v2timsdklistener.onkickedoffline()) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMSDKListener-p.html#a0f56352869133d50d43c060448e208e7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMSDKListener.html#a5eb8b0014c044296cf440a2e7a3c45ff)). В этом случае вы можете уведомить пользователя и вызвать `login` для повторного входа.
- Отключен в офлайн-режиме: Если пользователь был отключен в офлайн-режиме, он успешно войдет в систему по умолчанию при возвращении в сеть. Если вам нужно вернуть код ошибки ERR_LOGIN_KICKED_OFF_BY_OTHER (6208) для отключения в офлайн-режиме, вам необходимо отдельно настроить это в консоли.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ad269a2664e811ef81cf525400d5f8ef.png)

API `login` не требуется вызывать в следующих сценариях:

- После разрыва и восстановления сетевого подключения пользователя вам не требуется вызывать функцию `login`, поскольку SDK автоматически перейдет в сеть.
- Процесс входа выполняется.

> **Примечание:** После вызова API SDK и успешного входа в систему начинается расчет MAU; поэтому вызывайте API входа по мере необходимости, чтобы избежать высокого MAU. Вы не можете одновременно входить в несколько учетных записей SDK одного приложения; в противном случае в сети будет только последняя зарегистрированная учетная запись.

Пример кода:

Java

Swift

Objective-C

C++

```
String userID = "your user id";String userSig = "userSig from your server";V2TIMManager.getInstance().login(userID, userSig, new V2TIMCallback() {    @Override    public void onSuccess() {        Log.i("imsdk", "success");    }    @Override    public void onError(int code, String desc) {        // The following error codes indicate an expired `userSig`, and you need to generate a new one for login again.        // 1. ERR_USER_SIG_EXPIRED (6206)        // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED (70001)        // Note: Do not call the login API in case of other error codes; otherwise, the SDK may enter an infinite loop of login.        Log.i("imsdk", "failure, code:" + code + ", desc:" + desc);    }});
```

```
let userID = "your user id";let userSig = "userSig from your server";V2TIMManager.shared.login(userID: userID, userSig: userSig) {    print("login succ")} fail: { code, message in    // The following error codes indicate an expired `userSig`, and you need to generate a new one for login again.    // 1. ERR_USER_SIG_EXPIRED (6206)    // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED (70001)    // Note: Do not call the login API in case of other error codes; otherwise, the SDK may enter an infinite loop of login.    if code == 6206 || code == 70001 {        print("UserSig expired, please get a new UserSig.")    } else {        print("Login failure, code: \\(code), message: \\(message)")    }}
```

```
NSString *userID = @"your user id";NSString *userSig = @"userSig from your server";[[V2TIMManager sharedInstance] login:userID userSig:userSig succ:^{    NSLog(@"success");} fail:^(int code, NSString *desc) {    // The following error codes indicate an expired `userSig`, and you need to generate a new one for login again.    // 1. ERR_USER_SIG_EXPIRED (6206)    // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED (70001)    // Note: Do not call the login API in case of other error codes; otherwise, the SDK may enter an infinite loop of login.    NSLog(@"failure, code:%d, desc:%@", code, desc);}];
```

```
class LoginCallback final : public V2TIMCallback {public:    LoginCallback() = default;    ~LoginCallback() override = default;    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString userID = "your user id";V2TIMString userSig = "userSig from your server";auto callback = new LoginCallback;callback->SetCallback(    [=]() {        std::cout << "success";        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {          // The following error codes indicate an expired `userSig`, and you need to generate a new one for login again.       // 1. ERR_USER_SIG_EXPIRED (6206)       // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED (70001)       // Note: Do not call the login API in case of other error codes; otherwise, the SDK may enter an infinite loop of login.        std::cout << "failure, code:" << error_code << ", desc:" << error_message.CString();        delete callback;    });V2TIMManager::GetInstance()->Login(userID, userSig, callback);
```

### Получение UserID

После успешного входа вызовите `getLoginUser` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#ad4b2e5a7df5e786ba369054ac582007f) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getloginuser()) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a78ca7f39bca860e46620f8f766508fb0) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#ad19e832506181f6ec955d9e0d2035797)) для получения `UserID`.
Если вход не удается, `UserID` будет пустым.

Пример кода:

Java

Swift

Objective-C

C++

```
// Get the `UserID` of the logged-in userString loginUserID = V2TIMManager.getInstance().getLoginUser();
```

```
// Get the `UserID` of the logged-in userlet loginUserID = V2TIMManager.shared.getLoginUser()
```

```
// Get the `UserID` of the logged-in userNSString *loginUserID = [[V2TIMManager sharedInstance] getLoginUser];
```

```
// Get the `UserID` of the logged-in userV2TIMString loginUserID = V2TIMManager::GetInstance()->GetLoginUser();
```

### Получение статуса входа

Вызовите `getLoginStatus` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a1836146275265b2a120412f18961db95) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.getloginstatus()) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#acfd2f6366780badf80ebf66d95550f89) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#ad5888b2d240c2fcb076b060d298a2c22)) для получения статуса входа. Если пользователь вошел в систему или входит, не вызывайте API входа часто. SDK поддерживает следующие статусы входа:

| Статус входа | Описание |
| --- | --- |
| V2TIM_STATUS_LOGINED | Вошел в систему |
| V2TIM_STATUS_LOGINING | Вход в систему |
| V2TIM_STATUS_LOGOUT | Не вошел в систему |

Пример кода:

Java

Swift

Objective-C

C++

```
int loginStatus = V2TIMManager.getInstance().getLoginStatus();
```

```
let loginStatus = V2TIMManager.shared.getLoginStatus()
```

```
V2TIMLoginStatus loginStatus = [[V2TIMManager sharedInstance] getLoginStatus];
```

```
V2TIMLoginStatus loginStatus = V2TIMManager::GetInstance()->GetLoginStatus();
```

## Вход с нескольких клиентов и отключение

- Вы можете настроить политики входа с нескольких клиентов для SDK в [консоли Chat](https://console.trtc.io/). Существует несколько политик входа с нескольких клиентов, такие как **пользователь может одновременно находиться в сети на мобильной или настольной платформе и веб-платформе** или **пользователь может одновременно находиться в сети на всех платформах**.
Дополнительные сведения о конфигурации см. в разделе [Конфигурация функций](https://intl.cloud.tencent.com/document/product/1047/34419).
- Вы можете настроить **максимальное количество экземпляров входа на пользователя на платформу** для SDK в [консоли Chat](https://console.trtc.io/), то есть максимальное количество экземпляров на одной платформе, которые могут одновременно находиться в сети. Эта функция доступна только для Pro, Pro Plus и Enterprise. Значение для **Web** и **Android, iPhone, iPad, Windows, Mac** составляет соответственно 10 или 3. Дополнительные сведения о конфигурации см. в разделе [Конфигурация функций](https://intl.cloud.tencent.com/document/product/1047/34419).
- При вызове API `login` для входа, если превышен лимит, указанный политикой входа с нескольких клиентов для вашей учетной записи, вновь зарегистрированный экземпляр отключит более ранний. Если вы вызвали `addIMSDKListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a2f0297e96d365013e7923275ce2a5d4e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addimsdklistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#ac569656a58908afba491710a8cb3c8d9) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a1982f2c3a698176ec3fb79ef3f945ed5)) во время инициализации для добавления слушателя SDK, более ранний экземпляр входа получит обратный вызов `onKickedOffline` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKListener.html#a0f56352869133d50d43c060448e208e7) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMSDKListener.html#v2timsdklistener.onkickedoffline()) / [Objective-C](https://im.sdk.qcloud.com/doc/en/protocolV2TIMSDKListener-p.html#a0f56352869133d50d43c060448e208e7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMSDKListener.html#a5eb8b0014c044296cf440a2e7a3c45ff)).

## Выход из системы

Как правило, если жизненный цикл приложения совпадает с жизненным циклом SDK, перед выходом из приложения выходить не требуется.
В особых случаях, например если вы используете SDK только после входа в конкретный интерфейс и больше не используете его после выхода из интерфейса, вы можете вызвать API `logout` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a0398924fa1b62a8f5cc9b51673273b48) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.logout(succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a20b495d7f7a231ea33507ca4a79f811f) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#abf4f7e18d22fe8f75b5212fcf82e7113)) для выхода из SDK, после чего вы больше не будете получать новые сообщения. Обратите внимание, что в этом случае вам также необходимо вызвать `unInitSDK` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a8ac73b4f71f9d9a1ca01551c919d3cdd) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.uninitsdk()) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a286e5358ec4cd0a8f9c66f4d2d7d4544) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a6c88218989a1c714b4e989d1696439a0)) после выхода, чтобы деинициализировать SDK.

Пример кода:

Java

Swift

Objective-C

C++

```
V2TIMManager.getInstance().logout(new V2TIMCallback() {    @Override    public void onSuccess() {        Log.i("imsdk", "success");    }    @Override    public void onError(int code, String desc) {        Log.i("imsdk", "failure, code:" + code + ", desc:" + desc);    }});
```

```
V2TIMManager.shared.logout(succ: {    print("logout succ.")}, fail: { code, desc in    print("logout fail, code: \\(code), desc: \\(desc)")})
```

```
[[V2TIMManager sharedInstance] logout:^{    NSLog(@"success");} fail:^(int code, NSString *desc) {    NSLog(@"failure, code:%d, desc:%@", code, desc);}];
```

```
class Callback final : public V2TIMCallback {public:    using SuccessCallback = std::function<void()>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    Callback() = default;    ~Callback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess() override {        if (success_callback_) {            success_callback_();        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMString userID = "your user id";V2TIMString userSig = "userSig from your server";auto callback = new Callback{};callback->SetCallback(    [=]() {        std::cout << "success";        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        std::cout << "failure, code:" << error_code << ", desc:" << error_message.CString();        delete callback;    });V2TIMManager::GetInstance()->Logout(callback);
```

## Переключение учетной записи

Вызовите `login` для переключения между учетными записями в приложении.

Например, чтобы переключить вошедшего пользователя с `alice` на `bob`, просто выполните вход bob. Вам не требуется явно вызывать `logout alice`, так как эта операция будет автоматически обработана внутри SDK.


---
*Источник: [https://trtc.io/document/47971](https://trtc.io/document/47971)*

---
*Источник (EN): [step-3-login-and-logout.md](./step-3-login-and-logout.md)*
