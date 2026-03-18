# Шифрование прямых трансляций FLV

Большинство частных прямых трансляций или трансляций, требующих защиты контента, не нуждаются в аппаратной защите и сложных процессах распределения и проверки сертификатов. Кроме того, на внутреннем рынке прямые трансляции по протоколу FLV также популярны. Требуется защищенное решение для прямых трансляций FLV.

**Сценарий использования**: При использовании протокола FLV для воспроизведения требуется шифровать содержимое потока, чтобы злоумышленники не могли перехватить его через сеть, и даже если поток будет сохранен локально, его нельзя было бы воспроизвести.

**План реализации**: Tencent Cloud CSS разработала собственное решение для шифрования потока. Клиенты могут запросить шифрование FLV, отправив тикет с указанием режима шифрования (видео шифрование, аудио и видео шифрование), и Tencent Cloud будет шифровать прямую трансляцию в соответствии с указанным модулем. При расшифровке и воспроизведении клиенты могут получить ключевое поле TXEncryptionToken через интерфейс API Tencent Cloud DescribeDRMLicense, добавить его в параметры URL воспроизведения и предоставить его SDK для расшифровки и воспроизведения.

**Процесс самостоятельной разработки шифрования и расшифровки выглядит следующим образом:**

![](https://staticintl.cloudcachetci.com/cms/backend-cms/3c4e692e5da611ee9ff8525400d917da.png)

**Метод реализации:** Для получения подробной информации о процессе реализации обратитесь к отделу продаж Tencent Cloud или отправьте тикет в службу поддержки Tencent Cloud CSS.

**Преимущества решения:** Весь процесс управляем, имеется поддержка продуктов и инструментов для ключей и шифрования/расшифровки. Tencent Cloud предоставляет Player SDK, который легко интегрировать и имеет зрелое решение.

**Существующие проблемы:** Необходимость интеграции SDK, поддержка только пользовательских плееров. Веб и браузеры не поддерживаются.

Это решение предоставляет два метода доступа для iOS и Android. Нажмите [здесь](https://www.tencentcloud.com/document/product/1071/55454), чтобы загрузить SDK.

## Интеграция iOS

```
/**Create a Player Instance. */V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];/** * Set the video rendering View for the player. This control is responsible for displaying the video content. * * @param view Player Rendering View * @return Return Value {@link V2TXLiveCode} *         - V2TXLIVE_OK：Success */[player setRenderView:view];/** * Set the player callback. * * By setting the callback, you can listen to some callback events of the V2TXLivePlayer player, * This includes player status, playback volume callback, audio and video first frame callback, statistical data, warnings, and error information, etc. * @param observer The target object for the player's callback. For more information, please check {@link V2TXLivePlayerObserver} */[player setObserver:self];/** * For key requests, please refer to License acquisition. * Set the Key * * @note The URL in the JSON must be the same as the URL in startLivePlay. The SDK performs a second validation through the URL to avoid incorrect decryption caused by a mismatch between the key and the URL. */NSString *url = @"http://5000.liveplay.myqcloud.com/live/flvtest100_1000.flv?request_type=STDFLV&TXEncryptionToken=ZW5jTW9kZT01JmVuY0tleT0yNmFjZWIxMjViNDczMWNjODRkZTAxZWEyNDA3ZDVmZCZlbmNJVj1iZmEwYmI0NDRhN2NhNDUyMDRjMmNhNzZhYWQyMWFjNA==";/** * Start playing the audio and video stream. * * @param url The playback address of the audio and video stream, supporting RTMP, HTTP-FLV, TRTC，HLS。 * @return Return Value {@link V2TXLiveCode} *         - V2TXLIVE_OK: Operation successful, start connecting and playing *         - V2TXLIVE_ERROR_INVALID_PARAMETER: Operation failed, the URL is not valid *         - V2TXLIVE_ERROR_REFUSED: RTC does not support pushing and pulling the same StreamId on the same device at the same time.[player startLivePlay:url];
```

## Интеграция Android

```
/** * Create a Player Instance. */V2TXLivePlayer player = new V2TXLivePlayer();/** * Set the video rendering View for the player. This control is responsible for displaying the video content. * * @param view Player rendering View * @return Return value {@link V2TXLiveCode} *         - V2TXLIVE_OK：Success */player.setRenderView(view);/** * Set the player callback.  * * By setting the callback, you can listen to some callback events of the V2TXLivePlayer player, * including player status, playback volume callback, audio and video first frame callback, statistical data, warnings, and error information, etc. * * @param observer the callback target object of the player,For more information, please refer to {@link V2TXLivePlayerObserver} */player.setObserver(this);/** * For key request, please refer to License acquisition * Set the key * * @note The URL in the JSON must be the same as the URL in startLivePlay. The SDK performs a secondary verification through the URL to avoid the situation where the key and URL do not match, causing incorrect decryption. */String url = "http://5000.liveplay.myqcloud.com/live/flvtest100_1000.flv?request_type=STDFLV&TXEncryptionToken=ZW5jTW9kZT01JmVuY0tleT0yNmFjZWIxMjViNDczMWNjODRkZTAxZWEyNDA3ZDVmZCZlbmNJVj1iZmEwYmI0NDRhN2NhNDUyMDRjMmNhNzZhYWQyMWFjNA==";/** * Start playing the audio and video stream.  * * @param url @param url The playback address of the audio and video stream, supporting RTMP, HTTP-FLV, TRTC, and HLS. * @return Return value {@link V2TXLiveCode} *         - V2TXLIVE_OK: Operation succeeded, start connecting and playing *         - V2TXLIVE_ERROR_INVALID_PARAMETER: Operation failed, the URL is not valid *         - V2TXLIVE_ERROR_REFUSED: RTC does not support pushing and pulling the same StreamId on the same device at the same time.。 */player.startLivePlay(url);
```

## Получение лицензии

- Установите имя интерфейса API как DescribeDRMLicense.
- Домен запроса интерфейса: drm.tencentcloudapi.com.
- Разработчикам необходимо указать значение типа DRM как NORMALAES, значение типа Track как SD для шифрования, значение ContentType как LiveVideo и ContentId как идентификатор потока пользователя.
  - Пример:
  - Запрос в тестовой среде:

```
POST / HTTP/1.1Host: drm.tencentcloudapi.comContent-Type: application/jsonX-TC-Action: DescribeDRMLicense<Public Request Parameters>{ "DrmType":"NORMALAES", "ContentId":"flvtest100", "Tracks":[  "SD" ], "ContentType":"LIVEVIDEO"}
```

  - Результат запроса:

```
{ "Response": {  "ContentId": "flvtest100",  "TXEncryptionToken": "ZW5jTW9kZT01JmVuY0tleT0yNmFjZWIxMjViNDczMWNjODRkZTAxZWEyNDA3ZDVmZCZlbmNJVj1iZmEwYmI0NDRhN2NhNDUyMDRjMmNhNzZhYWQyMWFjNA==",  "RequestId": "47f336fd-b05a-4192-b1f4-8f9d4c5f76f1" }}
```


---
*Источник: [https://www.tencentcloud.com/document/product/267/57047](https://www.tencentcloud.com/document/product/267/57047)*

---
*Источник (EN): [live-flv-encryption.md](./live-flv-encryption.md)*
