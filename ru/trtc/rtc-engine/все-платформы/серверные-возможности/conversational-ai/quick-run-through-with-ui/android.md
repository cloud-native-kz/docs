# Android

Этот документ содержит рекомендации по интеграции компонента `AIConversationKit` за короткое время. Следуя этому руководству, вы выполните следующие ключевые шаги в течение 20 минут и реализуете проект conversational AI с полным интерфейсом.

| **Интерфейс Conversational AI**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e2c65f4312e511f09fca52540099c741.png) |
| --- |
|  |

## Подготовка окружения

- Минимальная совместимость с Android 4.4 (SDK API Level 19). Рекомендуется использовать Android 5.0 (SDK API Level 21) и выше.
- Android Studio 3.5 и выше (Gradle 3.5.4 и выше).
- Мобильные устройства с Android 4.4 и выше.

## Шаг первый: активация сервиса

Перед инициацией диалога с AiConversationKit необходимо перейти в консоль и активировать сервис conversational AI для AIConversationKit. Подробные инструкции см. в разделе [Activate Service](https://www.tencentcloud.com/document/product/647/69002#).

## Шаг второй: загрузка компонента TUIRoomKit

1. Клонируйте код из [Github](https://github.com/Tencent-RTC/AIConversationKit), затем скопируйте подпапку `aiconversatonkit` из папки `Android` в папку того же уровня, что и app в вашем текущем проекте, как показано на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e2b1d43812e511f0aaa3525400e889b2.png)

## Шаг третий: конфигурация

1. Найдите файл `setting.gradle (или settings.gradle.kts)` в корневой папке проекта и добавьте в него следующий код. Это позволит импортировать компонент `aiconversationkit` в ваш текущий проект.

settings.gradle

settings.gradle.kts

```
include ':aiconversationkit'
```

```
include (":aiconversationkit")
```

2. Найдите файл `build.gradle (или build.gradle.kts)` в папке app и добавьте в него следующий код. Это позволит текущему `app` зависеть от новоприбавленного компонента `aiconversationkit`.

build.gradle

build.gradle.kts

```
api project(':aiconversationkit')
```

```
api(project(":aiconversatonkit"))
```

3. Поскольку в SDK используются функции отражения Java, некоторые классы в SDK необходимо добавить в список исключений из обфускации. Поэтому вам нужно добавить следующий код в файл proguard-rules.pro:

```
-keep class com.tencent.** { *; }
```

4. Найдите файл AndroidManifest.xml в папке app. Добавьте `tools:replace="android:allowBackup"` в узел `application`. Это переопределит параметры внутри компонента и использует ваши собственные параметры.

```
  // app/src/main/AndroidManifest.xml  <application    android:name=".DemoApplication"    android:allowBackup="false"    android:icon="@drawable/app_ic_launcher"    android:label="@string/app_name"    android:largeHeap="true"    android:theme="@style/AppTheme"    tools:replace="android:allowBackup">
```

## Шаг четвёртый: вход в систему

Добавьте следующий код в ваш проект. Это позволит компоненту выполнить вход, вызвав соответствующие API в `TUILogin`. **Этот шаг является критичным**, так как функции `AIConversationkit` можно использовать нормально только после входа. Пожалуйста, внимательно проверьте, правильно ли настроены соответствующие параметры.

Java

Kotlin

```
String userId = "denny"; // Пожалуйста, замените на ваш UserIDint sdkAppId = 1400000001; // Пожалуйста, замените на sdkAppId, полученный на шаге 1String sdkSecretKey = "xxxx"; // Пожалуйста, замените на sdkSecretKey, полученный на шаге 1String userSig = GenerateTestUserSig.genTestUserSig(sdkAppId, userId, sdkSecretKey);TUILogin.login(this, sdkAppId, userId, userSig, new TUICallback() {    @Override public void onSuccess() {}    @Override public void onError(int errorCode, String errorMessage) {}});
```

```
val userId = "denny" // Пожалуйста, замените на ваш UserIDval sdkAppId = 1400000001 // Пожалуйста, замените на sdkAppId, полученный на шаге 1val sdkSecretKey = "xxxx" // Пожалуйста, замените на sdkSecretKey, полученный на шаге 1val userSig = GenerateTestUserSig.genTestUserSig(sdkAppId, userId, sdkSecretKey)TUILogin.login(this, sdkAppId, userId, userSig, object : TUICallback() {      override fun onSuccess() {}      override fun onError(errorCode: Int, errorMessage: String) {}})
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | Пользователи могут самостоятельно настраивать пользовательские ID пользователей в соответствии со своим бизнесом. Допускается использование только букв в верхнем и нижнем регистре (a-z A-Z), цифр (0-9), подчеркивания и дефиса. |
| sdkAppId | int | Уникальный идентификатор SDKAppID аудио-видео приложения, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| secretKey | String | SDKSecretKey аудио-видео приложения, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| userSig | String | Подпись защиты безопасности, используемая для аутентификации входа пользователя, которая подтверждает подлинность пользователя и предотвращает несанкционированное использование ваших прав на облачные услуги со стороны злоумышленников. |

> **Примечания:****Среда разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации userSig. При использовании этого метода SDKSecretKey может быть легко декомпилирован и подвергнут обратному взлому. После утечки ключа злоумышленники смогут несанкционированно использовать ваш трафик Tencent Cloud.**Production среда**: Если вы хотите запустить свой проект, пожалуйста, используйте [генерацию UserSig сервером](https://trtc.io/document/35166).

## Шаг пятый: начало первого AI диалога

После успешного выполнения [TUILogin.login](https://www.tencentcloud.com/document/product/647/69004#07002a30-aca6-4e6e-991f-0d8b65e315a6), см. следующий код для инициации сервиса conversational AI.

Java

Kotlin

```
AIConversationDefine.StartAIConversationParams startParams = new AIConversationDefine.StartAIConversationParams();int sdkAppId = 1400000001;      // 1,Замените на ваш sdkAppIdString sdkSecretKey = "xxxx";   // 2,Замените на ваш sdkSecretKeyString aiRobotId = "robot_" + TUILogin.getUserId();String aiRobotSig = GenerateTestUserSig.genTestUserSig(sdkAppId, aiRobotId, sdkSecretKey);startParams.agentConfig = AIConversationDefine.AgentConfig.generateDefaultConfig(aiRobotId, aiRobotSig);startParams.secretId = "xxx";  // 3,Замените на ваш secretIdstartParams.secretKey = "xxx"; // 4,Замените на ваш secretKey// 5,Замените на ваш llmConfigstartParams.llmConfig = "{\\"LLMType\\":\\"openai\\",\\"Model\\":\\"hunyuan-turbo-latest\\",\\"SystemPrompt\\":\\"You are a private assistant\\",\\"APIUrl\\":\\"https:xxx\\",\\"APIKey\\":\\"xxx\\",\\"History\\":5,\\"Streaming\\":true}"; // 6,Замените на ваш ttsConfigstartParams.ttsConfig = "{\\"TTSType\\":\\"tencent\\",\\"AppId\\":\\"xxx\\",\\"SecretId\\":\\"xxx\\",\\"SecretKey\\":\\"xxx\\",\\"VoiceType\\":\\"502001\\",\\"Speed\\":1.25,\\"Volume\\":5,\\"PrimaryLanguage\\":1,\\"FastVoiceType\\":\\"\\"}";Intent intent = new Intent(this, AIConversationActivity.class);intent.putExtra(KEY_START_AI_CONVERSATION, startParams);startActivity(intent);
```

```
val startParams = AIConversationDefine.StartAIConversationParams()val sdkAppId = 1400000001 // 1,Замените на ваш sdkAppIdval sdkSecretKey = "xxxx" // 2,Замените на ваш sdkSecretKeyval aiRobotId = "robot_" + TUILogin.getUserId()val aiRobotSig = GenerateTestUserSig.genTestUserSig(sdkAppId, aiRobotId, sdkSecretKey)startParams.agentConfig = AIConversationDefine.AgentConfig.generateDefaultConfig(aiRobotId, aiRobotSig)startParams.secretId = "xxx" // 3,Замените на ваш secretIdstartParams.secretKey = "xxx" // 4,Замените на ваш secretKey// 5,Замените на ваш llmConfigstartParams.llmConfig = "{\\"LLMType\\":\\"openai\\",\\"Model\\":\\"hunyuan-turbo-latest\\",\\"SystemPrompt\\":\\"You are a private assistant\\",\\"APIUrl\\":\\"https:xxx\\",\\"APIKey\\":\\"xxx\\",\\"History\\":5,\\"Streaming\\":true}"// 6,Замените на ваш ttsConfigstartParams.ttsConfig = "{\\"TTSType\\":\\"tencent\\",\\"AppId\\":\\"xxx\\",\\"SecretId\\":\\"xxx\\",\\"SecretKey\\":\\"xxx\\",\\"VoiceType\\":\\"502001\\",\\"Speed\\":1.25,\\"Volume\\":5,\\"PrimaryLanguage\\":1,\\"FastVoiceType\\":\\"\\"}"val intent = Intent(this, AIConversationActivity::class.java)intent.putExtra(KEY_START_AI_CONVERSATION, startParams)startActivity(intent)
```

1. Используйте данные, полученные на [шаге четвёртый](https://www.tencentcloud.com/document/product/647/69004#07002a30-aca6-4e6e-991f-0d8b65e315a6), для sdkAppId и sdkSecretKey.
2. На странице деталей приложения выберите **RTC-Engine** **> Conversational AI**, см. раздел [No-Code Quick Integration Of Conversational AI Feature](https://www.tencentcloud.com/document/product/647/68137), чтобы настроить параметры сервиса conversational AI, включая основную конфигурацию, STT, LLM, TTS, нажмите кнопку **Quick Interation** в нижнем правом углу, переключитесь на Android и получите параметры SecretId, SecretKey и Config.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e2d9131512e511f0a9cd5254007c27c5.png)

3. Скопируйте SecretId и SecretKey API TencentCloud в `startParams.secretId` и `startParams.secretKey`.
4. Скопируйте информацию Config в инструмент для парсинга JSON, такой как [JsonUtil](https://www.json.cn/). Скопируйте значение строки, соответствующей LLMConfig, в `startParams.llmConfig`, и скопируйте значение строки, соответствующей TTSConfig, в `startParams.ttsConfig`.

> **Примечание:****Среда разработки**: Если вы находитесь на этапе локальной разработки и отладки, вы можете быстро интегрировать AI диалог, используя указанный выше метод. При использовании этого метода информация учётной записи может быть легко декомпилирована и подвергнута обратному взлому. После утечки ключа злоумышленники смогут неправомерно использовать ваш трафик Tencent Cloud.**Среда production**: Если ваш проект будет запущен, пожалуйста, сохраняйте вышеуказанную информацию учётной записи на сервере, чтобы избежать неправомерного использования трафика. Связанные конфигурации диалога также можно сохранять на сервере для удобной динамической настройки эффекта AI диалога.

## Свяжитесь с нами

Если у вас есть вопросы или предложения в процессе интеграции, не стесняйтесь обращаться: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/69004](https://trtc.io/document/69004)*

---
*Источник (EN): [android.md](./android.md)*
