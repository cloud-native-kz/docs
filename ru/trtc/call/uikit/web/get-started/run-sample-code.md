# Запуск примера кода

В этой статье будет рассказано, как быстро реализовать демо аудио- и видеозвонков. Вы выполните следующие ключевые шаги в течение 10 минут и получите функцию видеозвонков с полным пользовательским интерфейсом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/be8d9e591bd211efa1975254005ac0ca.png)

## Подготовка среды

- [Node.js](https://nodejs.org/en/) версии 16+.
- Современный браузер с поддержкой WebRTC API.

## Шаг 1: Загрузите демо

1. Откройте терминал и клонируйте репозиторий.

```
git clone https://github.com/Tencent-RTC/TUICallKit.git
```

2. Установите зависимости.

React

Vue3

```
 cd ./TUICallKit/Web/basic-react
```

```
 cd ./TUICallKit/Web/basic-vue3
```

```
 npm install
```

## Шаг 2: Настройте демо

[Перейдите на страницу активации услуги](https://trtc.io/document/59832?platform=web&product=call&menulabel=web) и получите `SDKAppID и SDKSecretKey`**, затем заполните их в файле**`GenerateTestUserSig-es.js`.

React

Vue3

Путь к файлу: `TUICallKit/Web/basic-react/src/debug/GenerateTestUserSig-es.js`

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0cf5a502668411ef97015254002693fd.png)

Путь к файлу: `TUICallKit/Web/basic-vue3/src/debug/GenerateTestUserSig-es.js`

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2846515e668411efb0e2525400a9236a.png)

## Шаг 3: Запустите демо

Откройте терминал и скопируйте пример команды для запуска демо.

TUICallKit/Web/basic-react

TUICallKit/Web/basic-vue3

```
npm run dev
```

```
npm run dev
```

> **Предупреждение:****Для локальной среды получайте доступ по протоколу localhost. Для доступа в общественную сеть получайте доступ по протоколу HTTPS. Подробнее см.**[Инструкции по протоколам доступа в сеть](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/tutorial-05-info-browser.html#h2-3)**.**

## Шаг 4: Совершите свой первый вызов

1. Откройте страницу браузера, введите адрес запуска проекта и войдите с userID (определяется вами).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ca8e7485668311ef86bb525400fdb830.png)

2. Введите userID абонента и нажмите кнопку вызова, чтобы совершить свой первый вызов.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f06fe362668311efa32852540075b605.png)


---
*Источник: [https://trtc.io/document/60415](https://trtc.io/document/60415)*

---
*Источник (EN): [run-sample-code.md](./run-sample-code.md)*
