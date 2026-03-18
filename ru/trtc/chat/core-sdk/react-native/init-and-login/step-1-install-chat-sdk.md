# Шаг 1: Установка Chat SDK

Этот документ описывает, как быстро интегрировать Tencent Cloud Chat SDK в ваш проект React Native.

> **Примечание:** Интеграция [@tencentcloud/chat](https://www.npmjs.com/package/@tencentcloud/chat) в проект React Native требует загрузки версии 3.4.3 или более поздней. Интеграция [tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin) в проект React Native требует загрузки версии 1.4.0 или более поздней.

## Требования к окружению

| Платформа | Версия |
| --- | --- |
| React Native | v0.75.0 или более поздняя. |
| Android | Android Studio 3.5 или более поздняя. Приложение требует устройства Android 4.1 или более поздней версии. |
| iOS | Xcode 11.0 или более поздняя. Для тестирования на реальном устройстве убедитесь, что ваш проект имеет действительную подпись разработчика. |
| Node | Версия 18.0 или более поздняя. |

## Конфигурирование среды разработки

Если это ваш первый проект React Native, обратитесь к официальным инструкциям React Native [set-up-your-environment](https://reactnative.dev/docs/set-up-your-environment) для конфигурирования среды разработки.

Если вы столкнулись с проблемами окружения при создании или компиляции проекта, вы можете запустить `npx react-native doctor` для диагностики окружения.

## Создание проекта (может быть пропущено, если у вас уже есть проект)

```
npx react-native@latest init chatExample
```

`npm react-native` создает проекты с версией Android gradle 8.8. Если ваша версия Android gradle ниже 8.8, откройте Android Studio для синхронизации версии gradle.

## Интеграция Chat SDK

- Интегрируйте Chat SDK в ваш проект React Native с помощью npm.
- Вы можете интегрировать плагин загрузки [tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin) для более быстрой и безопасной загрузки ресурсов сообщений с расширенным содержимым.
- Улучшите пользовательский опыт в условиях плохой сети или при переключении сети путем интеграции [@react-native-community/netinfo](https://www.npmjs.com/package/@react-native-community/netinfo).

Установите зависимости Chat SDK в ваш проект React Native.

```
npm install @tencentcloud/chat tim-upload-plugin  @react-native-community/netinfo --save
```

## Инициализация

У вас должен быть правильный SDKAppID для продолжения инициализации.
SDKAppID — это уникальный идентификатор, который Tencent Cloud IM использует для различения аккаунтов клиентов. Мы рекомендуем подать заявку на новый SDKAppID для каждого независимого приложения. Сообщения между разными SDKAppIDs по сути изолированы и не могут взаимодействовать.
Вы можете просмотреть все SDKAppIDs в [консоли Chat](https://console.trtc.io/). Нажмите **Create application** для создания нового SDKAppID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/224ad8c766a111ef9664525400d5f8ef.png)

Импортируйте Chat SDK и инициализируйте его в файле App.tsx вашего проекта.

```
import TencentCloudChat from '@tencentcloud/chat';import TIMUploadPlugin from 'tim-upload-plugin';import NetInfo from '@react-native-community/netinfo';let options = {  SDKAppID: 0 // Replace 0 with the SDKAppID of your Chat application when connecting};// Create an SDK instance. The `TencentCloudChat.create()` method returns the same instance for the same `SDKAppID`let chat = TencentCloudChat.create(options); // The SDK instance is usually referred to as chatchat.setLogLevel(0); // Normal level, with a lot of logs; it's recommended for integration// Register the Tencent Cloud Instant Messaging rich media resource upload pluginchat.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});// Register the network monitoring pluginchat.registerPlugin({'chat-network-monitor': NetInfo});
```

## Прослушивание событий

#### SDK_READY

Это срабатывает, когда SDK входит в состояние готовности. После того как обращающаяся сторона прослушает это событие, она может вызывать API SDK для отправки сообщений или использования других функций SDK.

```
let onSdkReady = function(event) {  // After listening to the SDK ready event, you can make API calls};chat.on(TencentCloudChat.EVENT.SDK_READY, onSdkReady);
```

#### SDK_NOT_READY

Это срабатывает, когда SDK входит в состояние неготовности. В этот момент обращающаяся сторона не сможет использовать функции, такие как отправка сообщений через SDK. Для возобновления использования обращающаяся сторона должна вызвать интерфейс входа и привести SDK в состояние готовности.

```
let onSdkNotReady = function(event) {  // chat.login({userID: 'your userID', userSig: 'your userSig'});};chat.on(TencentCloudChat.EVENT.SDK_NOT_READY, onSdkNotReady);
```

#### MESSAGE_RECEIVED

Когда SDK получает новые сообщения из индивидуального чата, группового чата, групповых подсказок или групповых системных уведомлений, обращающаяся сторона может пройти через event.data для получения данных списка сообщений и отобразить их в пользовательском интерфейсе.

```
let onMessageReceived = function(event) {  // event.data - An array that stores `Message` objects - [Message]};chat.on(TencentCloudChat.EVENT.MESSAGE_RECEIVED, onMessageReceived);
```

#### CONVERSATION_LIST_UPDATED

Список разговоров обновлен. event.data — это массив, содержащий объекты Conversation.

```
let onConversationListUpdated = function(event) {  console.log(event.data); // Array that stores Conversation instances};chat.on(TencentCloudChat.EVENT.CONVERSATION_LIST_UPDATED, onConversationListUpdated);
```

> **Примечание:** Если вы хотите узнать больше об уведомлениях о событиях SDK, просмотрите [список событий SDK](https://trtc.io/document/33999?platform=web&product=chat&menulabel=sdk#event).

## Деинициализация

Завершите экземпляр SDK. SDK выполнит выход, разорвет постоянное соединение WebSocket и затем освободит ресурсы.

```
chat.destroy();
```

## Вход

Вход требует предоставления информации, такой как userID и userSig. Пожалуйста, войдите в [консоль Chat](https://console.trtc.io/) для их получения.

- userID
  - Нажмите для входа в [Application](https://console.trtc.io/app), который вы создали, и вы увидите запись Chat Product на левой панели. Нажмите для входа.
  - После входа на подстраницу Chat Product нажмите Users для входа на страницу управления пользователями.
  - Нажмите Create account для открытия формы информации об учетной записи. Если это обычный пользователь, мы рекомендуем выбрать тип General.
  - Для улучшения вашего опыта с функциями отправки и получения сообщений мы рекомендуем создать два userID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f458ea6166a111ef9664525400d5f8ef.png)

- userSig можно сгенерировать в реальном времени с помощью инструментов разработки, предоставляемых консолью. Пожалуйста, нажмите [Chat Console > Development Tools > UserSig Tools > Signature (UserSig) Generator](https://console.trtc.io/usersig).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2fd484fd66a211ef97015254002693fd.png)

```
let promise = chat.login({  userID: 'your userID',  userSig: 'your userSig',});promise.then(function(imResponse) {  if (imResponse.data.repeatLogin === true) {    // This indicates that the account is already logged in. This login attempt is a duplicate login.    console.log(imResponse.data.errorInfo);  }}).catch(function(imError) {  // Information related to login failure  console.warn('login error:', imError);});
```

## Компиляция и запуск приложения React Native

Для компиляции и запуска проекта вам нужно использовать реальное устройство или эмулятор. **Рекомендуется использовать реальное устройство.** Вы можете обратиться к официальному веб-сайту React Native [running-on-device](https://reactnative.dev/docs/running-on-device) для подключения реального устройства для отладки.

Android

iOS

1. Включите режим разработчика на вашем телефоне и включите переключатель **USB Debugging**.
2. Подключите ваш телефон через USB. Рекомендуется выбрать опцию **Transfer files**, **не выбирайте опцию Charging only**.
3. После подтверждения успешного подключения телефона выполните `npm run android` для компиляции и запуска проекта.

```
npm run android
```

1. Подключите мобильный телефон кабелем USB и откройте директорию ios проекта с помощью Xcode.
2. Конфигурируйте информацию подписания в соответствии с официальным веб-сайтом React Native [running-on-device](https://reactnative.dev/docs/running-on-device?platform=ios).
3. Перейдите в директорию ios и установите зависимости.

```
cd iospod install
```

4. Вернитесь в корневую директорию и выполните `npm run ios` для компиляции и запуска проекта.

```
cd ../npm run ios
```

## Интеграция сторонних модулей

Если вам нужно реализовать функции отправки **Изображений, Видео, Файлов, Голоса**, рекомендуется использовать сторонние модули, представленные ниже.

- **Выбор изображений и видео, Съемка фото, Запись видео**, вам нужно интегрировать [react-native-image-picker](https://www.npmjs.com/package/react-native-image-picker).

```
npm install react-native-image-picker --save
```

Выбрать изображение

Сделать фото

Выбрать видео

Записать видео

```
import {launchImageLibrary} from 'react-native-image-picker'; // 1. Select an ImagelaunchImageLibrary({  mediaType: 'photo',  selectionLimit: 1,}).then((result) => { const file = result.assets[0]; // 2. Create a message instance. The instance returned by the interface can be displayed on the screen let message = chat.createImageMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: { file: file },    // React Native does not support upload progress callback    // onProgress: function(event) { console.log('file uploading:', event) }  });  // 3. Send Image  let promise = chat.sendMessage(message);  promise.then(function(imResponse) {    // The message was successfully sent    console.log(imResponse);  }).catch(function(imError) {    // The message failed to be sent    console.warn('sendMessage error:', imError);  });});
```

```
import {launchCamera} from 'react-native-image-picker';// 1. Take PhotolaunchCamera({  mediaType: 'photo',  cameraType: 'back',}).then((result) => { const file = result.assets[0]; // 2. Create a message instance. The instance returned by the interface can be displayed on the screen let message = chat.createImageMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: { file: file },    // React Native does not support upload progress callback    // onProgress: function(event) { console.log('file uploading:', event) }  });  // 3. Send Image  let promise = chat.sendMessage(message);  promise.then(function(imResponse) {    // The message was successfully sent    console.log(imResponse);  }).catch(function(imError) {    // The message failed to be sent    console.warn('sendMessage error:', imError);  });});
```

```
import {launchImageLibrary} from 'react-native-image-picker'; // 1. Select a VideolaunchImageLibrary({  mediaType: 'video',  selectionLimit: 1,}).then((result) => { const file = result.assets[0]; // 2. Create a message instance. The instance returned by the interface can be displayed on the screen let message = chat.createVideoMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: { file: file },    // React Native does not support upload progress callback    // onProgress: function(event) { console.log('file uploading:', event) }  });  // 3. Send Video  let promise = chat.sendMessage(message);  promise.then(function(imResponse) {    // The message was successfully sent    console.log(imResponse);  }).catch(function(imError) {    // The message failed to be sent    console.warn('sendMessage error:', imError);  });});
```

```
import {launchCamera} from 'react-native-image-picker';// 1. Record VideolaunchCamera({  mediaType: 'video',  cameraType: 'back',}).then((result) => { const file = result.assets[0]; // 2. Create a message instance. The instance returned by the interface can be displayed on the screen let message = chat.createVideoMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: { file: file },    // React Native does not support upload progress callback    // onProgress: function(event) { console.log('file uploading:', event) }  });  // 3. Send Video  let promise = chat.sendMessage(message);  promise.then(function(imResponse) {    // The message was successfully sent    console.log(imResponse);  }).catch(function(imError) {    // The message failed to be sent    console.warn('sendMessage error:', imError);  });});
```

- **Выбор файлов**, вам нужно интегрировать [react-native-document-picker](https://www.npmjs.com/package/react-native-document-picker).

```
npm install react-native-document-picker --save
```

```
import DocumentPicker from 'react-native-document-picker'; // 1. Select FileDocumentPicker.pick({  type: [DocumentPicker.types.allFiles],}).then((result) => { const file = result[0]; // 2. Create a message instance. The instance returned by the interface can be displayed on the screen let message = chat.createFileMessage({    to: 'user1',    conversationType: TencentCloudChat.TYPES.CONV_C2C,    payload: { file: file },    // React Native does not support upload progress callback    // onProgress: function(event) { console.log('file uploading:', event) }  });  // 3. Send File  let promise = chat.sendMessage(message);  promise.then(function(imResponse) {    // The message was successfully sent    console.log(imResponse);  }).catch(function(imError) {    // The message failed to be sent    console.warn('sendMessage error:', imError);  });});
```

- **Запись голоса**, вам нужно интегрировать [react-native-audio-recorder-player](https://www.npmjs.com/package/react-native-audio-recorder-player).

```
npm install react-native-audio-recorder-player --save
```

```
import AudioRecorderPlayer, {AVEncodingOption} from 'react-native-audio-recorder-player'; // Record recording durationlet duration = 0;// Record recording file pathlet uri = ''; // 1. Start recordingconst onStartRecord = async () => {  await audioRecorderPlayer.startRecorder('test.aac',{    VFormatIDKeyIOS: AVEncodingOption.aac,  });  audioRecorderPlayer.addRecordBackListener((e: any) => {    duration = e.currentPosition;  });};// 2. Stop recordingconst onStopRecord = async () => {  uri = await audioRecorderPlayer.stopRecorder();  audioRecorderPlayer.removeRecordBackListener();};// 3. Send voiceconst file = {  uri: uri,  duration: duration,};let message = chat.createAudioMessage({  to: 'user1',  conversationType: 'C2C',  payload: {    file: file,  },  // React Native does not support upload progress callback  // onProgress: function(event) { console.log('file uploading:', event) }});let promise = chat.sendMessage(message);promise.then(function(imResponse) {  // The message was successfully sent  console.log(imResponse);}).catch(function(imError) {  // The message failed to be sent  console.warn('sendMessage error:', imError);});
```

> **Примечание:** Чтобы включить воспроизведение `VoiceMessage` на всех платформах, упаковка приложения iOS требует указания VFormatIDKeyIOS как AVEncodingOption.aac для записи голоса.

Для использования альбома, камеры и микрофона вам нужно конфигурировать соответствующие разрешения. После конфигурирования вам нужно перекомпилировать и запустить проект для обеспечения эффективности.

Android

iOS

В директории android найдите app/src/main/AndroidManifest.xml и добавьте следующие разрешения:

```
 <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" /> <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" /> <uses-permission android:name="android.permission.RECORD_AUDIO" />
```

В директории ios найдите Info.plist и добавьте следующие разрешения:

```
<key>NSCameraUsageDescription</key><string>We need access to your camera to take photos</string><key>NSPhotoLibraryUsageDescription</key><string>We need access to your album to select photos</string><key>NSMicrophoneUsageDescription</key><string>We need access to your microphone to record audio</string>
```

## Пользовательская структура файла сообщения с расширенным содержимым

Если вы выбрали другие плагины третьих сторон для выбора изображений, видео, файлов и записи голоса, пожалуйста, соберите файл согласно следующей структуре:

Изображение

Видео

Файл

Голос

**uri, fileName, type, width, height** — обязательны, fileSize — опционально, если недоступен.

```
const file = {  uri: 'xxx',  fileName: 'xxx',  fileSize: 1,  type: 'xxx',  width: 1,  height: 1,};
```

**uri, fileName, type** — обязательны, и формат type должен быть ****/***. fileSize и duration — опциональны, если недоступны.

```
const file = {  uri: 'xxx',  fileName: 'xxx',  fileSize: 1,  type: 'xxx',  duration: 0,};
```

**uri, size, name** — обязательны, и size должен быть больше 0.

```
const file = {  uri: 'xxx',  name: 'xxx',  size: 1,};
```

**uri, fileName, duration** — обязательны. duration измеряется в миллисекундах (мс). fileSize — опционально, если недоступен.

```
const file = {  uri: 'xxx',  fileName: 'xxx',  fileSize: 1,  duration: 0,};
```

## Часто задаваемые вопросы

1. При запуске npm run android и возникновении ошибки, как показано на изображении, пожалуйста, переустановите переменные окружения в корневой директории проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7eeeed1065a711efb66652540055f650.png)

```
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

2. Если выполнение команды Build в Xcode вызывает проблему с переменными окружения node, пожалуйста, сделайте следующее:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/65fcdae165ab11efb66652540055f650.png)

```
cd iosecho export NODE_BINARY=$(command -v node) > .xcode.env
```

## Документация

- Для получения дополнительной информации об API Chat SDK, пожалуйста, обратитесь к [Client API](https://trtc.io/document/33999?platform=web&product=chat&menulabel=sdk).


---
*Источник: [https://trtc.io/document/48865](https://trtc.io/document/48865)*

---
*Источник (EN): [step-1-install-chat-sdk.md](./step-1-install-chat-sdk.md)*
