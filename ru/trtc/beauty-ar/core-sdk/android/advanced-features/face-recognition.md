# Распознавание лиц

Обнаруживает, когда лицо частично захвачено или скрыто, или когда присутствуют несколько лиц; распознает 256 точек лица.

## Индексное изображение для 256 точек лица

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d9b5b0d1f54811ed95155254007e6a5b.png)

## Руководство по интеграции для Android

Инструкции по интеграции Beauty AR SDK для Android см. в руководстве по интеграции [Интеграция SDK (Android)](https://www.tencentcloud.com/document/product/1143/60195).

## Регистрация слушателя Xmagic

Этот API используется для настройки обратного вызова точек лица и других данных.

**Версия 2.6.0** и более ранние версии используют следующий метод.

```
void setYTDataListener(XmagicApi.XmagicYTDataListener ytDataListener)public interface XmagicYTDataListener {    void onYTDataUpdate(String data)}
```

**Версия 3.0.0** использует следующий метод.

```
void setAIDataListener(XmagicApi.OnAIDataListener aiDataListener)public interface OnAIDataListener {    void onFaceDataUpdated(List<TEFaceData> faceDataList);    void onHandDataUpdated(List<TEHandData> handDataList);    void onBodyDataUpdated(List<TEBodyData> bodyDataList);    void onAIDataUpdated(String data); //This method is a new method added in version 3.0.0, and the data structure is consistent with the XmagicYTDataListener interface used in previous versions.}
```

`onYTDataUpdate` и `onAIDataUpdated` возвращают структуру JSON-строки, содержащую информацию до 5 лиц:

```
{ "face_info":[{  "trace_id":5,  "face_256_point":[    180.0,    112.2,    ...  ],  "face_256_visible":[    0.85,    ...  ],  "out_of_screen":true,  "left_eye_high_vis_ratio:1.0,  "right_eye_high_vis_ratio":1.0,  "left_eyebrow_high_vis_ratio":1.0,  "right_eyebrow_high_vis_ratio":1.0,  "mouth_high_vis_ratio":1.0 }, ... ]}
```

### Поля

| Поле | Тип | Диапазон значений | Описание |
| --- | --- | --- | --- |
| trace_id | int | [1,INF) | ID лица. Если лица, полученные непрерывно из видеопотока, имеют одинаковый ID лица, они принадлежат одному и тому же человеку. |
| face_256_point | float | [0,screenWidth] или [0,screenHeight] | 512 значений всего для 256 точек лица. (0,0) — верхний левый угол экрана. |
| face_256_visible | float | [0,1] | Видимость 256 точек лица. |
| out_of_screen | bool | true/false | Находится ли лицо вне области просмотра экрана. |
| left_eye_high_vis_ratio | float | [0,1] | Процент точек с высокой видимостью для левого глаза. |
| right_eye_high_vis_ratio | float | [0,1] | Процент точек с высокой видимостью для правого глаза. |
| left_eyebrow_high_vis_ratio | float | [0,1] | Процент точек с высокой видимостью для левой брови. |
| right_eyebrow_high_vis_ratio | float | [0,1] | Процент точек с высокой видимостью для правой брови. |
| mouth_high_vis_ratio | float | [0,1] | Процент точек с высокой видимостью для рта. |

#### Параметры

| Параметры | Описание |
| --- | --- |
| XmagicApi.XmagicYTDataListener ytDataListener | Класс реализации функции обратного вызова. |


---
*Источник: [https://trtc.io/document/60310](https://trtc.io/document/60310)*

---
*Источник (EN): [face-recognition.md](./face-recognition.md)*
