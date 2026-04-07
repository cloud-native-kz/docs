# Планирование конференций

**Если пользовательский интерфейс конференции (TUIRoomKit) не соответствует требованиям вашего продукта, и вам требуется собственная логика взаимодействия и бизнес-логика для пользовательской реализации функций взаимодействия, связанных с запланированной конференцией, вы можете интегрировать TUIRoomEngineSDK и обратиться к**[ключевому коду](https://www.tencentcloud.com/document/product/647/63139#14dd6ab2-f191-4934-9447-a24cfb8d1a25) связанные вызовы для удовлетворения ваших потребностей.

## Описание функции

TUIRoomKit поддерживает планирование конференций, позволяя пользователям забронировать комнату и запланировать конференцию. В этой статье подробно описаны функции этой возможности и объяснено, как ее использовать в компоненте TUIRoomKit.

| Планирование конференции | Список конференций | Настройка конференции | Приглашение участников |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3217e0227b1411ef8829525400fdb830.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4649c9477b1411ef8631525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63b0da5f7b1411ef8631525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7f5f98d47b1411efb9d8525400f69702.png) |

## Интеграция функции

Перед использованием функции планирования конференции необходимо завершить соответствующую конфигурацию для TUIRoomKit и **войти**. Дополнительные сведения см. в разделе [Быстрый доступ](https://www.tencentcloud.com/document/product/647/54843#087dff27-11d0-42ec-bb14-202b4b333452).

> **Примечание:****Функция планирования конференций требует Conference v2.5.0 и выше.**

### Как запланировать конференцию

Для использования функции планирования конференции необходимо получить доступ к странице планирования конференции, предоставляемой TUIRoomKit:

Android

iOS

Flutter

В соответствии с вашим бизнесом просто вызовите следующий код в соответствующей Activity для планирования конференции.

java

kotlin

```
Intent intent = new Intent(this, ScheduleConferenceActivity.class);
startActivity(intent);
```

```
val intent = Intent(this, ScheduleConferenceActivity::class.java)startActivity(intent)
```

```
class YourViewController: UIViewContrller {    func jumpToScheduleViewController {        let scheduleViewController = ScheduleConferenceViewController()        navigationController?.pushViewController(scheduleViewController, animated: true)  }}
```

В соответствии с вашим бизнесом при необходимости перейдите на `ScheduleRoomPage` для доступа к странице планирования конференции.

```
import 'package:tencent_conference_uikit/tencent_conference_uikit.dartNavigator.push(  context,  MaterialPageRoute(    builder: (context) => ScheduleRoomPage(),  ),);
```

- Настройка деталей конференции: Название комнаты, Тип комнаты, Время начала, Длительность комнаты, Часовой пояс, Приглашение участников (список участников должен быть импортирован), Шифрование комнаты и Управление участниками (Отключить микрофон для всех, Запретить рисование для всех).
- Как приглашать участников: Нажмите "Добавить" для приглашения участников. По умолчанию необходимо ввести список пользователей. Для удобства быстрого тестирования мы предоставляем демонстрационный список пользователей. Пожалуйста, обратитесь к разделу [Как приглашать участников](https://www.tencentcloud.com/document/product/647/63139#ca6f6f6b-ca47-4bf0-aedd-ca817ae3401d).

| Вход в интерфейс планирования конференции | Настройка деталей конференции | Конференция запланирована успешно |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c1a2c2857b1411ef80ff525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc187b477b1411ef8631525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fecf7f357b1411ef80ff525400d5f8ef.png) |

### Просмотр запланированных конференций

TUIRoomKit предоставляет компоненты пользовательского интерфейса для списка конференций. Расположив компонент списка конференций на вашей странице, вы можете просматривать и управлять всеми конференциями текущего пользователя:

Android

iOS

Flutter

1. В соответствии с вашим бизнесом добавьте макет списка конференций на вашу страницу:

```
<!-- Например, если ваш родительский макет ConstraintLayout, добавьте следующий код --><FrameLayout
    android:id="@+id/tuiroomkit_fl_conference_list_container"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintTop_toTopOf="parent"
    app:layout_constraintBottom_toBottomOf="parent"/>
```

2. Добавьте следующий код в соответствующую Activity для вызова списка конференций:

java

kotlin

```
ConferenceListFragment fragment = new ConferenceListFragment();
FragmentTransaction transaction = this.getSupportFragmentManager().beginTransaction();
transaction.add(R.id.tuiroomkit_fl_conference_list_container, fragment);
transaction.commitAllowingStateLoss();
```

```
val fragment = ConferenceListFragment()val transaction = supportFragmentManager.beginTransaction()transaction.add(R.id.tuiroomkit_fl_conference_list_container, fragment)transaction.commitAllowingStateLoss()
```

```
class YourViewController: UIView {        // Инициализация ConferenceListView требует два параметра:        // @param viewController, viewController, к которому добавляется страница списка конференций        func showConferenceList {             let listView = ConferenceListView(viewController: self)             view.addSubview(listView)        }}
```

```
import 'package:flutter/material.dart';import 'package:tencent_conference_uikit/tencent_conference_uikit.dart';// На вашей собственной странице добавьте ConferenceListWidgetclass YourPage extends StatelessWidget {  const YourPage({Key? key}) : super(key: key);  @override  Widget build(BuildContext context) {    return Scaffold(      appBar: AppBar(title: const Text("Your Page")),      body: Column(        children: [          ...YourWidgets(),              // Ваши другие виджеты, это просто пример          const ConferenceListWidget(),  // Компонент списка конференций        ],      ),    );  }}
```

Список конференций предоставляет следующие функции:

- Просмотр списка конференций: Список включает конференции, которые вы создали, и конференции, на которые вас пригласили.
- Просмотр деталей конференции: Вы можете щелкнуть на конкретную конференцию, чтобы просмотреть ее детали.
- Изменение информации о конференции: Щелкните на конференцию в списке конференций, **если конференция еще не началась и вы являетесь организатором**, вы можете отредактировать информацию для этой конференции.

| Нажмите на список конференций | Просмотр деталей конференции | Изменение информации о конференции |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4811e33b7b1511ef8631525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5d9a3ce57b1511efb9d8525400f69702.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c7c0a357b1511ef82535254002693fd.png) |

### Как приглашать участников

В интерфейсе планирования конференции или изменения конференции вы можете нажать кнопку **Участники** для вызова интерфейса выбора участников. **По умолчанию TUIRoomKit использует цепочку отношений Chat. Мы также поддерживаем установку**списка контактов**. Для разных платформ, пожалуйста, обратитесь к:

Android

iOS

Flutter

#### Установка данных контактов

Вы можете установить список контактов пользователей через метод setParticipants.

java

kotlin

```
List<ConferenceDefine.User> participants = new ArrayList<>();ConferenceDefine.User user = new ConferenceDefine.User();user.id = "Jack";participants.add(user);ConferenceSession.sharedInstance().setParticipants(participants);
```

```
// Получите список выбранных пользователейval participants = bundle.getSerializable(CONFERENCE_PARTICIPANTS) as ConferenceParticipantsval selectedList: ArrayList<User> = participants.selectedList
```

> **Примечание:**Если пользовательский интерфейс контактов TUIRoomKit не соответствует вашим потребностям, мы поддерживаем связь вашего собственного пользовательского интерфейса контактов с TUIRoomKit. Пожалуйста, обратитесь к: [Как установить пользовательские контакты](https://www.tencentcloud.com/document/product/647/63139#2599316c-d14b-4288-99b4-e9cd0aa963ef).

### Как испытать функцию приглашения участников

Сначала обратитесь к разделу [Запуск примера кода](https://www.tencentcloud.com/document/product/647/60442) и завершите демонстрацию. В файле `members.json` проекта демонстрации предварительно настроена некоторая информация о тестовых пользователях. Вы можете выбрать два учетных записи, войти с помощью настроенного userId на двух разных телефонах, а затем выбрать другого пользователя при планировании или редактировании конференции. Таким образом, запланированная конференция появится в списке расписания другого пользователя.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1ba7dada7bdd11efbe435254000bb03d.png)

### Реализация кода для страницы списка участников

Учитывая сложность данных списка пользователей на странице приглашения участников, мы разработали решение, позволяющее вам настроить интерфейс выбора участников. Далее мы покажем вам, как интегрировать вашу собственную страницу выбора участников (конечно, вы также можете напрямую использовать пользовательский интерфейс, предоставленный в демонстрации, который будет представлен позже).

1. Подготовьте свой viewController страницы выбора друзей, реализующий протокол `SelectMemberControllerProtocol`.

```
// Пример кодаclass SelectMemberViewController: UIViewController, ContactViewProtocol {    weak var delegate: ContactViewSelectDelegate?    var selectedUsers: [User]        func didSelectFinished() {    // Через делегат вызовите выбранных участников в Conference в методе, где выполняется выбор        delegate?.onMemberSelected(self, invitees: selectedMembers)    }}
```

> **Примечание:**Функция вызова в конференции также требует использования вашего компонента пользовательских контактов. Если вам все еще нужно использовать функцию вызова в конференции, рекомендуется поместить объект `ConferenceParticipants` в параметр конструктора вашей страницы контактов. Источник данных будет упомянут в коде на шаге два.Класс `ConferenceParticipants` имеет двух членов:selectedList: выбранные участники;unSelectableList: невыбираемые участники. Вы можете установить соответствующих участников как невыбираемых в пользовательском интерфейсе. Функция планирования конференций не использует это поле.

2. **Верните список выбранных пользователей из пользовательских**контактов**в TUIRoomKit:** После завершения выбора пользователей в контактах необходимо вернуть список выбранных пользователей в TUIRoomKit. Вы можете вернуть данные в TUIRoomKit, используя следующий метод.

```
// Пример кодаConferenceSession.sharedInstance.setContactsViewProvider { participants in    return SelectMemberViewController(participants: participants)}
```

3. С помощью описанных выше двух шагов вы можете отобразить вашу собственную страницу выбора участников. Мы также предоставляем код страницы в демонстрации, как показано на изображении выше. Вы можете напрямую скопировать следующие файлы в ваш проект, чтобы получить нашу пример страницу.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1b90193a7bdd11ef8631525400a9236a.png)

В методе `loadMembers` `SelectMembersViewModel` вы можете загрузить данные вашего собственного списка участников (вы также можете напрямую получить данные цепочки отношений Chat).

Когда вам нужно использовать функцию приглашения участников для приглашения участников на конференцию, мы предоставляем вам следующие два решения для добавления участников, которых вам нужно пригласить:

### Решение 1: Использование json для настройки информации о пользователе

Вы можете обратиться к нашему [примеру проекта](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Flutter/tencent_conference_uikit/example). В каталоге example/assets `members.json` хранит информацию о пользователе, необходимую для приглашений. Выполните следующие шаги:

1. В каталоге `assets` вашего проекта создайте новый файл `members.json`, в котором перечислены все необходимые вам информация о пользователе. Формат файла должен быть таким же, как упомянутый выше `members.json`.
2. В файле `pubspec.yaml` вашего проекта завершите следующую конфигурацию:

```
assets:  - assets/members.json
```

После завершения вышеупомянутой конфигурации вы сможете выбрать участников, перечисленных в `members.json`, в интерфейсе приглашения участников.

### Решение 2: Использование информации друзей Chat

Если вы не настроили упомянутый выше `members.json`, интерфейс приглашения друзей по умолчанию будет извлекать информацию о ваших друзьях Chat. Когда вам нужно пригласить других участников на конференцию, вы можете добавить участников, которых хотите пригласить, в друзья в соответствии с вашими потребностями.

- Предварительные условия: войдите в Chat SDK, процесс входа аналогичен [входу в плавающий чат](https://www.tencentcloud.com/document/product/647/57508#69f9a5eb-0191-4af4-9294-2a7dde5b4615). Если вы уже завершили процесс входа или используете [чат в конференции](https://www.tencentcloud.com/document/product/647/61632), вы можете пропустить этот шаг.
- Код для добавления друзей выглядит следующим образом:

```
import 'package:tencent_cloud_chat_sdk/manager/v2_tim_manager.dart';// В Flutter Conference уже есть зависимость от tencent_cloud_chat_sdk, поэтому отдельная конфигурация не требуется// Замените userID в коде на UserID пользователя, которого хотите добавить, чтобы завершить добавление друга V2TIMManager().getFriendshipManager().addFriend(       userID: 'userID', addType: FriendTypeEnum.V2TIM_FRIEND_TYPE_BOTH);
```

После добавления друзей вы можете выбрать для приглашения добавленных пользователей **каждый раз**, когда вы делаете резервирование.

Если вам нужны дополнительные операции с друзьями, пожалуйста, обратитесь к: [Управление друзьями](https://trtc.io/document/48157). Если вам нужно использовать REST API для массового добавления друзей, пожалуйста, обратитесь к: [Добавление друзей RestAPI](https://trtc.io/document/34902).

После завершения описанных выше шагов, нажав кнопку **Добавить**, появится интерфейс выбора участников. Здесь вы можете пригласить или удалить участников. После изменения запланированная вами конференция **появится в списке конференций другого пользователя**.

| Нажмите **Добавить** в интерфейсе планирования конференции | Добавить или удалить участников из списка пользователей |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a325dc8f7b1511ef8631525400a9236a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aee6b2107b1511ef80ff525400d5f8ef.png) |

### Примечания

- После успешного планирования конференции вы можете получить идентификатор конференции и информацию о резервировании.
- Для массового планирования конференций на разные даты/время выберите время и отправьте пакетами.
- Время начала планирования конференции не может быть раньше текущего времени, но нет ограничений на количество дней заранее.
- После достижения запланированной конференцией времени окончания, если конференция не была распущена и в конференции нет пользователей, конференция будет сохранена в течение 6 часов с момента запланированного времени окончания. В течение этого периода вы все еще можете вводить конференцию в любое время.

## Настройка функции

Если текущий пользовательский интерфейс не соответствует вашим потребностям, вы можете достичь желаемого эффекта пользовательского интерфейса, изменив исходный код. Для разных платформ, пожалуйста, обратитесь к:

Android

iOS

Flutter

Вы можете достичь желаемого эффекта пользовательского интерфейса, изменив исходный код в каталоге [Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/schedule](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/schedule). Чтобы облегчить вам настройку пользовательского интерфейса, вот введение в файл пароля комнаты.

```
SchdeuleConference   âââ ConferenceDetails          // Интерфейс деталей конференции   âââ ConferenceList             // Интерфейс списка конференций   âââ ModifyConference           // Интерфейс изменения конференции   âââ SelectScheduleParticipant  // Вызов списка контактов, переданного извне   âââ TimeZone                   // Интерфейс настройки часового пояса   âââ View                       // Интерфейс планирования конференции
```

### Как установить пользовательские контакты

1. Передайте свой пользовательский интерфейс контактов:

Вы можете использовать следующие методы для импорта ваших контактов перед [планированием конференции](https://www.tencentcloud.com/document/product/647/63139#8be0d151-7bb2-4b84-a462-5fa7ff8fe037) и [открытием списка конференций](https://www.tencentcloud.com/document/product/647/63139#c1574ffd-812a-49ff-8826-74791e61f8ff)

java

kotlin

```
// Замените SelectParticipantActivity.class на вашу activity контактовConferenceSession.sharedInstance().setContactsViewProvider(SelectParticipantActivity.class);
```

```
// Замените SelectParticipantActivity.class на вашу activity контактовConferenceSession.sharedInstance().setContactsViewProvider(SelectParticipantActivity::class.java)
```

2. Ваши контакты возвращают список выбранных пользователей в TUIRoomKit:

После завершения выбора пользователя в контактах необходимо вернуть список выбранных пользователей в TUIRoomKit. Вы можете вернуть данные в TUIRoomKit следующим образом.

java

kotlin

```
Intent intent = new Intent();// participants - это список выбранных пользователей и должен быть типа ArrayList<User>.intent.putExtra(SELECTED_PARTICIPANTS, participants);setResult(3, intent);finish();
```

```
val intent = Intent()// participants - это список выбранных пользователей и должен быть типа ArrayList<User>.intent.putExtra(SELECTED_PARTICIPANTS, participants)setResult(3, intent)finish()
```

3. TUIRoomKit передает список выбранных пользователей вашим контактам:

Вы можете получить список пользователей, выбранных для конференции, следующим методом.

java

kotlin

```
// Получите список выбранных пользователейConferenceParticipants participants = (ConferenceParticipants) bundle.getSerializable(CONFERENCE_PARTICIPANTS);ArrayList<User> selectedList = participants.selectedList;
```

```
// Получите список выбранных пользователейval participants = bundle.getSerializable(CONFERENCE_PARTICIPANTS) as ConferenceParticipantsval selectedList: ArrayList<User> = participants.selectedList
```

Вы можете достичь удовлетворительного пользовательского интерфейса, изменив исходный код в каталоге [iOS/TUIRoomKit/Source](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/iOS/TUIRoomKit/Source). Чтобы облегчить вам настройку пользовательского интерфейса, вот введение в файлы, связанные с паролем комнаты.

```
Source    âââ ConferenceListView.swift                  // Список конференцийâââ ScheduleConferenceViewController.swift    // Интерфейс планирования конференцииâââ View    âââ ConferenceOptions     Â Â  âââ ConferenceInvitation              // Приглашение на конференцию     Â Â  âââ MemberSelect                      // Приглашение участников     Â Â  âââ ModifySchedule                    // Изменение конференции     Â Â  âââ ScheduleConference             âââ View                âââ ScheduleConference        // Планирование конференции                 âââ ScheduleDetails           // Детали планирования конференции                âââ Widget                    // Виджет всплывающего окна конференции
```

Вы можете изменить исходный код в каталоге [tencent_conference_uikit/lib/pages](https://github.com/Tencent-RTC/TUIRoomKit/tree/main/Flutter/tencent_conference_uikit/lib/pages) для достижения желаемого результата пользовательского интерфейса. Чтобы облегчить настройку пользовательского интерфейса, вот введение в файлы для запланированной конференции.

```
pages      âââ conferenceList                            // Папка для списка запланированных конференций  |       âââ view.dart                         // Страница списка запланированных конференций  |       âââ widget.dart                           |             âââ conference_date_item.dart   // Виджет одной даты в списке конференций  |             âââ conference_item.dart        // Виджет одной конференции в списке конференций  |             âââ no_schedule_widget.dart     // Виджет, отображаемый при отсутствии конференций в списке конференций  âââ schedule_conference                       // Папка для страницы запланированной конференции  â       âââ view.dart                         // Страница запланированной конференции  â       âââ widgets  â             âââ attendee_selector           // Папка для страницы выбора участников  â             â      âââ view.dart            // Страница выбора участников  â             â      âââ widgets  â             â             âââ selected_attendees.dart  // Всплывающая страница выбранных участников  â             âââ duration_selector.dart      // Виджет для выбора длительности конференции  â             âââ room_control.dart           // Виджет для отключения/включения микрофона для всех участников или отключения/включения видео во время конференции  â             âââ room_info.dart              // Виджет для общей информации о комнате запланированной конференции  â             âââ room_type.dart              // Виджет для выбора типа комнаты  â             âââ start_time_selector.dart    // Виджет для выбора времени начала конференции  â             âââ time_zone_selector.dart     // Страница для выбора часового пояса конференции  âââ schedule_details                          // Папка для деталей конференции  â       âââ view.dart                         // Страница с деталями конференции   â       âââ widgets  â           âââ details_button_item.dart      // Виджет одной кнопки на странице деталей конференции  âââ         âââ room_info.dart                // Виджет информации о встрече
```

> **Примечание:**Если у вас есть какие-либо предложения или отзывы, свяжитесь с нами по адресу info_rtc@tencent.com.

## Ключевой код

Если вы хотите реализовать функцию планирования конференции с нуля, пожалуйста, обратитесь к TUIConferenceListManager: [Android](https://www.tencentcloud.com/document/product/647/64482#d5eaa3d13b4939e42a645d2c10016fcc), [iOS&Mac](https://www.tencentcloud.com/document/product/647/64476).


---
*Источник: [https://trtc.io/document/63139](https://trtc.io/document/63139)*

---
*Источник (EN): [conference-scheduling.md](./conference-scheduling.md)*
