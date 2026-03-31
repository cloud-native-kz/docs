# Распознавание лиц

Обнаруживает, когда лицо частично захвачено или скрыто, а также когда присутствует несколько лиц; распознает 256 ключевых точек лица.

## Индекс изображения для 256 ключевых точек лица

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d9b5b0d1f54811ed95155254007e6a5b.png)

## Описание iOS API

### Руководство по интеграции для iOS

Инструкции по интеграции Beauty AR SDK для iOS см. в руководстве по интеграции [Integrating SDK (iOS)](https://www.tencentcloud.com/document/product/1143/60193).

### Регистрация прослушивателя Xmagic

```
/// @brief Прослушиватель событий SDK/// @param listener Прослушиватель событий SDK, включая события AI, советы и события ресурсов.- (void)registerSDKEventListener:(id<YTSDKEventListener> _Nullable)listener;
```

### Описание обратного вызова `YTSDKEventListener`

```
#pragma mark - Event callback APIs/// @brief API обратного вызова события SDK@protocol YTSDKEventListener <NSObject>/// @brief Обратный вызов события `YTDataUpdate`/// @param event: Обратный вызов в формате NSString*- (void)onYTDataEvent:(id _Nonnull)event;/// @brief Обратный вызов события AI/// @param event: Обратный вызов в формате dict- (void)onAIEvent:(id _Nonnull)event;/// @brief Обратный вызов события совета/// @param event: Обратный вызов в формате dict- (void)onTipsEvent:(id _Nonnull)event;/// @brief Обратный вызов события пакета ресурсов/// @param event: Обратный вызов в формате string- (void)onAssetEvent:(id _Nonnull)event;@end
```

После успешной конфигурации обратных вызовов **в версиях 2.6.0 и более ранних** SDK будет отправлять обратный вызов с данными о лице для каждого видеокадра.

```
- (void)onYTDataEvent:(id _Nonnull)event;
```

После успешной конфигурации обратных вызовов **в версии 3.0.0** SDK будет отправлять обратный вызов с данными о лице для каждого видеокадра.

```
- (void)onAIEvent:(id _Nonnull)event;   //onAIEvent callback funtion can get the data.   NSDictionary *eventDict = (NSDictionary *)event;    if (eventDict[@"ai_info"] != nil) {      NSLog(@"ai_info %@",eventDict[@"ai_info"]);    }
```

Возвращаемые данные находятся в формате JSON и включают следующие поля (подробнее о 256 ключевых точках лица см. иллюстрацию выше):

```
/// @note Список описаний полей/**| Поле | Тип | Диапазон значений | Описание || :---- | :---- |:---- | :---- || trace_id                     | int   | [1,INF)                      | ID лица. Если лица, полученные непрерывно из видеопотока, имеют одинаковый ID лица, они принадлежат одному и тому же человеку. || face_256_point               | float | [0,screenWidth] или [0,screenHeight] | 512 значений для 256 ключевых точек лица. (0,0) — верхний левый угол экрана. || face_256_visible             | float | [0,1]                        | Видимость 256 ключевых точек лица.                  || out_of_screen                | bool  | true/false                   | Находится ли лицо вне видимой области экрана.                       || left_eye_high_vis_ratio      | float | [0,1]                               | Процент ключевых точек с высокой видимостью для левого глаза.                                    || right_eye_high_vis_ratio     | float | [0,1]                               | Процент ключевых точек с высокой видимостью для правого глаза.                                   || left_eyebrow_high_vis_ratio  | float | [0,1]                        | Процент ключевых точек с высокой видимостью для левой брови.                   || right_eyebrow_high_vis_ratio | float | [0,1]                        | Процент ключевых точек с высокой видимостью для правой брови.                   || mouth_high_vis_ratio         | float | [0,1]                               | Процент ключевых точек с высокой видимостью для рта.                                     |**/- (void)onYTDataEvent:(id _Nonnull)event;
```


---
*Источник: [https://trtc.io/document/60198](https://trtc.io/document/60198)*

---
*Источник (EN): [face-recognition.md](./face-recognition.md)*
