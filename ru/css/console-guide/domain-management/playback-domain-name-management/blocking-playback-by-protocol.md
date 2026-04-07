# Блокировка воспроизведения по протоколу

Вы можете блокировать воспроизведение для домена путем блокирования определённых протоколов. Запросы на воспроизведение, использующие заблокированные протоколы, будут отклонены.

## Предварительные требования

- Вы активировали CSS и вошли в [консоль CSS](https://console.tencentcloud.com/live/livestat).
- Вы добавили [доменное имя для воспроизведения](https://intl.cloud.tencent.com/document/product/267/35970).

## Блокирование протоколов

1. Выберите [Domain Management](https://console.tencentcloud.com/live/domainmanage) на левой боковой панели. Щелкните на имя целевого доменного имени для воспроизведения или нажмите **Manage** справа, чтобы перейти на страницу управления доменом.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/847684513f2d11efa56d525400d5f8ef.png)

2. Выберите вкладку **Access Control**. В области **Block playback by protocol** вы можете блокировать воспроизведение, использующее протоколы RTMP, FLV, HLS, DASH и WebRTC.
3. Нажмите **Edit** и включите протоколы, которые вы хотите блокировать.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/14797758cc0911f08e74525400bf7822.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/2c084906cc0911f08658525400454e06.png)

4. Нажмите **Save**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/426b340fcc0911f0ae4f52540099c741.png)

> **Примечание:** Конфигурация блокирования применяется некоторое время. После настройки заблокированных протоколов подождите, пока конфигурация вступит в силу, прежде чем блокировать другие протоколы. За исключением HLS, блокирование протокола применяется только к новым трансляциям. Это не влияет на текущие потоки.

## Разблокирование протоколов

Для разблокирования заблокированного протокола выполните следующие шаги:

1. Выберите [Domain Management](https://console.tencentcloud.com/live/domainmanage) на левой боковой панели. Щелкните на имя целевого доменного имени для воспроизведения или нажмите **Manage** справа, чтобы перейти на страницу управления доменом.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/07550d3d3f2e11efa56d525400d5f8ef.png)

2. Выберите вкладку **Access Control**. В области **Block playback by protocol** отключите протокол, который вы хотите разблокировать.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/502f09dfcc0911f096d1525400e889b2.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9ff3409fcc0c11f08e74525400bf7822.png)

3. Нажмите **Save**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b1580272cc0c11f091ab5254007c27c5.png)


---
*Источник: [https://www.tencentcloud.com/document/product/267/48703](https://www.tencentcloud.com/document/product/267/48703)*

---
*Источник (EN): [blocking-playback-by-protocol.md](./blocking-playback-by-protocol.md)*
