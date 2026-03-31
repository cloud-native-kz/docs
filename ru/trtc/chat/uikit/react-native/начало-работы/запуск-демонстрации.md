# Запуск демонстрации

chat-uikit-react-native — это библиотека компонентов пользовательского интерфейса React Native, основанная на Tencent Cloud Chat SDK. Она предоставляет универсальные компоненты пользовательского интерфейса, включая функции разговоров, чата и групп. С помощью этих хорошо разработанных компонентов пользовательского интерфейса вы можете быстро создавать элегантные, надежные и масштабируемые приложения для чата. Интерфейс UIKit, разработанный с помощью React Native, лучше соответствует привычкам использования зарубежных клиентов и поддерживает интернационализацию. Если ваш бизнес нуждается в расширении за границей, мы приглашаем вас его интегрировать. Подробнее см. в [открытом исходном коде](https://github.com/TencentCloud/chat-demo-react-native).

Эффект интерфейса chat-uikit-react-native показан ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/036274b3b8fa11efa1ff525400bdab9d.png)

## Предварительные требования

### Включение сервиса

1. Войдите в [консоль Chat](https://console.trtc.io/), перейдите на страницу **управления приложением** и нажмите **Создать новое приложение**. Если у вас уже есть приложение, вы можете пропустить процесс создания приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6d6cbd15c07911f0a6dd5254005ef0f7.png)

2. На странице **управления приложением** получите SDKAppID и информацию о ключе из столбца SDKAppID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6d51e946c07911f0b4a7525400454e06.png)

> **Примечание:** Просмотр информации о ключе требует проверки личности. Информация о ключе — это конфиденциальная информация. Чтобы предотвратить несанкционированное использование, храните её в безопасности и защищайте от утечек.

3. [Перейдите на страницу управления пользователями](https://console.trtc.io/chat/account-management), создайте 2–3 тестовых учётных записи для демонстрации возможностей чата C2C и группового чата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6ccd717cc07911f08c0e52540044a08e.png)

4. Информация о userSig. Нажмите [Консоль Chat > Средства разработки > Инструмент userSig](https://console.trtc.io/usersig), введите созданный userID для создания userSig.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6cf1125dc07911f0a6dd5254005ef0f7.png)

### Требования к среде разработки

- React Native 0.75.0
- [Node.js](https://nodejs.org/en/) версия 18+
- Xcode версия 14.0 или выше
- Android Studio

### Настройка среды разработки

Если вы разрабатываете проект React Native в первый раз, обратитесь к инструкциям на официальном веб-сайте React Native [set-up-your-environment](https://reactnative.dev/docs/set-up-your-environment) для настройки среды разработки.

Если вы столкнётесь с проблемами среды при создании или компиляции проекта, вы можете выполнить `npx react-native doctor` для диагностики среды.

## Загрузка демонстрации

```
git clone https://github.com/TencentCloud/chat-demo-react-native
```

```
cd chat-demo-react-native/Demo
```

Установка с помощью `npm`

```
npm i --legacy-peer-deps
```

## Настройка демонстрации

> **Примечание:** Чтобы соблюдать авторские права на дизайн эмодзи, проект Chat Demo/TUIKit не включает обрезки больших элементов эмодзи. Перед официальным запуском для коммерческого использования замените их своими дизайнами или другими пакетами эмодзи, на которые у вас есть авторские права. **Показанный ниже пакет эмодзи со смайликом по умолчанию защищён авторским правом Tencent RTC**, вы можете обновиться до [Chat Pro Plus Edition и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro) для использования без дополнительной оплаты.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d1eda06a9aa611f0bf2352540044a08e.png)

1. Откройте проект Demo, файл GenerateTestUserSig.js в каталоге ./debug.
2. Установите `SDKAPPID` и `SECRETKEY` в файле `GenerateTestUserSig.js`, которые можно получить из [Консоли Chat](https://console.trtc.io/). Нажмите на карточку целевого приложения, чтобы перейти на его страницу конфигурации.

```
const SDKAppID = 0; // numberconst SECRETKEY = 'xxx'; // stringconst APPKey = 'xxx'; // string, and For Offline Push only, optional to fill in.
```

## Запуск демонстрации

- Для компиляции и запуска проекта необходимо использовать реальное устройство или эмулятор. Рекомендуется использовать реальное устройство. Вы можете обратиться к официальному веб-сайту React Native [running-on-device](https://reactnative.dev/docs/running-on-device) для подключения реального устройства для отладки.

Android

iOS

1. Включите режим разработчика на телефоне и включите переключатель **USB Debugging**.
2. Подключите телефон кабелем USB, рекомендуется выбрать опцию **Transferring File**, **не выбирайте опцию Charge Only**.
3. После подтверждения успешного подключения телефона выполните `npm run android` для компиляции и запуска проекта.

```
npm run android
```

1. Подключите телефон кабелем USB и откройте директорию проекта ios с помощью Xcode.
2. Настройте информацию подписания в соответствии с разделом [running-on-device](https://reactnative.dev/docs/running-on-device?platform=ios) на официальном веб-сайте React Native.
3. Перейдите в директорию ios и установите зависимости.

```
cd iospod install
```

4. Вернитесь в корневую директорию и выполните npm run ios для компиляции и запуска проекта.

```
cd ../npm run ios
```

## Отправка первого сообщения

1. После запуска проекта нажмите Initiate Session в левом верхнем углу.
2. Введите окно инициации разговора. В строке поиска введите созданный userID из шага 2 (**test_2**), выберите его и откройте разговор.
3. Введите сообщение в поле ввода и нажмите отправить.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/03c6e4f6b8fa11ef86025254002693fd.png)

## Часто задаваемые вопросы

1. Если при запуске npm run android вы столкнётесь с ошибкой, показанной на рисунке, переустановите переменные среды в корневой директории проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0368a004b8fa11ef89f2525400d5f8ef.png)

```
export ANDROID_HOME=$HOME/Library/Android/sdkexport PATH=$PATH:$ANDROID_HOME/emulatorexport PATH=$PATH:$ANDROID_HOME/platform-tools
```

2. Если при выполнении команды Build в Xcode вы столкнётесь с проблемами переменных среды node, выполните следующие шаги:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/03ebc4ccb8fa11ef86025254002693fd.png)

```
cd iosecho export NODE_BINARY=$(command -v node) > .xcode.env
```

## Справочная документация

- [chat-uikit-react-native npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-react-native)
- [Документация по быстрой интеграции UIKit](https://www.tencentcloud.com/document/product/1047/56573)
- [Руководство по API chat-uikit-engine](https://web.sdk.qcloud.com/im/doc/chat-engine/index.html)
- [chat-uikit-engine npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-engine)


---
*Источник: [https://trtc.io/document/52397](https://trtc.io/document/52397)*

---
*Источник (EN): [run-demo.md](./run-demo.md)*
