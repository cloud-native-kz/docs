# Чат во время конференции

Во время видеоконференций участники могут отправлять сообщения в реальном времени в область чата, обмениваться мнениями и идеями, создавать расслабленную и приятную среду общения, обмениваясь смайликами и анимациями. Чтобы поддерживать порядок на встрече, хост или администратор может установить запрет на отправку сообщений участниками в чат, обеспечивая сосредоточенность и эффективность содержания конференции. Гибко используя эти функции, видеоконференции могут обеспечить эффективный и удобный опыт общения для различных сценариев.

## Введение в функции

### Взаимодействие текстовой и мультимедийной информацией

Нажмите опцию **Chat** внизу интерфейса конференции для доступа к интерфейсу чата. Участники могут свободно отправлять **текстовые**, **картинки**, **видео** и **голосовые** сообщения, обеспечивая общение в реальном времени без нарушения хода конференции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/14e47d8839e811ef9397525400fdb830.png)

### Взаимодействие со смайликами

Нажмите **значок смайлика** в редакторе панели сообщений в интерфейсе чата, чтобы открыть список смайликов. Нажмите на соответствующий смайлик, чтобы отобразить его на панели сообщений для отправки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/15340a0139e811ef9397525400fdb830.png)

### Разрешения чата в панели управления

Хост/администратор может установить разрешения чата члена в управлении участниками. Если отключить звук, обычные члены не смогут отправлять сообщения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1511345239e811ef9c9c525400d5f8ef.png)

## Интеграция функций

### Интеграция компонента чата

Добавьте зависимость плагина [tencent_cloud_chat_message](https://pub.dev/packages/tencent_cloud_chat_message) в файл `pubspec.yaml` вашего проекта.

```
dependencies:       tencent_cloud_chat_message: latest version
```

### Конфигурация международного языка

Этот шаг обязателен. Сначала импортируйте инструменты локализации в файл точки входа приложения.

```
import 'package:tencent_cloud_chat_intl/localizations/tencent_cloud_chat_localizations.dart';
```

Затем добавьте конфигурацию локализации в записи, предоставленные пакетами третьих сторон, такими как `MaterialApp` или `GetMaterialApp`. Здесь в качестве примера используется `GetMaterialApp`:

```
GetMaterialApp(  localizationsDelegates: const [    /// Your original configuration    GlobalMaterialLocalizations.delegate,        /// Add this line    ...TencentCloudChatLocalizations.localizationsDelegates,   ],  supportedLocales: [    /// Your original configuration    ...S.delegate.supportedLocales,    /// Add this line    ...TencentCloudChatLocalizations.supportedLocales,  ],  /// Other settings)
```

### **Инициализация и вход**

Добавьте следующий код в свой проект. Его функция — завершить инициализацию и вход путем вызова соответствующих интерфейсов в компоненте чата. Этот шаг критичен, так как чат может использоваться нормально только после инициализации. Поэтому, пожалуйста, будьте терпеливы и проверьте, правильно ли настроены соответствующие параметры. Среди параметров **sdkAppId**, **userID** и **userSig** вы уже использовали их при [входе в TUIRoomKit](https://www.tencentcloud.com/document/product/647/57508#db8f1a75-1b7d-4621-b981-3d52bcad4e95).

```
import 'package:tencent_cloud_chat/components/component_config/tencent_cloud_chat_message_common_defines.dart';import 'package:tencent_cloud_chat/components/component_config/tencent_cloud_chat_message_config.dart';import 'package:tencent_cloud_chat/models/tencent_cloud_chat_models.dart';import 'package:tencent_cloud_chat/tencent_cloud_chat.dart';import 'package:tencent_cloud_chat_message/tencent_cloud_chat_message.dart';await TencentCloudChat.controller.initUIKit(    options: TencentCloudChatInitOptions(      sdkAppID: 'SDKAPPID',  // Your SDKAPPID      userID: 'userID',      // Your userID      userSig: 'userSig',    // Your userSig    ),    components: TencentCloudChatInitComponentsRelated(      usedComponentsRegister: [TencentCloudChatMessageManager.register],  // Register chat components      componentConfigs: TencentCloudChatComponentConfigs(        messageConfig: TencentCloudChatMessageConfig(          // The following configuration is recommended.          showMessageSenderName: ({groupID, topicID, userID}) => true,          showSelfAvatar: ({groupID, topicID, userID}) => true,          defaultMessageMenuConfig: ({groupID, topicID, userID}) =>              TencentCloudChatMessageDefaultMessageMenuConfig(            enableMessageForward: false,            enableMessageSelect: false,          ),        ),      ),    ),    plugins: [],);
```

### Использование смайликов (необязательно)

Если вам нужно отправлять и получать смайлики, вам необходимо выполнить следующую конфигурацию:

#### Добавление зависимостей

В файл `pubspec.yaml` вашего проекта добавьте зависимость плагина [tencent_cloud_chat_sticker](https://pub.dev/packages/tencent_cloud_chat_sticker).

#### Завершение конфигурации

В `plugins` [Инициализации и входа](https://www.tencentcloud.com/document/product/647/61632#3d0fd007-2189-48e0-8391-27d840e075f4) на предыдущем шаге добавьте следующий код:

```
plugins: [  TencentCloudChatPluginItem(    name: "sticker",    initData: TencentCloudChatStickerInitData(      useDefaultSticker: true,            // Default stickers, only this sticker pack can interoperate with TUIRoomKit from other platforms.      useDefaultCustomFace_4350: false,   // If you do not need to use TUIRoomKit from other platforms, you can enable the following emoji pack.      useDefaultCustomFace_4351: false,      useDefaultCustomFace_4352: false,      userID: 'userId',                   // Your userId    ).toJson(),    pluginInstance: TencentCloudChatStickerPlugin(      context: context,    ),  ),],
```

> **Примечание:** Чтобы уважать авторские права на дизайн смайликов, пример проекта TUIRoomKit не включает большие элементы вырезания смайликов. Перед официальным коммерческим использованием замените их на свои собственные дизайны или другие пакеты смайликов, на которые у вас есть авторские права. Пакет смайликов **Little Yellow Face по умолчанию защищен авторским правом Tencent Cloud** и может быть лицензирован за плату. Если вы хотите получить лицензию, вы можете [отправить заявку](https://console.tencentcloud.com/workorder/category) для связи с нами.

### Использование чата

Когда вы [успешно создали или присоединились к конференции](https://www.tencentcloud.com/document/product/647/57508#1.E5.AF.B91.E8.A7.86.E9.A2.91.E9.80.9A.E8.AF.9D), вам нужно передать `chatWidget` на страницу конференции `ConferenceMainPage`. После передачи кнопка чата будет **отображаться** на нижней панели инструментов. Нажатие кнопки чата автоматически перейдет на `chatWidget`.

```
Navigator.push(  context,  MaterialPageRoute(    builder: (context) => ConferenceMainPage( // Conference main page      chatWidget: TencentCloudChatMessage(          options: TencentCloudChatMessageOptions(groupID: 'yourConferenceId'),  // Your Confere      ),    ),  ),);
```

После завершения описанной выше конфигурации вы сможете нажать кнопку чата для общения во время конференции.


---
*Источник: [https://trtc.io/document/61632](https://trtc.io/document/61632)*

---
*Источник (EN): [in-conference-chat.md](./in-conference-chat.md)*
