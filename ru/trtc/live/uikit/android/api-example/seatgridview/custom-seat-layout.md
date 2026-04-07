# Пользовательский макет мест

Этот документ в основном описывает, как настроить макет мест для `SeatGridView`.

## Предварительные требования

Перед использованием `SeatGridView` необходимо [интегрировать и войти](https://www.tencentcloud.com/document/product/647/67506#) в SeatGridView, чтобы обеспечить правильную работу последующих функций.

## Руководство по использованию

### Шаг 1: Добавление SeatGridView в представление

Сначала необходимо импортировать модуль `SeatGridView`, затем создать объект SeatGridView и добавить его в представление.

iOS

Android

```
import UIKitimport RTCRoomEngineimport SeatGridView class CustomizeSeatLayoutController: UIViewController {    private let seatGridView: SeatGridView = {         let view = SeatGridView()      return view    }        override func viewDidLoad() {        super.viewDidLoad()        // Add seatGridView to the view and set layout constraints    }}
```

```
import com.trtc.uikit.livekit.seatGridView.SeatGridView;public class CustomizeSeatLayoutActivity extends AppCompatActivity {    @Override    protected void onCreate(@Nullable Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        SeatGridView seatGridView = new SeatGridView(this);        addContentView(seatGridView,                new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));    }}
```

### Шаг 2: Подготовка параметров макета мест

При вызове API `setLayoutMode` необходимо заполнить ключевые параметры `layoutMode` и `layoutConfig`. Ниже приведено подробное описание:

#### Параметр 1: layoutMode

`layoutMode` — это перечисление типа `SGLayoutMode`.

| Значения перечисления | Значение | Дополнительные примечания |
| --- | --- | --- |
| focus | Централизованный макет (например, макет 1-3-3, 1 элемент в первой строке, 3 элемента во второй и третьей строках) | Встроенные стили макета |
| grid | Сеточный макет | Встроенные стили макета (это стиль по умолчанию) |
| vertical | Вертикальный макет | Встроенные стили макета |
| free | Свободный макет | Пользовательские стили макета |

> **Примечания:** При использовании встроенных стилей макета `seatGridView` не требуется предоставлять дополнительные параметры `SGSeatViewLayoutConfig`. Необходимо только передать параметр `SGLayoutMode` в setLayoutMode.

#### Параметр 2: layoutConfig

`layoutConfig` — это структура типа `SGSeatViewLayoutConfig`, состоящая из полей `rowConfigs` и `rowSpacing`.

| Имя параметра | Описание поля | Тип данных |
| --- | --- | --- |
| rowConfigs | Используется для хранения конфигурации макета мест каждой строки. | Массив типа SGSeatViewLayoutRowConfig |
| rowSpacing | Используется для хранения расстояния между строками в макете мест | Число с плавающей точкой |

`SGSeatViewLayoutRowConfig` состоит из четырёх полей: `count`, `seatSpacing`, `seatSize` и `alignment`.

| Имя параметра | Описание поля | Тип данных |
| --- | --- | --- |
| count | Количество мест в строке | Целое число |
| seatSpacing | Вертикальное расстояние между местами в одной строке | Число с плавающей точкой |
| seatSize | Размер места | Тип Size |
| alignment | Расположение мест в одной строке | SGSeatViewLayoutRowAlignment |

`SGSeatViewLayoutRowAlignment` — это перечисление.

| Значения перечисления | Значение |
| --- | --- |
| spaceAround | Рассредоточенное выравнивание, не против стенки контейнера, с равномерно распределённым оставшимся пространством по обеим сторонам каждого элемента |
| spaceBetween | Выравнивание с промежутками, крайние левые и правые элементы прижимаются к левой или правой границе, равное расстояние между элементами. |
| spaceEvenly | Среднее выравнивание, не против стенки контейнера, с равномерно распределённым оставшимся пространством. |
| start | Выравнивание влево |
| end | Выравнивание вправо |
| center | Центрирование |

### Шаг 3: Установка макета мест

После подготовки параметров `layoutMode` и `layoutConfig` на шаге 2 можно вызвать функцию API `setLayoutMode` для установки макета мест.

#### Встроенный макет

При использовании встроенного макета необходимо только передать параметр `layoutMode`.

iOS

Android

```
// Централизованный макетself.seatGridView.setLayoutMode(layoutMode: .focus)// Сеточный макетself.seatGridView.setLayoutMode(layoutMode: .grid)// Вертикальныйself.seatGridView.setLayoutMode(layoutMode: .vertical)
```

```
// Централизованный макетseatGridView.setLayoutMode(VoiceRoomDefine.LayoutMode.FOCUS, null);// Сеточный макетseatGridView.setLayoutMode(VoiceRoomDefine.LayoutMode.GRID, null);// Вертикальный макетseatGridView.setLayoutMode(VoiceRoomDefine.LayoutMode.VERTICAL, null);
```

#### Пользовательский макет

При использовании пользовательского макета значение `layoutMode` должно быть `free`, и необходимо передать соответствующий параметр конфигурации макета мест `layoutConfig`.

Например, для настройки пользовательского макета 2, 1, 2 с расположением каждой строки как spaceBetween, center и spaceBetween:

iOS

Android

```
// Create seat configuration for each rowlet firstRowConfig = SGSeatViewLayoutRowConfig(count: 2,     seatSpacing: 10.0, seatSize: CGSize(width: 50, height: 50), alignment: .spaceBetween)let secondRowConfig = SGSeatViewLayoutRowConfig(count: 1,    seatSpacing: 10.0, seatSize: CGSize(width: 72, height: 72), alignment: .center)let thirdRowConfig = SGSeatViewLayoutRowConfig(count: 2,     seatSpacing: 10.0, seatSize: CGSize(width: 50, height: 50), alignment: .spaceBetween)    let rowConfigs: [SGSeatViewLayoutRowConfig] = [firstRowConfig, secondRowConfig, thirdRowConfig]let layoutConfig = SGSeatViewLayoutConfig(rowConfigs: rowConfigs, rowSpacing: 20.0)// Set layout modeself.seatGridView.setLayoutMode(layoutMode: .free, layoutConfig: layoutConfig)
```

```
// Create seat configuration for each rowVoiceRoomDefine.SeatViewLayoutRowConfig firstRowConfig = new VoiceRoomDefine.SeatViewLayoutRowConfig();firstRowConfig.count = 2;firstRowConfig.seatSpacing = 10;firstRowConfig.seatSize = new VoiceRoomDefine.Size(50,50);firstRowConfig.alignment = SPACE_BETWEEN;VoiceRoomDefine.SeatViewLayoutRowConfig secondRowConfig = new VoiceRoomDefine.SeatViewLayoutRowConfig();secondRowConfig.count = 1;secondRowConfig.seatSpacing = 10;secondRowConfig.seatSize = new VoiceRoomDefine.Size(72,72);secondRowConfig.alignment = CENTER;VoiceRoomDefine.SeatViewLayoutRowConfig thirdRowConfig = new VoiceRoomDefine.SeatViewLayoutRowConfig();thirdRowConfig.count = 2;thirdRowConfig.seatSpacing = 10;thirdRowConfig.seatSize = new VoiceRoomDefine.Size(50,50);thirdRowConfig.alignment = SPACE_BETWEEN;List<VoiceRoomDefine.SeatViewLayoutRowConfig> rowConfigs = new ArrayList<>();rowConfigs.add(firstRowConfig);rowConfigs.add(secondRowConfig);rowConfigs.add(thirdRowConfig);VoiceRoomDefine.SeatViewLayoutConfig config = new VoiceRoomDefine.SeatViewLayoutConfig();config.rowConfigs = rowConfigs;config.rowSpacing = 20;// Set layout modeseatGridView.setLayoutMode(LayoutMode.FREE, config);
```


---
*Источник: [https://trtc.io/document/67500](https://trtc.io/document/67500)*

---
*Источник (EN): [custom-seat-layout.md](./custom-seat-layout.md)*
