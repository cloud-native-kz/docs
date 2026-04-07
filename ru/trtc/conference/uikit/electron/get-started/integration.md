# Интеграция

В этой статье описывается быстрая интеграция компонентов TUIRoomKit. Вы пройдёте через несколько ключевых этапов менее чем за 10 минут и получите полный пользовательский интерфейс для многопользовательской конференции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/70d5301470aa11ef92db52540055f650.png)

## Демонстрация TUIRoomKit

Вы можете скачать [версию для Mac OS](https://web.sdk.qcloud.com/trtc/electron/download/solution/TUIRoomKit/TUIRoomKit-Electron-mac-latest.zip) и [версию для Windows](https://web.sdk.qcloud.com/trtc/electron/download/solution/TUIRoomKit/TUIRoomKit-Electron-windows-latest.zip), чтобы опробовать больше функций TUIRoomKit Electron.
Вы можете перейти на [GitHub](https://github.com/tencentyun/TUIRoomKit) для скачивания кода TUIRoomKit и обратиться к документу README.md в репозитории для запуска примера проекта TUIRoomKit Electron.

## Подготовка окружения

- Версия Node.js: Node.js ≥ 16.19.1 (рекомендуется использовать официальную LTS версию; убедитесь, что версия npm совпадает с версией node).
- **Интеграция NPM пакета**
  - Среда разработки Vue3, интегрируйте NPM пакет [@tencentcloud/room-electron-vue3](https://www.npmjs.com/package/@tencentcloud/roomkit-electron-vue3).
  - Среда разработки Vue2.7: интегрируйте NPM пакет [@tencentcloud/roomkit-electron-vue2.7](https://www.npmjs.com/package/@tencentcloud/roomkit-electron-vue2.7).
- **Интеграция исходного кода**
  - Среда разработки Vue3 + TypeScript: скопируйте исходный код из NPM пакета [@tencentcloud/room-electron-vue3](https://www.npmjs.com/package/@tencentcloud/roomkit-electron-vue3).
  - Среда разработки Vue2.7 + TypeScript: скопируйте исходный код из NPM пакета [@tencentcloud/roomkit-electron-vue2.7](https://www.npmjs.com/package/@tencentcloud/roomkit-electron-vue2.7).
- **Шаблонный проект**
  - Electron + vite + vue3 [electron-vite-vue](https://github.com/electron-vite/electron-vite-vue)

## Интеграция компонента TUIRoomKit

Если **у вас нет проекта Vue**, вы можете перейти на [GitHub](https://github.com/Tencent-RTC/TUIRoomKit/tree/main) для скачивания кода TUIRoomKit и обратиться к README.md репозитория для запуска примера проекта TUIRoomKit Electron.

Если вам требуется интегрировать в существующий проект, выполните следующие шаги.

### **Шаг 1: Установка зависимостей**

Vue3

Vue2

```
npm install @tencentcloud/roomkit-electron-vue3 pinia@2.0.24 --save
```

```
# Обратите внимание, что здесь требуется версия Vue >= 2.7.16. Если установка не удаётся, проверьте, поддерживается ли ваша версия Vue
npm install @tencentcloud/roomkit-electron-vue2.7 pinia
```

> **Примечание:** Если вы выполняете интеграцию посредством скачивания шаблонного проекта [electron-vite-vue](https://github.com/electron-vite/electron-vite-vue), необходимо переключить шаблонный проект на версию v1.0.0. Вы можете обратиться к следующей инструкции:
> ```
> git clone https://github.com/electron-vite/electron-vite-vue.git
> cd electron-vite-vue
> git checkout v1.0.0
> ```

### **Шаг 2: Конфигурация проекта**

#### **1. Корректировка политик безопасности контента**

В системе Mac параметры политики безопасности контента по умолчанию вызовут ошибку при загрузке компонентов TUIRoomKit. Чтобы предотвратить отсутствие загрузки страниц TUIRoom или появление ошибок при вызовах интерфейса, можно откорректировать политику безопасности контента. Файл корректировки — `packages/renderer/index.html`.

```
<head>  <meta charset="UTF-8" />  <link rel="icon" href="/favicon.ico" />  <meta name="viewport" content="width=device-width, initial-scale=1.0" />  <!-- Измените этот параметр для Mac -->  <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline' 'unsafe-eval'; worker-src 'self' blob:;"/>  <title>Vite App</title></head>
```

#### **2. Регистрация Pinia**

TUIRoom использует Pinia для управления данными комнаты, поэтому необходимо зарегистрировать Pinia в файле входа проекта. Файл входа — это файл `src/main.ts`.

Vue3

Vue2

```
// файл src/main.ts
import { createPinia } from 'pinia';
const app = createApp(App);
// Регистрируем pinia
app.use(createPinia());
app.mount('#app')
```

```
// файл src/main.ts
import { createPinia, PiniaVuePlugin } from 'pinia';
Vue.use(PiniaVuePlugin);
const pinia = createPinia();
new Vue({
  pinia,
  render: h => h(App),
}).$mount('#app');
```

#### **3. Конфигурация vite.config.ts**

Чтобы унифицировать стиль кода и импортировать trtc-electron-sdk через import на уровне пользовательского интерфейса (в противном случае необходимо импортировать через require), требуется конфигурация в `packages/renderer/vite.config.ts`. Замените содержимое в resolve следующими элементами конфигурации, подробнее см. файл [packages/renderer/vite.config.ts](https://github.com/Tencent-RTC/TUIRoomKit/blob/main/Electron/example/vue3/packages/renderer/vite.config.ts).

> **Примечание:** Если ваш проект упакован с помощью vite, выполните следующие шаги для конфигурации. Причина в том, что vite по умолчанию поддерживает только модули ES6, а trtc-electron-sdk требует взаимодействия с API Node.js, который является модулем Common JS, поэтому этот шаг предназначен для совместимости типов модулей. Если ваш проект упакован с помощью webpack, вы можете пропустить этап vite.config.ts.

```
// vite.config.ts
export default defineConfig({
  // ...
  plugins: [
   resolve({
      'trtc-electron-sdk': `
          const TRTCCloud = require("trtc-electron-sdk");
          const TRTCParams = TRTCCloud.TRTCParams;
          const TRTCAppScene = TRTCCloud.TRTCAppScene;
          const TRTCVideoStreamType = TRTCCloud.TRTCVideoStreamType;
          const TRTCScreenCaptureSourceType = TRTCCloud.TRTCScreenCaptureSourceType;
          const TRTCVideoEncParam = TRTCCloud.TRTCVideoEncParam;
          const Rect = TRTCCloud.Rect;
          const TRTCAudioQuality = TRTCCloud.TRTCAudioQuality;
          const TRTCScreenCaptureSourceInfo = TRTCCloud.TRTCScreenCaptureSourceInfo;
          const TRTCDeviceInfo = TRTCCloud.TRTCDeviceInfo;
          const TRTCVideoQosPreference = TRTCCloud.TRTCVideoQosPreference;
          const TRTCQualityInfo = TRTCCloud.TRTCQualityInfo;
          const TRTCQuality = TRTCCloud.TRTCQuality;
          const TRTCStatistics = TRTCCloud.TRTCStatistics;
          const TRTCVolumeInfo = TRTCCloud.TRTCVolumeInfo;
          const TRTCDeviceType = TRTCCloud.TRTCDeviceType;
          const TRTCDeviceState = TRTCCloud.TRTCDeviceState;
          const TRTCBeautyStyle = TRTCCloud.TRTCBeautyStyle;
          const TRTCVideoResolution = TRTCCloud.TRTCVideoResolution;
          const TRTCVideoResolutionMode = TRTCCloud.TRTCVideoResolutionMode;
          const TRTCVideoMirrorType = TRTCCloud.TRTCVideoMirrorType;
          const TRTCVideoRotation = TRTCCloud.TRTCVideoRotation;
          const TRTCVideoFillMode = TRTCCloud.TRTCVideoFillMode;
          const TRTCRoleType = TRTCCloud.TRTCRoleType;
          const TRTCScreenCaptureProperty = TRTCCloud.TRTCScreenCaptureProperty;
          export {
            TRTCParams,
            TRTCAppScene,
            TRTCVideoStreamType,
            TRTCScreenCaptureSourceType,
            TRTCVideoEncParam,
            Rect,
            TRTCAudioQuality,
            TRTCScreenCaptureSourceInfo,
            TRTCDeviceInfo,
            TRTCVideoQosPreference,
            TRTCQualityInfo,
            TRTCStatistics,
            TRTCVolumeInfo,
            TRTCDeviceType,
            TRTCDeviceState,
            TRTCBeautyStyle,
            TRTCVideoResolution,
            TRTCVideoResolutionMode,
            TRTCVideoMirrorType,
            TRTCVideoRotation,
            TRTCVideoFillMode,
            TRTCRoleType,
            TRTCQuality,
            TRTCScreenCaptureProperty,
          };
          export default TRTCCloud.default;
        `,
    }),
  ]
});
```

### Шаг 3: **Подключение компонента TUIRoomKit**

> **Примечание:** Введите компонент ConferenceMainView, который по умолчанию находится в [режиме постоянной отображения](https://www.tencentcloud.com/document/product/647/54885#1489e306-bc17-4bd2-b0bb-f4b8e3efad51) (компонент всегда отображается, его видимость не контролируется внутренне. Без контроля со стороны бизнеса компонент останется видимым).

Vue3

Vue2

```
<template>
  <ConferenceMainView></ConferenceMainView>
</template>

<script setup>
import { ConferenceMainView } from '@tencentcloud/roomkit-electron-vue3';
</script>
```

```
<template>
  <ConferenceMainView></ConferenceMainView>
</template>

<script>
import { ConferenceMainView } from '@tencentcloud/roomkit-electron-vue2.7';
export default {
  components: {
    ConferenceMainView,
  },
};
</script>
```

### Шаг 4: Вход в компонент TUIRoomKit

Перед началом встречи необходимо вызвать интерфейс [login](https://www.tencentcloud.com/document/product/647/54885#5a429689-e07a-4c01-bfc6-bfb67f7f5b7f) для входа и получить sdkAppId, userId, userSig, как описано в разделе [Активация сервиса](https://www.tencentcloud.com/document/product/647/59973#).

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7
import { conference } from '@tencentcloud/roomkit-electron-vue3';

conference.login({
        sdkAppId: 0,  // Замените на ваш sdkAppId
    userId: '',  // Замените на ваш userId
    userSig: '',  // Замените на ваш userSig
});
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userID | String | Клиенты могут настроить ID пользователя в соответствии со своим бизнесом; допускаются только прописные и строчные английские буквы (a-z A-Z), цифры (0-9), подчеркивание и дефис. |
| sdkAppID | int | Уникальный идентификатор SDKAppID [активированного сервиса](https://www.tencentcloud.com/document/product/647/59973#), созданного в консоли TRTC для аудио/видео в реальном времени. |
| secretKey | String | SDKSecretKey [активированного сервиса](https://www.tencentcloud.com/document/product/647/59973#), созданного в консоли TRTC для аудио/видео в реальном времени. |
| userSig | String | Подпись защиты безопасности, используемая для аутентификации учётных данных входа пользователя, подтверждения подлинности пользователя и предотвращения кража вашего доступа к облачным сервисам злоумышленниками. |

> **Примечание:** Среда разработки: если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию **GenerateTestUserSig.genTestSig** для генерации userSig. SDKSecretKey в этом методе можно легко декомпилировать и обратить в обратном направлении, и после утечки ключа злоумышленники смогут украсть ваш трафик Tencent Cloud.
> 
> Производственная среда: если ваш проект должен быть развернут в сети Интернет, используйте метод [генерации UserSig на стороне сервера](https://www.tencentcloud.com/document/product/647/41664).

### Шаг пятый: Запуск новой встречи

Хозяин встречи может инициировать новую встречу, вызвав интерфейс [start](https://www.tencentcloud.com/document/product/647/54885#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd). Другие участники могут обратиться к описанию в [шаге шесть](https://www.tencentcloud.com/document/product/647/54844#061c9593-1112-4763-aff2-7289b3af0c41) и присоединиться к встречи, вызвав интерфейс [join](https://www.tencentcloud.com/document/product/647/54885#b08d0951-c1f4-4db4-a84d-8414b853d0f1).

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7
import { conference } from '@tencentcloud/roomkit-electron-vue3';

const startConference = async () => {
    await conference.login({
          sdkAppId: 0,  // Замените на ваш sdkAppId
      userId: '',  // Замените на ваш userId
      userSig: '',  // Замените на ваш userSig
    });
    await conference.start('123456', {
      roomName: 'TestRoom',
      isSeatEnabled: false,
      isOpenCamera: false,
      isOpenMicrophone: false,
    });
}

startConference()
```

### Шаг шесть: Вход в существующую встречу

Участники могут присоединиться к встречи, инициированной хозяином в [шаге пятом](https://www.tencentcloud.com/document/product/647/54844#7e2fb3c2-2b17-4445-985d-4af641ff66be), вызвав интерфейс [join](https://www.tencentcloud.com/document/product/647/54885#b08d0951-c1f4-4db4-a84d-8414b853d0f1) и заполнив соответствующий параметр roomId.

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7
import { conference } from '@tencentcloud/roomkit-electron-vue3';

const joinConference = async () => {
    await conference.login({
          sdkAppId: 0,  // Замените на ваш sdkAppId
      userId: '',  // Замените на ваш userId
      userSig: '',  // Замените на ваш userSig
    });
    await conference.join('123456', {
      isOpenCamera: false,
      isOpenMicrophone: false,
    });
}

joinConference()
```

## Работа в среде разработки

1. Выполните команду для среды разработки. (В качестве примера здесь используется проект vue3 + vite по умолчанию; однако команда dev может отличаться для разных проектов. Пожалуйста, отрегулируйте в соответствии с вашим проектом)

```
npm run dev
```

> **Примечание:** Если при выполнении возникают ошибки eslint в каталоге src/TUIRoom, вы можете добавить путь /src/TUIRoom/ в файл .eslintignore для игнорирования проверок eslint.

2. Испытайте функции компонента TUIRoomKit.

## Развёртывание в производственной среде

Упаковка проектов

```
npm run build
```

## Часто возникающие проблемы

### **Если при установке зависимостей на шаге 1 возникает проблема с несоответствием версий vue, как её решить?**

Вам необходимо зафиксировать версию **vue** на **3.3.13** в файле **package.json**

### **Если при выполнении происходит сбой приложения, как его решить?**

**Проблема может быть вызвана неспособностью получить разрешения на использование камеры и микрофона.**

Решение:

1. Пожалуйста, проверьте, работает ли устройство вашей камеры или микрофона должным образом и не занято ли оно другими приложениями.
2. В файле **/packages/main/index.ts** закомментируйте вызов метода `checkAndApplyDevicePrivilege`, чтобы пропустить проверку разрешений устройства.

### **Если вы столкнулись со следующей ошибкой на этапе выполнения или упаковки, как её решить?**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0ac2519e726611ef82535254002693fd.png)

**Вам необходимо включить опцию **allowJs** в файле **tsconfig.json**:**

```
// tsconfig.json
{
    "compilerOptions": {
      "allowJs": true    // ...Другие опции
  }
    // ...Другие опции
}
```

### **Если вы столкнулись со следующей ошибкой на этапе выполнения или упаковки, как её решить?**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0755158970ad11efbd54525400f69702.png)

Вам необходимо добавить следующее содержимое в файл **index.html**:

```
// index.html
<head>
  ....
  <script>const exports = module.exports;</script>
<head>
```

- [TUIRoomKit](https://www.tencentcloud.com/document/product/647/54885#)
- [Быстрый запуск TUIRoom Demo](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Electron)
- [Настройка пользовательского интерфейса (TUIRoomKit)](https://www.tencentcloud.com/document/product/647/54847#)
- [Часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/57419#)

## Связь и обратная связь

Если у вас есть какие-либо вопросы или предложения, вы можете связаться с нами: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/54844](https://trtc.io/document/54844)*

---
*Источник (EN): [integration.md](./integration.md)*
