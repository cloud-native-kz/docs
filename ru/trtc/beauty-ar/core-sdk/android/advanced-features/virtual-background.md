# Виртуальный фон

Точно удаляет фон в режиме реального времени и применяет виртуальный фон (настраивается):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f3efaa5ea4c111f0b1565254001c06ec.png)

### Руководство интеграции Android

Руководство интеграции Android SDK. См. [Интеграция основного SDK (Android)](https://www.tencentcloud.com/document/product/1143/60195).

### Методология

```
setEffect(String effectName, int effectValue, String resourcePath, Map<String, String> extraInfo)
```

Подробное описание параметров см. в [setEffect](https://www.tencentcloud.com/document/product/1143/60201#32a345ed-73c4-4c60-bc7e-3f91b9a4755c).

### Параметры виртуального фона

```
mXmagicApi.setEffect(EffectName.EFFECT_SEGMENTATION, 45, AppConfig.motionResPath + "/segmentMotionRes/video_segmentation_blur_45", null);
```

### Параметры пользовательского фона

```
 Map<String, String> extraInfo = new HashMap<>(); extraInfo.put("segType", "custom_background"); extraInfo.put("bgType", "0"); extraInfo.put("bgPath", imgPath); mXmagicApi.setEffect(EffectName.EFFECT_SEGMENTATION, 0, AppConfig.motionResPath + "/segmentMotionRes/video_empty_segmentation", extraInfo);
```

###


---
*Источник: [https://trtc.io/document/60311](https://trtc.io/document/60311)*

---
*Источник (EN): [virtual-background.md](./virtual-background.md)*
