# Использование распознавания жестов

Tencent Effect SDK поддерживает распознавание жестов рук начиная с версии v1.0.23.

## Включение модуля распознавания жестов рук

Включите модуль распознавания жестов рук при инициализации SDK.

```
import { ArSdk } from 'tencentcloud-webar';const sdk = new ArSdk( {   module: {     beautify: true, // Модуль красоты, макияжа и эффектов для лица     handGesture: true // Модуль распознавания жестов рук   },   auth: { // Информация аутентификации     licenseKey: 'xxxxxxxxx',     appId: 'xxx',     authFunc: authFunc   },   camera: { // Передайте параметры камеры        width: 1280,        height: 720   },   beautify: {      whiten: 0.1,      dermabrasion: 0.3,      eye: 0.2,      chin: 0,      lift: 0.1,      shave: 0.2   },   … // Дополнительные параметры конфигурации см. в ãDocumentation APIã })
```

## Прослушивание изменений жестов

После включения распознавания жестов событие `handGesture` срабатывает при обнаружении изменения жеста.

```
// После включения распознавания жестов оно срабатывает при обнаружении изменения жеста.sdk.on('handGesture',(hands)=>{    console.log('handGesture', hands) // Значение hands см. в разделе "Структура объекта Hand" ниже.    … // Другой бизнес-код, например установка эффектов через интерфейс setEffect SDK и т.д.})
```

## Структура объекта Hand

```
Hand: {    gesture: string // Название жеста, возможные значения: None, Thumb_Up, Thumb_Down, Victory, Pointing_Up, Open_Palm, ILoveYou, Closed_Fist.    handedness: string // Определена как левая или правая рука, значения: Left, Right.}Hands: Array<Hand>
```

## Список поддерживаемых жестов

| **Значение жеста рук** | **Описание** |
| --- | --- |
| None | Не распознан действительный жест |
| Thumb_Up | Палец вверх ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/91d39bd31b6d11f09240525400bf7822.png) |
| Thumb_Down | Палец вниз ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a7d5509a1b6d11f0897952540099c741.png) |
| Victory | Знак победы ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b5875ba41b6d11f091eb525400454e06.png) |
| Pointing_Up | Указание вверх ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c18c95fa1b6d11f091eb525400454e06.png) |
| Open_Palm | Открытая ладонь ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cd0ae7aa1b6d11f091eb525400454e06.png) |
| ILoveYou | Я тебя люблю ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/da52f8531b6d11f0abe05254005ef0f7.png) |
| Closed_Fist | Сжатый кулак ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ece4471f1b6d11f09240525400bf7822.png) |


---
*Источник: [https://trtc.io/document/69309](https://trtc.io/document/69309)*

---
*Источник (EN): [using-gesture-recognition.md](./using-gesture-recognition.md)*
