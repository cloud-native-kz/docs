# Эффекты красоты

`BaseBeautyStore` — это модуль в **AtomicXCore**, отвечающий за управление основными эффектами косметической обработки портретов. Этот модуль позволяет легко добавить функции естественного улучшения внешнего вида в приложения для прямой трансляции или видеоконференций.

## Основные возможности

- **Регулировка сглаживания кожи**: Настройка интенсивности сглаживания (0–9).
- **Регулировка отбеливания**: Настройка интенсивности отбеливания (0–9).
- **Регулировка румяца**: Настройка интенсивности румяца (0–9).
- **Сброс эффектов**: Мгновенное восстановление всех параметров косметической обработки на значения по умолчанию.
- **Мониторинг состояния:** Доступ к значениям в реальном времени применяемых в настоящий момент параметров косметической обработки.

## Основные концепции

| **Основная концепция** | **Тип** | **Основные обязанности и описание** |
| --- | --- | --- |
| `BaseBeautyState` | `data` | Представляет текущее состояние модуля основной косметической обработки. Содержит применяемые в настоящий момент значения интенсивности для сглаживания (smoothLevel), отбеливания (whitenessLevel) и румяца (ruddyLevel). |
| `BaseBeautyStore` | `abstract` | Основной класс управления для работы с функциями основной косметической обработки. Реализован как глобальный синглтон (shared), отвечает за установку, сброс и синхронизацию всех параметров основной косметической обработки. |

## Реализация

### Шаг 1: Интеграция компонента

- **Прямая трансляция видео**: Обратитесь к [Быстрому старту](https://www.tencentcloud.com/document/product/647/74593) для интеграции AtomicXCore и завершения настройки LiveCoreView.
- **Голосовой чат-рум**: Обратитесь к [Быстрому старту](https://www.tencentcloud.com/document/product/647/74681) для интеграции AtomicXCore и завершения настройки LiveCoreView.

### Шаг 2: Получение экземпляра и подписка на состояние

Получите глобальный синглтон экземпляра `BaseBeautyStore` и подпишитесь на получение обновлений состояния текущих параметров косметической обработки в реальном времени.

#### Реализация

1. **Получение синглтона**: Используйте `BaseBeautyStore.shared()` для доступа к глобальному экземпляру.
2. **Подписка на состояние**: Подпишитесь на `baseBeautyStore.baseBeautyState` для получения обновлений BaseBeautyState в реальном времени.

#### Пример кода

```
import io.trtc.tuikit.atomicxcore.api.device.BaseBeautyStateimport io.trtc.tuikit.atomicxcore.api.device.BaseBeautyStoreimport kotlinx.coroutines.CoroutineScopeimport kotlinx.coroutines.Dispatchersimport kotlinx.coroutines.launchimport kotlinx.coroutines.flow.MutableStateFlowclass BeautyManager() {    // 1. Получение синглтона    private val baseBeautyStore = BaseBeautyStore.shared()    private val coroutineScope = CoroutineScope(Dispatchers.Main)    private val _smoothLevel = MutableStateFlow(0f)    private val _whitenessLevel = MutableStateFlow(0f)    private val _ruddyLevel = MutableStateFlow(0f)    // Предоставление состояния красоты извне    val baseBeautyState = BaseBeautyState(        smoothLevel = _smoothLevel,        whitenessLevel = _whitenessLevel,        ruddyLevel = _ruddyLevel    )    init {        // 2. Подписка на состояние        subscribeToBeautyState()    }    private fun subscribeToBeautyState() {        coroutineScope.launch(Dispatchers.Main) {            baseBeautyStore.baseBeautyState.smoothLevel.collect { smoothLevel ->                _smoothLevel.value = smoothLevel            }        }        coroutineScope.launch(Dispatchers.Main) {            baseBeautyStore.baseBeautyState.whitenessLevel.collect { whitenessLevel ->                _whitenessLevel.value = whitenessLevel            }        }        coroutineScope.launch(Dispatchers.Main) {            baseBeautyStore.baseBeautyState.ruddyLevel.collect { ruddyLevel ->                _ruddyLevel.value = ruddyLevel            }        }    }    // ... последующие методы}
```

### Шаг 3: Установка параметров косметической обработки

Когда пользователи регулируют ползунок косметической обработки или выбирают предустановку, вызовите соответствующий API для установки требуемой интенсивности.

#### Реализация

1. **Получение значения интенсивности**:
- Получите значение из элемента управления пользовательского интерфейса (например, `SeekBar`).
- Обратите внимание, что интерфейс SDK принимает диапазон параметров `[0, 9]`, где 0 означает отключение эффекта, а 9 означает максимальную выраженность эффекта. Вам необходимо преобразовать значение элемента управления интерфейса (например, `0.0 - 1.0` для `UISlider`) в диапазон `0 - 9`.
2. **Вызов API**: Используйте `setSmoothLevel(smoothLevel:)`, `setWhitenessLevel(whitenessLevel:)` и `setRuddyLevel(ruddyLevel:)` для установки интенсивности сглаживания, отбеливания и румяца.

#### Пример кода

```
class BeautyManager() {    private val baseBeautyStore = BaseBeautyStore.shared()        // Установка уровня сглаживания (входной диапазон 0–100, внутренне преобразуется в 0–9)    fun updateSmoothLevel(uiLevel: Int) {        val sdkLevel = (uiLevel / 100.0f * 9.0f)        baseBeautyStore.setSmoothLevel(sdkLevel)        println("Set smoothing level: UI=$uiLevel, SDK=$sdkLevel")    }    // Установка уровня отбеливания (входной диапазон 0–100, внутренне преобразуется в 0–9)    fun updateWhitenessLevel(uiLevel: Int) {        val sdkLevel = (uiLevel / 100.0f * 9.0f)        baseBeautyStore.setWhitenessLevel(sdkLevel)        println("Set whitening level: UI=$uiLevel, SDK=$sdkLevel")    }    // Установка уровня румяца (входной диапазон 0–100, внутренне преобразуется в 0–9)    fun updateRuddyLevel(uiLevel: Int) {        val sdkLevel = (uiLevel / 100.0f * 9.0f)        baseBeautyStore.setRuddyLevel(sdkLevel)        println("Set rosy level: UI=$uiLevel, SDK=$sdkLevel")    }}
```

### Шаг 4: Сброс эффектов косметической обработки

Когда пользователи нажимают кнопку «Сброс» или «Отключить красоту», восстановите все параметры косметической обработки на значения по умолчанию (как правило, 0).

#### Реализация

- **Вызов API**: Вызовите метод `baseBeautyStore.reset()`.

#### Пример кода

```
class BeautyManager() {    private val baseBeautyStore = BaseBeautyStore.shared()    // Сброс всех эффектов основной косметической обработки    fun resetBeautyEffects() {        baseBeautyStore.reset()    }}
```

## Расширенные возможности

### Сравнение: основная и расширенная косметическая обработка

AtomicXCore также предоставляет функции расширенной косметической обработки для более требовательных сценариев:

| **Элемент сравнения** | **Основная косметическая обработка (BaseBeautyStore)** | **Расширенная косметическая обработка (TEBeautyKit, требуется дополнительная интеграция)** |
| --- | --- | --- |
| Основные возможности | Сглаживание, отбеливание, румянец | Включает все основные функции плюс V-образное лицо, регулировка расстояния между глазами, утончение носа, трёхмерные наклейки, фильтры, макияж и многое другое |
| Цена | Бесплатно (включено в лицензию AtomicXCore) | Платная опция (требуется отдельная лицензия Tencent Effects SDK) |
| Метод интеграции | Встроено по умолчанию; используйте BaseBeautyStore.shared() напрямую | Требует дополнительной интеграции компонента TEBeautyKit и аутентификации |
| Рекомендуемые сценарии | Сценарии с основными потребностями в косметической обработке и требованиями быстрой реализации | Сценарии, требующие расширенной косметической обработки, коррекции формы, наклеек, фильтров и других премиум-функций |

### Интеграция расширенной косметической обработки

Для использования функций расширенной косметической обработки обратитесь к документации [Advanced Beauty](https://trtc.io/document/60196?product=beautyar&menulabel=core%20sdk&platform=android). После интеграции и аутентификации TEBeautyKit используйте его API для управления всеми эффектами косметической обработки.

## Документация по API

Подробную информацию о всех открытых интерфейсах, свойствах и методах [BaseBeautyStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-base-beauty-store/index.html) и связанных классов см. в официальной документации по API для фреймворка [AtomicXCore](https://tencent-rtc.github.io/TUIKit_Android/index.html). Соответствующие хранилища, упомянутые в этом руководстве:

| **Хранилище/компонент** | **Описание функции** | **Документация по API** |
| --- | --- | --- |
| `LiveCoreView` | Основной компонент представления для отображения и взаимодействия с потоками прямой трансляции видео. Обрабатывает рендеринг видео и виджеты представления, поддерживает трансляцию хостом, совместное размещение аудитории, подключения хостов и многое другое. | [Документация по API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.view/-live-core-view/index.html) |
| `BaseBeautyStore` | Основная косметическая обработка: регулировка сглаживания, отбеливания и румяца (уровни 0–9), сброс состояния, синхронизация параметров эффектов. | [Документация по API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-base-beauty-store/index.html) |
| `DeviceStore` | Управление устройствами аудио и видео: микрофон (включение/отключение, громкость), камера (включение/отключение, переключение, качество), общий доступ к экрану, мониторинг состояния устройства в реальном времени. | [Документация по API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.device/-device-store/index.html) |

## Часто задаваемые вопросы

### Я установил параметры косметической обработки, но почему нет эффекта?

**Проверьте следующее:**

1. **Камера включена**: Убедитесь, что камера включена (например, через DeviceStore.shared().openLocalCamera). Эффекты красоты не могут применяться к чёрному экрану или потоку только с аудио.
2. **Использование расширенной косметической обработки**: Если вы интегрировали `TEBeautyKit` (расширенную косметическую обработку), убедитесь, что вы используете API, предоставленные `TEBeautyKit`, для регулировки эффектов косметической обработки.
3. **Диапазон параметров**: Если вы используете функцию основной косметической обработки, убедитесь, что значения интенсивности, которые вы предоставляете, находятся в допустимом диапазоне (значения с плавающей точкой от 0 до 9).


---
*Источник: [https://trtc.io/document/74605](https://trtc.io/document/74605)*

---
*Источник (EN): [beauty-effects.md](./beauty-effects.md)*
