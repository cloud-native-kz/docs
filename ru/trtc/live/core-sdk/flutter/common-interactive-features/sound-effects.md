# Звуковые эффекты

В этом руководстве показано, как использовать модули `AudioEffectStore` и `DeviceStore` из фреймворка `AtomicXCore` для быстрого добавления элементов управления звуковыми эффектами в приложение для потоковой трансляции. С помощью этих модулей вы можете реализовать функции, такие как регулировка громкости микрофона, мониторинг в наушниках и набор интересных эффектов изменения голоса и реверберации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5a187583f76311f0859b52540097cba1.png)

## Основные возможности

Благодаря интеграции `AudioEffectStore` и `DeviceStore`, вы можете включить следующие функции в приложение для потоковой трансляции:

- **Управление громкостью микрофона**: регулируйте громкость локального захвата, чтобы управлять тем, насколько громко звучит ведущий для аудитории.
- **Мониторинг в наушниках**: позволяет ведущим или гостям слышать свой собственный голос в реальном времени через наушники для контроля и исправления произношения.
- **Эффекты изменения голоса**: предоставляет несколько вариантов изменения голоса, таких как Ребенок, Девочка, Дядя и другие.
- **Эффекты реверберации**: имитируют различные акустические среды, включая караоке, металлический звук, глубокий, яркий и другие.

## Обзор концепций

| Основная концепция | Тип | Ключевые обязанности и описание |
| --- | --- | --- |
| [AudioEffectState](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_audio_effect_store/AudioEffectState-class.html) | class | Отслеживает текущее состояние модуля звуковых эффектов, обычно для отображения в UI. Включает статус изменения голоса, статус реверберации, статус включения мониторинга в наушниках и громкость мониторинга в наушниках. Все свойства являются ValueListenable и поддерживают подписку на изменения состояния. |
| [AudioEffectStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_audio_effect_store/AudioEffectStore-class.html) | class | Одноэкземплярный менеджер данных модуля звуковых эффектов. Используйте это для вызова API звуковых эффектов. После вызова API соответствующее свойство audioEffectState обновляется автоматически; подпишитесь на это реактивное состояние для получения обновлений в реальном времени. |
| [DeviceState](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_device_store/DeviceState-class.html) | class | Отслеживает текущее состояние модуля устройства, обычно для отображения в UI. Ключевые свойства включают статус устройства камеры и микрофона, громкость захвата и другие. Все свойства являются ValueListenable и поддерживают подписку на изменения состояния. |
| [DeviceStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_device_store/DeviceStore-class.html) | class | Одноэкземплярный менеджер данных модуля устройства. Используйте это для управления API камеры и микрофона. После вызова API соответствующее свойство состояния обновляется автоматически; подпишитесь на это реактивное состояние для получения обновлений в реальном времени. |

## Этапы реализации

### Шаг 1: Интеграция компонента

- **Потоковая трансляция**: см. [Быстрая интеграция](https://www.tencentcloud.com/document/product/647/77552) для интеграции **AtomicXCore** и завершения подключения служб.
- **Голосовой чат**: см. [Быстрая интеграция](https://www.tencentcloud.com/document/product/647/77561) для интеграции **AtomicXCore** и завершения подключения служб.

### Шаг 2: Получение экземпляра Store

И `AudioEffectStore`, и `DeviceStore` являются одноэкземплярными (singleton). Вы можете получить доступ к их экземплярам в любом месте вашего проекта, используя свойство shared. Полный пример реализации см. в файле [audio_effect_panel_widget.dart](https://github.com/Tencent-RTC/TUIKit_Flutter/blob/main/live/livekit/lib/component/audio_effect/audio_effect_panel_widget.dart) в демопроекте TUILiveKit с открытым исходным кодом.

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';class _AudioEffectPanelWidgetState {  final _audioEffectStore = AudioEffectStore.shared;  final _deviceStore = DeviceStore.shared;}
```

### Шаг 3: Реализация мониторинга в наушниках

Мониторинг в наушниках позволяет пользователям слышать входной сигнал своего микрофона в реальном времени. Вы можете управлять этой функцией, используя описанные ниже API.

> **Примечание:** функция мониторинга в наушниках обычно требует подключения наушников для правильной работы.

1. **Включение/отключение мониторинга в наушниках**: используйте виджет Switch для включения или отключения мониторинга в наушниках.
2. **Установка громкости мониторинга в наушниках**: используйте виджет Slider для установки громкости. Сопоставьте значение ползунка с параметром громкости и вызовите `setVoiceEarMonitorVolume(volume)`. Допустимый диапазон — [0, 150], поэтому сопоставьте значение элемента управления вашего интерфейса (например, ползунок 0,0–1,0) с диапазоном 0–150.
3. **Прослушивание обновлений состояния для обновления UI**: прослушивайте изменения состояния мониторинга в наушниках в реальном времени для соответствующего обновления вашего интерфейса.

#### Пример кода

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';/// Компонент управления мониторингом в наушниках class EarMonitorWidget extends StatelessWidget {  const EarMonitorWidget({super.key});  @override  Widget build(BuildContext context) {    final audioEffectStore = AudioEffectStore.shared;    return Column(      crossAxisAlignment: CrossAxisAlignment.start,      children: [        // 1. Включение/отключение мониторинга в наушниках        ValueListenableBuilder<bool>(          valueListenable: audioEffectStore.audioEffectState.isEarMonitorOpened,          builder: (context, isOpened, child) {            return SwitchListTile(              title: const Text('Ear Monitoring'),              subtitle: const Text('Insert a headset')              value: isOpened,              onChanged: (value) {                audioEffectStore.setVoiceEarMonitorEnable(value);              },            );          },        ),        // 2. Регулировка громкости мониторинга в наушниках        ValueListenableBuilder<int>(          valueListenable: audioEffectStore.audioEffectState.earMonitorVolume,          builder: (context, volume, child) {            return ListTile(              title: const Text('Ear Monitoring Volume'),              subtitle: Slider(                value: volume.toDouble(),                min: 0,                max: 150,                divisions: 150,                onChanged: (value) {                  audioEffectStore.setVoiceEarMonitorVolume(value.toInt());                },              ),              trailing: Text('$volume'),            );          },        ),      ],    );  }}
```

#### Параметры API SetVoiceEarMonitorEnable

| **Имя параметра** | **Тип** | **Описание** |
| --- | --- | --- |
| `enable` | `bool` | Включить мониторинг в наушниках:`true`: включить.`false`: отключить. |

#### Параметры API SetVoiceEarMonitorVolume

| **Имя параметра** | **Тип** | **Описание** |
| --- | --- | --- |
| `volume` | `int` | Громкость мониторинга в наушниках.Диапазон значений: от 0 до 150.Значение по умолчанию: 100. |

### Шаг 4: Регулировка громкости микрофона

Для управления громкостью захвата микрофона ведущего вызовите `DeviceStore.setCaptureVolume(volume)` с желаемым значением.

1. **Установка громкости захвата**: вы можете использовать элемент управления `Slider` для перетаскивания ползунка влево и вправо для регулировки громкости и сопоставить значение `Slider` со значением громкости перед вызовом `setCaptureVolume(volume)`. Обратите внимание, что этот API принимает диапазон параметров `[0, 150]`, поэтому вам необходимо сопоставить значение элемента управления интерфейса (такого как `0.0 - 1.0` ползунка) с диапазоном `0 - 150`.
2. **Подписка на обновления состояния**: прослушивайте изменения громкости захвата в реальном времени для обновления вашего интерфейса.

#### Пример кода

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';/// Компонент управления громкостью голоса class CaptureVolumeWidget extends StatelessWidget {  const CaptureVolumeWidget({super.key});  @override  Widget build(BuildContext context) {    final deviceStore = DeviceStore.shared;    return ValueListenableBuilder<int>(      valueListenable: deviceStore.state.captureVolume,      builder: (context, volume, child) {        return ListTile(          title: const Text('Voice Volume'),          subtitle: Slider(            value: volume.toDouble(),            min: 0,            max: 150,            divisions: 150,            onChanged: (value) {              deviceStore.setCaptureVolume(value.toInt());            },          ),          trailing: Text('$volume'),        );      },    );  }}
```

#### Параметры API SetCaptureVolume

| **Имя параметра** | **Тип** | **Описание** |
| --- | --- | --- |
| `volume` | `int` | Размер громкости захвата.Диапазон значений: от 0 до 150.Значение по умолчанию: 100. |

### Шаг 5: Применение эффектов изменения голоса

Для изменения голоса ведущего вызовите `setAudioChangerType(type)` и передайте желаемое значение перечисления.

#### Пример кода

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';/// Компонент выбора эффекта изменения голоса class VoiceChangerWidget extends StatelessWidget {  const VoiceChangerWidget({super.key});  @override  Widget build(BuildContext context) {    final audioEffectStore = AudioEffectStore.shared;    return Column(      crossAxisAlignment: CrossAxisAlignment.start,      children: [        const Padding(          padding: EdgeInsets.all(16),          child: Text('Voice-changing effect', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),        ),        ValueListenableBuilder<AudioChangerType>(          valueListenable: audioEffectStore.audioEffectState.audioChangerType,          builder: (context, changerType, child) {            return Padding(              padding: const EdgeInsets.symmetric(horizontal: 16),              child: Wrap(                spacing: 8,                runSpacing: 8,                children: AudioChangerType.values.map((type) {                  return ChoiceChip(                    label: Text(_getChangerTypeName(type)),                    selected: changerType == type,                    onSelected: (selected) {                      if (selected) {                        audioEffectStore.setAudioChangerType(type);                      }                    },                  );                }).toList(),              ),            );          },        ),      ],    );  }  String _getChangerTypeName(AudioChangerType type) {    switch (type) {      case AudioChangerType.none:        return 'Disable';      case AudioChangerType.child:        return 'mischievous child';      case AudioChangerType.girl:        return 'loli';      case AudioChangerType.uncle:        return 'uncle';      case AudioChangerType.ethereal:        return 'ethereal';    }  }}
```

#### Параметры API SetAudioChangerType

| **Имя параметра** | **Тип** | **Описание** |
| --- | --- | --- |
| `type` | [AudioChangerType](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_audio_effect_store/AudioChangerType.html) | Перечисление эффектов изменения голоса. |

### Шаг 6: Применение эффектов реверберации

Для добавления эффектов реверберации к голосу ведущего вызовите `setAudioReverbType(type)` и передайте желаемое значение перечисления.

#### Пример кода

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';/// Компонент выбора эффекта реверберации class ReverbWidget extends StatelessWidget {  const ReverbWidget({super.key});  @override  Widget build(BuildContext context) {    final audioEffectStore = AudioEffectStore.shared;    return Column(      crossAxisAlignment: CrossAxisAlignment.start,      children: [        const Padding(          padding: EdgeInsets.all(16),          child: Text('Reverb effect', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),        ),        ValueListenableBuilder<AudioReverbType>(          valueListenable: audioEffectStore.audioEffectState.audioReverbType,          builder: (context, reverbType, child) {            return Padding(              padding: const EdgeInsets.symmetric(horizontal: 16),              child: Wrap(                spacing: 8,                runSpacing: 8,                children: AudioReverbType.values.map((type) {                  return ChoiceChip(                    label: Text(_getReverbTypeName(type)),                    selected: reverbType == type,                    onSelected: (selected) {                      if (selected) {                        audioEffectStore.setAudioReverbType(type);                      }                    },                  );                }).toList(),              ),            );          },        ),      ],    );  }  String _getReverbTypeName(AudioReverbType type) {    switch (type) {      case AudioReverbType.none:        return 'Disable';      case AudioReverbType.ktv:        return 'KTV';      case AudioReverbType.room:        return 'Small room';      case AudioReverbType.hall:        return 'Great hall';      case AudioReverbType.deep:        return 'deep';      case AudioReverbType.loud:        return 'resonant';      case AudioReverbType.metallic:        return 'metallic sound';      case AudioReverbType.magnetic:        return 'magnetic';      case AudioReverbType.recordingStudio:        return 'studio';    }  }}
```

#### Параметры API SetAudioReverbType

| **Имя параметра** | **Тип** | **Описание** |
| --- | --- | --- |
| `type` | [AudioReverbType](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_audio_effect_store/AudioReverbType.html) | Перечисление эффектов реверберации. |

### Шаг 7: Сброс настроек звуковых эффектов

> **Важно:** AudioEffectStore и DeviceStore являются одноэкземплярными (singleton), поэтому настройки звуковых эффектов и устройства действуют глобально. Если вы не хотите, чтобы параметры текущей комнаты потоковой трансляции влияли на другие комнаты потоковой трансляции, созданные позже, необходимо сбросить параметры звуковых эффектов и устройства при завершении текущей комнаты потоковой трансляции.

Может потребоваться сбросить параметры звуковых эффектов в следующих двух сценариях:

1. **При завершении текущей комнаты потоковой трансляции** вызовите метод `reset()` хранилища для сброса звуковых эффектов.
2. **Когда требуется сбросить все параметры устройств и звуковых эффектов** вызовите метод `reset()` хранилища для сброса звуковых эффектов.

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';/// Компонент сброса звуковых эффектов class AudioEffectResetWidget extends StatelessWidget {  const AudioEffectResetWidget({super.key});  void _resetAudioEffect() {    AudioEffectStore.shared.reset();    DeviceStore.shared.reset();  }  @override  Widget build(BuildContext context) {    return ElevatedButton(      onPressed: _resetAudioEffect,      child: const Text('Reset sound effect settings'),    );  }}
```

## Полный пример кода

```
import 'package:flutter/material.dart';import 'package:atomic_x_core/atomicxcore.dart';/// Страница настроек звуковых эффектов class AudioEffectPage extends StatelessWidget {  const AudioEffectPage({super.key});  @override  Widget build(BuildContext context) {    final audioEffectStore = AudioEffectStore.shared;    final deviceStore = DeviceStore.shared;    return Scaffold(      appBar: AppBar(title: const Text('Sound effect settings')),      body: ListView(        children: [          // Voice volume          const Padding(            padding: EdgeInsets.all(16),            child: Text('Voice volume', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),          ),          ValueListenableBuilder<int>(            valueListenable: deviceStore.state.captureVolume,            builder: (context, volume, child) {              return ListTile(                title: const Text('Capture Volume'),                subtitle: Slider(                  value: volume.toDouble(),                  min: 0,                  max: 150,                  divisions: 150,                  onChanged: (value) {                    deviceStore.setCaptureVolume(value.toInt());                  },                ),                trailing: Text('$volume'),              );            },          ),          const Divider(),          // Ear return settings          const Padding(            padding: EdgeInsets.all(16),            child: Text('Ear monitoring', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),          ),          ValueListenableBuilder<bool>(            valueListenable: audioEffectStore.audioEffectState.isEarMonitorOpened,            builder: (context, isOpened, child) {              return SwitchListTile(                title: const Text('Enable Ear Monitoring'),                subtitle: const Text('Insert a headset')                value: isOpened,                onChanged: (value) {                  audioEffectStore.setVoiceEarMonitorEnable(value);                },              );            },          ),          ValueListenableBuilder<int>(            valueListenable: audioEffectStore.audioEffectState.earMonitorVolume,            builder: (context, volume, child) {              return ListTile(                title: const Text('Ear Monitoring Volume'),                subtitle: Slider(                  value: volume.toDouble(),                  min: 0,                  max: 150,                  divisions: 150,                  onChanged: (value) {                    audioEffectStore.setVoiceEarMonitorVolume(value.toInt());                  },                ),                trailing: Text('$volume'),              );            },          ),          const Divider(),          // Voice changing settings          const Padding(            padding: EdgeInsets.all(16),            child: Text('Voice-changing', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),          ),          ValueListenableBuilder<AudioChangerType>(            valueListenable: audioEffectStore.audioEffectState.audioChangerType,            builder: (context, changerType, child) {              return Padding(                padding: const EdgeInsets.symmetric(horizontal: 16),                child: Wrap(                  spacing: 8,                  runSpacing: 8,                  children: AudioChangerType.values.map((type) {                    return ChoiceChip(                      label: Text(_getChangerTypeName(type)),                      selected: changerType == type,                      onSelected: (selected) {                        if (selected) {                          audioEffectStore.setAudioChangerType(type);                        }                      },                    );                  }).toList(),                ),              );            },          ),          const SizedBox(height: 16),          const Divider(),          // Reverb settings          const Padding(            padding: EdgeInsets.all(16),            child: Text('Reverb', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),          ),          ValueListenableBuilder<AudioReverbType>(            valueListenable: audioEffectStore.audioEffectState.audioReverbType,            builder: (context, reverbType, child) {              return Padding(                padding: const EdgeInsets.symmetric(horizontal: 16),                child: Wrap(                  spacing: 8,                  runSpacing: 8,                  children: AudioReverbType.values.map((type) {                    return ChoiceChip(                      label: Text(_getReverbTypeName(type)),                      selected: reverbType == type,                      onSelected: (selected) {                        if (selected) {                          audioEffectStore.setAudioReverbType(type);                        }                      },                    );                  }).toList(),                ),              );            },          ),          const SizedBox(height: 24),          // reset button          Padding(            padding: const EdgeInsets.all(16),            child: ElevatedButton(              onPressed: () {                audioEffectStore.reset();                deviceStore.reset();              },              child: const Text('Reset sound effect settings'),            ),          ),        ],      ),    );  }  String _getChangerTypeName(AudioChangerType type) {    switch (type) {      case AudioChangerType.none:        return 'Disable';      case AudioChangerType.child:        return 'mischievous child';      case AudioChangerType.girl:        return 'loli';      case AudioChangerType.uncle:        return 'uncle';      case AudioChangerType.ethereal:        return 'ethereal';    }  }  String _getReverbTypeName(AudioReverbType type) {    switch (type) {      case AudioReverbType.none:        return 'Disable';      case AudioReverbType.ktv:        return 'KTV';      case AudioReverbType.room:        return 'Small room';      case AudioReverbType.hall:        return 'Great hall';      case AudioReverbType.deep:        return 'deep';      case AudioReverbType.loud:        return 'resonant';      case AudioReverbType.metallic:        return 'metallic sound';      case AudioReverbType.magnetic:        return 'magnetic';      case AudioReverbType.recordingStudio:        return 'studio';    }  }}
```

## Документация API

Подробная информация о всех открытых интерфейсах и атрибутах [AudioEffectStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_audio_effect_store/AudioEffectStore-class.html), [DeviceStore](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_device_store/DeviceStore-class.html) и связанных классов доступна в официальной документации API фреймворка [AtomicXCore](https://tencent-rtc.github.io/TUIKit_Flutter/index.html).

| **Store/компонент** | **Описание функции** | **Справка по API** |
| --- | --- | --- |
| **AudioEffectStore** | Управление звуковыми эффектами: выполнение параметров звуковых эффектов и получение состояния звуковых эффектов в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_audio_effect_store/AudioEffectStore-class.html) |
| **DeviceStore** | Управление устройством: выполнение операций с камерой и микрофоном и получение состояния устройства в реальном времени. | [Документация API](https://tencent-rtc.github.io/TUIKit_Flutter/api_device_device_store/DeviceStore-class.html) |

## Часто задаваемые вопросы

### Есть ли какие-либо ограничения на время вызова API звуковых эффектов и устройства?

Нет, никаких ограничений. Параметры в `AudioEffectStore` и `DeviceStore` являются глобальными. Вы можете вызывать связанные API (такие как установка изменения голоса, реверберации или мониторинга в наушниках) в любое время до или после присоединения к комнате потоковой трансляции. Изменения вступают в силу немедленно и сохраняются.

### В чем разница между "Громкостью микрофона" и "Громкостью мониторинга в наушниках"?

Это частая причина путаницы. Различия следующие:

- Громкость микрофона (громкость захвата): установлена через `DeviceStore.shared.setCaptureVolume()`. Управляет тем, насколько громко ведущий звучит для аудитории.
- Громкость мониторинга в наушниках (громкость мониторинга в наушниках): установлена через `AudioEffectStore.shared.setVoiceEarMonitorVolume()`. Контролирует только то, насколько громко ведущий слышит себя в наушниках и не влияет на аудиторию.

### Почему в только что созданной комнате потоковой трансляции уже есть звуковые эффекты или громкость неожиданно высокая или низкая?

Потому что `AudioEffectStore` и `DeviceStore` являются одноэкземплярными (singleton), параметры звуковых эффектов и устройства являются глобальными. Это обычно происходит, если вы ранее устанавливали звуковые эффекты и не сбросили их. Обязательно вызывайте `reset()` когда это необходимо.

### Почему я не слышу себя после включения "Мониторинга в наушниках"?

Проверьте следующее:

1. Подключены ли наушники? Мониторинг в наушниках обычно требует наушников. Убедитесь, что подключены проводные или Bluetooth наушники.
2. Установлена ли громкость на 0? Убедитесь, что "Громкость мониторинга в наушниках" не установлена на 0.
3. Включен ли микрофон? Убедитесь, что микрофон в DeviceStore включен (т. е. был вызван `openLocalMicrophone()`).

### Можно ли использовать эффекты изменения голоса и реверберации одновременно?

Да. `AudioChangerType` и `AudioReverbType` можно использовать вместе. Например, вы можете применять одновременно как `AudioChangerType.girl`, так и `AudioReverbType.ktv`.


---
*Источник: [https://trtc.io/document/77558](https://trtc.io/document/77558)*

---
*Источник (EN): [sound-effects.md](./sound-effects.md)*
