# Отправка вашего первого сообщения

Этот документ поможет вам интегрировать TUIKit или TUIChat и успешно отправить ваше первое сообщение.

Или, если вы предпочитаете более быстрый и автоматизированный подход, вы можете обратиться к [Начало работы с интеграцией AI](https://www.tencentcloud.com/document/product/1047/72277) для оптимизации процесса.

## Требования к окружению

- Xcode 10 или позже
- iOS 9.0 или позже
- CocoaPods 1.7.5 или позже

## Создание приложения

Перед интеграцией TUIKit вам необходимо перейти в [Консоль](https://console.trtc.io/) и создать новое приложение Chat следующим образом:

1. [Зарегистрируйте аккаунт Tencent Cloud](https://trtc.io/zh/register?s_url=https://console.trtc.io) и добавьте способ оплаты.
2. Войдите в [консоль Chat](https://console.trtc.io) и нажмите **Создать приложение**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c483245cc2811f091ab5254007c27c5.png)

3. Введите имя приложения в диалоговом окне создания и выберите **Chat**, выберите соответствующий **Регион развертывания**, затем нажмите **Создать**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c441a71cc2811f0afdc52540044a08e.png)

4. После создания вы можете просмотреть статус приложения, версию сервиса, SDKAppID, SDKSecretKey, время создания и время истечения на текущей [**странице сведений о продукте Chat**](https://console.trtc.io/chat) или [**Мои приложения**](https://console.trtc.io/app).

> **Примечание:** Версия сервиса нового приложения по умолчанию — это пробная версия, и статус включен по умолчанию. Один аккаунт Tencent Cloud может создать до 300 приложений Chat. Если у вас уже есть 300 приложений, вы можете сначала [деактивировать и удалить](https://www.tencentcloud.com/document/product/1047/34540#357049f6-9802-456e-8f51-755d906f014a) неиспользуемые приложения перед созданием новых. **После удаления приложения все данные и услуги, соответствующие SDKAppID, не могут быть восстановлены. Будьте осторожны.**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c5aa77ccc2811f0afdc52540044a08e.png)

## Создание аккаунтов

Создание приложения гарантирует только нормальную инициализацию SDK. Чтобы успешно отправлять сообщения, вам также необходимо создать учетные записи пользователей в приложении. Существует множество способов создания аккаунтов, например прямо в консоли или через регистрацию клиента API. Вы можете выбрать любой подходящий метод.

> **Примечание:** Отправка сообщений требует взаимодействия как минимум двух пользователей, поэтому вам необходимо создать как минимум 2 аккаунта для этого шага. Пожалуйста, запомните userID этих 2 аккаунтов, так как они будут использоваться на следующих шагах.

**Вариант A: Создание в консоли**

> **Примечание:** Для получения дополнительной информации об операциях с аккаунтами см. [Управление аккаунтами](https://www.tencentcloud.com/document/product/1047/50301).

1. Войдите в [консоль Chat](https://console.trtc.io), выберите **Chat >** [**Пользователи**](https://console.trtc.io/chat/account-management) в левой боковой панели и выберите целевое приложение **вверху**.
2. На странице управления аккаунтом нажмите Создать аккаунт.
3. В диалоговом окне Создать аккаунт настройте следующие параметры:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c4a90fdcc2811f093295254001c06ec.png)

  - Тип аккаунта: Чувствителен к регистру для обычного и административного аккаунта. "Администратор приложения" — это роль с наивысшим уровнем привилегий для приложения, позволяющая вызывать API RESTful для выполнения операций, таких как создание/расформирование групп и отправка сообщений всем пользователям. Каждое приложение поддерживает конфигурацию до 10 администраторов.
  - Имя пользователя: Введите имя пользователя (UserID), обязательно.
  - Никнейм пользователя: Введите никнейм пользователя, опционально.
  - Аватар: Введите URL аватара пользователя, опционально.
4. Нажмите **Подтвердить** для сохранения конфигурации.
5. После создания аккаунта вы можете просмотреть имя пользователя, никнейм, тип аккаунта, аватар и время создания в списке аккаунтов.

**Вариант B: Создание аккаунтов при входе**

Для регистрации через клиент просто введите совершенно новый UserID в разделе [Вход в TUIKit](#288b702c-cc18-4c33-976d-af38aabcac80) ниже. При этом TUIKit автоматически зарегистрирует UserID для вас.

## Генерация UserSig

> **Примечание:** Для получения дополнительной информации об операциях, связанных с UserSig, обратитесь к [Генерация и проверка UserSig](https://www.tencentcloud.com/document/product/1047/34580#usersig-.E7.94.9F.E6.88.90.26.E6.A0.A1.E9.AA.8C).

1. Войдите в [консоль Chat > Инструменты разработки > Инструменты UserSig](https://console.trtc.io/usersig).
2. В разделе инструмента генерации UserSig **выберите приложение** и **вручную введите UserID**.
3. Нажмите **Генерировать подпись (UserSig)** для создания подписи. Период действия подписи по умолчанию составляет 180 дней.
4. Нажмите **Копировать подпись (UserSig)** для вставки и сохранения подписи.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c5058a4cc2811f091ab5254007c27c5.png)

## Интеграция TUIKit

Функция отправки сообщений в чат-взаимодействиях реализована с помощью `TUIChat`. Вам необходимо интегрировать как минимум `TUIChat` для правильной отправки и получения сообщений. Другие компоненты, такие как `TUIConversation`, `TUIContact` и `TUIGroup`, можно интегрировать по мере необходимости.

- Если вам нужны несколько компонентов пользовательского интерфейса, вы можете интегрировать TUIKit. Подробнее см. [Интеграция TUIKit](https://www.tencentcloud.com/document/product/1047/50056#cocoapods-.E9.9B.86.E6.88.90).
- Если вам нужно интегрировать только TUIChat, см. [Интеграция только TUIChat](https://www.tencentcloud.com/document/product/1047/60169).

## Вход в TUIKit

TUILogin предоставляет API для входа в TUIKit, как следует:

```
// API location: TUICore/TUILogin.h+ (void)login:(int)sdkAppID userID:(NSString *)userID userSig:(NSString *)userSig succ:(__nullable TSucc)succ fail:(__nullable TFail)fail;
```

Этот API требует три параметра:

- SDKAppID, SDKAppID созданного нового приложения, был получен на предыдущем шаге [Создание приложения](#91aad40c-f055-48a6-b64b-c507d16cad7f).
- UserID, UserID пользователя 1, был получен на предыдущем шаге [Создание аккаунта](#bafe82cd-d58d-4d09-956d-c318e2e49bc5). Обратите внимание, что это не NickName пользователя.
- UserSig, UserSig пользователя 1, был получен в контексте [Генерация UserSig](#1678b9aa-cc39-49ab-8a9d-d5e8857df988).

Пример:

Swift

Objective-C

```
#pragma mark - Life cyclefunc application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {        TUILogin.login(Int32(SDKAPPID), userID: userID, userSig: userSig, config: loginConfig, succ:{            //Success        }, fail: { code, msg in            //Failed        })        return true}
```

```
#pragma mark - Life cycle- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {    [TUILogin login:SDKAPPID userID:self.userID userSig:self.userSig config:self.loginConfig succ:^{        //Success    } fail:^(int code, NSString *msg) {        //Failed    }];    return YES;}
```

## Переход к интерфейсу чата

Для отправки сообщений следующий шаг:

1. Используйте один из ранее зарегистрированных аккаунтов (далее называется user1) для входа в TUIKit, и user1 выходит в сеть.
2. User1 отправляет сообщение другому аккаунту (далее называется user2). User2 не нужно входить и не нужно быть друзьями с user1.

> **Примечание:** Следующие шаги объясняют, как отправить сообщение user2 после входа как user1. Если вы хотите, чтобы user1 и user2 взаимодействовали через чат, вам необходимо использовать те же шаги для входа как user2 и входа в интерфейс чата с user1.

Вы можете перенаправить или вложить интерфейс чата в обратный вызов успешного входа user1 для отправки сообщения user2.

Пример кода ниже, где userID должен быть userID user2.

Swift

Objective-C

```
// Pass userID for 1v1 conversation.func pushToChatViewController(groupID: String?, userID: String?) {    // Create conversationData.    let conversationData = TUIChatConversationModel()    conversationData.userID = userID        // Create c2c chatVC.    let chatVC = TUIC2CChatViewController_Minimalist()    chatVC.conversationData = conversationData        // Option 1: navigate to chatVC.    navigationController?.pushViewController(chatVC, animated: true)    // Option 2: add chatVC as a childVC to your parent VC.    // addChild(chatVC)    // view.addSubview(chatVC.view)}
```

```
// Pass userID for 1v1 conversation.- (void)pushToChatViewController:(NSString *)groupID userID:(NSString *)userID {    // Create conversationData.    TUIChatConversationModel *conversationData = [[TUIChatConversationModel alloc] init];    conversationData.userID = userID;        // Create c2c chatVC.    TUIBaseChatViewController_Minimalist *chatVC = [[TUIC2CChatViewController_Minimalist alloc] init];    chatVC.conversationData = conversationData;        // Option 1: navigate to chatVC.    [self.navigationController pushViewController:chatVC animated:YES];    // Option 2: add chatVC as a childVC to your parent VC.    // [self addChildViewController:vc];    // [self.view addSubview:vc.view];}
```

## Отправка вашего первого сообщения

После завершения предыдущих шагов вы можете перейти к интерфейсу чата, показанному ниже. Быстро и вручную нажмите на поле ввода для отправки вашего первого сообщения:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cea1842b2c8c11ef9130525400bf8054.png)

## Свяжитесь с нами

Если у вас есть какие-либо вопросы по этой статье, не стесняйтесь присоединиться к [группе технической поддержки Telegram](https://t.me/+EPk6TMZEZMM5OGY1), где вы получите надежную техническую поддержку.


---
*Источник: [https://trtc.io/document/60521](https://trtc.io/document/60521)*

---
*Источник (EN): [sending-your-first-message.md](./sending-your-first-message.md)*
