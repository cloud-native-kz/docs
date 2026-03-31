# All Platform

### Во время голосового или видеовызова появляется сообщение об ошибке `[-100035]The package you purchased does not support this ability. Please purchase the package`

Для совершения голосовых или видеовызовов необходимо подписаться на наш пакет вызовов "Call Monthly Package". Вы можете попробовать его бесплатно в течение 7 дней. Дополнительную информацию о том, как активировать сервис, см. здесь: [Activate Service (TUICallKit)](https://www.tencentcloud.com/document/product/647/59832).

### Некорректный или несуществующий UserID отправителя или получателя сообщения

Если пользователь, которого вы вызываете, не вошел в систему, вызов не удастся. Пожалуйста, попробуйте вызвать пользователя, который успешно вошел в систему.

### Ошибка: inviteID недействителен или приглашение уже обработано

inviteID может быть недействительным, если оно было отменено инициатором вызова или если приглашение уже было принято. В некоторых случаях пропускная способность сети также может влиять на сигнализацию, вызывая ошибки недействительности inviteID.

### **Как получить номер комнаты вызова RoomId?**

После установления вызова вы можете получить номер комнаты вызова (RoomId) через поле roomid, возвращаемое методом [onCallBegin](https://www.tencentcloud.com/document/product/647/51007#onCallBegin).

### Ошибка кода "-3301" с сообщением "Services are not available in your region" после входа в комнату

Если вы получили этот код ошибки, [свяжитесь с нами](https://trtc.io/contact) для получения поддержки.

### В интегрированных сценариях TUIChat + TUICallKit после обновления версии TUICallKit новая версия не может получать вызовы от старой версии

Начиная с версии TUICallKit 3.1, в интегрированных сценариях TUIChat + TUICallKit инициирование вызова через кнопку вызова в TUIChat по умолчанию использует новый API вызовов. Поэтому, если ваш бизнес уже запущен в production, вы можете использовать расширенный API для переключения интерфейса вызовов на call или groupCall для сохранения совместимости с пользователями онлайн-версии.

Необходимо вызвать расширенный API один раз после успешного входа в систему. Использование на всех платформах выглядит следующим образом:

iOS(Swift)

iOS(Objective-C)

Android(java)

Android(kotlin)

Flutter(Dart)

Web & Mini Programs

```
let jsonParams: [String: Any] = ["api": "forceUseV2API",                                 "params": ["enable": true,],]guard let data = try? JSONSerialization.data(withJSONObject: jsonParams, options: JSONSerialization.WritingOptions(rawValue: 0)) else { return }guard let paramsString = NSString(data: data, encoding: String.Encoding.utf8.rawValue) as? String else { return }TUICallKit.createInstance().callExperimentalAPI(jsonStr: paramsString)
```

```
NSDictionary *jsonParams = @{@"api": @"forceUseV2API",                                 @"params": @{@"enable": @YES}};NSError *error = nil;NSData *data = [NSJSONSerialization dataWithJSONObject:jsonParams options:0 error:&error];if (error || !data) { return; }NSString *paramsString = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];if (!paramsString) { return;}[[TUICallKit createInstance] callExperimentalAPIWithJsonStr:paramsString];
```

```
 try {    JSONObject params = new JSONObject();    params.put("enable", true);    JSONObject jsonObject = new JSONObject();    jsonObject.put("api", "forceUseV2API");    jsonObject.put("params", params);    TUICallKit.createInstance(context).callExperimentalAPI(jsonObject.toString());} catch (Exception e) {    e.printStackTrace();}
```

```
try {    val params = JSONObject()    params.put("enable", true)    val jsonObject = JSONObject()    jsonObject.put("api", "forceUseV2API")    jsonObject.put("params", params)    TUICallKit.createInstance(context).callExperimentalAPI(jsonObject.toString())} catch (e: Exception) {    e.printStackTrace()}
```

```
final jsonParams = {'api': 'forceUseV2API',                     'params': {'enable': true} };                   try {        final jsonString = json.encode(jsonParams);        TUICallKit.instance.callExperimentalAPI(jsonStr: jsonString);  } catch (e) {        return;  }
```

```
const jsonObject = {    api: "forceUseV2API",    params: {      enable: true,    }};TUICallKitServer.getTUICallEngineInstance().callExperimentalAPI(JSON.stringfy(jsonObject));
```

### 

### Как получить файлы журналов для каждой платформы?

Текущие пути файлов журналов для каждой платформы приведены ниже:

- iOS или Mac: Documents/log
- Android: /sdcard/Android/data/[имя пакета вашего приложения]/files/log/liteav/
- Windows: C:/Users/[имя пользователя системы]/AppData/Roaming/liteav/log, то есть %APPDATA%/liteav/log


---
*Источник: [https://trtc.io/document/53565](https://trtc.io/document/53565)*

---
*Источник (EN): [all-platform.md](./all-platform.md)*
