# Корректировка содержания биллинга для стандартного транскодирования и транскодирования с кодеком Top Speed облачных сервисов трансляции

Для обеспечения более упорядоченного и четкого опыта выверки, начиная с **16 апреля 2024 года в полночь**, облачные сервисы трансляции (CSS) внесут изменения в название подпродукта, идентификатор ресурса, тип компонента, название компонента, единицу цены, использование, продолжительность использования и единицу продолжительности в счете за стандартное транскодирование и транскодирование с кодеком Top Speed, а также добавят типы транскодирования для различения различных интервалов биллинга транскодирования.

Взяв в качестве примера стандартное транскодирование с дневной выверкой H264_1080P, сравнение счета до и после корректировки выглядит следующим образом:

| До и после корректировки счета | ProductName | SubproductName | TransactionTime | Usage Start Time | Usage End Time | InstanceID | Region | ComponentType | ComponentName | Component List Price | Component Contracted Price | Transcode Type | Component Price Measurement Unit | Component Usage | Component Usage Unit | Usage Duration | Duration Unit | Blended Discount Multiplier | Total Cost (Including Tax) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| До корректировки | Cloud Streaming Services | *live-domestic* | 2024/5/3 06:52 | 2024/5/2 00:00 | 2024/5/2 23:59 | *1234567888_101618_live_trans_20240502_liveprocessor_H264_1080P_1* | Regions Outside Chinese Mainland | *live_transcoding* | *live_transcoding_monthly* | 0.0111 | 0.0111 | - | *USD/3Minute/Minute* | *3* | Minute | *80000* | *Minute* | 1 | 888 |
| После корректировки | Cloud Streaming Services | *live transcoding* | 2024/5/3 06:52 | 2024/5/2 00:00 | 2024/5/2 23:59 | *1234567888_301262_sv_live_transcode_daily_20240502_liveprocessor_H264_1080P_1* | Regions Outside Chinese Mainland | *Live Transcode Duration* | *Live Transcode Daily* | 0.0111 | 0.0111 | *Standard Transcode H.264_1080P* | *USD/Minute* | *80000* | Minute | *1* | *Day* | 1 | 888 |

> **Примечание:** Ранее счет за транскодирование использовал единицу цены и использование для обозначения различных интервалов биллинга транскодирования, и фактическое использование было включено в продолжительность использования, что могло легко вызвать двусмысленность при выверке. В скорректированном счете фактическое использование включено в использование. Эта корректировка изменяет только содержание отображения счета и не влияет на правила выставления счетов или сумму выставления счетов.

Если у вас возникнут вопросы, не стесняйтесь [связаться с нами](https://console.tencentcloud.com/workorder/category). Мы искренне благодарны пользователям за доверие и поддержку облачных сервисов трансляции (CSS) Tencent Cloud.

****

**2024-04-03**

**Команда облачных сервисов трансляции Tencent Cloud**


---
*Источник: [https://www.tencentcloud.com/document/product/267/59865](https://www.tencentcloud.com/document/product/267/59865)*

---
*Источник (EN): [billing-content-adjustment-for-cloud-streaming-services-standard-transcoding-and-top-speed-codec-transcoding.md](./billing-content-adjustment-for-cloud-streaming-services-standard-transcoding-and-top-speed-codec-transcoding.md)*
