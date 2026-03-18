# Конфигурация Smart Highlight

Функция Smart Highlight отключена по умолчанию для потокового вещания. В этой статье показано, как включить функцию Smart Highlight при связывании шаблона Smart Highlight с указанным доменом push, а также как отвязать шаблон и отключить функцию Smart Highlight после успешной связи.

## Примечания

- После успешного создания шаблона его можно связать с доменом push. После успешной связи потребуется примерно 5-10 минут для вступления в силу, и Smart Highlight будет активирован сразу же, когда связанный домен успешно начнет отправлять данные.
- Изменения, связывание и отвязывание шаблона влияют только на трансляции, обновляемые в дальнейшем. Текущие трансляции остаются без изменений; чтобы применить новые правила, текущую трансляцию необходимо прервать и повторно отправить.
- С одним доменом можно связать только один шаблон Smart Highlight. После связи все потоки под этим доменом будут использовать Smart Highlight в соответствии со связанным шаблоном.

## Предварительные условия

- Вы успешно вошли в [консоль CSS](https://console.tencentcloud.com/live/livestat) и завершили [добавление собственного домена](https://www.tencentcloud.com/document/product/267/35970).
- Шаблон Smart Highlight был успешно создан.

## Связывание шаблона Smart Highlight

1. Перейдите в [Управление доменами](https://console.tencentcloud.com/live/domainmanage). Нажмите на **Имя домена**, который требуется настроить, или **Управление**, чтобы перейти на страницу деталей домена.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d77ddc24c5b711f0a62b5254007c27c5.png)

2. Выберите вкладку **Конфигурация шаблона**. Нажмите **Редактировать** в правом верхнем углу раздела **Конфигурация Smart Highlight**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b8f0de0ac5ba11f086d9525400e889b2.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/cc257e90c5ba11f0a7ca5254001c06ec.png)

3. Выберите шаблон конфигурации Smart Highlight в соответствии с вашими бизнес-требованиями и нажмите **Подтвердить**, чтобы завершить конфигурацию.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/ecaebc8fc5ba11f0a62b5254007c27c5.png)

## Отвязывание шаблона Smart Highlight

1. Перейдите в [Управление доменами](https://console.tencentcloud.com/live/domainmanage). Нажмите на **Имя домена**, который требуется настроить, или **Управление**, чтобы перейти на страницу деталей домена.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/dd967c6dc5b711f0a7ca5254001c06ec.png)

2. Выберите вкладку **Конфигурация шаблона** и нажмите **Редактировать** в правом верхнем углу раздела **Конфигурация Smart Highlight**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9e6766f9c5ba11f0a62b5254007c27c5.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/06c24c54c5bb11f0a62b5254007c27c5.png)

3. В зависимости от ваших бизнес-требований снимите флажок с соответствующего шаблона и нажмите **Подтвердить** для продолжения.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/15775d62c5bb11f085c7525400454e06.png)

> **Примечание:** Отвязывание шаблона Smart Highlight не влияет на текущие прямые трансляции.


---
*Источник: [https://www.tencentcloud.com/document/product/267/74573](https://www.tencentcloud.com/document/product/267/74573)*

---
*Источник (EN): [smart-highlight-configuration.md](./smart-highlight-configuration.md)*
