# ITXDeviceManager

Copyright (c) 2021 Tencent. All rights reserved.

Модуль: модуль управления аудио/видео устройствами

Описание: управляет аудио/видео устройствами, такими как камера, микрофон и динамик.

**ITXDeviceManager**

## ITXDeviceManager

| FuncList | DESC |
| --- | --- |
| [isFrontCamera](https://www.tencentcloud.com/document/product/647/50774#0f9d6b1396b1cafc2fe0e9e6995eaff1) | Проверка использования фронтальной камеры. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/50774#643e0deb4a02eccd7b1fa9e186353481) | Переключение между фронтальной и задней камерой (для мобильных ОС). |
| [getCameraZoomMaxRatio](https://www.tencentcloud.com/document/product/647/50774#3622c34b4499a12757e052a502f27408) | Получение максимального коэффициента масштабирования камеры (для мобильных ОС). |
| [setCameraZoomRatio](https://www.tencentcloud.com/document/product/647/50774#1200e0cde542f5e3cbf5ae703d68167b) | Установка коэффициента масштабирования камеры (для мобильных ОС). |
| [isAutoFocusEnabled](https://www.tencentcloud.com/document/product/647/50774#a9c12dfcdb51f9d45f8bee002b55d4f7) | Проверка поддержки автоматического обнаружения лиц (для мобильных ОС). |
| [enableCameraAutoFocus](https://www.tencentcloud.com/document/product/647/50774#30fe7ff8b3ca773e2084b7b99bd43e2a) | Включение автофокуса (для мобильных ОС). |
| [setCameraFocusPosition](https://www.tencentcloud.com/document/product/647/50774#f3d30dbe5d65b2454d10635083051fa6) | Настройка фокуса (для мобильных ОС). |
| [enableCameraTorch](https://www.tencentcloud.com/document/product/647/50774#41656f5fe1011c59544c8a20f45d5c39) | Включение/отключение вспышки (режим фонарика) (для мобильных ОС). |
| [setAudioRoute](https://www.tencentcloud.com/document/product/647/50774#e8877bbaaefb9beed5afc17f536202d1) | Установка маршрута аудио (для мобильных ОС). |
| [getDevicesList](https://www.tencentcloud.com/document/product/647/50774#514e123e8955eb408ba2fddd704ad2ee) | Получение списка устройств (для настольных ОС). |
| [setCurrentDevice](https://www.tencentcloud.com/document/product/647/50774#a6ce23ec66c6d809518d37600b58eede) | Установка используемого устройства (для настольных ОС). |
| [getCurrentDevice](https://www.tencentcloud.com/document/product/647/50774#7b89a49457ca9796d778501b820dc76c) | Получение текущего используемого устройства (для настольных ОС). |
| [setCurrentDeviceVolume](https://www.tencentcloud.com/document/product/647/50774#74ebb73b17e8b373ce7414955c26f745) | Установка громкости текущего устройства (для настольных ОС). |
| [getCurrentDeviceVolume](https://www.tencentcloud.com/document/product/647/50774#dd96184a23fa00d84ca80afd1652ff6b) | Получение громкости текущего устройства (для настольных ОС). |
| [setCurrentDeviceMute](https://www.tencentcloud.com/document/product/647/50774#f552e7fc52cd86ec3cb6c4207bba2677) | Отключение звука текущего устройства (для настольных ОС). |
| [getCurrentDeviceMute](https://www.tencentcloud.com/document/product/647/50774#3726402fd265556feca2db4841bae145) | Проверка отключения звука текущего устройства (для настольных ОС). |
| [enableFollowingDefaultAudioDevice](https://www.tencentcloud.com/document/product/647/50774#a288cca0ea46d34c494f3dc277e7ba25) | Установка использования SDK звукового устройства в соответствии с системным устройством по умолчанию (для настольных ОС). |
| [startCameraDeviceTest](https://www.tencentcloud.com/document/product/647/50774#cf9fcee895f531fee24cbf313ac56d90) | Начало тестирования камеры (для настольных ОС). |
| [stopCameraDeviceTest](https://www.tencentcloud.com/document/product/647/50774#2f26ea999b1d98de3f5f67816d1d31fc) | Завершение тестирования камеры (для настольных ОС). |
| [startMicDeviceTest](https://www.tencentcloud.com/document/product/647/50774#174b1e8a4204caace366f2731d49efb7) | Начало тестирования микрофона (для настольных ОС). |
| [startMicDeviceTest](https://www.tencentcloud.com/document/product/647/50774#776b50823f9bd88f9164c4ff10dee85c) | Начало тестирования микрофона (для настольных ОС). |
| [stopMicDeviceTest](https://www.tencentcloud.com/document/product/647/50774#cd9086b5a20cf68057c2f74541781028) | Завершение тестирования микрофона (для настольных ОС). |
| [startSpeakerDeviceTest](https://www.tencentcloud.com/document/product/647/50774#172044ecaba3934d3056dc14dd5a4306) | Начало тестирования динамика (для настольных ОС). |
| [stopSpeakerDeviceTest](https://www.tencentcloud.com/document/product/647/50774#f8ae44f6c8b4a34c2d0152009ed0447a) | Завершение тестирования динамика (для настольных ОС). |
| [startCameraDeviceTest](https://www.tencentcloud.com/document/product/647/50774#2900f3321c02eb7a4eaff1609303e416) | Начало тестирования камеры (для настольных ОС). |
| [setApplicationPlayVolume](https://www.tencentcloud.com/document/product/647/50774#2c64c587956888b01d42a98f3f6b4920) | Установка громкости текущего процесса в микшере громкости (для Windows). |
| [getApplicationPlayVolume](https://www.tencentcloud.com/document/product/647/50774#b174ef28c2d73868d18900a880e6fb5a) | Получение громкости текущего процесса в микшере громкости (для Windows). |
| [setApplicationMuteState](https://www.tencentcloud.com/document/product/647/50774#066978eb11cac8c3fb5381262d22c05f) | Отключение звука текущего процесса в микшере громкости (для Windows). |
| [getApplicationMuteState](https://www.tencentcloud.com/document/product/647/50774#3c79d03fa504902dd6a7dbc6f820bbe7) | Проверка отключения звука текущего процесса в микшере громкости (для Windows). |
| [setCameraCapturerParam](https://www.tencentcloud.com/document/product/647/50774#72bae8b9c2f0e059caccfee5984c5088) | Установка предпочтений захвата камеры. |
| [setDeviceObserver](https://www.tencentcloud.com/document/product/647/50774#cd81927639621556c20a5be90371b8c0) | Установка обратного вызова onDeviceChanged. |
| [setSystemVolumeType](https://www.tencentcloud.com/document/product/647/50774#9356758d7c8374559bd2e82f5a23a383) | Установка типа системной громкости (для мобильных ОС). |

## StructType

| FuncList | DESC |
| --- | --- |
| [TXCameraCaptureParam](https://www.tencentcloud.com/document/product/647/50774#654f738285ec7c055a692afa6ed803ea) | Параметры захвата камеры. |
| [ITXDeviceInfo](https://www.tencentcloud.com/document/product/647/50774#f55bf48d14e276018af1339206295b6a) | Информация об аудио/видео устройстве (для настольных ОС). |
| [ITXDeviceCollection](https://www.tencentcloud.com/document/product/647/50774#312a6009954927a114d23bee272e02b5) | Список информации об устройствах (для настольных ОС). |

## EnumType

| EnumType | DESC |
| --- | --- |
| [TXSystemVolumeType](https://www.tencentcloud.com/document/product/647/50774#9e22ac3a1dd66fee5bed02bc61c5e58b) | Тип системной громкости. |
| [TXAudioRoute](https://www.tencentcloud.com/document/product/647/50774#39c508dc7c357c2feda25e56f2d729c1) | Маршрут аудио (маршрут воспроизведения звука). |
| [TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) | Тип устройства (для настольных ОС). |
| [TXMediaDeviceState](https://www.tencentcloud.com/document/product/647/50774#0e59520d0b5cd9b6826a30ea0dbba8f7) | Операция с устройством. |
| [TXCameraCaptureMode](https://www.tencentcloud.com/document/product/647/50774#aede0b6f9c933df04f1b4e096ced41e6) | Предпочтения захвата камеры. |

## isFrontCamera

**isFrontCamera**

**Проверка использования фронтальной камеры.**

## switchCamera

**switchCamera**

| int switchCamera | (bool frontCamera) |
| --- | --- |

**Переключение между фронтальной и задней камерой (для мобильных ОС).**

## getCameraZoomMaxRatio

**getCameraZoomMaxRatio**

**Получение максимального коэффициента масштабирования камеры (для мобильных ОС).**

## setCameraZoomRatio

**setCameraZoomRatio**

| int setCameraZoomRatio | (float zoomRatio) |
| --- | --- |

**Установка коэффициента масштабирования камеры (для мобильных ОС).**

| Param | DESC |
| --- | --- |
| zoomRatio | Диапазон значений: [1, 5]. 1 указывает на самый широкий угол обзора (исходный), а 5 — на самый узкий угол обзора (увеличенный). Рекомендуется максимальное значение 5. Если значение превышает 5, видео станет размытым. |

## isAutoFocusEnabled

**isAutoFocusEnabled**

**Проверка поддержки автоматического обнаружения лиц (для мобильных ОС).**

## enableCameraAutoFocus

**enableCameraAutoFocus**

| int enableCameraAutoFocus | (bool enabled) |
| --- | --- |

**Включение автофокуса (для мобильных ОС).**

После включения автофокуса камера будет автоматически обнаруживать и всегда фокусировать внимание на лицах.

## setCameraFocusPosition

**setCameraFocusPosition**

| int setCameraFocusPosition | (float x |
| --- | --- |
|  | float y) |

**Настройка фокуса (для мобильных ОС).**

Этот API можно использовать для достижения следующего:

1. Пользователь может нажать на предпросмотр камеры.

2. На месте нажатия пользователя появится прямоугольник, указывающий на точку, на которой камера будет сфокусирована.

3. Пользователь передает координаты точки в SDK с помощью этого API, и SDK направляет камеру на фокусировку по мере необходимости.

| Param | DESC |
| --- | --- |
| position | Точка, на которой нужно сфокусироваться. Передайте координаты точки, на которой вы хотите сфокусироваться. |

> **Примечание** Перед использованием этого API необходимо сначала отключить автофокус с помощью [enableCameraAutoFocus](https://www.tencentcloud.com/document/product/647/50774#30fe7ff8b3ca773e2084b7b99bd43e2a).

**Описание возвращаемого значения:**

0: операция успешна; отрицательное число: операция не удалась.

## enableCameraTorch

**enableCameraTorch**

| int enableCameraTorch | (bool enabled) |
| --- | --- |

**Включение/отключение вспышки (режим фонарика) (для мобильных ОС).**

## setAudioRoute

**setAudioRoute**

| int setAudioRoute | ([TXAudioRoute](https://www.tencentcloud.com/document/product/647/50774#39c508dc7c357c2feda25e56f2d729c1) route) |
| --- | --- |

**Установка маршрута аудио (для мобильных ОС).**

Мобильный телефон имеет два устройства воспроизведения звука: приемник вверху и динамик внизу.

Если маршрут аудио установлен на приемник, громкость относительно низкая, и звук можно услышать только при поднесении телефона к уху. Этот режим имеет высокий уровень конфиденциальности и подходит для ответа на звонки.

Если маршрут аудио установлен на динамик, громкость относительно высокая и нет необходимости прижимать телефон к уху. Этот режим включает функцию «громкой связи».

## getDevicesList

**getDevicesList**

| ITXDeviceCollection* getDevicesList | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type) |
| --- | --- |

**Получение списка устройств (для настольных ОС).**

| Param | DESC |
| --- | --- |
| type | Тип устройства. Установите его на тип устройства, которое вы хотите получить. Дополнительные сведения см. в определении [TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b). |

> **Примечание** Чтобы убедиться, что SDK может управлять жизненным циклом объекта ` ITXDeviceCollection `, после использования этого API вызовите метод ` release ` для освобождения ресурсов. Не используйте ` delete ` для освобождения объекта Collection, так как удаление указателя ITXDeviceCollection* вызовет аварийное завершение. Допустимые значения ` type ` — это ` TXMediaDeviceTypeMic `, ` TXMediaDeviceTypeSpeaker ` и ` TXMediaDeviceTypeCamera `. Этот API можно использовать только на macOS и Windows.

## setCurrentDevice

**setCurrentDevice**

| int setCurrentDevice | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type |
| --- | --- |
|  | const char* deviceId) |

**Установка используемого устройства (для настольных ОС).**

| Param | DESC |
| --- | --- |
| deviceId | ID устройства. Вы можете получить ID устройства с помощью API [getDevicesList](https://www.tencentcloud.com/document/product/647/50774#514e123e8955eb408ba2fddd704ad2ee). |
| type | Тип устройства. Дополнительные сведения см. в определении ` TXMediaDeviceType `. |

**Описание возвращаемого значения:**

0: операция успешна; отрицательное число: операция не удалась.

## getCurrentDevice

**getCurrentDevice**

| ITXDeviceInfo* getCurrentDevice | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type) |
| --- | --- |

**Получение текущего используемого устройства (для настольных ОС).**

## setCurrentDeviceVolume

**setCurrentDeviceVolume**

| int setCurrentDeviceVolume | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type |
| --- | --- |
|  | uint32_t volume) |

**Установка громкости текущего устройства (для настольных ОС).**

Этот API используется для установки громкости захвата микрофона или громкости воспроизведения динамика, но не громкости камеры.

| Param | DESC |
| --- | --- |
| volume | Громкость. Диапазон значений: [0, 100]; по умолчанию: 100 |

## getCurrentDeviceVolume

**getCurrentDeviceVolume**

| uint32_t getCurrentDeviceVolume | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type) |
| --- | --- |

**Получение громкости текущего устройства (для настольных ОС).**

Этот API используется для получения громкости захвата микрофона или громкости воспроизведения динамика, но не громкости камеры.

## setCurrentDeviceMute

**setCurrentDeviceMute**

| int setCurrentDeviceMute | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type |
| --- | --- |
|  | bool mute) |

**Отключение звука текущего устройства (для настольных ОС).**

Этот API используется для отключения звука микрофона или динамика, но не камеры.

## getCurrentDeviceMute

**getCurrentDeviceMute**

| bool getCurrentDeviceMute | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type) |
| --- | --- |

**Проверка отключения звука текущего устройства (для настольных ОС).**

Этот API используется для проверки отключения звука микрофона или динамика. Отключение звука камеры не поддерживается.

## enableFollowingDefaultAudioDevice

**enableFollowingDefaultAudioDevice**

| int enableFollowingDefaultAudioDevice | ([TXMediaDeviceType](https://www.tencentcloud.com/document/product/647/50774#f023a4d94be317eb399df83a25af6b2b) type |
| --- | --- |
|  | bool enable) |

**Установка использования SDK звукового устройства в соответствии с системным устройством по умолчанию (для настольных ОС).**

Этот API используется для установки типов микрофона и динамика. Следование камеры системному устройству по умолчанию не поддерживается.

| Param | DESC |
| --- | --- |
| enable | Следовать ли системному звуковому устройству по умолчанию. true: следовать. Когда системное звуковое устройство по умолчанию изменяется или подключается новое звуковое устройство, SDK немедленно переключает звуковое устройство. false: не следовать. Когда системное звуковое устройство по умолчанию изменяется или подключается новое звуковое устройство, SDK не переключает звуковое устройство. |
| type | Тип устройства. Дополнительные сведения см. в определении ` TXMediaDeviceType `. |

## startCameraDeviceTest

**startCameraDeviceTest**

| int startCameraDeviceTest | (void* view) |
| --- | --- |

**Начало тестирования камеры (для настольных ОС).**

> **Примечание** Вы можете использовать API [setCurrentDevice](https://www.tencentcloud.com/document/product/647/50774#a6ce23ec66c6d809518d37600b58eede) для переключения между камерами во время тестирования.

## stopCameraDeviceTest

**stopCameraDeviceTest**

**Завершение тестирования камеры (для настольных ОС).**

## startMicDeviceTest

**startMicDeviceTest**

| int startMicDeviceTest | (uint32_t interval) |
| --- | --- |

**Начало тестирования микрофона (для настольных ОС).**

Этот API используется для проверки правильной работы микрофона. Обнаруженный объем микрофона (диапазон значений: [0, 100]) возвращается через обратный вызов.

| Param | DESC |
| --- | --- |
| interval | Интервал обратных вызовов громкости в миллисекундах. |

> **Примечание** При вызове этого интерфейса звук, записанный микрофоном, по умолчанию воспроизводится через динамики.

## startMicDeviceTest

**startMicDeviceTest**

| int startMicDeviceTest | (uint32_t interval |
| --- | --- |
|  | bool playback) |

**Начало тестирования микрофона (для настольных ОС).**

Этот API используется для проверки правильной работы микрофона. Обнаруженный объем микрофона (диапазон значений: [0, 100]) возвращается через обратный вызов.

| Param | DESC |
| --- | --- |
| interval | Интервал обратных вызовов громкости в миллисекундах. |
| playback | Следует ли воспроизводить звук микрофона. Пользователь услышит собственный звук при тестировании микрофона, если ` playback ` имеет значение true. |

## stopMicDeviceTest

**stopMicDeviceTest**

**Завершение тестирования микрофона (для настольных ОС).**

## startSpeakerDeviceTest

**startSpeakerDeviceTest**

| int startSpeakerDeviceTest | (const char* filePath) |
| --- | --- |

**Начало тестирования динамика (для настольных ОС).**

Этот API используется для проверки правильной работы устройства воспроизведения звука путем воспроизведения указанного аудиофайла. Если пользователи слышат звук во время тестирования, устройство работает правильно.

| Param | DESC |
| --- | --- |
| filePath | Путь к аудиофайлу |

## stopSpeakerDeviceTest

**stopSpeakerDeviceTest**

**Завершение тестирования динамика (для настольных ОС).**

## startCameraDeviceTest

**startCameraDeviceTest**

| int startCameraDeviceTest | ([ITRTCVideoRenderCallback](https://www.tencentcloud.com/document/product/647/50771#fce7830c6c3adc13fe5fa5da776a9da3)* callback) |
| --- | --- |

**Начало тестирования камеры (для настольных ОС).**

Этот API поддерживает пользовательское рендеринг, что означает, что вы можете использовать API обратного вызова ` ITRTCVideoRenderCallback ` для получения изображений, захватываемых камерой, для пользовательского рендеринга.

## setApplicationPlayVolume

**setApplicationPlayVolume**

| int setApplicationPlayVolume | (int volume) |
| --- | --- |

**Установка громкости текущего процесса в микшере громкости (для Windows).**

## getApplicationPlayVolume

**getApplicationPlayVolume**

**Получение громкости текущего процесса в микшере громкости (для Windows).**

## setApplicationMuteState

**setApplicationMuteState**

| int setApplicationMuteState | (bool bMute) |
| --- | --- |

**Отключение звука текущего процесса в микшере громкости (для Windows).**

## getApplicationMuteState

**getApplicationMuteState**

**Проверка отключения звука текущего процесса в микшере громкости (для Windows).**

## setCameraCapturerParam

**setCameraCapturerParam**

| void setCameraCapturerParam | (const [TXCameraCaptureParam](https://www.tencentcloud.com/document/product/647/50774#654f738285ec7c055a692afa6ed803ea)& params) |
| --- | --- |

**Установка предпочтений захвата камеры.**

## setDeviceObserver

**setDeviceObserver**

| void setDeviceObserver | (ITXDeviceObserver* observer) |
| --- | --- |

**Установка обратного вызова onDeviceChanged.**

## setSystemVolumeType

**setSystemVolumeType**

| int setSystemVolumeType | ([TXSystemVolumeType](https://www.tencentcloud.com/document/product/647/50774#9e22ac3a1dd66fee5bed02bc61c5e58b) type) |
| --- | --- |

**Установка типа системной громкости (для мобильных ОС).**

@deprecated Этот API не рекомендуется использовать после v9.5. Пожалуйста, используйте API ` startLocalAudio(quality) ` в ` TRTCCloud `, где параметр ` quality ` используется для определения качества звука.

## TXSystemVolumeType(Deprecated)

**TXSystemVolumeType(Deprecated)**

**Тип системной громкости.**

| Enum | Value | DESC |
| --- | --- | --- |
| TXSystemVolumeTypeAuto | 0 | Автоматический |
| TXSystemVolumeTypeMedia | 1 | Громкость мультимедиа |
| TXSystemVolumeTypeVOIP | 2 | Громкость вызова |

## TXAudioRoute

**TXAudioRoute**

**Маршрут аудио (маршрут воспроизведения звука).**

Маршрут аудио — это маршрут (динамик или приемник), по которому воспроизводится звук. Он применяется только к мобильным устройствам, таким как мобильные телефоны.

Мобильный телефон имеет два динамика: один вверху (приемник) и один внизу.

- Если маршрут аудио установлен на приемник, громкость относительно низкая, и звук можно услышать только при поднесении телефона к уху. Этот режим имеет высокий уровень конфиденциальности и подходит для ответа на звонки.
- Если маршрут аудио установлен на динамик, громкость относительно высокая и нет необходимости прижимать телефон к уху. Этот режим включает функцию «громкой связи».

| Enum | Value | DESC |
| --- | --- | --- |
| TXAudioRouteSpeakerphone | 0 | Громкая связь: динамик внизу используется для воспроизведения (без использования рук). При относительно высокой громкости используется для воспроизведения музыки вслух. |
| TXAudioRouteEarpiece | 1 | Наушник: приемник вверху используется для воспроизведения. При относительно низкой громкости подходит для сценариев вызовов, требующих конфиденциальности. |

## TXMediaDeviceType

**TXMediaDeviceType**

**Тип устройства (для настольных ОС).**

Этот переч

---
*Источник (EN): [itxdevicemanager.md](./itxdevicemanager.md)*
