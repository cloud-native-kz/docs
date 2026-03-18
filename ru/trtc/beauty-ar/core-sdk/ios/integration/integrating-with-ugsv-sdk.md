# Интеграция с UGSV SDK

## Предварительные требования

1. Скачайте и распакуйте [демо-пакет](https://liteav.sdk.qcloud.com/download/latest/XiaoShiPin_UGC_iOS_latest.zip), затем скопируйте папку `xmagickit` из директории `demo/XiaoShiPin/` в директорию Podfile вашего проекта.
2. Добавьте следующие зависимости в ваш `Podfile` и запустите `pod install`.

```
pod 'xmagickit', :path => 'xmagickit/xmagickit.podspec'
```

3. Установите `Bundle ID` на bundle ID, привязанный к вашей лицензии.

### Требования к окружению

- Xcode 11 или позже (загрузите из App Store или [отсюда](https://developer.apple.com/xcode/resources/))
- Рекомендуемое окружение выполнения:
  - Требования к устройству: iPhone 5 или позже. iPhone 6 и старые модели поддерживают до 720p для фронтальной камеры.
  - Требования к системе: iOS 12.0 или позже.

## Интеграция API SDK

### Шаг 1. Аутентификация

Добавьте следующий код в `didFinishLaunchingWithOptions` класса `AppDelegate` (`LicenseURL` и `LicenseKey` — это информация об авторизации, полученная от Tencent Cloud; см. [Активировать сервис](https://www.tencentcloud.com/document/product/1143/69831)). Если версия вашего SDK ранее 2.5.1, вы можете найти `TELicenseCheck.h` в `XMagic.framework`; если версия SDK 2.5.1 или позже, `TELicenseCheck.h` находится в `YTCommonXMagic.framework`.

```
[TXUGCBase setLicenceURL:LicenseURL key:LicenseKey];[TELicenseCheck setTELicense:LicenseURL key:LicenseKey completion:^(NSInteger authresult, NSString * _Nonnull errorMsg) {              if (authresult == TELicenseCheckOk) {                   NSLog(@"Authentication successful");               } else {                   NSLog(@"Authentication failed");               }       }];
```

**Коды ошибок аутентификации:**

| Код ошибки | Описание |
| --- | --- |
| 0 | Успешно. |
| -1 | Входной параметр неверен; например, `URL` или `KEY` пусты. |
| -3 | Ошибка загрузки. Проверьте параметры сети. |
| -4 | Не удалось получить информацию об аутентификации Tencent Effect из локальной системы, что может быть вызвано сбоем ввода-вывода. |
| -5 | Файл лицензии VCUBE TEMP пуст, что может быть вызвано сбоем ввода-вывода. |
| -6 | JSON поле в файле `v_cube.license` некорректно. Обратитесь в команду Tencent Cloud. |
| -7 | Проверка подписи не пройдена. Обратитесь в команду Tencent Cloud. |
| -8 | Ошибка расшифровки. Обратитесь в команду Tencent Cloud. |
| -9 | JSON поле в `TELicense` некорректно. Обратитесь в команду Tencent Cloud. |
| -10 | Информация об аутентификации Tencent Effect, полученная в Интернете, пуста. Обратитесь в команду Tencent Cloud. |
| -11 | Не удалось записать информацию об аутентификации SDK Tencent Effect в локальный файл, что может быть вызвано сбоем ввода-вывода. |
| -12 | Ошибка загрузки и не удалось проанализировать локальные ресурсы. |
| -13 | Ошибка аутентификации. |
| Прочие | Обратитесь в команду Tencent Cloud. |

### Шаг 2. Установите путь материалов SDK

```
CGSize previewSize = [self getPreviewSizeByResolution:self.currentPreviewResolution];NSString *beautyConfigPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) lastObject];beautyConfigPath = [beautyConfigPath stringByAppendingPathComponent:@"beauty_config.json"];NSFileManager *localFileManager=[[NSFileManager alloc] init];BOOL isDir = YES;NSDictionary * beautyConfigJson = @{};if ([localFileManager fileExistsAtPath:beautyConfigPath isDirectory:&isDir] && !isDir) {    NSString *beautyConfigJsonStr = [NSString stringWithContentsOfFile:beautyConfigPath encoding:NSUTF8StringEncoding error:nil];    NSError *jsonError;    NSData *objectData = [beautyConfigJsonStr dataUsingEncoding:NSUTF8StringEncoding];    beautyConfigJson = [NSJSONSerialization JSONObjectWithData:objectData                                            options:NSJSONReadingMutableContainers                                            error:&jsonError];}NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",                            @"root_path":[[NSBundle mainBundle] bundlePath],                            @"tnn_"                            @"beauty_config":beautyConfigJson};// Init beauty kitself.beautyKit = [[XMagic alloc] initWithRenderSize:previewSize assetsDict:assetsDict];
```

### Шаг 3. Добавьте слушатели журналов и событий

```
// Register log[self.beautyKit registerSDKEventListener:self];[self.beautyKit registerLoggerListener:self withDefaultLevel:YT_SDK_ERROR_LEVEL];
```

### Шаг 4. Настройте эффекты

```
- (int)configPropertyWithType:(NSString *_Nonnull)propertyType withName:(NSString *_Nonnull)propertyName withData:(NSString*_Nonnull)propertyValue withExtraInfo:(id _Nullable)extraInfo;
```

### Шаг 5. Отрендеризуйте видео

В обратном вызове предварительной обработки кадра создайте `YTProcessInput` и передайте `textureId` в SDK для отрисовки.

```
 [self.xMagicKit process:inputCPU withOrigin:YtLightImageOriginTopLeft withOrientation:YtLightCameraRotation0]
```

### Шаг 6. Приостановите/Возобновите SDK

```
[self.beautyKit onPause];[self.beautyKit onResume];
```

### Шаг 7. Добавьте панель эффектов в макет

```
UIEdgeInsets gSafeInset;#if __IPHONE_11_0 && __IPHONE_OS_VERSION_MAX_ALLOWED >= __IPHONE_11_0if(gSafeInset.bottom > 0){}if (@available(iOS 11.0, *)) {    gSafeInset = [UIApplication sharedApplication].keyWindow.safeAreaInsets;} else#endif    {        gSafeInset = UIEdgeInsetsZero;    }dispatch_async(dispatch_get_main_queue(), ^{    // Effect option UI    _vBeauty = [[BeautyView alloc] init];    [self.view addSubview:_vBeauty];    [_vBeauty mas_makeConstraints:^(MASConstraintMaker *make) {        make.width.mas_equalTo(self.view);        make.centerX.mas_equalTo(self.view);        make.height.mas_equalTo(254);        if(gSafeInset.bottom > 0.0){  // Adapt to full-view screen            make.bottom.mas_equalTo(self.view.mas_bottom).mas_offset(0);        } else {            make.bottom.mas_equalTo(self.view.mas_bottom).mas_offset(-10);        }    }];        _vBeauty.hidden = YES;});
```


---
*Источник: [https://trtc.io/document/73775](https://trtc.io/document/73775)*

---
*Источник (EN): [integrating-with-ugsv-sdk.md](./integrating-with-ugsv-sdk.md)*
