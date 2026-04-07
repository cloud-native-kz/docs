# Маршрутизация HTTPDNS

## Обзор

CSS по умолчанию маршрутизирует глобальный трафик push и playback на основе разрешения DNS. Это распространённый и простой способ. Однако из-за сложности глобальной сетевой среды часто возникают ошибки разрешения DNS и кросс-сетевой трафик. Мы рекомендуем использовать HTTPDNS от Tencent Cloud для оптимизации маршрутизации трафика прямых трансляций.

Локальный DNS выход провайдера интернет-услуг выполняет NAT на основе IP-адреса авторитетного DNS или перенаправляет запрос разрешения на другие DNS-серверы. Это затрудняет правильную идентификацию авторитетным DNS-сервером IP-адреса локального DNS провайдера, что приводит к ошибкам разрешения и кросс-сетевому трафику. Служба HTTPDNS от Tencent Cloud работает благодаря передовым технологиям DNS-кластера и поддерживает маршрутизацию мультиоператора и пользовательские маршруты. Дополнительные сведения см. в разделе [HTTPDNS](https://intl.cloud.tencent.com/document/product/1130/44448).

> **Примечание:** В этом документе показано, как использовать HTTPDNS для оптимизации маршрутизации трафика прямых трансляций по всему миру. Подробнее об используемом API HTTPDNS см. в разделе [Запросы с использованием методов HTTP-запроса](https://intl.cloud.tencent.com/document/product/1130/44468).

## Подготовка

1. Активируйте HTTPDNS. Подробные инструкции см. в разделе [Активирование HTTPDNS](https://intl.cloud.tencent.com/document/product/1130/44461).
2. Перейдите на страницу [Конфигурация разработки](https://console.tencentcloud.com/httpdns/configure), чтобы просмотреть ID авторизации и ключ DES.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/57a14841513711ee84f2525400494e51.png)

## Маршрутизация трафика Push с использованием HTTPDNS

### Запрос IP-адреса push

Используйте HTTP GET-запрос в формате `http://119.29.29.98/d?dn={$push_domain DES-encrypted string}&ip={$ip DES-encrypted string}&id=$id` для запроса IP-адреса push из HTTPDNS.

- `push_domain` указывает домен push, который должен быть зашифрован с помощью алгоритма DES. Вы можете просмотреть ключ на странице [Конфигурация разработки HTTPDNS](https://console.tencentcloud.com/httpdns/configure). Подробнее см. в разделе [Шифрование/дешифрование AES/DES](https://intl.cloud.tencent.com/document/product/1130/44470).
- `ip` указывает общий выходящий IP-адрес запрашивающей стороны. Это поле определяет регион и провайдера IP-адреса, на который маршрутизируется трафик. Оно также должно быть зашифровано с помощью алгоритма DES.
- `id` указывает ID авторизации, который уникально идентифицирует пользователя.

### Дешифрование IP-адреса

Данные, полученные из HTTPDNS, зашифрованы с помощью DES. Расшифруйте их, чтобы получить IP-адрес (`server_ip`). Подробнее см. в разделе [Шифрование/дешифрование AES/DES](https://intl.cloud.tencent.com/document/product/1130/44470).

### Формирование URL push

Формат URL push: `rtmp://server_ip/live/streamname?txTime=xxx&txSecret=xxx&txHost=domain`. `server_ip` — это **IP-адрес push, полученный на предыдущем этапе**. `txHost` (важно) — это домен, который вы используете для push.

## Маршрутизация трафика Playback с использованием HTTPDNS

### Запрос IP-адреса playback

Используйте HTTP GET-запрос в формате `http://119.29.29.98/d?dn={$domain DES-encrypted string}&ip={$ip DES-encrypted string}&id=$id` для запроса IP-адреса playback из HTTPDNS.

| Поле | Описание |
| --- | --- |
| play_domain | Домен playback. Значение этого поля должно быть зашифровано с помощью алгоритма DES. Вы можете просмотреть ключ на странице [Конфигурация разработки HTTPDNS](https://console.tencentcloud.com/httpdns/configure). Подробнее см. в разделе [Шифрование/дешифрование AES/DES](https://intl.cloud.tencent.com/document/product/1130/44470). |
| ip | Общий выходящий IP-адрес запрашивающей стороны. Это поле определяет регион и провайдера IP-адреса, на который маршрутизируется трафик. Оно также должно быть зашифровано с помощью алгоритма DES. |
| id | ID авторизации, который уникально идентифицирует пользователя. |

### Дешифрование IP-адреса

Данные, полученные из HTTPDNS, зашифрованы с помощью DES. Расшифруйте их, чтобы получить IP-адрес (`server_ip`). Подробнее см. в разделе [Шифрование/дешифрование AES/DES](https://intl.cloud.tencent.com/document/product/1130/44470).

### Формирование URL playback

- **HTTP**: Форматы HTTP URL playback для FLV и HLS представлены ниже (`server_ip` — это **IP-адрес playback, полученный на предыдущем этапе**, а `play_domain` — это домен playback):

```
http://server_ip/play_domain/live/streamname.flv?xxxxxxxxxxhttp://server_ip/play_domain/live/ streamname.m3u8?xxxxxxxxxxhttp://server_ip/play_domain/live/ streamname -123.ts?xxxxxxxxxx
```

- **RTMP**: Формат URL playback RTMP представлен ниже (`server_ip` — это **IP-адрес playback, полученный на предыдущем этапе**, а `play_domain` — это домен playback):

```
rtmp://server_ip/play_domain/live/ streamname?xxxxxxxxxx
```

> **Примечание:** Существует небольшая вероятность ошибок запроса HTTPDNS. Если истечёт время ожидания вашего запроса или возвращённый результат не является IP-адресом или пуст, выполните разрешение на локальном DNS-сервере. Поскольку IP не поддерживает HTTPS, это решение в настоящее время не поддерживается для оптимизированного планирования.


---
*Источник: [https://www.tencentcloud.com/document/product/267/31568](https://www.tencentcloud.com/document/product/267/31568)*

---
*Источник (EN): [httpdns-routing.md](./httpdns-routing.md)*
