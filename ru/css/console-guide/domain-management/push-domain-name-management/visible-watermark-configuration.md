# Конфигурация видимого водяного знака

Функция видимого водяного знака отключена по умолчанию для прямого вещания. В этом документе описано, как связать/отвязать доменное имя вещания с/от шаблона видимого водяного знака для включения/отключения функции видимого водяного знака.

## Примечания

- Конфигурация шаблона вступит в силу примерно через 5–10 минут.
- После успешной привязки шаблона функция видимого водяного знака будет включена для адресов вещания под указанным доменным именем вещания.
- Одно доменное имя можно привязать только к одному шаблону видимого водяного знака. После их привязки все потоки под этим доменным именем будут снабжены видимым водяным знаком в соответствии с этим шаблоном.

## Предварительные требования

- Вы вошли в [консоль CSS](https://console.tencentcloud.com/live/livestat) и добавили [доменное имя для вещания](https://tencentcloud.com/document/product/267/35970).
- Вы создали [шаблон видимого водяного знака](https://www.tencentcloud.com/document/product/267/31073#Watermark).

## Привязка шаблона видимого водяного знака

1. Перейдите в раздел [Domain Management](https://console.tencentcloud.com/live/domainmanage) и нажмите на **доменное имя для вещания**, которое необходимо настроить, или **Manage**, чтобы открыть страницу сведений о доменном имени.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/7d85d9d6d0c411f084a45254005ef0f7.png)

2. Выберите **Template Configuration** и нажмите **Edit** в разделе **Visible Watermark Configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/fb2a7544d1a511f08f8f525400454e06.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/147fd44fd1a611f0b1675254001c06ec.png)

3. Выберите шаблон водяного знака и нажмите **Confirm**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/f1dd36d7d0c311f0b638525400e889b2.png)

> **Примечание:** Вы можете нажать **Preview** в столбце Operation, чтобы просмотреть видимый водяной знак.

## Отвязка шаблона видимого водяного знака

1. Перейдите в раздел [Domain Management](https://console.tencentcloud.com/live/domainmanage) и нажмите на **доменное имя для вещания**, которое необходимо настроить, или **Manage**, чтобы открыть страницу сведений о доменном имени.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/881633b3d0c411f08823525400454e06.png)

2. Выберите **Template Configuration** и нажмите **Edit** в разделе **Visible Watermark Configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/72c91d37d1a611f0b1675254001c06ec.png)

3. Очистите целевой шаблон и нажмите **Confirm**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/4c915748d0c411f0a3b05254007c27c5.png)


---
*Источник: [https://www.tencentcloud.com/document/product/267/31064](https://www.tencentcloud.com/document/product/267/31064)*

---
*Источник (EN): [visible-watermark-configuration.md](./visible-watermark-configuration.md)*
