# Управление аудиторией

В данном документе основное внимание уделяется описанию использования SDK `RTC Room Engine` для реализации функций настройки аудио.

## Предварительные требования

Перед использованием функций настройки аудио, предоставляемых SDK `RTC Room Engine`, необходимо завершить [вход в SDK](https://www.tencentcloud.com/document/product/647/66960#) и убедиться, что вы находитесь в прямой комнате.

## Руководство пользователя

### Включение/выключение локального микрофона

iOS

Android

Вы можете включить или выключить локальный микрофон, вызвав API `openLocalMicrophone` и `closeLocalMicrophone` соответственно.

При вызове `openLocalMicrophone` для включения микрофона необходимо передать параметр типа `TUIAudioQuality` с именем `quality` для установки качества кодирования аудио. `TUIAudioQuality` включает следующие типы, которые вы можете выбрать в зависимости от ваших бизнес-требований:

| Типы значений перечисления | Значение |
| --- | --- |
| speech | Режим голоса. Моно; битрейт аудио: 18 кбит/с; подходит для сценариев голосовых вызовов. |
| default | Режим по умолчанию. Моно; битрейт аудио: 50 кбит/с; качество аудио SDK по умолчанию, рекомендуется, если нет специальных требований. |
| music | Режим музыки. Стерео + полный диапазон; битрейт аудио: 128 кбит/с; подходит для сценариев, требующих высокоточной передачи музыки, таких как онлайн-караоке и музыкальные прямые трансляции. |

Вы можете включить или выключить локальный микрофон, вызвав API `openLocalMicrophone` и `closeLocalMicrophone` соответственно.

При вызове `openLocalMicrophone` для включения микрофона необходимо передать параметр типа `AudioQuality` с именем `quality` для установки качества кодирования аудио. `AudioQuality` включает следующие типы, которые вы можете выбрать в зависимости от ваших бизнес-требований:

| Типы значений перечисления | Значение |
| --- | --- |
| SPEECH | Режим голоса. Моно; битрейт аудио: 18 кбит/с; подходит для сценариев голосовых вызовов. |
| DEFAULT | Режим по умолчанию. Моно; битрейт аудио: 50 кбит/с; качество аудио SDK по умолчанию, рекомендуется, если нет специальных требований. |
| MUSIC | Режим музыки. Стерео + полный диапазон; битрейт аудио: 128 кбит/с; подходит для сценариев, требующих высокоточной передачи музыки, таких как онлайн-караоке и музыкальные прямые трансляции. |

Ниже приведен пример включения и выключения локального микрофона в режиме по умолчанию.

iOS

Android

```
import RTCRoomEnginelet roomEngine = TUIRoomEngine.sharedInstance()// Turn on the local microphoneroomEngine.openLocalMicrophone(.default) {    // Successfully turned on the mic} onError: { code, message in    // Failed to turn on the mic}// Turn off the local microphoneroomEngine.closeLocalMicrophone()
```

```
TUIRoomEngine roomEngine = TUIRoomEngine.sharedInstance();// Turn on the local microphoneroomEngine.openLocalMicrophone(TUIRoomDefine.AudioQuality.DEFAULT, new TUIRoomDefine.ActionCallback() {    @Override    public void onSuccess() {        // Successfully turned on the mic    }    @Override    public void onError(TUICommonDefine.Error error, String message) {        // Failed to turn on the mic    }});// Turn off the local microphoneroomEngine.closeLocalMicrophone();
```

### Обновление качества кодирования локального аудио

iOS

Android

При обновлении качества кодирования локального аудио тип параметра `TUIAudioQuality` аналогичен упомянутому выше. Ниже приведен пример использования режима по умолчанию для вызова API `updateAudioQuality` для обновления качества кодирования локального аудио:

```
import RTCRoomEnginelet audioQuality: TUIAudioQuality = .defaultTUIRoomEngine.sharedInstance().updateAudioQuality(audioQuality)
```

При обновлении качества кодирования локального аудио тип параметра `AudioQuality` аналогичен упомянутому выше. Ниже приведен пример использования режима по умолчанию для вызова API `updateAudioQuality` для обновления качества кодирования локального аудио:

```
TUIRoomDefine.AudioQuality audioQuality = TUIRoomDefine.AudioQuality.DEFAULT;TUIRoomEngine.sharedInstance().updateAudioQuality(audioQuality);
```

### Приостановка/возобновление публикации локального аудиопотока

Находясь в прямой комнате, вам может потребоваться приостановить/возобновить публикацию вашего локального аудиопотока. Вы можете достичь этого, вызвав следующий API:

iOS

Android

```
import RTCRoomEnginelet roomEngine = TUIRoomEngine.sharedInstance()// Pause publishing local audio streamsroomEngine.muteLocalAudio()// Resume publishing local audio streamsroomEngine.unmuteLocalAudio() {    // Resume publishing successful} onError: { code, message in    // Resume publishing failed}
```

```
TUIRoomEngine roomEngine = TUIRoomEngine.sharedInstance();// Pause publishing local audio streamsroomEngine.muteLocalAudio();// Resume publishing local audio streamsroomEngine.unmuteLocalAudio(new TUIRoomDefine.ActionCallback() {    @Override    public void onSuccess() {        // Resume publishing successful    }    @Override    public void onError(TUICommonDefine.Error error, String message) {        // Resume publishing failed    }});
```

> **Примечание:** В комнате, если вы включили микрофон, после вызова вышеприведенного API для приостановки/возобновления публикации локального аудиопотока SDK уведомит пользователей в комнате через обратный вызов `TUIRoomObserver` [onUserAudioStateChanged](https://www.tencentcloud.com/document/product/647/64184#57eafbcdec43b9cacef68034b3087e45).


---
*Источник: [https://trtc.io/document/67665](https://trtc.io/document/67665)*

---
*Источник (EN): [audience-management.md](./audience-management.md)*
