# Виртуальный фон

TUICallKit запустил новую функцию виртуального фона, позволяющую пользователям устанавливать размытый или изображение фона во время видеозвонков. Это скрывает реальную среду вызова, защищает конфиденциальность и делает звонок более интересным. Далее в этой статье подробно описано, как использовать эту функцию в компоненте TUICallKit.

## Эффект интеграции

Эффект отображения компонента TUICallKit после интеграции функции виртуального фона выглядит следующим образом:

| Исходная камера | Эффект размытого фона | Эффект фона с изображением |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f8898ac518d411efadbe525400720cb5.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fd264d4a18d411ef81a8525400f65c2a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0115f38618d511efad1a52540019e87e.png) |

## Требования подготовки

1. Перед использованием функции виртуального фона от Tencent Cloud вам необходимо посетить консоль для активации служб Audio and Video для вашего приложения и приобрести пакет `Group Call`. Подробные инструкции см. в разделе [Активация сервиса](https://www.tencentcloud.com/document/product/647/59832#).
2. Укажите версию SDK LiteAVSDK_Professional.

Поддержка виртуального фона начинается с tencent_calls_uikit: 2.3.2 (LiteAVSDK_Professional 11.7.0.12001), для разных версий SDK LiteAVSDK_Professional требуются разные файлы моделей.

Android

iOS

В файле `build.gradle` укажите версию TXLiteAVSDK_Professional, например установите её на `11.8.0.14176`, которая может быть изменена в зависимости от потребностей и итераций версий.

```
api "com.tencent.liteav:LiteAVSDK_Professional:11.8.0.14176"
```

Измените зависимости в вашем Podfile, чтобы указать версию TXLiteAVSDK_Professional, например установите её на `11.8.15669`, которая может быть изменена в зависимости от потребностей и итераций версий.

```
pod 'TXLiteAVSDK_Professional', '11.8.15669'
```

3. Загрузите файлы моделей в соответствии с [совместимостью файла модели с SDK](https://www.tencentcloud.com/document/product/647/60479#8e1c4015-d0f9-4b57-8f81-4c6c23820ca7) и добавьте их в проекты Android Studio и Xcode.

Android

iOS

После распаковки скопируйте файл `LiteavSegmentModel.zip` в директорию `assets` вашего проекта Android.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d86250d181311ef9c015254002977b6.png)

После распаковки перетащите файл `LiteavSegmentModel.bundle` в ваш проект Xcode.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2daf6700181311efb366525400762795.png)

## Включение размытого фона

Дизайн UI TUICallKit поддерживает установку размытого фона. Вызвав следующий интерфейс, вы можете отобразить кнопку функции размытого фона на UI. Нажатие кнопки напрямую включит функцию размытого фона.

```
TUICallKit.instance.enableVirtualBackground(true);
```

## Установка фона с изображением (опционально)

Реализация фона с изображением должна быть выполнена пользователем. Добавьте файл изображения в проект Flutter (вам нужно добавить ресурсы в файл pubspec.yaml) и вызовите интерфейс для установки фонового изображения (в настоящее время поддерживаются только локальные пути изображений, сетевые изображения пока не поддерживаются).

```
TUICallEngine.instance.setVirtualBackground("***.png", (code, message) { });
```

## Часто задаваемые вопросы

### Размытый фон не реагирует или задерживается?

- Убедитесь, что вы приобрели пакет `Group Call`, см. [Активация сервиса](https://www.tencentcloud.com/document/product/647/59832#) для получения дополнительных сведений.
- Убедитесь, что файл модели загружен локально.

Если файл модели не добавлен в локальный путь, при включении функции размытого фона SDK загрузит файл модели. При нормальных условиях сети загрузка займёт 1~3 сек; чем хуже сеть, тем дольше это займёт.

- Проверьте соответствие файла модели и SDK.

### Как согласовать файл модели с SDK?

TUICallKit — это сценарий видео- и аудиозвонков, реализованный на основе Chat SDK и TRTC SDK. Виртуальный фон — это отличительная функция, предоставляемая TRTC SDK. Важно отметить, что файл модели виртуального фона должен соответствовать версии TRTC SDK; в противном случае функция размытого фона может работать неправильно. В таблице ниже указаны отношения между файлами моделей и версиями TRTC SDK:

| Версия SDK | Адрес загрузки файла модели виртуального фона |
| --- | --- |
| com.tencent.liteav:LiteAVSDK_Professional:11.7.0.12001 | [segmention_1.0](https://liteav.sdk.qcloud.com/sdkres/feature/virtual_background/model/versions/1.0/segmention_model_1.0.zip) |
| com.tencent.liteav:LiteAVSDK_Professional:11.8.0.14176 | [segmention_2.0](https://liteav.sdk.qcloud.com/sdkres/feature/virtual_background/model/versions/2.0/person_segmention_2.0.zip) |


---
*Источник: [https://trtc.io/document/60479](https://trtc.io/document/60479)*

---
*Источник (EN): [virtual-background.md](./virtual-background.md)*
