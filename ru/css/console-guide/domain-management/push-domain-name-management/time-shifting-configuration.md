# Конфигурация сдвига времени

В этом документе описано, как привязать шаблон сдвига времени к домену push для включения функции сдвига времени для домена, а также как отвязать шаблон для отключения функции. Функция сдвига времени отключена по умолчанию.

## Ограничения использования

- После успешной привязки шаблона сдвига времени к домену push функция сдвига времени будет включена для push-адресов в этом домене.
- Один домен может быть привязан только к одному шаблону сдвига времени. После привязки функция сдвига времени будет включена для всех потоков в домене.

## Предварительные условия

- Вы вошли в [консоль CSS](https://console.tencentcloud.com/live) и добавили [домен push](https://intl.cloud.tencent.com/document/product/267/35970).
- Вы создали [шаблон сдвига времени](https://www.tencentcloud.com/document/product/267/53312#creating-a-time-shifting-template).

## Привязка шаблона сдвига времени

1. Перейдите в [Domain Management](https://console.tencentcloud.com/live/domainmanage), нажмите на целевой **домен push** или нажмите **Manage**, чтобы перейти на страницу сведений о домене.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/34e25fd10c6111ef8fbd5254008af8cc.png)

2. Выберите вкладку **Template Configuration** и нажмите **Edit** в области **Time shifting configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/1eb17b2aab0711f09b75525400bf7822.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/104dd197ab0711f09b75525400bf7822.png)

3. Выберите шаблон сдвига времени и нажмите **Confirm**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/00d34634737711f087e15254005ef0f7.png)

## Отвязка шаблона сдвига времени

1. Перейдите в [Domain Management](https://console.tencentcloud.com/live/domainmanage), нажмите на целевой **домен push** или нажмите **Manage**, чтобы перейти на страницу сведений о домене.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/489a63c70c6111ef8fbd5254008af8cc.png)

2. Выберите вкладку **Template Configuration** и нажмите **Edit** в области **Time shifting configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/1cef3083737711f084fc525400bf7822.png)

3. Снимите выделение с шаблона и нажмите **Save**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/48aaac9a737711f0b9a25254007c27c5.png)

> **Примечание:** Отвязка шаблона сдвига времени не повлияет на текущие трансляции.


---
*Источник: [https://www.tencentcloud.com/document/product/267/52829](https://www.tencentcloud.com/document/product/267/52829)*

---
*Источник (EN): [time-shifting-configuration.md](./time-shifting-configuration.md)*
