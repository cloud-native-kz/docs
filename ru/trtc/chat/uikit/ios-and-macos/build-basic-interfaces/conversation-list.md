# Список беседы

Эта статья проведет вас через процесс создания интерфейса списка бесед.

## Эффект отображения

Эффект списка бесед показан ниже:

### ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/df6480772c7811ef9130525400bf8054.png)

## Требования к окружению

- Xcode 10 или более поздняя версия
- iOS 9.0 или более поздняя версия

## Предварительные условия

Перед созданием интерфейса убедитесь, что вы завершили следующие 4 пункта:

1. Создали приложение в консоли.
2. Создали учетные записи пользователей в консоли.
3. Интегрировались с `TUIKit` или `TUIConversation`.
4. Вызвали API `login` в `TUILogin` для входа в компонент.

> **Примечание:** Все компоненты используют этот API для входа. Вы можете входить один раз каждый раз при запуске приложения. Убедитесь, что вход выполнен успешно, и мы рекомендуем выполнить следующее в обратном вызове успешного входа.

Если вы не завершили вышеуказанные 4 шага, пожалуйста, сначала обратитесь к соответствующим шагам в [Начало работы](https://www.tencentcloud.com/document/product/1047/60521), иначе вы можете столкнуться с препятствиями при реализации следующих функций.

Если вы их уже завершили, пожалуйста, продолжайте чтение ниже.

## Инструкции по шагам

Создание списка бесед обычно включает следующие 3 шага:

1. Загрузить список бесед. Список соответствует объекту `TUIConversationListController`. После загрузки `TUIConversationListController` автоматически получит недавние беседы.
2. Когда пользователь нажимает на строку в списке бесед, `TUIConversationListController` запускает событие `didSelectConversation`.
3. Ответить на нажатие в `didSelectConversation`, что обычно означает переход в интерфейс чата для этой беседы.

Пример кода:

Минималистичная версия

Классическая версия

Swift

Objective-C

```
import UIKit// ConversationController is your own ViewControllerclass ConversationController: UIViewController {    override func viewDidLoad() {        super.viewDidLoad()        // TUIConversationListController_Minimalist        let vc = TUIConversationListController_Minimalist()        vc.delegate = self                // Option 1: push vc.        navigationController?.pushViewController(vc, animated: true)        // Option 2: Add TUIConversationListController_Minimalist to your own ViewController        // addChild(vc)        // view.addSubview(vc.view)    }}extension ConversationController: TUIConversationListControllerListener {    func conversationListController(_ conversationController: UIViewController, didSelectConversation conversation: TUIConversationCellData) -> Bool {        // Conversation list click event, typically, opening the chat UI        let conversationData = TUIChatConversationModel()        conversationData.userID = conversation.userID        conversationData.title = conversation.title        conversationData.faceUrl = conversation.faceUrl                // Create chatVC by groupID or userID.        var chatVC: TUIBaseChatViewController_Minimalist?                if let groupID = conversationData.groupID, !groupID.isEmpty {            chatVC = TUIGroupChatViewController_Minimalist()        } else if let userID = conversationData.userID, !userID.isEmpty {            chatVC = TUIC2CChatViewController_Minimalist()        }                chatVC?.conversationData = conversationData                // Option 1: push chatVC.        navigationController?.pushViewController(chatVC!, animated: true)        // Option 2: add chatVC to your own ViewController.        // addChild(chatVC!)        // view.addSubview(chatVC!.view)    }}
```

```
#import "TUIConversationListController_Minimalist.h"#import "TUIBaseChatViewController_Minimalist.h"#import "TUIGroupChatViewController_Minimalist.h"#import "TUIC2CChatViewController_Minimalist.h"// ConversationController is your own ViewController@implementation ConversationController- (void)viewDidLoad {    [super viewDidLoad];    // TUIConversationListController_Minimalist    TUIConversationListController_Minimalist *vc = [[TUIConversationListController_Minimalist alloc] init];    vc.delegate = self;        // Option 1: push vc.    [self.navigationController pushViewController:vc animated:YES];    // Option 2: Add TUIConversationListController_Minimalist to your own ViewController    // [self addChildViewController:vc];    // [self.view addSubview:vc.view];}- (void)conversationListController:(TUIConversationListController_Minimalist *)conversationController             didSelectConversation:(TUIConversationCellData *)conversation {    // Conversation list click event, typically, opening the chat UI    TUIChatConversationModel *conversationData = [TUIChatConversationModel new];    conversationData.userID = conversation.userID;    conversationData.title = conversation.title;    conversationData.faceUrl = conversation.faceUrl;        // Create chatVC by groupID or userID.    TUIBaseChatViewController_Minimalist *chatVC = nil;    if (conversationData.groupID.length > 0) {        chatVC = [[TUIGroupChatViewController_Minimalist alloc] init];    } else if (conversationData.userID.length > 0) {        chatVC = [[TUIC2CChatViewController_Minimalist alloc] init];    }    chatVC.conversationData = conversationData;        // Option 1: push chatVC.    [self.navigationController pushViewController:chatVC animated:YES];    // Option 2: add chatVC to your own ViewController.    // [self addChildViewController:vc];    // [self.view addSubview:vc.view];}@end
```

Swift

Objective-C

```
import UIKit// ConversationController is your own ViewControllerclass ConversationController: UIViewController {    override func viewDidLoad() {        super.viewDidLoad()        // TUIConversationListController        let vc = TUIConversationListController()        vc.delegate = self                // Option 1: push vc.        navigationController?.pushViewController(vc, animated: true)        // Option 2: Add TUIConversationListController to your own ViewController        // addChild(vc)        // view.addSubview(vc.view)    }}extension ConversationController: TUIConversationListControllerListener {    func conversationListController(_ conversationController: UIViewController, didSelectConversation conversation: TUIConversationCellData) -> Bool {        // Conversation list click event, typically, opening the chat UI        let conversationData = TUIChatConversationModel()        conversationData.userID = conversation.userID        conversationData.title = conversation.title        conversationData.faceUrl = conversation.faceUrl                // Create chatVC by groupID or userID.        var chatVC: TUIBaseChatViewController?                if let groupID = conversationData.groupID, !groupID.isEmpty {            chatVC = TUIGroupChatViewController()        } else if let userID = conversationData.userID, !userID.isEmpty {            chatVC = TUIC2CChatViewController()        }                chatVC?.conversationData = conversationData                // Option 1: push chatVC.        navigationController?.pushViewController(chatVC!, animated: true)        // Option 2: add chatVC to your own ViewController.        // addChild(chatVC!)        // view.addSubview(chatVC!.view)    }}
```

```
#import "TUIConversationListController.h"#import "TUIBaseChatViewController_Minimalist.h"#import "TUIGroupChatViewController.h"#import "TUIC2CChatViewController.h"// ConversationController is your own ViewController@implementation ConversationController- (void)viewDidLoad {    [super viewDidLoad];    // TUIConversationListController    TUIConversationListController *vc = [[TUIConversationListController alloc] init];    vc.delegate = self;        // Option 1: push vc.    [self.navigationController pushViewController:vc animated:YES];    // Option 2: Add TUIConversationListController to your own ViewController    // [self addChildViewController:vc];    // [self.view addSubview:vc.view];}- (void)conversationListController:(TUIConversationListController *)conversationController             didSelectConversation:(TUIConversationCellData *)conversation {    // Conversation list click event, typically, opening the chat UI    TUIChatConversationModel *conversationData = [TUIChatConversationModel new];    conversationData.userID = conversation.userID;    conversationData.title = conversation.title;    conversationData.faceUrl = conversation.faceUrl;        // Create chatVC by groupID or userID.    TUIBaseChatViewController *chatVC = nil;    if (conversationData.groupID.length > 0) {        chatVC = [[TUIGroupChatViewController alloc] init];    } else if (conversationData.userID.length > 0) {        chatVC = [[TUIC2CChatViewControlleralloc] init];    }    chatVC.conversationData = conversationData;        // Option 1: push chatVC.    [self.navigationController pushViewController:chatVC animated:YES];    // Option 2: add chatVC to your own ViewController.    // [self addChildViewController:vc];    // [self.view addSubview:vc.view];}@end
```

> **Примечание:** Если вы ранее не отправляли сообщения никому и ни в одну группу, беседа не будет создана. В этом случае загрузка `TUIConversationListController` будет показывать пустой список. Для лучшего опыта рекомендуется сначала отправить сообщения некоторым учетным записям, чтобы запустить создание бесед. Если вы хотите узнать, как отправлять сообщения в интерфейсе чата, пожалуйста, обратитесь к документу: [Создание интерфейса чата](https://www.tencentcloud.com/document/product/1047/61215#).

## Дополнительные практики

Вы можете локально [запустить исходный код TUIKitDemo](https://www.tencentcloud.com/document/product/1047/45913), чтобы изучить больше реализаций интерфейсов.

## Свяжитесь с нами

Если у вас есть вопросы по этой статье, присоединяйтесь к [Telegram Технической группе](https://t.me/+EPk6TMZEZMM5OGY1), где вы получите надежную техническую поддержку.


---
*Источник: [https://trtc.io/document/61217](https://trtc.io/document/61217)*

---
*Источник (EN): [conversation-list.md](./conversation-list.md)*
