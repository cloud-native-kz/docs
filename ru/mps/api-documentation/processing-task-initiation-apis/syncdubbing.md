# SyncDubbing

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для синхронного возврата ID типа голоса клона или результатов синтеза звука.

Максимум 20 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: SyncDubbing. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Text | Нет | String | Текст для синтеза. Это требуется для преобразования текста в речь. Текст не может превышать 2000 символов в длину. |
| TextLang | Нет | String | Язык текста. Если оставить пусто, по умолчанию используется zh (китайский). Поддерживаемые языки: zh: китайский. en: английский. ja: японский. de: немецкий. fr: французский. ko: корейский. ru: русский. uk: украинский. pt: португальский. it: итальянский. es: испанский. id: индонезийский. nl: нидерландский. tr: турецкий. fil: филипинский. ms: малайский. el: греческий. fi: финский. hr: хорватский. sk: словацкий. pl: польский. sv: шведский. hi: хинди. bg: болгарский. ro: румынский. ar: арабский. cs: чешский. da: датский. ta: тамильский. hun: венгерский. vi: вьетнамский. no: норвежский. yue: кантонский. th: тайский. he: иврит. ca: каталанский. nn: букмол. af: африкаанс. fa: персидский. sl: словенский. |
| VoiceId | Нет | String | ID типа голоса. Это требуется для синтеза с определенным типом голоса. Поддерживаются системные типы голосов и клонирование типа голоса. |
| AudioData | Нет | String | Звук в кодировке Base64 для клонирования. |
| AudioLang | Нет | String | Язык клонирования звука. Язык по умолчанию — китайский. Поддерживаемые языки совпадают с языками для TextLang. |
| ExtParam | Нет | String | Расширенные параметры в формате строки JSON. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| ErrorCode | Integer | Код ошибки. Возвращается 0, если запрос выполнен успешно. |
| Msg | String | Сообщение об ошибке. Возвращается success, если запрос выполнен успешно. |
| AudioData | String | Синтезированный звук в кодировке Base64 и формате WAV. Примечание: это поле может возвращать null, что указывает на то, что нет доступных действительных значений. |
| VoiceId | String | ID клонированного типа голоса. Примечание: это поле может возвращать null, что указывает на то, что нет доступных действительных значений. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1: Пример преобразования текста в речь

#### Входной пример

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: SyncDubbing
<Common request parameters>

{
    "Text": "Hello",
    "VoiceId": "s1_2GSzVAf00hl7+A+LJTNvVI6nFJB0qliIvR8wntPeaniVSstd7Z4E4UL8Hky3azMHVlDSps1zWW4nJ7ll9w==",
    "ExtParam": "{\"engine\": \"\"}"
}
```

#### Выходной пример

```json
{
    "Response": {
        "AudioData": "UklGRuxnAABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YchnAABBAEUAQwBFAEgARwBJAEIASQBOAEwASABKAEkASgBJAEgASABMAEoASABIAEgASgBIAEkASQBIAEkASABHAEcASABIAEoASABJAEgARwBKAEoASABFAEkASQBIAEYARwBHAEgARwBIAEYARgBFAEUARABFAEcARQBEAEQARQBEAEQARABEAEUARQBDAEMARQBDAEMAQQBBAEMAQAA/AEAAQAA/AEAAQgA/AEAAQgA/AD8APwA+AD8APQA7AD0APQA9ADoAOgA7ADoAOgA9ADwAOwA6ADkAOQA3ADgAOQA3ADgANwA4ADgANwA2ADcANwA3ADcANwA1ADQANgA1ADQANAA1ADUANQA1ADMAMwAzADUAMgAyADMAMwAzADIAMgAwADEAMQAxADEAMAAvADEALwAyADAALwAxAC8AMQAwAC0ALAAtAC0ALAAtAC8ALAAsAC4ALgAsAC0ALAAqACoAKwAqACoAKwArACoAKgApACkAKQAoACcAKAAoACYAJwAnACcAJgAmACYAJgAmACQAJAAkACMAJAAjACQAJQAlACMAIwAjACMAIwAkACQAIgAhACIAIgAhACEAIgAjACEAIgAiAB8AIQAgACAAIQAhACAAIAAhAB8AIAAgACAAIAAfAB8AIAAgAB8AHwAfAB8AHwAfAB4AHgAdABwAHQAdAB0AGwAcABwAGwAcABwAHAAcABwAGwAbABsAHQAdABsAGwAbABwAHgAcABsAHQAcABoAGQAaABwAHAAZABkAGAAaABoAGQAZABgAFwAZABoAGAAXABgAGQAYABkAGQAWABgAGAAYABcAGAAXABkAGgAWABUAGAAaABcAFgAXABUAFwAYABgAGAAWABYAFgAaABkAFwAVABcAFgAWABcAFwAWABYAFgAWABUAEwAVABYAFQAXABcAFwAWABUAFQAVABcAFwAWABgAFQATABUAFQAXABcAFwAWABcAFQAWABYAFQAVABYAFQAVABYAFAAWABUAFQAWABUAFgAXABUAFwAXABcAFgAWABUAFAAUABcAFgATABUAFQATABUAEwARABQAEwATABUAFQAVABQAFgATABEAFAASABQAFAATABIAEQATABUAEwASABMAEAAUABMADwATABMAFAAQABEAEwARABEAEQARABEAEQARABEAEAAPABEAEQARAA8ADwARABAADwAPAA8AEQARAA8ADwAQABEAEQASAA8ADgAPAA8ADwAPAA8ADwAPAA8ADwAQAA8ADQANAA0ADAANAA0ADAAMAAsACwAKAAwADAALAAsADAANAAwADQANAAsACwALAAsACwALAAsACwALAAsACwALAAkACwAKAAcABwAFAAUABQAFAAMAAgAEAAIAAgABAAEAAQABAAEAAgACAAEAAwAAAAEAAAD/////AAD//wAAAAD//wAAAQAAAAAAAAD//wAA//8AAAAA//8AAAAAAAD//wAAAAAAAAEAAQAAAAAA/////wAA//8AAAAAAAD//wAA//////3//f/7//v/+f/5//n/+v/7//j/9//4//b/9//2//X/9f/0//P/8//x//L/9P/z//D/8v/x//L/8v/x//H/8v/x//D/8f/x//D/8f/v//P/8//x//L/8f/0//T/9P/z//P/9P/z//P/9f/1//X/9P/0//T/8//0//T/8//1//P/9P/z//T/9f/1//X/9f/1//X/9f/2//j/9f/2//b/9v/3//j/+P/3//b/9v/4//j/+P/5//f/+P/5//n/+//4//r/+//7//v/+//7//v//P/7//v/+//8//7//v/+////AAD//wEA//8AAAEAAAABAAEAAwACAAEAAwAEAAYABQAFAAUABgAFAAYABwAGAAYABgAGAAgACAAJAAoACgALAAsADQANAA4ADgANAA8AEAASABIAEgATABIAFAAUABQAFQAWABcAGAAYABcAGgAbABsAGwAdABoAHAAeAB8AIAAgACIAIgAiACIAIwAjACUAJQAmACUAJwAmACcAKAApACkAKAAqACsALAAqACwALQAtAC8AMQAvAC8AMQAxADEAMwAzADQANQA1ADUANAA2ADcANwA3ADcAOQA4ADkAOQA7ADsAPAA9ADsAPQA9AD8AQAA/AEYAQAA/AEEAQQBDAEIARQBEAEQARQBFAEQARABGAEYARgBHAEcASQBJAEoASgBKAEoASgBLAE0ASwBMAEwASgBNAE4ATQBNAE0ATwBPAE4ATQBPAE8ATwBRAFEATwBQAFMAUgBRAFEAUQBSAFIAUwBTAFMAVABUAFUAVABTAFMAVABTAFcAVgBTAFUAVABVAFYAVgBVAFUAVQBVAFUAVQBWAFUAVABTAFYAUwBWAFUAUwBUAFUAVQBVAFUAVgBWAFYAVQBUAFQAVgBVAFUAVABTAFMAVABWAFQAUwBTAFUAUwBUAFUAVABXAFUAVQBUAFMAVABUAFQAUgBTAFMAVABUAFMAUwBRAFEAUwBTAFEAUgBTAFIAUABQAFAATgBOAFAATgBPAE8ATgBPAE0ATQBPAEwATQBOAEwASwBLAE0ASwBJAEoASQBLAEsASQBJAEgASABHAEgASQBHAEkASABIAEYARQBGAEUARQBFAEQARABDAEQAQwBDAEMAQQBCAEIAQwBCAEEAQQBAAD4AQQA/AD8AQAA/AD8AQABAAD4APwA/AD4APQA8AD0AQAA9ADsAOwA6ADoAOQA5ADgAOAA4ADkAOQA5ADcANgA3ADcANwA3ADUANgA2ADUANwA2ADUAMwAyADIAMQAzADEAMQAxADEAMQAxAC8ALwAvAC8AMAAvAC8ALgAvAC8ALwAuAC0ALQAsAC4AKwArACkALAAtACgAKwApACgAKgAoACkAKgApACkAKQAnACcAJgAnACgAJgAnACYAJgAmACYAJQAkACUAJgAmACQAJAAjACIAIwAjACIAJAAjACIAIgAjACIAIQAhACEAIgAiACEAIQAiACIAIAAhACEAIAAeAB8AIQAgAB8AHwAeAB4AHwAeAB8AHwAeAB4AHwAfACAAIQAfAB4AHQAfAB8AHwAdAB0AHgAdAB4AHgAfAB8AHQAeAB8AHgAeAB0AHgAeABwAHQAfAB0AHAAeAB0AHgAeAB0AHAAdABwAHAAdAB0AHQAdAB0AHgAcAB0AHgAfAB4AHwAgAB8AHwAgAB4AIAAfACAAIAAhACIAHgAfAB8AIAAjACIAIAAfACEAIgAhACAAIQAjACIAIgAkACUAJQAkACUAJgAmACQAJQAlACcAJQAmACYAJQAnACcAJwAoACYAJwApACgAKAApACgAKAAqACkAKgArACsALAAsACwAKwAsAC4ALAAsAC4ALwAyAC4ALwAxAC8ALwAxADAAMgAxAC8AMgAzADEAMwAzADMAMwA0ADQAMwA0ADMANgA1ADIANQA2ADUAOAA2ADcAOQA4ADkANQA3ADkAOgA5ADgAOQA7ADwAPAA8ADwAPgA+AD0APgA/AD4AQAA+AD4AQAA/AEEAQQBBAEEAQQBBAEMAQwBCAEQAQwBEAEQAQwBDAEQARQBFAEMARABFAEUARQBGAEUARgBGAEcARwBJAEgASABIAEkASQBJAEkASQBLAEoASgBLAEsASwBLAEwASwBMAEwATwBPAE0ATQBNAFAATwBPAFAATwBOAFAAUQBRAE8AUQBQAFAAUgBQAFEAUABQAFEAUQBRAFEAUQBSAFUAUgBSAFQAVQBVAFMAVgBXAFUAUwBUAFYAVABTAFUAVgBVAFYAVQBXAFcAVwBYAFYAVwBaAFcAVgBYAFgAWABWAFgAVwBXAFgAVwBYAFgAWQBYAFgAVwBYAFcAVwBaAFgAVwBYAFgAWwBZAFgAWQBXAFcAVwBZAFkAWQBaAFkAWgBaAFsAWQBaAFoAWQBZAFgAWABZAFkAWgBaAFkAWwBbAFoAWgBaAFkAWwBZAFkAWQBaAFoAWwBaAFgAWgBZAFgAWQBZAFkAWQBYAFsAWgBYAFgAWQBZAFoAWABXAFgAWABXAFgAWABYAFkAVgBYAFgAVgBYAFkAWABYAFkAWABXAFcAWABXAFkAWABVAFcAVwBXAFYAVgBVAFgAVwBUAFcAVgBXAFYAVQBVAFUAVQBXAFQAVQBUAFQAVQBVAFQAVABTAFQAUgBSAFIAUwBTAFIAUABPAFAATgBSAFAATQBQAE4AUQBQAE8AUQBPAE8AUABQAFAATgBRAE8ATwBQAE4AUQBPAE0ATgBNAEwATQBNAE4ATgBMAEsASwBMAEsASwBMAEsASwBMAEwASwBKAEgASgBLAEkASgBJAEYARwBIAEYASABIAEcARwBHAEcARgBGAEcARQBFAEQARABHAEcARQBEAEUARQBEAEUARABDAEQAQwBDAEQAQgBCAEMAQwBAAEEAQABAAEIAQQBBAEAAQABAAD8AQAA/AD8AQABBAD8APgA+AD0APgA9AD0APQA+AD4AOgA+ADsAOwA7ADoAOwA7ADgAOgA6ADcAOQA4ADgAOAA4ADYANwA2ADcANwA2ADcANgA0ADYANQA1ADQANAA1ADUANQA1ADYANQA0ADQANAA0ADQAMwAzADMAMQAyADAAMQAxADEALwAwADAALQAxADAALwAvAC4ALwAtAC0ALQAsACwALAAsACwALAArACkAKQApACoALAApACgAJwApACcAJgAqACcAKQAnACcAJwAlACYAJQAlACcAJQAmACUAIwAjACUAJQAkACUAJQAkACUAIwAkACQAIQAiACIAIgAhACAAIAAfACEAHgAgACEAIQAgACEAHgAfAB8AHQAcAB0AHQAfABwAGwAcABwAGwAcABwAGwAbABsAGgAbABwAHQAaABcAGAAaABoAGQAXABgAGQAZABkAFgAXABcAFgAUABYAFgAUABQAFQAXABQAEwATABMAFAARABEAEQARABEAEQARABAAEAAQAA8ADwAQAA8ADgAPAA4ADgAOAA8ADgAOAA8ADgANAA4ADQALAAsADAALAAwADAAMAAsACwAJAAcADQAKAAkABwAHAAcABwAKAAkABwAHAAYABgAHAAUABwAGAAUABQAFAAYABwADAAQABgAFAAIAAgAEAAQABQACAAIAAwACAAEAAQABAAEAAgACAAIA//8CAAIAAAAAAAAAAAAAAAEAAAAAAAAAAAD/////AAAAAP////8AAP7//f///////v/9//7//v/9/////v/9//7//P/7//v/+//8//v/+//6//n/+v/6//v/+//7//v/+f/5//n/+f/5//n/+f/5//n/+f/5//n/+f/5//f/9//5//j/+P/3//j/+P/3//f/9f/4//j/9v/2//f/9//2//b/9//3//j/+P/4//f/+P/3//b/+f/3//b/9//3//n/9//2//f/9//3//b/9P/2//X/9v/0//T/9f/1//X/9f/1//b/9//1//X/9v/3//X/9f/1//f/9//3//f/9v/1//j/+f/3//f/9//3//f/9//3//f/9f/1//f/9//1//X/9f/2//f/9//1//X/9v/2//f/9//2//b/+f/3//f/9//3//j/9//3//f/+P/5//f//P/7//n/+f/6//r/+f/5//j/+v/6//z/+f/3//j/+P/5//n/+v/3//f/+f/5//n/+P/5//j/+//7//r/+f/5//n/+//8//n/+f/8//3//P/6//j/+//9//3//f/9//3//f///////v/9/////f/+//7///////3//f/8//z//v/+//7////+/wAAAQD/////AAD//wAA//8AAAAAAAAAAP////8AAAAAAAAAAAAAAAD///////8AAAAAAAD//wAAAAAAAAEAAAAAAAAAAQABAAEAAQAAAAEAAAACAAMAAAAAAAEAAwACAAEAAQAAAAEAAgABAAEAAQABAAIAAQABAAEABAADAAQAAgABAAMAAwABAAEAAgABAAMAAwACAAIABAAEAAQAAwACAAMABAAEAAYAAwAFAAYABQAGAAMABQAEAAUABQAFAAQABQAGAAUABAAFAAMABQAEAAUABQAEAAUAAQAHAAYABQAFAAQABwAHAAYABwAHAAUABwAJAAYABQAIAAgABgAEAAcABwAGAAgACAAGAAUABgAGAAcABgAFAAcABQAIAAgABwAIAAgABQAHAAgACAAJAAkACQAGAAYACAAKAAkABwAIAAkABwAIAAgABwAIAAkACAAHAAcABwAIAAYACAAHAAcACQAJAAgACAAKAAkABwAHAAgABwAIAAcABwAJAAoACAAJAAkABwAHAAcACAAHAAgACQAHAAcABwAJAAkACQAHAAgACAAIAAYABgAHAAcACQAHAAgACgAIAAcACQAIAAgACAAJAAcABwAIAAcABwAHAAkACQAHAAcACQAJAAcACgALAAoACQAJAAkACQAJAAoACQAKAAoACQAJAAoACgAKAAoACgAIAAYABgAIAAgACQAJAAkACQAKAAgACAAJAAkACQAJAAkACQAJAAkACAALAAgACAALAAoACQAKAAwACwAIAAoACwAKAAoACgAJAAkACgAKAAsACQAKAAkACQAJAAoACQAKAAoACQAJAAoACQAIAAoACQAKAAkACQAJAAkABwAIAAkACgAJAAoACQAJAAkACQAJAAoACQAHAAsACgAKAAoACAAKAAkACgALAAsACwAKAAwADQANAAsADAALAAsADAALAAsADAALAAwACwALAAwADAAMAAsACwAKAAwACgAMAAsACQANAA4ADQAOAA0ADgAOAA0ACwAMAAwADQANAAsADQANAAwADgAMAAwADQANAA4ADQALAA0ADgALAAwADQANAAwADQANAA4ADQALAA0ADQAPAA8ADQAOABAADwAOAA4ADwAPABAAEAAQAA8ADwATABIAEQAQAA8AEQAQABAAEwAQAA8ADwAPABEAEQASABMAEQASABIAEgAUABMAEQATABQAEwATABMAEgASABMAFAAVABMAEwATABMAEwAUABIAEQAUABIAEAAPABEAFAAQABEAFQATABMAEwASABMAEQATABQAFAAUABIAFwAWABMAFQAWABUAFAAXABYAFgAWABcAFwAWABcAFgAXABYAGAAWABcAFgAWABgAFQAXABgAFgAVABgAGQAZABkAGAAYABgAGgAZABYAGAAZABoAGAAXABcAGAAZABgAFwAYABwAGAAZABgAFwAaABsAGQAaABcAGgAcABoAGgAaABsAGgAcABwAGwAZABwAHQAdABwAHwAfAB8AHQAdAB0AHQAfAB8AHQAcAB0AHQAdAB0AHwAeACAAIQAdAB4AIAAfAB0AHgAfAB4AHgAdAB4AHgAeAB0AHwAdAB0AHgAcABwAHQAdAB0AHgAfAB8AHQAfACAAHwAdAB0AIAAeAB0AHgAfAB8AHwAdAB0AHwAgACAAIQAhAB8AIAAgACEAIQAfAB8AIQAhACAAIQAhACIAIgAeACAAHwAgACIAIAAhACEAIQAhACIAIgAhACEAIgAiACEAIAAeACAAIAAiACIAIAAhACEAIAAgAB8AHQAeACAAIQAgAB8AHwAeAB4AHQAeAB8AHgAdAB4AHQAeACEAHgAdABwAHQAeAB0AHQAdAB8AHQAdABsAHAAdABsAHAAdABwAHAAaABwAGgAaABsAGgAdABoAGgAcABwAGgAaABkAGgAaABkAGwAbABoAGQAZABoAGwAbABkAGgAYABgAGgAXABYAGQAXABkAGQAZABgAFwAXABcAFwAWABYAFgATABcAFgAVABcAFQAVABQAFAAWABQAEgATABIAEgATABMAFAATABMAEgAQABIAEQAPABEAEAAPABE

# Синтез речи

## Обзор

API синтеза речи преобразует текст в высококачественную речь. Поддерживается множество голосов и языков.

## Аутентификация

Все запросы должны включать заголовок `Authorization`:

```
Authorization: Bearer YOUR_API_KEY
```

## Конечная точка

```
POST /v1/audio/speech
```

## Параметры запроса

| Параметр | Тип | Описание | Обязательный |
|----------|-----|---------|------------|
| `text` | string | Текст для синтеза | Да |
| `voice_id` | string | ID голоса для использования | Да |
| `speed` | number | Скорость речи (0.5-2.0) | Нет |
| `pitch` | number | Высота голоса (-20 до 20) | Нет |

## Доступные голоса

- `v1_default` - голос по умолчанию
- `v1_female_01` - женский голос 1
- `v1_male_01` - мужской голос 1
- `v1_child` - детский голос

## Примеры использования

### cURL

```bash
curl -X POST https://api.example.com/v1/audio/speech \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Привет, мир!",
    "voice_id": "v1_default",
    "speed": 1.0
  }'
```

### Python

```python
import requests

response = requests.post(
    "https://api.example.com/v1/audio/speech",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={
        "text": "Привет, мир!",
        "voice_id": "v1_default",
        "speed": 1.0
    }
)

audio_data = response.content
```

## Ответ

При успешном запросе возвращается аудиоданные в формате WAV:

```json
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "VoiceId": "v1_jRFTM0hdReIsnPll+lDRCpW6+3Drq0RcmXwUTiCOGUiTuv3aNPOainIwzGPtKXaeLGs=",
        "RequestId": "15468f21-9d4a-4958-b652-454d6f7646ea"
    }
}
```

## Коды ошибок

| Код | Описание |
|-----|----------|
| 0 | Успех |
| 400 | Неверный запрос |
| 401 | Не авторизован |
| 429 | Превышен лимит запросов |
| 500 | Ошибка сервера |

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Отсутствуют коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Коды общих ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).


---
*Источник: [https://www.tencentcloud.com/document/product/1041/77775](https://www.tencentcloud.com/document/product/1041/77775)*

---
*Источник (EN): [syncdubbing.md](./syncdubbing.md)*
