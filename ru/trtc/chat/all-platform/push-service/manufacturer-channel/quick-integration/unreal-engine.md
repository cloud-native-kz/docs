# Unreal Engine

### Этапы операции

### Этап 1: Интеграция TIMPush

Загрузите [TIMPush](https://github.com/TencentCloud/TIMSDK/tree/master/UE5/Push/pushdemo/Plugins/TIMPush) и скопируйте в директорию `Plugins` под проектом. В файле Build.cs основного модуля введите TIMPush.

| копировать директорию | Введение плагина |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35973802920011f0a14552540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35b10658920011f097255254005ef0f7.png) |

### Этап 2: Конфигурация параметров Push

iOS

Android

Загрузите полученный сертификат iOS APNs Push в консоль IM во время процесса конфигурации производителя.

Консоль IM выделит вам ID сертификата, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/56265220920011f090a8525400e889b2.png)

Установите businessID:

Откройте "Project Settings" в редакторе UE4, найдите `Additional Plist Data`, измените следующий текст и скопируйте его в текстовое поле. `YourBusinessID` требуется, а `YourGroupID` необходимо изменить, когда вам нужно подсчитать данные охвата и клика push.

```
<key>businessID</key><string>YourBusinessID</string><key>TIMPushAppGroupID</key><string>YourGroupID</string>
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/359506c8920011f0bdaa525400bf7822.png)

Включите возможность удалённого push:

После завершения конфигурации ID сертификата необходимо включить возможность Push Notifications приложения:

- Если ваш движок UE собран из исходного кода вручную, вы можете включить соответствующую возможность, отметив "Enable Remote Notifications Support" в Project Settings > iOS.
- Если ваш движок UE загружен из Epic Games, вы можете открыть "`<proj_dir>/Config/DefaultEngine.ini`" и добавить следующее под `IOSRuntimeSettings` в скрипт:

```
// Some code[/Script/IOSRuntimeSettings.IOSRuntimeSettings]bEnableRemoteNotificationsSupport=True
```

- Кроме того, вы также можете открыть созданный UE файл YourProject.xcworkspace с помощью Xcode в корневой директории проекта. В разделе Project > Target нажмите опцию Signing & Capabilities, выберите Capability в левом верхнем углу и найдите, чтобы добавить возможность Push Notifications в ваш проект.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/364bb072920011f087025254001c06ec.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35d75229920011f0aa79525400454e06.png)

После завершения конфигурации информации производителя консоли загрузите и добавьте файл конфигурации в проект. Поместите загруженный файл `timpush-configs.json` в директорию `Source/ThirdParty/TIMPushLibrary/Android/TIMPush/Assets`.

| загрузить файл конфигурации | путь копирования |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/88117792920011f08e0452540044a08e.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35f54d32920011f090a8525400e889b2.png) |

### Этап 3: Конфигурация производителя на клиенте

iOS

Android

На iOS нет необходимости выполнять этот этап.

Детали конфигурации APL настроены, нужно только заменить на собственные сообщения конфигурации. Путь к TIMPush_APL.xml: /Plugins/TIMPush/Source/TIMPush/

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35c75556920011f087025254001c06ec.png)

#### Конфигурация интеграции пакета Push

```
 <buildGradleAdditions>    <insert>      dependencies {        // Version number "VERSION", please visit update log to get configuration.        // Push main package requires integration        implementation 'com.tencent.timpush:tpush:VERSION'              // Integrate corresponding manufacturers as needed        implementation 'com.tencent.timpush:huawei:VERSION'        implementation 'com.tencent.timpush:xiaomi:VERSION'        implementation 'com.tencent.timpush:oppo:VERSION'        implementation 'com.tencent.timpush:vivo:VERSION'        implementation 'com.tencent.timpush:honor:VERSION'        implementation 'com.tencent.timpush:meizu:VERSION'        implementation 'com.tencent.timpush:fcm:VERSION'       }    </insert>  </buildGradleAdditions>
```

#### Адаптация Vivo и Honor (внимание требуется только для интеграции производителя)

Согласно руководству по доступу производителей vivo и Honor, вам необходимо добавить APPID и APPKEY в файл конфигурации, в противном случае могут возникнуть проблемы компиляции.

```
<buildGradleAdditions>    <insert>      android {        defaultConfig {                             manifestPlaceholders = [                              "VIVO_APPKEY" : "xxxxxx",    // VIVO AppKey                          "VIVO_APPID" : "xxxxxx",     // VIVO AppId              "HONOR_APPID" : "xxxxxx"     // Honor AppId          ]            }      }    </insert>  </buildGradleAdditions>
```

#### 3. **Адаптация Huawei, Honor и Google FCM**

Интегрируйте соответствующий плагин и файл конфигурации json, используя метод производителя.

> **Примечание:** Примечание: следующая адаптация Honor требует конфигурации для версии 7.7.5283 и выше.

3.1 Загрузите файл конфигурации json и добавьте его в директорию плагина TIMPush `Source/ThirdParty/TIMPushLibrary/Android/TIMPush/`.

Huawei

Honor

Google FCM

Путь назначения

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35ca6045920011f08e0452540044a08e.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/36525597920011f090a8525400e889b2.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9b28d260920011f08e0452540044a08e.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/36395776920011f0bdaa525400bf7822.png)

3.2 Конфигурация плагина настроена и может масштабироваться или адаптироваться по версиям по мере необходимости.

```
<baseBuildGradleAdditions>    <insert>      allprojects {        repositories {            mavenCentral()            maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }            maven { url "https://mirrors.tencent.com/repository/maven/liteavsdk/" }            maven { url 'https://developer.huawei.com/repo/' }            maven { url 'https://mirrors.tencent.com/repository/maven/SensitiveScan' }            maven { url 'https://developer.hihonor.com/repo' }        }      }  </insert>  </baseBuildGradleAdditions>  <buildscriptGradleAdditions>    <insert>      repositories {          mavenCentral()          maven { url "https://mirrors.tencent.com/nexus/repository/maven-public/" }          maven { url "https://mirrors.tencent.com/repository/maven/liteavsdk/" }          maven { url 'https://developer.huawei.com/repo/' }          maven { url 'https://mirrors.tencent.com/repository/maven/SensitiveScan' }          maven { url 'https://developer.hihonor.com/repo' }      }      dependencies {        classpath 'com.google.gms:google-services:4.4.3' // FCM Plugin        classpath 'com.huawei.agconnect:agcp:1.9.1.300'  // Huawei Plugin        classpath 'com.hihonor.mcs:asplugin:2.0.1.300'   // Honor Plugin            }    </insert>  </buildscriptGradleAdditions>  <buildGradleAdditions>    <insert>      apply plugin: 'com.google.gms.google-services'  // FCM Plugin      apply plugin: 'com.huawei.agconnect'            // Huawei Plugin      apply plugin: 'com.hihonor.mcs.asplugin'        // Honor Plugin    </insert>  </buildGradleAdditions>
```

### Этап 4: Обработка обратного вызова клика сообщения и парсинг параметров

Если вам необходим пользовательский парсинг для полученного удалённого push, вы можете реализовать это следующим методом.

> **Примечание:** Рекомендуется поместить время регистрации обратного вызова в функцию входа программы. Сконфигурируйте консоль и выполняющие действия с помощью следующей конфигурации. Выберите **открыть указанную страницу в приложении**. Не изменяйте и используйте значения по умолчанию. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ded3a9a4920011f0a14552540099c741.png)

```
class DemoPushListener: public PushListener {public:    using OnRecvPushMessageCallback = std::function<void(const PushMessage &)>;    using OnRevokePushMessageCallback = std::function<void(const FString &)>;    using OnNotificationClickedCallback = std::function<void(const FString &)>;        void SetCallback(OnRecvPushMessageCallback recv_cb, OnRevokePushMessageCallback revoke_cb, OnNotificationClickedCallback clicked_cb) {        on_recv_message_callback_ = std::move(recv_cb);        on_revoke_message_callback_ = std::move(revoke_cb);        on_notification_clicked_callback_ = std::move(clicked_cb);    }        void OnRecvPushMessage(const PushMessage& message) override {        if (on_recv_message_callback_) {            on_recv_message_callback_(message);        }    }        void OnRevokePushMessage(const FString& messageID) override {        if (on_revoke_message_callback_) {            on_revoke_message_callback_(messageID);        }    }    void OnNotificationClicked(const FString& ext) override {        if (on_notification_clicked_callback_) {            on_notification_clicked_callback_(ext);        }    }    private:    OnRecvPushMessageCallback on_recv_message_callback_;    OnRevokePushMessageCallback on_revoke_message_callback_;    OnNotificationClickedCallback on_notification_clicked_callback_;};auto listener = new DemoPushListener();listener.SetCallback(    [](const PushMessage& message) {        UE_LOG(LogTemp, Warning, TEXT("Push Called in OnRecvPushMessage. Message title: %s, desc: %s, ext: %s, id: %s"), *message.GetTitle(), *message.GetDesc(), *message.GetExt(), *message.GetMessageID());    },    [](const FString& messageID) {        UE_LOG(LogTemp, Warning, TEXT("Push Called in OnRevokePushMessage. Message id: %s"), *messageID);    },    [](const FString& ext) {        UE_LOG(LogTemp, Warning, TEXT("Push Called in OnNotificationClicked. Message ext: %s"), *ext);    });PushManager::GetInstance()->AddPushListener(&DEMO_PUSH_LISTENER);
```

### Этап 6: Регистрация плагина Push

Вызовите API для push после успешной регистрации. Вы можете получать уведомления об автономном push.

```
template <class T>class DemoPushValueCallback : public PushValueCallback<T> {public:    using SuccessCallback = std::function<void(const T &)>;    using ErrorCallback = std::function<void(int, const FString &)>;        DemoPushValueCallback<T>() = default;    ~DemoPushValueCallback() override = default;        void SetCallback(SuccessCallback success_cb, ErrorCallback error_cb) {        success_callback_ = std::move(success_cb);        error_callback_ = std::move(error_cb);    }        void OnSuccess(const T &value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const FString &error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }    private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};auto callback = new DemoPushValueCallback<FString>();callback->SetCallback(    [=](const FString &value) {      UE_LOG(LogTemp, Warning, TEXT("Push succeed, device token is %s"), *value);      delete callback;    },    [=](int error_code, const FString &error_message) {      UE_LOG(LogTemp, Warning, TEXT("Push failed erro code: %d, desc: %s"), error_code, *error_message);      delete callback;    });PushManager::GetInstance()->RegisterPush(your sdkAppId, "your appKey", callback);
```

### Этап 7: Статистика доставки сообщений Push

Если вам требуется статистика данных охвата, завершите конфигурацию следующим образом:

Huawei

Honor

vivo

Meizu

iOS

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/35fc301d920011f0aa79525400454e06.png)

Адрес получения:

Сингапур : https://apisgp.im.qcloud.com/v3/offline_push_report/huawei

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/huawei

США: https://apiusa.im.qcloud.com/v3/offline_push_report/huawei

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/huawei

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/huawei

Китай: https://api.im.qcloud.com/v3/offline_push_report/huawei

> **Примечание:** Примечание: ID сертификата Huawei Push <= 11344 использует Huawei Push v2 API. Охват и получение клика не поддерживаются. Пожалуйста, переизданите и обновите ID сертификата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/36969b34920011f08e0452540044a08e.png)

Адрес получения:

Сингапур : https://apisgp.im.qcloud.com/v3/offline_push_report/honor

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/honor

США: https://apiusa.im.qcloud.com/v3/offline_push_report/honor

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/honor

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/honor

Китай: https://api.im.qcloud.com/v3/offline_push_report/honor

| Конфигурация адреса обратного вызова | Конфигурация ID получения в консоли IM |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/364b8068920011f089d25254007c27c5.png) Адрес получения: Сингапур: https://apisgp.im.qcloud.com/v3/offline_push_report/vivo Корея: https://apikr.im.qcloud.com/v3/offline_push_report/vivo США: https://apiusa.im.qcloud.com/v3/offline_push_report/vivo Германия: https://apiger.im.qcloud.com/v3/offline_push_report/vivo Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/vivo Китай: https://api.im.qcloud.com/v3/offline_push_report/vivo | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7cd8096920011f089d25254007c27c5.png) |

| Включение переключателя получения | Конфигурация адреса получения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d3ce364a920011f090a8525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/366033c9920011f0aa79525400454e06.png) |

Адрес получения:

Сингапур : https://apisgp.im.qcloud.com/v3/offline_push_report/meizu

Корея: https://apikr.im.qcloud.com/v3/offline_push_report/meizu

США: https://apiusa.im.qcloud.com/v3/offline_push_report/meizu

Германия: https://apiger.im.qcloud.com/v3/offline_push_report/meizu

Индонезия: https://apiidn.im.qcloud.com/v3/offline_push_report/meizu

Китай: https://api.im.qcloud.com/v3/offline_push_report/meizu

> **Примечание:** Примечание: после включения переключателя получения убедитесь, что адрес получения сконфигурирован правильно. Без конфигурации или с неправильным адресом это повлияет на функцию уведомлений push.

1. Если вам нужно отслеживать данные охвата и клика уведомлений push, вам нужно изменить "YourGroupID" на собственный ID группы приложения в ["параметрах проекта"](#b6edca76-1595-426f-b963-976e76e8ac56) ([см. конфигурация производителя - генерирование App GroupID](https://www.tencentcloud.com/document/product/1047/60548#ae5590eb-b974-4226-9f1b-720fb0201c85)).
2. После конфигурирования ID группы приложения вам нужно использовать Xcode для открытия файла xcworkspace, созданного UE в директории проекта, и ссылаться на метод в [Конфигурация производителя - Генерирование App Group ID - Этап 4](https://www.tencentcloud.com/document/product/1047/60548#ae5590eb-b974-4226-9f1b-720fb0201c85) для конфигурирования вашего ID группы приложения. Затем включите Notification Service Extension Target в `Editor - Add Target` в проекте Xcode.
3. Вам также нужно распаковать два сжатых пакета framework в пути `Plugins-TIMPush-Source-ThirdParty-TIMPushLibrary-iOS` корневой директории проекта и добавить внутреннюю папку .framework в свою цель pushservice в проекте Xcode.
4. Теперь вы можете вызвать функцию статистики скорости доставки push в методе `-didReceiveNotificationRequest:withContentHandler:` [Notification Service Extension](https://github.com/TencentCloud/TIMSDK/blob/master/iOS/Demo/pushservice/NotificationService.m):

```
@implementation NotificationService- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {    //appGroup indicates the shared APP Group between the main APP and Extension, and the App Groups capacity needs to be configured in the main APP's Capability.    //Format: group + [main bundleID] + key    //for example group.com.tencent.im.pushkey    NSString * appGroupID = kTIMPushAppGroupKey;    __weak typeof(self) weakSelf = self;    [TIMPushManager handleNotificationServiceRequest:request appGroupID:appGroupID callback:^(UNNotificationContent *content) {        weakSelf.bestAttemptContent = [content mutableCopy];        // Modify the notification content here...        // self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]", self.bestAttemptContent.title];        weakSelf.contentHandler(weakSelf.bestAttemptContent);    }];}@end
```

> **Примечание:** Отчёт о достижении данных push. Для поддержки функции Extension для iOS 10 необходимо включить переключатель mutable-content. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/79c492cd920011f08e0452540044a08e.png) Детали данных можно просмотреть на странице данных push. Страница данных push доступна только после [покупки плагина push](https://console.tencentcloud.com/im/plugin/TIMPush).

Другие производители поддерживаются без необходимости конфигурации. FCM в настоящее время не поддерживает функцию статистики уведомлений push.

Поздравляем с завершением интеграции плагина push. Напоминаем: плагин push **автоматически прекратит предоставление услуги push (включая стандартный offline push сообщений, push всем пользователям/тегам и т.д.) после истечения пробного периода или периода покупки**. Чтобы избежать влияния на нормальную работу бизнеса, пожалуйста, заранее [приобретите](https://buy.tencentcloud.com/avc?activeId=plugin&regionId=1)/[продлите](https://console.tencentcloud.com/account/renewal).

> **Примечание:** Offline каналы производителей имеют [механизм категоризации сообщений](https://www.tencentcloud.com/document/product/1047/60576), и различные типы также будут иметь различные стратегии push. Если потребность в push относится к push типу IM и требует своевременной доставки, установите своё приложение на соответствующий тип push в соответствии с правилами производителя. Оно будет категоризировано как тип системного сообщения с высоким приоритетом или тип важного сообщения. И наоборот, offline push имеет ограничения по количеству и частоте и может не достичь устройства вовремя. Интеграция завершена, но уведомления push не получены. Пожалуйста, сначала используйте [инструмент поиска и устранения неисправностей](https://www.tencentcloud.com/document/product/1047/60541) для проверки причины. Для просмотра данных метрик push используйте [статистику данных](https://www.tencentcloud.com/document/product/1047/60540) для запроса. Для функции уведомления push всем пользователям/тегам, пожалуйста, обратитесь к: [RESTful APIs - Инициировать Push всем пользователям/тегам](https://www.tencentcloud.com/document/product/1047/60561).


---
*Источник: [https://trtc.io/document/73892](https://trtc.io/document/73892)*

---
*Источник (EN): [unreal-engine.md](./unreal-engine.md)*
