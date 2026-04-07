# Включение функций красоты и эффектов

Этот туториал в основном рассказывает о том, как реализовать функцию эффектов красоты в прямых трансляциях TRTC. С помощью управления красотой вы можете использовать следующие функции:

- Настройка "разглаживания кожи", "отбеливания", "румяна" и других эффектов красоты.
- Настройка "увеличения глаз", "сужения лица", "V-образного лица", "регулировки подбородка" и "укорочения лица", "сужения носа", "осветления глаз", "отбеливания зубов", "удаления мешков под глазами", "удаления морщин", "удаления морщин" и т.д. для исправления специальных эффектов лица.
- Установка "линии волос", "расстояния между глазами", "уголков глаз", "формы рта", "ноздрей", "положения носа", "толщины губ" и "формы лица" и т.д. для исправления специальных эффектов лица.
- Настройка "теней для век", "румян" и других эффектов красоты.
- Настройка анимированных эффектов, таких как динамические стикеры и подвески на лице.

## Предварительные требования

Для использования функции эффектов красоты вам потребуется SDKAppID. Пожалуйста, убедитесь, что статус службы RTC в норме. В качестве альтернативы вы можете интегрировать **TEBeautyKit** для получения большего количества функций AR красоты. Подробности см. в разделе [Beauty AR](https://trtc.io/document/60216).

## Установка алгоритма красоты и уровня

TRTC предоставляет вам различные алгоритмы обработки кожи, включая **smooth**, **natural** и **optimal**, вы можете выбрать наиболее подходящее решение в соответствии с вашим продуктом.

В отличие от трех других платформ, для установки эффекта красоты через класс управления красотой `TXBeautyManager`, **платформа TRTC Windows** требует вызова [setBeautyStyle](https://trtc.io/document/50770#b7be60907f35f85041714fcedcc34719) для установки красоты, отбеливания, румяна и других специальных эффектов.

Android

iOS

Mac

Windows

```
// Declare the TRTCCloud variable and initializeprivate TRTCCloud mCloud;mCloud = TRTCCloud.sharedInstance(getApplicationContext());TXBeautyManager beautyManager = mCloud.getBeautyManager();beautyManager.setBeautyStyle(TXBeautyManager.TXBeautyStyleSmooth); // Beauty Style set to smoothbeautyManager.setBeautyLevel(9); // Beauty level set to 9
```

```
//  AppDelegate.h@property (nonatomic, strong) TRTCCloud *trtcCloud;//  AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance]; // Creating the TRTC instanceTXBeautyManager * beautyManager = [self.trtcCloud getBeautyManager];[beautyManager setBeautyStyle:TXBeautyStyleSmooth]; // Beauty Style set to smooth[beautyManager setBeautyLevel:9]; // Beauty level set to 9
```

```
//  AppDelegate.h@property (nonatomic, strong) TRTCCloud *trtcCloud;//  AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance]; // Creating the TRTC instanceTXBeautyManager * beautyManager = [self.trtcCloud getBeautyManager];[beautyManager setBeautyStyle:TXBeautyStyleSmooth]; // Beauty Style set to smooth[beautyManager setBeautyLevel:9]; // Beauty level set to 9
```

```
ITRTCCloud* trtc_cloud_;trtc_cloud_->setBeautyStyleSmooth(TRTCBeautyStyleSmooth, 5, 5, 5); // Set beauty, whitening, reddening and other special effects
```

> **Примечание:** Значение уровня красоты колеблется от 0 до 9, где 0 означает отключение, а 9 означает наиболее очевидный эффект. Если вы установите только стиль красоты, но не установите уровень красоты, вы не сможете увидеть эффект стиля красоты, так как уровень красоты по умолчанию равен 0.

## Установка уровня отбеливания и уровня румяна

Вызовите `setWhitenessLevel` и `setRuddyLevel` соответственно для установки уровня отбеливания и уровня румяна. Параметры двух указанных выше интерфейсов такие же, как у `setBeautyLevel`.

Android

iOS

Mac

```
// Declare the TRTCCloud variable and initializeprivate TRTCCloud mCloud;mCloud = TRTCCloud.sharedInstance(getApplicationContext());TXBeautyManager beautyManager = mCloud.getBeautyManager();beautyManager.setWhitenessLevel(9); // Whitening level set to 9beautyManager.setRuddyLevel(9); // Set the redness level to 9
```

```
//  AppDelegate.h@property (nonatomic, strong) TRTCCloud *trtcCloud;//  AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance]; // Creating the TRTC instanceTXBeautyManager * beautyManager = [self.trtcCloud getBeautyManager];[beautyManager setWhitenessLevel:9]; // Whitening level set to 9[beautyManager setRuddyLevel:9]; // Set the redness level to 9
```

```
//  AppDelegate.h@property (nonatomic, strong) TRTCCloud *trtcCloud;//  AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance]; // Creating the TRTC instanceTXBeautyManager * beautyManager = [self.trtcCloud getBeautyManager];[beautyManager setWhitenessLevel:9]; // Whitening level set to 9[beautyManager setRuddyLevel:9]; // Set the redness level to 9
```

## Установка эффекта цветного фильтра и интенсивности

Цветной фильтр — это изображение таблицы поиска цветов, содержащее отношение отображения цветов. В соответствии с отношением отображения в таблице поиска SDK будет проводить вторичную обработку исходного видеоизображения, захваченного камерой, для достижения ожидаемого эффекта фильтра.

Android

iOS

Mac

```
// Declare the TRTCCloud variable and initializeprivate TRTCCloud mCloud;mCloud = TRTCCloud.sharedInstance(getApplicationContext());TXBeautyManager beautyManager = mCloud.getBeautyManager();Bitmap filterMap = BitmapFactory.decodeResource(getResources(), R.drawable.filterImage);
beautyManager.setFilter(filterMap); // Set the filter effectbeautyManager.setFilterStrength(1); // Set the color filter strength to 1
```

```
//  AppDelegate.h@property (nonatomic, strong) TRTCCloud *trtcCloud;//  AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance]; // Creating the TRTC instanceTXBeautyManager * beautyManager = [self.trtcCloud getBeautyManager];UIImage *filterImage = [UIImage imageNamed:@"filterImage"];[beautyManager setFilter:filterImage]; // Set the filter effect[beautyManager setFilterStrength:1]; // Set the color filter strength to 1
```

```
//  AppDelegate.h@property (nonatomic, strong) TRTCCloud *trtcCloud;//  AppDelegate.m_trtcCloud = [TRTCCloud sharedInstance]; // Creating the TRTC instanceTXBeautyManager * beautyManager = [self.trtcCloud getBeautyManager];NSImage *filterImage = [NSImage imageNamed:@"filterImage"];[beautyManager setFilter:filterImage]; // Set the filter effect[beautyManager setFilterStrength:1]; // Set the color filter strength to 1
```

> **Примечание:** Диапазон значений интенсивности цветного фильтра составляет 0–1, значение по умолчанию — 0.5, чем больше значение, тем более очевидным будет эффект фильтра.

## Установка специальных эффектов

TRTC предоставляет разнообразные эффекты для лица на платформах Android и iOS, включая "увеличение глаз", "сужение лица", "V-образное лицо", "регулировка подбородка" и "укорочение лица", "сужение носа", "осветление глаз", "отбеливание зубов", "удаление мешков под глазами", "удаление морщин", "удаление морщин" и другие эффекты, которые требуют интеграции с **TEBeautyKit** для использования. См. [Интеграция TEBeautyKit на Android](https://trtc.io/document/60196?platform=android&product=beautyar) и [Интеграция TEBeautyKit на iOS](https://trtc.io/document/60194?platform=ios&product=beautyar).

- Справочник по продвинутым функциям красоты на **платформе Android:** [Android Tencent beauty effects SDK](https://trtc.io/document/45391)
- **На платформе iOS:** [iOS Tencent beauty effects SDK](https://trtc.io/document/45390)

## Свяжитесь с нами

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/64698](https://trtc.io/document/64698)*

---
*Источник (EN): [enabling-beauty-and-effects.md](./enabling-beauty-and-effects.md)*
