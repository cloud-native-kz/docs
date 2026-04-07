# Конфигурация невидимого водяного знака (цифровой водяной знак)

Функция невидимого водяного знака (цифрового водяного знака) отключена по умолчанию для прямых трансляций. В этом документе описано, как привязать/отвязать имя домена отправки к/от шаблона невидимого водяного знака (цифрового водяного знака) для включения/отключения функции невидимого водяного знака.

## Примечания

- Конфигурация шаблона вступит в силу примерно через 5–10 минут.
- После успешной привязки шаблона функция цифрового водяного знака будет включена для адресов отправки под указанным именем домена отправки.
- Одно имя домена может быть привязано только к одному шаблону цифрового водяного знака. После привязки все потоки под доменом будут помечены цифровым водяным знаком согласно этому шаблону.

## Предварительные требования

- Вы вошли в [консоль CSS](https://console.tencentcloud.com/live/livestat) и добавили [имя домена отправки](https://www.tencentcloud.com/document/product/267/35970).
- Вы создали [шаблон невидимого водяного знака](https://www.tencentcloud.com/document/product/267/74854#Watermark).

## Привязка шаблона невидимого водяного знака

1. Перейдите в [Domain Management](https://console.tencentcloud.com/live/domainmanage) и нажмите на **имя домена отправки**, который требуется настроить, или на **Manage**, чтобы перейти на страницу деталей домена.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/90348c36d0c411f093295254001c06ec.png)

2. Выберите **Template Configuration** и нажмите **Edit** в разделе **Invisible Watermark Configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/03f35254d1a611f08f8f525400454e06.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/8741fd89d1a611f09f555254007c27c5.png)

3. Выберите шаблон водяного знака и нажмите **Confirm**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/ff3d57e3d0c511f0a3b05254007c27c5.png)

## Отвязка шаблона невидимого водяного знака

1. Перейдите в [Domain Management](https://console.tencentcloud.com/live/domainmanage) и нажмите на **имя домена отправки**, который требуется настроить, или на **Manage**, чтобы перейти на страницу деталей домена.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/962e26bfd0c411f0800752540099c741.png)

2. Выберите **Template Configuration** и нажмите **Edit** в разделе **Invisible Watermark Configuration**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9af0f6f8d1a611f08206525400e889b2.png)

3. Очистите целевой шаблон и нажмите **Confirm**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/2b9ec05ad0c611f0b638525400e889b2.png)


---
*Источник: [https://www.tencentcloud.com/document/product/267/74855](https://www.tencentcloud.com/document/product/267/74855)*

---
*Источник (EN): [invisible-watermarkdigital-watermarkconfiguration.md](./invisible-watermarkdigital-watermarkconfiguration.md)*
