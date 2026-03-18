# Виртуальный фон

TUICallKit запустил новую функцию виртуального фона, позволяющую пользователям устанавливать размытый или фоновое изображение во время видеозвонков. Это скрывает реальную среду звонка, защищает конфиденциальность и делает звонок более интересным. Далее в этой статье подробно описано, как использовать эту функцию в компоненте TUICallKit.

## Эффект интеграции

Результат отображения компонента TUICallKit после интеграции функции виртуального фона выглядит следующим образом:

| Исходная камера | Эффект размытого фона | Эффект фонового изображения |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/05d6304918ed11efac7f5254007bbd8c.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/06ae308e18ed11ef88ad5254002977b6.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/063e4ee718ed11ef8bfe5254002fd0a8.png) |

## Требования подготовки

1. Перед использованием функции Virtual Background от Tencent Cloud вам необходимо посетить консоль для активации служб аудио и видео для вашего приложения и приобрести пакет `Group Call`. Подробные инструкции см. в разделе [Активировать сервис.](https://www.tencentcloud.com/document/product/647/59832#)
2. Загрузите файл [Virtual Background Model](https://www.tencentcloud.com/document/product/647/60490#8e1c4015-d0f9-4b57-8f81-4c6c23820ca7), распакуйте его и скопируйте файл `LiteavSegmentModel.zip` в директорию `assets` вашего проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/150f3ff6008611ef9125525400275b90.png)

3. В директории `tuicallkit-kt` проекта найдите файл `build.gradle` и замените версию `TRTC SDK` на Professional Version.

```
api "com.tencent.liteav:LiteAVSDK_Professional:11.8.0.14176"
```

> **Примечание:** Существует соответствие между версией TRTC SDK и файлом модели, убедитесь, что номер версии соответствует модели, см. ниже: [Соответствие файла модели с SDK](https://www.tencentcloud.com/document/product/647/60490#8e1c4015-d0f9-4b57-8f81-4c6c23820ca7).

## Включение размытого фона

Дизайн пользовательского интерфейса TUICallKit поддерживает установку размытого фона. Вызвав следующий интерфейс, вы можете отобразить кнопку функции размытого фона в пользовательском интерфейсе. Нажатие кнопки напрямую включит функцию размытого фона.

```
TUICallKit.createInstance(getApplicationContext()).enableVirtualBackground(true);
```

## Установка фонового изображения (опционально)

Реализация фонового изображения требует от пользователей локального сохранения изображения. После сохранения вызовите следующий интерфейс для установки (в настоящее время поддерживаются только изображения с локальным путем, изображения с uri пока не поддерживаются).

```
TUICallEngine.createInstance(context).setVirtualBackground("imagePath", null)
```

## Часто задаваемые вопросы

### Включение размытого фона не реагирует или работает с задержкой?

- Убедитесь, что вы приобрели пакет аудио и видеозвонков `Group Call`, см. [Активировать сервис.](https://www.tencentcloud.com/document/product/647/59832#)
- Убедитесь, что файл модели загружен локально.

Если файл модели не добавлен в локальный путь, при включении функции размытого фона SDK загрузит файл модели. При нормальных условиях сети загрузка занимает 1–3 секунды; чем хуже сеть, тем дольше это займет.

- Проверьте, соответствует ли файл модели и SDK друг другу.

### Как согласовать файлы модели с SDK?

TUICallKit основан на Chat SDK и TRTC SDK для сценариев аудио и видеозвонков. Виртуальный фон — это функция, предоставляемая TRTC SDK. Существует соответствие между файлом модели виртуального фона и версией TRTC SDK. Если они не совпадают, включение размытого фона может быть неэффективным. Соответствие между файлом модели и TRTC SDK представлено ниже:

| Версия SDK | Адрес загрузки файла модели виртуального фона |
| --- | --- |
| com.tencent.liteav:LiteAVSDK_Professional:11.7.0.12001 | [segmention_1.0](https://liteav.sdk.qcloud.com/sdkres/feature/virtual_background/model/versions/1.0/segmention_model_1.0.zip) |
| com.tencent.liteav:LiteAVSDK_Professional:11.8.0.14176 | [segmention_2.0](https://liteav.sdk.qcloud.com/sdkres/feature/virtual_background/model/versions/2.0/person_segmention_2.0.zip) |


---
*Источник: [https://trtc.io/document/60490](https://trtc.io/document/60490)*

---
*Источник (EN): [virtual-background.md](./virtual-background.md)*
