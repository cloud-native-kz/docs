# TXDeviceManager

Авторские права (c) 2021 Tencent. Все права защищены.

Модуль: модуль управления аудио/видео устройствами

Описание: управляет аудио/видео устройствами, такими как камера, микрофон и динамик.

**TXDeviceManager**

## TXDeviceObserver

| FuncList | DESC |
| --- | --- |
| [onDeviceChanged:type:state:](https://www.tencentcloud.com/document/product/647/50759#dfd15b3a97c8d91d85618afb47ea252f) | Статус локального устройства изменился (только для настольных ОС). |

## TXDeviceManager

| FuncList | DESC |
| --- | --- |
| [isFrontCamera](https://www.tencentcloud.com/document/product/647/50759#6d3ec289d7e2325835e0d1da358103a6) | Запрос о том, используется ли передняя камера. |
| [switchCamera:](https://www.tencentcloud.com/document/product/647/50759#a6c41b29145df78c75f83db394a5757d) | Переключение на переднюю/заднюю камеру (для мобильных ОС). |
| [isCameraZoomSupported](https://www.tencentcloud.com/document/product/647/50759#3d221dfef2379ff2d7465873b190d279) | Запрос о том, поддерживает ли текущая камера масштабирование (для мобильных ОС). |
| [getCameraZoomMaxRatio](https://www.tencentcloud.com/document/product/647/50759#36e2b33316fc8b7a9d4ba089594c77ff) | Получение максимального коэффициента масштабирования камеры (для мобильных ОС). |
| [setCameraZoomRatio:](https://www.tencentcloud.com/document/product/647/50759#aa61befc4a161b72e2a3eb9703e8ab8a) | Установка коэффициента масштабирования камеры (для мобильных ОС). |
| [isAutoFocusEnabled](https://www.tencentcloud.com/document/product/647/50759#a8d8a4fa66b628c21a080177204744b2) | Запрос о том, поддерживается ли автоматическое обнаружение лиц (для мобильных ОС). |
| [enableCameraAutoFocus:](https://www.tencentcloud.com/document/product/647/50759#b73d99629f1936b786b6ada790e458dd) | Включение автофокуса (для мобильных ОС). |
| [setCameraFocusPosition:](https://www.tencentcloud.com/document/product/647/50759#2f2ceca9ad0f46650334e6b5aa813633) | Регулировка фокуса (для мобильных ОС). |
| [isCameraTorchSupported](https://www.tencentcloud.com/document/product/647/50759#0f67ffd852a08dc7735f51d3b3f0f163) | Запрос о том, поддерживается ли вспышка (для мобильных ОС). |
| [enableCameraTorch:](https://www.tencentcloud.com/document/product/647/50759#bf86fe99b08324c7114c2da6875baca9) | Включение/отключение вспышки, т.е. режима фонарика (для мобильных ОС). |
| [setAudioRoute:](https://www.tencentcloud.com/document/product/647/50759#669f49baa33336be868377f8bc8e6f32) | Установка маршрута аудио (для мобильных ОС). |
| [setExposureCompensation:](https://www.tencentcloud.com/document/product/647/50759#da0dea11c433416dc2b20e27937bc92f) | Установка параметров экспозиции камеры в диапазоне от -1 до 1. |
| [getDevicesList:](https://www.tencentcloud.com/document/product/647/50759#cf4514b579d88cadae56a424baeb110f) | Получение списка устройств (для настольных ОС). |
| [setCurrentDevice:deviceId:](https://www.tencentcloud.com/document/product/647/50759#1c0a01aa96ce0aa6c596c654041fbee6) | Установка устройства для использования (для настольных ОС). |
| [getCurrentDevice:](https://www.tencentcloud.com/document/product/647/50759#c56fd31ac73ceda8a28d9f4bfe834bbd) | Получение используемого в данный момент устройства (для настольных ОС). |
| [setCurrentDeviceVolume:deviceType:](https://www.tencentcloud.com/document/product/647/50759#aefc135c5b1cf942a4d7445274fa2465) | Установка громкости текущего устройства (для настольных ОС). |
| [getCurrentDeviceVolume:](https://www.tencentcloud.com/document/product/647/50759#1fc1b55bc7722cc70a07302e46507467) | Получение громкости текущего устройства (для настольных ОС). |
| [setCurrentDeviceMute:deviceType:](https://www.tencentcloud.com/document/product/647/50759#647a252eb815bae8854023af3717a79f) | Отключение звука текущего устройства (для настольных ОС). |
| [getCurrentDeviceMute:](https://www.tencentcloud.com/document/product/647/50759#7b46a3e3052b4b59e685fb8365c3955d) | Запрос о том, отключен ли звук текущего устройства (для настольных ОС). |
| [enableFollowingDefaultAudioDevice:enable:](https://www.tencentcloud.com/document/product/647/50759#f1a3e4a48a4a2e81e7d0eee4c9f37bb7) | Установка следования аудиоустройства, используемого SDK, системному устройству по умолчанию (для настольных ОС). |
| [startCameraDeviceTest:](https://www.tencentcloud.com/document/product/647/50759#e2d8e209071fef8bbf78f16971bae39f) | Начало тестирования камеры (для настольных ОС). |
| [stopCameraDeviceTest](https://www.tencentcloud.com/document/product/647/50759#30be4cfa94699be138130c1919b3af68) | Завершение тестирования камеры (для настольных ОС). |
| [startMicDeviceTest:](https://www.tencentcloud.com/document/product/647/50759#3dce7bfcf95708a5ce69f5ce7baad6f4) | Начало тестирования микрофона (для настольных ОС). |
| [startMicDeviceTest:playback:](https://www.tencentcloud.com/document/product/647/50759#f4002f97005e59258de6fe5088ae75b8) | Начало тестирования микрофона (для настольных ОС). |
| [stopMicDeviceTest](https://www.tencentcloud.com/document/product/647/50759#d0adbc1fbeae9620cf4c78d06b24d26e) | Завершение тестирования микрофона (для настольных ОС). |
| [startSpeakerDeviceTest:](https://www.tencentcloud.com/document/product/647/50759#e4ac7cc2a6dbecee30b0b4a9a17ce3b3) | Начало тестирования динамика (для настольных ОС). |
| [stopSpeakerDeviceTest](https://www.tencentcloud.com/document/product/647/50759#d9f52ca878aa99ec873170b4bc394f11) | Завершение тестирования динамика (для настольных ОС). |
| [setObserver:](https://www.tencentcloud.com/document/product/647/50759#e277523e1a2b2426d66ef6fdecae1fb8) | Установка обратного вызова onDeviceChanged (для Mac). |
| [setCameraCapturerParam:](https://www.tencentcloud.com/document/product/647/50759#0d4167b17f3b52529be4b7a04f648a0d) | Установка предпочтений захвата камеры. |
| [setSystemVolumeType:](https://www.tencentcloud.com/document/product/647/50759#632301e178fc664876e5888669368049) | Установка типа системного звука (для мобильных ОС). |

## StructType

| FuncList | DESC |
| --- | --- |
| [TXCameraCaptureParam](https://www.tencentcloud.com/document/product/647/50759#654f738285ec7c055a692afa6ed803ea) | Параметры захвата камеры. |
| [TXMediaDeviceInfo](https://www.tencentcloud.com/document/product/647/50759#39885544680b92cd423ccc7141a3fe96) | Информация об аудио/видео устройстве (для настольных ОС). |

## EnumType

| EnumType | DESC |
| --- | --- |
| [TXSystemVolumeType](https://www.tencentcloud.com/document/product/647/50759#9e22ac3a1dd66fee5bed02bc61c5e58b) | Тип системного звука. |
| [TXAudioRoute](https://www.tencentcloud.com/document/product/647/50759#39c508dc7c357c2feda25e56f2d729c1) | Маршрут аудио (маршрут воспроизведения аудио). |
| [TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b) | Тип устройства (для настольных ОС). |
| [TXMediaDeviceState](https://www.tencentcloud.com/document/product/647/50759#0e59520d0b5cd9b6826a30ea0dbba8f7) | Операция устройства. |
| [TXCameraCaptureMode](https://www.tencentcloud.com/document/product/647/50759#aede0b6f9c933df04f1b4e096ced41e6) | Предпочтения захвата камеры. |

## onDeviceChanged:type:state:

**onDeviceChanged:type:state:**

| - (void)onDeviceChanged: | (NSString*)deviceId |
| --- | --- |
| type: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))mediaType |
| state: | ([TXMediaDeviceState](https://www.tencentcloud.com/document/product/647/50759#0e59520d0b5cd9b6826a30ea0dbba8f7))mediaState |

**Статус локального устройства изменился (только для настольных ОС).**

SDK возвращает этот обратный вызов, когда локальное устройство (камера, микрофон или динамик) подключается или отключается.

| Param | DESC |
| --- | --- |
| deviceId | Идентификатор устройства |
| state | Статус устройства. `0`: подключено; `1`: отключено; `2`: запущено |
| type | Тип устройства |

## isFrontCamera

**isFrontCamera**

**Запрос о том, используется ли передняя камера.**

## switchCamera:

**switchCamera:**

| - (NSInteger)switchCamera: | (BOOL)frontCamera |
| --- | --- |

**Переключение на переднюю/заднюю камеру (для мобильных ОС).**

## isCameraZoomSupported

**isCameraZoomSupported**

**Запрос о том, поддерживает ли текущая камера масштабирование (для мобильных ОС).**

## getCameraZoomMaxRatio

**getCameraZoomMaxRatio**

**Получение максимального коэффициента масштабирования камеры (для мобильных ОС).**

## setCameraZoomRatio:

**setCameraZoomRatio:**

| - (NSInteger)setCameraZoomRatio: | (CGFloat)zoomRatio |
| --- | --- |

**Установка коэффициента масштабирования камеры (для мобильных ОС).**

| Param | DESC |
| --- | --- |
| zoomRatio | Диапазон значений: [1, 5]. Значение 1 обозначает самый широкий угол обзора (исходный), а 5 - самый узкий угол обзора (увеличенный). Максимальное значение рекомендуется устанавливать в 5. Если значение превышает 5, видео будет размытым. |

## isAutoFocusEnabled

**isAutoFocusEnabled**

**Запрос о том, поддерживается ли автоматическое обнаружение лиц (для мобильных ОС).**

## enableCameraAutoFocus:

**enableCameraAutoFocus:**

| - (NSInteger)enableCameraAutoFocus: | (BOOL)enabled |
| --- | --- |

**Включение автофокуса (для мобильных ОС).**

После включения автофокуса камера будет автоматически обнаруживать и всегда фокусироваться на лица.

## setCameraFocusPosition:

**setCameraFocusPosition:**

| - (NSInteger)setCameraFocusPosition: | (CGPoint)position |
| --- | --- |

**Регулировка фокуса (для мобильных ОС).**

Этот API можно использовать для следующего:

1. Пользователь может нажать на предпросмотр камеры.

2. На месте нажатия пользователя появится прямоугольник, указывающий на точку, на которую будет сфокусирована камера.

3. Пользователь передает координаты точки в SDK с помощью этого API, и SDK дает указание камере фокусироваться в соответствии с требованиями.

| Param | DESC |
| --- | --- |
| position | Точка фокусировки. Передайте координаты точки, на которой требуется сфокусироваться. |

> **Примечание** Перед использованием этого API необходимо сначала отключить автофокус с помощью [enableCameraAutoFocus](https://www.tencentcloud.com/document/product/647/50759#b73d99629f1936b786b6ada790e458dd).

**Описание возвращаемого значения:**

0: операция успешна; отрицательное число: операция не удалась.

## isCameraTorchSupported

**isCameraTorchSupported**

**Запрос о том, поддерживается ли вспышка (для мобильных ОС).**

## enableCameraTorch:

**enableCameraTorch:**

| - (NSInteger)enableCameraTorch: | (BOOL)enabled |
| --- | --- |

**Включение/отключение вспышки, т.е. режима фонарика (для мобильных ОС).**

## setAudioRoute:

**setAudioRoute:**

| - (NSInteger)setAudioRoute: | ([TXAudioRoute](https://www.tencentcloud.com/document/product/647/50759#39c508dc7c357c2feda25e56f2d729c1))route |
| --- | --- |

**Установка маршрута аудио (для мобильных ОС).**

Мобильный телефон имеет два устройства воспроизведения аудио: приемник в верхней части и динамик в нижней части.

Если маршрут аудио установлен на приемник, громкость относительно низкая, и звук можно услышать только при поднесении телефона к уху. Этот режим обеспечивает высокий уровень конфиденциальности и подходит для ответов на вызовы.

Если маршрут аудио установлен на динамик, громкость относительно высокая, и не требуется поднесение телефона к уху. Этот режим обеспечивает функцию "громкой связи".

## setExposureCompensation:

**setExposureCompensation:**

| - (NSInteger)setExposureCompensation: | (CGFloat)value |
| --- | --- |

**Установка параметров экспозиции камеры в диапазоне от -1 до 1.**

## getDevicesList:

**getDevicesList:**

| - (NSArray<TXMediaDeviceInfo *> * _Nullable)getDevicesList: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |
| --- | --- |

**Получение списка устройств (для настольных ОС).**

| Param | DESC |
| --- | --- |
| type | Тип устройства. Установите его на тип устройства, которое вы хотите получить. Более подробную информацию см. в определении [TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b). |

> **Примечание** Для обеспечения управления жизненным циклом объекта `ITXDeviceCollection` SDK после использования этого API необходимо вызвать метод `release` для освобождения ресурсов. Не используйте `delete` для освобождения объекта Collection, так как удаление указателя ITXDeviceCollection* приведет к сбою. Допустимые значения `type` - это `TXMediaDeviceTypeMic`, `TXMediaDeviceTypeSpeaker` и `TXMediaDeviceTypeCamera`. Этот API можно использовать только на macOS и Windows.

## setCurrentDevice:deviceId:

**setCurrentDevice:deviceId:**

| - (NSInteger)setCurrentDevice: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |
| --- | --- |
| deviceId: | (NSString *)deviceId |

**Установка устройства для использования (для настольных ОС).**

| Param | DESC |
| --- | --- |
| deviceId | Идентификатор устройства. Вы можете получить ID устройства с помощью API [getDevicesList](https://www.tencentcloud.com/document/product/647/50759#cf4514b579d88cadae56a424baeb110f). |
| type | Тип устройства. Более подробную информацию см. в определении `TXMediaDeviceType`. |

**Описание возвращаемого значения:**

0: операция успешна; отрицательное число: операция не удалась.

## getCurrentDevice:

**getCurrentDevice:**

| - (TXMediaDeviceInfo * _Nullable)getCurrentDevice: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |
| --- | --- |

**Получение используемого в данный момент устройства (для настольных ОС).**

## setCurrentDeviceVolume:deviceType:

**setCurrentDeviceVolume:deviceType:**

| - (NSInteger)setCurrentDeviceVolume: | (NSInteger)volume |
| --- | --- |
| deviceType: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |

**Установка громкости текущего устройства (для настольных ОС).**

Этот API используется для установки громкости захвата микрофона или громкости воспроизведения динамика, но не громкости камеры.

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 100]; по умолчанию: 100 |

## getCurrentDeviceVolume:

**getCurrentDeviceVolume:**

| - (NSInteger)getCurrentDeviceVolume: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |
| --- | --- |

**Получение громкости текущего устройства (для настольных ОС).**

Этот API используется для получения громкости захвата микрофона или громкости воспроизведения динамика, но не громкости камеры.

## setCurrentDeviceMute:deviceType:

**setCurrentDeviceMute:deviceType:**

| - (NSInteger)setCurrentDeviceMute: | (BOOL)mute |
| --- | --- |
| deviceType: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |

**Отключение звука текущего устройства (для настольных ОС).**

Этот API используется для отключения звука микрофона или динамика, но не камеры.

## getCurrentDeviceMute:

**getCurrentDeviceMute:**

| - (BOOL)getCurrentDeviceMute: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |
| --- | --- |

**Запрос о том, отключен ли звук текущего устройства (для настольных ОС).**

Этот API используется для запроса о том, отключен ли звук микрофона или динамика. Отключение звука камеры не поддерживается.

## enableFollowingDefaultAudioDevice:enable:

**enableFollowingDefaultAudioDevice:enable:**

| - (NSInteger)enableFollowingDefaultAudioDevice: | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50759#f023a4d94be317eb399df83a25af6b2b))type |
| --- | --- |
| enable: | (BOOL)enable |

**Установка следования аудиоустройства, используемого SDK, системному устройству по умолчанию (для настольных ОС).**

Этот API используется для установки типов микрофона и динамика. Следование камеры за системным устройством по умолчанию не поддерживается.

| Param | DESC |
| --- | --- |
| enable | Следовать ли системному аудиоустройству по умолчанию. true: следовать. Когда устройство аудио по умолчанию в системе изменяется или подключается новое аудиоустройство, SDK немедленно переключает аудиоустройство. false: не следовать. Когда устройство аудио по умолчанию в системе изменяется или подключается новое аудиоустройство, SDK не переключает аудиоустройство. |
| type | Тип устройства. Более подробную информацию см. в определении `TXMediaDeviceType`. |

## startCameraDeviceTest:

**startCameraDeviceTest:**

| - (NSInteger)startCameraDeviceTest: | (NSView *)view |
| --- | --- |

**Начало тестирования камеры (для настольных ОС).**

> **Примечание** Во время тестирования вы можете использовать API [setCurrentDevice](https://www.tencentcloud.com/document/product/647/50759#1c0a01aa96ce0aa6c596c654041fbee6) для переключения между камерами.

## stopCameraDeviceTest

**stopCameraDeviceTest**

**Завершение тестирования камеры (для настольных ОС).**

## startMicDeviceTest:

**startMicDeviceTest:**

| - (NSInteger)startMicDeviceTest: | (NSInteger)interval |
| --- | --- |

**Начало тестирования микрофона (для настольных ОС).**

Этот API используется для проверки правильной работы микрофона. Обнаруженная громкость микрофона (диапазон значений: [0, 100]) возвращается через обратный вызов.

| Param | DESC |
| --- | --- |
| interval | Интервал обратных вызовов громкости в миллисекундах. |

> **Примечание** При вызове этого интерфейса звук, записываемый микрофоном, по умолчанию будет воспроизводиться динамиками.

## startMicDeviceTest:playback:

**startMicDeviceTest:playback:**

| - (NSInteger)startMicDeviceTest: | (NSInteger)interval |
| --- | --- |
| playback: | (BOOL)playback |

**Начало тестирования микрофона (для настольных ОС).**

Этот API используется для проверки правильной работы микрофона. Обнаруженная громкость микрофона (диапазон значений: [0, 100]) возвращается через обратный вызов.

| Param | DESC |
| --- | --- |
| interval | Интервал обратных вызовов громкости в миллисекундах. |
| playback | Воспроизводить ли звук микрофона. Пользователь услышит свой собственный звук при тестировании микрофона, если `playback` имеет значение true. |

## stopMicDeviceTest

**stopMicDeviceTest**

**Завершение тестирования микрофона (для настольных ОС).**

## startSpeakerDeviceTest:

**startSpeakerDeviceTest:**

| - (NSInteger)startSpeakerDeviceTest: | (NSString *)audioFilePath |
| --- | --- |

**Начало тестирования динамика (для настольных ОС).**

Этот API используется для проверки правильной работы устройства воспроизведения аудио путем воспроизведения указанного аудиофайла. Если пользователи слышат аудио во время тестирования, устройство работает правильно.

| Param | DESC |
| --- | --- |
| filePath | Путь к аудиофайлу |

## stopSpeakerDeviceTest

**stopSpeakerDeviceTest**

**Завершение тестирования динамика (для настольных ОС).**

## setObserver:

**setObserver:**

| - (void)setObserver: | (nullable id<[TXDeviceObserver](https://www.tencentcloud.com/document/product/647/50759#57dea2455f64baf02792e6d2d227e200)>) observer |
| --- | --- |

**Установка обратного вызова onDeviceChanged (для Mac).**

## setCameraCapturerParam:

**setCameraCapturerParam:**

| - (void)setCameraCapturerParam: | ([TXCameraCaptureParam](https://www.tencentcloud.com/document/product/647/50759#654f738285ec7c055a692afa6ed803ea) *)params |
| --- | --- |

**Установка предпочтений захвата камеры.**

## setSystemVolumeType:

**setSystemVolumeType:**

| - (NSInteger)setSystemVolumeType: | ([TXSystemVolumeType](https://www.tencentcloud.com/document/product/647/50759#9e22ac3a1dd66fee5bed02bc61c5e58b))type |
| --- | --- |

**Установка типа системного звука (для мобильных ОС).**

@deprecated Этот API не рекомендуется после v9.5. Пожалуйста, используйте вместо него API `startLocalAudio(quality)` в `TRTCCloud`, параметр `quality` которого используется для определения качества аудио.

## TXSystemVolumeType(Deprecated)

**TXSystemVolumeType(Deprecated)**

**Тип системного звука.**

| Enum | Value | DESC |
| --- | --- | --- |
| TXSystemVolumeTypeAuto | 0 | Автоматический |
| TXSystemVolumeTypeMedia | 1 | Звук мультимедиа |
| TXSystemVolumeTypeVOIP | 2 | Громкость вызова |

## TXAudioRoute

**TXAudioRoute**

**Маршрут аудио (маршрут воспроизведения аудио).**

Маршрут аудио - это маршрут (динамик или приемник), через который воспроизводится аудио. Применяется только к мобильным устройствам, таким как мобильные телефоны.

Мобильный телефон имеет два динамика: один в верхней части (приемник) и один в нижней части.

- Если маршрут аудио установлен на приемник, громкость относительно низкая, и звук можно услышать только при поднесении телефона к уху. Этот режим обеспечивает высокий уровень кон

---
*Источник (EN): [txdevicemanager.md](./txdevicemanager.md)*
