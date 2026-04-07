# Web

В этой статье описывается процесс интеграции сервиса Web Push в веб-приложение для реализации функции push-уведомлений.

## Предварительные требования

#### Включение сервиса

Войдите в [**Chat Console > App Push > Access settings**](https://console.trtc.io/chat/push-plugin-push-identifier) > Push Basic Information, включите **Push service** и получите `SDKAppID` и `AppKey`, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b540b2cddcae11f0be395254005ef0f7.png)

### Требования к окружению

- **Среда выполнения**: Node.js версии 12 или выше.
- **Браузер**: Должен поддерживать Service Worker и Push API. Основные требования: Chrome 50+, Firefox 44+, Edge 17+.
- **Протокол безопасности**: В production окружении необходимо использовать HTTPS. HTTP (http://localhost) допускается для локальной разработки.

### Поддержка браузерами

> **Примечание:** В специальных окружениях, таких как iframe, webview и режим приватности браузера, веб-push недоступен. Дополнительные сведения о совместимости можно найти в разделе Notification в [инструменте проверки совместимости браузеров](https://caniuse.com/?search=Notification).

| Тип браузера | Минимальная требуемая версия |
| --- | --- |
| Chrome | 50+ |
| Edge | 17+ |
| Firefox | 44+ |
| Opera | 25+ |
| Safari | 16+ |

## Этапы интеграции

### Шаг 1: Интеграция @Tencentcloud/Web-Push

npm

yarn

```
npm install @tencentcloud/web-push --save
```

```
yarn add @tencentcloud/web-push
```

### Шаг 2: Настройка файла Service Worker

После интеграции `@tencentcloud/web-push` скопируйте **Service Worker (sw.js)** в **корневую папку** вашего проекта. После развертывания веб-сайта убедитесь, что этот файл доступен по адресу `https://your-domain.com/sw.js`. В противном случае браузер не сможет зарегистрировать **Service Worker**.

> **Примечание:** Файл sw.js **должен находиться в корневой папке веб-сайта** для правильной работы из-за ограничений безопасности браузера. Файл sw.js можно зарегистрировать только под **HTTPS соединением (или в локальной среде разработки localhost)**. Убедитесь, что ваш production веб-сайт поддерживает **HTTPS**.

**Назначение публичной папки**: В современных фронтенд-проектах (таких как Vue, React, Next.js и т. д.) **публичная папка — это уникальная папка, содержимое которой не будет компилироваться или переименовываться при сборке**. Файлы, размещенные в публичной папке, будут скопированы в корневую папку веб-сайта как есть.

> **Примечание:** Если разместить sw.js в папке src или других папках, он может быть скомпилирован или переименован (например, преобразован в sw.123abcde.js) инструментами упаковки (Webpack/Vite), что приведет к неправильной регистрации. Если в вашем проекте **нет публичной папки** (например, в старых HTML-проектах), разместите **sw.js** в той же папке, что и **index.html**, чтобы убедиться, что он находится в корневой папке после вывода сборки.

macOS

Windows

```
cp node_modules/@tencentcloud/web-push/dist/sw.js public/sw.js
```

```
copy node_modules\\@tencentcloud\\web-push\\dist\\sw.js public\\sw.js
```

### Шаг 3: **Регистрация для сервиса Push**

На вашей домашней странице (например: `index.js`) добавьте `@tencentcloud/web-push` и выполните регистрацию.

| Параметр | Тип | Описание |
| --- | --- | --- |
| SDKAppID | Number | SDKAppID для сервиса push Push. Справка: [Предварительные требования > Включение сервиса](#ef1e073e-23da-422d-b06b-f13fcda46734) для получения SDKAppID. |
| appKey | String | Ключ клиента для сервиса push Push. Справка: [Предварительные требования > Включение сервиса](#ef1e073e-23da-422d-b06b-f13fcda46734) для получения AppKey. |
| userID | String | Зарегистрируйте userID для сервисов push. Уникальный идентификатор пользователя, определяемый вами, может содержать только прописные и строчные буквы (a-z, A-Z), цифры (0-9), подчеркивание и дефис. |

```
import WebPush from '@tencentcloud/web-push';const SDKAppID = 0; // Your SDKAppIDconst appKey = ''; // client keyconst userID = ''; // user ID// Register for push serviceawait WebPush.registerPush({ SDKAppID, appKey, userID });// Listen to push messagesWebPush.addPushListener(WebPush.EVENT.MESSAGE_RECEIVED, (message) => {  console.log('received push message:', message);});// Listen to notification clickWebPush.addPushListener(WebPush.EVENT.NOTIFICATION_CLICKED, (data) => {  console.log('notification clicked:', data);});
```

### Шаг 4: Получите опыт первого push-уведомления

Перед тестовым push-уведомлением выполните следующие операции:

1. Откройте консоль браузера и проверьте наличие сообщения `registerPush ok`.
2. Отправьте первое push-сообщение, используя функцию [Server API > UserID-Targeted Push](https://www.tencentcloud.com/document/product/1047/67553).
3. После успешного вызова API (обычно возвращается код успешного статуса) проверьте, получена ли уведомление в строке уведомлений устройства.

Успешные push-уведомления показаны ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b828de9d66a11f091e252540044a08e.png)

## Обратный вызов результата push-уведомления

После включения сервиса push результат push-уведомления будет передан в backend через webhook. Подробнее см.:

- [Push-уведомление для всех пользователей / Теги / UserID Callback](https://www.tencentcloud.com/document/product/1047/67551)
- [Другие Push-обратные вызовы](https://www.tencentcloud.com/document/product/1047/67552)

## Часто задаваемые вопросы

### Устранение неполадок при неудачном получении push-уведомлений

1. Убедитесь, что разрешение на уведомления включено.
  - Операционная система разрешает браузеру отправлять уведомления.

macOS: **System Preferences** > **Notifications**, включите разрешение на уведомления для соответствующего браузера.

Windows: **Settings** > **Privacy** > **Notifications**, включите разрешение на уведомления для соответствующего браузера.

  - Разрешите веб-сайтам отправлять уведомления в браузере.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a789c600db1211f09dea52540044a08e.png)

2. Убедитесь, что веб-сайт действительно доступен через `https` (исключение: локальный localhost).
  - Production окружение: `https://`
  - Локальная разработка: `http://localhost`
3. Убедитесь, что sw.js настроен успешно.
  - Локальное окружение: После запуска вашего проекта посетите `http://localhost:номер порта/sw.js` в браузере. Если вы видите код JavaScript, это означает успешную конфигурацию.
  - Production окружение: Посетите `https://your-domain.com/sw.js` в браузере. Если вы видите код JavaScript, это означает успешную конфигурацию.
4. Проверьте поддержку браузером WebPush. См.: [Предварительные требования > Поддержка браузерами](#b4bcb1f9-b87b-449a-af2f-d475738d47e8).
5. Проверьте, что окружение браузера может получить доступ к международной сети.
6. Используйте [инструмент устранения неполадок Push-уведомлений](https://www.tencentcloud.com/document/product/1047/60541), предоставленный сервисом push, для диагностики статуса отправки и возможных причин сбоя.

### Устранение неполадок ошибки RegisterPush: "Error: {"Message": Invalid Webpush Domain, "Code": 70109}"

- Production окружение: Основной домен веб-сайта отличается от домена, настроенного в [консоли](https://console.trtc.io/).
- Локальное окружение: Доменное имя веб-сайта не является `http://localhost`.


---
*Источник: [https://trtc.io/document/75529](https://trtc.io/document/75529)*

---
*Источник (EN): [web.md](./web.md)*
