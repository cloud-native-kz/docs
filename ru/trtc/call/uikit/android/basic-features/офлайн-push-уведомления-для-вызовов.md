# Офлайн push-уведомления для вызовов

Плагин TIMPush — это мощная платная функция, которая обеспечивает механизмы VoIP-уведомлений для платформы Google. В сочетании с возможностями обмена данными `Firebase Cloud Messaging (FCM)` и компонентом `TUICallKit` он предоставляет интерфейс отображения входящего вызова с настраиваемой разметкой.

> **Примечание:** Телефоны с Google Mobile Services. Функция FCM для передачи данных доступна только в TIMPush **7.9.5668** и более поздних версиях. Поддержка TUICallKit ограничена версией **2.3** и выше.

В этой статье подробно описано, как интегрировать плагин TIMPush в компонент TUICallKit, использовать сообщения данных FCM и достичь отображения баннеров для входящих аудио- и видеовызовов.

## Результат интеграции

TUICallKit успешно интегрировал сообщения данных FCM в примере проекта на GitHub. Вы можете быстро реализовать нормальную работу функции, обратившись к [примеру проекта Call UIKit](https://github.com/tencentyun/TUICallKit/tree/main/Android). На следующей диаграмме показаны представления входящего вызова после получения приглашения на вызов, когда **приложение находится на переднем плане, в фоне** или когда **процесс приложения не существует**.

| Представление отображения, когда **приложение находится на переднем плане** | Представление отображения, когда **приложение находится в фоне** или **отключено** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7403235ffd3911eea33752540095b445.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74164c7afd3911ee82c9525400275b90.png) |

> **Примечание:** Для достижения хорошего качества вызовов, как показано выше, рекомендуется включить разрешения "уведомления", "отображение поверх других приложений" и "фоновые всплывающие окна" в вашем приложении. Дополнительные сведения см. в разделе: [Включение соответствующих разрешений](https://www.tencentcloud.com/document/product/647/50999#4f15e437-fb41-4a95-8f7c-5c8473ad063b).

## Требования к подготовке

1. Зарегистрируйте ваше приложение на [платформе FCM Push](https://console.firebase.google.com/), чтобы получить параметры, такие как **AppID** и **AppKey**, а также файл `google-services.json`.
2. Войдите в [консоль чатов мгновенных сообщений](https://console.intl.cloud.tencent.com/im), перейдите в **управление push-уведомлениями** > **параметры доступа**, выберите FCM, добавьте сертификат FCM и выберите **прозрачную передачу (данные) сообщения**.

| Платформа FCM | Конфигурация в консоли чата |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0d855493fd4f11eeb7f5525400a7e516.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3c0a7789fd4f11eeb7f5525400a7e516.png) |

## Быстрая интеграция

#### 1. Загрузка и добавление файла конфигурации

После завершения информации о push в консоли загрузите файл `timpush-configs.json` и добавьте его в каталог `assets` модуля приложения, а также добавьте `google-services.json` в каталог приложения проекта.

| Загрузка файла timpush-configs.json | Загрузка файла google-services.json | Добавить в проект |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5b20fa55fd5011eea33752540095b445.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9c9acee8fd5011eea33752540095b445.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7409e016fd3911ee82c9525400275b90.png) |

#### 2. Интеграция плагина TIMPush

В файле `app/build.gradle` добавьте следующую зависимость.

```
implementation "com.tencent.timpush:timpush:latest.release"implementation "com.tencent.timpush:fcm:latest.release"
```

> **Примечание:** TIMPush требует интеграции с Chat SDK версии **7.9.5668** и выше. Вы можете изменить версию Chat SDK в файле `tuicallkit-kt/build.gradle`.

#### 3. Завершение конфигурации проекта

- В файле `build.gradle` на уровне проекта в разделе `buildscript -> dependencies` добавьте следующую конфигурацию.

```
buildscript {    dependencies {        classpath 'com.google.gms:google-services:4.3.15'    }}
```

- В файле `app/build.gradle` добавьте следующую конфигурацию.

```
apply plugin: 'com.google.gms.google-services'
```

- В файле `app/proguard-rules.pro` добавьте классы TIMPush в список исключений из обфускации.

```
-keep class com.tencent.qcloud.** { *; }-keep class com.tencent.timpush.** { *; }
```

- В файле `app/build.gradle` измените имя пакета приложения на ваше фактическое имя пакета приложения.

```
applicationId 'com.****.callkit'
```

#### 4. Завершение автоматического входа

В вашем классе `application` слушайте события TIMPush и реализуйте метод автоматического входа самостоятельно.

Kotlin

Java

```
import com.tencent.qcloud.tuicore.TUIConstants
import com.tencent.qcloud.tuicore.TUICore
import com.tencent.qcloud.tuicore.interfaces.ITUINotification

class BaseApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        TUICore.registerEvent(TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_KEY,
            TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_SUB_KEY) { key, subKey, param ->
            if (TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_KEY == key                 && TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_SUB_KEY == subKey) {
                //you need to login again to launch call activity, please implement this method by yourself
                autoLogin()
            }
        }
    }
}
```

```
import com.tencent.qcloud.tuicore.TUIConstants;
import com.tencent.qcloud.tuicore.TUICore;
import com.tencent.qcloud.tuicore.interfaces.ITUINotification;public class BaseApplication extends Application {    @Override    public void onCreate() {        super.onCreate();        TUICore.registerEvent(TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_KEY,                TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_SUB_KEY, new ITUINotification() {                    @Override                    public void onNotifyEvent(String key, String subKey, Map<String, Object> param) {                        if (TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_KEY.equals(key)                                && TUIConstants.TIMPush.EVENT_IM_LOGIN_AFTER_APP_WAKEUP_SUB_KEY.equals(subKey)) {                            //you need to login again to launch call activity, please implement this method by yourself                            autoLogin();                        }                    }                });    }}
```

После завершения вышеуказанных шагов вы сможете использовать возможность офлайн push-уведомлений в TUICallKit.

> **Примечание:** Если ваше приложение Android испытывает проблемы при получении push-уведомлений или открытии страниц, вы можете обратиться к [политике отображения вызовов вызываемой стороной](https://trtc.io/document/51022?platform=android&product=call&menulabel=android#bfe2ed33-0611-4ca2-9aa8-f75b2a443e4a) для устранения неполадок.

## Расширенные функции

#### Пользовательский звук вызова

Если вы хотите настроить звук вызова, вы можете заменить файл `tuicallkit-kt/src/main/res/raw/phone_ringing.mp3`.

> **Примечание:** После замены звука вызова, независимо от того, находится ли приложение на переднем плане, в фоне или отключено, звук будет заменённым. После замены звук вызова, полученный другими телефонами производителей при приглашении, также будет заменённым.

## Часто задаваемые вопросы

#### **1. Невозможно открыть интерфейс входящего вызова после закрытия приложения**

- Подтвердите получение push-уведомления. Если push-уведомление не может быть получено, см. шаг 1 в приведённом выше документе **Быстрая интеграция**, чтобы проверить, были ли сертификаты правильно добавлены в консоль чата.
- Убедитесь, что в консоли выбрана **прозрачная передача (данные) сообщения** FCM, в соответствии со вторым шагом приведённых выше **требований к подготовке**.
- Подтвердите получение сообщений данных, отфильтруйте журналы (ключевое слово: TIMPush) и проверьте следующие журналы на печать (если сообщения не получены).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/73fce76afd3911eea33752540095b445.png)

- Подтвердите реализацию **автоматического входа**. Только после **автоматического входа** запросы вызова получаются и отображается интерфейс входящего вызова.

#### 2. **Включение соответствующих разрешений**

Для обеспечения качественного опыта вызовов рекомендуется включить разрешения "уведомления", "отображение поверх других приложений (плавающее окно)" и "фоновые всплывающие окна" в вашем приложении. Конкретные методы приведены ниже:

Руководство по коду

Включение вручную

- **Разрешения уведомлений**: Для отображения push-уведомлений см. [Разрешения уведомлений во время выполнения](https://developer.android.com/develop/ui/views/notifications/notification-permission) и [Запрос разрешений во время выполнения](https://developer.android.com/training/permissions/requesting#request-permission) и реализуйте в соответствии с потребностями вашего приложения.
- **Разрешение плавающего окна**: Используется для отображения пользовательских уведомлений входящего вызова и плавающих окон вызовов.
- **Фоновые всплывающие окна:** Используется для открытия интерфейса, когда приложение находится в фоне (например, на телефоне VIVO).

```
fun requestPermission(context: Context?) {    //In TUICallKit,Please open both OverlayWindows and Background pop-ups permission.    PermissionRequester.newInstance(         PermissionRequester.FLOAT_PERMISSION, PermissionRequester.BG_START_PERMISSION)        .request()}
```

После установки приложения вы можете долго нажать на значок приложения, выбрать "Информация приложения", а затем включить разрешения "уведомления", "отображение поверх других приложений" и "фоновые всплывающие окна". Кроме того, вы можете перейти в `мобильный телефон > параметры системы > управление приложениями > приложение` и вручную включить эти разрешения.

| Pixel 4a | VIVO |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d980d6cfd6c11ee9f79525400a7e516.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d9623dafd6c11ee848952540095b445.png) |

## Предложения и обратная связь

Если у вас есть какие-либо предложения или замечания, пожалуйста, свяжитесь с `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/50999](https://trtc.io/document/50999)*

---
*Источник (EN): [offline-call-push.md](офлайн-push-уведомления-для-вызовов.md)*
