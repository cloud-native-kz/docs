# Ошибка смешивания потока в прямом эфире `InvalidParameter.OtherError`

## Ошибка

Ошибка `InvalidParameter.OtherError` возникает при инициировании смешивания потока.

## Возможные причины

- Ширина или высота изображения входящего потока превышает 2000 пикселей.
- Одновременные каналы потока превышают 20.
- Учётная запись в режиме «Channel Mode» использует API `CreateCommonMixStream`.

## Решения

В следующем разделе описаны общие методы устранения неполадок для кодов подошибок.

#### Ошибка 1: `"Message":"InnerErrCode : [ -10021 ],IrnerErrMsg: [ Params Error ]"`

1. Используйте FFplay для воспроизведения потока в прямом эфире и просмотра его разрешения. Разрешение ниже составляет `1920 x 1080`, что не вызовет ошибку.
Команда: `ffplay -i "URL воспроизведения"`.
![](https://staticintl.cloudcachetci.com/cms/backend-cms/5568cc2ad44f11ee89c5525400170219.png)
2. [Используйте VLC](https://intl.cloud.tencent.com/document/product/267/32483) для воспроизведения потока в прямом эфире:
  - Откройте VLC, нажмите **Media** > **Open Network Stream** > **Network** и введите URL. После подтверждения вы сможете получить поток в прямом эфире.
  - Вы можете просмотреть разрешение потока в прямом эфире в **Tools** > **Media Information** > **Codec**.

#### Ошибка 2: `"Message":"InnerErrCode:[ -41 ],InnerErrMsg: [ ]"`

Предположим, что хост создаёт сеанс смешивания потока и затем выходит из сеанса без его отмены. Если хост войдёт в другие сеансы, одно и то же имя потока будет использоваться несколькими сеансами смешивания, что вызовет эту ошибку.

Если сеанс смешивания потока прерывается, экран смешивания остановится на последнем кадре, если фоновый поток не прерывается. Вы можете вызвать API `CancelCommonMixStream`, чтобы последний кадр не оставался на экране. Если фоновый поток прерывается, весь экран зависнет.

- Если все входящие потоки с одинаковыми именами успешно отправлены в течение 15 минут, сеанс смешивания потока будет восстановлен.
- Если все входящие потоки прерываются, сеанс смешивания потока будет автоматически отменён через 15 минут.

#### Ошибка 3: `"Message":"InnerErrCode:[ -4 ],InnerErrMsg: [ get liveconfig failed! ]"`

Вы можете обновить консоль CSS до последней версии (режим кода потока в прямом эфире) для устранения этой ошибки.

#### Ошибка 4: `"Message":"input stream num is not match the template id!"`

Для получения информации о параметрах и направлениях см. [API CreateCommonMixStream > MixStreamTemplateId](https://intl.cloud.tencent.com/document/product/267/35997).

#### Ошибка 5: `"Message":"InnerErrCode:[ -300 ],InnerErrMsg: [ outputstreamid not avaliable, outputstreamid alread use as background in other sessionid ]"`

Вы можете установить **другой** `OutputStreamName` для сеанса B, чтобы устранить эту ошибку.

#### Ошибка 6: `"Message": "InnerErrCode:[ -2 ],InnerErrMsg: [ small picture out of the background ]"`

- Инструкции по установке `LocationX` см. в разделе [CommonMixLayoutParams > LocationX](https://intl.cloud.tencent.com/document/product/267/30767#CommonMixLayoutParams).
- Инструкции по установке `LocationY` см. в разделе [CommonMixLayoutParams > LocationX](https://intl.cloud.tencent.com/document/product/267/30767#CommonMixLayoutParams).
- Для получения дополнительных примеров использования шаблонов смешивания потоков см. раздел [Смешивание потока в прямом эфире](https://intl.cloud.tencent.com/document/product/267/37665).

#### Ошибка 7: `"Message": "InnerErrCode:[ -111 ],InnerErrMsg: [ output_stream_type is [0],but output_stream_id xxxxx is not in input stream list ]"`

- Если вы установили `OutputStreamType` на `0` или оставили его пустым, вам необходимо установить `OutputStreamName` на одно из имён входящего потока.
- Если вы хотите использовать новый `OutputStreamName`, установите `OutputStreamType` на `1`.
- Если установить `OutputStreamType` на `1`, вы не сможете установить `OutputStreamName` на имена потоков ни из `InputStreamList`, ни из серверной части трансляции в прямом эфире.


---
*Источник: [https://www.tencentcloud.com/document/product/267/40599](https://www.tencentcloud.com/document/product/267/40599)*

---
*Источник (EN): [live-stream-mixing-error-invalidparameterothererror.md](./live-stream-mixing-error-invalidparameterothererror.md)*
