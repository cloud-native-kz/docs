# Опорные точки тела

## Обзор

Эта функция обрабатывает текстуры OpenGL камеры и выводит трёхмерные данные тела. Вы можете передать данные в Unity для управления вашей моделью или использовать данные для реализации других функций.

## Интеграция (iOS)

Следуйте указаниям в разделе [Интеграция Tencent Effect SDK](https://www.tencentcloud.com/document/product/1143/60193) для интеграции Tencent Effect SDK.

### Вызовы API

1. Включите функцию (XMagic.h).

```
- (void)setFeatureEnableDisable:(NSString *_Nonnull)featureName enable:(BOOL)enable;
```

Установите `featureName` в значение `XmagicConstant.FeatureName.BODY_3D_POINT`.

2. Настройте обратный вызов данных (XMagic.h).

**Версия 2.6.0** и более ранние версии используют следующий метод.

```
//XMagic.h- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;@implementation listener- (void)onYTDataEvent:(id)event{    NSLog(@"YTData %@", event);}@end
```

`onYTDataEvent` возвращает JSON-строку.

  - `face_info` — это данные лица, которые не используются этой функцией.
  - Значения полей в `body_3d_info` описаны ниже.

**Версия 3.0.0** использует следующий метод.

```
//XMagic.h- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;- (void)onAIEvent:(id)event{    NSDictionary *eventDict = (NSDictionary *)event;    if (eventDict[@"ai_info"] != nil) {      NSLog(@"ai_info %@",eventDict[@"ai_info"]);    }}
```

`eventDict[@"ai_info"]` возвращает JSON-строку.

  - `face_info` — это данные лица, которые не используются этой функцией.
  - Значения полей в `body_3d_info` описаны ниже.

## Опорные точки тела и их описания

Подробные сведения об опорных точках тела см. в разделе [Опорные точки тела и их описания](https://www.tencentcloud.com/document/product/1143/74184#c3fe9b5b-8422-4fcb-84aa-781a126dd4f6).


---
*Источник: [https://trtc.io/document/74185](https://trtc.io/document/74185)*

---
*Источник (EN): [body-keypoints.md](./body-keypoints.md)*
