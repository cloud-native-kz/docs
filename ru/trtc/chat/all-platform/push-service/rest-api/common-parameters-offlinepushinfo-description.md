# Общие параметры (описание OfflinePushInfo)

## Описание OfflinePushInfo для push-уведомлений

OfflinePushInfo — это объект JSON, предназначенный для конфигурации push-уведомлений в строке уведомлений, позволяющий вам настраивать закрытие push-уведомления, заголовок push-уведомления, описание текста, passthrough push-уведомления и связанные параметры поставщиков push-услуг.

### Стандартное push-уведомление в строке уведомлений

- Push-уведомление маркетингового контента.

```
{    // other parameters...    "OfflinePushInfo": {        "PushFlag": 0,        "Title":"Offline Push Title"        "Desc": "offline push content"        "Ext": "{\\"entity\\":{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}}",  // passthrough field, push uses string in json format        "AndroidInfo": {             "Sound": "shake",  // ringtone filename, without suffix            "XiaoMiChannelID": "xiaomi_channel_id",            "OPPOChannelID": "oppo_channel_id",            "OPPOCategory": "MARKETING",   // OPPO message categorization: content and marketing            "VIVOCategory": "MARKETING",   // VIVO message categorization: operational messages            "HuaWeiCategory": "MARKETING", // Huawei message category: information marketing            "HonorImportance": "LOW",      // Honor message category: information marketing            "MeiZuNoticeMsgType": 0        // Meizu Message category: information marketing        },        "ApnsInfo": {            "Sound": "apns.mp3", // ringtone filename, with suffix            "BadgeMode": 1,            "Title":"apns title",            "SubTitle":"apns subtitle",            "Image":"www.image.com",            "MutableContent": 1        }    }}
```

- Push-уведомление приватного сообщения.

```
{    // other parameters...    "OfflinePushInfo": {        "PushFlag": 0,        "Title":"Offline Push Title"        "Desc": "offline push content"        "Ext": "{\\"entity\\":{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}}",  // passthrough field, recommended string in json format        "AndroidInfo": {             "Sound": "shake",  // ringtone filename, without suffix            "XiaoMiChannelID": "xiaomi_channel_id",            "OPPOChannelID": "oppo_channel_id",            "VIVOCategory": "IM",                 // vivo message categorization: system message            "HuaWeiCategory": "IM",               // Huawei message category: service and communication            "HonorImportance": "NORMAL",          // Honor message category: service communication            "MeiZuNoticeMsgType": 0               // Meizu Message category: private message            "OPPOCategory": "IM",                 // OPPO message category: communication and service            "OPPOPrivateMsgTemplateId": "xxxx",   // OPPO private message template id            "OPPOPrivateTitleParameters": {       // OPPO private message title template parameters in json format                "k1": "v1"                ...            },            "OPPOPrivateContentParameters": {     // OPPO private message content template parameters in json format                "k1": "v1",                ...            },        },        "ApnsInfo": {            ...    // For details, refer to the ApnsInfo field description        }    }}
```

### APNs Passthrough Push

```
{    // other parameters...    "OfflinePushInfo": {        "Ext": "{\\"entity\\":{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}}"  // passthrough field, push uses string in json format        "ApnsInfo": {            "ContentAvailable": 1 // APNs Transparent Push Feature        },        "AndroidInfo": {            ...    // For details, see AndroidInfo field description        }    }}
```

### APNs VoIP Push

```
{    // other parameters...    "OfflinePushInfo": {        "Title":"Offline Push Title",  // Fallback to ordinary Notification push Title when recipient's VoIP token is not reported        "Desc": "Offline Push Content",  // Fallback to ordinary Notification push Desc when recipient's VoIP token is not reported        "Ext": "{\\"entity\\":{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}}"  // passthrough field, push uses string in json format        "ApnsInfo": {            "IsVoipPush": 1 // APNs VoIP Push        },        "AndroidInfo": {              ...   // For details, see AndroidInfo field description        }    }}
```

### APNs LiveActivity (Dynamic Island) Push

- Обновление LiveActivity.

```
{  // other parameters...  "OfflinePushInfo": {      "Title": "Offline Push Title",      "Desc": "Offline push content",      "Ext": "{\\"entity\\":{\\"k1\\":\\"v1\\",\\"k2\\":\\"v2\\"}}",  // passthrough field, push uses string in json format      "ApnsInfo": {           "LiveActivity": {               "LaId": "timpush",               "Event": "update", // Update LiveActivity push               "ContentState": {                   "k1": v1,                   "k2": v2,                   ...                }            }        },        "AndroidInfo": {            ... // For details, see AndroidInfo field description        }  }}
```

- Завершение LiveActivity.

```
{  // other parameters...  "OfflinePushInfo": {      "Title": "Offline Push Title",      "Desc": "Offline push content",      "Ext": "{\\"entity\\":{\\"k1\\":\\"v1\\",\\"k2\\":\\"v2\\"}}",  // passthrough field, push uses string in json format      "ApnsInfo": {           "LiveActivity": {               "LaId": "timpush",               "Event": "end", // End LiveActivity push               "ContentState": {                   "k1": v1,                   "k2": v2,                   ...                },               "DismissalDate": 1739502750            }        },        "AndroidInfo": {            ... // For details, see AndroidInfo field description        }  }}
```

### Многоязычный push

```
{    // other parameters...    "OfflinePushInfo": {        "PushFlag": 0,        "Title":"Offline Push Title"        "Desc": "offline push content"        "MultiLanguageContent":[            {                "Language":"zh-hant",                "Title":"Offline Push Title"                "Desc":"offline push content"            },            {                "Language":"en",                "Title":"Offline Push Notification Title",                "Desc":"Offline Push Notification Desc"            }        ],        "Ext": "{\\"entity\\":{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}}",  // passthrough field, push uses string in json format        "AndroidInfo": {             ... // For details, refer to the AndroidInfo field description        },        "ApnsInfo": {            ... // For details, refer to the ApnsInfo field description        }    }}
```

### Push на основе шаблона

- Переменные, заранее установленные в шаблоне (только для push-уведомлений чатов).

```
{    // Other parameters...    "OfflinePushInfo": {        "PushFlag": 0,        "Title":"Offline Push Title",        "Desc": "Offline Push Content",        "PushTemplateId":"1400000000-1" // If the template only contains preset variables, PushTemplateParam is not required    }}
```

- Пользовательские переменные шаблона.

```
{    // Other parameters...    "OfflinePushInfo": {        "PushFlag": 0,        "Title":"Offline Push Title",        "Desc": "Offline Push Content",        "PushTemplateId":"1400000000-2",        "PushTemplateParam":{"UserName":"aaaa","ProductID":"bbbb"}    }}
```

### Описание полей OfflinePushInfo

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| PushFlag | Integer | Необязательно | 0: Обычный поток push-уведомлений. Если устройство в сети, отправляется сообщение в сети; в противном случае отправляется оффлайн-уведомление.1: Устройство получает только сообщения в сети. |
| Title | String | Необязательно | Заголовок push-уведомления в строке уведомлений. |
| Desc | String | Необязательно | Содержание push-уведомления в строке уведомлений. |
| MultiLanguageContent | Array | Необязательно | Содержание многоязычного push-уведомления. Бэкенд выбирает содержание push-уведомления на основе языка системы устройства. Если совпадение не найдено, используются стандартные Title и Desc. Функция требует версии SDK 8.5.6870 или выше. Пример кода см. в разделе [Многоязычные push-уведомления](#f94f5e36-30aa-4bef-aebf-4bbe992c8b87). |
| Language | String | Необязательно | Языковой флаг для Title и Desc. Подробнее см. в разделе [Таблица многоязычных кодов](https://www.tencentcloud.com/document/product/1047/52154#code). |
| Ext | String | Необязательно | Содержание push-уведомления (passthrough). Поскольку производители Android-телефонов в материковой части имеют разные требования к платформам push-уведомлений, убедитесь, что это поле имеет формат JSON, в противном случае доставка может не пройти для offline push-уведомлений конкретных производителей. |
| AndroidInfo | Object | Необязательно | Параметры управления push-уведомлениями Android. Конкретные поля см. в разделе [Описание полей AndroidInfo](#1078aae2-c4ef-417c-8f09-4c43edd36c19). |
| ApnsInfo | Object | Необязательно | Параметры управления push-уведомлениями APNs. Конкретные поля см. в разделе [Описание полей ApnsInfo](#8bb656b5-6786-4b9d-b714-86b50189b820). |
| HarmonyInfo | Object | Необязательно | Параметры управления push-уведомлениями Harmony. Конкретные поля см. в разделе [Описание полей HarmonyInfo](#42c5bd72-b2fc-48d5-835a-6a7663a8845d). |
| BadgeAddNum | Integer | Необязательно | Устанавливает значение увеличения для номера значка, добавляя к текущему значку.APNs Push: Диапазон значений: [1-99]. Если присутствуют оба BadgeAddNum и BadgeSetNum, приоритет имеет BadgeSetNum. Если ни один из них не установлен, см. ApnsInfo.BadgeMode.Huawei/Honor/Harmony Push: Диапазон значений: [1-99]. Если присутствуют оба BadgeAddNum и BadgeSetNum, приоритет имеет BadgeSetNum. Если ни один из них не установлен, номер значка увеличивается на 1.Для других поставщиков push-уведомлений: это поле не оказывает влияния. |
| BadgeSetNum | Integer | Необязательно | Установить номер значка.Для APNs push диапазон значений составляет [0~999].Для Huawei/Honor/HarmonyOS push диапазон значений составляет [0~99].Для других поставщиков push-уведомлений это поле не будет действовать.В других случаях см. BadgeAddNum для накопления значков. |
| PushTemplateId | String | Необязательно | ID шаблона push-уведомления. Вы должны предварительно создать шаблон в разделе [Параметры push-уведомлений](https://console.trtc.io/chat/push-plugin-push-setting). Формат: `1400000000-1`. Если не указано, используется стиль push-уведомления системы по умолчанию.**Примечание:** Если шаблон содержит переменные, предустановленные системой, он поддерживается только в сценариях Chat; сценарии чистого Push (например [одиночный push](https://www.tencentcloud.com/document/product/1047/67553)) вернут ошибку. |
| PushTemplateParam | JSON Object | Необязательно | Параметры заполнения шаблона, используемые для заполнения пользовательских переменных. Пример: Если название шаблона — `{{UserName}} Order Notification`, передайте `{"UserName":"aaaa"}` здесь.**Примечание:** Следующие переменные заполняются системой автоматически и не должны быть указаны в `PushTemplateParam`:`timTitle`: заменяется исходным названием push-уведомления.`timDesc`: заменяется исходным содержимым push-уведомления.`timSenderNick`: заменяется никнеймом отправителя.`timGroupName`: заменяется названием группы для группового чата, пустая строка для C2C чата. |

#### Описание полей AndroidInfo

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| Sound | String | Необязательно | Имя файла рингтона системного уведомления Android без расширения. Например, установка «shake» относится к локальному файлу «/res/raw/shake.xxx» в соответствующем приложении. |
| PushStyle | Integer | Необязательно | Стиль строки уведомлений Android. «0» представляет стиль по умолчанию, «1» представляет стиль большого текста. Если не указано, по умолчанию используется 0. Применимо только к Huawei, Honor и OPPO. |
| XiaoMiChannelID | String | Необязательно | Поле адаптации категории уведомлений Mi Push (Channel) для MIUI 10 или выше.Если это поле не пусто, оно переопределяет значение ChannelID в конфигурации сертификата push-уведомлений консоли. |
| OPPOChannelID | String | Необязательно | Поле адаптации канала уведомлений OPPO Push для Android 8.0 или выше.Если это поле не пусто, оно переопределяет значение ChannelID в конфигурации сертификата push-уведомлений консоли. |
| OPPOCategory | String | Необязательно | Категоризация сообщений OPPO push, используется для определения типа сообщения. Подробнее см. в разделе [описание категории](https://open.oppomobile.com/new/developmentDoc/info?id=13189).Если это поле не пусто, оно переопределяет значение категории в конфигурации сертификата push-уведомлений консоли. |
| OPPOPrivateMsgTemplateId | String | Необязательно | ID шаблона приватного сообщения OPPO push, должен быть указан при доставке соответствующего шаблона приватного сообщения. Если OPPOCategory установлено на контент и маркетинг, это поле неактивно. Подробнее см. в разделе ["Проверка шаблона приватного сообщения OPUSH"](https://open.oppomobile.com/documentation/page/info?id=12391). |
| OPPOPrivateTitleParameters | JSON Object | Необязательно | Параметры названия шаблона приватного сообщения OPPO push. Пример шаблона названия: добро пожаловать в ${city}$, ${city}$ приветствует вас. Содержание параметра: `{"city":"Beijing"}` |
| OPPOPrivateContentParameters | JSON Object | Необязательно | Параметры содержания шаблона приватного сообщения OPPO push. Пример шаблона содержания: `{"userName":"Tom", "city":"Shenzhen city"}` |
| OPPONotifyLevel | Integer | Необязательно | Определение уровня напоминания сообщения в строке уведомлений OPPO push. Подробнее см. в разделе [описание notify_level](https://open.oppomobile.com/new/developmentDoc/info?id=11236).1: Строка уведомлений2: Строка уведомлений + экран блокировки16: Строка уведомлений + экран блокировки + баннер + вибрация + рингтонПри использовании OPPONotifyLevel требуется OPPOCategory. |
| VIVOClassification | Integer | Необязательно | Категоризация сообщения vivo push: «0» представляет операционные сообщения, «1» представляет системные сообщения. По умолчанию 1, если не указано. (Служба vivo push оптимизировала правила классификации сообщений 3 апреля 2023 г. Рекомендуется использовать AndroidInfo. VIVOCategory для установки типа сообщения.) |
| VIVOCategory | String | Необязательно | Категоризация сообщения vivo push, используется для определения типа сообщения. Подробнее см. в разделе [описание категории](https://dev.vivo.com.cn/documentCenter/doc/359).Если это поле не пусто, оно переопределяет значение категории в конфигурации сертификата push-уведомлений консоли. |
| VIVONotifyType | String | Необязательно | Тип уведомления 1: Нет, 2: Звонок, 3: Вибрация, 4: Звонок и вибрация. Стандартная установка — 4, см. [notifyType](https://dev.vivo.com.cn/documentCenter/doc/362). |
| HuaWeiImportance | String | Необязательно | Уровень напоминания сообщения Huawei push, значение LOW, NORMAL. |
| HuaWeiCategory | String | Необязательно | Классификация сообщений Huawei push, используется для определения типа сообщения. Подробнее см. в разделе [описание категории](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-References/https-send-api-0000001050986197#section13271045101216).Если это поле не пусто, оно переопределяет значение категории в конфигурации сертификата push-уведомлений консоли. |
| HuaWeiImage | String | Необязательно | URL маленького значка для уведомлений Huawei push в строке уведомлений. URL должен использовать протокол HTTPS. Пример: `https://example.com/image.png`. Файл изображения должен быть меньше 512 КБ, рекомендуемый размер 40dp x 40dp с радиусом углов 8dp. Изображения, превышающие рекомендуемый размер, могут быть сжаты или не полностью отображены. Рекомендуемые форматы изображений — JPG, JPEG или PNG. |
| HonorImage | String | Необязательно | URL значка для уведомлений Honor push в строке уведомлений. URL должен использовать протокол HTTPS. Пример: `https://example.com/image.png`. Значок должен быть меньше 512 КБ, рекомендуемый размер 40dp x 40dp с радиусом углов 8dp. Значки, превышающие рекомендуемый размер, могут быть сжаты или не полностью отображены. |
| HuaWeiChannelID | String | Необязательно | Поле канала уведомлений Huawei Push для EMUI 10.0 или выше.Если это поле не пусто, оно переопределяет значение ChannelID в конфигурации сертификата push-уведомлений консоли. |
| HonorImportance | String | Необязательно | Категоризация сообщений Honor push, значения LOW или NORMAL. Подробнее см. в разделе [Категоризация сообщений Honor](https://developer.honor.com/cn/docs/11002/guides/notification-class). |
| GoogleImage | String | Необязательно | URL значка для уведомлений Google push в строке уведомлений. Ресурс изображения не должен превышать 1 МБ, поддерживает форматы JPG, JPEG или PNG. Пример: `https://example.com/image.png`. |
| GooglePriority | String | Необязательно | Приоритет сообщения уведомления Google Push, см. [priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority).normal: Когда устройство находится на переднем плане, сообщения доставляются немедленно. Когда устройство находится в фоновом режиме или режиме Doze, сообщения доставляются пакетами с задержкой.high: Независимо от состояния устройства (фоновый/Doze/передний план), сообщения пробуждают устройство и доставляются немедленно. |
| GoogleChannelID | String | Необязательно | Поле канала уведомлений Google Push для Android 8.0 или выше. |
| MeiZuNoticeMsgType | Integer | Необязательно | Категоризация сообщений Meizu push. «0» представляет официальное сообщение, «1» представляет приватное сообщение. Подробнее см. в разделе [Описание классификации сообщений Meizu](https://open-res.flyme.cn/fileserver/upload/file/202504/13dc49a671b643438431b386e071f59e.pdf).Если это поле не пусто, оно переопределяет категоризацию сообщений в конфигурации сертификата Meizu Push в консоли. |

#### Описание полей ApnsInfo

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| BadgeMode | Integer | Необязательно | 0 означает, что подсчет требуется, 1 означает, что это сообщение не учитывается, и номер в верхнем правом углу значка не увеличивается.**Примечание:**Значение по умолчанию — 0 в сценариях Chat и 1 в не-Chat сценариях (например при вызове API [одиночный push](https://www.tencentcloud.com/document/product/1047/67553)). |
| Title | String | Необязательно | Это поле используется для определения названия APNs push. Если указано, оно переопределит название верхнего уровня. |
| SubTitle | String | Необязательно | Это поле используется для определения подзаголовка APNs push. |
| Image | String | Необязательно | Это поле используется для определения адреса изображения, передаваемого APNs. Когда клиент получает это поле, изображение может быть отображено во всплывающем окне путем загрузки ресурса изображения. |
| MutableContent | Integer | Необязательно | Установите значение 1 для включения расширения push-уведомлений для iOS 10+. По умолчанию 0. |
| Sound | String | Необязательно | Имя файла рингтона системного уведомления iOS с расширением. Продолжительность пользовательского рингтона не может превышать 30 секунд. Файл аудио должен быть предварительно добавлен в проект Xcode. Пример значения: `shake.mp3`. |
| InterruptionLevel | String | Необязательно | Уровень уведомления для push-уведомлений iOS 15+ может быть только одним из: active, critical, passive или time-sensitive. Подробнее см. в разделе: [Описание APNs InterruptionLevel](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel). |
| ContentAvailable | Integer | Необязательно | 1 указывает на «тихий» push-уведомление для iOS без всплывающего окна в баннере уведомлений. Apple рекомендует отправлять не более 3 тихих сообщений в час. Подробнее см. в разделе: [Фоновые уведомления APNs](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app). |
| IsVoipPush | Integer | Необязательно | 1 указывает на VoIP push-уведомление для iOS. Если получатель не предоставил VoIP токен, он будет автоматически понижен до обычного push-уведомления APNs. |
| LiveActivity | Object | Необязательно | Параметры управления push-уведомлением LiveActivity. Конкретные поля см. в разделе [Описание полей LiveActivity](#f4199d1f-0337-4c0b-bdd2-aed25d59bdab). |

##### Описание полей Harmony

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| Title | String | Необязательно | Это поле используется для определения названия push-уведомления Harmony. Если указано, оно переопределит название верхнего уровня. |
| Category | String | Необязательно | Категоризация сообщений HarmonyOS push, используется для определения типа сообщения. Подробнее см. в разделе [описание категории](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/push-scenariozed-api-request-param-V5#section17371529101117).Если не пусто, это поле переопределит значение категории в конфигурации сертификата Push в консоли. |
| Image | String | Необязательно | URL большого значка уведомления. URL должен использовать протокол HTTPS. |
| Sound | String | Необязательно | Пользовательский звук уведомления сообщения. Файл рингтона, установленный здесь, должен быть размещен в пути /resources/rawfile приложения. Например, установка «alert.mp3» соответствует локальному файлу /resources/rawfile/alert.mp3 в приложении. Поддерживаемые форматы файлов включают MP3, WAV, MPEG. Если не установлено, используется стандартный системный рингтон.Когда запрос не содержит поле SoundDuration, рекомендуется, чтобы продолжительность рингтона не превышала 30 секунд. Если превышает 30 секунд, усечь. Когда запрос содержит поле SoundDuration, подробнее см. описание поля [SoundDuration](#SoundDuration).**Примечание:** Устройства для носки, ТВ, ПК/2в1 не поддерживают настраиваемый рингтон |
| SoundDuration | Integer | Необязательно | Продолжительность пользовательского рингтона уведомления сообщения. Должно использоваться вместе с полем Sound, действует только когда запрос содержит оба поля Sound и SoundDuration. Поддерживает только цифры, в секундах, в диапазоне [1,60].Пользовательский рингтон уведомления сообщения, передаваемый в поле Sound, будет воспроизводиться до достижения значения поля SoundDuration. Если продолжительность пользовательского рингтона уведомления сообщения недостаточна, он будет воспроизводиться в цикле и остановиться при достижении значения поля SoundDuration. |

##### Описание полей LiveActivity

| Поле | Тип | Атрибут | Описание |
| --- | --- | --- | --- |
| LaId | String | Обязательно | Идентификатор действительной активности, которую необходимо отправить, соответствует clientActivityID, длина не превышает 64 байта. Подробнее см. в разделе [реализация функции LiveActivity (Dynamic Island)](https://www.tencentcloud.com/document/product/1047/69235). |
| Event | String | Обязательно | Для обновления введите `update`; для завершения введите `end`. |
| ContentState | Object | Обязательно | Пользовательский объект ключ-значение. Должен соответствовать значению клиентского SDK.Соответствует официальному документу APNs: [Запуск и обновление действительной активности с помощью push-уведомлений ActivityKit \| Apple Developer Documentation](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications) |
| DismissalDate | Integer | Необязательно | Когда Event имеет значение «end», Unix-время, отображаемое для завершения действительной активности на экране блокировки. Если не указано, по умолчанию использу

---
*Источник (EN): [common-parameters-offlinepushinfo-description.md](./common-parameters-offlinepushinfo-description.md)*
