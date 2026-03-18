# Компонент Live Gift

Это руководство описывает, как быстро интегрировать компонент подарков TUILiveKit в ваш проект.

## Обзор компонента

Функция подарков в TUILiveKit состоит из двух основных компонентов UI:

| **Название компонента** | **Имя класса** | **Описание** |
| --- | --- | --- |
| Панель выбора подарков | `GiftListView` | Отображает доступные подарки и обрабатывает выбор пользователя и действия отправки. |
| Отображение анимации подарков | `GiftPlayView` | Получает сообщения о подарках и воспроизводит анимации (например, SVGA) на экране. |

### Примеры эффектов

| **Панель подарков** | **Подарки в чате прямой трансляции** | **Полноэкранные подарки** |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/53c618d6db2711f09ea65254001c06ec.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/54c2c7d8db2711f09c08525400bf7822.gif) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/55533380db2711f09dea52540044a08e.gif) |

## Быстрый старт

### Шаг 1: Активация услуги

Следуйте руководству [Активация услуги](https://www.tencentcloud.com/document/product/647/60033) для включения TUILiveKit.

> **Примечание:** Для использования системы подарков активируйте версию **Free Trial** или **Pro**. Количество настраиваемых подарков зависит от выбранного пакета. Для получения подробной информации см. раздел **Gift System** в [Описание функций и биллинга](https://www.tencentcloud.com/document/product/647/59407#658e2423-30d2-45e2-91b8-128b2730b072) и выберите подходящий вам пакет.

### Шаг 2: Интеграция кода

- **Конфигурация проекта**:
  - **Сценарий видеотрансляции**: Следуйте разделу [Видеотрансляция - Подготовка](https://www.tencentcloud.com/document/product/647/72217) для завершения интеграции TUILiveKit.
  - **Сценарий голосовой комнаты**: Следуйте разделу [Голосовая комната - Подготовка](https://www.tencentcloud.com/document/product/647/60335) для завершения интеграции TUILiveKit.
- **Требование к версии**: TUILiveKit >= 3.2.0.

### Шаг 3: Интеграция панели выбора подарков

`GiftListView` обычно отображается как всплывающее окно или нижняя панель. Добавьте её в макет вашей `Activity` или `Fragment`, как показано ниже.

```
import android.os.Bundleimport android.widget.FrameLayoutimport androidx.appcompat.app.AppCompatActivityimport com.trtc.uikit.livekit.Rimport com.trtc.uikit.livekit.component.gift.GiftListViewclass YourLiveActivity : AppCompatActivity() {    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_live_room)        // Получить контейнер корневого макета        val rootView = findViewById<FrameLayout>(R.id.root_view)        // 1. Создать компонент списка подарков        val giftListView = GiftListView(this)        // 2. Инициализировать компонент с текущим ID комнаты        // Примечание: убедитесь, что у вас есть действительный roomId на этот момент        giftListView.init("your_room_id")        // 3. Добавить компонент в иерархию представлений        rootView.addView(giftListView)    }}
```

### Шаг 4: Интеграция компонента воспроизведения подарков

`GiftPlayView` — это прозрачный оверлей для анимации подарков. Расположите его над видеослоем и под интерактивными элементами управления.

```
import android.os.Bundleimport android.widget.FrameLayoutimport androidx.appcompat.app.AppCompatActivityimport com.trtc.uikit.livekit.Rimport com.trtc.uikit.livekit.component.gift.GiftPlayViewclass YourLiveActivity : AppCompatActivity() {    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_live_room)        val rootView = findViewById<FrameLayout>(R.id.root_view)        // 1. Создать компонент воспроизведения подарков        val giftPlayView = GiftPlayView(this)        // 2. Инициализировать компонент с текущим ID комнаты        // Компонент будет автоматически прослушивать сообщения о подарках в этой комнате и воспроизводить анимации        giftPlayView.init("your_room_id")        // 3. Добавить компонент в иерархию представлений        // Рекомендуется: добавить это представление над видеослоем и под элементами управления UI        rootView.addView(giftPlayView)    }}
```

## Следующие шаги

После завершения интеграции UI ваше приложение будет поддерживать базовую функциональность подарков. Для создания готовой к использованию системы подарков обратитесь к руководству [Интеграция backend и расширенные функции](https://www.tencentcloud.com/document/product/647/69849) для реализации следующего:

- **Пользовательская конфигурация подарков:** Загружайте пользовательские иконки подарков, анимации и цены через API сервера.
- **Интеграция платежей:** Настройте URL обратного вызова для обработки проверки баланса и обработки платежей через ваш серверный биллинг.
- **Синхронизация баллов PK:** Преобразуйте значения подарков в баллы PK в реальном времени во время боёв хостов.
- **Аналитика:** Получайте доступ к записям транзакций подарков, показателям доходов и другим операционным данным.
- **Обновление SDK эффектов подарков**: Если SVGA не соответствует вашим требованиям, вы можете интегрировать продвинутые плееры анимаций для поддержки MP4, PAG или других высокачественных форматов прозрачной анимации.


---
*Источник: [https://trtc.io/document/73996](https://trtc.io/document/73996)*

---
*Источник (EN): [live-gift-component.md](./live-gift-component.md)*
