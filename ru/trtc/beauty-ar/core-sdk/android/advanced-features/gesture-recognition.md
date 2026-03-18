# Распознавание жестов

## Обзор

Введите текстуру OpenGL камеры и получите данные распознавания жестов в реальном времени. Вы можете использовать эти данные для дальнейшей разработки.

## Руководство интеграции на Android

Интегрируйте Beauty AR SDK на Android, подробности см. в разделе: [Интеграция SDK (Android)](https://www.tencentcloud.com/document/product/1143/60195).

## Вызов интерфейсов Android

1. Включите переключатель функции распознавания жестов (в XmagicApi.java)

```
public void setFeatureEnableDisable(String featureName, boolean enable);
```

Заполните featureName значением XmagicConstant.FeatureName.HAND_DETECT и установите enable в true.

2. Установите обратный вызов данных (в XmagicApi.java)

```
void setAIDataListener(XmagicApi.OnAIDataListener aiDataListener)public interface OnAIDataListener {    void onFaceDataUpdated(List<TEFaceData> faceDataList);    void onHandDataUpdated(List<TEHandData> handDataList);    void onBodyDataUpdated(List<TEBodyData> bodyDataList);    void onAIDataUpdated(String data);}
```

onAIDataUpdated возвращает строковые данные с структурой JSON.

## Описание данных обратного вызова JSON

В данных обратного вызова JSON данные, относящиеся к жестам, находятся в "hand_info", и их формат выглядит следующим образом:

```
"hand_info": {â    "gesture": "PAPER",â    "hand_point_2d": [180.71888732910156, 569.2958984375, ... , 353.8714294433594, 836.246826171875]}
```

Описание каждого поля в hand_info приведено ниже:

| Поле | Описание |
| --- | --- |
| gesture | Название типа жеста |
| hand_point_2d | Информация захватанных данных жеста |

В настоящее время поддерживаются следующие жесты:

| Порядок | Жест | Название типа | Пример изображения |
| --- | --- | --- | --- |
| 1 | Сердце | HEART | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57270e64311a11ee9bd25254005c1bd1.png) |
| 2 | Жест с числом 5 (раскрытый) | PAPER | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/56fd6ba7311a11ee8de9525400c56988.png) |
| 3 | Жест с числом 2 | SCISSOR | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5710aad4311a11eeba71525400088f3a.png) |
| 4 | Кулак | FIST | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/570d3360311a11ee872a525400cea498.png) |
| 5 | Жест с числом 1 | ONE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/571a5fd5311a11ee872a525400cea498.png) |
| 6 | Я тебя люблю | LOVE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57184da3311a11ee872a525400cea498.png) |
| 7 | Большой палец вверх | LIKE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57243fed311a11ee872a525400cea498.png) |
| 8 | OK | OK | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5731f138311a11ee872a525400cea498.png) |
| 9 | Рок | ROCK | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/573a2c03311a11ee8de9525400c56988.png) |
| 10 | Жест с числом 6 | SIX | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57487b1d311a11ee872a525400cea498.png) |
| 11 | Жест с числом 8 | EIGHT | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/575df525311a11ee8de9525400c56988.png) |
| 12 | Поднять | LIFT | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57479456311a11eeba71525400088f3a.png) |
| 13 | Жест с числом 3 | THREE | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/577a4ca5311a11ee8de9525400c56988.png) |
| 14 | Жест с числом 4 | FOUR | ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/575872f9311a11ee9bd25254005c1bd1.png) |

Если жест не распознан, название типа жеста — OTHER.


---
*Источник: [https://trtc.io/document/60309](https://trtc.io/document/60309)*

---
*Источник (EN): [gesture-recognition.md](./gesture-recognition.md)*
