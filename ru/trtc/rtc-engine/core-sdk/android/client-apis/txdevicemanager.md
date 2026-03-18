# TXDeviceManager

Copyright (c) 2021 Tencent. All rights reserved.

Модуль: модуль управления аудио/видео устройствами

Описание: управляет аудио/видео устройствами, такими как камера, микрофон и динамик.

**TXDeviceManager**

## TXDeviceManager

| Список функций | Описание |
| --- | --- |
| [isFrontCamera](https://www.tencentcloud.com/document/product/647/50767#71820ed8e774434ec01d6dc6a44dfe3d) | Проверка использования передней камеры. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/50767#98743c4b46e3baea8308a8e27cf44c8a) | Переключение на переднюю/заднюю камеру (для мобильных ОС). |
| [getCameraZoomMaxRatio](https://www.tencentcloud.com/document/product/647/50767#c792f2cefe9b867591a00071f673da52) | Получение максимального коэффициента масштабирования камеры (для мобильных ОС). |
| [setCameraZoomRatio](https://www.tencentcloud.com/document/product/647/50767#de6f0bc85a439308d2bca3f5a338e3f7) | Установка коэффициента масштабирования камеры (для мобильных ОС). |
| [isAutoFocusEnabled](https://www.tencentcloud.com/document/product/647/50767#f3c9fb1db152e2ef198256dcf992fc30) | Проверка поддержки автоматического обнаружения лиц (для мобильных ОС). |
| [enableCameraAutoFocus](https://www.tencentcloud.com/document/product/647/50767#5bb9ad6ffa0c173d8864188d143a6332) | Включение автофокуса (для мобильных ОС). |
| [setCameraFocusPosition](https://www.tencentcloud.com/document/product/647/50767#c50deb76ecaed735d7a7571ae9e1e719) | Регулировка фокуса (для мобильных ОС). |
| [enableCameraTorch](https://www.tencentcloud.com/document/product/647/50767#b71d15b7be8cd6fa6f4cf6435d7548be) | Включение/выключение вспышки, то есть режима фонарика (для мобильных ОС). |
| [setAudioRoute](https://www.tencentcloud.com/document/product/647/50767#bd5eb5475f6b3cf2e2881fe4c4dee818) | Установка маршрута аудио (для мобильных ОС). |
| [setExposureCompensation](https://www.tencentcloud.com/document/product/647/50767#260167d6608887a70694ee2983fefc10) | Установка параметров экспозиции камеры в диапазоне от - 1 до 1. |
| [setCameraCapturerParam](https://www.tencentcloud.com/document/product/647/50767#3a720bdf065f7984d709180bdd28cd02) | Установка предпочтений захвата камеры. |
| [setSystemVolumeType](https://www.tencentcloud.com/document/product/647/50767#d4219ee8b3e722282cd8e564f79d4cd8) | Установка типа системного объема (для мобильных ОС). |

## StructType

| Список функций | Описание |
| --- | --- |
| [TXCameraCaptureParam](https://www.tencentcloud.com/document/product/647/50767#654f738285ec7c055a692afa6ed803ea) | Параметры захвата камеры. |

## EnumType

| EnumType | Описание |
| --- | --- |
| [TXSystemVolumeType](https://www.tencentcloud.com/document/product/647/50767#9e22ac3a1dd66fee5bed02bc61c5e58b) | Тип системного объема. |
| [TXAudioRoute](https://www.tencentcloud.com/document/product/647/50767#39c508dc7c357c2feda25e56f2d729c1) | Маршрут аудио (маршрут воспроизведения звука). |
| [TXCameraCaptureMode](https://www.tencentcloud.com/document/product/647/50767#aede0b6f9c933df04f1b4e096ced41e6) | Предпочтения захвата камеры. |

## isFrontCamera

**isFrontCamera**

**Проверка использования передней камеры.**

## switchCamera

**switchCamera**

| int switchCamera | (boolean frontCamera) |
| --- | --- |

**Переключение на переднюю/заднюю камеру (для мобильных ОС).**

## getCameraZoomMaxRatio

**getCameraZoomMaxRatio**

**Получение максимального коэффициента масштабирования камеры (для мобильных ОС).**

## setCameraZoomRatio

**setCameraZoomRatio**

| int setCameraZoomRatio | (float zoomRatio) |
| --- | --- |

**Установка коэффициента масштабирования камеры (для мобильных ОС).**

| Параметр | Описание |
| --- | --- |
| zoomRatio | Диапазон значений: [1, 5]. 1 означает самый широкий угол зрения (оригинал), а 5 — самый узкий угол зрения (увеличение). Рекомендуется, чтобы максимальное значение составляло 5. Если значение превышает 5, видео станет размытым. |

## isAutoFocusEnabled

**isAutoFocusEnabled**

**Проверка поддержки автоматического обнаружения лиц (для мобильных ОС).**

## enableCameraAutoFocus

**enableCameraAutoFocus**

| int enableCameraAutoFocus | (boolean enabled) |
| --- | --- |

**Включение автофокуса (для мобильных ОС).**

После включения автофокуса камера будет автоматически обнаруживать и постоянно фокусироваться на лицах.

## setCameraFocusPosition

**setCameraFocusPosition**

| int setCameraFocusPosition | (int x |
| --- | --- |
|  | int y) |

**Регулировка фокуса (для мобильных ОС).**

Этот API можно использовать для следующего:

1. Пользователь может коснуться предпросмотра камеры.

2. На месте касания появится прямоугольник, указывающий точку, на которой камера будет сосредоточена.

3. Пользователь передает координаты точки в SDK с помощью этого API, и SDK указывает камере сфокусироваться по мере необходимости.

| Параметр | Описание |
| --- | --- |
| position | Точка для фокусировки. Передайте координаты точки, на которую вы хотите сфокусироваться. |

> **Примечание** Перед использованием этого API необходимо сначала отключить автофокус с помощью [enableCameraAutoFocus](https://www.tencentcloud.com/document/product/647/50767#5bb9ad6ffa0c173d8864188d143a6332).

**Описание возвращаемого значения:**

0: операция успешна; отрицательное число: операция не удалась.

## enableCameraTorch

**enableCameraTorch**

| boolean enableCameraTorch | (boolean enable) |
| --- | --- |

**Включение/выключение вспышки, то есть режима фонарика (для мобильных ОС).**

## setAudioRoute

**setAudioRoute**

| int setAudioRoute | ([TXAudioRoute](https://www.tencentcloud.com/document/product/647/50767#39c508dc7c357c2feda25e56f2d729c1) route) |
| --- | --- |

**Установка маршрута аудио (для мобильных ОС).**

Мобильный телефон имеет два устройства воспроизведения звука: приемник вверху и динамик внизу.

Если маршрут аудио установлен на приемник, громкость относительно низкая, и звук можно услышать только при поднесении телефона к уху. Этот режим имеет высокий уровень приватности и подходит для ответа на звонки.

Если маршрут аудио установлен на динамик, громкость относительно высокая, и нет необходимости подносить телефон к уху. Этот режим обеспечивает функцию "свободные руки".

## setExposureCompensation

**setExposureCompensation**

| int setExposureCompensation | (float value) |
| --- | --- |

**Установка параметров экспозиции камеры в диапазоне от - 1 до 1.**

## setCameraCapturerParam

**setCameraCapturerParam**

| void setCameraCapturerParam | ([TXCameraCaptureParam](https://www.tencentcloud.com/document/product/647/50767#654f738285ec7c055a692afa6ed803ea) params) |
| --- | --- |

**Установка предпочтений захвата камеры.**

## setSystemVolumeType

**setSystemVolumeType**

| int setSystemVolumeType | ([TXSystemVolumeType](https://www.tencentcloud.com/document/product/647/50767#9e22ac3a1dd66fee5bed02bc61c5e58b) type) |
| --- | --- |

**Установка типа системного объема (для мобильных ОС).**

@deprecated Этот API не рекомендуется после версии 9.5. Пожалуйста, используйте вместо этого API ` startLocalAudio(quality) ` в ` TRTCCloud `, параметр ` quality ` которого используется для определения качества звука.

## TXSystemVolumeType(Deprecated)

**TXSystemVolumeType(Deprecated)**

**Тип системного объема.**

| Enum | Значение | Описание |
| --- | --- | --- |
| TXSystemVolumeTypeAuto | Not Defined | Авто |
| TXSystemVolumeTypeMedia | Not Defined | Громкость медиа |
| TXSystemVolumeTypeVOIP | Not Defined | Громкость звонка |

## TXAudioRoute

**TXAudioRoute**

**Маршрут аудио (маршрут воспроизведения звука).**

Маршрут аудио — это маршрут (динамик или приемник), через который воспроизводится звук. Применяется только к мобильным устройствам, таким как мобильные телефоны.

Мобильный телефон имеет два динамика: один вверху (приемник) и один внизу.

- Если маршрут аудио установлен на приемник, громкость относительно низкая, и звук можно услышать только при поднесении телефона к уху. Этот режим имеет высокий уровень приватности и подходит для ответа на звонки.
- Если маршрут аудио установлен на динамик, громкость относительно высокая, и нет необходимости подносить телефон к уху. Этот режим обеспечивает функцию "свободные руки".

| Enum | Значение | Описание |
| --- | --- | --- |
| TXAudioRouteSpeakerphone | Not Defined | Громкая связь: динамик внизу используется для воспроизведения (свободные руки). С относительно высокой громкостью используется для громкого воспроизведения музыки. |
| TXAudioRouteEarpiece | Not Defined | Наушник: приемник вверху используется для воспроизведения. С относительно низкой громкостью подходит для сценариев звонков, требующих приватности. |

## TXCameraCaptureMode

**TXCameraCaptureMode**

**Предпочтения захвата камеры.**

Это перечисление используется для установки параметров захвата камеры.

| Enum | Значение | Описание |
| --- | --- | --- |
| TXCameraResolutionStrategyAuto | Not Defined | Автоматическая регулировка параметров захвата камеры. SDK выбирает подходящие параметры вывода камеры в соответствии с фактической производительностью устройства захвата и ситуацией в сети, поддерживая баланс между производительностью устройства и качеством предпросмотра видео. |
| TXCameraResolutionStrategyPerformance | Not Defined | Приоритет производительности оборудования. SDK выбирает ближайшие параметры вывода камеры в соответствии с разрешением и частотой кадров кодировщика пользователя, чтобы обеспечить производительность устройства. |
| TXCameraResolutionStrategyHighQuality | Not Defined | Приоритет качества предпросмотра видео. SDK выбирает более высокие параметры вывода камеры для улучшения качества видео предпросмотра. В этом случае на предварительную обработку видео будет потребляться больше ЦП и памяти. |
| TXCameraCaptureManual | Not Defined | Позволяет пользователю установить ширину и высоту видео, захватываемого локальной камерой. |

## TXCameraCaptureParam

**TXCameraCaptureParam**

**Параметры захвата камеры.**

Этот параметр определяет качество изображения локального предпросмотра.

| EnumType | Описание |
| --- | --- |
| height | Описание поля: высота захватываемого изображения |
| mode | Описание поля: предпочтения захвата камеры, см. [TXCameraCaptureMode](https://www.tencentcloud.com/document/product/647/50767#aede0b6f9c933df04f1b4e096ced41e6) |
| width | Описание поля: ширина захватываемого изображения |


---
*Источник: [https://trtc.io/document/50767](https://trtc.io/document/50767)*

---
*Источник (EN): [txdevicemanager.md](./txdevicemanager.md)*
