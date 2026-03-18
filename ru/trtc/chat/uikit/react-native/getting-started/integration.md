# Интеграция

## Введение в chat-uikit-react-native

chat-uikit-react-native — это библиотека компонентов пользовательского интерфейса React Native, основанная на Tencent Cloud Chat SDK, предоставляющая общие компоненты пользовательского интерфейса, такие как сеансы, чат и функции групп. Благодаря этим хорошо разработанным компонентам пользовательского интерфейса вы можете быстро создавать элегантные, надежные и масштабируемые приложения для обмена сообщениями. Стиль пользовательского интерфейса, разработанный на основе React Native, лучше соответствует привычкам зарубежных пользователей и поддерживает интернационализацию. Мы приглашаем вас на интеграцию.

Эффект интерфейса chat-uikit-react-native показан ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2e7900faa26a11ef820f525400d5f8ef.png)

## Требования к окружению

- React Native 0.75.0
- [Node.js](https://nodejs.org/en/) версия 18+
- JDK 17
- Xcode версия 14.0 или выше
- Android Studio

## Настройка окружения разработки

Если вы разрабатываете проект React Native впервые, обратитесь к этапам официального сайта React Native [set-up-your-environment](https://reactnative.dev/docs/set-up-your-environment) для настройки среды разработки.

Если вы столкнулись с проблемами окружения при создании или компиляции проекта, вы можете запустить `npx react-native doctor` для диагностики окружения.

## Интеграция chat-uikit-react-native

### Шаг 1: Создание проекта (этот шаг можно пропустить, если у вас уже есть проект)

1. Создайте новый проект React Native.

```
npx @react-native-community/cli@latest init MyChatApp --version 0.75.0
```

2. После создания проекта перейдите в его директорию.

```
cd MyChatApp
```

### Шаг 2. Интеграция chat-uikit-react-native

- Загрузите [chat-uikit-react-native](https://www.npmjs.com/package/@tencentcloud/chat-uikit-react-native) через npm/yarn и используйте его в проекте. Вы также можете использовать его для вторичной разработки.

npm

yarn

```
npm install @tencentcloud/chat-uikit-react-native react-native-image-picker react-native-document-picker react-native-video
```

```
yarn add @tencentcloud/chat-uikit-react-native react-native-image-picker react-native-document-picker react-native-video
```

- Добавьте разрешения устройства

Android

iOS

Добавьте следующие разрешения в файл android/app/src/main/AndroidManifest.xml.

```
 <uses-permission android:name="android.permission.READ_MEDIA_ChatAGES" /> <uses-permission android:name="android.permission.READ_MEDIA_AUDIO" /> <uses-permission android:name="android.permission.READ_MEDIA_VIDEO" /> <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" /> <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

Добавьте следующее описание использования разрешений в файл info.plist.

```
  <key>NSCameraUsageDescription</key>    <string> we would like to use your camera</string>   <key>NSPhotoLibraryUsageDescription</key>    <string> we would like to use your photo library</string>  <key>NSMicrophoneUsageDescription</key>    <string>we would like to use your microphone</string>
```

### Шаг 3: Установка навигации

Установите зависимости React Navigation. Обратитесь к документации [React Navigation](https://reactnavigation.org/docs/getting-started).

npm

yarn

```
npm install @react-navigation/native@^6.1.18 react-native-screens@^3.34.0 react-native-safe-area-context @react-navigation/native-stack@^6.11.0
```

```
yarn add @react-navigation/native@^6.1.18 react-native-screens@^3.34.0 react-native-safe-area-context @react-navigation/native-stack@^6.11.0
```

### Шаг 4. Импорт chat-uikit-react-native

> **Примечание:** Следующий код не содержит SDKAppID, userID и userSig, которые должны быть заменены после получения соответствующей информации на Шаге 5. Чтобы уважать авторские права на дизайн эмодзи, проект Chat Demo/TUIKit не включает вырезки крупных элементов эмодзи. Пожалуйста, замените их на свои дизайны или другие наборы эмодзи, на которые у вас есть авторские права, перед официальным запуском в коммерческое использование. **Показанный ниже набор эмодзи улыбающегося лица по умолчанию защищен авторским правом Tencent RTC**, вы можете обновиться до [Chat Pro Plus Edition и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro) для бесплатного использования.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2e708462a26a11efa04c5254002693fd.png)

App.tsx

Screens.tsx

> **Примечание:** Код ниже не содержит `SDKAppID`, `userID` и `userSig`, которые должны быть заменены после получения соответствующей информации на **Шаге 5**.

Замените содержимое в App.tsx или создайте новый компонент для импорта.

```
import React from 'react';import {  View,  TouchableOpacity,  Text,  Image,  StyleSheet,} from 'react-native';import { NavigationContainer, useNavigation } from '@react-navigation/native';import { createNativeStackNavigator } from '@react-navigation/native-stack';import { UIKitProvider } from '@tencentcloud/chat-uikit-react-native';import resources from '@tencentcloud/chat-uikit-react-native/i18n';import { TUITranslateService } from '@tencentcloud/chat-uikit-engine';import { TUILogin } from '@tencentcloud/tui-core';import { ConversationListScreen, ChatScreen, ChatSettingScreen } from './Screens';const LoginScreen = () => {  const navigation = useNavigation<any>();  // Init localization  TUITranslateService.provideLanguages(resources);  TUITranslateService.useI18n('en-US');  // Login  const Login = () => {    TUILogin.login({      SDKAppID: 0, // Your SDKAppID      userID: 'test_1', // Login UserID      userSig: '', // Login userSig      useUploadPlugin: true,      framework: 'rn',    }).then(() => {      navigation.navigate('ConversationList');    });  }  return (    <View style={styles.container}>      <Image        style={styles.logo}        source={{uri:'https://web.sdk.qcloud.com/im/assets/images/tencent_rtc_logo.png'}}      />      <TouchableOpacity style={styles.buttonContainer} onPress={Login}>        <Text style={styles.buttonText}>Log in</Text>      </TouchableOpacity>    </View>  );};const Navigation = () => {  const Stack = createNativeStackNavigator();  return (    <NavigationContainer>      <Stack.Navigator        screenOptions={{ headerShown: false }}        initialRouteName="Login">        <Stack.Screen          name="Login"          component={LoginScreen} />        <Stack.Screen          name="ConversationList"          component={ConversationListScreen} />        <Stack.Screen          name="Chat"          component={ChatScreen} />        <Stack.Screen          name="ChatSetting"          component={ChatSettingScreen}/>      </Stack.Navigator>    </NavigationContainer>  );};const App = () => {  return (    <UIKitProvider>      <Navigation />    </UIKitProvider>  );};const styles = StyleSheet.create({  container: {    flex: 1,    justifyContent: 'center',    alignItems: 'center',    backgroundColor: '#FFFFFF',  },  logo: {    width: 232,    height: 80,  },  buttonContainer: {    width: '80%',    justifyContent: 'center',    alignItems: 'center',    paddingVertical: 11,    borderRadius: 5,    backgroundColor: '#2F80ED',  },  buttonText: {    fontSize: 18,    lineHeight: 24,    color: '#FFFFFF',  },});export default App;
```

Создайте новый файл Screens.tsx в той же директории, что и файл App.tsx.

```
import React from 'react';import { useNavigation } from '@react-navigation/native';import { ConversationList, Chat, ChatSetting } from '@tencentcloud/chat-uikit-react-native';export const ConversationListScreen = () => {  const navigation = useNavigation<any>();  const onPressConversation = () => {    navigation.navigate('Chat');  };  return (    <ConversationList onPressConversation={onPressConversation} />  );};export const ChatScreen = () => {  const navigation = useNavigation<any>();  const navigateBack = () => {    navigation.goBack();  };  const navigateToChatSetting = () => {    navigation.navigate('ChatSetting');  };  return (    <Chat      navigateBack={navigateBack}      navigateToChatSetting={navigateToChatSetting}    />  );};export const ChatSettingScreen = () => {  const navigation = useNavigation<any>();  // Navigate to Chat when you click header back button.  const navigateBack = () => {    navigation.goBack();  };  // Navigate to Chat when you click the send message button.  const navigateToChat = () => {    navigation.goBack();  };  // Navigate to ConversationList when you disband group or leave group.  const navigateToConversationList = () => {    navigation.navigate('ConversationList');  };  return (    <ChatSetting      navigateBack={navigateBack}      navigateToChat={navigateToChat}      navigateToConversationList={navigateToConversationList}    />  );};
```

### Шаг 5: Получение SDKAppID, userID и userSig

Получите соответствующие параметры SDKAppID, userID и соответствующий userSig из `Login`:

- `SDKAppID`, можно получить через [Chat Console](https://console.trtc.io/app) в разделе `Applications`:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2ec13858a26a11ef992f52540075b605.png)

- `userID`
  - Щелкните, чтобы открыть [Application](https://console.trtc.io/app), которое вы создали выше, вы увидите запись продукта `Chat` на левой боковой панели, щелкните, чтобы открыть ее.
  - После входа на подстраницу продукта Chat щелкните `Users`, чтобы открыть страницу управления пользователями.
  - Щелкните `Create account`, чтобы открыть диалоговое окно заполнения информации о создании учетной записи. Если это просто обычный участник, мы рекомендуем выбрать тип `General`.
  - **Для лучшего взаимодействия с обмена сообщениями и другими функциями рекомендуется создать два идентификатора пользователей (test_1, test_2)**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2e93b04da26a11efa04c52540055f650.png)

- `userSig` может быть сгенерирован в реальном времени с помощью инструментов разработки, предоставленных консолью. Для инструментов разработки щелкните [Chat Console > Development Tools > UserSig Tools > Signature (UserSig) Generator](https://console.trtc.io/usersig).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2e946583a26a11efaaca525400fdb830.png)

### Шаг 6: Компиляция и запуск проекта

- Для компиляции и запуска проекта необходимо использовать реальное устройство или эмулятор. Рекомендуется использовать реальное устройство. Вы можете обратиться к официальному сайту React Native [running-on-device](https://reactnative.dev/docs/running-on-device) для подключения реального устройства для отладки.
- Замените SDKAppID, userID, userSig в App.tsx, затем выполните следующую команду:

Android

iOS

1. Включите режим разработчика на телефоне и включите переключатель **USB Debugging**.
2. Подключите телефон кабелем USB, рекомендуется выбрать опцию **Transfering File**, **не выбирайте опцию Charge Only**.
3. После подтверждения успешного подключения телефона выполните `npm run android` для компиляции и запуска проекта.

```
npm run start
```

1. Подключите телефон кабелем USB и откройте директорию проекта ios с помощью Xcode.
2. Настройте информацию подписи согласно разделу [running-on-device](https://reactnative.dev/docs/running-on-device?platform=ios) официального сайта React Native.
3. Перейдите в директорию ios и установите зависимости.

```
cd iospod install
```

4. Вернитесь в корневую директорию и выполните npm run ios для компиляции и запуска проекта.

```
cd ../npm run start
```

## Шаг 7: Отправка первого сообщения

1. После запуска проекта нажмите Initiate Session в верхнем левом углу.
2. Откройте окно Initiate Session. В строке поиска введите идентификатор пользователя, созданный на Шаге 5 (**test_2**), выберите его и откройте сеанс.
3. Введите сообщение в поле ввода и нажмите отправить.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2e895f8aa26a11efa0b3525400bdab9d.png)

## Обмен информацией и обратная связь

Присоединитесь к [Telegram Technical Support Group](https://t.me/tencent_imsdk) или [WhatsApp Communication Group](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik) для получения поддержки от профессиональных инженеров для решения ваших проблем.

## Часто задаваемые вопросы

#### Что делать при возникновении ошибки среды выполнения?

Вы можете запустить следующую команду для диагностики окружения.

```
npx react-native doctor
```

## Документация

#### Относящаяся к UIKit:

- [chat-uikit-react-native npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-react-native)


---
*Источник: [https://trtc.io/document/56573](https://trtc.io/document/56573)*

---
*Источник (EN): [integration.md](./integration.md)*
