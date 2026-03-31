# Начало интеграции

Данный документ описывает, как быстро и безопасно подключиться к **Beauty AR Web** и использовать его функции. Если у вас есть вопросы, пожалуйста, [свяжитесь с нами](https://trtc.io/contact).

## Подготовка

Перед подключением к SDK убедитесь, что вы приобрели веб-лицензию и создали проект в соответствии с инструкциями в разделе [Активация услуги](https://trtc.io/document/60213#web).

### Получение информации параметров

1. Получите `App ID`, `License Key` и `License Token` из [Управления лицензиями](https://console.trtc.io/beauty/license).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f4d320c0a2311f0b3015254001c06ec.png)

**Web Domain**: Информация о домене, введенная во время создания проекта. Лицензия может использоваться только под этим доменом.

> **Примечание:** Убедитесь, что вы используете ключ лицензии и токен лицензии, которые **соответствуют разрабатываемому домену**, в противном случае аутентификация не пройдет и SDK не сможет быть правильно инициализирован.

### Подготовка информации подписи

Помимо ключа лицензии, необходимого для авторизации SDK, вам также нужно использовать токен для подписания API, вызываемых в SDK.

#### Процесс аутентификации алгоритма подписи

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f4e32af0a2311f0ae6a525400454e06.jpeg)

- Token: Ваш уникальный идентификатор, используется для подписания API SDK.
- App ID: `APP ID`, отображаемый в консоли Beauty AR.
- Timestamp: Текущее время с точностью до секунды (10 цифр).
- Signature: Подпись, используемая для подписания, действительна в течение пяти минут.

#### Развертывание сервиса подписи

Поскольку подпись действует ограниченное время и чтобы предотвратить утечку токена, вам необходимо развернуть сервис генерирования подписи.

> **Примечание:** Если токен будет скомпрометирован, ваша личность будет украдена, что приведет к утечке ваших ресурсов. Если метод генерирования подписи реализован на фронтенде, токен может быть скомпрометирован. Поэтому в целях защиты безопасности мы рекомендуем не реализовывать генерирование подписей на фронтенде.

```
// Пример с использованием бэкенда `express`// Алгоритм подписи: sha256(timestamp+token+appid+timestamp)const { createHash } = require('crypto');const config = {    appid: 'Your Tencent Cloud `APPID`',    token: 'Your token',}const sha256 = function(str) {    return createHash('sha256')        .update(str)        .digest('hex');}const genSignature = function() {    const timestamp = Math.round(new Date().getTime() / 1000);    const signature = sha256(timestamp + config.token + config.appid + timestamp).toUpperCase(); // Используйте полученные выше токен и APP ID для генерирования зашифрованной строки и возврата ее    return { signature, timestamp };}app.get("/get-ar-sign", (req, res) => {    const sign = genSignature();    res.setHeader('Access-Control-Allow-Origin','*');    res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');    res.send(sign);})
```

#### Вызов сервиса подписи на фронтенде

После развертывания сервиса подписи добавьте метод получения подписи на вашу веб-страницу, к которому SDK может подключиться и вызвать.

Web

```
async function getSignature() {    const res = await fetch('Your domain/get-ar-sign')    const authdata = await res.json()    console.log('authdata',authdata)    return authdata}
```

## Интеграция SDK

После завершения описанной выше подготовки следуйте процессу ниже, чтобы подключиться к SDK и использовать его функции.

### Описание процесса

**Tencent Effect web SDK** предлагает простые и минимально инвазивные API. Чтобы интегрировать его и использовать его функции, вам нужно только инициализировать экземпляр и добавить узел рендера на вашу веб-страницу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f4f63560a2311f0a6d15254007c27c5.png)

### Установка SDK

SDK предлагается как npm пакет.

```
npm install tencentcloud-webar
```

Кроме того, вы также можете использовать его для своего проекта путем импорта JS.

```
<script charset="utf-8" src="https://webar-static.tencent-cloud.com/ar-sdk/resources/latest/webar-sdk.umd.js"></script>
```

### Инициализация SDK

Для веб-интеграции мы предлагаем два режима инициализации SDK.

- [Встроенная камера и проигрыватель](https://trtc.io/document/50101?platform=web&product=beautyar): Используется встроенная камера и проигрыватель устройства. Вызовы API просты и быстры с богатыми интерактивными функциями.
- [Пользовательские потоки](https://trtc.io/document/50102?platform=web&product=beautyar): Вы можете использовать этот режим, если хотите применить эффекты к своим собственным потокам или хотите большей гибкости и контроля.

### Использование SDK

##### Настройка фильтров красоты и спецэффектов

Для получения дополнительной информации см. [Настройка фильтров и эффектов](https://trtc.io/document/54291?platform=web&product=beautyar).

##### Сегментация

Функция ключинга позволяет выделять и менять фон на изображении. Подробнее см. [Настройка сегментации](https://trtc.io/document/50105?platform=web&product=beautyar).

##### 3D эффекты

Для получения дополнительной информации см. [Настройка фильтров и эффектов](https://trtc.io/document/54291?platform=web&product=beautyar).

##### Анимоджи и виртуальные аватары

Эта возможность зависит от окружения WebGL2. Для получения дополнительной информации см. [Настройка анимоджи и виртуальных аватаров](https://trtc.io/document/51231?platform=web&product=beautyar).

## Параметры и API

См. [Параметры и API](https://trtc.io/document/50106?platform=web&product=beautyar).

## Пример кода

См. [Быстрый старт](https://trtc.io/document/53939).


---
*Источник: [https://trtc.io/document/68777](https://trtc.io/document/68777)*

---
*Источник (EN): [start-integration.md](./start-integration.md)*
