# Настройка сегментации

Модуль сегментации необходимо включить во время инициализации для реализации виртуальных фонов. Для получения дополнительной информации см. [Custom Stream or Image](https://www.tencentcloud.com/document/product/1143/50102) и [Built-in Camera](https://www.tencentcloud.com/document/product/1143/50101).

## Установка фона

```
const config = {  module: {      beautify: true, // Whether to enable the effect module, which offers beautification and makeup effects as well as stickers      segmentation: true // Whether to enable the segmentation module, which allows you to change the background      segmentationLevel: 0 // Switch background segmentation models supported since Versions 1.0.19  },  auth: authData, // The authentication information  input: stream, // The input stream  beautify: { // The effect parameters for initialization (optional)      whiten: 0.1,      dermabrasion: 0.3,      eye: 0.2,      chin: 0,      lift: 0.1,      shave: 0.2  },  background: {      type: 'blur' // Blur the background  }}const sdk = new ArSdk(  // Pass in a config object to initialize the SDK  config)
```

- Вы также можете изменить фон.

```
sdk.setBackground({  type: 'image', // The background image  src: 'https://webar-static.tencent-cloud.com/assets/background/1.jpg'})
```

- Поддержка динамических фонов видео-типа (**поддерживается с версии 1.0.23**):

```
sdk.setBackground({  type: 'video', // The background video  src: 'https://webar-static.tencent-cloud.com/assets/background/video-bg-1.mp4',})
```

## Использование прозрачных фонов

```
sdk.setBackground({    type: 'transparent'})
```

> **Примечание:** Имейте в виду следующее: Сегментация поддерживается как на мобильных, так и на настольных браузерах. Поскольку WebRTC не поддерживает альфа-каналы, вы можете использовать прозрачные фоны только локально. Прозрачность фона не будет работать после публикации. Прозрачность фона поддерживается на настольных Chrome и Firefox, но не поддерживается на настольных или мобильных Safari. Начиная с версии 1.0.19 и выше, поддерживается переключение моделей сегментации фона с параметрами: 0, 1, 2. Уровень 0 обеспечивает лучшую производительность, но относительно среднюю результативность сегментации. Уровень 1 обеспечивает умеренную производительность и эффект. Уровень 2 обеспечивает лучшие результаты сегментации и наибольшее время вывода, подходит для приложений с высокими требованиями к эффектам сегментации и низкими требованиями к производительности.

---
*Источник: [https://trtc.io/document/50105](https://trtc.io/document/50105)*

---
*Источник (EN): [configuring-segmentation.md](./configuring-segmentation.md)*
