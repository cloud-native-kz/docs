# Шаг 3: Вход и выход

## Описание функции

Пользователи могут отправлять и получать сообщения только после входа в Chat SDK. Для входа на серверы бэкенда Tencent пользователю необходимо предоставить информацию, включая `UserID` и `UserSig`. Дополнительные сведения об этих параметрах см. в разделе [Аутентификация входа](https://www.tencentcloud.com/document/product/1047/33517).

## Вход

> **Примечание:** После успешного входа необходимо дождаться, пока SDK будет в состоянии готовности (путем прослушивания события `TencentCloudChat.EVENT.SDK_READY`), прежде чем вызывать интерфейсы, требующие аутентификации, такие как `sendMessage`. По умолчанию многоэкземплярный вход не поддерживается, что означает, что если эта учетная запись уже вошла на другую страницу, успешный вход на текущую страницу может привести к отключению других страниц от сети. Когда пользователь отключен от сети, срабатывает событие `TencentCloudChat.EVENT.KICKED_OUT`, и пользователь может обработать его соответствующим образом после прослушивания события. Чтобы поддержать многоэкземплярный вход (разрешение входа в одну и ту же учетную запись одновременно на нескольких веб-страницах), войдите в [Chat Console](https://console.trtc.io/), найдите целевой `SDKAppID` и нажмите **Application > Configuration > Login and Message > Login Settings > Max Login Instances per User per Platform** для настройки количества экземпляров. Конфигурация вступит в силу через 5 минут. Для платформ mini-programs, mini-games, uni-app и **React Native** (даже если упакованы в нативное приложение) входы считаются веб-экземплярами. Если этот интерфейс возвращает код ошибки 60020, это означает, что вы не приобрели пакет, пакет истек или приобретенный пакет все еще настраивается и еще не вступил в силу. Пожалуйста, перейдите на страницу покупки Chat и переупакуйте пакет. После покупки это вступит в силу в течение 5 минут. Если этот интерфейс возвращает код ошибки 2801 на платформе mini-program, пожалуйста, проверьте конфигурацию доверенного домена mini-program.

##### API

```
chat.login(options);
```

##### Параметры

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| UserID | String | ID пользователя. |
| UserSig | String | Пароль, с помощью которого пользователь входит в консоль Chat. По сути, это зашифрованный текст, полученный путем шифрования информации, такой как UserID. Подробный метод генерации см. в разделе [Генерирование UserSig](https://www.tencentcloud.com/document/product/1047/34385). |

##### Возвращаемое значение

`Promise`

##### Примеры

```
let promise = chat.login({userID: 'your userID', userSig: 'your userSig'});promise.then(function(imResponse) {  console.log(imResponse.data);  // Logged in successfully  if (imResponse.data.repeatLogin === true) {  // This indicates that the account is already logged in.    console.log(imResponse.data.errorInfo);  }}).catch(function(imError) {  console.warn('login error:', imError);});
```

## Получение информации вошедшего пользователя

##### API

```
chat.getLoginUser();
```

##### Параметры

Отсутствуют

##### Возвращаемое значение

`String`

##### Примеры

```
const userID = chat.getLoginUser();
```

## Получение времени сервера

##### API

```
chat.getServerTime();
```

##### Параметры

Отсутствуют

##### Возвращаемое значение

`Number`

##### Примеры

```
const serverTime = chat.getServerTime();
```

## Готовность SDK

После того как SDK будет готов, разработчики могут вызывать API SDK для отправки сообщений и использования различных функций SDK.

Разработчики также могут прослушивать:

- `SDK_READY`, который срабатывает, когда SDK переходит в состояние готовности.
- `SDK_NOT_READY`, который срабатывает, когда SDK переходит в состояние неготовности.

##### API

```
chat.isReady();
```

##### Параметры

Отсутствуют

##### Возвращаемое значение

`Boolean`

##### Примеры

```
let isReady = chat.isReady();
```

## Выход

Этот API используется для выхода из Chat SDK. Обычно он вызывается при переключении между учетными записями. Этот API очищает статус входа текущей учетной записи и все данные в памяти.

> **Примечание:** При вызове этого API экземпляр публикует событие `SDK_NOT_READY`. В этом случае экземпляр выходит из системы и не может получать или отправлять сообщения. Если параметр "Number of Concurrent Online Web Instances" в [Chat Console](https://console.trtc.io/) больше 1, и одна и та же учетная запись вошла в экземпляры a1 и a2 (включая клиент mini program), после выполнения a1.logout(), a1 выйдет из системы и не сможет получать или отправлять сообщения, в то время как a2 не будет затронут. Если "Number of Concurrent Online Web Instances" установлено на 2, и ваша учетная запись вошла в экземпляры a1 и a2, при входе в экземпляр a3 один из a1 или a2 будет отключен от сети. Обычно экземпляр, который первым вошел в состояние входа, отключается от сети. Это называется отключением от сети из-за многоэкземплярного входа. Если a1 отключен, в a1 выполняется процесс выхода и срабатывает событие `KICKED_OUT`. Вы можете прослушивать это событие и перенаправить на страницу входа при срабатывании. В этот момент a1 находится в автономном режиме, в то время как a2 и a3 продолжают работать.

##### API

```
chat.logout();
```

##### Параметры

Отсутствуют

##### Возвращаемое значение

`Promise`

##### Примеры

```
let promise = chat.logout();promise.then(function(imResponse) {  console.log(imResponse.data);// Logged out successfully}).catch(function(imError) {  console.warn('logout error:', imError);});
```

## Завершение

Вы можете завершить работу экземпляров SDK. SDK сначала выполнит выход, затем отключит долгосрочное соединение WebSocket и, наконец, освободит все ресурсы.

##### API

```
chat.destroy();
```

##### Параметры

Отсутствуют

##### Возвращаемое значение

`Promise`

##### Примеры

```
let promise = chat.destroy();
```

## Параметры входа

По умолчанию многоэкземплярный вход не поддерживается. Если вы используете учетную запись, которая уже вошла на другую страницу, для входа на текущую страницу, учетная запись может быть отключена на другой странице, что вызовет событие `KICKED_OUT`. Вы можете действовать соответствующим образом после обнаружения события путем прослушивания.

Ниже приведен пример:

```
let onKickedOut = function (event) {  console.log(event.data.type);  // TencentCloudChat.TYPES.KICKED_OUT_MULT_ACCOUNT (The user is forcibly logged out because the same account logs in from multiple webpages on the web client.)  // TencentCloudChat.TYPES.KICKED_OUT_MULT_DEVICE (The user is forcibly logged out because the same account logs in from multiple terminals.)  // TencentCloudChat.TYPES.KICKED_OUT_USERSIG_EXPIRED (The signature expired.)  // TencentCloudChat.TYPES.KICKED_OUT_REST_API (The user is forcibly logged out by the RESTful API.)};chat.on(TencentCloudChat.EVENT.KICKED_OUT, onKickedOut);
```


---
*Источник: [https://trtc.io/document/47970](https://trtc.io/document/47970)*

---
*Источник (EN): [step-3-login-and-logout.md](./step-3-login-and-logout.md)*
