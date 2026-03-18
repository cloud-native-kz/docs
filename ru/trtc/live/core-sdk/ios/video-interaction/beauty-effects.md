# Эффекты красоты

`BaseBeautyStore` — это модуль в **AtomicXCore**, отвечающий за управление базовыми эффектами косметической обработки портретов. Этот модуль позволяет легко добавлять функции естественного улучшения внешнего вида в приложения для прямых трансляций или видеозвонков.

## Основные возможности

- **Сглаживание кожи**: настройка интенсивности сглаживания (0–9).
- **Отбеливание кожи**: настройка интенсивности отбеливания (0–9).
- **Румяна**: настройка интенсивности румян (0–9).
- **Сброс эффектов**: мгновенное восстановление всех параметров косметической обработки по умолчанию.
- **Мониторинг состояния**: реальный доступ к текущим применяемым параметрам косметической обработки.

## Основные концепции

| **Основная концепция** | **Тип** | **Основные обязанности и описание** |
| --- | --- | --- |
| `BaseBeautyState` | `struct` | Представляет текущее состояние модуля базовой косметической обработки. Содержит текущие значения интенсивности для сглаживания (smoothLevel), отбеливания (whitenessLevel) и румян (ruddyLevel). |
| `BaseBeautyStore` | `class` | Основной класс управления для взаимодействия с функциями базовой косметической обработки. Реализован как глобальный синглтон (`shared`). Отвечает за установку параметров, сброс эффектов и синхронизацию состояния в приложении. |

## Реализация

### Шаг 1: интеграция компонентов

- **Видео прямая трансляция**: см. [Быстрый старт](https://www.tencentcloud.com/document/product/647/74594) для интеграции AtomicXCore и завершения настройки LiveCoreView.
- **Голосовой чат-комната**: см. [Быстрый старт](https://www.tencentcloud.com/document/product/647/74682) для интеграции AtomicXCore и завершения настройки LiveCoreView.

### Шаг 2: получение экземпляра и подписка на состояние

Получите глобальный экземпляр синглтона `BaseBeautyStore` и подпишитесь на получение обновлений состояния текущих параметров косметической обработки в реальном времени.

#### Реализация

1. **Получить синглтон**: используйте `BaseBeautyStore.shared()` для доступа к глобальному экземпляру.
2. **Подписаться на состояние**: подпишитесь на `baseBeautyStore.baseBeautyState` для получения обновлений `BaseBeautyState` в реальном времени.

#### Пример кода

```
import Foundationimport AtomicXCore import Combine     class BeautyManager {    // 1. Get the singleton instance    private let baseBeautyStore = BaseBeautyStore.shared    private var cancellables = Set<AnyCancellable>()        // Expose beauty status externally    let beautyStatePublisher = CurrentValueSubject<BaseBeautyState, Never>(BaseBeautyState())    init() {        // 2. Subscribe to the state        subscribeToBeautyState()    }        private func subscribeToBeautyState() {        baseBeautyStore.state            .subscribe()            .receive(on: DispatchQueue.main)            .assign(to: \\.value, on: beautyStatePublisher)            .store(in: &cancellables)    }        // ... Subsequent methods}
```

### Шаг 3: установка параметров косметической обработки

Когда пользователи регулируют ползунок косметической обработки или выбирают предустановку, вызовите соответствующий API для установки требуемой интенсивности.

#### Реализация

1. **Получить значение интенсивности**:
  - Получите значение интенсивности, установленное пользователем из элемента управления пользовательского интерфейса (например, `UISlider`).
  - Обратите внимание, что интерфейс SDK принимает диапазон параметров `[0, 9]`, где 0 означает отключение эффекта, а 9 означает максимальную выраженность эффекта. Необходимо преобразовать значение элемента управления пользовательского интерфейса (например, `0.0 - 1.0` для `UISlider`) в диапазон `0 - 9`.
2. **Вызвать API**: используйте `setSmoothLevel(smoothLevel:)`, `setWhitenessLevel(whitenessLevel:)` и `setRuddyLevel(ruddyLevel:)` для установки интенсивности сглаживания, отбеливания и румян.

#### Пример кода

```
extension BeautyManager {    /// Set the smoothing level (Input range 0.0 ~ 1.0, converted internally to 0 ~ 9)    func updateSmoothLevel(uiLevel: Float) {        // Map UI's 0.0 ~ 1.0 to SDK's 0 ~ 9        let sdkLevel = uiLevel * 9.0        baseBeautyStore.setSmoothLevel(smoothLevel: sdkLevel)    }    /// Set the whitening level (Input range 0.0 ~ 1.0, converted internally to 0 ~ 9)    func updateWhitenessLevel(uiLevel: Float) {        let sdkLevel = uiLevel * 9.0        baseBeautyStore.setWhitenessLevel(whitenessLevel: sdkLevel)    }    /// Set the rosiness level (Input range 0.0 ~ 1.0, converted internally to 0 ~ 9)    func updateRuddyLevel(uiLevel: Float) {        let sdkLevel = uiLevel * 9.0        baseBeautyStore.setRuddyLevel(ruddyLevel: sdkLevel)    }}
```

### Шаг 4: сброс эффектов косметической обработки

Когда пользователи нажимают «Сброс» или «Отключить красоту», восстановите все параметры косметической обработки в их значения по умолчанию (обычно 0).

#### Реализация

- **Вызвать API**: вызовите метод `baseBeautyStore.reset()`.

#### Пример кода

```
extension BeautyManager {    /// Reset all basic beauty effects    func resetBeautyEffects() {        baseBeautyStore.reset()    }}
```

## Дополнительные возможности

### Сравнение: базовая и расширенная косметическая обработка

AtomicXCore также предоставляет расширенные функции косметической обработки для более требовательных сценариев:

| **Пункт сравнения** | **Базовая косметическая обработка (BaseBeautyStore)** | **Расширенная косметическая обработка (TEBeautyKit)** |
| --- | --- | --- |
| Основные возможности | Сглаживание, отбеливание, румяна | Включает все базовые функции, а также V-образное лицо, регулировка расстояния между глазами, утончение носа, 3D-наклейки, фильтры, макияж и многое другое |
| Ценообразование | Бесплатно (включено в лицензию AtomicXCore) | Платно (требуется отдельная лицензия) |
| Интеграция | Встроено по умолчанию; используйте `BaseBeautyStore.shared()` непосредственно | Требует дополнительной интеграции компонента TEBeautyKit и аутентификации |
| Рекомендуемые сценарии | Сценарии с базовыми требованиями к косметической обработке и требованиями быстрой реализации | Сценарии, требующие расширенной косметической обработки, моделирования, наклеек, фильтров и других премиум-функций |

### Интеграция расширенной косметической обработки

Для использования расширенных функций косметической обработки см. документацию [Advanced Beauty](https://trtc.io/document/60194?product=beautyar&menulabel=core%20sdk&platform=ios). После интеграции и аутентификации TEBeautyKit используйте его API для управления всеми эффектами косметической обработки.

## Документация API

Для получения подробной информации обо всех общедоступных интерфейсах, свойствах и методах [BaseBeautyStore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/basebeautystore) и связанных классов см. официальную документацию API для платформы [AtomicXCore](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore). Соответствующие хранилища, упомянутые в этом руководстве:

| **Хранилище/компонент** | **Описание** | **Справочник API** |
| --- | --- | --- |
| `LiveCoreView` | Основной компонент представления для отображения и взаимодействия с потоками видео прямой трансляции. Обрабатывает отображение видео и виджеты представления, поддерживает трансляцию хоста, совместное участие аудитории, подключение хостов и многое другое. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.view/-live-core-view/index.html) |
| `DeviceStore` | Управление аудио- и видеоустройствами: микрофон (включение/отключение, громкость), камера (включение/отключение, переключение, качество), совместное использование экрана и мониторинг состояния устройства в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/index.html) |
| `BaseBeautyStore` | Базовые косметические фильтры: регулировка сглаживания/отбеливания/румян (0–100), сброс состояния красоты и синхронизация параметров эффектов. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-base-beauty-store/index.html) |

## Часто задаваемые вопросы

### Я отрегулировал параметры, но видеоэффект не изменился.

**Проверьте следующее:**

1. **Состояние камеры**: убедитесь, что камера включена (например, через DeviceStore.shared().openLocalCamera). Эффекты красоты не могут применяться к черному экрану или потоку только звука.
2. **Конфликт SDK**: если вы интегрировали `TEBeautyKit`, API `BaseBeautyStore` могут быть переопределены. Используйте вместо этого API `TEBeautyKit`.
3. **Диапазон значений**: убедитесь, что вы передаете значения от 0 до 9. Передача 0 приведет к отсутствию видимого эффекта.


---
*Источник: [https://trtc.io/document/74606](https://trtc.io/document/74606)*

---
*Источник (EN): [beauty-effects.md](./beauty-effects.md)*
