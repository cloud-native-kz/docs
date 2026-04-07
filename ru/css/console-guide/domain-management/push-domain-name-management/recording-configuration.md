# Конфигурация записи

Функция живой записи отключена по умолчанию. Этот документ описывает, как привязать шаблон записи к домену трансляции, чтобы включить функцию записи, а также как отвязать шаблон, чтобы отключить эту функцию.

## Ограничения использования

- Шаблон вступает в силу примерно через 5-10 минут после привязки к домену.
- После успешной привязки шаблона к домену трансляции запись будет включена для адресов трансляции под этим доменом.
- К одному домену можно привязать только один шаблон записи. После привязки все потоки под этим доменом будут записаны согласно шаблону.
- Смешанная запись потоков не поддерживает смешивание потоков внутри китайского материка с потоками снаружи. Это вызовет ошибку и воспроизведение не будет работать.

## Предварительные условия

- Вы вошли в [консоль CSS](https://console.tencentcloud.com/live) и добавили [домен трансляции](https://intl.cloud.tencent.com/document/product/267/35970).
- Вы [создали шаблон записи](https://intl.cloud.tencent.com/document/product/267/34223).

## Привязка шаблона записи

1. Перейдите на страницу [Domain Management](https://console.tencentcloud.com/live/domainmanage), щелкните целевой **домен трансляции** или нажмите **Manage**, чтобы войти на страницу сведений о домене.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/1f54892b4a6111efbaba525400d5f8ef.png)

2. Выберите вкладку **Template Configuration** и нажмите **Edit** в области **Recording configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/2dbaa107ab0511f09710525400e889b2.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/4827df4bab0511f09710525400e889b2.png)

3. Выберите шаблон записи и нажмите **Confirm**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/6ea76cdeab0511f0b08552540044a08e.png)

## Отвязка шаблона записи

1. Перейдите на страницу [Domain Management](https://console.tencentcloud.com/live/domainmanage), щелкните целевой **домен трансляции** или нажмите **Manage**, чтобы войти на страницу сведений о домене.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7a78374f4a6111efbaba525400d5f8ef.png)

2. Выберите вкладку **Template Configuration** и нажмите **Edit** в области **Recording configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/e83400d9ab0511f0a68e5254001c06ec.png)

3. Отмените выбор шаблона и нажмите **Save**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/3d643c5dab0611f0b08552540044a08e.png)

> **Примечание:** Отвязка шаблона записи не повлияет на текущие живые трансляции. Чтобы отменить запись для текущих потоков, остановите потоки и отправьте их снова.

## Получение файлов записи

### Запись на VOD

#### Из консоли VOD

Войдите в [консоль VOD](https://console.intl.cloud.tencent.com/vod/app-manage), выберите целевое подприложение и нажмите **Video/Audio Management** на левой боковой панели. На этой странице вы сможете просмотреть все файлы записей.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/6eb5ea3d4a6211efb36952540075b605.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/f66ce7564a6211ef8f105254002693fd.png)

#### Из обратных вызовов записи

Если вы настроили адрес обратного вызова записи в консоли или с помощью API, после создания файла записи на настроенный адрес обратного вызова будет отправлено уведомление. Подробную информацию о полях обратного вызова см. в разделе [How to Receive Event Notification](https://intl.cloud.tencent.com/document/product/267/38080).

> **Примечание:** Метод обратного вызова записи рекомендуется благодаря его надежности и оперативности.

#### Использование API VOD

Вы также можете вызвать API [SearchMedia](https://intl.cloud.tencent.com/document/product/266/34179) VOD для запроса файлов записи.

### Запись на COS

#### Из консоли COS

Войдите в консоль COS, нажмите [Bucket List](https://console.tencentcloud.com/cos/bucket) на левой боковой панели, а затем нажмите целевой бакет. Вы сможете найти файлы записей в списке файлов.


---
*Источник: [https://www.tencentcloud.com/document/product/267/34224](https://www.tencentcloud.com/document/product/267/34224)*

---
*Источник (EN): [recording-configuration.md](./recording-configuration.md)*
