# Ключевые точки тела

## Обзор

Эта возможность обрабатывает текстуры OpenGL камеры и выводит данные о теле в 3D. Вы можете передать данные в Unity для управления вашей моделью или использовать данные для реализации других функций.

## Интеграция (Android)

Следуйте указаниям в [Интегрирование Tencent Effect SDK](https://www.tencentcloud.com/document/product/1143/60195) для интеграции Tencent Effect SDK.

### Вызовы API

1. Включите функцию (XmagicApi.java).

```
public void setFeatureEnableDisable(String featureName, boolean enable);
```

Установите `featureName` в `XmagicConstant.FeatureName.BODY_3D_POINT`.

2. Настройте обратный вызов данных (XmagicApi.java).

**Версия 2.6.0** и более ранние версии используют следующий метод.

```
void setYTDataListener(XmagicApi.XmagicYTDataListener ytDataListener)public interface XmagicYTDataListener { void onYTDataUpdate(String data)}
```

`onYTDataUpdate` возвращает строку JSON. Пример можно найти ниже.

  - `face_info` — это данные лица, которые не используются этой возможностью.
  - Значения полей в `body_3d_info` см. ниже.

**Версия 3.0.0** использует следующий метод.

```
void setAIDataListener(XmagicApi.OnAIDataListener aiDataListener)public interface OnAIDataListener {    void onFaceDataUpdated(List<TEFaceData> faceDataList);    void onHandDataUpdated(List<TEHandData> handDataList);    void onBodyDataUpdated(List<TEBodyData> bodyDataList);    void onAIDataUpdated(String data); //Этот метод — это новый метод, добавленный в версии 3.0.0, структура данных соответствует интерфейсу XmagicYTDataListener, используемому в предыдущих версиях.}
```

`onAIDataUpdated` возвращает строку JSON. Пример можно найти ниже.

  - `face_info` — это данные лица, которые не используются этой возможностью.
  - Значения полей в `body_3d_info` см. ниже.

## Ключевые точки тела и описания

- Ключевые точки SMPL.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6cce97fd865e11eda61e525400463ef7.png)

- Ключевые точки рук SMPL-X

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/601c5987866411eda151525400c56988.png)

Вот пример строки JSON, выводимой SDK:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6cd1e5fe865e11eda61e525400463ef7.png)

В следующем разделе приведены подробные сведения о полях в `body_3d_info`:

- `imageWidth` и `imageHeight`: ширина и высота изображений, отправляемых в SDK.
- `items`: массив. В настоящее время содержит только один элемент.
- `index`: зарезервированное поле. Вы можете его игнорировать.
- `pose`:
  - Позиция [0,2]. 3D местоположение (xyz) корневой кости тела с камерой в центре.
  - Позиция [3,12]. Форма тела. Включает 10 чисел с плавающей точкой на основе 10 сеток SMPL.
  - Позиция [13]. Фокусное расстояние, которое равно 5000.
  - Позиция [14,29]. Матрица проекции OpenGL в 3D пространстве, сгенерированная на основе фокусного расстояния. Матрица проекции 4 x 4 рассчитывается следующим образом в алгоритме:

```
matrix={    2 * focal_length / img_wid, 0, 0, 0,    0, 2 * focal_length / img_hei, 0,0,    0,0, (zf + zn) / (zn - zf), -1,    0, 0, (2.0f * zf * zn) / (zn - zf), 0};}
```

  - Позиция [30,33]. Находятся ли на земле левый палец, левая пятка, правый палец и правая пятка.
- position_x, position_y, position_z:
  - Позиция [0,23]. 2D ключевые точки тела (рисунок 1 выше). Значение `position_z` для всех 2D ключевых точек равно `0`.
  - Позиция [24,47]. 3D ключевые точки тела (рисунок 1 выше).
- rotation
  - Позиция [0,23]. Кватернионы ротации костей тела (wxyz).
  - Позиция [25,54]. Кватернионы ротации костей рук (wxyz). Для каждой руки есть 15 кватернионов.

## Названия костей

| Номер | Название кости | Название кости 2 |
| --- | --- | --- |
| 01234567891011121314151617181920212223 | "pelvis","left_hip","right_hip","spine1","left_knee","right_knee","spine2","left_ankle","right_ankle","spine3","left_foot","right_foot","neck","left_collar","right_collar","head","left_shoulder","right_shoulder","left_elbow","right_elbow","left_wrist","right_wrist","left_hand""right_hand" | "Hips""LeftUpLeg""RightUpLeg""Spine""LeftLeg""RightLeg""Spine1""LeftFoot""RightFoot""Spine2""""""Neck""LeftShoulder""RightShoulder""Head""LeftArm""RightArm""LeftForeArm""RightForeArm""LeftHand""RightHand""""" |
| 252627282930313233343536373839 | "left_index1""left_index2""left_index3""left_middle1""left_middle2""left_middle3""left_pinky1""left_pinky2""left_pinky3""left_ring1""left_ring2""left_ring3""left_thumb1""left_thumb2""left_thumb3 | IndexFinger1_LIndexFinger2_LIndexFinger3_LMiddleFinger1_LMiddleFinger2_LMiddleFinger3_LPinkyFinger1_LPinkyFinger2_LPinkyFinger3_LRingFinger1_LRingFinger2_LRingFinger3_LThumbFinger1_LThumbFinger2_LThumbFinger3_L |
| 404142434445464748495051525354 | "right_index1""right_index2""right_index3""right_middle1""right_middle2""right_middle3""right_pinky1""right_pinky2""right_pinky3""right_ring1""right_ring2""right_ring3""right_thumb1""right_thumb2""right_thumb3" | IndexFinger1_RIndexFinger2_RIndexFinger3_RMiddleFinger1_RMiddleFinger2_RMiddleFinger3_RPinkyFinger1_RPinkyFinger2_RPinkyFinger3_RRingFinger1_RRingFinger2_RRingFinger3_RThumbFinger1_RThumbFinger2_RThumbFinger3_R |


---
*Источник: [https://trtc.io/document/74184](https://trtc.io/document/74184)*

---
*Источник (EN): [body-keypoints.md](./body-keypoints.md)*
