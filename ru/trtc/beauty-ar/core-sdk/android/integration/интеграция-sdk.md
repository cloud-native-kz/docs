# Интеграция SDK

Если вы хотите быстро интегрировать и ознакомиться с возможностями BeautyAR, мы рекомендуем применить подход [Интеграции UIKit](https://www.tencentcloud.com/document/product/1143/60196).

Для тех, кто интегрирует эффекты красоты наряду с MLVB SDK / TRTC SDK / Short Video SDK (UGSV), пожалуйста, следуйте рекомендациям по интеграции для [Интеграции с MLVB SDK](https://www.tencentcloud.com/document/product/1143/73767), [Интеграции с TRTC SDK](https://www.tencentcloud.com/document/product/1143/73768) и [Интеграции с UGSV SDK](https://www.tencentcloud.com/document/product/1143/73769) соответственно.

Если вы предпочитаете не использовать UIKit и вместо этого напрямую реализовать вызовы интерфейса Core SDK, вы можете продолжить с этого руководства по интеграции.

## Требования к среде разработчика

- Рекомендуется Android 7.0 (уровень API SDK 24) или более поздние версии.
- Android Studio 3.5 или более поздние версии.

## Демонстрационный проект: TEBeauty_API_Example

Клонируйте [демонстрационный проект](https://github.com/Tencent-RTC/TencentEffect_Android) с GitHub, где TEBeautyDemo — это демонстрационный проект с пользовательским интерфейсом, а TEBeauty_API_Example — это демонстрационный проект без пользовательского интерфейса.

Следуйте инструкциям в документе TEBeauty_API_Example/README для запуска TEBeauty_API_Example, а затем изучите этот текст, чтобы разобраться в подробных этапах интеграции SDK без пользовательского интерфейса.

## Интеграция SDK

> **Примечание:** В демонстрационном проекте на GitHub SDK интегрирован с помощью Maven.

Maven Integration

Manual Integration (Built-in Resources)

Manual Integration (Dynamic Resource Download)

SDK был выпущен в репозиторий mavenCentral, и вы можете настроить Gradle для автоматического скачивания обновлений.

1. Добавьте зависимость BeautyAR SDK в раздел dependencies.

```
dependencies {//Например, пакет S1-04 выглядит следующим образом: implementation 'com.tencent.mediacloud:TencentEffect_S1-04:номер версии'//Номер версии можно найти на странице истории версий на официальном веб-сайте, например, 3.0.0.13. Вы также можете использовать latest.release для номера версии.//Однако обратите внимание: использование latest.release всегда будет держать вашу версию SDK в актуальном состоянии, что может не соответствовать вашим ожиданиям относительно версий с основными изменениями. Используйте latest.release с осторожностью.
```

2. В defaultConfig укажите архитектуру CPU для приложения.

```
defaultConfig { ndk {     abiFilters "armeabi-v7a", "arm64-v8a" }}
```

> **Примечание:** В настоящее время BeautyAR SDK поддерживает armeabi-v7a и arm64-v8a.

3. Нажмите ![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d7a7a79270d811efa016525400bdab9d.png)<2> для автоматического скачивания SDK и интеграции его в проект.

#### Адреса Maven для каждого пакета

| Версия | Адрес Maven |
| --- | --- |
| A1 - 01 | implementation 'com.tencent.mediacloud:TencentEffect_A1-01:номер версии' |
| A1 - 02 | implementation 'com.tencent.mediacloud:TencentEffect_A1-02:номер версии' |
| A1 - 03 | implementation 'com.tencent.mediacloud:TencentEffect_A1-03:номер версии' |
| A1 - 04 | implementation 'com.tencent.mediacloud:TencentEffect_A1-04:номер версии' |
| A1 - 05 | implementation 'com.tencent.mediacloud:TencentEffect_A1-05:номер версии' |
| A1 - 06 | implementation 'com.tencent.mediacloud:TencentEffect_A1-06:номер версии' |
| S1 - 00 | implementation 'com.tencent.mediacloud:TencentEffect_S1-00:номер версии' |
| S1 - 01 | implementation 'com.tencent.mediacloud:TencentEffect_S1-01:номер версии' |
| S1 - 02 | implementation 'com.tencent.mediacloud:TencentEffect_S1-02:номер версии' |
| S1 - 03 | implementation 'com.tencent.mediacloud:TencentEffect_S1-03:номер версии' |
| S1 - 04 | implementation 'com.tencent.mediacloud:TencentEffect_S1-04:номер версии' |
| S1 - 05 | implementation 'com.tencent.mediacloud:TencentEffect_S1-05:номер версии' |
| S1 - 06 | implementation 'com.tencent.mediacloud:TencentEffect_S1-06:номер версии' |
| S1 - 07 | implementation 'com.tencent.mediacloud:TencentEffect_S1-07:номер версии' |

#### Скачивание SDK

[Скачайте SDK](https://trtc.io/sdkDownload?id=beauty) и распакуйте его. Структура каталога выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/de32550570d811efa25e52540075b605.png)

#### Интеграция

Скопируйте файл `xmagic-xxxx.aar` из папки `SDK` в каталог `libs` вашего проекта.

#### Метод импорта

Откройте `build.gradle` модуля приложения и добавьте ссылку на зависимость:

```
android{    ...    defaultConfig {        applicationId "Замените на имя пакета, привязанное к авторизованной лицензии."        ....    }    packagingOptions {        pickFirst '**/libc++_shared.so'    }}dependencies{    ...    compile fileTree(dir: 'libs', include: ['*.jar','*.aar'])//добавить *.aar}Примечание:
```

#### Руководство по динамической загрузке ресурсов, библиотек .so и ресурсов динамических эффектов

Для снижения размера пакета вы можете изменить режим загрузки ресурсов assets, библиотек .so и ресурсов динамических эффектов MotionRes (некоторые базовые SDK не имеют ресурсов динамических эффектов) на режим онлайн. После успешной загрузки предоставьте пути к указанным выше файлам в SDK через настройку.

Вы можете использовать существующий сервис загрузки, но мы рекомендуем использовать логику загрузки из демонстрации. Подробные инструкции по реализации динамической загрузки см. в разделе [Снижение размера SDK](https://www.tencentcloud.com/document/product/1143/60206).

> **Примечание:** **При интеграции без Maven необходимо также добавить следующие зависимости** SDK Version >=4.1.0dependencies{    implementation 'com.google.code.gson:gson:2.8.5'    implementation 'com.tencent.tav:libpag:4.4.35-noffavc'}SDK Version >=4.0.0dependencies{    implementation 'com.google.code.gson:gson:2.8.5'    implementation 'com.tencent.tav:libpag:4.4.24-noffavc'}SDK Version >=3.9.2dependencies{    implementation 'com.google.code.gson:gson:2.8.2'    implementation 'com.tencent.tav:libpag:4.4.24-noffavc'}SDK Version >=3.5.0dependencies{    implementation 'com.google.code.gson:gson:2.8.2'    implementation 'com.tencent.tav:libpag:4.3.33-noffavc'}SDK Version >=3.2.0implementation 'com.google.code.gson:gson:2.8.2'dependencies{    implementation 'com.google.code.gson:gson:2.8.2'}SDK Version >=2.6.0dependencies{    implementation 'com.google.code.gson:gson:2.8.2'    implementation 'androidx.exifinterface:exifinterface:1.3.3'}Если вы хотите использовать другую версию pag, пожалуйста, нажмите [FAQs](https://www.tencentcloud.com/document/product/1143/60312) для просмотра.

## Интеграция ресурсов эффектов

Если ваш пакет включает функции динамических эффектов и фильтров, вам необходимо загрузить соответствующие ресурсы со [страницы загрузки SDK](https://trtc.io/sdkDownload?id=beauty) и поместить материалы динамических эффектов и фильтров в следующие каталоги в вашем проекте:

- Динамические эффекты: `../assets/MotionRes`
- Фильтр: `../assets/lut`

Дополнительные конфигурации ресурсов см. в разделе [Использование материалов (Android)](https://www.tencentcloud.com/document/product/1143/73782).

## Этапы использования SDK

### Этап 1: Аутентификация

1. Подайте заявку на авторизацию, чтобы получить URL лицензии и ключ лицензии. Пожалуйста, обратитесь к [Руководству по лицензии](https://www.tencentcloud.com/document/product/1143/69831).
2. Установите URL и ключ в код инициализации связанного бизнес-модуля для **запуска загрузки лицензии, чтобы избежать временной загрузки перед использованием**. Например, в нашем демонстрационном проекте загрузка запускается в методе onCreate приложения. Однако мы не рекомендуем запускать её здесь в вашем проекте, так как разрешение на доступ в сеть может быть недоступно или в этот момент может быть высокий процент сбоев сети. Выберите более подходящее время для запуска загрузки лицензии.

```
//Если вы хотите только запустить загрузку или обновление лицензии без учёта результата аутентификации, введите null в четвёртый параметр.TELicenseCheck.getInstance().setXMagicLicense(context, URL, KEY, null);
```

3. Выполните аутентификацию перед фактическим использованием функции красоты:

```
TELicenseCheck.getInstance().setTELicense(context, URL, KEY, new TELicenseCheckListener() {         @Override         public void onLicenseCheckFinish(int errorCode, String msg) {             //Примечание: Этот callback может быть не в потоке вызова.             if (errorCode == TELicenseCheck.ERROR_OK) {                 // Аутентификация прошла успешно.             } else {                 // Аутентификация не удалась.             }         }     });
```

**Описание кодов ошибок аутентификации:**

| Код ошибки | Описание |
| --- | --- |
| 0 | Успех |
| -1 | Неверные входные параметры, такие как пустой URL или KEY |
| -3 | Ошибка загрузки. Пожалуйста, проверьте параметры сети. |
| -4 | Локально прочитанная информация об авторизации TE пуста, возможно из-за ошибки ввода-вывода. |
| -5 | Содержимое файла лицензии VCUBE TEMP пусто, возможно из-за ошибки ввода-вывода. |
| -6 | Поля JSON в файле v_cube.license неверны. Пожалуйста, обратитесь в команду Tencent Cloud. |
| -7 | Проверка подписи не удалась. Пожалуйста, обратитесь в команду Tencent Cloud. |
| -8 | Ошибка расшифровки. Пожалуйста, обратитесь в команду Tencent Cloud. |
| -9 | Поля JSON в поле TELicense неверны. Пожалуйста, обратитесь в команду Tencent Cloud. |
| -10 | Информация об авторизации TE, проанализированная из сети, пуста. Пожалуйста, обратитесь в команду Tencent Cloud. |
| -11 | Не удалось записать информацию об авторизации TE в локальный файл, возможно из-за ошибки ввода-вывода. |
| -12 | Загрузка не удалась, и анализ локальных ресурсов также не удался. |
| -13 | Аутентификация не удалась. Пожалуйста, проверьте, находится ли файл .so в пакете или правильно ли установлен путь .so. |
| 3004/3005 | Неверная авторизация. Пожалуйста, обратитесь в команду Tencent Cloud. |
| 3015 | Несоответствие Bundle ID/Package Name. Проверьте, соответствует ли Bundle ID/Package Name, используемые вашим приложением, применённым, и убедитесь, что вы используете правильный файл лицензии. |
| 3018 | Срок действия файла лицензии истёк. Вам необходимо подать заявку на продление в Tencent Cloud. |
| Прочие | Пожалуйста, обратитесь в команду Tencent Cloud. |

### Этап 2: Копирование ресурсов

Файлы ресурсов, упомянутые здесь, состоят из двух частей:

- Файлы моделей SDK, расположенные в каталоге `assets` пакета AAR SDK.
- Файлы ресурсов фильтров и динамических эффектов, расположенные в каталоге `assets` демонстрационного проекта, с названиями `lut` и `MotionRes` соответственно.

Перед использованием эффекта красоты вам необходимо скопировать вышеуказанные ресурсы в приватный каталог приложения. Если версия SDK не обновлена, вам нужно скопировать её только один раз. После успешного копирования вы можете записать это в SharedPreference приложения, чтобы вам не нужно было копировать её снова в следующий раз. Для подробности обратитесь к `TEMenuActivity.java` в демонстрационном проекте.

```
String resPath = new File(getFilesDir(), AppConfig.getInstance().getBeautyFileDirName()).getAbsolutePath();if (!resPath.endsWith(File.separator)) {    resPath = resPath + File.separator;}AppConfig.resPathForSDK = resPath;AppConfig.lutFilterPath = resPath + "light_material/lut";AppConfig.motionResPath = resPath + "MotionRes";new Thread(() -> {    Context context = getApplicationContext();    int addResult = XmagicApi.addAiModeFilesFromAssets(context, AppConfig.resPathForSDK);    Log.d(TAG, "copyRes, add ai model files result = " + addResult);    String lutDirNameInAsset = "lut";    boolean result = FileUtil.copyAssets(context, lutDirNameInAsset, AppConfig.lutFilterPath);    Log.d(TAG, "copyRes, copy lut, result = " + result);    String motionResDirNameInAsset = "MotionRes";    boolean result2 = FileUtil.copyAssets(context, motionResDirNameInAsset, AppConfig.motionResPath);    Log.d(TAG, "copyRes, copy motion res, result = " + result2);}).start();
```

### Этап 3: Инициализация и использование SDK

1. (Опционально) Быстрая реализация камер.

Мы предполагаем, что вы уже реализовали приложение камеры, можете нормально запустить камеру и можете вызвать информацию текстуры SurfaceTexture камеры обратно в Activity для обработки эффекта красоты, как показано ниже:

```
@Overridepublic int onCustomProcessTexture(int textureId, int textureWidth, int textureHeight) {     // SDK эффекта красоты обрабатывает textureId здесь, добавляет эффекты красоты и специальные эффекты для него и возвращает обработанный новый textureID.}
```

Если вы ещё не реализовали приложение камеры, вы можете обратиться к `TECameraBaseActivity.java` в демонстрационном проекте и использовать компонент `GLCameraXView` для быстрого добавления к макету Activity для предварительного просмотра камеры:

```
<com.tencent.demo.camera.camerax.GLCameraXView       android:id="@+id/te_camera_layout_camerax_view"     android:layout_width="match_parent"      android:layout_height="match_parent"     app:back_camera="false"      app:surface_view="false"    app:transparent="true" />
```

2. Инициализируйте SDK красоты на любом потоке, хотя рекомендуется делать это на побочном потоке. **Создание должно произойти после успешной аутентификации лицензии.**

```
//AppConfig.resPathForSDK — это путь ресурса, определённый на этапе копирования ресурса.mXmagicApi = new XmagicApi(this, AppConfig.resPathForSDK);
```

**Параметр**

| Параметр | Значение |
| --- | --- |
| Context context | Контекст |
| String resDir | Каталог файлов ресурсов. Для подробности обратитесь к [Этап 2](https://www.tencentcloud.com/document/product/1143/45385#.E6.AD.A5.E9.AA.A4.E4.BA.8C.EF.BC.9A.E8.B5.84.E6.BA.90.E6.8B.B7.E8.B4.9D) |
| OnXmagicPropertyErrorListener errorListener | Опционально. Реализация функции обратного вызова, для обработки некоторых кодов ошибок во время процесса инициализации и использования SDK. Для значений кодов ошибок обратитесь к [Документации API](https://www.tencentcloud.com/document/product/1143/45399#xmagicapi) |

3. SDK эффекта красоты обрабатывает каждый кадр данных и возвращает соответствующие результаты обработки. Подробную информацию о методе process см. в [Документации API](https://www.tencentcloud.com/document/product/1143/45399#process).

```
@Overridepublic int onCustomProcessTexture(int textureId, int textureWidth, int textureHeight) {    return mXmagicApi.process(textureId, textureWidth, textureHeight);}
```

4. Установите эффекты красоты или специальные эффекты.
  - Используйте метод `setEffect` для **версии 3.5.0 и более поздней**. Подробную информацию см. в [Документации API](https://www.tencentcloud.com/document/product/1143/60201#32a345ed-73c4-4c60-bc7e-3f91b9a4755c).
  - Используйте метод `updateProperty` для **версии 3.3.0 и более ранней**. Подробную информацию см. в [Документации API](https://www.tencentcloud.com/document/product/1143/45399#xmagicproperty).

```
//Используйте этот метод для версии 3.5.0 и более поздней.mXmagicApi.setEffect(String effectName, int effectValue, String resourcePath, Map<String, String> extraInfo)// Например, установите свойство отбеливания с интенсивностью//mXmagicApi.setEffect(XmagicConstant.EffectName.BEAUTY_WHITEN, 50, null,null);// Доступные входные параметры свойств можно получить из XmagicResParser.parseRes().// Используйте этот метод для версии 3.3.0 и более ранней.@DeprecatedmXmagicApi.updateProperty(XmagicProperty<?> p);
```

5. Метод жизненного цикла `onResume`: Рекомендуется вызывать его в методе `onResume()` Activity. При вызове он возобновит звук в эффектах.

```
mXmagicApi.onResume();
```

6. Метод жизненного цикла `onPause`: Рекомендуется вызывать его в методе `onPause()` Activity. При вызове он приостановит звук в эффектах.

```
mXmagicApi.onPause();
```

7. Выпуск SDK эффекта красоты: Вызывается при завершении окружения OpenGL. **Необходимо вызывать в потоке GL и нельзя вызывать в главном потоке (onDestroy Activity);** в противном случае это может привести к утечкам ресурсов и белому или чёрному экрану после нескольких входов и выходов.

```
@Overridepublic void onGLContextDestroy() {    mXmagicApi.onDestroy();}
```

### Этап 4: Конфигурация запутывания

- Если вы включите оптимизацию компиляции (установите minifyEnabled в true) при упаковке выпуска, это обрежет некоторый код, который не вызывается на уровне Java. Этот код может быть вызван уровнем native, что вызывает исключение ` no xxx method`.
- Если вы включили такую оптимизацию компиляции, вам следует добавить эти правила keep, чтобы предотвратить обрезание кода xmagic:

```
-keep class com.tencent.xmagic.** { *;}-keep class org.light.** { *;}-keep class org.libpag.** { *;}-keep class org.extra.** { *;}-keep class com.gyailib.**{ *;}-keep class com.tencent.cloud.iai.lib.** { *;}-keep class com.tencent.beacon.** { *;}-keep class com.tencent.qimei.** { *;}-keep class androidx.exifinterface.** { *;}
```

### Приложение (структура файлов SDK):

> **Примечание:** Эта таблица содержит список всех файлов, используемых SDK. Некоторые файлы могут быть не включены в ваш пакет, но это не повлияет на использование функции этого пакета.

| Тип файла |  |  | Описание |
| --- | --- | --- | --- |
| assets | audio2exp |  | Модель синтеза речи аватара виртуального человека: Если эта функция не используется, модель не требуется. |
|  | benchmark |  | Используется для адаптации модели. |
|  | Light3DPlugin |  | Используется для 3D стикеров. |
|  | LightBodyPlugin | LightBody3DModel.bundle | Используется для 3D точек скелета человека. |
|  |  | LightBodyModel.bundle | Используется для функции красоты тела. |
|  | LightCore |  | Основные ресурсы модели SDK |
|  | LightHandPlugin |  | Требуется для функции жестовых стикеров и определения точек рук. |
|  | LightSegmentPlugin |  | Требуется для функции сегментации фона. |
|  | lut |  | Ресурсы бесплатного фильтра |
| demo_xxx_android_xxxx | - |  | Демонстрационный проект |
| jniLibs | libace_zplan.so |  | Библиотека 3D движка |
|  | libaudio2exp.so |  | Библиотека синтеза речи аватара виртуального человека: Если эта функция не используется, библиотека не требуется. |
|  | libc++_shared.so |  | libc_shared.so — это общая библиотека стандартной библиотеки C. Она предоставляет набор функций и классов стандартной библиотеки C для поддержки разработки и работы программ на языке C. Она широко используется в системе Android и является неотъемлемой частью приложений и библиотек на языке C. Если ваш проект уже включает общую библиотеку C, вы можете оставить только одну копию. |
|  | liblight-sdk.so |  | Основная библиотека Light SDK |
|  | libpag.so |  | Библиотека файлов анимации, от которой зависит light SDK |
|  | libtecodec.so |  | Библиотека кодека, от которой зависит light SDK |
|  | libv8jni.so |  | Библиотека анализа JavaScript, от которой зависит light SDK |
|  | libYTCommonXMagic.so |  | Используется для аутентификации лицензии |
| libs | xmagic-xxxx.aar |  | Файл .aar SDK эффекта красоты |
| MotionRes | 2dMotionRes |  | 2D стикеры |
|  | 3dMotionRes |  | 3D стикеры |
|  | avatarRes |  | Материалы аватаров |
|  | ganMotionRes |  | Забавные стикеры |
|  | handMotionRes |  | Жестовые стикеры |
|  | makeupRes |  | Стикеры макияжа |
|  | segmentMotionRes |  | Стикеры сегментации фона |
| unity | aar |  | Мост AAR, требуемый для проекта unity |
|  | module |  | Исходный проект для моста AAR |


---
*Источник: [https://trtc.io/document/60195](https://trtc.io/document/60195)*

---
*Источник (EN): [integrating-sdk.md](интеграция-sdk.md)*
