# Структура запроса

## 1. Адрес сервиса

API поддерживает доступ как из ближайшего региона (на trtc.intl.tencentcloudapi.com), так и из указанного региона (например, trtc.ap-guangzhou.tencentcloudapi.com для Гуанчжоу).

Мы рекомендуем использовать доменное имя для доступа к ближайшему серверу. При вызове API запрос автоматически разрешается на сервере в регионе, **ближайшем** к местоположению, откуда инициирован API. Например, при инициировании запроса API в Гуанчжоу это доменное имя автоматически разрешается на сервер Гуанчжоу, результат идентичен результату указания региона в доменном имени, как "trtc.ap-guangzhou.tencentcloudapi.com".

**Примечание: для приложений, чувствительных к задержкам, мы рекомендуем указывать регион в доменном имени.**

Tencent Cloud в настоящее время поддерживает следующие регионы:

| Регион хостинга | Доменное имя |
| --- | --- |
| Регион локального доступа (рекомендуется, только для нефинансовых зон доступности) | trtc.intl.tencentcloudapi.com |
| Южный Китай (Гуанчжоу) | trtc.ap-guangzhou.tencentcloudapi.com |
| Восточный Китай (Шанхай) | trtc.ap-shanghai.tencentcloudapi.com |
| Восточный Китай (Нанкин) | trtc.ap-nanjing.tencentcloudapi.com |
| Северный Китай (Пекин) | trtc.ap-beijing.tencentcloudapi.com |
| Юго-западный Китай (Чэнду) | trtc.ap-chengdu.tencentcloudapi.com |
| Юго-западный Китай (Чунцин) | trtc.ap-chongqing.tencentcloudapi.com |
| Гонконг, Макао, Тайвань (Гонконг, Китай) | trtc.ap-hongkong.tencentcloudapi.com |
| Юго-восточная Азия (Сингапур) | trtc.ap-singapore.tencentcloudapi.com |
| Юго-восточная Азия (Джакарта) | trtc.ap-jakarta.tencentcloudapi.com |
| Юго-восточная Азия (Бангкок) | trtc.ap-bangkok.tencentcloudapi.com |
| Северо-восточная Азия (Сеул) | trtc.ap-seoul.tencentcloudapi.com |
| Северо-восточная Азия (Токио) | trtc.ap-tokyo.tencentcloudapi.com |
| Восточное побережье США (Виргиния) | trtc.na-ashburn.tencentcloudapi.com |
| Западное побережье США (Кремниевая долина) | trtc.na-siliconvalley.tencentcloudapi.com |
| Южная Америка (Сан-Паулу) | trtc.sa-saopaulo.tencentcloudapi.com |
| Европа (Франкфурт) | trtc.eu-frankfurt.tencentcloudapi.com |

## 2. Протокол связи

Все API Tencent Cloud взаимодействуют через HTTPS, обеспечивая высокозащищённые каналы связи.

## 3. Методы запроса

Поддерживаемые методы HTTP-запроса:

POST (рекомендуется)
GET

Типы Content-Type, поддерживаемые POST-запросами:

application/json (рекомендуется). Должен использоваться алгоритм подписи TC3-HMAC-SHA256.
application/x-www-form-urlencoded. Должен использоваться алгоритм подписи HmacSHA1 или HmacSHA256.
multipart/form-data (поддерживается только некоторыми API). Необходимо использовать TC3-HMAC-SHA256 для расчёта подписи.

Размер пакета GET-запроса составляет до 32 КБ. Размер POST-запроса составляет до 1 МБ при использовании алгоритма подписи HmacSHA1 или HmacSHA256 и до 10 МБ при использовании TC3-HMAC-SHA256.

## 4. Кодировка символов

Используется только кодировка UTF-8.


---
*Источник: [https://trtc.io/document/34262](https://trtc.io/document/34262)*

---
*Источник (EN): [request-structure.md](./request-structure.md)*
