# Экран сообщений (Android & IOS & Flutter)

## Введение в функции

Интерактивная функция Danmaku поддерживает следующие возможности: отправка сообщений с ливнем, вставка пользовательских сообщений, настройка стилей сообщений и т. д. Сообщения Danmaku поддерживают ввод эмодзи, делая сообщения более интересными и взаимодействие более приятным.

## Инструкции по использованию

После успешной [интеграции TUIRoomKit](https://www.tencentcloud.com/document/product/647/54843) и успешного входа вы можете использовать эту функцию. TUIRoomKit поддерживает следующие функции экрана сообщений:

- Отправка и получение текстовых сообщений или эмодзи.
- Скрытие кнопки экрана сообщений.
- Экран сообщений автоматически исчезает через 5 секунд.

| Экран сообщений | Отправка эмодзи | Скрытие экрана сообщений (нижняя панель: настройки) |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5ca781620eab11f09ecc52540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/596c906b0eab11f09d28525400bf7822.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/832cc7960eaa11f0b3015254001c06ec.png) |

## Настройка функций

Если текущий интерфейс не соответствует вашим требованиям, вы можете изменить его, модифицируя исходный код для достижения желаемого пользовательского интерфейса. Для различных платформ см.:

Android

iOS

Flutter

Вы можете достичь желаемого пользовательского интерфейса, модифицируя исходный код в директории [Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/main/floatchat](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/main/floatchat). Для более удобной настройки пользовательского интерфейса здесь приводится описание файлов экрана сообщений.

```
// Расположение: Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/main/floatchatFloatChat         ├── View   │   ├── MessageBarrageView.java       // Интерфейс для каждого сообщения с ливнем  │   └── FloatChatSendView.java        // Интерфейс поля ввода для отправки экрана сообщений  ├── TUIFloatChatButton.java           // Кнопка отправки для экрана сообщений  └── TUIFloatChatDisplayView.java      // Область для отображения сообщений экрана
```

Вы можете достичь желаемого пользовательского интерфейса, модифицируя исходный код в директории Source/Common/Components/FloatChat. Для более удобной настройки пользовательского интерфейса здесь приводится описание файлов экрана сообщений.

```
FloatChat         ├── FloatChatButton.swift          // Кнопка отправки экрана сообщений  ├── FloatChatDisplayView.swift      // Область для отображения сообщений экрана  └── FloatChatInputController.swift      // Интерфейс поля ввода для отправки экрана сообщений
```

Компонент экрана сообщений Flutter находится в плагине [tencent_float_chat_widget](https://pub.dev/packages/tencent_float_chat_widget). Вы можете достичь желаемого пользовательского интерфейса, модифицируя исходный код в директории `tencent_float_chat_widget/lib/float_chat`. Для более удобной настройки пользовательского интерфейса здесь приводится описание файла экрана сообщений.

```
// Расположение файла: tencent_float_chat_widget/lib/float_chat
```

## Критический код

Android

iOS

Flutter

### Основной API

Компонент чата с экраном сообщений предоставляет в основном два API:

[`TUIFloatChatButton`](https://github.com/Tencent-RTC/TUIRoomKit/blob/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/main/floatchat/TUIFloatChatButton.java): После нажатия открывает интерфейс отправки экрана сообщений.

[`TUIFloatChatDisplayView`](https://github.com/Tencent-RTC/TUIRoomKit/blob/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/main/floatchat/TUIFloatChatDisplayView.java): Область для отображения сообщений экрана.

В сценариях, где требуется отправка сообщений экрана, создайте TUIFloatChatButton. При нажатии появляется интерфейс ввода.

```
TUIFloatChatButton button = new TUIFloatChatButton(mContext, roomId);mButtonContainer.addView(button);
```

В сценариях, где требуется отображение сообщений экрана, используйте TUIFloatChatDisplayView для отображения сообщений экрана.

```
TUIFloatChatDisplayView view = new TUIFloatChatDisplayView(mContext, roomId);mLayoutDisplayViewContainer.addView(view);
```

Компонент чата с экраном сообщений в основном состоит из двух частей:

**FloatChatButton**: После нажатия открывает интерфейс отправки экрана сообщений.

**FloatChatDisplayView**: Область для отображения сообщений экрана.

Вы можете создать эти два компонента самостоятельно и поместить их в любую позицию представления.

```
let floatchatButton = FloatChatButton()floatchatButton.updateRoomId(roomId:"your room Id") // Установите roomIdself.view.addSubView(floatchatButton)
```

```
let displayView = FloatChatDisplayView()self.view.addSubView(displayView)
```

В компоненте чата с экраном сообщений ([tencent_float_chat_widget](https://pub.dev/packages/tencent_float_chat_widget)) внешне открыты следующие классы:

- **FloatChatWidget**: Содержит кнопку чата с экраном сообщений и область отображения сообщений экрана. Вы можете выполнить компоновку следующим образом, где необходимо:

```
import 'package:tencent_float_chat_widget/tencent_float_chat_widget.dart';                       FloatChatWidget(roomId: yourRoomId)  // Компоновка там, где требуется, введите roomId комнаты для отправки и получения сообщений.
```

- **InputWidget**: Поле ввода для отправки сообщений чата с экраном. Вы должны разместить его на самом верхнем уровне `Stack` на странице, которую вы компонуете, чтобы он не был закрыт другими компонентами. После завершения компоновки он по умолчанию не отображается. Как только вы нажмете кнопку чата с экраном сообщений в **FloatChatWidget**, поле ввода и клавиатура автоматически появятся.

```
import 'package:tencent_float_chat_widget/tencent_float_chat_widget.dart';Stack(    children: [      ...yourWidget,        // Еще один из ваших виджетов, здесь как пример      const InputWidget(),  // Поле ввода для отправки сообщений чата с экраном    ],)
```

- **FloatChatManager**: Класс предоставляет метод deleteStatus(). Когда вы выходите из текущей комнаты, этот метод должен быть вызван для очистки статуса чата с экраном сообщений.

```
import 'package:tencent_float_chat_widget/tencent_float_chat_widget.dart';FloatChatManager().deleteStatus();
```

> **Примечание:** Если у вас есть какие-либо требования или отзывы во время процесса интеграции и использования, вы можете связаться по адресу: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/68975](https://trtc.io/document/68975)*

---
*Источник (EN): [bullet-screen-chat-android-ios-flutter.md](./bullet-screen-chat-android-ios-flutter.md)*
