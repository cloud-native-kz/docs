# Описание автономной отправки V2TIMOfflinePushInfo.vendorParams

В этой статье описаны описания полей и пример использования автономной отправки `V2TIMOfflinePushInfo.vendorParams`.

## Описание полей

| Поле | Тип | Атрибут | Инструкции по использованию | Примечания |
| --- | --- | --- | --- | --- |
| fcmPriority | String | Опционально | Параметры приоритета отправки сообщений FCM"normal": Обычный приоритет. Когда приложение работает на переднем плане, сообщения с обычным приоритетом будут передаваться немедленно. Когда приложение работает в фоне, доставка сообщений может быть отложена. Для нечувствительных ко времени сообщений (таких как уведомления о новой почте, синхронизация интерфейса или синхронизация данных приложения в фоне) рекомендуем выбрать обычный приоритет доставки."high": Высокий приоритет. Даже если устройство находится в режиме низкого энергопотребления, FCM немедленно попытается передать сообщения высокого приоритета. Сообщения высокого приоритета подходят для содержимого, чувствительного ко времени и видимого пользователю. | Нет |
| vivoNotifyType | Integer | Опционально | Тип уведомления vivo:Отсутствует2: Звонок.3: Вибрация.4: Звонок и вибрация.Значение по умолчанию: 4. | Нет |
| oppoTemplateId | String | Опционально | Идентификатор шаблона для приложения приватного сообщения OPPO. О способе применения см. [Приватный канал сообщений OPPO](https://www.tencentcloud.com/document/product/1047/60576#d6a5a27f-af6d-459c-b006-a133df86729e): При отправке должен использоваться соответствующий шаблон приватного сообщения. Пользовательское содержимое не поддерживается. | **Примечание:**Консоль также поддерживает отдельную настройку идентификатора шаблона, в основном используется для отправки сообщений в сценариях Chat (**category = "IM"**). Идентификатор шаблона вступает в силу:После установки идентификатора шаблона в настройках консоли поля title и desc [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/zh-cn/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) будут автоматически заполнены заголовком и содержимым шаблона следующим образом:{    "oppoTitleParam": {         "title":"titleInfo"     },    "oppoContentParam":{        "desc":"descInfo"    }} Пример применения шаблона:TemplateID: IDТип сообщения: IMЗаголовок: ${title}$Содержимое: ${desc}$**Указанное решение поддерживает адаптацию автономных сообщений для функции шаблонов приватных сообщений в существующих сценариях Chat, достигая цели, при которой сообщения Chat существующих пользователей могут по-прежнему доставляться через канал приватных сообщений. Этот метод также рекомендуется для сообщений типа Chat для использования шаблонов приватных сообщений.** |
| oppoTitleParam | JSON | Опционально | Параметры заполнения заголовка шаблона OPPO:Пример: Идентификатор шаблона приватного сообщения, шаблон заголовка: Welcome to ${city}, ${city} welcomes you.Содержимое параметра: {"city":"Beijing"} |  |
| oppoContentParam | JSON | Опционально | Параметры заполнения содержимого шаблона OPPO:Пример: Идентификатор шаблона приватного сообщения, шаблон содержимого: Welcome ${userName} to ${city}.Содержимое параметра: {"userName":"Tom", "city":"Shenzhen city"} |  |

### Пример использования

Android

iOS

C++

Java

Kotlin

```
V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();Map<String, Object> map = new HashMap<>();map.put("fcmPriority", "high");map.put("vivoNotifyType", 4);map.put("oppoTemplateId", "oppoid");Map<String, Object> oppoTitleMap = new HashMap<>();oppoTitleMap.put("title", "title");map.put("oppoTitleParam", new Gson().toJson(oppoTitleMap));Map<String, Object> oppoContentMap = new HashMap<>();oppoContentMap.put("desc", "desc");map.put("oppoContentParam", new Gson().toJson(oppoContentMap));String param = new Gson().toJson(map);v2TIMOfflinePushInfo.setVendorParams(param);
```

```
val map = mutableMapOf<String, Any>(    "fcmPriority" to "high",    "vivoNotifyType" to 4,    "oppoTemplateId" to "oppoid")val oppoTitleMap = mapOf("title" to "title")map["oppoTitleParam"] = Gson().toJson(oppoTitleMap)val oppoContentMap = mapOf("desc" to "desc")map["oppoContentParam"] = Gson().toJson(oppoContentMap)val param = Gson().toJson(map)V2TIMOfflinePushInfo v2TIMOfflinePushInfo = new V2TIMOfflinePushInfo();v2TIMOfflinePushInfo.setVendorParams(param)
```

OC

Swift

```
NSMutableDictionary *map = [@{    @"fcmPriority": @"high",    @"vivoNotifyType": @4,    @"oppoTemplateId": @"oppoid"} mutableCopy];NSDictionary *oppoTitleMap = @{@"title": @"title"};NSData *titleData = [NSJSONSerialization dataWithJSONObject:oppoTitleMap options:0 error:nil];NSString *oppoTitleJson = [[NSString alloc] initWithData:titleData encoding:NSUTF8StringEncoding];[map setObject:oppoTitleJson forKey:@"oppoTitleParam"];NSDictionary *oppoContentMap = @{@"desc": @"desc"};NSData *contentData = [NSJSONSerialization dataWithJSONObject:oppoContentMap options:0 error:nil];NSString *oppoContentJson = [[NSString alloc] initWithData:contentData encoding:NSUTF8StringEncoding];[map setObject:oppoContentJson forKey:@"oppoContentParam"];NSData *paramsData = [NSJSONSerialization dataWithJSONObject:map options:0 error:nil];NSString *params = [[NSString alloc] initWithData:paramsData encoding:NSUTF8StringEncoding];V2TIMOfflinePushInfo *v2TIMOfflinePushInfo = [[V2TIMOfflinePushInfo alloc] init];v2TIMOfflinePushInfo.vendorParams = params;
```

```
var map: [String: Any] = [    "fcmPriority": "high",    "vivoNotifyType": 4,    "oppoTemplateId": "oppoid"]let oppoTitleMap: [String: String] = ["title": "title"]if let titleData = try? JSONSerialization.data(withJSONObject: oppoTitleMap),   let oppoTitleJson = String(data: titleData, encoding: .utf8) {    map["oppoTitleParam"] = oppoTitleJson}let oppoContentMap: [String: String] = ["desc": "desc"]if let contentData = try? JSONSerialization.data(withJSONObject: oppoContentMap),   let oppoContentJson = String(data: contentData, encoding: .utf8) {    map["oppoContentParam"] = oppoContentJson}let paramsData = try! JSONSerialization.data(withJSONObject: map)let params = String(data: paramsData, encoding: .utf8)!let v2TIMOfflinePushInfo = V2TIMOfflinePushInfo()v2TIMOfflinePushInfo.vendorParams = params;
```

```
#include <sstream>#include <string>V2TIMOfflinePushInfo offline_push_info;//std::string param = R"({"fcmPriority":"high","vivoNotifyType":4})";std::ostringstream param;// Build the main structparam << "{";param << "\\"fcmPriority\\":\\"high\\",";param << "\\"vivoNotifyType\\":4,";param << "\\"oppoTemplateId\\":\\"oppoid\\",";// Build the json string of oppoTitleParamstd::string oppo_title_json = "{\\"title\\":\\"title\\"}";param << "\\"oppoTitleParam\\":\\"";for (const char c : oppo_title_json) {    // Escape double quotes in nested json    if (c == '"') oss << '\\\\';    oss << c;}param << "\\",";// Build the json string of oppoContentParamstd::string oppo_content_json = "{\\"desc\\":\\"desc\\"}";param << "\\"oppoContentParam\\":\\"";for (const char c : oppo_content_json) {    if (c == '"') oss << '\\\\';    oss << c;}param << "\\"}"; offline_push_info.vendorParams = param.str();
```

> **Примечание:**Поддерживается IMSDK версии 8.7 и выше.

## Справочник API

Android: [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html)

iOS:[V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMOfflinePushInfo.html)

C++:[V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/structV2TIMOfflinePushInfo.html)


---
*Источник: [https://trtc.io/document/73940](https://trtc.io/document/73940)*

---
*Источник (EN): [offline-push-v2timofflinepushinfovendorparams-description.md](./offline-push-v2timofflinepushinfovendorparams-description.md)*
