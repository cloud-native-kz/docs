# Снижение размера SDK

## Динамическая загрузка ресурсов модели BeautyAR

Чтобы уменьшить размер пакета, вы можете загружать требуемый ресурс модели красоты и ресурс динамического эффекта MotionRes (некоторые базовые версии SDK не имеют ресурса динамического эффекта) онлайн. После успешной загрузки установите путь к файлу в SDK. См. демонстрацию: [TEBeauty_Download_Example](https://github.com/Tencent-RTC/TencentEffect_iOS/tree/main/TEBeauty_Download_Example).

1. Загрузите ZIP-пакет ресурса модели эффекта красоты в облако и создайте URL для загрузки, например `https://server_address/LightCore.bundle.zip`.
2. Используйте созданный URL в проекте для загрузки файла и распаковки его в песочницу (пример: путь песочницы `Document/Xmagic`). На этом этапе папка Document/Xmagic содержит ресурсы, необходимые для SDK.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2b57cba864c411ed83b6525400c56988.png)

3. Во время инициализации SDK введите путь песочницы из предыдущего шага в поле root_path.

```
 NSDictionary *assetsDict = @{@"core_name":@"LightCore.bundle",                           @"root_path":_filePath //_filePath is the parent directory after beauty resource is downloaded to local:xx/Ducument/Xmagic, }; // Init beauty kit                                 @"root_path":Ducument/Xmagic, self.beautyKit = [[XMagic alloc] initWithRenderSize:_inputSize assetsDict:assetsDict];
```

## Загрузка ресурсов фильтров и эффектов движения

- Каждый фильтр — это изображение в формате png, а каждый эффект движения — это папка. Для ресурсов фильтров и эффектов движения рекомендуется загружать один элемент при каждом клике пользователя для использования. После успешной загрузки вызовите API SDK [setEffect](https://www.tencentcloud.com/document/product/1143/60202#setEffect) и установите путь к фильтру или путь к папке эффекта движения в SDK.
- Ресурсы фильтров и эффектов движения можно сохранять в любом каталоге мобильного телефона. Рекомендуется сохранять их в приватном каталоге приложения, чтобы избежать случайного удаления.


---
*Источник: [https://trtc.io/document/60205](https://trtc.io/document/60205)*

---
*Источник (EN): [reducing-sdk-size.md](./reducing-sdk-size.md)*
