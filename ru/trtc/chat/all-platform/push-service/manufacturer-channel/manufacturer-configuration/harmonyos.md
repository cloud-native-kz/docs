# HarmonyOS

## Конфигурация консоли HarmonyOS

### Шаг 1: Включение службы Push

1. Войдите в [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/), выберите **Develop and Services** на главной странице, выберите соответствующий проект и нажмите **Enable Now**, чтобы включить службу push.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71d736927da011f0bd33525400454e06.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71a3dcad7da011f09e56525400e889b2.png)

2. В параметрах проекта найдите "Push" на вкладке управления API и включите службу push.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71a076e27da011f09cab525400bf7822.png)

### Шаг 2: Заявка на сертификат и подпись

1. **Заявка на сертификат: вы должны подать заявку на отладочный сертификат на этапе отладки и на финальный сертификат на этапе выпуска.**
  - Войдите в [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html), выберите **Certificates, APP ID and Profile**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71d723177da011f09cab525400bf7822.png)

  - Выберите **Certificates, APP ID and Profile** в левой боковой панели, выберите **Certificate**, затем нажмите **Add Certificate** на странице **Certificate**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/719505147da011f0bd33525400454e06.png)

  - В появившемся окне "Add Certificate" заполните информацию о полученном сертификате и нажмите **Submit**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/716db6f57da011f09e56525400e889b2.png)

> **Примечание:** файл запроса сертификата (CSR) должен быть получен в DevEco Studio. Дополнительные сведения см. в разделе [generate certificate request file](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section462703710326).

  - После успешной подачи заявки на странице **certificate management** отображается имя сертификата и другая информация. Нажмите **Download**, чтобы сохранить созданный сертификат в локальный каталог для последующего использования при отладке подписей.
2. **Регистрация отладочного устройства (требуется только на этапе отладки)**
  - Войдите в [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html), выберите **Certificates, APP ID and Profile**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71f9487f7da011f0914f52540099c741.png)

  - Выберите **Certificates, APP ID and Profile** в левой боковой панели, выберите **Device**, затем перейдите на страницу **Device**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71a15a167da011f09cab525400bf7822.png)

  - Чтобы добавить одно устройство, нажмите **Add Device** в верхнем правом углу, заполните информацию об устройстве во всплывающем окне, а затем нажмите **Submit** по завершении.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71ddeff47da011f09e56525400e889b2.png)

> **Примечание:** чтобы узнать, как получить UDID для различных типов устройств, см. [UDID Retrieval Method](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-device-0000001946142249#section67331926102911).

3. **Заявка на файл профиля: вы должны подать заявку на отладочный файл профиля на этапе отладки и на финальный файл профиля на этапе выпуска.**
  - Войдите в [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html), выберите **Certificates, APP ID and Profile**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71e7d2d37da011f09a9a5254001c06ec.png)

  - Выберите **Profile** в левой боковой панели, затем нажмите **Add**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71928bcb7da011f0bda35254007c27c5.png)

  - На странице **Add Profile** введите имя приложения, имя профиля и другую необходимую информацию, затем нажмите **Add** после заполнения всей информации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71a8d9637da011f09cab525400bf7822.png)

4. **Ручная подпись.**

Настройте файл SecretKey (.p12), полученный отладочный сертификат (.cer) и отладочный файл Profile (.p7b) в DevEco Studio. В окне **File > Project Structure > Project > Signing Configs** снимите флажок "Automatically generate signature" (если это приложение HarmonyOS, установите флажок "**Support HarmonyOS**"), затем настройте информацию о подписи проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71e9d4d77da011f0960452540044a08e.png)

### Шаг 3: Создание учетных данных сертификата консоли IM

1. Войдите в [API Console](https://gitee.com/link?target=https%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fconsole%2Foverview), нажмите **My APIs** на левой боковой панели страницы. Убедитесь, что служба push доступна под именем проекта. Если нет, нажмите **Apply for new HMS API service** справа.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71a3bcd17da011f080fb5254005ef0f7.png)

2. Нажмите **API service** > **Credential** на левой боковой панели, затем нажмите **Create credential** под **Service account key**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71a38a137da011f09cab525400bf7822.png)

3. Заполните необходимые поля и нажмите **Create public/private key**. Создайте и загрузите JSON файл. Загруженный файл — это именно ваш файл учетных данных Service Account.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71fa61cf7da011f0960452540044a08e.png)

4. Сохраните загруженный файл для использования в конфигурации консоли IM.

### Шаг 4: Заявка на права и преимущества на основе сценариев

Push Kit поддерживает различные типы сообщений на основе сценариев. Некоторые типы сообщений на основе сценариев требуют, чтобы вы подали заявку на специальные права и преимущества для нормальной отправки, такие как типы сценариев сообщений Chat.

Войдите в [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html), выберите **Develop and Services**, нажмите **Push Service**, и на странице **Configuration** нажмите, чтобы подать заявку на преимущества самостоятельной классификации. Следуйте подсказкам для подачи заявки и активации. Дополнительные сведения см. в разделе [Push Scenario-Based Message Benefits](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-apply-right).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71d2dc0a7da011f0960452540044a08e.png)

## Конфигурация консоли Chat

1. Войдите в [Chat Console](https://console.qcloud.com/avc), перейдите на страницу [Chat > Push > Access Settings](https://console.trtc.io/chat/push-plugin-push-identifier) и нажмите Add Certificate, чтобы создать сертификат.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71dea8527da011f09a9a5254001c06ec.png)

2. Выберите учетные данные сертификата, созданные в [процедуре 3](#step3) выше, и загрузите их в новый добавленный сертификат HarmonyOS.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71d0f5317da011f09a9a5254001c06ec.png)

3. Нажмите на последующие действия
  - Open app: нажмите сообщение в строке уведомлений, чтобы по умолчанию открыть домашнюю страницу приложения.
  - Open specified in-app page: после получения push-сообщения нажмите в строке уведомлений. Компонент осуществит Webhook этого события клика и сквозную передачу автономного сообщения.
4. После добавления сертификата консоль IM выделит вам ID сертификата для доступа и использования.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71e1394e7da011f0960452540044a08e.png)


---
*Источник: [https://trtc.io/document/72237](https://trtc.io/document/72237)*

---
*Источник (EN): [harmonyos.md](./harmonyos.md)*
