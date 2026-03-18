# Параметры эффектов

При использовании функции `setEffect` для обновления эффектов красоты вы можете обратиться к следующей таблице параметров. Константы `effectName`, указанные в таблице параметров, определены в файле `XmagicConstant.java` для Android и в файле `XmagicConstant.h` для iOS.

## Улучшение красоты, Улучшение фигуры

| **Тип** | **Название** | effectName |  | **effectValue** | **resourcePath** |
| --- | --- | --- | --- | --- | --- |
|  |  | Имя константы | **Значение константы** | Интенсивность эффекта | **Путь ресурса** |
| Фильтр красоты | Осветление - **Ярко белый** | BEAUTY_WHITEN0 | beauty.lutFoundationAlpha0 | 0 ~ 100 | До V3.9.0: НетV3.9.0 и позже: ãОпционально ãпользовательский путь белого lut |
|  | Осветление - **Натуральный** | BEAUTY_WHITEN | beauty.lutFoundationAlpha | 0 ~ 100 | До V3.9.0: НетV3.9.0 и позже: ãОпционально ãпользовательский путь белого lut |
|  | Осветление - **Розоватый белый** | BEAUTY_WHITEN2 | beauty.lutFoundationAlpha2 | 0 ~ 100 | До V3.9.0: НетV3.9.0 и позже: ãОпционально ãпользовательский путь белого lut |
|  | Осветление - **Холодный белый** | BEAUTY_WHITEN3 | beauty.lutFoundationAlpha3 | 0 ~ 100 | До V3.9.0: НетV3.9.0 и позже: ãОпционально ãпользовательский путь белого lut |
|  | Черный **(V3.7.0)** | BEAUTY_BLACK_1 | beauty.lutBlackAlpha1 | 0 ~ 100 | Нет |
|  | Коричневый **(V3.7.0)** | BEAUTY_BLACK_2 | beauty.lutBlackAlpha2 | 0 ~ 100 | Нет |
|  | Сглаживание - **Молодежное** | BEAUTY_SMOOTH | smooth.smooth | 0 ~ 100 | Нет |
|  | Сглаживание - **Текстура** **(V3.9.3)** | BEAUTY_SMOOTH2 | smooth.smooth2 | 0 ~ 100 | Нет |
|  | Сглаживание - **Реалистичное** **(V3.9.3)** | BEAUTY_SMOOTH3 | smooth.smooth3 | 0 ~ 100 | Нет |
|  | Сглаживание - **Классическое** **(V3.9.3)** | BEAUTY_SMOOTH4 | smooth.smooth4 | 0 ~ 100 | Нет |
|  | Ретушь кожи Gan (ретушь кожи AI) **(V3.9.3)** | BEAUTY_FACE_SKIN_RETOUCH | beauty.skinRetouch | 0 ~ 100 | Нет |
|  | Выделение кожи (V4.0.0) | BEAUTY_SKIN_HIGHLIGHT | beauty.skinHighlight | 0 ~ 100 | Нет |
|  | Розовая кожа | BEAUTY_ROSY | smooth.rosy | 0 ~ 100 | Нет |
| Регулировка экрана | Контрастность | BEAUTY_CONTRAST | beauty.imageContrastAlpha | -100 ~ 100 | Нет |
|  | Насыщенность | BEAUTY_SATURATION | smooth.saturation | -100 ~ 100 | Нет |
|  | Четкость | BEAUTY_CLEAR | beauty.lutClearAlpha | 0 ~ 100 | Нет |
|  | Заточка | BEAUTY_SHAPE | smooth.sharpen | 0 ~ 100 | Нет |
|  | Яркость **(V3.8.0)** | BEAUTY_IMAGE_BRIGHTNESS | beauty.imageBrightness | -100 ~ 100 | НЕТ |
|  | Шумоподавление **(V3.6.0)** | BEAUTY_IMAGE_DENOISE | postEffect.denoise | 0 ~ 100 | Нет |
|  | Теплота | BEAUTY_IMAGE_WARMTH | beauty.imageWarmth | -100 ~ 100 | Нет |
|  | Оттенок | BEAUTY_IMAGE_TINT | beauty.imageTint | -100 ~ 100 | Нет |
| Расширенная эстетика | Большие глаза | BEAUTY_ENLARGE_EYE | basicV7.enlargeEye | 0 ~ 100 | Нет |
|  | Светлые глаза | BEAUTY_EYE_LIGHTEN | beauty.eyeLighten | 0 ~ 100 | Нет |
|  | Расстояние между глазами | BEAUTY_EYE_DISTANCE | basicV7.eyeDistance | -100 ~ 100 | Нет |
|  | Уголки глаз | BEAUTY_EYE_ANGLE | basicV7.eyeAngle | -100 ~ 100 | Нет |
|  | Ширина глаз | BEAUTY_EYE_WIDTH | basicV7.eyeWidth | -100 ~ 100 | Нет |
|  | Высота глаз | BEAUTY_EYE_HEIGHT | basicV7.eyeHeight | -100 ~ 100 | Нет |
|  | Положение глаз **(V3.8.0)** | BEAUTY_EYE_POSITION | basicV7.eyePosition | -100 ~ 100 | Нет |
|  | Внешний уголок глаза **(V3.9.0)** | BEAUTY_EYE_OUT_CORNER | basicV7.eyeOutCorner | -100 ~ 100 | Нет |
|  | Мешки под глазами | BEAUTY_FACE_REMOVE_EYE_BAGS | beauty.removeEyeBags | 0 ~ 100 | Нет |
|  | Угол бровей | BEAUTY_EYEBROW_ANGLE | basicV7.eyebrowAngle | -100 ~ 100 | Нет |
|  | Расстояние между бровями | BEAUTY_EYEBROW_DISTANCE | basicV7.eyebrowDistance | -100 ~ 100 | Нет |
|  | Высота бровей | BEAUTY_EYEBROW_HEIGHT | basicV7.eyebrowHeight | -100 ~ 100 | Нет |
|  | Длина бровей | BEAUTY_EYEBROW_LENGTH | basicV7.eyebrowLength | -100 ~ 100 | Нет |
|  | Толщина бровей | BEAUTY_EYEBROW_THICKNESS | basicV7.eyebrowThickness | -100 ~ 100 | Нет |
|  | Хребет брови | BEAUTY_EYEBROW_RIDGE | basicV7.eyebrowRidge | -100 ~ 100 | Нет |
|  | Размер носа | BEAUTY_NOSE_THIN | basicV7.thinNose | 0 ~ 100 | Нет |
|  | Крылья носа | BEAUTY_NOSE_WING | basicV7.noseWing | -100 ~ 100 | Нет |
|  | Положение носа | BEAUTY_NOSE_HEIGHT | basicV7.noseHeight | -100 ~ 100 | Нет |
|  | Спинка носа | BEAUTY_NOSE_BRIDGE_WIDTH | basicV7.noseBridgeWidth | -100 ~ 100 | Нет |
|  | Переносица | BEAUTY_NASION | basicV7.nasion | -100 ~ 100 | Нет |
|  | Белые зубы | BEAUTY_TOOTH_WHITEN | beauty.toothWhiten | 0 ~ 100 | Нет |
|  | Форма губ | BEAUTY_MOUTH_SIZE | basicV7.mouthSize | -100 ~ 100 | Нет |
|  | Высота губ | BEAUTY_MOUTH_HEIGHT | basicV7.mouthHeight | -100 ~ 100 | Нет |
|  | Ширина губ | BEAUTY_MOUTH_WIDTH | basicV7.mouthWidth | -100 ~ 100 | Нет |
|  | Положение губ | BEAUTY_MOUTH_POSITION | basicV7.mouthPosition | -100 ~ 100 | Нет |
|  | Улыбающиеся губы | BEAUTY_SMILE_FACE | basicV7.smileFace | -100 ~ 100 | Нет |
|  | Ширина лица | BEAUTY_FACE_THIN | basicV7.thinFace | 0 ~ 100 | Нет |
|  | Худое лицо - **Натуральное** | BEAUTY_FACE_NATURE | basicV7.natureFace | 0 ~ 100 | Нет |
|  | Худое лицо - **Богиня** | BEAUTY_FACE_GODNESS | basicV7.godnessFace | 0 ~ 100 | Нет |
|  | Худое лицо - **Красавец** | BEAUTY_FACE_MALE_GOD | basicV7.maleGodFace | 0 ~ 100 | Нет |
|  | V-образное лицо | BEAUTY_FACE_V | basicV7.vFace | 0 ~ 100 | Нет |
|  | Узкая челюсть | BEAUTY_FACE_JAW | basicV7.faceJaw | 0 ~ 100 | Нет |
|  | Длина лица | BEAUTY_FACE_SHORT | basicV7.shortFace | 0 ~ 100 | Нет |
|  | Форма лица | BEAUTY_FACE_BASIC | liquefaction.basic3 | 0 ~ 100 | Нет |
|  | Подбородок | BEAUTY_FACE_THIN_CHIN | basicV7.chin | -100 ~ 100 | Нет |
|  | Лоб | BEAUTY_FACE_FOREHEAD | basicV7.forehead | -100 ~ 100 | Нет |
|  | Лоб 2 **(V3.9.1)** | BEAUTY_FACE_FOREHEAD2 | basicV7.forehead2 | -100 ~ 100 | Нет |
|  | Морщины | BEAUTY_FACE_REMOVE_WRINKLE | beauty.removeWrinkle | 0 ~ 100 | Нет |
|  | Линии улыбки | BEAUTY_FACE_REMOVE_LAW_LINE | beauty.removeLawLine | 0 ~ 100 | Нет |
|  | Скулы | BEAUTY_FACE_THIN_CHEEKBONE | basicV7.cheekboneThin | 0 ~ 100 | Нет |
| Макияж одной точкой | Помада |  BEAUTY_MOUTH_LIPSTICK | beauty.faceFeatureLipsLut | 0 ~ 100 | Абсолютный путь к изображению помады на мобильном телефоне или относительный путь к каталогу файла модели красоты. Пример: `/images/beauty/lips_fuguhong.png` |
|  | Румяна | BEAUTY_FACE_RED_CHEEK | beauty.faceFeatureRedCheek | 0 ~ 100 | Пример: `/images/beauty/saihong_jianyue.png` |
|  | Контур |  BEAUTY_FACE_SOFTLIGHT | beauty.faceFeatureSoftlight | 0 ~ 100 | Пример: `/images/beauty/liti_ziran.png` |
|  | Цвет волос **(V3.7.0)** | BEAUTY_HAIR_COLOR_LUT | beauty.hairColorLut | 0 ~ 100 | Пример: `/images/hair_color/red.png` |
|  | Тени для век |  BEAUTY_FACE_EYE_SHADOW | beauty.faceFeatureEyesMakeup.eyeShadow | 0 ~ 100 | Пример: `/images/beauty/eyes_makeup_eye_shadow_0-albatross.png` |
|  | Подводка для глаз |  BEAUTY_FACE_EYE_LINER | beauty.faceFeatureEyesMakeup.eyeLiner | 0 ~ 100 | Пример: `/images/beauty/eyes_makeup_eye_liner_0.png` |
|  | Накладные ресницы |  BEAUTY_FACE_EYELASH | beauty.faceFeatureEyesMakeup.eyelash | 0 ~ 100 | Пример: `/images/beauty/eyes_makeup_eyelash_0.png` |
|  | Брови |  BEAUTY_FACE_EYEBROW | beauty.faceFeatureEyesMakeup.eyebrow | 0 ~ 100 | Пример: `/images/beauty/eyes_makeup_eyebrow_0.png` |
|  | Радужка глаза |  BEAUTY_FACE_EYEBALL | beauty.faceFeatureEyesMakeup.eyeball | 0 ~ 100 | Пример: `/images/beauty/eyes_makeup_eyeball_0.png` |
|  | Веки **(V3.8.0)** | BEAUTY_FACE_MAKEUP_EYELIDS | beauty.faceFeatureEyesMakeup.eyelids | 0 ~ 100 | Пример: `/images/beauty/eyes_makeup_eyelids_kaishan.png` |
|  | Мешки под глазами **(V3.8.0)** | BEAUTY_FACE_MAKEUP_EYEWOCAN | beauty.faceFeatureEyesMakeup.eyewocan | 0 ~ 100 | Пример: `/images/beauty/eyes_makeup_eye_wocan_keai.png` |
| Улучшение фигуры | Одноклик похудение | BODY_AUTOTHIN_BODY_STRENGTH | body.autothinBodyStrength | 0 ~ 100 | Нет |
|  | Удлинение ног | BODY_LEG_STRETCH | body.legStretch | 0 ~ 100 | Нет |
|  | Тонкие ноги | BODY_SLIM_LEG_STRENGTH | body.slimLegStrength | 0 ~ 100 | Нет |
|  | Тонкая талия | BODY_WAIST_STRENGTH | body.waistStrength | 0 ~ 100 | Нет |
|  | Узкие плечи | BODY_THIN_SHOULDER_STRENGTH | body.thinShoulderStrength | 0 ~ 100 | Нет |
|  | Коррекция груди | BODY_ENLARGE_CHEST_STRENGTH | body.enlargeChestStrength | -100 ~ 100 | Нет |
|  | Размер головы | BODY_SLIM_HEAD_STRENGTH | body.slimHeadStrength | 0 ~ 100 | Нет |

## Фильтры, Косметика, Эффекты движения, Сегментация

| Тип | effectName |  | effectValue | **resourcePath** | **extraInfo** |
| --- | --- | --- | --- | --- | --- |
|  | Имя константы | **Значение константы** | **Интенсивность эффекта** | **Путь ресурса** | Дополнительные параметры (тип пары ключ-значение) |
| **Фильтр** |  EFFECT_LUT | lut | 0 ~ 100 | Абсолютный путь к изображению фильтра на мобильном устройстве, например: `/data/user/0/com.tencent.pitumotiondemo.effects/files/xmagic/light_material/lut/aiqing_lf.png` Если вы хотите отменить фильтр, введите здесь null | Нет |
| **Легкий макияж** **(V3.9.0)** | EFFECT_LIGHT_MAKEUP | light.makeup | 0~100 | Абсолютный путь к материалам красоты на мобильном телефоне. Чтобы отменить макияж красоты, заполните здесь 'null' |  **[Опционально]** `makeupLutStrength`: Интенсивность фильтра в материале макияжа, значение в диапазоне "0" - "100" |
| **Макияж** |  EFFECT_MAKEUP | makeup | 0 ~ 100 | Абсолютный путь к материалам красоты на мобильном телефоне. Чтобы отменить макияж красоты, заполните здесь 'null' | **[Опционально]** `makeupLutStrength`: Интенсивность фильтра в материале макияжа, значение в диапазоне "0" - "100" **[Опционально]** `mergeWithCurrentMotion`: Представляет, накладывается ли на текущий эффект движения, "true" или "false". Если это поле не заполнено, оно считается false |
| **Движение** |  EFFECT_MOTION | motion | Нет | Абсолютный путь к материалу эффектов движения на мобильном устройстве, например: `/data/user/0/com.tencent.pitumotiondemo.effects/files/xmagic/light_material/motion/video_keaituya` Если вы хотите отменить эффект движения, заполните здесь 'null' | **[Опционально]** `mergeWithCurrentMotion`: "true" или "false", указывает, накладывается ли на текущий эффект движения. Если это поле не заполнено, предполагается false |
| **Сегментация фона** **(обычная)** |  EFFECT_SEGMENTATION | segmentation | Нет | Абсолютный путь к материалу сегментации фона на мобильном телефоне. Если вы хотите отменить сегментацию, заполните здесь null | **[Опционально]** `mergeWithCurrentMotion`: "true" или "false", указывает, накладывается ли на текущий эффект движения. Если это поле не заполнено, предполагается false |
| **Сегментация фона** **(зеленый экран_1)** |  EFFECT_SEGMENTATION | segmentation | Нет | Абсолютный путь к материалу зеленого экрана сегментации фона 1 на мобильном телефоне. Если вы хотите отменить сегментацию, заполните здесь null | **[Обязательно]** `segType`: "green_background" **[Обязательно]** `bgType`: Определяемый пользователем тип фона, "0" представляет изображения (поддерживаемые форматы изображений: **png, jpg, jpeg**) или pag, "1" представляет видео **[Обязательно]** `bgPath`: Определяемый пользователем путь к изображению или видео фона **[Опционально]** `keyColor`: Цвет зеленого экрана RGB, формат выглядит как "#00ff00" **[Опционально]** `tex_protect_rect`: Область защиты зеленого экрана относится к области, которая остается неизменной и не заменяется. Например: `"[0.0,0.0,0.3,0.3]"`, Нижний левый угол экрана имеет координаты (0,0), а верхний правый угол имеет координаты (1,1). **[Опционально]** `mergeWithCurrentMotion`: "true" или "false", указывает, накладывается ли на текущий эффект анимации. Если это поле не заполнено, оно считается false |
| **Сегментация фона** **(зеленый экран V2)** **(V3.9.2)** |  EFFECT_SEGMENTATION | segmentation | Нет | Абсолютный путь к материалу зеленого экрана сегментации фона 2 на мобильном телефоне. Если вы хотите отменить сегментацию, заполните здесь null | **[Обязательно]** `segType`: "green_background_v2" **[Обязательно]** `bgType`: Определяемый пользователем тип фона, "0" представляет изображения (поддерживаемые форматы изображений: **png, jpg, jpeg**) или pag, "1" представляет видео **[Обязательно]** `bgPath`: Определяемый пользователем путь к изображению или видео фона **[Опционально]** `mergeWithCurrentMotion`: "true" или "false", указывает, накладывается ли на текущий эффект анимации. Если это поле не заполнено, оно считается false **[Опционально]** `green_params_v2`: Параметры тонкой настройки эффекта зеленого экрана, такие как `"[30,20,1,30,1]"`. [Описание подробных параметров](https://www.tencentcloud.com/document/product/1143/73789). **[Опционально]** `tex_protect_rect`: Область защиты зеленого экрана относится к области, которая остается неизменной и не заменяется. Например: `"[0.0,0.0,0.3,0.3]"`, Нижний левый угол экрана имеет координаты (0,0), а верхний правый угол имеет координаты (1,1). |
| **Сегментация фона** **(синий экран V2)** **(V3.9.2)** |  EFFECT_SEGMENTATION | segmentation | Нет | Абсолютный путь к материалу синего экрана сегментации фона на мобильном телефоне. Если вы хотите отменить сегментацию, заполните здесь null | **[Обязательно]** `segType`: "green_background_v2" **[Обязательно]** `bgType`: Определяемый пользователем тип фона, "0" представляет изображения (поддерживаемые форматы изображений: **png, jpg, jpeg**) или pag, "1" представляет видео **[Обязательно]** `bgPath`: Определяемый пользователем путь к изображению или видео фона **[Опционально]** `mergeWithCurrentMotion`: "true" или "false", указывает, накладывается ли на текущий эффект анимации. Если это поле не заполнено, оно считается false **[Опционально]** `green_params_v2`: Параметры тонкой настройки эффекта зеленого экрана, такие как `"[35,8,1,10,1]"`. [Описание подробных параметров](https://www.tencentcloud.com/document/product/1143/73789). **[Опционально]** `tex_protect_rect`: Область защиты зеленого экрана относится к области, которая остается неизменной и не заменяется. Например: `"[0.0,0.0,0.3,0.3]"`, Нижний левый угол экрана имеет координаты (0,0), а верхний правый угол имеет координаты (1,1). |
| **Сегментация фона** **(пользовательская)** |  EFFECT_SEGMENTATION | segmentation | Нет | Абсолютный путь к материалу сегментации фона на мобильном телефоне. Если вы хотите отменить сегментацию, заполните здесь null | **[Обязательно]** `segType`: "custom_background" **[Обязательно]** `bgType`: Определяемый пользователем тип фона, "0" обозначает изображение (поддерживаемые форматы изображений: **png, jpg, jpeg**) или pag, "1" указывает на видео **[Обязательно]** `bgPath`: Путь к определяемому пользователем изображению или видео фона **[Опционально]** `mergeWithCurrentMotion`: "true" или "false", указывает, накладывается ли на текущий эффект движения. Если это поле оставлено пусто, предполагается false |


---
*Источник: [https://trtc.io/document/60207](https://trtc.io/document/60207)*

---
*Источник (EN): [effect-parameters.md](./effect-parameters.md)*
