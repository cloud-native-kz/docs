# Интеграция TEBeautyKit

## Возможности

Чтобы облегчить быструю интеграцию эффектов красоты для клиентов и упростить разработку панелей пользовательского интерфейса, мы предоставляем компонент пользовательского интерфейса эффектов красоты: TEBeautyKit. Он включает дополнительную инкапсуляцию SDK и настраиваемые панели пользовательского интерфейса, как показано на рисунке ниже. Если вы предпочитаете не использовать этот пользовательский интерфейс, см. [Интеграция Core SDK (Android)](https://www.tencentcloud.com/document/product/1143/60195).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8011db4fd1bc11f08f8f525400454e06.png)

## Демонстрационный проект: **TEBeautyDemo**

Клонируйте [демонстрационный проект](https://github.com/Tencent-RTC/TencentEffect_Android) из GitHub, следуя инструкциям в документе TEBeautyDemo/README, запустите TEBeautyDemo, а затем обратитесь к этому документу для получения подробных инструкций по интеграции SDK с пользовательским интерфейсом.

## Интегрировать TEBeautyKit

> **Примечание:** Эта библиотека поддерживает только **Tencent Effect SDK версии 3.5.0** и более поздние версии.

### Шаг 1: Добавить библиотеку зависимостей

- [Интеграция BeautyAR SDK](https://www.tencentcloud.com/document/product/1143/60195#.E9.9B.86.E6.88.90.E5.87.AD.E5.A4.86)
- [Интеграция BeautyAR Resources](https://www.tencentcloud.com/document/product/1143/60195#d45c5308-0cf3-4ed7-99ad-4e6156981a89)

### Шаг 2: Добавить зависимость TEBeautyKit

Интеграция исходного кода (рекомендуется)

Интеграция Maven

Загрузка интеграции AAR

1. Скопируйте модуль TEBeautyKit из [демонстрационного проекта](https://github.com/Tencent-RTC/TencentEffect_Android/tree/main/TEBeautyDemo) в ваш проект и измените тип пакета SDK и номер версии в `tebeautykit/build.gradle`, чтобы они совпадали с типом пакета SDK и номером версии на шаге 1.

```
implementation 'com.tencent.mediacloud:TencentEffect_S1-04:SDK version number'
```

2. Затем добавьте зависимость на модуль TEBeautyKit в соответствующий модуль вашего приложения:

```
implementation project(':tebeautykit')
```

1. Добавьте зависимость на библиотеку TEBeautyKit в зависимости вашего приложения. Номер версии SDK должен совпадать с номером версии на шаге 1.

```
dependencies{    ...    implementation 'com.tencent.mediacloud:TEBeautyKit:SDK version number'}
```

2. Поскольку TEBeautyKit также зависит от компонентов, таких как Gson и OkHttp, вам необходимо добавить следующие зависимости:

```
dependencies{    implementation 'com.google.code.gson:gson:2.8.2'    implementation 'com.squareup.okhttp3:okhttp:3.9.0'    implementation 'com.github.bumptech.glide:glide:4.12.0'    implementation 'androidx.appcompat:appcompat:1.0.0'    implementation 'androidx.constraintlayout:constraintlayout:2.1.3'    implementation 'androidx.recyclerview:recyclerview:1.2.1'}
```

1. [Загрузите TEBeautyKit](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/latest/tebeautykit_latest.zip) (Загруженный файл будет zip-файлом. Распакуйте его, чтобы получить файл AAR.)
2. Скопируйте файл `tebeautykit-xxxx.aar` в каталог `libs` проекта приложения.
3. Откройте `build.gradle` модуля приложения и добавьте ссылку на зависимость:

```
dependencies{    ...    implementation fileTree(dir: 'libs', include: ['*.jar','*.aar'])}
```

4. Поскольку TEBeautyKit также зависит от компонентов, таких как Gson и OkHttp, вам необходимо добавить следующие зависимости:

```
dependencies{    implementation 'com.google.code.gson:gson:2.8.2'    implementation 'com.squareup.okhttp3:okhttp:3.9.0'    implementation 'com.github.bumptech.glide:glide:4.12.0'    implementation 'androidx.appcompat:appcompat:1.0.0'    implementation 'androidx.constraintlayout:constraintlayout:2.1.3'    implementation 'androidx.recyclerview:recyclerview:1.2.1'}
```

### Шаг 3: Добавить файл JSON конфигурации панели

Получите файл конфигурации панели из папки `demo/src/main/assets/beauty_panel` [демонстрационного проекта](https://github.com/Tencent-RTC/TencentEffect_Android/tree/main/TEBeautyDemo) или нажмите здесь, чтобы [загрузить](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/latest/beauty_panel-2024-05-14.zip) и распаковать. Файл включает конфигурации для красоты, красоты тела, фильтров, наклеек с динамическими эффектами и свойств сегментации. Выберите набор файлов JSON в соответствии с типом вашего пакета и поместите их в папку `assets/beauty_panel` в вашем проекте (папка **panel_icon** также должна быть помещена в эту директорию).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f9bcf8d012c511f1a92352540097cba1.png)

Загруженный архив содержит файлы, показанные выше. Каждому имени пакета соответствует несколько файлов JSON. В таблице ниже объясняется каждый файл JSON.

| **Файл** | **Описание** |
| --- | --- |
| beauty.json | Файл конфигурации эффектов красоты, формирования лица, корректировки изображения и т. д. |
| beauty_base_shape.json | Файл конфигурации базовой коррекции контуров лица. |
| beauty_body.json | Файл конфигурации красоты тела. |
| beauty_general_shape.json | Файл конфигурации общей коррекции контуров лица. |
| beauty_image.json | Файл конфигурации корректировки качества изображения. |
| beauty_makeup.json | Файл конфигурации одноточечного макияжа. |
| beauty_shape.json | Файл конфигурации премиум-стайлинга. |
| beauty_template | Файл конфигурации шаблона фильтра красоты. |
| light_makeup.json | Файл конфигурации легкого макияжа. |
| lut.json | Файл конфигурации фильтра. Примечание: Поскольку разные клиенты используют разные материалы фильтров, клиенты могут конфигурировать в соответствии со структурой JSON после загрузки (см. [Описание структуры файла JSON](#1ee2863b-9110-4bbc-8b47-29f6484cb077)) и удалить конфигурацию по умолчанию. |
| makeup.json | Файл конфигурации для полного макияжа всего лица. Примечание: Поскольку разные клиенты используют разные материалы для макияжа всего лица, клиенты могут конфигурировать в соответствии со структурой JSON после загрузки (см. [Описание структуры файла JSON](#1ee2863b-9110-4bbc-8b47-29f6484cb077)). |
| motion_2d.json | Файл конфигурации наклейки с 2D динамическим эффектом. Примечание: Поскольку разные клиенты используют разные материалы наклеек с динамическими эффектами, клиенты могут конфигурировать в соответствии со структурой JSON после загрузки (см. [Описание структуры файла JSON](#1ee2863b-9110-4bbc-8b47-29f6484cb077)). |
| motion_3d.json | Файл конфигурации наклейки с 3D анимацией. Примечание: Поскольку разные клиенты могут использовать разные материалы наклеек с анимацией, клиенты могут конфигурировать в соответствии со структурой JSON после загрузки (см. [Описание структуры файла JSON](#1ee2863b-9110-4bbc-8b47-29f6484cb077) для получения подробной информации). |
| motion_gesture.json | Файл конфигурации наклейки с анимацией жестов. Примечание: Поскольку разные клиенты могут использовать разные материалы наклеек с анимацией, клиенты могут конфигурировать в соответствии со структурой JSON после загрузки (см. [Описание структуры файла JSON](#1ee2863b-9110-4bbc-8b47-29f6484cb077)). |
| segmentation.json | Файл конфигурации сегментации фона (виртуальный фон). Примечание: Поскольку разные клиенты используют разные материалы сегментации, клиенты могут конфигурировать в соответствии со структурой JSON после загрузки (см. [Описание структуры файла JSON](#1ee2863b-9110-4bbc-8b47-29f6484cb077)). |
| panel_icon | Эта папка используется для хранения изображений, сконфигурированных в файле JSON, и должна быть добавлена. |

## Использование TEBeautyKit

Мы настоятельно рекомендуем вам обратиться к `TEMenuActivity.java` и `TECameraBaseActivity.java` [демонстрационного проекта](https://github.com/Tencent-RTC/TencentEffect_Android/tree/main/TEBeautyDemo), чтобы понять, как интегрировать TEBeautyKit.

### Шаг 1: Аутентификация

1. Подайте заявку на авторизацию, чтобы получить URL лицензии и ключ лицензии. Пожалуйста, обратитесь к [Руководству по лицензии](https://trtc.io/document/60219).
2. Установите URL и ключ в коде инициализации соответствующего модуля бизнеса для **запуска загрузки лицензии, чтобы избежать временной загрузки перед использованием**. Например, в нашем демонстрационном проекте загрузка запускается в методе onCreate приложения. Однако мы не рекомендуем запускать это здесь в вашем проекте, так как сетевое разрешение может быть недоступно или могут быть высокие показатели сетевых сбоев в это время. Пожалуйста, выберите более подходящее время для запуска загрузки лицензии.

```
// If you only want to trigger the download or update the license without caring about the authentication result, input null for the fourth parameter.//TEApplication.javaTEBeautyKit.setTELicense(context, LicenseConstant.mXMagicLicenceUrl, LicenseConstant.mXMagicKey, null);
```

3. Выполните аутентификацию перед фактическим использованием функции красоты (например, перед запуском камеры):

```
//TEMenuActivity.javaTEBeautyKit.setTELicense(context, LicenseConstant.mXMagicLicenceUrl, LicenseConstant.mXMagicKey, new TELicenseCheckListener() {         @Override         public void onLicenseCheckFinish(int errorCode, String msg) {             // Note: This callback may not be on the calling thread.             if (errorCode == TELicenseCheck.ERROR_OK) {                 // Authentication succeeded.             } else {                 // Authentication failed.             }         }     });
```

**Описание кодов ошибок аутентификации:**

| Код ошибки | Описание |
| --- | --- |
| 0 | Успех |
| -1 | Неверные входные параметры, такие как пустой URL или KEY |
| -3 | Ошибка загрузки. Пожалуйста, проверьте параметры сети. |
| -4 | Локально прочитанная информация об авторизации TE пуста, возможно из-за сбоя ввода-вывода. |
| -5 | Содержимое файла лицензии VCUBE TEMP пусто, возможно из-за сбоя ввода-вывода. |
| -6 | JSON поля в файле v_cube.license неверны. Пожалуйста, свяжитесь с командой Tencent Cloud для решения. |
| -7 | Ошибка проверки подписи. Пожалуйста, свяжитесь с командой Tencent Cloud для решения. |
| -8 | Ошибка расшифровки. Пожалуйста, свяжитесь с командой Tencent Cloud для решения. |
| -9 | JSON поля в поле TELicense неверны. Пожалуйста, свяжитесь с командой Tencent Cloud для решения. |
| -10 | Информация об авторизации TE, разобранная из сети, пуста. Пожалуйста, свяжитесь с командой Tencent Cloud для решения. |
| -11 | Ошибка при записи информации об авторизации TE в локальный файл, возможно из-за сбоя ввода-вывода |
| -12 | Загрузка не удалась, и разбор локальных ресурсов также не удался. |
| -13 | Ошибка аутентификации. Проверьте, находится ли файл .so в пакете или правильно ли установлен путь .so. |
| 3004/3005 | Неверная авторизация. Пожалуйста, свяжитесь с командой Tencent Cloud для решения. |
| 3015 | Несоответствие Bundle ID/Package Name. Проверьте, совпадает ли Bundle ID/Package Name, используемый вашим приложением, с заявленным, и убедитесь, что вы используете правильный файл лицензии. |
| 3018 | Срок действия файла лицензии истёк. Вам необходимо подать заявку на продление в Tencent Cloud. |
| Другие | Пожалуйста, свяжитесь с командой Tencent Cloud для решения. |

### Шаг 2: Установить путь

```
    //TEMenuActivity.java  String resPath = new File(getFilesDir(), AppConfig.getInstance().getBeautyFileDirName()).getAbsolutePath();  TEBeautyKit.setResPath(resPath);
```

### Шаг 3: Копировать ресурсы

Упомянутые здесь файлы ресурсов состоят из двух частей:

- Файлы модели SDK, находящиеся в каталоге `assets` пакета AAR SDK.
- Файлы ресурсов фильтров и динамических эффектов, находящиеся в каталоге `assets` демонстрационного проекта, названные `lut` и `MotionRes` соответственно.

Перед использованием эффекта красоты вам необходимо скопировать вышеупомянутые ресурсы в resPath, установленный на шаге 2. Если версия SDK не обновляется, вам нужно скопировать её только один раз. После успешного копирования вы можете записать это в SharedPreference приложения, чтобы вам не требовалось копировать её в следующий раз. Подробности см. в методе `copyRes` класса `TEMenuActivity.java` в демонстрационном проекте.

```
//TEMenuActivity.javaprivate void copyRes() {
    if (!isNeedCopyRes()) {
        return;
    }
    new Thread(() -> {
        TEBeautyKit.copyRes(getApplicationContext());
    }).start();
}
```

### Шаг 4: Инициализировать TEBeautyKit и добавить представление на страницу

```
//TECameraBaseActivity.javaTEBeautyKit.create(this.getApplicationContext(), beautyKit -> {    mBeautyKit = beautyKit;    initBeautyView(beautyKit);});public void initBeautyView(TEBeautyKit beautyKit){        List<TEPanelDataModel> panelDataModels = TEUIConfig.getInstance().getPanelDataList();TEUIConfig.getInstance().getPanelDataList();        panelDataModels.clear();        //Add the corresponding JSON based on the package features        TEPanelDataModel template = new TEPanelDataModel("beauty_panel/beauty_template.json", TEUIProperty.UICategory.BEAUTY_TEMPLATE);        TEPanelDataModel beauty1 = new TEPanelDataModel("beauty_panel/beauty.json", TEUIProperty.UICategory.BEAUTY);new TEPanelDataModel("beauty_panel/beauty.json", TEUIProperty.UICategory.BEAUTY);        TEPanelDataModel beauty2 = new TEPanelDataModel("beauty_panel/beauty_image.json", TEUIProperty.UICategory.BEAUTY);new TEPanelDataModel("beauty_panel/beauty_image.json", TEUIProperty.UICategory.BEAUTY);        TEPanelDataModel beauty4 = new TEPanelDataModel("beauty_panel/beauty_shape.json", TEUIProperty.UICategory.BEAUTY);        TEPanelDataModel beauty3 = new TEPanelDataModel("beauty_panel/beauty_makeup.json", TEUIProperty.UICategory.BEAUTY);        TEPanelDataModel lut = new TEPanelDataModel("beauty_panel/lut.json", TEUIProperty.UICategory.LUT);new TEPanelDataModel("beauty_panel/lut.json", TEUIProperty.UICategory.LUT);        TEPanelDataModel lightMakeup = new TEPanelDataModel("beauty_panel/light_makeup.json",new TEPanelDataModel("beauty_panel/light_makeup.json",                TEUIProperty.UICategory.LIGHT_MAKEUP);        TEPanelDataModel makeup = new TEPanelDataModel("beauty_panel/makeup.json", TEUIProperty.UICategory.MAKEUP);        TEPanelDataModel motion = new TEPanelDataModel("beauty_panel/motion_2d.json", TEUIProperty.UICategory.MOTION);        TEPanelDataModel motion2 = new TEPanelDataModel("beauty_panel/motion_3d.json", TEUIProperty.UICategory.MOTION);        TEPanelDataModel motion_gesture = new TEPanelDataModel("beauty_panel/motion_gesture.json",new TEPanelDataModel("beauty_panel/motion_gesture.json",                TEUIProperty.UICategory.MOTION);        TEPanelDataModel seg = new TEPanelDataModel("beauty_panel/segmentation.json", TEUIProperty.UICategory.SEGMENTATION);        panelDataModels.add(template);        panelDataModels.add(beauty1);        panelDataModels.add(beauty2);        panelDataModels.add(beauty4);        panelDataModels.add(beauty3);        panelDataModels.add(lut);        panelDataModels.add(lightMakeup);        panelDataModels.add(makeup);        panelDataModels.add(motion);        panelDataModels.add(motion2);        panelDataModels.add(motion_gesture);        panelDataModels.add(seg);        mTEPanelView = new TEPanelView(this);    mTEPanelView.setTEPanelViewCallback(this);    mTEPanelView.setupWithTEBeautyKit(beautyKit);    mTEPanelView.showView(this);    this.mPanelLayout.addView(mTEPanelView, new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));}
```

В зависимости от вашего плана подписки заполните соответствующий JSON функции. Например, если ваш план не включает сегментацию, нет необходимости добавлять `segmentation.json`. Аналогично, если ваш пакет не поддерживает 3D наклейки, вы должны опустить `motion_3d.json`.

### Шаг 5: Использование эффекта красоты

Предполагаем, что вы уже реализовали приложение камеры, можете нормально запустить камеру и можете вызвать информацию текстуры SurfaceTexture камеры обратно в Activity для обработки эффектов красоты, как показано ниже:

```
//TECameraBaseActivity.java@Overridepublic int onCustomProcessTexture(int textureId, int textureWidth, int textureHeight) {     // The beauty effect SDK processes the textureId here, adds beauty effects and special effects for it, and returns the processed new textureID.}
```

Если вы еще не реализовали приложение камеры, вы можете обратиться к `TECameraBaseActivity.java` в демонстрационном проекте и использовать компонент `GLCameraXView` для добавления его в макет Activity для быстрого предварительного просмотра камеры:

```
<com.tencent.demo.camera.camerax.GLCameraXView       android:id="@+id/te_camera_layout_camerax_view"     android:layout_width="match_parent"      android:layout_height="match_parent"     app:back_camera="false"      app:surface_view="false"    app:transparent="true" />
```

SDK эффектов красоты обрабатывает каждый кадр данных и возвращает соответствующие результаты обработки. Для получения подробной информации о методе процесса см. [Документацию API](https://www.tencentcloud.com/document/product/1143/60201).

```
//TECameraBaseActivity.java@Override
public int onCustomProcessTexture(int textureId, int textureWidth, int textureHeight) {
    return mBeautyKit.process(textureId, textureWidth, textureHeight);
}
```

### Шаг 6: Управление жизненным циклом

- Метод жизненного цикла onResume: Рекомендуется вызывать в методе `onResume()` класса `Activity`. При вызове будет восстановлен звук в эффектах.

```
mBeautyKit.onResume();
```

- Метод жизненного цикла onPause: Рекомендуется вызывать в методе `onPause()` класса Activity. При вызове будет приостановлен звук в эффектах.

```
mBeautyKit.onPause();
```

- Освобождение SDK эффектов красоты: Вызывается при завершении окружения OpenGL. **Это необходимо вызывать в GL потоке, а не в главном потоке (onDestroy класса Activity);** в противном случае это может привести к утечкам ресурсов и результату белого или чёрного экрана после нескольких входов и выходов.

```
@Override
public void onGLContextDestroy() {
    mBeautyKit.onDestroy();
}
```

### Шаг 7: Экспорт и импорт параметров эффектов красоты

Экспортируйте текущие параметры эффектов красоты и сохраните их в SharedPreference:

```
String json = mBeautyKit.exportInUseSDKParam();
if (json != null) {
    getSharedPreferences("demo_settings", Context.MODE_PRIVATE).edit().      putString("current_beauty_params", json).commit();
}
```

В следующий раз при инициализации TEBeautyKit импортируйте эту строку, чтобы изменить эффект красоты по умолчанию:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f9c736547c8111ef8631525400a9236a.png)

## Приложение

### Пояснение файла JSON панели

- **Красота, формирование тела.**

****

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2db7d35ac0b111ee9000525400461a83.png)

****

| Поле | Описание |
| --- | --- |
| displayName | Китайское имя. |
| displayNameEn | Английское имя. |
| hasSubTitle | Должны ли быть включены и отображены подзаголовки. |
| verticalLayout | Является ли список атрибутов красоты вертикально прокручиваемым. |
| id | Шаблон фильтра красоты содержит это поле данных, которое отсутствует в других файлах JSON, служит идентификатором шаблона. |
| icon | URL изображения, поддерживает как локальные, так и онлайн изображения в параметре Setting. Локальные изображения могут поступать из ресурсов assets и SD. Как показано выше, изображения assets и карточки SD устанавливаются как полный путь изображения, а онлайн изображения устанавливаются на соответствующую ссылку http в Setting |
| sdkParam | Красота SDK содержит четыре атрибута, см. таблицу параметров красоты для получения дополнительной информации |
| effectName | Ключевые атрибуты красоты, см. [таблицу параметров атрибутов](https://www.tencentcloud.com/document/product/1143/60207). |
| effectValue | Установка интенсивности атрибута, см. [таблицу параметров атрибутов](https://www.tencentcloud.com/document/product/1143/60207). |
| resourcePath | Установка пути ресурса, см. [таблицу параметров атрибутов](https://www.tencentcloud.com/document/product/1143/60207). |
| extraInfo | Установка другой информации, см. [таблицу параметров атрибутов](https://www.tencentcloud.com/document/product/1143/60207). |
| uiState | Используется ли текущий атрибут или выбран, всего 3 возможных значения:0: Не используется и не выбран.1: В использовании.2: Выбран и в использовании. |

- **Фильтр, наклейка, сегментация.**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2dbc518fc0b111ee9000525400461a83.png)

Конфигурация фильтров и наклеек с динамическими эффектами в основном идентична, поэтому JSON фильтра используется в качестве иллюстрации. Были добавлены два новых поля: downloadPath и resourceUri.

| Поле | Описание |
| --- | --- |
| downloadPath | Если ваш материал фильтра загружается из Интернета, конфигурация здесь представляет локальное место хранения после загрузки. Этот путь является **относительным путём**; полный путь представляет собой комбинацию [шага 2](https://www.tencentcloud.com/document/product/1143/60196#1af9a4f7-925a-48fb-86e9-03e4753ce7d1) **+ установленный здесь путь** |
| resourceUri | Если ваш материал нужно загрузить через сеть, укажите сетевой адрес здесь, как в третьем красном поле на изображении выше. Однако если ваш материал фильтра локальный, укажите соответствующий локальный адрес согласно изображению выше. |

- **Макияж**

****

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2db6f138c0b111ee9000525400461a83.png)

В полный макияж всего лица было добавлено дополнительное поле `makeupLutStrength` под `extraInfo`. Это поле используется для модерирования инт

---
*Источник (EN): [integrating-tebeautykit.md](./integrating-tebeautykit.md)*
