# 7. Оценка качества сети

Данный документ описывает способы оценки текущих условий сети.

Когда вы находитесь в видеозвонке в WeChat при плохом качестве сети (например, в лифте), WeChat отображает сообщение о низком качестве сети. Данный документ описывает способ использования TRTC для реализации аналогичного взаимодействия в вашем приложении.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dae0aa5d37fa11edb1de525400c56988.png)

## Руководство по использованию

TRTC предоставляет callback **onNetworkQuality** для отправки отчетов о текущем качестве сети один раз в две секунды. Он содержит два параметра: `localQuality` и `remoteQuality`.

- **localQuality** указывает ваше текущее качество сети, которое имеет шесть уровней: `Excellent`, `Good`, `Poor`, `Bad`, `VeryBad` и `Down`.
- **remoteQuality** - это массив, указывающий на качество сети удаленных пользователей. Каждый элемент в этом массиве представляет качество сети одного удаленного пользователя.

| Качество | Название | Описание |
| --- | --- | --- |
| 0 | Unknown | Неизвестно |
| 1 | Excellent | Текущая сеть отличного качества. |
| 2 | Good | Текущая сеть хорошего качества. |
| 3 | Poor | Текущая сеть в норме. |
| 4 | Bad | Текущая сеть низкого качества. Могут быть явные зависания и задержки. |
| 5 | VeryBad | Текущая сеть очень низкого качества. TRTC может поддерживать соединение, но не может гарантировать качество связи. |
| 6 | Down | Текущая сеть не соответствует минимальным требованиям TRTC, и невозможно провести нормальный аудио- и видеозвонок. |

Вам нужно только прослушивать callback [onNetworkQuality](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCallback.html#event:onNetworkQuality) TRTC и отображать соответствующую подсказку в пользовательском интерфейсе.

```
import TRTCCloud, { TRTCQuality } from 'trtc-electron-sdk';const rtcCloud = new TRTCCloud();function onNetworkQuality(localQuality, remoteQuality) {  switch(localQuality.quality) {    case TRTCQuality.TRTCQuality_Unknown:      console.log('SDK has not yet sensed the current network quality.');      break;    case TRTCQuality.TRTCQuality_Excellent:      console.log('The current network is very good.');      break;    case TRTCQuality.TRTCQuality_Good:      console.log('The current network is good.');      break;    case TRTCQuality.TRTCQuality_Poor:      console.log('The current network quality barely meets the demand.');      break;    case TRTCQuality.TRTCQuality_Bad:      console.log('The current network is poor, and there may be significant freezes and call delays.');      break;    case TRTCQuality.TRTCQuality_Vbad:      console.log('The current network is very poor, the communication quality cannot be guaranteed.');      break;    case TRTCQuality.TRTCQuality_Down:      console.log('The current network does not meet the minimum requirements.');      break;    default:      break;  }  for (let i = 0; i < remoteQuality.length; i++) {    console.log(`remote user: ${remoteQuality[i].userId}, quality: ${remoteQuality[i].quality}`);  }}rtcCloud.on('onNetworkQuality', onNetworkQuality);
```


---
*Источник: [https://trtc.io/document/47640](https://trtc.io/document/47640)*

---
*Источник (EN): [7sensing-network-quality.md](./7sensing-network-quality.md)*
