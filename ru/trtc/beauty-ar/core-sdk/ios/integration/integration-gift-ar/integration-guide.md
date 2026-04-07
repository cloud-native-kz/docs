# Руководство по интеграции

Этот документ в основном описывает, как быстро интегрировать Tencent Gift AR SDK в ваш проект. Выполните следующие шаги конфигурации для завершения работ по интеграции SDK.

## Требования к среде разработки

- Xcode 9.0+.
- iPhone или iPad под управлением iOS 9.0 или более поздней версии.
- Проект настроен с действительной подписью разработчика.

## Руководство по интеграции

### Ручная интеграция

1. Загрузите [MediaX_Android_iOS_Latest.zip](https://mediacloud-76607.gzc.vod.tencent-cloud.com/MediaX/download/latest/MediaX_iOS_SDK_Latest.zip). После завершения загрузки распакуйте архив, чтобы получить файлы библиотеки SDK.
2. Используйте Gift AR Player. Необходимо интегрировать следующие frameworks:

**Библиотека SDK**

  - TCMediaX.xcframework
  - TCEffectPlayer.xcframework
  - libtcpag.xcframework
  - YTCommonXMagic.framework

**Системная база данных**

  - libz.tbd
  - libc++.tbd
  - AVFoundation.framework

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dce8bb4904a211f08c4452540044a08e.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dce67b3a04a211f09c4a5254001c06ec.png)

3. Установите флаги компоновщика Other Linker Flags

Установите "-ObjC" в "Other linker Flags" в "Build Settings".

## Интеграция через Pods

В настоящее время Gift AR SDK поддерживает интеграцию через канал Pods. Выполните следующие шаги для интеграции Pods:

```
# Introduce TCMediaXpod 'TCMediaX', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/MediaX/iOS/podspec/release/3.3/3.3.256/TCMediaX.podspec'# Introduce TCEffectPlayerpod 'TCEffectPlayer', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/MediaX/iOS/podspec/release/3.3/3.3.256/TCEffectPlayer.podspec'# Introduce YTCommonXMagic.frameworkpod 'YTCommonXMagic', :podspec => 'https://mediacloud-76607.gzc.vod.tencent-cloud.com/MediaX/iOS/podspec/release/YTCommonXMagic_1.3.1/YTCommonXMagic.podspec'
```

TCEffectPlayer поддерживает отдельную интеграцию или интеграцию в зависимости от интеграции Tencent Cloud Player SDK. Разница между ними заключается в том, использует ли интеграция мощные возможности декодирования Tencent Cloud Player.

- Если вы используете способ независимой интеграции, тип декодера (`TCEffectConfig#vapEngineType`) видео необходимо установить как TCEPCodecTypeAVPlayer при интеграции с Tencent Cloud Player SDK.
- Если вы интегрируете упрощённый SDK Tencent Cloud Player (LiteAVSDK_Player_Mini), тип декодера видео (TCEffectConfig - vapEngineType) должен быть установлен как TCEPCodecTypeVODPlayer. Упрощённый Player SDK не требует дополнительного применения Player License.
- Если TCEffect SDK уже интегрирован в ваш проект, проверьте, включён ли Player SDK. Одновременно проверьте, подали ли вы заявку и настроили ли вы Player License, [Руководство по применению Player License](https://www.tencentcloud.com/document/product/266/51098?lang=en&pg=).
- Документацию по доступу Tencent Cloud Player см. в [документации по интеграции Tencent Cloud Player](https://www.tencentcloud.com/document/product/266/49669?lang=en&pg=).

## Применение для получения лицензии Gift AR SDK

Использование Gift AR SDK требует применения для получения Gift AR Playback License. Подробный процесс применения см. в [руководстве по применению лицензии в консоли](https://trtc.io/document/60219?platform=android&product=beautyar).

## Часто задаваемые вопросы

### Как разрешить конфликт YTCommonXMagic?

Если в ваш проект интегрирован Beauty Special Effects SDK, во время интеграции возникнет конфликт символов, поскольку как Beauty Special Effects SDK, так и Gift AR SDK используют библиотеку авторизации YTCommonXMagic.framework. В этом случае при интеграции Effect Player SDK не требуется дополнительно интегрировать YTCommonXMagic.framework. Достаточно использовать одну копию YTCommonXMagic.framework из Beauty Special Effects SDK.


---
*Источник: [https://trtc.io/document/70537](https://trtc.io/document/70537)*

---
*Источник (EN): [integration-guide.md](./integration-guide.md)*
