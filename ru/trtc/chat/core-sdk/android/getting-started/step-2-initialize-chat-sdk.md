# Шаг 2: Инициализация Chat SDK

## Описание функции

Вы **должны** инициализировать SDK перед использованием его функций. В большинстве сценариев требуется инициализировать SDK только один раз в течение жизненного цикла приложения.

## Инициализация

Вы можете инициализировать SDK в следующих шагах:

1. Подготовьте `SDKAppID`.
2. Настройте объект `V2TIMSDKConfig`.
3. Добавьте слушатель событий SDK.
4. Вызовите `initSDK` для инициализации SDK.

Подробные шаги описаны ниже.

### Подготовка SDKAppID

`SDKAppID`

уникально идентифицирует аккаунт. Рекомендуется подать заявку на новый

`SDKAppID`

для каждого приложения. Сообщения естественным образом изолированы и не могут взаимодействовать между разными

`SDKAppID`

. Для выполнения инициализации необходимо иметь правильный

`SDKAppID`

.
В

Chat Console

вы можете просмотреть все ваши

`SDKAppID`

и нажать

**Create Application**

для создания

`SDKAppID`

.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5c3e5f2e1ce911efb25c5254003359ae.png)

### Настройка `V2TIMSDKConfig`

Перед инициализацией SDK необходимо инициализировать объект `V2TIMSDKConfig` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKConfig.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMSDKConfig.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMSDKConfig.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMSDKConfig.html)), который используется для начальной настройки SDK, такой как установка уровня логирования и обратного вызова слушателя логов.

#### Установка уровня логирования

SDK поддерживает следующие уровни логирования:

| Уровень логирования | Вывод логов |
| --- | --- |
| V2TIM_LOG_NONE | Логи не выводятся. |
| V2TIM_LOG_DEBUG | Выводятся логи уровней DEBUG, INFO, WARNING и ERROR (уровни логирования по умолчанию). |
| V2TIM_LOG_INFO | Выводятся логи уровней INFO, WARNING и ERROR. |
| V2TIM_LOG_WARN | Выводятся логи уровней WARNING и ERROR. |
| V2TIM_LOG_ERROR | Выводятся логи уровня ERROR. |

Правила хранения логов SDK следующие:

- Локальные логи SDK по умолчанию хранятся в течение семи дней, после чего они будут автоматически очищены при инициализации SDK.
- По умолчанию логи SDK на Android хранятся в директории `/sdcard/tencent/imsdklogs/имя_пакета_приложения` для версий ранее v4.8.50 и в директории `/sdcard/Android/data/имя_пакета/files/log/tencent/imsdk` для v4.8.50 и более поздних версий.
- По умолчанию логи SDK на iOS хранятся в директории `/Library/Caches/com_tencent_imsdk_log`.
- По умолчанию логи SDK на Windows хранятся в директории запуска программы. Например, если программа работает в директории `C:\\App`, SDK будет сохранять логи в директории `C:\\App\\com_tencent_imsdk_log`.

Начиная с версии v4.7.1, для вывода логов SDK используется модуль xlog от WeChat, логи сжимаются по умолчанию и должны быть распакованы с использованием скрипта Python.

- Чтобы получить скрипт распаковки, нажмите [Decode Log 27](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/tools/xlog_decoder_python27.py) (для Python 2.7) или [Decode Log 30](https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/tools/xlog_decoder_python30.py) (для Python 3.0).
- В консоли Windows или macOS вы можете распаковать файлы логов, выполнив следующую команду. После распаковки имена файлов будут заканчиваться на "xlog.log", и вы можете открыть эти файлы с помощью текстового редактора.

```
python decode_mars_nocrypt_log_file.py imsdk_yyyyMMdd.xlog
```

#### Установка слушателя логов

Если вам требуется прослушивать логи SDK в реальном времени, вы можете вызвать `setLogListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMSDKConfig.html#a5e8f7fa8dc56123e353a416d8742835b) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMSDKConfig.html#v2timsdkconfig.loglistener) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMSDKConfig.html#aef1bb8224f845539ecb15cccfd07f82b) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMSDKConfig.html#ac9d77ab98d5e412d413e412b398c9a2b)) для установки слушателя логов.
После установки SDK будет выбрасывать информацию логов через этот обратный вызов в реальном времени.

> **Примечание:** Обратный вызов выполняется в основном потоке. Обратные вызовы логов могут происходить часто, поэтому будьте осторожны и не синхронизируйте слишком много трудоемких задач в обратном вызове, что может заблокировать основной поток.

Пример кода настройки `V2TIMSDKConfig` выглядит следующим образом:

Java

Swift

Objective-C

C++

```
// Инициализация объекта `config`V2TIMSDKConfig config = new V2TIMSDKConfig();// Указание уровня вывода логовconfig.setLogLevel(V2TIMSDKConfig.V2TIM_LOG_INFO);// Указание слушателя логовconfig.setLogListener(new V2TIMLogListener() {    @Override    public void onLog(int logLevel, String logContent) {        // `logContent` - это содержание лога SDK    }});
```

```
// Инициализация объекта `config`let config = V2TIMSDKConfig()// Указание уровня вывода логовconfig.logLevel = .V2TIM_LOG_INFO// Установка слушателя логовconfig.logListener = { logLevel, logContent in       // `logContent` - это содержание лога SDK    print("Log Level: \\(logLevel), Log Content: \\(logContent)")}
```

```
// Инициализация объекта `config`V2TIMSDKConfig *config = [[V2TIMSDKConfig alloc] init];// Указание уровня вывода логовconfig.logLevel = V2TIM_LOG_INFO;// Установка слушателя логовconfig.logListener = ^(V2TIMLogLevel logLevel, NSString *logContent) {    // `logContent` - это содержание лога SDK};
```

```
class LogListener final : public V2TIMLogListener {public:    LogListener() = default;    ~LogListener() override = default;    void OnLog(V2TIMLogLevel logLevel, const V2TIMString& logContent) override {        // `logContent` - это содержание лога SDK    }};// Обратите внимание, что `logListener` не должен быть освобожден перед деинициализацией SDK,// в противном случае обратный вызов логов не может быть вызван.LogListener logListener;// Инициализация объекта `config`V2TIMSDKConfig config;// Указание уровня вывода логовconfig.logLevel = V2TIMLogLevel::V2TIM_LOG_INFO;// Указание слушателя логовconfig.logListener = &logListener;
```

### Добавление слушателя событий SDK

После инициализации SDK будет сообщать о событиях, таких как состояние подключения и истечение билета входа, через `V2TIMSDKListener`.
Рекомендуется вызвать API `addIMSDKListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a2f0297e96d365013e7923275ce2a5d4e) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.addimsdklistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#ac569656a58908afba491710a8cb3c8d9) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a1982f2c3a698176ec3fb79ef3f945ed5)) для добавления слушателя событий SDK и выполнения обработки логики в соответствующем обратном вызове.

Обратные вызовы `V2TIMSDKListener` следующие:

| Обратный вызов события | Описание | Рекомендуемое действие |
| --- | --- | --- |
| onConnecting | SDK подключается к экземпляру CVM. | Отобразите статус "подключение" в интерфейсе. |
| onConnectSuccess | SDK успешно подключился к экземпляру CVM. | - |
| onConnectFailed | Не удалось подключить SDK к экземпляру CVM. | Уведомите пользователя, что сетевое соединение в настоящий момент недоступно. |
| onKickedOffline | Текущий пользователь отключен от сети. | Отобразите сообщение "Вы уже вошли с другого устройства. Вы уверены, что хотите войти снова?" в интерфейсе. |
| onUserSigExpired | Билет входа истек. | Выполните вход с новым `UserSig`. |
| onSelfInfoUpdated | Профиль текущего пользователя обновлен. | Обновите фото профиля и никнейм в интерфейсе. |

> **Примечание:** Если вы получили обратный вызов `onUserSigExpired`, то `UserSig`, использованный для входа, истек. В этом случае вам необходимо войти снова с новым `UserSig`. Если вы продолжите использовать истекший `UserSig`, SDK войдет в бесконечный цикл входа.

Пример кода:

Java

Swift

Objective-C

C++

```
// Тип `sdkListener` - `V2TIMSDKListener`.V2TIMManager.getInstance().addIMSDKListener(sdkListener);
```

```
// Тип `self` - id<V2TIMSDKListener>.V2TIMManager.shared.addIMSDKListener(listener: self)
```

```
// Тип `self` - id<V2TIMSDKListener>.[[V2TIMManager sharedInstance] addIMSDKListener:self];
```

```
// `sdkListener` - это экземпляр V2TIMSDKListener.V2TIMManager::GetInstance()->AddSDKListener(&sdkListener);
```

### Вызов API инициализации

После выполнения вышеуказанных шагов вы можете вызвать `initSDK` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#aaad4f7139ba213f7e36da3e337c2f890) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.initsdk(sdkappid:config:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a2b417a8af0e974233baf1593ffa6c0f0) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#aecee922675b671cd979d68604a4be1bb)) для инициализации SDK.

Пример кода:

Java

Swift

Objective-C

C++

```
// 1. Получите `SDKAppID` из консоли IM.// 2. Инициализируйте объект `config`.V2TIMSDKConfig config = new V2TIMSDKConfig();// 3. Укажите уровень вывода логов.config.setLogLevel(V2TIMSDKConfig.V2TIM_LOG_INFO);// 4. Добавьте слушатель события `V2TIMSDKListener`. `sdkListener` - это класс реализации `V2TIMSDKListener`. Если вам не нужно слушать события SDK, пропустите этот шаг.V2TIMManager.getInstance().addIMSDKListener(sdkListener);// 5. Инициализируйте SDK. Вы можете вызвать API входа сразу же после вызова этого API.int  sdkAppID = 1400000000; // пожалуйста, установите sdkAppID вашего собственного приложенияV2TIMManager.getInstance().initSDK(context, sdkAppID, config);
```

```
// 1. Получите `SDKAppID` из консоли IM.// 2. Инициализируйте объект `config`.let config = V2TIMSDKConfig()// 3. Укажите уровень вывода логов.config.logLevel = .V2TIM_LOG_INFO // Используйте значения перечисления// 4. Добавьте слушатель события `V2TIMSDKListener`. `self` - это класс реализации id<V2TIMSDKListener>. Если вам не нужно слушать события SDK, пропустите этот шаг.V2TIMManager.shared.addIMSDKListener(listener: self)// 5. Инициализируйте SDK. Вы можете вызвать API входа сразу же после вызова этого API.V2TIMManager.shared.initSDK(sdkAppID: sdkAppID, config: config)
```

```
// 1. Получите `SDKAppID` из консоли IM.// 2. Инициализируйте объект `config`.V2TIMSDKConfig *config = [[V2TIMSDKConfig alloc] init];// 3. Укажите уровень вывода логов.config.logLevel = V2TIM_LOG_INFO;// 4. Добавьте слушатель события `V2TIMSDKListener`. `self` - это класс реализации id<V2TIMSDKListener>. Если вам не нужно слушать события SDK, пропустите этот шаг.[[V2TIMManager sharedInstance] addIMSDKListener:self];// 5. Инициализируйте SDK. Вы можете вызвать API входа сразу же после вызова этого API.int  sdkAppID = 1400000000; // пожалуйста, установите sdkAppID вашего собственного приложения[[V2TIMManager sharedInstance] initSDK:sdkAppID config:config];
```

```
// 1. Получите `SDKAppID` из консоли IM.// 2. Инициализируйте объект `config`.V2TIMSDKConfig config;// 3. Укажите уровень вывода логов.config.logLevel = V2TIMLogLevel::V2TIM_LOG_INFO;// 4. Добавьте слушатель события `V2TIMSDKListener`. `sdkListener` - это класс реализации `V2TIMSDKListener`.//    Если вам не нужно слушать события SDK, пропустите этот шаг.V2TIMManager::GetInstance()->AddSDKListener(&sdkListener);// 5. Инициализируйте SDK. Вы можете вызвать API входа сразу же после вызова этого API.int  sdkAppID = 1400000000; // пожалуйста, установите sdkAppID вашего собственного приложенияV2TIMManager::GetInstance()->InitSDK(sdkAppID, config);
```

### Деинициализация

Как правило, если жизненный цикл вашего приложения совпадает с жизненным циклом SDK, вам не нужно деинициализировать SDK перед выходом из приложения.
Однако вы можете деинициализировать SDK в особых случаях, например, только после входа на определенный интерфейс и больше не используется после выхода с интерфейса.

Деинициализация требует двух шагов:

1. Если вы вызвали `addIMSDKListener` для добавления слушателя SDK, вызовите `removeIMSDKListener` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a9b98e6b9ac0f883f055ef82563467b43) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.removeimsdklistener(listener:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a2e2a7e64bf51888c98636e5974a8aca7) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a0be850c20964cbbdceee33902cd2ed5d)) для его удаления.
2. Вызовите API деинициализации `unInitSDK` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMManager.html#a8ac73b4f71f9d9a1ca01551c919d3cdd) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.uninitsdk()) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a286e5358ec4cd0a8f9c66f4d2d7d4544) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a6c88218989a1c714b4e989d1696439a0)).

Пример кода:

Java

Swift

Objective-C

C++

```
// Удаление слушателя события `V2TIMSDKListener`. `sdkListener` - это класс реализации `V2TIMSDKListener`.V2TIMManager.getInstance().removeIMSDKListener(sdkListener);// Деинициализация SDKV2TIMManager.getInstance().unInitSDK();
```

```
// `self` - это класс реализации id<V2TIMSDKListener>.V2TIMManager.shared.removeIMSDKListener(listener: self)// Деинициализация SDKV2TIMManager.shared.unInitSDK()
```

```
// `self` - это класс реализации id<V2TIMSDKListener>.[[V2TIMManager sharedInstance] removeIMSDKListener:self];// Деинициализация SDK[[V2TIMManager sharedInstance] unInitSDK];
```

```
// Удаление слушателя события `V2TIMSDKListener`. `sdkListener` - это экземпляр V2TIMSDKListener.V2TIMManager::GetInstance()->RemoveSDKListener(&sdkListener);// Деинициализация SDKV2TIMManager::GetInstance()->UnInitSDK();
```

## Часто задаваемые вопросы

1. **Что мне делать, если при вызове API входа или другого API возвращается код ошибки 6013 с описанием "not initialized"?**

Вы должны инициализировать SDK перед использованием функций входа, сообщений, групп, разговоров, цепочки отношений и профиля, а также сигнализации.


---
*Источник: [https://trtc.io/document/47968](https://trtc.io/document/47968)*

---
*Источник (EN): [step-2-initialize-chat-sdk.md](./step-2-initialize-chat-sdk.md)*
