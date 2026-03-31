# TMIO SDK

## Обзор

С появлением все большего количества протоколов потокового вещания создание приложения, поддерживающего все протоколы, стало сложной задачей. Для решения этой проблемы мы разработали SDK Tencent Media IO (TMIO), оптимизированный для основных протоколов на рынке, чтобы помочь вам легко создавать стабильные и высокодоступные медиа-приложения.
SDK TMIO поддерживает основные протоколы, включая SRT и QUIC, а также собственный протокол Tencent — Elastic Transmission Control (ETC). В будущем будут добавлены новые протоколы.

### Преимущества

- **Поддержка множества платформ**: SDK доступен для Android, iOS, Linux, macOS и Windows.
- **Различные методы интеграции**:
  - Вы можете использовать неинтрузивный [режим прокси](#integration-directions) для работы с SDK без каких-либо изменений кода.
  - Простой дизайн API также позволяет вам быстро [интегрировать](#integrating-the-tmio-sdk-into-your-application) SDK в ваше приложение, заменив существующие протоколы.
- **Простой дизайн API с высокой совместимостью и гибкостью**:
  - Предлагаются удобные в использовании API.
  - Вы можете выбрать различные режимы и политики в зависимости от вашего бизнес-сценария.
  - SDK может быть расширен для поддержки других протоколов.
- **Поддержка и оптимизация нескольких протоколов**:
  - SDK поддерживает новые протоколы потокового вещания, включая SRT и QUIC, а также собственный протокол ETC компании Tencent.
  - Он может удовлетворить многие требования в различных бизнес-сценариях.
  - Обеспечивает передачу с низкой задержкой, безопасную и надежную передачу на базе UDP.
  - Поддерживает ускорение с несколькими подключениями, что гарантирует стабильность и плавность передачи.

### Тестирование (TMIO SRT)

- **SDK TMIO поддерживает протокол SRT, который может повысить стабильность восходящего канала и плавность нисходящего канала в условиях плохого качества сети или при передаче на большие расстояния.**
В приведенном ниже тесте с потоковой передачей RTMP воспроизведение начинает заикаться при потере пакетов 10%, но при потоковой передаче SRT стабильность и низкая задержка гарантируются даже при потере пакетов 30%.

### Функции

- **Передача потокового медиа на базе SRT**
  - **Высокая устойчивость к случайной потере пакетов**
  - **Механизм повторной передачи на основе ARQ и политика тайм-аута**
  - **Передача с низкой задержкой, безопасная и надежная на базе UDT**
  - **Передача с несколькими подключениями и режим агрегированной передачи**:
Вы можете настроить несколько подключений для передачи данных. Например, мобильные устройства могут передавать данные как через Wi-Fi, так и через сеть данных 4G/5G, поэтому даже если одно из подключений разорвано, передача данных не будет нарушена. Это повышает надежность передачи.

| Режим передачи | Описание |
| --- | --- |
| Режим трансляции | Вы можете отправлять избыточные данные по нескольким интернет-подключениям для обеспечения целостности данных и надежности передачи. |
| Режим основного/резервного | В этом режиме активно только одно подключение одновременно. Подключение выбирается в реальном времени на основе стабильности и надежности. Это также снижает использование полосы пропускания, поскольку избыточные данные не отправляются. |
| Режим агрегации | В сценариях, требующих высокого битрейта и полосы пропускания, полоса пропускания одного интернет-подключения может быть недостаточной. Этот режим может разбивать данные, отправлять их по нескольким подключениям, а затем объединять их на стороне получателя. |

- **Передача медиа на базе QUIC**
  - **Адаптивный алгоритм управления перегруженностью**
  - **Плавное переключение сети**
  - **Поддержка протокола HTTP/3 следующего поколения**
  - **Меньше избыточных данных при ограниченной полосе пропускания или нестабильной сети**
- **Собственный протокол потокового вещания ETC**
  - **Инновационный, легкий и кроссплатформенный**
  - **Поддержка устройств IoT (одноранговая связь)**
  - **Быстрый запуск, низкая задержка и эффективное использование полосы пропускания**
  - **Быстрое и точное обнаружение изменений интернет-соединения для обеспечения использования оптимальной политики передачи**
  - **Справедливое и стабильное использование полосы пропускания при использовании вместе с основными протоколами потокового вещания**

## Направления интеграции

Приведенные ниже направления используют протокол RTMP over SRT в качестве примера.

### Использование режима прокси

#### Рабочий процесс

![](https://staticintl.cloudcachetci.com/cms/backend-cms/70006c282b9311ee818e525400088f3a.jpeg)

#### Инструкции

1. **Создайте экземпляр**`TmioProxy`**:**

```
std::unique_ptr<tmio::TmioProxy> proxy_ = tmio::TmioProxy::createUnique();
```

2. **Установите слушателя**:

```
void setListener(TmioProxyListener *listener);
```

Ниже приведены обратные вызовы `TmioProxyListener`:

Обратный вызов конфигурации TMIO

Обратный вызов запуска прокси TMIO

Обратный вызов ошибки

Вы можете настроить параметры `Tmio` в этом обратном вызове. **Для простой конфигурации вы можете использовать вспомогательные методы, предусмотренные в**`tmio-preset.h`**.**

```
/*void onTmioConfig(Tmio *tmio);*/void onTmioConfig(tmio::Tmio *tmio) override {        auto protocol = tmio->getProtocol();        if (protocol == tmio::Protocol::SRT) {                tmio::SrtPreset::rtmp(tmio);        } else if (protocol == tmio::Protocol::RIST) {                tmio->setIntOption(tmio::base_options::RECV_SEND_FLAGS,                                                     tmio::base_options::FLAG_SEND);        }}
```

```
/*void onStart(const char *local_addr, uint16_t local_port); */void onStart(const char *addr, uint16_t port) override {        LOGFI("ip %s, port %" PRIu16, addr, port);}
```

Этот обратный вызов указывает, что удаленный сервер успешно подключен, а локальный TCP-порт успешно привязан. Вы можете начать отправку потоков.

```
/*void onError(ErrorType type, const std::error_code &err);*/void onError(tmio::TmioProxyListener::ErrorType type,                        const std::error_code &err) override {        LOGFE("error type %s, %s, %d", tmio::TmioProxyListener::errorType(type),                    err.message().c_str(), err.value());}
```

Вы можете использовать `ErrorType` для определения того, является ли ошибка локальной или удаленной ошибкой ввода-вывода. Локальная ошибка ввода-вывода обычно возникает потому, что потоковое вещание RTMP остановлено трансляционным устройством. Поэтому, если потоковое вещание завершилось, вы можете игнорировать такие ошибки. Однако удаленная ошибка ввода-вывода обычно требует обработки.

3. **Запустите прокси**:

```
std::error_code start(const std::string &local_url, const std::string &remote_url, void * config=nullptr)
```

  - Параметры API

| Параметр | Описание |
| --- | --- |
| local_url | Поддерживает только схему TCP в формате tcp://${ip}:${port}. `port` может быть `0`, что указывает на привязку к случайному порту. После успешной привязки привязанный порт будет возвращен приложению через обратный вызов `onStart()`. Использование порта `0` может избежать отказов при привязке из-за проблем, таких как занятость порта и отсутствие разрешений. |
| remote_url | URL удаленного сервера. |
| config | Параметр конфигурации. Этот параметр действителен, если включена привязка подключений SRT или QUIC H3. Подробнее см. определение структуры `SrtFeatureConfig` в tmio.h. |

  - Пример кода для одного подключения:

```
 proxy_->start(local_url, remote_url, NULL);
```

  - Пример кода для привязки нескольких подключений:

```
tmio::TmioFeatureConfig option;option_.protocol = tmio::Protocol::SRT;option_.trans_mode = static_cast<int>(tmio::SrtTransMode::SRT_TRANS_BACKUP);/*-----------------------------------------------------------*/{// Вы можете добавить несколько подключений по мере необходимости.option_.addAvailableNet(net_name, local_addr, remote_url, 0, weight, -1);}/*-----------------------------------------------------------*/ proxy_->start(local_url, remote_url, &option_);
```

4. **Остановите прокси**:

```
/*void stop();*/proxy_.stop();
```

### Интеграция SDK TMIO в ваше приложение

#### Рабочий процесс

![](https://staticintl.cloudcachetci.com/cms/backend-cms/701447d22b9311eea27e525400c56988.jpeg)

## Инструкции

1. **Создайте экземпляр**`Tmio`**и настройте параметры**:

```
tmio_ = tmio::TmioFactory::createUnique(tmio::Protocol::SRT);tmio::SrtPreset::mpegTsLossless(tmio_.get());tmio_->setIntOption(tmio::srt_options::CONNECT_TIMEOUT, 4000);tmio_->setBoolOption(tmio::base_options::THREAD_SAFE_CHECK, true);
```

  - **Создайте экземпляр**`Tmio`**: Вы можете использовать `TmioFactory` для его создания.
  - **Настройте параметры**: Выберите различные API для настройки параметров:
    - Параметры: см. tmio-option.h.
    - Простая конфигурация: см. tmio-preset.h.

```
// Выберите подходящую конфигурацию на основе различных атрибутов параметровbool setBoolOption(const std::string &optname, bool value);bool setIntOption(const std::string &optname, int64_t value);bool setDoubleOption(const std::string &optname, double value);bool setStrOption(const std::string &optname, const std::string &value);...
```

2. **Начните подключение**:

```
/** * открыть поток, указанный url * * @param config зависит от протокола */virtual std::error_code open(const std::string &url,                              void *config = nullptr) = 0;
```

  - Одно подключение (`config` может быть `NULL`)

```
// Одно подключение по умолчаниюauto err = tmio->open(TMIO_SRT_URL);if (err) {LOGE("open failed, %d, %s", err.value(), err.message().c_str());}
```

  - Привязка нескольких подключений (в настоящее время поддерживается только протокол SRT)
    - Для информации о том, как установить `config` для функции привязки SRT, см. определение структуры `TmioFeatureConfig` в файле `tmio.h`.

```
tmio::TmioFeatureConfig option_;option_.protocol = tmio::Protocol::SRT;option_.trans_mode = static_cast<int>(tmio::SrtTransMode::SRT_TRANS_BACKUP);option_.addAvailableNet(net_name, local_addr, remote_url, 0, weight, -1);
```

```
// Привязка нескольких подключенийauto err = tmio_->open(TMIO_SRT_URL, &option_);if (err) { LOGE("open failed, %d, %s", err.value(), err.message().c_str());}
```

  - При привязке нескольких подключений вы можете использовать API `open` для добавления новых подключений передачи в группу.
3. **Отправьте данные**:

```
int ret = tmio_->send(buf.data(), datalen, err);if (ret < 0) {        LOGE("send failed, %d, %s", err.value(), err.message().c_str());        break;}
```

4. **Получение данных**:
  - Для протоколов, включающих взаимодействие, таких как RTMP, необходимо вызвать API для чтения данных. Мы предлагаем два API для этого:

```
/*** получить данные** @param err возвращает детали ошибки* @return количество полученных байтов или < 0 для указания ошибки*/virtual int recv(uint8_t *buf, int len, std::error_code &err) = 0;using RecvCallback = std::function<bool(const uint8_t *buf, int len, const std::error_code &err)>;/*** получить данные в цикле событий** recvLoop() блокирует текущий поток, получает данные в цикле и передает данные в recvCallback* @param recvCallback вернуть true для продолжения цикла приема, false для разрыва*/virtual void recvLoop(const RecvCallback &recvCallback) = 0;
```

  - Циклическое чтение приложением верхнего уровня:

```
        while (true) {    ret = tmio_->recv(buf.data(), buf.size(), err);    if (ret < 0) {        LOGE("recv error: %d, %s", err.value(), err.message().c_str());        break;    }    ...}
```

  - Чтение через обратный вызов:

```
FILE *file = fopen(output_path, "w");tmio_->recvLoop([file](const uint8_t *buf, int len,                                                const std::error_code &err) {    if (len < 0) {            fwrite(buf, 1, len, file);    } else if (len < 0) {            LOGE("recv error: %d, %s", err.value(), err.message().c_str());    }    return true;});
```

5. **Завершить экземпляр**`Tmio`**:**

```
tmio_->close();
```

6. **Дополнительно**:
Получить текущий статус соединения (ваше приложение может корректировать политику отправки потока на основе статуса):

```
tmio::PerfStats stats_;tmio_->control(tmio::ControlCmd::GET_STATS, &stats_);
```

## Обновления API и демонстрации

Чтобы получить последние обновления об API и демонстрациях SDK, посетите [эту страницу GitHub](https://github.com/tencentyun/tmio/blob/master/README_en.md).

## Часто задаваемые вопросы

### Поддерживается ли привязка нескольких подключений SRT на всех устройствах?

Привязку нескольких подключений могут использовать только устройства с несколькими доступными сетевыми интерфейсами, а устройства Android могут использовать эту функцию только если версия Android 6.0 или выше и уровень API 23 или выше.

### Как включить сеть данных 4G/5G на телефоне Android, подключенном к Wi-Fi?

Телефон Android, подключенный к Wi-Fi, не может передавать данные непосредственно через сеть 4G/5G. Чтобы включить сеть данных, запросите разрешение на использование сети данных следующим образом:

```
ConnectivityManager connectivityManager = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);NetworkRequest request = new NetworkRequest.Builder().addTransportType(NetworkCapabilities.TRANSPORT_CELLULAR)                                           .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)                                           .build();ConnectivityManager.NetworkCallback networkCallback = new ConnectivityManager.NetworkCallback(){    @Override    public void onAvailable(@NonNull Network network) {                Log.d(TAG, "The mobile data network has been enabled");        super.onAvailable(network);    }}
```


---
*Источник: [https://www.tencentcloud.com/document/product/267/51158](https://www.tencentcloud.com/document/product/267/51158)*

---
*Источник (EN): [tmio-sdk.md](./tmio-sdk.md)*
