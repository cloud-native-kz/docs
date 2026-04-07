# Детали интеграции Push Stream

Этот документ описывает, как интегрировать SDK или плагин в вашу программу для реализации функции толкающей трансляции CSS.

## Предварительные требования

- Вы активировали службу CSS.
- Выберите **Domain Management**, нажмите **Add Domain** и добавьте доменное имя для трансляции в соответствии с инструкциями в документе [Adding Your Own Domain](https://www.tencentcloud.com/document/product/267/35970).
- В консоли CSS создайте адрес трансляции в разделе **CSS Toolkit** > **Address Generator** в соответствии с инструкциями в документе [Address Generator](https://www.tencentcloud.com/document/product/267/31084). Затем реализуйте живую трансляцию в соответствии с вашими бизнес-сценариями следующим образом:

## Интеграция в собственное приложение

Загрузите и интегрируйте MLVB SDK в соответствии с руководствами интеграции для [iOS](https://www.tencentcloud.com/document/product/1071/38157) и [Android](https://www.tencentcloud.com/document/product/1071/38158).

> **Примечание** Для включения толкающей трансляции RTMP необходимо создать объект `TXLivePusher` и установить `V2TXLiveMode` на `_RTMP` при инициализации компонента `V2TXLivePusher`. Ниже представлена конфигурация для iOS и Android:iOSV2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTMP];AndroidV2TXLivePusher mLivePusher = new V2TXLivePusherImpl(this, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTMP);

## Интеграция в веб

Интеграция в веб в настоящее время поддерживает только протокол WebRTC для толкающей трансляции. Вы можете интегрировать SDK в соответствии с инструкциями в документе [WebRTC](https://www.tencentcloud.com/document/product/267/41620).

> **Примечание：** Вы также можете напрямую выполнить веб-трансляцию в разделе [Web Push](https://console.tencentcloud.com/live/tools/webpush) консоли CSS.

## Интеграция на ПК

Для ПК (Windows/macOS) вы можете напрямую использовать [OBS](https://obsproject.com/download) для толкающей трансляции. Это бесплатная программа с открытым исходным кодом для видеосъёмки и трансляции, которая поддерживает операционные системы, такие как Windows, macOS и Linux.

Если протокол толкающей трансляции — WebRTC, необходимо настроить плагин OBS, предоставленный Tencent Cloud, в соответствии с инструкциями в документе [OBS WebRTC live streaming](/document/product/267/57042).

## Дополнительно

- Использование MLVB SDK повлечёт за собой плату. Подробнее о расчётах см. в разделе [Billing Overview](https://www.tencentcloud.com/document/product/1071/55389?lang=en&pg=).


---
*Источник: [https://www.tencentcloud.com/document/product/267/58160](https://www.tencentcloud.com/document/product/267/58160)*

---
*Источник (EN): [push-stream-integration-details.md](./push-stream-integration-details.md)*
