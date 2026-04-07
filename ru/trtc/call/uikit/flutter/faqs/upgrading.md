# Обновление

## Инструкции по обновлению

**TUICallKit** — это новый компонент пользовательского интерфейса для аудио- и видеовызовов, разработанный Tencent Cloud. Это обновленная версия TUICalling, которая поддерживает больше функциональных возможностей, таких как групповые вызовы и подавление шума с помощью ИИ, и обеспечивает вызовы между всеми платформами с большей стабильностью. Мы приглашаем вас использовать новый компонент TUICallKit. Перед обновлением обратите внимание на следующее:

- TUICalling и TUICallKit поддерживают взаимные вызовы. Пожалуйста, сохраните SDKAppID неизменным до и после обновления, иначе это может повлиять на взаимное общение.
- TUICallKit необходимо использовать вместе с пакетом возможностей аудио- и видеовызовов IM. Вы можете перейти в [консоль IM](https://console.tencentcloud.com/im), открыть страницу **Базовая конфигурация** соответствующего приложения SDKAppID и найти область функции Вызов в нижней правой части страницы. Нажмите **Попробуйте сейчас**, чтобы открыть 7-дневный бесплатный пробный период TUICallKit. Если вы хотите официально запустить приложение, нажмите **Купить**, чтобы перейти на [страницу покупки](https://buy.tencentcloud.com/avc).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3c206347b5f511eeb395525400461a83.png)

> **Примечание:** Возможность аудио- и видеовызовов IM предоставляет дифференцированные платные версии для различных бизнес-потребностей, и вы можете узнать о включенных функциях и приобрести подходящую вам версию на [странице покупки IM](https://buy.tencentcloud.com/avc).

## Этапы обновления

TUICallKit был разработан с учетом потребностей обновления для клиентов TUICalling и может быть обновлен всего в два простых этапа, что займет примерно 20 минут:

### Обновление зависимостей до TUICallKit

Завершите обновление зависимостей до TUICallKit в вашем проекте и установите файл конфигурации **pubspec.yaml** для вашего проекта:

```
dependencies:  # Remove the old dependency tim_ui_kit_calling_plugin and add the new dependency tencent_calls_uikit:  tencent_calls_uikit:
```

После установки выполните команду `flutter pub get`.

> **Примечание:** Если вы ранее использовали компоненты IM, такие как TUIChat и TUIContact, вы можете использовать TUICallKit нормально после завершения этого этапа. Логика совместимости обработана внутри компонента TUICallKit.

### 2. Изменение использования API

После выполнения описанных выше шагов ваш проект не будет скомпилирован нормально. Вам необходимо заменить API TUICalling на новый API TUICallKit. Вы можете обратиться к следующей информации сравнения API и найти и заменить её.

| Значение API | TUICalling(tim_ui_kit_calling_plugin) | TUICallKit(tencent_calls_uikit) | Объяснение |
| --- | --- | --- | --- |
| Создание экземпляра TUICallKit | TUICalling.sharedInstance | TUICallKit.[instance](https://trtc.io/document/46660/51002/54904/54906) | Замените ссылку и имя. |
| Установка никнейма пользователя | TUICalling.setUserNickname | TUICallKit.[setSelfInfo](https://trtc.io/document/46660/51002/54904/54906#setSelfInfo) | Объедините интерфейс для установки аватара и никнейма в интерфейс setSelfInfo. |
| Установка аватара пользователя | TUICalling.setUserAvatar | TUICallKit.[setSelfInfo](https://trtc.io/document/46660/51002/54904/54906#setSelfInfo) | Объедините интерфейс для установки аватара и никнейма в интерфейс setSelfInfo. |
| Инициирование вызова 1v1 | TUICalling.call | TUICallKit.[call](https://trtc.io/document/46660/51002/54904/54906#call) | Подробности см. в разделе об изменениях интерфейса TUICalling.call. |
| Инициирование группового вызова | / | TUICallKit.[groupCall](https://trtc.io/document/46660/51002/54904/54906#groupCall) | / |
| Активное присоединение к текущему групповому вызову | / | TUICallKit.[joinInGroupCall](https://trtc.io/document/46660/51002/54904/54906#joinInGroupCall) | / |
| Установка пользовательского рингтона | TUICalling.setCallingBell | TUICallKit.[setCallingBell](https://trtc.io/document/46660/51002/54904/54906) | Замените ссылку и имя. |
| Включение/отключение режима без звука | TUICalling.enableMuteMode | TUICallKit.[enableMuteMode](https://trtc.io/document/46660/51002/54904/54906#enableMuteMode) | Замените ссылку и имя. |
| Включение/отключение функции плавающего окна | TUICalling.enableFloatWindow | TUICallKit.[enableFloatWindow](https://trtc.io/document/46660/51002/54904/54906#enableFloatWindow) | Замените ссылку и имя. |
| Установка слушателя | TUICalling.registerListener | TUICallEngine.[addObserver](https://trtc.io/document/46660/51002/54904/54907#addobserver) | Подробности см. в разделе об изменениях интерфейса TUICalling.registerListener. |

Вот решения адаптации для двух API, которые значительно изменились во время этого обновления:

#### Изменения интерфейса TUICalling.call

- **Пример кода TUICalling:**

```
// Original InterfaceFuture<void> call(String userId, CallingScenes type, [OfflinePushInfo? offlinePushInfo]);
```

- **Пример кода TUICallKit:**

```
// New InterfaceFuture<void> call(String userId, TUICallMediaType callMediaType, [TUICallParams? params]);// New Calling MethodTUIOfflinePushInfo offlinePushInfo = TUIOfflinePushInfo();offlinePushInfo.title = "Flutter TUICallKit";offlinePushInfo.desc = "This is an incoming call from Flutter TUICallkit";TUICallParams params = TUICallParams(offlinePushInfo: offlinePushInfo);TUICallKit.instance.call(callUserId, TUICallMediaType.audio, params);
```

#### Изменения интерфейса TUICallKit.setCallingListener

- **Пример кода TUICalling:**

```
TUICalling.sharedInstance().registerListener(TUICallingListener(    onInvited: (params) {    }    onCallingCancel: () {    }    …));
```

- **Пример кода TUICallKit:**

```
TUICallEngine.instance.addObserver(TUICallObserver(    onError:(int code, String message) {    },     onCallCancelled: (String callerId) {    },    onCallBegin:(TUIRoomId roomId, TUICallMediaType callMediaType, TUICallRole callRole) {    },    …));
```

После обновления вышеуказанных API вы можете использовать компонент `TUICallKit` нормально.


---
*Источник: [https://trtc.io/document/58626](https://trtc.io/document/58626)*

---
*Источник (EN): [upgrading.md](./upgrading.md)*
