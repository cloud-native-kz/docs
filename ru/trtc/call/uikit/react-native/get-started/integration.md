# Интеграция

Этот документ описывает, как быстро интегрировать компонент TUICallKit. Вы можете выполнить следующие ключевые шаги в течение 10 минут и получить полный интерфейс для аудио- и видеозвонков.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/49a11cacb92f11f0b9945254005ef0f7.png)

## Подготовка

### **Требования к окружению**

- [Node.js](https://nodejs.org/en/): версия 16 и выше.
- **Требования к устройству:** мобильные устройства под управлением Android 5.0 и выше.

### Активация сервиса

Обратитесь к документации [Активация сервиса](https://trtc.io/document/59832?platform=web&product=call), чтобы получить SDKAppID и SecretKey. Они будут использоваться как обязательные параметры на этапе [входа](#e087d4ca-739f-41e5-a297-802b8df9fd53).

## Реализация

### Шаг 1. Импорт компонентов

1. **Установка через npm/yarn:** вы можете загрузить компонент [@tencentcloud/call-uikit-react-native](https://www.npmjs.com/package/@tencentcloud/call-uikit-react), используя следующую команду:

```
yarn add @tencentcloud/call-uikit-react-native
```

2. Скопируйте файлы [Debug](https://github.com/Tencent-RTC/TUICallKit/tree/main/ReactNative/src/debug) (генерация UserSig): скопируйте директорию debug в ваш проект. Вы можете использовать файлы в этой директории для локального генерирования userSig с вашими `SDKAppID` и `SecretKey`.

Метод 1

Метод 2

Вы можете найти их в директории [TUICallKit/ReactNative/src/debug](https://github.com/Tencent-RTC/TUICallKit/tree/main/ReactNative/src/debug) репозитория [GitHub](https://github.com/Tencent-RTC/TUICallKit).

Из node_modules: Вы можете получить их из пакета [@tencentcloud/call-uikit-react-native](https://www.npmjs.com/package/@tencentcloud/call-uikit-react):

MacOS

Windows

```
cp -r node_modules/@tencentcloud/call-uikit-react-native/src/debug ./src
```

```
xcopy node_modules\\@tencentcloud\\call-uikit-react\\src\\debug .\\src\\debug /i /e
```

### Шаг 2. Вход в систему

Вы можете использовать пример кода входа в `App.tsx`. Этот процесс выполняет вход для компонента TUI. Этот шаг критически важен; вы можете использовать функции, предоставленные TUICallKit, только после успешного входа.

**login**

```
import { TUICallKit, MediaType } from '@tencentcloud/call-uikit-react-native';import * as GenerateTestUserSig from "./debug/GenerateTestUserSig-es";const handleLogin = async () => {  try {    const sdkAppID = 0;   // Replace with the SDKAppID obtained from the console    const secretKey = ''; // Replace with the SecretKey obtained from the console    const userId = 'jack' // Replace with your UserId    const { userSig } = genTestUserSig({      SDKAppID: sdkAppID,      SecretKey: secretKey,      userID: loginUserID,    });    await TUICallKit.login({      sdkAppId: sdkAppID,      userId: loginUserID,      userSig,    });    console.log('login success');  } catch (error) {    console.error('login fail:', error);  }};
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | Допускает только комбинацию прописных и строчных букв (a-z A-Z), цифр (0-9), дефисов и подчеркиваний. |
| SDKAppId | int | Уникальный идентификатор SDKAppID приложения для аудио/видео, созданного в [консоли Tencent RTC](https://console.trtc.io). |
| SecretKey | String | SDKSecretKey приложения для аудио/видео, созданного в [консоли Tencent RTC](https://console.trtc.io). |
| userSig | String | Подпись безопасности, используемая для аутентификации входа пользователя, проверки подлинности пользователя и предотвращения кража прав на использование облачного сервиса злоумышленниками. |

> **Примечание:** **Среда разработки**: если вы находитесь на этапе локальной разработки и отладки, вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерирования userSig. При этом методе secretKey очень легко декомпилировать и провести обратную инженерию. Если ваш ключ утекает, злоумышленники могут украсть трафик вашего Tencent Cloud. **Среда производства**: если ваш проект готов к запуску, реализуйте [серверную генерацию UserSig](https://www.tencentcloud.com/document/product/647/35166).

### Шаг 3. Установка никнейма и аватара [Опционально]

Пользователи, вошедшие в систему впервые, не имеют информации об аватаре и никнейме. Вы можете установить аватар и никнейм, используя интерфейс `setSelfInfo`:

**setSelfInfo**

```
import { TUICallKit, MediaType } from '@tencentcloud/call-uikit-react-native';const setSelfInfo = () => {  const nickName = 'mick';                      // Nickname to set  const avatar = 'https:/****/user_avatar.png'; // profile photo URL to set  TUICallKit.setSelfInfo(    nickName,    avatar,    () => {      console.log('setSelfInfo success.');    },    (errCode, errMsg) => {      console.error('setSelfInfo fail:', errCode, errMsg);    }  );};
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| nickName | String | Никнейм для установки целевому пользователю. |
| avatar | String | URL аватара для установки целевому пользователю. |

### Шаг 4. Инициирование звонка

Инициатор звонка инициирует аудио- или видеозвонок, вызывая функцию `calls` и указывая тип звонка и список User ID получателей. Интерфейс `calls` поддерживает как один-на-один, так и групповые звонки. Звонок один-на-один инициируется, когда userIDList содержит один User ID; групповой звонок инициируется, когда userIDList содержит несколько User ID.

**calls**

```
import { TUICallKit, MediaType } from '@tencentcloud/call-uikit-react-native';const calls = async () => {  try {    const userIdList: string[] = ['lee', 'jane']; // called list    const mediaType = MediaType.Audio             // call type    await TUICallKit.calls({      userIdList: userIdList,      mediaType,    });    console.log('calls success');  } catch (error) {    console.error('calls fail:', error);  }};
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | Array<String> | Список User ID целевых пользователей. |
| mediaType | [MediaType](https://www.tencentcloud.com/document/product/647/66840#fb7a5c31-59f7-421a-a743-a08ac55305d8) | Тип медиа звонка, такой как видеозвонок, голосовой звонок. MediaType.Audio — голосовой звонок. MediaType.Video — видеозвонок. |
| callParams | [callParams](https://www.tencentcloud.com/document/product/647/66840#7c505b92-4c45-43cd-a254-cbce7809a746) | Параметры расширения звонка, такие как номер комнаты, время ожидания приглашения на звонок, пользовательское содержание оффлайн-уведомления. |

### Шаг 5. Ответ на звонок

После успешного входа получателя и инициирования звонка инициатором получатель получит приглашение на звонок с сопровождением рингтона и вибрации.

## Дополнительные функции

### Настройка языка

- **Поддерживаемые языки:** мы в настоящее время поддерживаем упрощенный китайский, традиционный китайский, английский, японский и арабский языки.
- **Переключение языков:** язык по умолчанию TUICallKit соответствует языковой настройке операционной системы мобильного устройства. Если вам нужно переключить язык, вы можете использовать метод `setLanguage`.

**setLanguage**

```
import { Language } from '@tencentcloud/call-uikit-react-native';TUICallKit.setLanguage(Language.EN);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| language | string | Language.ZH_CN — упрощенный китайский. Language.ZH_TW — традиционный китайский. Language.EN — английский. Language.AR — арабский. |

> **Примечание:** если вам нужно настроить другие языки, обратитесь к нам по адресу **info_rtc@tencent.com**.

### Настройка рингтона

Вы можете настроить рингтон по умолчанию, режим без звука входящего звонка и рингтон оффлайн-уведомления, используя следующие методы:

- **Установка рингтона по умолчанию:** используйте интерфейс `setCallingBell` для установки рингтона входящего звонка, получаемого получателем.

**setCallingBell**

```
import { TUICallKit, MediaType } from '@tencentcloud/call-uikit-react-native';const setCallingBell = () => {  const filePath = 'path/to/your/bell.mp3'; // File path of the ringtone  TUICallKit.setCallingBell(filePath);};
```

**Подробности**: установленный рингтон должен быть файлом ресурса в главном проекте и должен быть настроен в файле pubspec.yaml главного проекта. Разрешены только локальные пути к файлам. Настройка рингтона привязана к устройству; даже если пользователь изменится, настройка рингтона остается прежней. Чтобы восстановить рингтон по умолчанию, просто передайте пустой filePath.

| Параметр | Тип | Описание |
| --- | --- | --- |
| filePath | String | Путь к файлу рингтона. |

- **Режим без звука входящего звонка:** вы можете установить режим отключения звука, используя `enableMuteMode`.

**enableMuteMode**

```
import { TUICallKit, MediaType } from '@tencentcloud/call-uikit-react-native';TUICallKit.enableMuteMode(true);
```

**Подробности**: когда включено, запрос на звонок не будет вызывать воспроизведение рингтона.

## Часто задаваемые вопросы

Если вы столкнулись с какими-либо проблемами во время интеграции и использования, обратитесь к [Часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/51024).

## Связаться с нами

Если у вас есть какие-либо предложения или отзывы, свяжитесь с нами по адресу `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/66932](https://trtc.io/document/66932)*

---
*Источник (EN): [integration.md](./integration.md)*
