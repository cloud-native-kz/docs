# Интеграция с MLVB SDK

BeautyAR Flutter SDK требует зависимости от BeautyAR SDK на стороне Android/iOS. Через плагины, предоставляемые Flutter, функции нативной части могут быть открыты для клиента Flutter. Поэтому при интеграции функций фильтра красоты вам необходимо вручную интегрировать SDK нативной части.

## Запуск демо

[Скачайте демо-проект](https://github.com/Tencent-RTC/TencentEffect_Flutter), измените файл `main.dart` в директории `demo/lib`, добавьте в этот файл ваши `licenseUrl` и `licenseKey`. Примеры кода использования функций красоты в MLVB находятся в основном в `demo/lib/page/live_page.dart` и `demo/lib/main.dart`.

Android

iOS

1. В demo/app найдите файл build.gradle, откройте его и измените значение `applicationId` на имя пакета, которое вы использовали при подаче заявки на лицензию.
2. В demo/lib выполните `flutter pub get`.
3. Откройте демо-проект в Android Studio и запустите его.
1. В директории demo выполните `flutter pub get`.
2. В директории demo/ios выполните `pod install`.
3. Откройте Runner.xcworkspace в Xcode.
4. Измените `bundle ID` проекта (должен совпадать с bundle ID, который вы указали при подаче заявки на лицензию).

## Интеграция SDK

### Нативная интеграция

Android

iOS

1. В модуле app найдите файл build.gradle и добавьте URL репозитория Maven для вашего соответствующего пакета. Например, если вы выбрали пакет S1-04, добавьте следующее:

```
dependencies {   implementation 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'}
```

**URL Maven, соответствующие каждому пакету, см. в**[документации](https://www.tencentcloud.com/document/product/1143/60195#e39cf4dd-0b61-47c1-92e8-710e762da797). Последний номер версии SDK можно найти в [Примечаниях к выпуску](https://www.tencentcloud.com/document/product/1143/60203).

2. В вашем проекте найдите модуль `android/app` и расположение папки `src/main/assets`. Скопируйте папки `demo/android/app/src/main/assetslut` и `MotionRes` из демо-проекта в директорию `android/app/src/main/assets` вашего проекта. Если в вашем проекте нет папки assets, вы можете создать её вручную.
3. Найдите файл AndroidManifest.xml под модулем app и добавьте следующий тег в раздел application:

```
   <uses-native-library            android:name="libOpenCL.so"            android:required="false" />        //true указывает, что libOpenCL необходима для текущего приложения. Без этой библиотеки система не позволит установить приложение        //false указывает, что libOpenCL не является обязательной для текущего приложения. Приложение можно установить нормально с библиотекой или без неё. Если на устройстве есть эта библиотека, эффекты типа GAN в Tencent Special Effects SDK (например, лицо сказки, лицо комикса) будут работать нормально. Если на устройстве нет этой библиотеки, эффекты типа GAN не будут работать, но это не повлияет на использование других функций в SDK.        //Информация о uses-native-library см. на официальном сайте Android: https://developer.android.com/guide/topics/manifest/uses-native-library-element
```

После добавления это выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bbb84547a55811ef9021525400f69702.png)

4. Конфигурация обфускации
  - Если вы включите оптимизацию компиляции (установите minifyEnabled в true) при упаковке релиза, это приведёт к удалению кода, который не вызывается на уровне Java. Этот код может быть вызван нативным уровнем, что может привести к исключению `no xxx method`.
  - Если вы включили такую оптимизацию компиляции, вы должны добавить эти правила keep, чтобы избежать удаления кода xmagic:

```
-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}-keep class com.tencent.effect.** { *;}
```

Скопируйте папку xmagic из директории ios/Runner демо-проекта в директорию ios/Runner вашего проекта. После добавления это выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bbb0617da55811efb7b7525400bdab9d.png)

> **Примечание:** Материалы, скопированные из демо-проекта, - это **тестовые материалы**. Официальные материалы необходимо получить у нас, [связавшись с сотрудниками](https://www.tencentcloud.com/document/product/1143/51280) после покупки пакета, а затем повторно добавить.

### Интеграция Flutter

#### **Способ 1:**

Удалённые зависимости, добавьте следующую ссылку в файл pubspec.yaml вашего проекта:

```
  tencent_effect_flutter:   git:     url: https://github.com/Tencent-RTC/TencentEffect_Flutter
```

#### **Способ 2**

Локальные зависимости, загрузите последнюю версию [tencent_effect_flutter](https://github.com/Tencent-RTC/TencentEffect_Flutter), затем добавьте папки android, ios, lib и файлы pubspec.yaml, tencent_effect_flutter.iml в директорию вашего проекта, а затем добавьте следующую ссылку в файл pubspec.yaml вашего проекта: (см. демо)

```
tencent_effect_flutter:    path: ../
```

Выполните следующую команду:

```
flutter pub get
```

> **Примечание:** tencent_effect_flutter предоставляет только мост, функция красоты зависит от SDK красоты, предоставляемых каждой платформой, поэтому если вам нужно обновить SDK красоты, вы можете обновить SDK, следуя следующим шагам: AndroidiOSНайдите файл build.gradle под модулем app в вашем проекте и измените поле `latest.release` в `implementation 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'` на последний номер версии. Если вам нужно изменить пакет, вам нужно изменить поле `TencentEffect_S1-04` на ваш пакет. **Необходимо изменить тип пакета и версию SDK:** Зависимость для Beauty Flutter SDK должна быть изменена на локальную зависимость. Найдите файл `ios/tencent_effect_flutter.podspec` в Beauty Flutter SDK, откройте его и измените `TencentEffect_All` на нужный вам пакет, вы также можете изменить номер версии на нужную вам версию. Выполните команду pod update в директории ios вашего проекта.

## Использование SDK

### 1. Связь с MLVB

Android

iOS

Добавьте следующий код в метод onCreate класса application (или метод onCreate FlutterActivity):

```
TXLivePluginManager.register(new XmagicProcesserFactory());
```

Добавьте следующий код в метод didFinishLaunchingWithOptions класса AppDelegate вашего приложения:

```
XmagicProcesserFactory *instance = [[XmagicProcesserFactory alloc] init];[TXLivePluginManager registerWithCustomBeautyProcesserFactory:instance];
```

После добавления это выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bbc669fda55811efbd5752540055f650.png)

### 2. Вызовите API инициализации ресурсов

v0.3.5.0 и более поздние

До v0.3.1.1

```
void _initSettings(InitXmagicCallBack callBack) async {  String resourceDir = await ResPathManager.getResManager().getResPath();  TXLog.printlog('$TAG method is _initResource ,xmagic resource dir is $resourceDir');  TencentEffectApi.getApi()?.setResourcePath(resourceDir);  /// Resource copying only needs to be done once. In the current version, if copied successfully once, there is no need to copy the resources again.  /// Copying the resource only needs to be done once. Once it has been successfully copied in the current version, there is no need to copy it again in future versions.  if (await isCopiedRes()) {    callBack.call(true);    return;  } else {    _copyRes(callBack);  }}void _copyRes(InitXmagicCallBack callBack) {  _showDialog(context);  TencentEffectApi.getApi()?.initXmagic((result) {    if (result) {      saveResCopied();    }    _dismissDialog(context);    callBack.call(result);    if (!result) {      Fluttertoast.showToast(msg: "initialization failed");    }  });}
```

```
String dir =  await BeautyDataManager.getInstance().getResDir(); TXLog.printlog('The file path: $dir'); TencentEffectApi.getApi()?.initXmagic(dir,(reslut) {     _isInitResource = reslut;     callBack.call(reslut);     if (!reslut) {         Fluttertoast.showToast(msg: "Failed to initialize the resources");     } });
```

### 3. Выполните авторизацию красоты

```
TencentEffectApi.getApi()?.setLicense(licenseKey, licenseUrl,           (errorCode, msg) {         TXLog.printlog("Print the authentication result errorCode = $errorCode   msg = $msg");         if (errorCode == 0) {            // Authentication succeeded         }       });
```

### 4. Включение/отключение фильтра красоты

```
/// Enable beauty filter operation/// Setting it to true enables the beauty filter, while setting it to false disables the beauty filter. var enableCustomVideo = await _livePusher.enableCustomVideoProcess(open);
```

> **Примечание:** При включении фильтра красоты на странице необходимо сначала отключить фильтр красоты перед закрытием камеры. Операции включения и отключения должны быть парными, чтобы обеспечить правильное функционирование.

### 5. Установка атрибутов красоты

v0.3.5.0 и более поздние

До v0.3.1.1

Для конкретных атрибутов красоты см. [Параметры эффектов](https://www.tencentcloud.com/document/product/1143/60207).

```
TencentEffectApi.getApi()?.setEffect(sdkParam.effectName!,    sdkParam.effectValue, sdkParam.resourcePath, sdkParam.extraInfo)
```

```
TencentEffectApi.getApi()?.updateProperty(_xmagicProperty!);/// You can call `BeautyDataManager.getInstance().getAllPannelData()` to get all the properties and call `updateProperty` to set properties.
```

### 6. Установка других свойств

- **Приостановка звуковых эффектов красоты**

```
 TencentEffectApi.getApi()?.onPause();
```

- **Возобновление звуковых эффектов красоты**

```
TencentEffectApi.getApi()?.onResume();
```

- **Мониторинг событий красоты**

```
TencentEffectApi.getApi()     ?.setOnCreateXmagicApiErrorListener((errorMsg, code) {       TXLog.printlog("Error creating an effect object errorMsg = $errorMsg , code = $code"); });   /// Needs to be set before creating the beauty filter
```

- **Установка обратного вызова для статуса обнаружения лица, жеста и тела**

```
TencentEffectApi.getApi()?.setAIDataListener(XmagicAIDataListenerImp());
```

- **Установка функции обратного вызова для динамических сообщений подсказок**

```
TencentEffectApi.getApi()?.setTipsListener(XmagicTipsListenerImp());
```

- **Конфигурация обратного вызова точек лица и других данных (доступно только в S1-05 и S1-06)**

```
TencentEffectApi.getApi()?.setYTDataListener((data) {   TXLog.printlog("setYTDataListener  $data"); });
```

- **Удаление всех обратных вызовов**

При завершении страницы необходимо удалить все обратные вызовы:

```
 TencentEffectApi.getApi()?.setOnCreateXmagicApiErrorListener(null); TencentEffectApi.getApi()?.setAIDataListener(null); TencentEffectApi.getApi()?.setYTDataListener(null); TencentEffectApi.getApi()?.setTipsListener(null);
```

> **Примечание:** Дополнительную информацию об API см. в [Документации API (Flutter)](https://www.tencentcloud.com/document/product/1143/60200). Для остального см. [Демо-проект](https://github.com/Tencent-RTC/TencentEffect_Flutter).

### 7. Добавление и удаление данных на панели эффектов

#### **Добавление ресурсов эффектов**

Добавьте файл ресурса в соответствующую папку, как описано на шаге 1. Например, для добавления ресурса 2D анимированного эффекта:

Android

iOS

Вы должны поместить ресурс в `android/xmagic/src.mian/assets/MotionRes/2dMotionRes` вашего проекта:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7ba2981770e211efa25e52540075b605.png)

Также добавьте ресурс в `ios/Runner/xmagic/2dMotionRes.bundle` вашего проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7ba310ed70e211ef8631525400a9236a.png)

#### Конфигурация панели красоты

V0.3.5.0 и более поздние

V0.3.1.1 и более ранние

Демо предоставляет простой UI панели красоты. Свойства панели конфигурируются через JSON файлы ([JSON файлы](https://www.tencentcloud.com/document/product/1143/60196#c3effdcb-00ed-4641-ad95-6fbeda7476d0)), расположение которых показано на следующей диаграмме. Реализацию панели можно посмотреть в демо-проекте.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7bac2a3970e211ef8829525400fdb830.png)

В классах BeautyDataManager, BeautyPropertyProducer, BeautyPropertyProducerAndroid и BeautyPropertyProducerIOS вы можете независимо конфигурировать данные панели красоты.

#### **Удаление ресурсов красоты**

Для некоторых лицензий, которые не авторизуют определённые функции красоты и формирования тела, эти функции не должны отображаться на панели красоты. Вам нужно удалить эти функции из конфигурации данных панели красоты.

Например, для удаления эффекта помады удалите следующий код из метода getBeautyData в классах BeautyPropertyProducerAndroid и BeautyPropertyProducerIOS.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7bad795b70e211ef825d525400bdab9d.png)


---
*Источник: [https://trtc.io/document/73779](https://trtc.io/document/73779)*

---
*Источник (EN): [integrating-with-mlvb-sdk.md](интеграция-с-mlvb-sdk.md)*
