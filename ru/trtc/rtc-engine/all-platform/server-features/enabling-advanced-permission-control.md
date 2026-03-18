# Включение расширенного управления разрешениями

## Обзор

Вы можете рассмотреть **включение расширенного управления разрешениями**, если хотите разрешить входить в комнату или использовать микрофоны только определённым пользователям, но опасаетесь, что выдача разрешений на стороне клиента делает сервис уязвимым для атак и взлома.

Вам не требуется включать расширенное управление разрешениями в следующих сценариях:

- Сценарий 1: Вы хотите иметь аудиторию как можно большего размера и не хотите контролировать доступ к комнатам.
- Сценарий 2: Предотвращение атак на стороне клиента не является вашим приоритетом в настоящий момент.

Мы рекомендуем включить расширенное управление разрешениями для повышения безопасности в следующих сценариях:

- Сценарий 1: Ваши видео- или аудиовызовы имеют высокие требования к безопасности.
- Сценарий 2: Вы хотите реализовать различные управления доступом для разных комнат.
- Сценарий 3: Вы хотите контролировать использование микрофонов аудиторией.

## Поддерживаемые платформы

| iOS | Android | macOS | Windows | Electron | Web | Flutter |
| --- | --- | --- | --- | --- | --- | --- |
| ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Понимание расширенного управления разрешениями

После включения расширенного управления разрешениями TRTC будет проверять не только `UserSig` (билет входа в комнату), но и **PrivateMapKey** (билет разрешения). Последний содержит зашифрованный `roomid` и список битов разрешений.

Пользователь, предоставляющий только `UserSig`, но не `PrivateMapKey`, не сможет входить в указанную комнату.

Список битов разрешений в `PrivateMapKey` использует восемь битов байта для представления различных разрешений пользователей, обладающих `PrivateMapKey`.

| Последовательность бита | Двоичный | Десятичный | Разрешение |
| --- | --- | --- | --- |
| Первый | 0000 0001 | 1 | Создание комнаты |
| Второй | 0000 0010 | 2 | Вход в комнату |
| Третий | 0000 0100 | 4 | Отправка аудио |
| Четвёртый | 0000 1000 | 8 | Получение аудио |
| Пятый | 0001 0000 | 16 | Отправка видео |
| Шестой | 0010 0000 | 32 | Получение видео |
| Седьмой | 0100 0000 | 64 | Отправка видео подпотока (экран) |
| Восьмой | 1000 0000 | 128 | Получение видео подпотока (экран) |

## Включение расширенного управления разрешениями

### Шаг 1. Войдите в консоль TRTC и включите расширенное управление разрешениями

1. Перейдите на страницу [Tencent RTC Console > Applications](https://console.trtc.io/app), нажмите **Manage** в строке целевого приложения, конфигурацию функций которого необходимо изменить, и выберите **Advanced Features** из столбца проекта слева.
2. В разделе **Advanced Features** нажмите кнопку справа от пункта **Enable Advanced Permission Control**, и в появившемся окне нажмите **Confirm** для завершения активации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d37397a6507d11efbaba525400d5f8ef.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d37a9765507d11efb36952540075b605.png)

> **Примечание:** После включения расширенного управления разрешениями для приложения (`SDKAppid`) все пользователи, использующие это приложение, должны передать `privateMapKey` в `TRTCParams` для входа в комнату (как описано в [Шаг 2](#step2) ниже). Поэтому не рекомендуется включать эту функцию, если у вас есть активные пользователи, использующие приложение.

### Шаг 2. Вычислите `PrivateMapKey` на вашем сервере

Мы предоставляем код для расчёта `PrivateMapKey` на Java, GO, PHP, Node.js, Python, C# и C++. Вы можете загрузить и интегрировать их на ваш сервер.

| Язык программирования | Ключевые функции | Ссылка загрузки |
| --- | --- | --- |
| Java | `genPrivateMapKey` и `genPrivateMapKeyWithStringRoomID` | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-java/blob/master/src/main/java/com/tencentyun/TLSSigAPIv2.java) |
| GO | `GenPrivateMapKey` и `GenPrivateMapKeyWithStringRoomID` | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-golang/blob/master/tencentyun/TLSSigAPI.go) |
| PHP | `genPrivateMapKey` и `genPrivateMapKeyWithStringRoomID` | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-php/blob/master/src/TLSSigAPIv2.php) |
| Node.js | `genPrivateMapKey` и `genPrivateMapKeyWithStringRoomID` | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-node/blob/master/TLSSigAPIv2.js) |
| Python | `genPrivateMapKey` и `genPrivateMapKeyWithStringRoomID` | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-python/blob/master/TLSSigAPIv2.py) |
| C# | `genPrivateMapKey` и `genPrivateMapKeyWithStringRoomID` | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-cs/blob/master/tls-sig-api-v2-cs/TLSSigAPIv2.cs) |
| C++ | `genPrivateMapKey` и `genPrivateMapKeyWithStringRoomID` | [GitHub](https://github.com/tencentyun/tls-sig-api-v2-cpp/blob/master/src/tls_sig_api_v2.cpp) |

### Шаг 3. Распределите `PrivateMapKey` с вашего сервера на приложение

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fcfc23bc3a7811ed90fd525400c56988.jpeg)

Как показано на рисунке выше,

`PrivateMapKey`

вычисляется на вашем сервере и распределяется на приложение, которое затем может передать

`PrivateMapKey`

в SDK двумя способами.

#### Способ 1: передача `PrivateMapKey` в SDK при вызове `enterRoom`

Вы можете установить **privateMapKey** в [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/en/group__TRTCCloudDef__ios.html#interfaceTRTCParams) при вызове API `enterRoom` объекта `TRTCCloud`.

Этот способ проверяет `PrivateMapKey` при входе пользователя в комнату. Он прост и используется для назначения разрешений пользователям перед входом в комнату.

#### Способ 2: обновление `PrivateMapKey` в SDK через экспериментальный API

Во время прямой трансляции, когда зрители включают свои микрофоны для совместного вещания, TRTC повторно проверит `PrivateMapKey`, переданный в `TRTCParams` при входе в комнату. Это означает, что если вы установили короткий период действия для `PrivateMapKey`, например 5 минут, повторная проверка может не пройти и привести к удалению зрителя из комнаты при переключении роли на «якорь».

Чтобы решить эту проблему, вы можете продлить период действия, например, с 5 минут на 6 часов, или перед тем как зритель вызовет `switchRole` для переключения роли на «якорь», запросить у вашего сервера новый `PrivateMapKey` и обновить его в SDK, вызвав экспериментальный API `updatePrivateMapKey`. Ниже приведён пример кода:

Android

iOS

C++

C#

```
JSONObject jsonObject = new JSONObject();try {    jsonObject.put("api", "updatePrivateMapKey");    JSONObject params = new JSONObject();    params.put("privateMapKey", "xxxxx"); // Введите новый `privateMapKey`.    jsonObject.put("params", params);    mTRTCCloud.callExperimentalAPI(jsonObject.toString());} catch (JSONException e) {    e.printStackTrace();}
```

```
NSMutableDictionary *params = [[NSMutableDictionary alloc] init];[params setObject:@"xxxxx" forKey:@"privateMapKey"]; // Введите новый `privateMapKey`.NSDictionary *dic = @{@"api": @"updatePrivateMapKey", @"params": params};NSData *jsonData = [NSJSONSerialization dataWithJSONObject:dic options:0 error:NULL];NSString *jsonStr = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];[WXTRTCCloud sharedInstance] callExperimentalAPI:jsonStr];
```

```
std::string api = "{\\"api\\":\\"updatePrivateMapKey\\",\\"params\\":{\\"privateMapKey\\":"xxxxx"}}";TRTCCloudCore::GetInstance()->getTRTCCloud()->callExperimentalAPI(api.c_str());
```

```
std::string api = "{\\"api\\":\\"updatePrivateMapKey\\",\\"params\\":{\\"privateMapKey\\":"xxxxx"}}";       mTRTCCloud.callExperimentalAPI(api);
```

## Часто задаваемые вопросы

#### 1. Почему я не могу войти ни в одну онлайн-комнату?

После включения управления разрешениями комнаты для приложения (`SDKAppid`) пользователи должны передать `PrivateMapKey` в `TRTCParams` для входа в любую комнату в этом приложении. Поэтому, если ваш онлайн-бизнес работает и вы не интегрировали в него логику `privateMapKey`, пожалуйста, не включайте управление разрешениями комнаты.

#### 2. В чём разница между `PrivateMapKey` и `UserSig`?

- `PrivateMapKey` является дополнительным параметром `TRTCParams`, который используется для проверки того, авторизован ли текущий пользователь на вход в указанную комнату (`roomid`) и подтверждения разрешений пользователя в комнате. Используйте `PrivateMapKey` только если вам нужно различать пользователей между собой.


---
*Источник: [https://trtc.io/document/35157](https://trtc.io/document/35157)*

---
*Источник (EN): [enabling-advanced-permission-control.md](./enabling-advanced-permission-control.md)*
