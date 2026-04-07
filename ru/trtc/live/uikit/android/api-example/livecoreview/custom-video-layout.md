# Пользовательская разметка видео

Этот документ в основном описывает, как использовать `LiveCoreView` модуля `LiveStreamCore` для реализации пользовательских разметок видео.

## Предварительные требования

Перед использованием `LiveStreamCore` необходимо [интегрировать и выполнить вход](https://www.tencentcloud.com/document/product/647/67475#) в LiveStreamCore, чтобы обеспечить правильную работу последующих функций.

## Руководство пользователя

### Шаг 1: добавление LiveCoreView в представление

Сначала необходимо импортировать модуль `LiveStreamCore`, затем создать объект представления `LiveCoreView` и добавить его в ваше представление.

iOS

Android

```
LiveStreamCore
```

```
import com.trtc.uikit.livekit.livestreamcore.LiveCoreView;public class CustomizeVideoLayoutActivity extends AppCompatActivity {    @Override    protected void onCreate(@Nullable Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        LiveCoreView liveCoreView = new LiveCoreView(this);        addContentView(liveCoreView,                new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));    }}
```

### Шаг 2: подготовка параметров разметки видео

При вызове API `setLayoutMode` необходимо заполнить ключевые параметры `layoutMode` и `layoutJson`. Подробности приведены ниже:

#### Параметр 1: LayoutMode

`layoutMode` — это перечисление типа `LayoutMode`.

| Значения перечисления | Значение | Дополнительные примечания |
| --- | --- | --- |
| gridLayout | Сеточная разметка | Встроенные стили разметки (это стиль по умолчанию) |
| floatLayout | Разметка плавающего окна | Встроенные стили разметки |
| freeLayout | Вертикальная разметка | Пользовательские стили разметки |

#### Параметр 2: layoutJson

layoutJson — это строка JSON разметки.

Описание структуры JSON:

```
{	"1": {                                 // Количество представлений видео		"backgroundColor": "#000000",      // Цвет фона холста в шестнадцатеричном формате RGB		"viewInfoList": [{                 // Информация разметки и цвет фона каждого представления видео			"x": 0,                        // Горизонтальное смещение как доля ширины экрана, диапазон [0, 1]			"y": 0,                        // Вертикальное смещение как доля ширины экрана, диапазон [0, 1]			"width": 1,                    // Ширина представления видео как доля ширины экрана, диапазон [0, 1]			"height": -1,                  // Высота представления видео как доля ширины экрана, диапазон [0, 1] или -1; -1 означает, что высота представления совпадает с высотой экрана			"zOrder": 0,                   // Z-порядок представления видео, большие значения означают, что представление находится сверху			"backgroundColor": "#000000"   // Цвет фона текущего представления видео в шестнадцатеричном формате RGB		}]	}}
```

### Шаг 3: пользовательская разметка видео

С готовыми параметрами `layoutMode` и `layoutConfig` из шага 2 можно вызвать функцию API `setLayoutMode` для установки разметки позиции микрофона.

#### Встроенная разметка

При использовании встроенной разметки необходимо только передать параметр `layoutMode`.

iOS

Android

```
// Сеточная разметкаself.liveCoreView.setLayoutMode(layoutMode: .gridLayout)// Разметка плавающего окнаself.liveCoreView.setLayoutMode(layoutMode: .floatLayout)
```

```
// Сеточная разметкаliveCoreView.setLayoutMode(LiveCoreViewDefine.LayoutMode.GRID_LAYOUT, "");// Разметка плавающего окнаliveCoreView.setLayoutMode(LiveCoreViewDefine.LayoutMode.FLOAT_LAYOUT, "");
```

#### Пользовательская разметка

При использовании пользовательской разметки значение `layoutMode` должно быть `freeLayout`, и необходимо передать соответствующий параметр конфигурации разметки позиции микрофона `layoutJson`.

Например, для достижения следующей разметки видео:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a2118d2abdd811ef8d65525400fdb830.png)

LayoutJson должен быть:

```
{  "1": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.0,      "width": 1.0,      "height": -1.0,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "2": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.5,      "height": 0.89333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.5,      "y": 0.384,      "width": 0.5,      "height": 0.89333,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "3": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.666666666,      "height": 0.666666666,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "4": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.5,      "height": 0.5,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.5,      "y": 0.384,      "width": 0.5,      "height": 0.5,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 0.8826,      "width": 0.5,      "height": 0.5,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.5,      "y": 0.8826,      "width": 0.5,      "height": 0.5,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "5": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "6": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "7": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 1.050666666,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "8": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 1.050666666,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 1.050666666,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }]  },  "9": {    "backgroundColor": "#000000",    "viewInfoList": [{      "x": 0.0,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.384,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 0.717333333,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.0,      "y": 1.050666666,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.333333333,      "y": 1.050666666,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }, {      "x": 0.666666666,      "y": 1.050666666,      "width": 0.333333333,      "height": 0.333333333,      "zOrder": 0,      "backgroundColor": "#000000"    }]  }}
```

Вызовите API `setLayoutMode` для реализации пользовательской разметки:

iOS

Android

```
let freeLayoutJson = ""  // Замените это предыдущей строкой JSONself.liveCoreView.setLayoutMode(layoutMode: .freeLayout, layoutJson: freeLayoutJson)
```

```
String freeLayoutJson = "";  // Замените это предыдущей строкой JSONliveCoreVjiew.setLayoutMode(LiveCoreViewDefine.FREE_LAYOUT, freeLayoutJson);
```


---
*Источник: [https://trtc.io/document/67470](https://trtc.io/document/67470)*

---
*Источник (EN): [custom-video-layout.md](./custom-video-layout.md)*
