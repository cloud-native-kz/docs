# Распознавание жестов

## Обзор

Введите текстуру OpenGL камеры и получите данные обнаружения жестов в реальном времени. Вы можете использовать эти данные для дальнейшей разработки.

## Руководство интеграции на iOS

Интегрируйте Beauty AR SDK на iOS. Подробнее см.: [Интеграция SDK (iOS)](https://www.tencentcloud.com/document/product/1143/60193).

## Вызов интерфейса iOS

1. Включите переключатель функции обнаружения жестов (в Xmagic.h)

```
- (void)setFeatureEnableDisable:(NSString *_Nonnull)featureName enable:(BOOL)enable;
```

Заполните featureName значением HAND_DETECT (можно импортировать из TEDefine.h) и установите enable в true.

2. Установите обратный вызов данных (в Xmagic.h)

```
- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;- (void)onAIEvent:(id)event{    NSDictionary *eventDict = (NSDictionary *)event;    if (eventDict[@"ai_info"] != nil) {      NSLog(@"ai_info %@",eventDict[@"ai_info"]);    }}
```

eventDict[@"ai_info"] — это возвращаемые данные строки с JSON структурой.

## Описание данных обратного вызова JSON

В данных обратного вызова JSON данные, связанные с жестами, находятся в "hand_info", формат следующий:

```
"hand_info": {â    "gesture": "PAPER",â    "hand_point_2d": [180.71888732910156, 569.2958984375, ... , 353.8714294433594, 836.246826171875]}
```

Объяснения для каждого поля в hand_info приведены ниже:

| Поле | Описание |
| --- | --- |
| gesture | Название типа жеста |
| hand_point_2d | Информация о данных захваченного жеста |

В настоящее время поддерживаются следующие жесты:

| Порядок | Жест | Название типа | Пример изображения |
| --- | --- | --- | --- |
| 1 | Сердце | HEART | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57270e64311a11ee9bd25254005c1bd1.png) |
| 2 | Жест с числом 5 (открытая ладонь) | PAPER | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/56fd6ba7311a11ee8de9525400c56988.png) |
| 3 | Жест с числом 2 | SCISSOR | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5710aad4311a11eeba71525400088f3a.png) |
| 4 | Кулак | FIST | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/570d3360311a11ee872a525400cea498.png) |
| 5 | Жест с числом 1 | ONE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/571a5fd5311a11ee872a525400cea498.png) |
| 6 | Я тебя люблю | LOVE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57184da3311a11ee872a525400cea498.png) |
| 7 | Палец вверх | LIKE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57243fed311a11ee872a525400cea498.png) |
| 8 | ОК | OK | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5731f138311a11ee872a525400cea498.png) |
| 9 | Рок | ROCK | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/573a2c03311a11ee8de9525400c56988.png) |
| 10 | Жест с числом 6 | SIX | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57487b1d311a11ee872a525400cea498.png) |
| 11 | Жест с числом 8 | EIGHT | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/575df525311a11ee8de9525400c56988.png) |
| 12 | Поднятие | LIFT | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57479456311a11eeba71525400088f3a.png) |
| 13 | Жест с числом 3 | THREE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/577a4ca5311a11ee8de9525400c56988.png) |
| 14 | Жест с числом 4 | FOUR | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/575872f9311a11ee9bd25254005c1bd1.png) |

Если жест не обнаружен, название типа жеста — OTHER.


---
*Источник: [https://trtc.io/document/60199](https://trtc.io/document/60199)*

---
*Источник (EN): [gesture-recognition.md](./gesture-recognition.md)*
