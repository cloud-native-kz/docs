# Запуск образца кода

В этой статье описано, как быстро запустить образец проекта TUIRoomKit и испытать высококачественную многопользовательскую видеоконференцию. Вы сможете пройти демонстрацию менее чем за 10 минут и испытать многопользовательскую видеоконференцию с полным интерфейсом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/25f46b18c0ce11efa28d525400329841.png)

## Предварительные требования

- Версия Node.js: Node.js ≥ 16.19.1 (рекомендуется использовать официальную версию LTS, версия npm должна соответствовать версии Node).
- Современный браузер, [поддерживающий WebRTC API](https://caniuse.com/?search=webrtc).

## Шаг 1. Загрузка демонстрации

1. Откройте Terminal, скопируйте и вставьте команду примера для клонирования репозитория.

```
git clone https://github.com/Tencent-RTC/TUIRoomKit.git
```

2. Установите зависимости.

```
cd ./TUIRoomKit/Electron/example/vue3
```

```
npm install
```

## Шаг 2. Настройка демонстрации

[Перейдите на страницу активации сервиса](https://trtc.io/document/59832?platform=web&product=call&menulabel=web) и получите `SDKAppID и SDKSecretKey`**, затем заполните их в файле **TUIRoomKit/Electron/example/vue3/packages/renderer/src/config/basic-info-config.js**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a2184e12c0ce11efad135254002693fd.png)

## Шаг 3. Запуск демонстрации

Запустите демонстрацию, введя команду в терминал.

```
npm run dev
```

> **Примечание:** Для локальной среды, пожалуйста, получайте доступ по протоколу localhost, обратитесь к [описанию протокола доступа к сети](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/tutorial-05-info-browser.html#h2-3).

## Шаг 4. Проведение первой конференции

1. Откройте страницу браузера и введите соответствующий URL.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0fcd1953bdfa11ef96d352540075b605.png)

2. Нажмите на **Новая комната** для создания вашей первой конференц-комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/11a416efbdfa11efb9d2525400329841.png)


---
*Источник: [https://trtc.io/document/60444](https://trtc.io/document/60444)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
