# Интеграция SDK

Если вы хотите быстро интегрировать и испытать функции BeautyAR, мы рекомендуем использовать подход [Integrating UIKit](https://www.tencentcloud.com/document/product/1143/60194).

Для тех, кто интегрирует эффекты красоты вместе с MLVB SDK / TRTC SDK / Short Video SDK(UGSV), пожалуйста, следуйте руководствам интеграции для [Integrating With MLVB SDK](https://www.tencentcloud.com/document/product/1143/73774), [Integrating With TRTC SDK](https://www.tencentcloud.com/document/product/1143/73773) и [Integrating With UGSV SDK](https://www.tencentcloud.com/document/product/1143/73775) соответственно.

Если вы предпочитаете не использовать UIKit и вместо этого непосредственно реализовать вызовы интерфейса Core SDK, вы можете следовать этому руководству для интеграции.

## Комплексный процесс интеграции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fe87dcb0a8e311f0b5345254005ef0f7.png)

## Предварительные условия

### Требования к окружению

- Xcode 11 или более поздняя версия (загрузите из App Store или [отсюда](https://developer.apple.com/xcode/resources/))
- Рекомендуемое рабочее окружение:
  - Требования к устройству: iPhone 5 или более поздней версии. iPhone 6 и более старые модели поддерживают до 720p для фронтальной камеры.
  - Требования к системе: iOS 10.0 или более поздняя версия.

### Импорт SDK

Вы можете использовать CocoaPods или загрузить и импортировать SDK вручную в свой проект.

CocoaPods

Ручной импорт

Динамическая загрузка и интеграция

1. **Установите CocoaPods.**

Введите следующую команду в терминал (сначала необходимо установить Ruby на вашем Mac):

```
sudo gem install cocoapods
```

2. **Создайте Podfile.**

Перейдите в каталог вашего проекта и введите следующую команду для создания Podfile в каталоге.

```
pod init
```

3. **Отредактируйте Podfile.**
  - Версия XMagic ранее 3.0.1:

Выберите версию для вашего проекта и отредактируйте Podfile:

    - **XMagic Standard.**

Отредактируйте Podfile следующим образом:

```
platform :ios, '9.0'target 'App' dopod 'XMagic'end
```

    - **XMagic Lite.**

Пакет установки XMagic Lite меньше, чем XMagic Standard. Он поддерживает только Basic A1-00, Basic A1-01 и Advanced S1-00. Отредактируйте Podfile следующим образом:

```
platform :ios, '9.0'target 'App' dopod 'XMagic_Smart'end
```

  - XMagic версия 3.0.1 и позже:

Выберите соответствующую версию на основе пакета вашего проекта и отредактируйте файл Podfile:

```
#Please install the corresponding library with 'pod install' based on your package#For example: if your package is of type 'all', then you only need to use pod 'TencentEffect_All'.#For example: if your package is of type 'S1-04', then you only need to use pod 'TencentEffect_S1-04'.pod 'TencentEffect_All'#pod 'TencentEffect_A1-00'#pod 'TencentEffect_A1-01'#pod 'TencentEffect_A1-02'#pod 'TencentEffect_A1-03'#pod 'TencentEffect_A1-04'#pod 'TencentEffect_A1-05'#pod 'TencentEffect_A1-06'#pod 'TencentEffect_S1-00'#pod 'TencentEffect_S1-01'#pod 'TencentEffect_S1-02'#pod 'TencentEffect_S1-03'#pod 'TencentEffect_S1-04'#pod 'TencentEffect_S1-05'#pod 'TencentEffect_S1-06'#pod 'TencentEffect_S1-07'#pod 'TencentEffect_X1-01'#pod 'TencentEffect_X1-02'
```

4. **Обновите локальный репозиторий и установите SDK.**

Введите следующую команду в окне терминала для обновления локального репозитория и установки SDK:

```
pod install
```

5. На вкладке **Build Settings** добавьте `-ObjC` к **Other Linker Flags**.
6. Измените bundle ID на bundle ID, привязанный к вашей лицензии.
1. Загрузите [SDK и ресурсы эффектов](https://trtc.io/zh/sdkDownload?id=beauty) и распакуйте файл. SDK находится в папке `frameworks`, а ресурсы bundle в `resources`.
2. **Если ваша версия SDK ранее 2.5.1:**

Откройте ваш проект Xcode и добавьте фреймворки из папки `frameworks` в ваш проект: выберите целевой объект для запуска, перейдите на вкладку **General**, разверните **Frameworks, Libraries, and Embedded Content** и нажмите **+** для добавления загруженных фреймворков, включая `XMagic.framework`, `YTCommonXMagic.framework` и `libpag.framework`, а также `MetalPerformanceShaders.framework`, `CoreTelephony.framework`, `JavaScriptCore.framework`, `VideoToolbox.framework` и `libc++.tbd`. При необходимости вы также можете добавить `Masonry.framework` (макет управления) и `SSZipArchive` (распаковка файлов).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa9633fc84ee11ed8467525400463ef7.png)

**Если ваша версия SDK 2.5.1 или позже:**

Откройте ваш проект Xcode и добавьте фреймворки из папки `frameworks` в ваш проект: выберите целевой объект для запуска, перейдите на вкладку **General**, разверните **Frameworks, Libraries, and Embedded Content** и нажмите **+** для добавления загруженных фреймворков, включая `XMagic.framework`, `YTCommonXMagic.framework`, `libpag.framework`, `Audio2Exp.framework` и `TEFFmpeg.framework(переименован в TECodec.framework после версии 3.0.0.)`, а также `MetalPerformanceShaders.framework`, `CoreTelephony.framework`, `JavaScriptCore.framework`, `VideoToolbox.framework` и `libc++.tbd`. При необходимости вы также можете добавить `Masonry.framework` (макет управления) и `SSZipArchive` (распаковка файлов).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa9a2af784ee11eda151525400c56988.png)

3. Добавьте ресурсы эффектов из папки `resources` в ваш проект.
4. На вкладке **Build Settings** добавьте `-ObjC` к **Other Linker Flags**.
5. Измените bundle ID на bundle ID, привязанный к вашей лицензии.

Чтобы уменьшить размер пакета SDK, вы можете динамически загружать необходимые ресурсы модуля и ресурсы анимированных эффектов (`MotionRes`, недоступны в некоторых базовых версиях SDK) с URL-адреса и, после загрузки, передать путь ресурсов в SDK.

Вы можете использовать существующий сервис загрузки, но мы рекомендуем использовать логику загрузки демонстрационной версии. Для подробных инструкций по реализации динамической загрузки см. раздел [Reducing SDK Size](https://www.tencentcloud.com/document/product/1143/60205).

## Импорт ресурсов эффектов

Если ваш пакет включает функции динамических эффектов и фильтров, вам необходимо загрузить соответствующие ресурсы со [страницы загрузки SDK](https://trtc.io/zh/sdkDownload?id=beauty). После распаковки импортируйте bundles из папки `resources/motionRes` в любой каталог вашего основного проекта по мере необходимости. После импорта это должно выглядеть как на изображении ниже, где `lut.bundle` содержит ресурсы фильтров, а остальные содержат ресурсы анимации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0035f63bfdbb11f094325254001d6acc.png)

Дополнительные конфигурации ресурсов см. в разделе [Material Usage (iOS)](https://www.tencentcloud.com/document/product/1143/73781).

### Конфигурация разрешений

Добавьте описания разрешений в файл `Info.plist`. Если этого не сделать, приложение аварийно завершит работу на iOS 10. Предоставьте приложению доступ к камере в **Privacy - Camera Usage Description**.

## Инструкции

### Шаг 1. Аутентификация

1. Подайте заявку на лицензию и получите `LicenseURL` и `LicenseKEY`. См. раздел [Activate the Service](https://www.tencentcloud.com/document/product/1143/69831).
2. Установите URL и ключ в коде инициализации вашего бизнес-модуля для загрузки лицензии. Избегайте загрузки непосредственно перед использованием. Вы также можете запустить загрузку в методе `didFinishLaunchingWithOptions` класса `AppDelegate` (значения `LicenseURL` и `LicenseKey` генерируются при привязке лицензии в консоли).

Если ваша версия SDK ранее 2.5.1, вы найдете `TELicenseCheck.h` в `XMagic.framework`; если ваша версия SDK 2.5.1 или позже, `TELicenseCheck.h` находится в `YTCommonXMagic.framework`. SDK можно использовать только после успешной аутентификации.

```
[TELicenseCheck setTELicense:LicenseURL key:LicenseKey completion:^(NSInteger authresult, NSString * _Nonnull errorMsg) { if (authresult == TELicenseCheckOk) {     NSLog(@"Authentication successful"); } else {     NSLog(@"Authentication failed"); }}];
```

**Коды ошибок аутентификации:**

| Коды ошибок | Описание |
| --- | --- |
| 0 | Успешно. |
| -1 | Входной параметр недействителен; например, `URL` или `KEY` пусто. |
| -3 | Ошибка загрузки. Проверьте параметры сети. |
| -4 | Невозможно получить информацию об аутентификации Tencent Effect из локальной системы, что может быть вызвано ошибкой ввода-вывода. |
| -5 | Файл лицензии VCUBE TEMP пуст, что может быть вызвано ошибкой ввода-вывода. |
| -6 | Поле JSON в файле `v_cube.license` некорректно. Пожалуйста, свяжитесь с командой Tencent Cloud для получения помощи. |
| -7 | Ошибка проверки подписи. Пожалуйста, свяжитесь с командой Tencent Cloud для получения помощи. |
| -8 | Ошибка расшифровки. Пожалуйста, свяжитесь с командой Tencent Cloud для получения помощи. |
| -9 | Поле JSON в `TELicense` некорректно. Пожалуйста, свяжитесь с командой Tencent Cloud для получения помощи. |
| -10 | Информация об аутентификации Tencent Effect, проанализированная в Интернете, пуста. Пожалуйста, свяжитесь с командой Tencent Cloud для получения помощи. |
| -11 | Ошибка при записи информации об аутентификации SDK Tencent Effect в локальный файл, что может быть вызвано ошибкой ввода-вывода. |
| -12 | Ошибка загрузки, не удалось проанализировать локальные ресурсы. |
| -13 | Ошибка аутентификации. |
| Прочие | Пожалуйста, свяжитесь с командой Tencent Cloud для получения помощи. |

### Шаг 2. Инициализация и использование SDK

Ниже приводится процесс использования SDK Tencent Effect:

1. Загрузите ресурсы эффектов.

```
NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle", @"root_path":[[NSBundle mainBundle] bundlePath]  // The directory where LightCore.bundle is located.};
```

2. Инициализируйте Xmagic.

```
/**previewSize: View width and heightassetsDict: LightCore.bundle configured in the previous step and its path*/self.xMagicApi = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];
```

3. SDK обрабатывает каждый кадр данных и возвращает результаты.

```
/**Take the device camera data output as an example*///sampleBufferï¼Data output by the device camera-(CMSampleBufferRef)didProcessCPUData:(CMSampleBufferRef)sampleBuffer{    CVPixelBufferRef pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer);    YTProcessInput *input = [[YTProcessInput alloc] init];    input.pixelData = [[YTImagePixelData alloc] init];    input.pixelData.data = pixelBuffer;    input.dataType = kYTImagePixelData;    YTProcessOutput *output = [self.xMagicKit process:input];    if (output.pixelData.data != nil) { //output.pixelData.dataï¼Data processed by Beauty Effeck SDK         CMSampleBufferRef outSampleBuffer = [self sampleBufferFromPixelBuffer:output.pixelData.data];        return outSampleBuffer;    }    return nil;}//PixelBuffer to sampleBuffer- (CMSampleBufferRef)sampleBufferFromPixelBuffer:(CVPixelBufferRef)pixelBuffer{    CFRetain(pixelBuffer);    CMSampleBufferRef outputSampleBuffer = NULL;    CMSampleTimingInfo timing = {kCMTimeInvalid, kCMTimeInvalid, kCMTimeInvalid};    CMVideoFormatDescriptionRef videoInfo = NULL;    OSStatus result = CMVideoFormatDescriptionCreateForImageBuffer(NULL, pixelBuffer, &videoInfo);    result = CMSampleBufferCreateForImageBuffer(kCFAllocatorDefault, pixelBuffer, true, NULL, NULL, videoInfo, &timing, &outputSampleBuffer);    CFArrayRef attachments = CMSampleBufferGetSampleAttachmentsArray(outputSampleBuffer, YES);    CFMutableDictionaryRef dict = (CFMutableDictionaryRef)CFArrayGetValueAtIndex(attachments, 0);    CFDictionarySetValue(dict, kCMSampleAttachmentKey_DisplayImmediately, kCFBooleanTrue);    CFRelease(videoInfo);    CFRelease(pixelBuffer);    return outputSampleBuffer;}
```

Дополнительные сведения о процессе прихорашивания и деталях API см. в разделе [API documentation](https://www.tencentcloud.com/document/product/1143/60202#process).

4. Освободите Xmagic.

```
// Called where SDK resources need to be released[self.xMagicApi deinit]
```

> **Примечание:** После завершения вышеуказанных шагов вы можете контролировать время отображения и другие параметры окружения устройства по мере необходимости.


---
*Источник: [https://trtc.io/document/60193](https://trtc.io/document/60193)*

---
*Источник (EN): [integrating-sdk.md](./integrating-sdk.md)*
