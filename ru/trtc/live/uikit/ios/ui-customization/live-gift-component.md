# Компонент Live Gift

В этом руководстве рассказывается о том, как быстро интегрировать компонент раздачи подарков TUILiveKit в ваш проект.

## Обзор компонента

Функция раздачи подарков в TUILiveKit состоит из двух основных компонентов пользовательского интерфейса:

| **Название компонента** | **Имя класса** | **Описание** |
| --- | --- | --- |
| Панель выбора подарков | `GiftListView` | Показывает доступные подарки и обрабатывает действия выбора и отправки пользователя. |
| Отображение анимации подарков | `GiftPlayView` | Получает сообщения о подарках и воспроизводит анимации (например, SVGA) на экране. |

### Демонстрация эффектов

| **Панель подарков** | **Подарки в прямом чате** | **Полноэкранные подарки** |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/541288dfdb2411f0bf585254005ef0f7.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/546c5700db2411f0b31e5254007c27c5.gif) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6fb56fb4db2411f0b45152540099c741.gif) |

## Быстрый старт

### Шаг 1. Активация сервиса

Следуйте руководству [Activate the Service](https://www.tencentcloud.com/document/product/647/60033) для включения TUILiveKit.

> **Примечание:** Для использования системы подарков активируйте либо **Free Trial**, либо **Pro** версию. Количество настраиваемых подарков зависит от выбранного пакета. Подробности см. в разделе **Gift System** в [Feature and Billing Description](https://www.tencentcloud.com/document/product/647/59407#658e2423-30d2-45e2-91b8-128b2730b072) и выберите пакет, соответствующий вашим потребностям.

### Шаг 2: Конфигурация вашего проекта

- **Конфигурация проекта**:
  - **Video Live Streaming**: Следуйте [Video Live Streaming - Preparation](https://www.tencentcloud.com/document/product/647/72223) для завершения интеграции TUILiveKit.
  - **Voice Chat Room**: Следуйте [Voice Chat Room - Preparation](https://www.tencentcloud.com/document/product/647/60334) для завершения интеграции TUILiveKit.
- **Требование к версии**: TUILiveKit >= 3.2.0.

### Шаг 3. Добавьте страницу отображения списка подарков

Добавьте в ваше приложение страницу отображения списка подарков, чтобы зрители могли просматривать доступные подарки. Используйте пример кода ниже для создания компонента `GiftListView` и его добавления в ваше представление:

```
import TUILiveKitclass YourGiftViewController: UIViewController {    // 1. Create GiftListView object    //    - roomId: Should match the roomId of the live stream the audience has joined    lazy var giftListView = {      let view = GiftListView(roomId: liveId)      return view    }()    private let liveId: String    // ... additional code ...    public override func viewDidLoad() {        super.viewDidLoad()        // 2. Add the component to your view and set up the layout        view.addSubView(giftListView)        giftPlayView.snp.remakeConstraints { make in            make.leading.trailing.equalToSuperview()            make.height.equalTo(256)            make.bottom.equalToSuperview()        }    }}
```

### Шаг 4. Добавьте страницу воспроизведения анимации подарков

Добавьте в ваше приложение страницу воспроизведения анимации подарков. Компонент `GiftPlayView` автоматически получает сообщения о подарках и воспроизводит соответствующие анимации. Используйте пример кода ниже для создания компонента `GiftPlayView` и его добавления в ваше представление:

```
import TUILiveKit// YourAnchorViewController represents your host view controller. Audience side can refer to the following example:class YourAnchorViewController: UIViewController {    // 1. Create and initialize GiftPlayView object    //    - roomId: Should match the roomId of the live stream the audience has joined    lazy var giftPlayView = {      let view = GiftPlayView(roomId: liveId)      return view    }()    private let liveId: String    // ... other code ...    public override func viewDidLoad() {        super.viewDidLoad()        // 2. Add the component to your view and set up the layout        view.addSubView(giftPlayView)        giftPlayView.snp.remakeConstraints { make in          make.edges.equalToSuperview()        }    }}
```

## Следующие шаги

После завершения интеграции пользовательского интерфейса ваше приложение будет поддерживать базовую функциональность раздачи подарков. Чтобы создать готовую к производству систему раздачи подарков, обратитесь к руководству [Backend Integration and Advanced Features](https://www.tencentcloud.com/document/product/647/69849) для реализации следующего:

- **Custom Gift Configuration:** Загружайте пользовательские значки подарков, анимации и цены через серверные API.
- **Payment Integration:** Настройте URL обратного вызова для обработки проверки баланса и обработки платежей через ваш биллинг-бэкенд.
- **PK Score Sync:** Конвертируйте значения подарков в очки PK в реальном времени во время боевых действий хостов.
- **Analytics:** Получите доступ к записям транзакций подарков, метрикам доходов и другим операционным данным.
- **Upgrade Gift Effect SDK**: Если SVGA не соответствует вашим требованиям, вы можете интегрировать продвинутые плееры анимации для поддержки MP4, PAG или других высококачественных форматов прозрачной анимации.


---
*Источник: [https://trtc.io/document/73997](https://trtc.io/document/73997)*

---
*Источник (EN): [live-gift-component.md](./live-gift-component.md)*
