# Живые комментарии

В этом руководстве показано, как использовать модуль `BarrageStore` в фреймворке `AtomicXCore` для быстрого добавления надежной, высокопроизводительной системы баража (оверлея живого чата) в приложение прямой трансляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e62bfa87f76211f0822d525400074c32.png)

## Основные возможности

`BarrageStore` предоставляет полное решение для живых комментариев в приложениях прямой трансляции. Ключевые возможности включают:

- Получение и отображение живых комментариев в трансляционной комнате.
- Отправку живых комментариев для взаимодействия с аудиторией.
- Отправку пользовательских живых комментариев для поддержки расширенных сценариев, таких как подарки, лайки и другое.
- Вставку системных подсказок в локальный список сообщений (например, "Добро пожаловать в трансляционную комнату").

## Основные концепции

| **Основная концепция** | **Тип** | **Основная ответственность и описание** |
| --- | --- | --- |
| [Barrage](https://tencent-rtc.github.io/TUIKit_Flutter/api_barrage_barrage_store/Barrage-class.html) | `class` | Представляет модель данных для живого комментария. Содержит всю ключевую информацию, такую как информация об отправителе (`sender`), содержание сообщения (`textContent` или `data`) и тип сообщения (`messageType`). |
| [BarrageState](https://tencent-rtc.github.io/TUIKit_Flutter/api_barrage_barrage_store/BarrageState-class.html) | `class` | Представляет текущее состояние модуля живых комментариев. Его основной атрибут `messageList` является `ValueListenable<List<Barrage>>`, хранит все живые комментарии в трансляционной комнате в хронологическом порядке, служит источником данных для отрисовки UI. |
| [BarrageStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_barrage_barrage_store/BarrageStore-class.html) | `class` | Центральный менеджер живых комментариев. Используется для отправки сообщений (`sendTextMessage`, `sendCustomMessage`) и прослушивания свойства `barrageState.messageList` для получения и отслеживания всех обновлений живых комментариев. |

## Этапы реализации

### Шаг 1: Интеграция компонента

- **Прямая трансляция**: обратитесь к [быстрой интеграции](https://www.tencentcloud.com/document/product/647/77552) для безупречной интеграции с **AtomicXCore** и доступу к услугам.
- **Голосовая чат-комната**: обратитесь к [быстрой интеграции](https://www.tencentcloud.com/document/product/647/77561) для безупречной интеграции с **AtomicXCore** и доступу к услугам.

Вернитесь в текущий проект после интеграции.

### Шаг 2: Инициализация и прослушивание обновлений живых комментариев

Создайте экземпляр `BarrageStore`, привязанный к `liveId` текущей трансляционной комнаты, и установите прослушиватель для получения обновлений полного списка живых комментариев в реальном времени.

```
import 'package:flutter/foundation.dart';import 'package:atomic_x_core/atomicxcore.dart';class BarrageManager {  final String liveId;  late final BarrageStore barrageStore;  late final VoidCallback _messageListChangedListener = _onMessageListChanged;  // Expose message list change notification to the public  final ValueNotifier<List<Barrage>> messagesNotifier =       ValueNotifier<List<Barrage>>([]);  BarrageManager({required this.liveId}) {    // 1. Get the singleton of BarrageStore by liveId (location parameter)    barrageStore = BarrageStore.create(liveId);    // 2. Start listening to the bullet screen immediately after initialization    _subscribeToBarrageUpdates();  }  void _subscribeToBarrageUpdates() {    // 3. Use ValueListenable's addListener to listen for messages list adjustment    barrageStore.barrageState.messageList.addListener(_messageListChangedListener);  }  void _onMessageListChanged() {    // 4. When the messageList is updating, get the new list and notify the UI layer    // Key point: The complete list obtained here contains ALL historical messages    messagesNotifier.value = barrageStore.barrageState.messageList.value;  }  void dispose() {    barrageStore.barrageState.messageList.removeListener(_messageListChangedListener);    messagesNotifier.dispose();  }}
```

### Шаг 3: Отправка живого комментария

Вызовите метод `sendTextMessage` для трансляции живого комментария всем пользователям в трансляционной комнате.

```
extension BarrageManagerSend on BarrageManager {  Send a text bullet screen  Future<void> sendTextMessage(String text) async {    // Recommendation: Add non-null verification to avoid sending invalid messages.    if (text.isEmpty) {      debugPrint("Bullet screen content cannot be empty");      return;    }    // Call this API to send a message    final result = await barrageStore.sendTextMessage(      text: text,      extensionInfo: null,    );    // Use isSuccess to check the result    if (result.isSuccess) {      debugPrint("Bullet screen text '$text' sent successfully");    } else {      debugPrint("Bullet screen text sending failure: ${result.errorMessage}");    }  }}
```

**Параметры API:**

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `text` | `String` | Отправляемое текстовое содержимое. |
| `extensionInfo` | `Map<String, String>?` | Дополнительная информация расширения. |

### Шаг 4: Отправка пользовательских живых комментариев

Отправка сообщений, содержащих пользовательские бизнес-данные, такие как подарки или лайки. Эти сообщения невидимы для других клиентов и должны быть разобраны вашей бизнес-логикой.

```
import 'dart:convert';extension BarrageManagerCustom on BarrageManager {  /// Send a custom barrage item, for example for sending a gift  Future<void> sendGiftMessage({    required String giftId,    required int giftCount,  }) async {    // 1. Define a business ID    const businessID = "live_gift";    // 2. Encode business data as a JSON string    final giftData = {"gift_id": giftId, "gift_count": giftCount};    final jsonString = jsonEncode(giftData);    // 3. Call this API to send custom messages    final result = await barrageStore.sendCustomMessage(      businessID: businessID,      data: jsonString,    );    if (result.isSuccess) {      debugPrint("Gift message (custom barrage item) sent successfully");    } else {      debugPrint("Gift message send fail: ${result.errorMessage}");    }  }}
```

**Параметры API:**

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `businessID` | `String` | Уникальный идентификатор бизнеса (например, "live_gift") для различения пользовательских сообщений. |
| `data` | `String` | Бизнес-данные, обычно строка в формате JSON. |

### Шаг 5: Вставка локальных подсказок

Вставьте локальное сообщение в список сообщений текущего пользователя. Это сообщение не будет отправлено другим пользователям в трансляционной комнате. Подходит для отображения приветствия системы, предупреждений или подсказок операций.

```
extension BarrageManagerLocal on BarrageManager {  Insert a welcome notification into the local message list  void showWelcomeMessage(LiveUserInfo user) {    // 1. Create a Barrage message (using named parameters construct function)    final welcomeTip = Barrage(      messageType: BarrageType.text,      Welcome ${user.userName} to the live room.    );    // 2. Call this API to insert it into the local list    barrageStore.appendLocalTip(welcomeTip);  }}
```

### Шаг 6: Управление разрешениями на отправку сообщений пользователем (заглушение и разблокировка)

В качестве ведущего или администратора вы можете управлять разрешением пользователя на отправку сообщений в трансляционной комнате для поддержания здоровой коммуникационной среды.

#### Заглушение или разблокировка отдельных пользователей

Заглушение или разблокировку определенных пользователей можно осуществить с помощью API `disableSendMessage` в `LiveAudienceStore`.

```
// 1. Get the LiveAudienceStore instance bound to the current live streaming room (location parameter)final liveId = "your_live_id";final audienceStore = LiveAudienceStore.create(liveId);// 2. Define the operating user ID and mute statusfinal userIdToMute = "user_id_to_be_muted";final shouldDisable = true; // true for mute, false for unblock// 3. Call API to perform operationfinal result = await audienceStore.disableSendMessage(  userID: userIdToMute,  isDisable: shouldDisable,);if (result.isSuccess) {  debugPrint("${shouldDisable ? "mute" : "unblock"} user $userIdToMute successfully");} else {  debugPrint("Operation failure: ${result.errorMessage}");}
```

#### Включение/отключение глобального заглушения

Для заглушения всех пользователей в трансляционной комнате (обычно исключая хоста) обновите информацию трансляционной комнаты через `LiveListStore`.

```
// 1. Get the LiveListStore singletonfinal liveListStore = LiveListStore.shared;// 2. Get the current live room information, create a new LiveInfo object, and modify the global mute statusfinal currentLiveInfo = liveListStore.liveState.currentLive.value;final updatedLiveInfo = LiveInfo(  liveID: currentLiveInfo.liveID,  liveName: currentLiveInfo.liveName,  isMessageDisable: true, // true for mute all, false for shutdown);// 3. Call the update API and specify the modify flags listfinal result = await liveListStore.updateLiveInfo(  liveInfo: updatedLiveInfo,  modifyFlagList: [ModifyFlag.isMessageDisable],);if (result.isSuccess) {  debugPrint("Global mute status updated successfully");} else {  debugPrint("Operation failure: ${result.errorMessage}");}
```

## Полный пример UI

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';class BarrageWidget extends StatefulWidget {  final String liveId;  const BarrageWidget({Key? key, required this.liveId}) : super(key: key);  @override  State<BarrageWidget> createState() => _BarrageWidgetState();}class _BarrageWidgetState extends State<BarrageWidget> {  late BarrageManager _barrageManager;  final TextEditingController _inputController = TextEditingController();  final ScrollController _scrollController = ScrollController();  @override  void initState() {    super.initState();    _barrageManager = BarrageManager(liveId: widget.liveId);  }  void _scrollToBottom() {    WidgetsBinding.instance.addPostFrameCallback((_) {      if (_scrollController.hasClients) {        _scrollController.animateTo(          _scrollController.position.maxScrollExtent,          duration: const Duration(milliseconds: 200),          curve: Curves.easeOut,        );      }    });  }  @override  void dispose() {    _barrageManager.dispose();    _inputController.dispose();    _scrollController.dispose();    super.dispose();  }  @override  Widget build(BuildContext context) {    return Column(      children: [        // Bullet screen list        Expanded(          child: ValueListenableBuilder<List<Barrage>>(            valueListenable: _barrageManager.messagesNotifier,            builder: (context, messageList, child) {              // Scroll to the bottom              _scrollToBottom();              return ListView.builder(                controller: _scrollController,                itemCount: messageList.length,                itemBuilder: (context, index) {                  final barrage = messageList[index];                  return _buildBarrageItem(barrage);                },              );            },          ),        ),        // input box        _buildInputBar(),      ],    );  }  Widget _buildBarrageItem(Barrage barrage) {    return Container(      margin: const EdgeInsets.symmetric(vertical: 4, horizontal: 8),      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),      decoration: BoxDecoration(        color: Colors.black54,        borderRadius: BorderRadius.circular(16),      ),      child: RichText(        text: TextSpan(          children: [            TextSpan(              text: '${barrage.sender.userName}: ',              style: const TextStyle(                color: Colors.yellow,                fontSize: 14,                fontWeight: FontWeight.bold,              ),            ),            TextSpan(              text: barrage.textContent,              style: const TextStyle(color: Colors.white, fontSize: 14),            ),          ],        ),      ),    );  }  Widget _buildInputBar() {    return Container(      padding: const EdgeInsets.all(8),      color: Colors.white,      child: Row(        children: [          Expanded(            child: TextField(              controller: _inputController,              decoration: const InputDecoration(                hintText: 'Say something...',                border: OutlineInputBorder(),                contentPadding: EdgeInsets.symmetric(horizontal: 12),              ),              onSubmitted: (_) => _sendMessage(),            ),          ),          const SizedBox(width: 8),          ElevatedButton(            onPressed: _sendMessage,            child: const Text('Send')          ),        ],      ),    );  }  void _sendMessage() {    final text = _inputController.text.trim();    if (text.isNotEmpty) {      _barrageManager.sendTextMessage(text);      _inputController.clear();    }  }}
```

## Продвинутое использование: Оптимизация производительности для высокой конкурентности

После интеграции функции живых комментариев с `BarrageStore` вам может потребоваться обработка более сложных сценариев для обеспечения гладкого и стабильного взаимодействия пользователя, особенно при трансляциях с высокой конкурентностью. Следующие варианты использования предоставляют практические стратегии оптимизации и образцы кода.

### Сценарий 1: Обработка живых комментариев при высокой конкурентности

Во время крупных событий в трансляционную комнату могут присоединиться большое количество зрителей, вызывая обновление живых комментариев десятки раз в секунду.

#### **Технический вызов**

SDK отправляет полный список живых комментариев с высокой частотой. Если пользовательский интерфейс перестраивается при каждом обновлении, главный поток может быть перегружен операциями макета и отрисовки, что приводит к задержкам.

#### **Стратегия оптимизации: пакетная обработка и подавление дребезга**

Вместо ответа на каждое обновление установите временный порог (например, 300 мс). Обновляйте пользовательский интерфейс только в том случае, если с момента последнего обновления прошло достаточно времени. Это сокращает перерисовку пользовательского интерфейса с десятков в секунду до всего нескольких, значительно улучшая плавность.

```
class BarrageUIManager {  List<Barrage>? _latestMessageList;  Timer? _refreshTimer;  final void Function(List<Barrage>) onUpdate;  BarrageUIManager({required this.onUpdate}) {    // Check whether need to refresh every 0.3 seconds    _refreshTimer = Timer.periodic(      const Duration(milliseconds: 300),      (_) => _refreshUIIfNeeded(),    );  }  /// This method is frequently invoked externally with the latest full list  void update(List<Barrage> fullList) {    _latestMessageList = fullList;  }  void _refreshUIIfNeeded() {    // Check whether there is new data pending refresh    final newList = _latestMessageList;    if (newList == null) return;    _latestMessageList = null; // Clear flags to avoid repeated refresh        // Update data source and refresh UI    onUpdate(newList);  }  void dispose() {    _refreshTimer?.cancel();  }}
```

### Сценарий 2: Поддержание стабильности памяти для длительных трансляций

Ваше приложение может потребоваться поддержка часовых или даже круглосуточных непрерывных трансляций, таких как игровые или медленные трансляции. Приложение должно оставаться стабильным и избегать сбоев из-за долгосрочной работы.

#### Технический вызов

`messageList` SDK растет неограниченно во время длительных трансляций. Даже с дросселированными обновлениями пользовательского интерфейса базовый массив данных может потреблять чрезмерное количество памяти, что в конечном итоге приводит к сбою.

#### **Стратегия оптимизации: циклический буфер фиксированного размера**

**Ограничьте количество сообщений, которые ваш источник данных сохраняет**. Независимо от размера полного списка SDK, отображайте только последние сообщения в вашем приложении.

```
void _refreshUIIfNeeded() {  final fullList = _latestMessageList;  if (fullList == null) return;  _latestMessageList = null;  // Key point: Take the latest N messages  const capacity = 500; // The client keeps the latest 500 messages only  final cappedList = fullList.length > capacity       ? fullList.sublist(fullList.length - capacity)      : fullList;  onUpdate(cappedList);}
```

## Документация API

Для получения подробной информации о ВСЕХ открытых интерфейсах, атрибутах и методах [BarrageStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_barrage_barrage_store/BarrageStore-class.html) и связанных с ним классов, см. официальную документацию API, включенную в фреймворк [AtomicXCore](https://tencent-rtc.github.io/TUIKit_Flutter/index.html).

## Часто задаваемые вопросы

### Как реализовать цветные живые комментарии, подарки или другие пользовательские стили?

Используйте пользовательские сообщения с `sendCustomMessage`. `BarrageStore` дает вам полную гибкость для бизнес-специфичных живых комментариев.

1. **Определите структуру данных:** Работайте со своей командой клиента и сервера, чтобы определить структуру JSON пользовательских сообщений. Например, цветной экран может быть определен следующим образом:

```
{  "type": "colored_text",  "text": "This is a color bullet screen!",  "color": "#FF5733" }
```

2. **Отправитель:** при отправке преобразуйте эту структуру JSON в строку и отправьте ее через параметр `data` `sendCustomMessage`. `businessId` можно установить на уникальный идентификатор, представляющий ваш бизнес, например "`barrage_style_v1`".
3. **Получатель**: после получения живых комментариев проверьте, является ли его `messageType` `.custom` и соответствует ли `businessId`. Если совпадает, разберите строку `data` (обычно парсинг JSON) и отрисуйте пользовательский стиль пользовательского интерфейса на основе разобранных данных (таких как `color, text`).

### Если я вызываю BarrageStore.create("some_id") в разных классах или файлах, создаст ли это несколько экземпляров?

Нет. Внутренняя логика `AtomicXCore` гарантирует, что при использовании одного и того же liveId вы всегда получите один и тот же экземпляр `BarrageStore` для этой трансляционной комнаты. Вам не нужно самостоятельно управлять одиночкой.

### Почему я не вижу отправленное сообщение в списке сообщений после вызова sendTextMessage?

**Устранение неполадок**:

1. **Проверьте результат**: метод sendTextMessage предоставляет обратный вызов завершения. Проверьте, успешен результат или нет. Если это не удалось, сообщение об ошибке будет указывать причину (например, "Вы были заглушены", "Ошибка сети" и т. д.).
2. **Подтвердите время подписки**: убедитесь, что вы подписались на barrageStore.state после того, как трансляционная комната для соответствующего liveId начала работу. Если вы начнете прослушивание до присоединения к трансляционной комнате, вы можете пропустить некоторые сообщения.
3. **Проверьте liveId**: убедитесь, что liveId, используемый при создании экземпляра BarrageStore, присоединении к трансляционной комнате и отправке сообщений, точно одинаков (чувствителен к регистру).
4. **Проблемы с сетью**: убедитесь, что устройство имеет рабочее сетевое соединение. Отправка сообщений зависит от подключения к сети.

### Как новые зрители могут видеть сообщения баража, отправленные до присоединения к трансляционной комнате?

`AtomicXCore` поддерживает получение истории живых комментариев, но это требует простой конфигурации в **консоли сервера**. После настройки SDK автоматически обрабатывает все остальное без необходимости писать дополнительный код.

#### **Шаг 1: Конфигурация в Live Console**

1. Войдите в [**консоль > Live > Configuration**](https://console.trtc.io/live/configuration) и выберите целевое приложение вверху.
2. На странице конфигурации Live выберите **new member pull historical messages**, измените **new member viewable latest message count**, поддерживается максимум **50**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f7e29319f76211f0831c52540073fd3b.png)

**Шаг 2: Получение данных на клиента без проблем**

После этой конфигурации изменения кода на клиенте не требуются.

Когда новый пользователь присоединяется к трансляционной комнате, `AtomicXCore` автоматически получает настроенное количество исторических сообщений на уровне SDK. Эти сообщения доставляются вашему пользовательскому интерфейсу через ту же `v` подписку, которую вы уже используете. Ваше приложение получит и отобразит эти исторические бараажи точно так же, как сообщения в реальном времени.


---
*Источник: [https://trtc.io/document/77555](https://trtc.io/document/77555)*

---
*Источник (EN): [live-comments.md](./live-comments.md)*
