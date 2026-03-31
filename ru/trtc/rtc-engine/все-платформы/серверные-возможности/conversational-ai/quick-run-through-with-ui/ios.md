# iOS

Этот документ поможет вам интегрировать компонент `AIConversationKit` за короткое время. Следуя этому руководству, вы завершите следующие ключевые шаги в течение 20 минут и реализуете проект разговорного ИИ с полноценным интерфейсом.

| **Интерфейс разговорного ИИ**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecf08a9312e511f0a9cd5254007c27c5.png) |
| --- |
|  |

## Подготовка окружения

- Минимальная совместимость с iOS 13. Рекомендуется использовать iOS 13 и более новые версии.
- Xcode 13 и более новые версии.

## Шаг первый: активация сервиса

Перед началом использования разговорного ИИ с AiConversationKit вам необходимо перейти в консоль и активировать сервис разговорного ИИ для AiConversationKit. Подробные инструкции см. в разделе [Активация сервиса](https://www.tencentcloud.com/document/product/647/69002#).

## Шаг второй: скачивание компонента AIConversationKit

Перейдите на [Github](https://github.com/Tencent-RTC/AIConversationKit) и скачайте zip-файл. После распаковки вы увидите директорию **AIConversationKit**, файл **AIConversationKit.podspec** и директорию **Resource**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecfada7b12e511f09fca52540099c741.png)

## Шаг третий: конфигурация

1. Скопируйте **AIConversationKit**, **podspec** и **Resource** из директории, распакованной на [шаге два](https://www.tencentcloud.com/document/product/647/69005#step2), в ваш проект:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed1d3d0e12e511f08c275254001c06ec.png)

2. Затем в `Podfile` вашего проекта добавьте следующие зависимости:

```
   pod 'AIConversationKit',:path => 'AIConversationKit.podspec':
```

3. После завершения конфигурации выполните `pod install` для завершения установки зависимостей;
4. Используйте XCode для открытия `.xcworkspace` и конфигурируйте информацию сертификата:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecee1d1412e511f0aaa3525400e889b2.png)

## Шаг четвёртый: вход в систему

Добавьте следующий код в ваш проект. Он позволяет компоненту выполнить вход, вызвав соответствующие API в `TUILogin`. **Этот шаг критически важен**, так как только после входа функции `AIConversationkit` будут работать корректно. Пожалуйста, внимательно проверьте, что все необходимые параметры конфигурированы правильно.

swift

```
import TUICoreimport AIConversationKitfunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        let sdkAppId = 1600000001  // Please replace with your sdkAppId        let userId = "people"      // Please replace with your UserID        let secretKey = "xxx"      // Please replace with your sdkSecretKey        let userSig = GenerateTestUserSig.genTestUserSig(sdkAppId: sdkAppId, identifier: userId, secrectkey: secretKey)        TUILogin.login(Int32(sdkAppId), userID: userId, userSig:userSig){            print("login success")        } fail: { code, message in            print("login failed, code: \\(code), error: \\(message ?? "nil")")        }    return true}
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userID | String | Пользователи определяют свои пользовательские ID согласно своему собственному бизнесу, допускаются только комбинации прописных и строчных латинских букв (a-z A-Z), цифр (0-9), подчеркивания и дефиса. |
| sdkAppID | Int32 | Уникальный идентификатор SDKAppID приложения аудио и видео, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| secretKey | String | SDKSecretKey приложения аудио и видео, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| userSig | String | Подпись защиты безопасности, используемая для аутентификации при входе пользователя, подтверждающая подлинность пользователя и предотвращающая неправомерное использование прав на облачные услуги злоумышленниками. |

> **Примечание:**
> **Окружение разработки**: если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию GenerateTestUserSig.genTestSig для генерации userSig. Обратите внимание, что SDKSecretKey в этом методе может быть легко декомпилирован и подвергнут обратному проектированию. При утечке ключа злоумышленники могут неправомерно использовать ваш трафик Tencent Cloud.
> **Окружение производства**: если вы хотите запустить свой проект, используйте [генерацию UserSig сервером](https://www.tencentcloud.com/zh/document/product/647/35166#.E6.AD.A3.E5.BC.8F.E8.BF.90.E8.A1.8C.E9.98.B6.E6.AE.B5.E5.A6.82.E4.BD.95.E8.AE.A1.E7.AE.97-usersig.EF.BC.9F).

## Шаг пятый: запуск вашего первого проекта разговорного ИИ

После успешного выполнения [TUILogin.login](https://www.tencentcloud.com/document/product/647/54843#07002a30-aca6-4e6e-991f-0d8b65e315a6), см. следующий код для инициирования разговорного ИИ.

Swift

Новый вариант

```
let startParams = StartAIConversationParams()let sdkAppId = 1600000001  // 1,Replace your sdkAppIdlet secretKey = "xxx"      // 2,Replace your sdkSecretKeylet aiRobotId = "robot_\\(TUILogin.getUserID() ?? "")"let aiRobotSig = GenerateTestUserSig.genTestUserSig(sdkAppId: sdkAppId, identifier: aiRobotId, secrectkey: secretKey)startParams.agentConfig = AIConversationDefine.AgentConfig.generateDefaultConfig(aiRobotId: aiRobotId, aiRobotSig: aiRobotSig)startParams.secretId = "xxx"           // 3,Replace your secretIdstartParams.secretKey = "xxx"          // 4,Replace your secretKey// 5,Replace your llmConfigstartParams.llmConfig = "{\\"LLMType\\":\\"openai\\",\\"Model\\":\\"hunyuan-turbo-latest\\",\\"SystemPrompt\\":\\"You are a personal assistant\\",\\"APIUrl\\":\\"https://hunyuan.cloud.tencent.com/openai/v1/chat/completions\\",\\"APIKey\\":\\"xxxx\\",\\"History\\":5,\\"Streaming\\":true}"// 6,Replace your ttsConfigstartParams.ttsConfig = "{\\"TTSType\\":\\"tencent\\",\\"AppId\\":\\"xxx\\",\\"SecretId\\":\\"xxx\\",\\"SecretKey\\":\\"xxx\\",\\"VoiceType\\":\\"502001\\",\\"Speed\\":1.25,\\"Volume\\":5,\\"PrimaryLanguage\\":1,\\"FastVoiceType\\":\\"\\"}"let aiViewController = AIConversationViewController(aiParams: startParams)navigationController?.pushViewController(aiViewController, animated: true)
```

```

```

1. Используйте данные, полученные на [шаге четвёртом](https://www.tencentcloud.com/document/product/647/69005#07002a30-aca6-4e6e-991f-0d8b65e315a6), для sdkAppId и sdkSecretKey.
2. На странице сведений об приложении выберите **RTC-Engine** **> Conversational AI**, обратитесь к [БессCodeодная быстрая интеграция функции разговорного ИИ](https://www.tencentcloud.com/document/product/647/68137) для конфигурации параметров сервиса разговорного ИИ, включая основную конфигурацию, STT, LLM, TTS, нажмите кнопку **Quick Interation** в нижнем правом углу, переключитесь на iOS, получите параметры SecretId, SecretKey и Config.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed13240112e511f09fca52540099c741.png)

3. Скопируйте SecretId и SecretKey TencentCloud API в `startParams.secretId` и `startParams.secretKey`.
4. Скопируйте информацию Config в средство парсинга JSON, например [JsonUtil](https://www.json.cn/). Скопируйте значение строки, соответствующей LLMConfig, в `startParams.llmConfig`, и скопируйте значение строки, соответствующей TTSConfig, в `startParams.ttsConfig`.

> **Примечание:**
> **Окружение разработки**: если вы находитесь на этапе локальной разработки и отладки, вы можете быстро интегрировать разговорный ИИ, используя вышеуказанный метод. При этом методе информация об учётной записи очень легко может быть декомпилирована и взломана обратным проектированием. При утечке вашего ключа злоумышленники могут неправомерно использовать ваш трафик Tencent Cloud.
> **Окружение живого производства**: если ваш проект будет запущен, пожалуйста, сохраняйте вышеуказанную информацию об учётной записи на сервере, чтобы избежать неправомерного использования трафика; соответствующие конфигурации диалога также могут быть сохранены на сервере для удобной динамической настройки эффекта диалога ИИ.

## Свяжитесь с нами

Если у вас есть какие-либо вопросы или предложения в процессе интеграции, вы можете свободно связаться с нами: info_rtc@tencent.com .


---
*Источник: [https://trtc.io/document/69005](https://trtc.io/document/69005)*

---
*Источник (EN): [ios.md](./ios.md)*
