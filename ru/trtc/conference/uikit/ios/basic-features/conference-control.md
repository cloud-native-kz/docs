# Управление конференцией

Этот документ предоставляет подробное введение в функции управления конференцией до её начала, во время конференции и другие аспекты `TUIRoomKit`, чтобы помочь вам лучше овладеть функциями управления конференцией в `TUIRoomKit`. Из этого документа вы узнаете, как полностью использовать возможности `TUIRoomKit` для организации высококачественных аудио и видеоконференций.

После создания и входа в комнату через платформы `Android&iOS&Flutter`, хост конференции или администратор могут получить доступ к параметрам управления участниками, нажав на кнопку членов на нижней панели инструментов. Это действие вызывает отображение списка участников в нижней части экрана. В этом списке хост или администратор могут выбрать любого обычного участника и применить действия, такие как **отключение микрофона пользователя** или **назначение администратором**, а также другие операции управления конференцией. Кроме того, хост или администратор могут выполнять действия управления на уровне всей конференции, такие как **отключение звука для всех участников** в комнате.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/265f34920c4311ef8d94525400f2c344.png)

## Управление до начала конференции

Перед входом в конференцию вы можете использовать функции управления до начала конференции в `TUIRoomKit`, чтобы предварительно установить соответствующие параметры конференции, обеспечивая её бесперебойное протекание.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/30fb0eb80c4311efb74e525400b3b5af.png)

iOS (Swift)

Android（Java）

Flutter (Dart)

```
// CreateRoomViewController for your own ViewControllerclass CreateConferenceViewController: UIViewController {    private var conferenceViewController: ConferenceMainViewController?    func quickStartConferenceAction() {      conferenceViewController = ConferenceMainViewController()      // Implement the pre-conference control features by setting the parameters in ConferenceParams.      let params = ConferenceParams()      params.isMuteMicrophone = false      params.isOpenCamera = false      params.isSoundOnSpeaker = true      params.name = "your conference name"      params.enableMicrophoneForAllUser = true      params.enableCameraForAllUser = true      params.enableMessageForAllUser = true      params.enableSeatControl = false      conferenceViewController?.setConferenceParams(params: params)      conferenceViewController?.setConferenceObserver(observer: self)      // After completing the settings, call the interface to start or join a conference. Here, we take starting a conference as an example.      conferenceViewController?.quickStartConference(conferenceId: "your conferenceId")    }}extension CreateConferenceViewController: ConferenceObserver {    func onConferenceStarted(conferenceId: String, error: ConferenceError) {      if error == .success, let vc = conferenceViewController {        navigationController?.pushViewController(vc, animated: true)      }      conferenceViewController = nil    }}
```

```
public class ConferenceOwnerActivity extends AppCompatActivity {    private static final String TAG = "ConferenceOwnerActivity";
    private ConferenceObserver mConferenceObserver;    @Override    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        setContentView(R.layout.app_activity_conference_main);
        // Implement the pre-conference control features by setting the parameters in ConferenceParams.        ConferenceParams params = new ConferenceParams();        params.setMuteMicrophone(false);        params.setOpenCamera(false);        params.setSoundOnSpeaker(true);
        params.setName("your conference name");        params.setEnableMicrophoneForAllUser(true);        params.setEnableCameraForAllUser(true);        params.setEnableMessageForAllUser(true);        params.setEnableSeatControl(false);        ConferenceMainFragment fragment = new ConferenceMainFragment();        fragment.setConferenceParams(params);        setConferenceObserver(fragment);        fragment.quickStartConference("your conferenceId");  // After completing the settings, call the interface to start or join a conference. Here, we take starting a conference as an example.    }

    private void setConferenceObserver(ConferenceMainFragment fragment) {        mConferenceObserver = new ConferenceObserver() {            @Override            public void onConferenceStarted(String conferenceId, ConferenceError error) {                super.onConferenceStarted(conferenceId, error);                if (error != ConferenceError.SUCCESS) {
                    Log.e(TAG, "Error : " + error);
                    return;
                }
                FragmentManager manager = getSupportFragmentManager();
                FragmentTransaction transaction = manager.beginTransaction();
                transaction.add(R.id.conference_owner_container, fragment);
                transaction.commitAllowingStateLoss();            }        };        fragment.setConferenceObserver(mConferenceObserver);    }}
```

```
var conferenceSession = ConferenceSession.newInstance("your conferenceId")        ..isMuteMicrophone = false      ..isOpenCamera = false      ..isSoundOnSpeaker = true      ..name = "your conference name"      ..enableMicrophoneForAllUser = true      ..enableCameraForAllUser = true      ..enableMessageForAllUser = true      ..enableSeatControl = false                ..onActionSuccess = () {    // Successful operation callback, you can navigate to the conference page here.        Navigator.push(          context,          MaterialPageRoute(          builder: (context) => ConferenceMainPage(),          ),        );      }                      ..onActionError = (ConferenceError error, String message) {}  // Failure operation callback      ..quickStart();         // After completing the settings, call the interface to start or join a conference. Here, we take starting a conference as an example.
```

Ниже приводится подробное введение в параметры в приведённом выше коде.

| Параметр | Тип | Значение |
| --- | --- | --- |
| isMuteMicrophone | bool | Отключен ли микрофон (по умолчанию false) |
| isOpenCamera | bool | Открыта ли камера (по умолчанию false) |
| isSoundOnSpeaker | bool | Включены ли динамики (по умолчанию true) |
| name | String | название конференции (по умолчанию ваше conferenceId) |
| enableMicrophoneForAllUser | bool | Включить ли разрешение микрофона для всех членов (по умолчанию true) |
| enableCameraForAllUser | bool | Включить ли разрешение камеры для всех членов (по умолчанию true) |
| enableMessageForAllUser | bool | Включить ли разрешение на отправку сообщений для всех членов (по умолчанию true) |
| enableSeatControl | bool | Включить ли режим выступления на сцене (по умолчанию false) |

> **Примечание:** Выше приводится введение в параметры для создания и присоединения к конференции в упомянутом выше коде. Вы можете создать либо комнату со свободным выступлением, либо комнату с выступлением на сцене на основе различных значений, передаваемых параметру isSeatEnable. Доступные функции управления в этих двух типах комнат будут также различаться: **Комната со свободным выступлением**: обычные пользователи могут свободно говорить и имеют право самостоятельно включать и выключать микрофоны и камеры. **Комната с выступлением на сцене**: только пользователи на сцене могут свободно включать и выключать микрофоны и камеры. Обычные зрители могут подать заявку на становление пользователями на сцене, подняв руку.

## Управление во время конференции

### Управление комнатой со свободным выступлением

Когда тип комнаты — комната со свободным выступлением, хост или администратор могут управлять всеми членами на встрече через **Участники** > Список участников.

- Хост или администратор могут выбрать любого участника для индивидуального управления: **отключение/включение микрофона**, **включение/отключение видео**, **назначение администратором**, **передача прав хоста**, **отключение/включение отправки сообщений** или **удаление из комнаты**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/be8d6a2a0c4511ef89045254000ded98.png)

- Хост или администратор могут выполнять групповые действия управления для всех членов в комнате: **отключение/включение звука для всех** или **отключение/включение видео для всех**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e85d99770c4511ef8d94525400f2c344.png)

### Управление комнатой с выступлением на сцене

Когда тип комнаты — комната с выступлением на сцене, хост или администратор могут управлять членами на встрече через **Участники** > Список участников, а также управлять статусом участников на сцене в разделе Управление сценой.

- Хост или администратор могут выбрать любого обычного участника для индивидуального управления: в дополнение к действиям, доступным в комнате со свободным выступлением, таким как **отключение/включение микрофона**, **включение/отключение видео**, **отключение/включение отправки сообщений**, **назначение администратором**, **передача прав хоста** и **удаление из комнаты**, комнаты с выступлением на сцене также предлагают уникальные действия, такие как **приглашение на сцену** и **просьба покинуть сцену**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4995001d0c4611ef9ef35254002977b6.png)

- Хост или администратор могут управлять статусом членов, которые подали заявку на выступление на сцене в комнате: в разделе **Управление сценой** они могут **одобрить или отклонить** выбранных членов или **одобрить всех членов**, которые подали заявку на выступление на сцене.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/836b54300ea111ef8c545254000781d8.png)


---
*Источник: [https://trtc.io/document/59974](https://trtc.io/document/59974)*

---
*Источник (EN): [conference-control.md](./conference-control.md)*
