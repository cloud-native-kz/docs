# Запуск примера кода

В этой статье описано, как быстро запустить пример проекта TUIRoomKit и испытать высококачественную видеоконференцию между несколькими участниками. Вы можете пройти демонстрацию менее чем за 10 минут и испытать многопользовательскую видеоконференцию с полноценным интерфейсом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fc2ad018bde711efb6f3525400dd4ba9.png)

## Предварительные требования

- Версия Node.js: Node.js ≥ 16.19.1 (рекомендуется использовать официальную версию LTS, версия npm должна соответствовать версии node).
- Современный браузер, [поддерживающий API WebRTC](https://caniuse.com/?search=webrtc).

## Шаг 1. Загрузка демонстрации

1. Откройте Терминал и скопируйте команду для клонирования репозитория.

```
git clone https://github.com/Tencent-RTC/TUIRoomKit.git
```

2. Установите зависимости.

Vue3

Vue2

```
cd ./TUIRoomKit/Web/example/vite-vue3-ts
```

```
cd ./TUIRoomKit/Web/example/webpack-vue2.7-ts
```

```
npm install
```

## Шаг 2. Конфигурация демонстрации

[Перейдите на страницу активации сервиса](https://trtc.io/document/59832?platform=web&product=call&menulabel=web) и получите `SDKAppID и SDKSecretKey`**, затем заполните их в файле **TUIRoomKit/Web/example/vite-vue3-ts/src/config/basic-info-config.js**.

> **Примечание:** Для проектов Vue2 откройте файл **TUIRoomKit/Web/example/webpack-vue2.7-ts/src/config/basic-info-config.js** и введите `SDKAppID и SDKSecretKey`, полученные при активации сервиса.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35094959bdec11efb51a525400bdab9d.png)

## Шаг 3. Запуск демонстрации

Запустите демонстрацию, введя команду в терминал.

Vue3

Vue2

```
npm run dev
```

```
npm run serve
```

> **Примечание:** Для локального окружения, пожалуйста, обращайтесь через протокол localhost. См. [описание протокола сетевого доступа](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/tutorial-05-info-browser.html#h2-3).

## Шаг 4. Проведение первой конференции

1. Откройте страницу браузера и введите соответствующий URL.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/31f031d4bdee11efb9d2525400329841.png)

2. Нажмите на **Новая комната** для создания вашей первой комнаты конференции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6f298dabdee11efba8d525400f69702.png)


---
*Источник: [https://trtc.io/document/60441](https://trtc.io/document/60441)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
