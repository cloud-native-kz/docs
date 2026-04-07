# Интеграция

Эта статья проведет вас через быструю интеграцию компонентов TUIRoomKit. Вы выполните несколько ключевых шагов менее чем за 10 минут и получите полный пользовательский интерфейс для многопользовательской конференции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bf302197021d11efaa01525400ae4d13.png)

## Демо TUIRoomKit

Вы можете посетить наше онлайн [демо TUIRoomKit](https://trtc.io/demo/homepage/#/detail?scene=roomkit), чтобы испытать больше функций TUIRoomKit.

Вы также можете посетить [Github](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Web), чтобы загрузить код TUIRoomKit и обратитесь к файлу README.md для запуска примера веб-проекта TUIRoomKit.

## Подготовка окружения

- Версия Node.js: Node.js ≥ 16.19.1 (рекомендуется использовать официальную версию LTS, и версия npm должна соответствовать версии node).
- Современный браузер, [поддерживающий WebRTC API](https://caniuse.com/?search=webrtc).

## Интеграция компонента TUIRoomKit

> **Примечание:** Если у вас **нет проекта vue**, вы можете напрямую обратиться к [примеру запуска демо](https://trtc.io/document/60441?platform=web&product=conference) через [Github](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Web) пример проекта.

Если вам нужно интегрировать его в существующий проект, выполните следующие шаги для интеграции.

### **Шаг 1: Установка зависимостей**

Vue3

Vue2

```
npm install @tencentcloud/roomkit-web-vue3 pinia --save
```

```
# Обратите внимание, что требуемая версия Vue >= 2.7.16. Если установка не удается, # пожалуйста, проверьте, поддерживается ли ваша версия Vue.npm install @tencentcloud/roomkit-web-vue2.7 pinia
```

> **Примечание:** пакет TUIRoomKit предоставляет компонент предварительного просмотра, компонент в ходе встречи и методы для запуска встреч, присоединения к встречам и точной настройки интерфейса. Подробнее см. [API RoomKit](https://trtc.io/document/54880?platform=web&product=conference). Если эти API не соответствуют вашим бизнес-требованиям, вы можете обратиться к [экспорту исходного кода UIKit](https://trtc.io/document/54851?platform=web&product=conference#method-2.3A-modify-the-uikit-source-code) для доступа к исходному коду TUIRoomKit.

### Шаг 2: Конфигурация инженерии проекта

**Регистрация Pinia**: TUIRoom использует Pinia для управления данными комнаты, и вам необходимо зарегистрировать Pinia в файле точки входа проекта. Файл точки входа проекта - это `src/main.ts`.

Vue3

Vue2

```
// src/main.tsimport { createPinia } from 'pinia';const app = createApp(App);// register piniaapp.use(createPinia()); app.mount('#app')
```

```
// src/main.tsimport { createPinia, PiniaVuePlugin } from 'pinia';Vue.use(PiniaVuePlugin);const pinia = createPinia();new Vue({  pinia,  render: h => h(App),}).$mount('#app');
```

### Шаг 3: Импорт компонента TUIRoom

> **Примечание:** Импортируйте компонент ConferenceMainView, который по умолчанию находится в [режиме постоянного отображения](https://www.tencentcloud.com/document/product/647/54880#1489e306-bc17-4bd2-b0bb-f4b8e3efad51) (компонент всегда отображается, и его отображение и скрытие не контролируются внутри. Если бизнес-сторона не контролирует его, компонент всегда будет оставаться видимым).

Vue3

Vue2

```
<template>  <ConferenceMainView></ConferenceMainView></template><script setup>import { ConferenceMainView } from '@tencentcloud/roomkit-web-vue3';</script>
```

```
<template>  <ConferenceMainView></ConferenceMainView></template><script>import { ConferenceMainView } from '@tencentcloud/roomkit-web-vue2.7';export default {  components: {    ConferenceMainView,  },};</script>
```

### Шаг 4: Вход в компонент TUIRoomKit

Перед инициированием встречи необходимо вызвать интерфейс [login](https://www.tencentcloud.com/document/product/647/54880#5a429689-e07a-4c01-bfc6-bfb67f7f5b7f) для аутентификации. Для получения `SDKAppID, userId, userSig` обратитесь к [активации сервиса](https://www.tencentcloud.com/document/product/647/59973#).

```
import { conference } from '@tencentcloud/roomkit-web-vue3';await conference.login({      sdkAppId: 0,  // Replace with your sdkAppId  userId: '',  // Replace with your userId  userSig: '',  // Replace with your userSig});
```

| **Параметр** | **Тип** | **Примечание** |
| --- | --- | --- |
| userID | String | **Уникальный идентификатор пользователя,** `определяемый вами`, **допускается содержать только прописные и строчные буквы (a-z, A-Z), цифры (0-9), подчеркивания и дефисы. |
| SDKAppID | Number | Уникальный идентификатор приложения для аудио и видео, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| SDKSecretKey | String | SDKSecretKey приложения для аудио и видео, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| userSig | String | Подпись защиты безопасности, используемая для аутентификации входа пользователя, чтобы подтвердить личность пользователя и предотвратить кражу прав на использование облачных сервисов злоумышленниками. |

> **Объяснение userSig:** **Окружение разработки:** Если вы запускаете демо локально и проводите отладку разработки, вы можете использовать функцию `genTestUserSig` (см. Шаг 3.2) в файле отладки для создания `userSig`. При таком методе SDKSecretKey уязвим для декомпиляции и обратного проектирования. Как только ваш ключ будет утечен, злоумышленники смогут украсть ваши права на использование облака Tencent. **Окружение производства:** Если ваш проект идет в продакшн, пожалуйста, используйте метод [Генерация UserSig на стороне сервера](https://trtc.io/document/35166).

### Шаг 5: Запуск новой встречи

Хост конференции может запустить новую конференцию, вызвав интерфейс [start](https://www.tencentcloud.com/document/product/647/54880#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd). Другие участники могут обратиться к описанию в [шаге 6](https://www.tencentcloud.com/document/product/647/54845#061c9593-1112-4763-aff2-7289b3af0c41) и вызвать интерфейс join для [присоединения](https://www.tencentcloud.com/document/product/647/54880#b08d0951-c1f4-4db4-a84d-8414b853d0f1) к конференции.

```
// Обратите внимание на имя пакета, если вы используете версию vue2, измените имя пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';const startConference = async () => {    await conference.login({          sdkAppId: 0,  // Replace with your sdkAppId      userId: '',  // Replace with your userId      userSig: '',  // Replace with your userSig    });    await conference.start('123456', {      roomName: 'TestRoom',      isSeatEnabled: false,      isOpenCamera: false,      isOpenMicrophone: false,    });}startConference()
```

### Шаг 6: Вход в существующую встречу

Участники могут [присоединиться](https://www.tencentcloud.com/document/product/647/54880#b08d0951-c1f4-4db4-a84d-8414b853d0f1) к конференции, инициированной хостом конференции в [шаге 5](https://www.tencentcloud.com/document/product/647/54845#7e2fb3c2-2b17-4445-985d-4af641ff66be), вызвав интерфейс join и заполнив соответствующий параметр roomId.

```
// Обратите внимание на имя пакета, если вы используете версию vue2, измените имя пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';const joinConference = async () => {    await conference.login({          sdkAppId: 0,  // Replace with your sdkAppId      userId: '',  // Replace with your userId      userSig: '',  // Replace with your userSig    });    await conference.join('123456', {      isOpenCamera: false,      isOpenMicrophone: false,    });}joinConference()
```

## Запуск в окружении разработки

1. Выполните команду окружения разработки. (Здесь мы берем проект vue3 + vite по умолчанию в качестве примера. Инструкции dev различных проектов могут отличаться. Пожалуйста, отрегулируйте в соответствии с вашим собственным проектом)

```
npm run dev
```

2. В соответствии с подсказками консоли откройте страницу в браузере, например: http://localhost:3000/.
3. Испытайте функции компонента TUIRoomKit.

## Развертывание в окружении производства

1. Упакуйте файл dist.

```
npm run build
```

2. Разверните файл dist на сервер.

> **Примечание:** Окружение производства требует использования доменного имени HTTPS.

## Другие документы

- [TUIRoomKit](https://www.tencentcloud.com/document/product/647/54880#)
- [Быстрый старт демо TUIRoom](https://github.com/tencentyun/TUIRoom/tree/main/Web)
- [Настройка интерфейса (TUIRoomKit)](https://www.tencentcloud.com/document/product/647/54851#)
- [Часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/37340#)

## Общение и обратная связь

Если у вас есть какие-либо вопросы или обратная связь, вы можете связаться с нами: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/54845](https://trtc.io/document/54845)*

---
*Источник (EN): [integration.md](./integration.md)*
