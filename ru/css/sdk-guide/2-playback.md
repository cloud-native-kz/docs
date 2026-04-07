# 2. Воспроизведение

## Предварительные требования

- Вы активировали сервис CSS.
- Выберите [Управление доменами](https://console.tencentcloud.com/live/domainmanage), нажмите **Добавить домен** и добавьте домен воспроизведения согласно инструкциям в разделе [Добавление собственного домена](https://www.tencentcloud.com/document/product/267/35970).
- В консоли CSS создайте адрес воспроизведения в **CSS Toolkit** > **Address Generator** согласно инструкциям в разделе [Address Generator](https://www.tencentcloud.com/document/product/267/31084). Затем реализуйте прямое воспроизведение в своем приложении на основе ваших сценариев следующим образом:

## Интеграция в приложение

Загрузите и интегрируйте MLVB SDK согласно инструкциям в руководствах интеграции для [iOS](https://www.tencentcloud.com/document/product/1071/41875) и [Android](https://www.tencentcloud.com/document/product/1071/44558).

> **Примечание:** Включите захват потока и воспроизведение. Ниже приведена конфигурация для iOS и Android:iOSV2TXLivePlayer *_txLivePlayer = [[V2TXLivePlayer alloc] init];AndroidV2TXLivePlayer mLivePlayer = new V2TXLivePlayerImpl(mContext);

## Дополнительно

- Использование MLVB SDK влечет за собой расходы. Сведения о выставлении счетов см. в разделе [Обзор выставления счетов](https://www.tencentcloud.com/document/product/1071/50630).


---
*Источник: [https://www.tencentcloud.com/document/product/267/51155](https://www.tencentcloud.com/document/product/267/51155)*

---
*Источник (EN): [2-playback.md](./2-playback.md)*
