# Конфигурация анимодзи и виртуальных аватаров

Tencent Effect SDK поддерживает анимодзи и VR виртуальные аватары начиная с версии v0.3.0.

## Проверка поддержки

Анимодзи и VR виртуальные аватары требуют окружение WebGL2. SDK предоставляет статический метод для проверки поддержки браузером этой возможности.

```
import {ArSdk} from 'tencentcloud-webar'if (ArSdk.isAvatarSupported()) {    // Initialize the feature} else {    alert('This browser does not support virtual avatars')    // Hide the feature}
```

## Анимодзи

### Получение моделей

После инициализации вы можете получить встроенные модели. В настоящее время SDK предлагает четыре встроенные модели анимодзи.

```
const avatarARList = await sdk.getAvatarList('AR')
```

> **Примечание:** Конфигурация анимодзи и виртуальных аватаров автоматически удалит другие эффекты, такие как макияж и стикеры, и наоборот.

### Установка модели

После получения списка встроенных моделей вы можете выбрать одну, указав параметр `EffectId`.

```
ar.setAvatar({  mode: 'AR', // Set the mode to `VR`  effectId: avatarARList[0].EffectId// Pass in the built-in ID}, () => {  // success callback});
```

### Настройка пользовательской модели

Если вам требуется настроить пользовательскую модель, пожалуйста, [свяжитесь с нами](https://trtc.io/contact).

## VR Виртуальные аватары

### Получение моделей

Список встроенных моделей можно получить после инициализации SDK. В настоящее время SDK предлагает 10 виртуальных аватаров.

```
const avatarVRList = await sdk.getAvatarList('VR')
```

### Установка сцены

```
ar.setAvatar({  mode: 'VR', // Set `mode` to `VR`   effectId: avatarVRList[0].EffectId, // Pass in the built-in ID  backgroundUrl: 'https://webar-static.tencent-cloud.com/assets/background/1.jpg',}, () => {    // success callback});
```

> **Примечание:** Для установки VR сцены необходимо установить URL фонового изображения, иначе по умолчанию будет использован чёрный фон.

### Настройка пользовательской модели

Вы можете быстро настроить пользовательский виртуальный аватар двумя способами и напрямую использовать его в SDK.

- Вариант 1. `readyplayer.me`
- Вариант 2. [Vroid](https://vroid.com/en/studio)

При использовании любого из этих вариантов необходимо загрузить экспортированную модель на CDN и использовать URL для установки SDK.

```
ar.setAvatar({  mode: 'VR', // Set `mode` to `VR`   url: 'https://xxxx.glb', // Pass in the built-in ID  backgroundUrl: 'https://webar-static.tencent-cloud.com/assets/background/1.jpg',}, () => {    // success callback});
```

В настоящее время пользовательская модель может быть в формате GLB или VRM.


---
*Источник: [https://trtc.io/document/51231](https://trtc.io/document/51231)*

---
*Источник (EN): [configuring-animojis-and-virtual-avatars.md](./configuring-animojis-and-virtual-avatars.md)*
