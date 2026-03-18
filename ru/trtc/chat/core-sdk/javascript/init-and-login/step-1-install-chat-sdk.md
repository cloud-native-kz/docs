# Шаг 1: Установка Chat SDK

Этот документ описывает способы быстрой интеграции Tencent Cloud Chat SDK в ваши проекты web, мини-программы, uni-app и React Native.

## Структура файлов Chat SDK

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/460419721a5311ee909c525400cea498.png)

## Интеграция SDK

- Вы можете интегрировать Chat SDK в ваши проекты web, мини-программы и uni-app, используя npm.
- Вы можете интегрировать плагин загрузки [tim-upload-plugin](https://www.npmjs.com/package/tim-upload-plugin) для более быстрой и безопасной загрузки ресурсов мультимедиа.

### Интеграция через npm (Рекомендуется)

Используйте npm для установки соответствующих зависимостей Chat SDK в вашем проекте.

```
npm install @tencentcloud/chat --save// Плагин загрузки Tencent Cloud Chat необходим для отправки сообщений, таких как изображения и файлы.npm install tim-upload-plugin --save
```

```
import TencentCloudChat from '@tencentcloud/chat';import TIMUploadPlugin from 'tim-upload-plugin';let options = {  SDKAppID: 0 // Замените 0 на SDKAppID вашего приложения Chat при подключении.};// Создайте экземпляр SDK.// Метод `TencentCloudChat.create()` возвращает один и тот же экземпляр для одного и того же `SDKAppID`.// Экземпляр SDK обычно представлен как chat.let chat = TencentCloudChat.create(options);// Установите уровень логирования SDK.// 0: обычный уровень. Рекомендуется использовать этот уровень при интеграции, так как он охватывает больше логов.// 1: уровень релиза. Рекомендуется использовать этот уровень для ключевой информации в производственной среде.chat.setLogLevel(0);// chat.setLogLevel(1);// Зарегистрируйте плагин загрузки Tencent Cloud Chat.chat.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});
```

### **Установка уровня логирования**

Установите уровень логирования. Логи ниже указанного уровня не будут выводиться.

##### **API**

```
chat.setLogLevel(level);
```

| Имя | Тип | Описание |
| --- | --- | --- |
| level | Number | Уровни логирования: 0 - обычный уровень с большим объемом логов. Рекомендуется использовать при интеграции. 1 - уровень релиза, SDK выводит ключевую информацию. Рекомендуется использовать в производственных средах. 2 - уровень предупреждения, SDK выводит только логи уровня предупреждения и ошибки. 3 - уровень ошибки, SDK выводит только логи уровня ошибки. 4 - без логирования, SDK не будет печатать никакие логи. |

##### **Примеры**

```
chat.setLogLevel(0);
```

### **Регистрация плагинов**

> **Примечание:** Для отправки сообщений, таких как изображения, голос, видео и файлы, вам необходимо использовать плагин загрузки `tim-upload-plugin` для загрузки файлов в хранилище объектов Tencent Cloud. При использовании `tim-upload-plugin` в проекте React Native вам необходимо обновить `tim-upload-plugin` до версии v1.3.1 или выше. Кроме того, для улучшения пользовательского опыта в условиях плохой сети или при переключении сети вам необходимо зарегистрировать плагин мониторинга статуса сети `@react-native-community/netinfo`. Для отправки сообщений с мультимедиа в приложение React Native вам необходимо добавить разрешения: Добавьте следующие разрешения в `AndroidManifest.xml` в проекте Android: <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" /> <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" /> <uses-permission android:name="android.permission.RECORD_AUDIO" /> Добавьте следующие разрешения в `Info.plist` в проекте iOS: <key>NSCameraUsageDescription</key><string>Нам нужен доступ к вашей камере для съемки фотографий</string><key>NSPhotoLibraryUsageDescription</key><string>Нам нужен доступ к вашей фотогалерее для выбора фотографий</string><key>NSMicrophoneUsageDescription</key><string>Нам нужен доступ к вашему микрофону для записи аудио</string>

##### **API**

```
chat.registerPlugin(options);
```

Параметр `options` имеет тип `Object`. Он содержит следующие значения атрибутов:

| Имя | Тип | Описание |
| --- | --- | --- |
| key | String | Имя плагина. |
| value | Class | Класс плагина. |

##### **Примеры**

```
chat.registerPlugin({'tim-upload-plugin': TIMUploadPlugin});
```

```
// Зарегистрируйте плагин мониторинга статуса сети в проекте React Native.npm install @react-native-community/netinfo --save import NetInfo from "@react-native-community/netinfo";chat.registerPlugin({'chat-network-monitor': NetInfo});
```

**Следующий шаг:** [**инициализация Chat SDK**](https://trtc.io/document/47967?platform=web&product=chat&menulabel=sdk)**.**

### Соответствующие ресурсы

- [Логи обновлений SDK](https://intl.cloud.tencent.com/document/product/1047/34281)
- [API SDK](https://www.tencentcloud.com/document/product/1047/33999)

## Часто задаваемые вопросы

**Есть ли открытые компоненты пользовательского интерфейса, которые можно переиспользовать или переделать?**
Tencent Cloud Chat предоставляет открытые UIKit для всех платформ, которые разработчики могут переиспользовать или переделать. Документация с подробной информацией доступна ниже:

- [Быстрый старт (React)](https://trtc.io/document/50055?platform=web&product=chat)
- [Быстрый старт (Vue)](https://trtc.io/document/58644?platform=web&product=chat)


---
*Источник: [https://trtc.io/document/34309](https://trtc.io/document/34309)*

---
*Источник (EN): [step-1-install-chat-sdk.md](./step-1-install-chat-sdk.md)*
