# Структура запроса

## 1. Адрес сервиса

API поддерживает доступ как с ближайшего региона (через mps.intl.tencentcloudapi.com), так и с указанного региона (например, через mps.ap-guangzhou.tencentcloudapi.com для Гуанчжоу).

Рекомендуется использовать доменное имя для доступа к ближайшему серверу. При вызове API запрос автоматически разрешается на сервер в регионе, **ближайшем** к месту инициирования API. Например, при инициировании API запроса в Гуанчжоу это доменное имя автоматически разрешается на сервер в Гуанчжоу, результат совпадает с результатом указания региона в доменном имени, как "mps.ap-guangzhou.tencentcloudapi.com".

**Примечание: для приложений, чувствительных к задержкам, рекомендуется указывать регион в доменном имени.**

Tencent Cloud в настоящее время поддерживает следующие регионы:

| Регион размещения | Доменное имя |
| --- | --- |
| Регион локального доступа (рекомендуется, только для нефинансовых зон доступности) | mps.intl.tencentcloudapi.com |
| Южный Китай (Гуанчжоу) | mps.ap-guangzhou.tencentcloudapi.com |
| Восточный Китай (Шанхай) | mps.ap-shanghai.tencentcloudapi.com |
| Восточный Китай (Нанкин) | mps.ap-nanjing.tencentcloudapi.com |
| Северный Китай (Пекин) | mps.ap-beijing.tencentcloudapi.com |
| Юго-Западный Китай (Чэнду) | mps.ap-chengdu.tencentcloudapi.com |
| Юго-Западный Китай (Чунцин) | mps.ap-chongqing.tencentcloudapi.com |
| Гонконг, Макао, Тайвань (Гонконг, Китай) | mps.ap-hongkong.tencentcloudapi.com |
| Юго-Восточная Азия (Сингапур) | mps.ap-singapore.tencentcloudapi.com |
| Юго-Восточная Азия (Джакарта) | mps.ap-jakarta.tencentcloudapi.com |
| Юго-Восточная Азия (Бангкок) | mps.ap-bangkok.tencentcloudapi.com |
| Северо-Восточная Азия (Сеул) | mps.ap-seoul.tencentcloudapi.com |
| Северо-Восточная Азия (Токио) | mps.ap-tokyo.tencentcloudapi.com |
| Восточное побережье США (Вирджиния) | mps.na-ashburn.tencentcloudapi.com |
| Западное побережье США (Кремниевая долина) | mps.na-siliconvalley.tencentcloudapi.com |
| Южная Америка (Сан-Паулу) | mps.sa-saopaulo.tencentcloudapi.com |
| Европа (Франкфурт) | mps.eu-frankfurt.tencentcloudapi.com |

## 2. Протокол связи

Все API Tencent Cloud взаимодействуют через HTTPS, обеспечивая высокозащищенные каналы связи.

## 3. Методы запроса

Поддерживаемые методы HTTP запросов:

POST (рекомендуется)
GET

Типы Content-Type, поддерживаемые POST запросами:

application/json (рекомендуется). Необходимо использовать алгоритм подписи TC3-HMAC-SHA256.
application/x-www-form-urlencoded. Необходимо использовать алгоритм подписи HmacSHA1 или HmacSHA256.
multipart/form-data (поддерживается только некоторыми API). Для вычисления подписи необходимо использовать TC3-HMAC-SHA256.

Размер пакета GET запроса составляет до 32 КБ. Размер POST запроса составляет до 1 МБ при использовании алгоритма подписи HmacSHA1 или HmacSHA256 и до 10 МБ при использовании TC3-HMAC-SHA256.

## 4. Кодировка символов

Используется только кодировка UTF-8.


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33627](https://www.tencentcloud.com/document/product/1041/33627)*

---
*Источник (EN): [request-structure.md](./request-structure.md)*
