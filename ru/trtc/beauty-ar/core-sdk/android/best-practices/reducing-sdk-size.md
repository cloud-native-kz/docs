# Сокращение размера SDK

Для уменьшения размера пакета можно настроить загрузку необходимых SO-библиотек и ресурсов моделей в интернете, требуется только загрузить эти файлы перед инициализацией SDK. Для ресурсов фильтров и динамических эффектов рекомендуется загружать их по одному при использовании пользователем.

## Демопроект: TEBeauty_Download_Example

Клонируйте [демопроект](https://github.com/Tencent-RTC/TencentEffect_Android) с GitHub, настройте и запустите TEBeauty_Download_Example согласно документации TEBeauty_Download_Example/readme, чтобы изучить полный процесс динамической загрузки.

## Загрузка SO-библиотек и ресурсов модели

Если вы повторно используете код загрузки из демопроекта

Если вы выполняете загрузку самостоятельно

1. Скопируйте код из директории `com.tencent.demo.download` демопроекта в ваш проект.
2. [Загрузите SDK](https://trtc.io/document/45377), распакуйте его, затем найдите пакет сжатия в формате `.zip` в директории "SDK", распакуйте его еще раз, и вы увидите следующие файлы:

![20240516-205143@2x](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5f3a13e513fc11efaa1c525400f65c2a.png)

3. Загрузите download_assets.zip, arm64-v8a.zip и armeabi-v7a.zip на ваш сервер, чтобы получить ссылки для загрузки. Вычислите MD5 этих 3 zip-файлов. Заполните ссылки для загрузки и значения MD5 в соответствующие константы в `ResDownloadConfig.java`.
4. Обратитесь к коду в `TEMenuActivity.java`, используйте `ResDownloadUtil.getValidLibsDirectory` для проверки того, была ли загружена SO-библиотека. Если нет, вызовите `ResDownloadUtil.checkOrDownloadFiles` для начала загрузки. После успешной загрузки получите путь SO-библиотеки sdkLibraryDirectory, затем вызовите `XmagicApi.setLibPathAndLoad(sdkLibraryDirectory)` для загрузки SO-библиотеки.

```
String validLibsDirectory = ResDownloadUtil.getValidLibsDirectory(this, libraryMD5);if (validLibsDirectory == null) {    ResDownloadUtil.checkOrDownloadFiles(this, ResDownloadUtil.FILE_TYPE_LIBS, libraryURL, libraryMD5,        new TEDownloadListener() {            @Override            public void onDownloadSuccess(String directory) {              sdkLibraryDirectory = directory;            }            @Override            public void onDownloading(int progress) {            }            @Override            public void onDownloadFailed(int errorCode) {            }        });} else {    sdkLibraryDirectory = validLibsDirectory;}
```

5. Обратитесь к коду в `TEMenuActivity.java`, используйте `ResDownloadUtil.getValidAssetsDirectory` для проверки того, были ли загружены ресурсы модели. Если нет, вызовите `ResDownloadUtil.checkOrDownloadFiles` для начала загрузки. Модуль загружает, организует и копирует эти ресурсы в директорию `AppConfig.resPathForSDK`, затем передает их в SDK при создании нового XmagicApi.

```
String validAssetsDirectory = ResDownloadUtil.getValidAssetsDirectory(this, ResDownloadConfig.DOWNLOAD_MD5_ASSETS);if (TextUtils.isEmpty(validAssetsDirectory)) {    ResDownloadUtil.checkOrDownloadFiles(this, ResDownloadUtil.FILE_TYPE_ASSETS,            ResDownloadConfig.DOWNLOAD_URL_ASSETS,            ResDownloadConfig.DOWNLOAD_MD5_ASSETS, new TEDownloadListener() {                @Override                public void onDownloadSuccess(String directory) {                }                @Override                public void onDownloading(int progress) {                }                @Override                public void onDownloadFailed(int errorCode) {                }            });} else {    }
```

6. В демопроекте по умолчанию включена перезагрузка с контрольной точки (свойство `ENABLE_RESUME_FROM_BREAKPOINT` в `ResDownloadUtil.java` установлено на `true`), что гарантирует возобновление загрузки с контрольной точки в случае прерывания из-за исключений. Если вы хотите включить перезагрузку с контрольной точки, убедитесь, что ваш сервис загрузки поддерживает возобновление с контрольной точки. Способ проверки:

```
Чтобы проверить, поддерживает ли сервер возобновление загрузки с контрольной точки, просто проверьте, поддерживает ли веб-сервер запросы Range. Способ тестирования — выполнить команду curl в командной строке:curl -i --range 0-9 https://your_server_address/downloaded_fileПример:curl -i --range 0-9 https://mediacloud-76607.gzc.vod.tencent-cloud.com/TencentEffect/Android/2.4.1.119/xmagic_S1-04_android_2.4.1.119.zipЕсли возвращаемое содержимое содержит поле Content-Range, это указывает, что сервер поддерживает возобновление с контрольной точки.
```

1. [Загрузите SDK](https://trtc.io/document/45377), распакуйте его, затем найдите пакет сжатия в формате .zip в директории "SDK", распакуйте его еще раз, и вы увидите следующие файлы. Файлы модели в assets и SO-файлы в jniLibs можно загружать динамически. aar в libs требуется встроить в пакет.

![20240516-205143@2x](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d74236e0141611ef83b95254002977b6.png)

2. Загрузите SO-файл и распакуйте его, затем вызовите `XmagicApi.setLibPathAndLoad(/path/to/so/files)` для загрузки SO-библиотеки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/123d40d0665811ed87ca525400463ef7.png)

> **Примечание:** Настоятельно рекомендуется загружать SO-файл в приватную директорию приложения, а не во внешнее хранилище, чтобы предотвратить его случайное удаление утилитами очистки. Кроме того, вы можете загружать SO-файл v8a или v7a в зависимости от типа CPU мобильного телефона пользователя для выборочной загрузки, чтобы ускорить процесс. Обратитесь к демопроекту TEMenuActivity в качестве справки.

3. Для файлов в пакете download_assets.zip после завершения загрузки распакуйте его, затем вызовите следующий код, чтобы позволить SDK скопировать файлы в правильную директорию (директорию, на которую указывает `AppConfig.resPathForSDK`). `downloadedDirectory` в коде — это директория, где расположены ваши распакованные файлы.

`addAiModeFiles` возвращает код ошибки -2, что означает сбой копирования файла во время процесса. Это может быть обусловлено недостаточным местом на мобильном телефоне или исключением ввода-вывода. Вы можете попробовать скопировать снова или переск​ачать.

```
  private static boolean organizeAssetsDirectory(String downloadedDirectory) {    for (String path : XmagicResourceUtil.AI_MODE_DIR_NAMES) {        if (XmagicApi.addAiModeFiles(downloadedDirectory + File.separator + path, AppConfig.resPathForSDK) == -2) {            return false;        }    }    return true;}
```

> **Примечание:** При обновлении версии SDK соответствующие .so-файлы и assets могут измениться. Чтобы обеспечить совместимость, вам необходимо перезагрузить эти файлы. Рекомендуется следовать подходу, продемонстрированному в демопроекте, используя проверку контрольной суммы MD5. Поскольку Tencent Effect SDK **также зависит от библиотек libpag и gson**, а текущая функция динамической загрузки предназначена только для самого Tencent Effect SDK, вам требуется вручную добавить зависимости для **libpag и gson** в вашем проекте. Для конкретных номеров версий обратитесь к [документации](https://www.tencentcloud.com/document/product/1143/60195#sdkversion).

## Загрузка ресурсов фильтров и анимаций

- Каждый фильтр — это изображение в формате png, а каждая анимация — это папка. Для ресурсов фильтров и анимаций рекомендуется загружать один элемент при клике пользователя на его использование. После успешной загрузки вызовите API [XmagicApi.setEffect](https://www.tencentcloud.com/document/product/1143/60207) SDK и установите путь фильтра или путь папки анимации в SDK.
- Ресурсы фильтров и анимаций можно сохранять в любой директории на мобильном телефоне. Рекомендуется сохранять их в приватной директории приложения, чтобы предотвратить их случайное удаление.


---
*Источник: [https://trtc.io/document/60206](https://trtc.io/document/60206)*

---
*Источник (EN): [reducing-sdk-size.md](./reducing-sdk-size.md)*
