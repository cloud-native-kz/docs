# Структура запроса

## 1. Адрес сервиса

API поддерживает доступ как из соседнего региона (на live.intl.tencentcloudapi.com), так и из указанного региона (например, на live.ap-guangzhou.tencentcloudapi.com для Гуанчжоу).

Рекомендуется использовать доменное имя для доступа к ближайшему серверу. При вызове API запрос автоматически разрешается на сервер в регионе **ближайшем** к месту инициирования API. Например, при инициировании запроса API в Гуанчжоу это доменное имя автоматически разрешается на сервер Гуанчжоу, результат идентичен результату указания региона в доменном имени, например "live.ap-guangzhou.tencentcloudapi.com".

**Примечание: для приложений, чувствительных к задержкам, рекомендуется указать регион в доменном имени.**

Tencent Cloud в настоящее время поддерживает следующие регионы:

| Размещённый регион | Доменное имя |
| --- | --- |
| Региональный доступ на месте (рекомендуется, только для нефинансовых зон доступности) | live.intl.tencentcloudapi.com |
| Южный Китай (Гуанчжоу) | live.ap-guangzhou.tencentcloudapi.com |
| Восточный Китай (Шанхай) | live.ap-shanghai.tencentcloudapi.com |
| Восточный Китай (Нанкин) | live.ap-nanjing.tencentcloudapi.com |
| Северный Китай (Пекин) | live.ap-beijing.tencentcloudapi.com |
| Юго-западный Китай (Чэнду) | live.ap-chengdu.tencentcloudapi.com |
| Юго-западный Китай (Чунцин) | live.ap-chongqing.tencentcloudapi.com |
| Гонконг, Макао, Тайвань (Гонконг, Китай) | live.ap-hongkong.tencentcloudapi.com |
| Юго-восточная Азия (Сингапур) | live.ap-singapore.tencentcloudapi.com |
| Юго-восточная Азия (Джакарта) | live.ap-jakarta.tencentcloudapi.com |
| Юго-восточная Азия (Бангкок) | live.ap-bangkok.tencentcloudapi.com |
| Северо-восточная Азия (Сеул) | live.ap-seoul.tencentcloudapi.com |
| Северо-восточная Азия (Токио) | live.ap-tokyo.tencentcloudapi.com |
| Восточное побережье США (Вирджиния) | live.na-ashburn.tencentcloudapi.com |
| Западное побережье США (Кремниевая долина) | live.na-siliconvalley.tencentcloudapi.com |
| Южная Америка (Сан-Паулу) | live.sa-saopaulo.tencentcloudapi.com |
| Европа (Франкфурт) | live.eu-frankfurt.tencentcloudapi.com |

## 2. Протокол связи

Все API Tencent Cloud взаимодействуют через HTTPS, обеспечивая высоконадежные каналы безопасной связи.

## 3. Методы запроса

Поддерживаемые методы HTTP-запроса:

POST (рекомендуется)
GET

Типы Content-Type, поддерживаемые POST-запросами:

application/json (рекомендуется). Необходимо использовать алгоритм подписи TC3-HMAC-SHA256.
application/x-www-form-urlencoded. Необходимо использовать алгоритм подписи HmacSHA1 или HmacSHA256.
multipart/form-data (поддерживается только некоторыми API). Необходимо использовать TC3-HMAC-SHA256 для расчёта подписи.

Размер пакета GET-запроса составляет до 32 КБ. Размер POST-запроса составляет до 1 МБ при использовании алгоритма подписи HmacSHA1 или HmacSHA256 и до 10 МБ при использовании TC3-HMAC-SHA256.

## 4. Кодировка символов

Используется только кодировка UTF-8.


---
*Источник: [https://www.tencentcloud.com/document/product/267/30762](https://www.tencentcloud.com/document/product/267/30762)*

---
*Источник (EN): [request-structure.md](./request-structure.md)*
