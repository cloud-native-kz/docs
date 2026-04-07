# Внутриконференционный звонок

## Описание функции

Conference (TUIRoomKit) поддерживает функцию внутриконференционного звонка. Пользователи могут звонить другим пользователям и приглашать их присоединиться к текущей конференции в любой момент без предварительного бронирования или планирования. Функция внутриконференционного звонка позволяет пользователям гибко приглашать или напоминать соответствующему персоналу участвовать во внутриконференционном звонке, повышая интерактивность и эффективность. В этой статье приводится подробное введение в эту функцию и объяснение того, как ее использовать в компоненте TUIRoomKit.

| Звонящий | Получатель звонка |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7b0fda7d797b11ef80ff525400d5f8ef.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8f5b5487797b11ef80ff525400d5f8ef.png) |

## Инструкции по использованию

### Звонок пользователям

Когда вы находитесь в конференции, вы можете позвонить пользователям, которые еще не присоединились к комнате, двумя способами:

#### Способ 1: Звонок пользователям из списка участников, которые не присоединились

В списке участников комнаты вы увидите строку заголовка **Не присоединился**. Щелкнув на **Не присоединился**, будут отображены все участники, которые в настоящее время не присоединились к конференции, и вы можете позвонить этим участникам, которые еще не присоединились.

Список пользователей, которые не присоединились, включает два типа:

- Участники, приглашенные во время планирования конференции, но не присоединившиеся
- Участники, которым звонили, но которые по-прежнему не присоединились к конференции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/07244792797c11efa87e52540055f650.png)

#### Способ 2: Звонок пользователям из списка контактов

Щелкнув на **Пригласить** в нижней панели > **Добавить участников**, вы можете открыть интерфейс своего списка контактов и позвонить выбранным участникам из него.

Если вам нужно использовать эту функцию, вам необходимо импортировать ваш собственный реализованный интерфейс списка контактов на основе ваших потребностей следующим образом:

Android

iOS

##### **Как использовать функцию звонка участникам из списка контактов**

Сначала обратитесь к [Запуск примера кода](https://www.tencentcloud.com/document/product/647/60443#), чтобы завершить запуск демонстрации. В файле [members.json](https://github.com/Tencent-RTC/TUIRoomKit/pull/529/files#diff-2855a12fa1c035713f68a111990f2fe1e15e00d395934bbca1daea6ffb0fb4c4) проекта демонстрации мы предварительно настроили некоторую информацию тестового пользователя. Вы можете выбрать два аккаунта, войти на два телефона соответственно, используя настроенный userId, а затем в конференции щелкните **Пригласить** в нижней панели > **Добавить участников**, чтобы открыть список контактов. Выберите другого пользователя из списка контактов и нажмите Подтвердить, чтобы сделать звонок. Таким образом, другой пользователь получит ваш звонок.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/14a21b70797911efa87e52540055f650.png)

##### Как использовать пользовательский список контактов

1. **Связывание TUIRoomKit с пользовательским списком контактов:** Перед звонком пользователям из списка контактов вам необходимо настроить пользовательский список контактов следующими методами:

java

kotlin

```
// Замените SelectParticipantActivity.class на класс пользовательского действия списка контактовConferenceSession.sharedInstance().setContactsViewProvider(SelectParticipantActivity.class);
```

```
// Замените SelectParticipantActivity.class на класс пользовательского действия списка контактовConferenceSession.sharedInstance().setContactsViewProvider(SelectParticipantActivity::class.java)
```

> **Примечание:** `SelectParticipantActivity` — это пример кода для пользовательского списка контактов. Вы можете посмотреть его в проекте Demo (каталог: app/src/main/java/com/tencent/liteav/demo/SelectParticipants).

2. **Возврат выбранного списка пользователей из пользовательского списка контактов в TUIRoomKit:** После завершения выбора пользователя в списке контактов вам необходимо вернуть выбранный список пользователей в TUIRoomKit. Вы можете вернуть данные в TUIRoomKit, используя следующий метод.

java

kotlin

```
Intent intent = new Intent();// participants — это список выбранных пользователей, должен быть типа ArrayList<User>.ConferenceParticipants participants = new ConferenceParticipants();// Добавьте ваших участников...
intent.putExtra(SELECTED_PARTICIPANTS, participants);setResult(3, intent);finish();
```

```
val intent = Intent()// participants — это список выбранных пользователей, должен быть типа ArrayList<User>.intent.putExtra(SELECTED_PARTICIPANTS, participants)setResult(3, intent)finish()
```

##### Как использовать функцию звонка участникам из списка контактов

Сначала обратитесь к [Запуск примера кода](https://www.tencentcloud.com/document/product/647/60442#), чтобы завершить запуск демонстрации. В файле `members.json` проекта демонстрации мы предварительно настроили некоторую информацию тестового пользователя. Вы можете выбрать два аккаунта, войти на два телефона соответственно, используя настроенный userId, а затем в конференции щелкните **Пригласить** в нижней панели > **Добавить участников**, чтобы открыть список контактов. Выберите другого пользователя из списка контактов и нажмите Подтвердить, чтобы сделать звонок. Таким образом, другой пользователь получит ваш звонок.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/14bdc903797911ef8829525400fdb830.png)

##### Как использовать пользовательский список контактов

Учитывая сложность данных списка пользователей на странице приглашения участников, мы разработали решение, которое позволяет вам настроить интерфейс выбора участников. Далее мы проведем вас через процесс интеграции вашей собственной страницы выбора участников (конечно, вы также можете напрямую использовать пользовательский интерфейс, который мы предоставляем в демонстрации, что будет представлено позже).

1. Подготовьте ваш viewController страницы выбора друзей и реализуйте протокол `ContactViewProtocol`.

```
// Пример кодаclass SelectMemberViewController: UIViewController, ContactViewProtocol {    weak var delegate: ContactViewSelectDelegate?    var selectedList: [User]        func didSelectFinished() {      // Через делегат вызовите обратно выбранных участников в RoomKit в методе, где происходит выбор         delegate?.onMemberSelected(self, invitees: selectedMembers)    }}
```

> **Примечание:** Рекомендуется разместить объект `ConferenceParticipants` в параметрах конструктора вашей страницы адресной книги с источниками данных, упомянутыми в коде второго шага. Класс `ConferenceParticipants` имеет двух участников: selectedList: выбранные участники; unSelectableList: несоздаваемые участники. Вы можете установить конкретных участников как несоздаваемых в пользовательском интерфейсе. Во время конференционного звонка несоздаваемые участники — это те, которые уже находятся в конференции.

2. Перед звонком пользователям в списке контактов **перед**, вам необходимо передать ваш пользовательский список контактов в TUIRoomKit, используя следующий метод:

```
ConferenceSession.sharedInstance.setContactsViewProvider { participants in            return SelectMemberViewController(participants: participants)}
```

3. После выполнения вышеуказанных двух шагов вы можете отобразить вашу собственную страницу списка контактов. Мы также предоставляем код страницы списка контактов в демонстрации, как показано на изображении выше. Вы можете напрямую скопировать эти файлы в ваш проект, чтобы получить нашу страницу примера.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/14c49a86797911ef82535254002693fd.png)

В классе `SelectMembersViewModel` вы можете загрузить данные списка участников (или напрямую получить данные цепочки отношений Chat), используя метод `loadMembers`.

### Был получен звонок

Когда вы получаете звонок в приложении, появляется страница, аналогичная показанной ниже. Вы можете перетащить ползунок, чтобы выбрать **Присоединиться сейчас**, или щелкните **Не входить сейчас**, чтобы отклонить звонок.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1d5561b5797c11ef82535254002693fd.png)

> **Примечание:** Когда пользователь находится либо **на конференции**, либо **получает звонок**, он автоматически отклонит все входящие звонки

## Настройка функции

Если текущий пользовательский интерфейс не соответствует вашим потребностям, вы можете достичь желаемых эффектов пользовательского интерфейса, изменив исходный код. Чтобы облегчить настройку пользовательского интерфейса, здесь представлены файлы, связанные с функцией внутриконференционного звонка.

### Настройка представления страницы полученного звонка

Если вам нужно настраиваемое представление для страницы полученного звонка, обратитесь к следующему пути для внесения изменений.

Android

iOS

```
// Расположение файла: Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/component/component    âââInvitationReceivedView.java
```

```
// Расположение файла: iOS/TUIRoomKit/Source/View/ConferenceOptions/ConferenceInvitationConferenceInvitation    âââ ConferenceInvitationViewController.swift  // Представление страницы полученного звонка
```

### Настройка представления звонка в списке участников

Если вам нужно настраиваемое представление звонка в списке участников, обратитесь к следующему пути для внесения изменений.

Android

iOS

```
// Расположение файла: Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/view/page/widget/UserControlPanel/UserControlPanel    âââ CallUserView.java // Кнопка звонка в списке участников
```

```
// Расположение файла: iOS/TUIRoomKit/Source/Page/Widget/UserControlPanelUserControlPanel            // Каталог представлений, связанных со списком участников    âââ UserListCell.swift  // Представление отдельного участника в списке участников, включая статус звонка пользователя
```

## Ключевой код

### Звонок пользователям

Android

iOS

```
// Расположение файла: TUIRoomKit/blob/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/model/controller/InvitationController.javapublic void inviteUsers(List<UserState.UserInfo> userInfoList, TUIConferenceInvitationManager.InviteUsersCallback callback) {    Log.d(TAG, "inviteUsers");    if (userInfoList.isEmpty()) {        return;    }    RoomToast.toastShortMessageCenter(TUILogin.getAppContext().getString(R.string.tuiroomkit_invitation_has_been_sent));    mConferenceInvitationManager.inviteUsers(mRoomState.roomId.get(), getUserIdListFromUserList(userInfoList), INVITE_TIME_OUT_SECONDS, "", new TUIConferenceInvitationManager.InviteUsersCallback() {        @Override        public void onSuccess(Map<String, TUIConferenceInvitationManager.InvitationCode> invitationResultMap) {            Log.d(TAG, "inviteUsers success");            if (callback != null) {                callback.onSuccess(invitationResultMap);            }        }        @Override        public void onError(TUICommonDefine.Error error, String message) {            Log.d(TAG, "inviteUsers error=" + error + " message=" + message);            if (callback != null) {                callback.onError(error, message);            }        }    });}
```

```
// Расположение файла: TUIRoomKit/iOS/TUIRoomKit/Source/Service/ConferenceInvitationService.swiftfunc inviteUsers(roomId: String, userIdList: [String]) -> AnyPublisher<InviteUsersResult, RoomError> {    return Future<InviteUsersResult, RoomError> { [weak self] promise in        guard let self = self else { return }        self.invitationManager?.inviteUsers(roomId, userIdList: userIdList, timeout: timeout, extensionInfo: "") {dic in            promise(.success((dic)))        } onError: { error, message in            promise(.failure(RoomError(error: error, message: message)))        }    }    .eraseToAnyPublisher()}
```

### Принятие звонка

Android

iOS

```
// Расположение файла: TUIRoomKit/blob/main/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/model/controller/InvitationController.java    public void accept(String roomId, TUIRoomDefine.ActionCallback callback) {    Log.d(TAG, "accept");    mConferenceInvitationManager.accept(roomId, new TUIRoomDefine.ActionCallback() {        @Override        public void onSuccess() {            Log.d(TAG, "accept success");            if (callback != null) {                callback.onSuccess();            }        }        @Override        public void onError(TUICommonDefine.Error error, String message) {            Log.d(TAG, "accept error=" + error + " message=" + message);            if (callback != null) {                callback.onError(error, message);            }        }    });}
```

```
// Расположение файла: TUIRoomKit/iOS/TUIRoomKit/Source/Service/ConferenceInvitationService.swiftfunc accept(roomId: String) -> AnyPublisher<String, RoomError> {    return Future<String, RoomError> { [weak self] promise in        guard let self = self else { return }        self.invitationManager?.accept(roomId) {            promise(.success(roomId))        } onError: { error, message in            promise(.failure(RoomError(error: error, message: message)))        }    }    .eraseToAnyPublisher()}
```

### Отклонение звонка

Android

iOS

```
// Расположение файла: TUIRoomKit/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/model/controller/InvitationController.javapublic void reject(String roomId, TUIConferenceInvitationManager.RejectedReason reason, TUIRoomDefine.ActionCallback callback) {    Log.d(TAG, "reject roomId= " + roomId + " reason=" + reason);    mConferenceInvitationManager.reject(roomId, reason, new TUIRoomDefine.ActionCallback() {        @Override        public void onSuccess() {            Log.d(TAG, "reject success");            if (callback != null) {                callback.onSuccess();            }        }        @Override        public void onError(TUICommonDefine.Error error, String message) {            Log.d(TAG, "reject error=" + error + " message=" + message);            if (callback != null) {                callback.onError(error, message);            }        }    });}
```

```
// Расположение файла: TUIRoomKit/iOS/TUIRoomKit/Source/Service/ConferenceInvitationService.swiftfunc reject(roomId: String, reason: TUIInvitationRejectedReason) -> AnyPublisher<String, RoomError> {    return Future<String, RoomError> { [weak self] promise in        guard let self = self else { return }        self.invitationManager?.reject(roomId, reason: reason) {            promise(.success(roomId))        } onError: { error, message in            promise(.failure(RoomError(error: error, message: message)))        }    }    .eraseToAnyPublisher()}
```

### Получение списка звонков в комнате

Android

iOS

```
// Расположение файла: TUIRoomKit/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/model/controller/InvitationController.javaprivate void getInvitationList() {    Log.d(TAG, "getInvitationList");    mConferenceInvitationManager.getInvitationList(mRoomState.roomId.get(), getAttendeeListCursor, SINGLE_FETCH_COUNT, new TUIConferenceInvitationManager.GetInvitationListCallback() {        @Override        public void onSuccess(TUIConferenceInvitationManager.InvitationListResult invitationListResult) {            Log.d(TAG, "getInvitationList");            for (TUIConferenceInvitationManager.Invitation invitation : invitationListResult.invitationList) {                InvitationState.Invitation invitationState = new InvitationState.Invitation();                invitationState.invitee = new UserState.UserInfo(invitation.invitee);                invitationState.inviter = new UserState.UserInfo(invitation.inviter);                invitationState.invitationStatus = invitation.status;                mInvitationState.invitationList.add(invitationState);            }            getInvitationListCursor = invitationListResult.cursor;            if (!"".equals(getInvitationListCursor)) {                getInvitationList();            }        }        @Override        public void onError(TUICommonDefine.Error error, String message) {            Log.d(TAG, "getInvitationList onError error=" + error + " message=" + message);        }    });}
```

```
// Расположение файла: TUIRoomKit/iOS/TUIRoomKit/Source/Service/ConferenceInvitationService.swiftfunc getInvitationList(roomId: String, cursor: String, count: Int = 20) -> AnyPublisher<InvitationfetchResult, RoomError> {    return Future<InvitationfetchResult, RoomError> { [weak self] promise in        guard let self = self else { return }        self.invitationManager?.getInvitationList(roomId, cursor: cursor, count: count) {invitations, cursor in            promise(.success((invitations, cursor)))        } onError: { error, message in            promise(.failure(RoomError(error: error, message: message)))        }    }    .eraseToAnyPublisher()}
```

### Слушатель получения звонка пользователем

Android

iOS

```
// Расположение файла: TUIRoomKit/Android/tuiroomkit/src/main/java/com/tencent/cloud/tuikit/roomkit/model/ConferenceServiceInitializer.javaprivate void initConferenceInvitationObserver() {    TUIConferenceInvitationManager invitationManager = (TUIConferenceInvitationManager) TUIRoomEngine.sharedInstance().getExtension(TUICommonDefine.ExtensionType.CONFERENCE_INVITATION_MANAGER);    invitationManager.addObserver(new TUIConferenceInvitationManager.Observer() {        @Override        public void onReceiveInvitation(TUIRoomDefine.RoomInfo roomInfo, TUIConferenceInvitationManager.Invitation invitation, String extensionInfo) {            if (ConferenceController.sharedInstance().getViewState().isInvitationPending.get()) {                ConferenceController.sharedInstance().getInvitationController().reject(roomInfo.roomId, REJECT_TO_ENTER, null);                return;            }            if (ConferenceController.sharedInstance().getRoomController().isInRoom()) {                ConferenceController.sharedInstance().getInvitationController().reject(roomInfo.roomId, IN_OTHER_CONFERENCE, null);                return;            }            Bundle bundle = new Bundle();            bundle.putString("roomId", roomInfo.roomId);            bundle.putString("conferenceName", roomInfo.name);            bundle.putString("ownerName", roomInfo.ownerName);            bundle.putString("inviterName", invitation.inviter.userName);            bundle.putString("inviterAvatarUrl", roomInfo.ownerAvatarUrl);            bundle.putInt("memberCount", roomInfo.memberCount);            TUICore.startActivity("InvitationReceivedActivity", bundle);        }    });}
```

```
// Расположение файла: TUIRoomKit/iOS/TUIRoomKit/Source/Service/InvitationObserverService.swiftfunc onReceiveInvitation(roomInfo: TUIRoomInfo, invitation: TUIInvitation, extensionInfo: String) {    let store = Container.shared.conferenceStore()    store.dispatch(action: ConferenceInvitationActions.onReceiveInvitation(payload: (roomInfo, invitation)))}
```


---
*Источник: [https://trtc.io/document/64691](https://trtc.io/document/64691)*

---
*Источник (EN): [in-conference-call.md](./in-conference-call.md)*
