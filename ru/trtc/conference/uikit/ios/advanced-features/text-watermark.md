# Текстовой водяной знак

## Описание функции

Conference (TUIRoomKit) поддерживает функцию текстового водяного знака, позволяя пользователям добавлять пользовательские текстовые водяные знаки на конференцию для защиты авторских прав на контент или передачи определенной информации. С помощью функции текстового водяного знака пользователи могут отображать личную информацию, названия компаний или темы конференции на экране конференции, повышая безопасность и профессионализм контента. В этой статье представлено подробное описание этой функции и объяснено, как использовать её в компоненте TUIRoomKit.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e98a071a798011efa87a525400bdab9d.png)

## Интеграция функции

### Включение водяного знака

В TUIRoomKit функция водяного знака отключена по умолчанию. Если вы хотите включить функцию текстового водяного знака, вы можете сделать это с помощью следующего кода.

Android

iOS

```
ConferenceSession.sharedInstance().enableWaterMark();
```

```
ConferenceSession.sharedInstance.enableWaterMark()
```

> **Примечание:** После включения текст водяного знака по умолчанию будет `Your userId (Your userName)`.

### Установка текста водяного знака

В TUIRoomKit вы можете настроить текст водяного знака в соответствии с вашими конкретными деловыми потребностями. Вы можете установить текст водяного знака, используя следующий код.

Android

iOS

```
ConferenceSession.sharedInstance().setWaterMarkText("yourWaterMarkText");  // Replace the string with the watermark content you need to set
```

```
ConferenceSession.sharedInstance.setWaterMarkText(waterMarkText: "yourWaterMarkText")  // Replace the string with the watermark content you need to set
```

## Кастомизация функции

Если текущий интерфейс не соответствует вашим требованиям, вы можете изменить исходный код для достижения желаемого эффекта интерфейса. Чтобы облегчить вам кастомизацию интерфейса, здесь приводится описание файлов, связанных с текстовым водяным знаком.

Android

iOS

Вы можете изменить исходный код в директории [Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/page/widget/WaterMark](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/page/widget/WaterMark) для достижения желаемого эффекта интерфейса. Чтобы облегчить вам кастомизацию интерфейса, здесь приводится описание файлов, связанных с текстовым водяным знаком.

```
// File Location: Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/page/widget/WaterMarkWaterMark                           // Directory related to text watermark views    âââ TextWaterMarkView.java      // Text watermark view    âââ WaterMarkLineStyle.java     // Text watermark style
```

Вы можете изменить исходный код в директории [iOS/TUIRoomKit/Source/View/Page/Widget/WaterMark](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/iOS/TUIRoomKit/Source/View/Page/Widget/WaterMark) для достижения желаемого эффекта интерфейса. Чтобы облегчить вам кастомизацию интерфейса, здесь приводится описание файлов, связанных с текстовым водяным знаком.

```
// File Location: iOS/TUIRoomKit/Source/View/Page/Widget/WaterMarkWaterMark                           // Directory related to text watermark views    âââ WaterMarkLayer.swift        // Text watermark view    âââ WaterMarkLineStyle.swift    // Text watermark style
```


---
*Источник: [https://trtc.io/document/64693](https://trtc.io/document/64693)*

---
*Источник (EN): [text-watermark.md](./text-watermark.md)*
