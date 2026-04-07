# Подключение гостя

**AtomicXCore** предоставляет модуль [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html), специализированный для управления полным процессом взаимодействия аудитории с микрофоном. Разработчикам не требуется обрабатывать сложную синхронизацию состояния или взаимодействие сигнализации; вызывая всего несколько простых методов, вы можете добавить мощные возможности взаимодействия между аудиторией и хостом в ваш опыт прямой трансляции.

## Основные сценарии

`CoGuestStore` поддерживает два наиболее распространённых сценария взаимодействия с гостями:

- **Аудитория запрашивает присоединение в качестве гостя**: Зритель активно инициирует запрос на присоединение. Хост получает запрос и может выбрать принять или отклонить его.
- **Хост приглашает аудиторию присоединиться в качестве гостя**: Хост может проактивно пригласить любого зрителя в эфире присоединиться в качестве гостя.

## Этапы реализации

### Этап 1: Интеграция компонента

Обратитесь к [Быстрому старту](https://www.tencentcloud.com/document/product/647/77552) для интеграции `AtomicXCore` и `LiveCoreWidget`.

После завершения интеграции переходите к реализации функции взаимодействия с гостями.

### Этап 2: Реализация запроса аудитории на присоединение в качестве гостя

**Реализация на стороне аудитории**

В качестве зрителя ваша основная задача — **инициировать заявку, получить результаты** и **стать слушателем**.

1. **Инициировать запрос на присоединение в качестве гостя**

Когда пользователь нажимает кнопку **Запросить присоединение** в интерфейсе, вызовите метод `applyForSeat`.

```
import 'package:atomic_x_core/atomicxcore.dart';final String liveId = "room ID";final CoGuestStore guestStore = CoGuestStore.create(liveId);// Пользователь нажимает кнопку "запрос на подключение микрофона"void requestToConnect() async {    // seatIndex: индекс слота микрофона, диапазон значений -1 (автоматический выбор пустого слота) и [0, максимальное количество слотов микрофона в текущей комнате -1], timeout: период ожидания запроса (секунды)    final result = await guestStore.applyForSeat(        seatIndex: 0,         timeout: 30,         extraInfo: null,    );    if (result.isSuccess) {        print("Запрос на подключение микрофона отправлен, ожидание обработки ведущим...");    } else {        print("Ошибка при отправке запроса: ${result.errorMessage}");    }}
```

2. **Прослушивание ответа хоста**

Добавьте слушатель с помощью `addGuestListener` для получения ответа хоста.

```
late GuestListener _guestListener;// Подписка на события при инициализации WidgetVoid subscribeGuestEvents() {    _guestListener = GuestListener(        onApplicationAccepted: (hostUser) {            print("Ведущий ${hostUser.userName} согласился с вашим запросом, подготовка к подключению микрофона");            // 1. Включить камеру, микрофон             DeviceStore.shared.openLocalCamera(isFront: true);            DeviceStore.shared.openLocalMicrophone();            // 2. Обновить интерфейс здесь, например отключить кнопку заявки и отобразить статус подключения микрофона        },        onApplicationRejected: (hostUser) {            print("Ведущий ${hostUser.userName} отклонил ваш запрос");            // Всплывающее уведомление пользователю, что запрос отклонён        },        onInvitationReceived: (hostUser) {            print("Получено приглашение на подключение микрофона от ведущего ${hostUser.userName}");            // Здесь откройте диалоговое окно для выбора "Принять" или "Отклонить"            _showInvitationDialog(hostUser);        },        onKickedOffSeat: () {            print("Вы были выгнаны с микрофона ведущим");            // Обновить интерфейс, выключить камеру и микрофон        },    );    guestStore.addGuestListener(_guestListener);}@overridevoid dispose() {    guestStore.removeGuestListener(_guestListener);    super.dispose();}
```

3. **Оставить место гостя**

Когда гость хочет завершить взаимодействие, вызовите метод `disconnect` для возврата в обычное состояние зрителя.

```
// Пользователь нажимает кнопку "оставить микрофон"void leaveSeat() async {    final result = await guestStore.disconnect();    if (result.isSuccess) {        print("Успешно оставили микрофон");    } else {        print("Ошибка при оставлении микрофона: ${result.errorMessage}");    }}
```

4. **(Опционально) Отменить запрос**

Если аудитория хочет отозвать запрос до его обработки хостом, вызовите `cancelApplication`.

```
// Во время ожидания пользователь нажимает "Отменить заявку"void cancelRequest() async {    final result = await guestStore.cancelApplication();    if (result.isSuccess) {        print("Заявка отменена");    } else {        print("Ошибка при отмене запроса: ${result.errorMessage}");    }}
```

**Реализация на стороне хоста**

В качестве хоста ваши основные задачи — получить запросы, отобразить список запросов и обработать запросы.

1. **Прослушивание новых запросов гостей**

Добавляя слушатель через `addHostListener`, вы можете получить мгновенное уведомление, когда новая аудитория подаёт заявку и получите оповещение.

```
import 'package:atomic_x_core/atomicxcore.dart';final String liveId = "room ID";final CoGuestStore guestStore = CoGuestStore.create(liveId);late HostListener _hostListener;late final VoidCallback _applicantsChangedListener = _onApplicantsChanged;// Подписка на событие ведущего void subscribeHostEvents() {    _hostListener = HostListener(        onApplicationReceived: (guestUser) {            print("Получена заявка на подключение к микрофону от аудитории ${guestUser.userName}");            // Обновите интерфейс здесь, например отобразите красную точку на кнопке "список заявок"        },        onInvitationAccepted: (guestUser) {            print("Аудитория ${guestUser.userName} принимает ваше приглашение");        },        onInvitationRejected: (guestUser) {            print("Аудитория ${guestUser.userName} отклонила ваше приглашение");        },    );    guestStore.addHostListener(_hostListener);}@overridevoid dispose() {    guestStore.removeHostListener(_hostListener);    super.dispose();}
```

2. **Отобразить список запросов**

`coGuestState` в `CoGuestStore` поддерживает текущий список заявителей в реальном времени. Вы можете прослушивать его для обновления интерфейса.

```
// Подписка на обновления статусаvoid subscribeApplicants() {    guestStore.coGuestState.applicants.addListener(_applicantsChangedListener);}void _onApplicantsChanged() {    final applicants = guestStore.coGuestState.applicants.value;    print("Текущее количество заявителей: ${applicants.length}");    // Обновите интерфейс "списка заявителей" здесь    setState(() {        _applicantList = applicants;    });}@overridevoid dispose() {    guestStore.coGuestState.applicants.removeListener(_applicantsChangedListener);    super.dispose();}
```

3. **Обработка запросов гостей**

Когда вы выбираете аудиторию из списка и нажимаете "Одобрить" или "Отклонить", вызовите соответствующий метод.

```
// Ведущий нажимает кнопку "Одобрить" и импортирует userID заявителяvoid accept(String userId) async {    final result = await guestStore.acceptApplication(userId);    if (result.isSuccess) {        print("Одобрена заявка $userId, другая сторона подключается к микрофону");    }}// Ведущий нажимает кнопку "Отклонить"void reject(String userId) async {    final result = await guestStore.rejectApplication(userId);    if (result.isSuccess) {        print("Отклонена заявка $userId");    }}
```

### Этап 3: Хост приглашает аудиторию присоединиться в качестве гостя

**Реализация на стороне хоста**

1. **Пригласить члена аудитории**

Когда хост выбирает кого-то из списка аудитории и нажимает **«Пригласить присоединиться»**, вызовите метод `inviteToSeat`.

```
// Ведущий выбирает аудиторию и инициирует приглашениеvoid invite(String userId) async {    // inviteeID: ID приглашённого, seatIndex: индекс слота микрофона, диапазон значений -1 (автоматический выбор пустого слота) и [0, максимальное количество слотов микрофона в текущей комнате -1]     // timeout: период ожидания приглашения    final result = await guestStore.inviteToSeat(        inviteeID: userId,        seatIndex: 0,        timeout: 30,         extraInfo: null,    );    if (result.isSuccess) {        print("Приглашение отправлено $userId, ожидание ответа...");    }}
```

2. **Прослушивание ответа аудитории**

Используйте `HostListener` для прослушивания событий ответа на приглашение.

```
// Обратный вызов, настроенный в HostListener_hostListener = HostListener(    onInvitationAccepted: (guestUser) {        print("Аудитория ${guestUser.userName} принимает ваше приглашение");    },    onInvitationRejected: (guestUser) {        print("Аудитория ${guestUser.userName} отклонила ваше приглашение");    },);
```

**Реализация на стороне аудитории**

1. **Получить приглашение хоста**

Прослушивайте события приглашения через `GuestListener`.

```
// Обратный вызов, настроенный в GuestListener_guestListener = GuestListener(    onInvitationReceived: (hostUser) {        print("Получено приглашение на подключение микрофона от ведущего ${hostUser.userName}");        // Здесь откройте диалоговое окно для выбора "Принять" или "Отклонить"        _showInvitationDialog(hostUser);    },);
```

2. **Ответить на приглашение**

Когда пользователь делает выбор в диалоговом окне, вызовите соответствующий метод.

```
String inviterId = "ID ведущего, инициирующего приглашение"; // Получено из обратного вызова onInvitationReceived// Пользователь нажимает "Принять"void acceptInvitation() async {    final result = await guestStore.acceptInvitation(inviterId);    if (result.isSuccess) {        // Включить камеру, микрофон          DeviceStore.shared.openLocalCamera(isFront: true);        DeviceStore.shared.openLocalMicrophone();    }}// Пользователь нажимает "Отклонить"void rejectInvitation() async {    await guestStore.rejectInvitation(inviterId);}
```

### Демонстрация функции

После интеграции вышеуказанной функциональности протестируйте взаимодействие с гостями, используя двух членов аудитории и хоста. Аудитория A включает камеру и микрофон, в то время как аудитория B включает только микрофон. Полученный результат показан ниже. Вы можете обратиться к следующему разделу для дальнейшей настройки логики интерфейса.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4bc40212f76011f08586525400380f7d.png)

## Уточнение деталей интерфейса

Вы можете использовать возможность слотов, предоставляемую параметром `VideoWidgetBuilder` компонента `LiveCoreWidget`, для добавления пользовательских представлений поверх видеопотоков гостей. Это позволяет отображать ники, аватары и другую информацию, либо предоставлять изображения-заполнители при отключённой камере, улучшая общий визуальный опыт.

### Отображение ников на видеопотоках

**Эффект демонстрации**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/20cd025ff76111f0831c52540073fd3b.png)

#### **Этапы реализации**

- **Этап 1**: Создайте представление переднего плана (**CustomSeatForegroundView**), используемое для отображения информации о пользователе над видеопотоком.

```
import 'package:flutter/material.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';/// Пользовательское представление с плавающей информацией о пользователе (передний план)class CustomSeatForegroundView extends StatelessWidget {    final SeatFullInfo seatInfo;    const CustomSeatForegroundView({        Key? key,         required this.seatInfo,    }) : super(key: key);    @override    Widget build(BuildContext context) {        return Container(            color: Colors.transparent,            child: Align(                alignment: Alignment.bottomLeft,                child: Container(                    margin: const EdgeInsets.all(5),                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),                    decoration: BoxDecoration(                        color: Colors.black.withOpacity(0.5),                        borderRadius: BorderRadius.circular(12),                    ),                    child: Text(                        seatInfo.userInfo.userName,                        style: const TextStyle(                            color: Colors.white,                            fontSize: 14,                        ),                    ),                ),            ),        );    }}
```

- **Этап 2**: Создайте представление фона (**CustomSeatBackgroundView**), используемое в качестве изображения-заполнителя, когда у пользователя отсутствует видеопоток.

```
import 'package:flutter/material.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';/// Пользовательское представление с аватаром-заполнителем (фон)class CustomSeatBackgroundView extends StatelessWidget {    final SeatFullInfo seatInfo;    const CustomSeatBackgroundView({        Key? key,         required this.seatInfo,    }) : super(key: key);    @override    Widget build(BuildContext context) {        final avatarUrl = seatInfo.userInfo.avatarUrl;        return Container(            decoration: BoxDecoration(                color: Colors.grey[800],            ),            child: Center(                child: Column(                    mainAxisSize: MainAxisSize.min,                    children: [                        ClipOval(                            child: avatarUrl.isNotEmpty                                ? Image.network(                                    avatarUrl,                                     width: 60,                                     height: 60,                                    fit: BoxFit.cover,                                    errorBuilder: (context, error, stackTrace) {                                        return _buildDefaultAvatar();                                    },                                )                                : _buildDefaultAvatar(),                        ),                        const SizedBox(height: 8),                        Text(                            seatInfo.userInfo.userName,                            style: const TextStyle(                                color: Colors.white,                                fontSize: 12,                            ),                        ),                    ],                ),            ),        );    }    Widget _buildDefaultAvatar() {        return Container(            width: 60,            height: 60,            color: Colors.grey,            child: const Icon(Icons.person, size: 40, color: Colors.white),        );    }}
```

- **Этап 3**: Постройте пользовательское представление через обратный вызов `coGuestWidgetBuilder` параметра `VideoWidgetBuilder` и верните соответствующее представление на основе значения `viewLayer`.

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';import 'package:rtc_room_engine/rtc_room_engine.dart';/// Страница трансляции с пользовательским представлением подключения гостяclass CustomCoGuestLiveWidget extends StatefulWidget {    final String liveId;    const CustomCoGuestLiveWidget({        Key? key,         required this.liveId,    }) : super(key: key);    @override    State<CustomCoGuestLiveWidget> createState() => _CustomCoGuestLiveWidgetState();}class _CustomCoGuestLiveWidgetState extends State<CustomCoGuestLiveWidget> {    late LiveCoreController _controller;    @override    void initState() {        super.initState();        _controller = LiveCoreController.create();        _controller.setLiveID(widget.liveId);    }    @override    void dispose() {        _controller.dispose();        super.dispose();    }    /// Построить пользовательское представление для аудитории, подключённой к микрофону    Widget _buildCoGuestWidget(        BuildContext context,         SeatFullInfo seatFullInfo,         ViewLayer viewLayer,    ) {        if (viewLayer == ViewLayer.foreground) {            // Слой переднего плана: всегда отображается поверх видеоизображения, используется для ника, информации и т.д.            return CustomSeatForegroundView(seatInfo: seatFullInfo);        } else {            // Слой фона: отображается только при отсутствии видеопотока у соответствующего пользователя, используется для отображения изображений-заполнителей аватара            return CustomSeatBackgroundView(seatInfo: seatFullInfo);        }    }    @override    Widget build(BuildContext context) {        return Scaffold(            body: LiveCoreWidget(                controller: _controller,                videoWidgetBuilder: VideoWidgetBuilder(                    coGuestWidgetBuilder: _buildCoGuestWidget,                ),            ),        );    }}
```

#### **Описание параметров:**

| **Параметр** | **Тип** | **Примечание** |
| --- | --- | --- |
| `seatFullInfo` | `SeatFullInfo` | Объект информации о месте, содержащий подробную информацию о ведущем. |
| `seatFullInfo.userInfo.userId` | `String` | ID пользователя ведущего. |
| `seatFullInfo.userInfo.userName` | `String` | Ник пользователя на микрофоне. |
| `seatFullInfo.userInfo.avatarUrl` | `String` | URL фотографии профиля пользователя на микрофоне. |
| `viewLayer` | `ViewLayer` | Перечисление слоя представления: `ViewLayer.foreground` представляет представление-подвеску, всегда отображается поверх видеоизображения. `ViewLayer.background` означает фоновый виджет, находящийся ниже переднего слоя, отображается только при отсутствии видеопотока у пользователя (например, камера выключена), обычно используется для отображения аватара пользователя по умолчанию или изображения-заполнителя. |

## Документация API

Для получения подробной информации обо всех публичных интерфейсах, свойствах и методах [CoGuestStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html) и его связанных классов см. официальную документацию API фреймворка [AtomicXCore](https://tencent-rtc.github.io/TUIKit_Flutter/index.html). Связанные Store, используемые в этом руководстве, приведены ниже:

| Store/Компонент | Описание функции | Документация API |
| --- | --- | --- |
| LiveCoreWidget | Основной компонент представления для отображения видеопотока прямой трансляции и взаимодействия: отвечает за отображение видео и обработку виджетов, поддерживает трансляцию хоста, взаимодействие с гостями, подключение хоста и другие сценарии. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_view_live_live_core_widget/LiveCoreWidget-class.html) |
| LiveCoreController | Контроллер для LiveCoreWidget: используется для установки ID прямой трансляции, управления предпросмотром и другими операциями. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_view_live_live_core_widget/LiveCoreController-class.html) |
| VideoWidgetBuilder | Адаптер видеопредставления: используется для настройки видеовиджетов потока для взаимодействия с гостями, подключения хоста, PK и других сценариев. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_view_live_live_core_widget/VideoWidgetBuilder-class.html) |
| DeviceStore | Управление устройствами аудио/видео: микрофон (включение/отключение / громкость), камера (включение/отключение / переключение / качество), общий доступ к экрану, мониторинг статуса устройства в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_device_store/DeviceStore-class.html) |
| CoGuestStore | Управление взаимодействием с гостями: запрос/приглашение/принятие/отклонение гостя, разрешения членов гостя (микрофон/камера), синхронизация состояния. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_live_co_guest_store/CoGuestStore-class.html) |

## Часто задаваемые вопросы

### Как мне управлять жизненным циклом и событиями пользовательских представлений, добавленных через VideoWidgetBuilder?

**LiveCoreWidget** автоматически управляет добавлением и удалением представлений, возвращаемых обратным вызовом `coGuestWidgetBuilder`, поэтому вам не требуется обрабатывать их вручную. При необходимости обработки взаимодействия пользователя (например, событий клика) в пользовательском представлении просто добавьте соответствующую обработку событий при создании представления.

### Какова цель параметра ViewLayer?

`ViewLayer` используется для различения представлений переднего плана и фона.

- `ViewLayer.foreground`: слой переднего плана, всегда отображается поверх видеоизображения.
- `ViewLayer.background`: слой фона, отображается только при отсутствии видеопотока у соответствующего пользователя (например, камера не включена), обычно используется для отображения аватара по умолчанию или изображения-заполнителя пользователя.

### Почему моё пользовательское представление не отображается?

- **Проверьте настройки VideoWidgetBuilder**: убедитесь, что параметр `videoWidgetBuilder` компонента `LiveCoreWidget` установлен правильно.
- **Проверьте реализацию обратного вызова**: убедитесь, что обратный вызов `coGuestWidgetBuilder` реализован правильно.
- **Проверьте возвращаемое значение**: убедитесь, что ваша функция обратного вызова возвращает действительный экземпляр `Widget`.


---
*Источник: [https://trtc.io/document/77553](https://trtc.io/document/77553)*

---
*Источник (EN): [guest-connection.md](./guest-connection.md)*
