# Включение красоты и эффектов

## Шаг 1: Бесшовная интеграция ресурсов специальных эффектов Tencent

1. [Загрузите демо-проект.](https://github.com/Tencent-RTC/TencentEffect_Flutter)
2. Перенесите ресурсы специальных эффектов Tencent

Android

iOS

1. Найдите папку `src/main/assets` в модуле `android/app` вашего проекта. Скопируйте папки lut и MotionRes из `demo/android/app/src/main/assets` в демо-проекте в `android/app/src/main/assets` в вашем проекте. Если в вашем проекте нет папки assets, вы можете создать её вручную.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c18e915b0ec011f0ae6a525400454e06.png)

2. В файле `android/app/build.gradle` вашего проекта добавьте зависимость Beauty SDK для стороны Android. Конкретная зависимость зависит от выбранного пакета. Например, если вы выбрали пакет S1-04, добавьте следующее:

```
dependencies {   implementation 'com.tencent.mediacloud:TencentEffect_S1-04:latest.release'}
```

> **Примечание:** URL-адреса maven, соответствующие каждому пакету, см. в [Документации](https://trtc.io/document/60195?platform=android&product=beautyar). Последний номер версии SDK можно просмотреть в [Истории версий](https://trtc.io/document/60203#).

3. Если вы используете версию Beauty SDK для Android менее 3.9, необходимо найти файл AndroidManifest.xml в модуле app и добавить следующие теги в таблицу application:

```
   <uses-native-library            android:name="libOpenCL.so"            android:required="false" />        //true указывает, что libOpenCL необходим для текущего приложения. Если такой библиотеки нет, система не будет устанавливать приложение.        //false указывает, что libOpenCL не требуется для текущего приложения. Приложение может быть установлено правильно независимо от наличия этой библиотеки. Если устройство имеет эту библиотеку, эффекты типа GAN в Beauty SDK (например, Fairy Tale Face, Chinese Cartoon face) будут работать нормально. Если устройство не имеет этой библиотеки, тип GAN не будет работать, но это не влияет на использование других функций в SDK.        //Описание uses-native-library см. на официальном сайте Android: https://developer.android.com/guide/topics/manifest/uses-native-library-element
```

После добавления выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ef18bdeb0ec011f09ecc52540044a08e.png)

4. Конфигурация обфускации.

При построении пакета релиза с включенными функциями оптимизации кода и обфускации (minifyEnabled = true) инструмент компиляции может удалить код, который не вызывается явно на уровне Java/Kotlin. Если этот код вызывается динамически собственным слоем, будет вызвано исключение NoSuchMethodError (например, нет метода xxx).

Рекомендуется активно сохранять необходимый код модуля Xmagic через правила ProGuard в proguard-rules.pro:

```
-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}-keep class com.tencent.effect.** { *;}
```

Скопируйте папку xmagic из каталога ios/Runner в демо-проекте в каталог ios/Runner в вашем проекте. После добавления выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d32db5430ec011f0ae6a525400454e06.png)

> **Примечание:** Материалы, скопированные из демо-проекта выше, являются тестовыми материалами. Для официальных материалов вам необходимо связаться с [сотрудниками](https://trtc.io/document/51280#) отдела специальных эффектов красоты Tencent после покупки пакета, чтобы получить их и добавить заново.

## Шаг два: Интеграция tencent_effect_flutter

Вы можете зависеть от tencent_effect_flutter в вашем Flutter-проекте следующими способами.

1. Удалённая зависимость

Добавьте следующую ссылку в файл pubspec.yaml:

```
  tencent_effect_flutter:   git:     url: https://github.com/Tencent-RTC/TencentEffect_Flutter
```

2. Локальная зависимость

Загрузите последнюю версию [tencent_effect_flutter](https://github.com/Tencent-RTC/TencentEffect_Flutter) из github, а затем добавьте следующую ссылку в файл pubspec.yaml:

```
tencent_effect_flutter:    path: path to tencent_effect_flutter
```

## Шаг 3: Связь эффектов красоты с TRTC

Android

iOS

Добавьте следующий код в метод onCreate класса приложения (или в метод onCreate FlutterActivity):

```
TRTCPlugin.setBeautyProcesserFactory(new XmagicProcesserFactory());
```

Добавьте следующий код в метод didFinishLaunchingWithOptions в файле AppDelegate в каталоге ios/Runner:

Swift

Object-C

```
let instance = XmagicProcesserFactory()TencentRTCCloud.setBeautyProcesserFactory(factory: instance)
```

```
XmagicProcesserFactory *instance = [[XmagicProcesserFactory alloc] init];[TencentRTCCloud setBeautyProcesserFactoryWithFactory:instance];
```

## Шаг 4: Инициализация и авторизация ресурсов эффектов красоты

1. Инициализация ресурсов

V0.3.5.0 и более поздние версии

V0.3.1.1 и более ранние версии

```
TencentEffectApi.getApi()?.setResourcePath(resourceDir);TencentEffectApi.getApi()?.initXmagic((result) {    // TODO});
```

```
TencentEffectApi.getApi()?.initXmagic(dir,(reslut) {    //TODO});
```

2. Авторизация красоты

```
TencentEffectApi.getApi()?.setLicense(licenseKey, licenseUrl, (errorCode, msg) {    if (errorCode == 0) {       // Success    }});
```

## Шаг 5: Включение/отключение эффектов красоты

После выполнения вышеуказанных операций вы можете включать/отключать эффекты красоты через скрытый интерфейс TRTC:

```
_enableCustomBeautyByNative(bool open) {  trtcCloud.callExperimentalAPI("{\\"api\\": \\"enableVideoProcessByNative\\", \\"params\\": {\\"enable\\": $open}}");}
```

> **Примечание:** Включите эффекты красоты на странице. При закрытии камеры необходимо сначала отключить эффекты красоты. Включение и отключение используются парами.

## Справочная документация

Вы завершили связь между TRTC и улучшением красоты специальных эффектов. Вы можете узнать больше о том, как использовать улучшение красоты специальных эффектов, в следующей документации:

- [Beauty Flutter SDK API Doc](https://trtc.io/document/60200?platform=flutter&product=beautyar)
- [Effects Parameter](https://trtc.io/document/60207?platform=android&product=beautyar)


---
*Источник: [https://trtc.io/document/69082](https://trtc.io/document/69082)*

---
*Источник (EN): [enabling-beauty-and-effects.md](./enabling-beauty-and-effects.md)*
