# Настройка шифрования DRM

CSS предлагает возможности шифрования DRM на основе Widevine, FairPlay и NormalAES, помогающие защитить ваш контент и предотвратить пиратство и hotlinking. Этот документ показывает, как настроить шифрование DRM в консоли CSS.

## Важные сведения

Tencent Cloud только шифрует ваш контент. Лицензии DRM предоставляются сторонними сервисами лицензирования SDMC и DRMtoday, которые взимают плату за лицензирование. Для получения дополнительной информации, пожалуйста, свяжитесь с компаниями.

## Предварительные требования

- Вы активировали CSS и добавили [доменное имя для воспроизведения](https://intl.cloud.tencent.com/document/product/267/35970).
- Вы создали аккаунт на [SDMC DRM](https://india-drm-console.sdmc.tv/setting/drm/index) или [DRMtoday](https://castlabs.com/free-trials/drmtoday/) и настроили ключ доступа.

## Параметры консоли

### Настройка информации ключа DRM

1. Войдите в консоль CSS и выберите **Feature Configuration** > [DRM management](https://console.tencentcloud.com/live/config/drm) на левой боковой панели.
2. Нажмите **Edit** справа, чтобы перейти на страницу настройки управления DRM.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/8ebde0af595111ef9bf1525400a9236a.png)

3. Заполните **информацию о секретном ключе** и выберите поставщика управления сертификатами. Вы можете выбрать SDMC или DRMtoday. Конкретная конфигурация выглядит следующим образом:
  - Если поставщик услуг лицензирования **SDMC**:

Введите ваш SDMC UID, Secret ID и Secret key (информацию необходимо получить у SDMC).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9c9eb1c4595111ef81cf525400d5f8ef.png)

  - Если поставщик услуг лицензирования **DRMtoday**:

Введите ваши DRMtoday `Merchantname`, `MerchantUUID`, `MerchantAPIName`, `MerchantAPIPassword`, `KeySeedID` и IVSeedID (информацию необходимо получить у DRMtoday).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/a4dfa8b6595111ef8f105254002693fd.png)

### Настройка шаблонов трансляции

1. Войдите в консоль CSS и перейдите в **Feature Configuration** > [Live Transcoding](https://console.tencentcloud.com/live/config/transcode).
2. Нажмите **Create Transcoding Template** для входа на страницу настройки трансляции. Нажмите ![](https://staticintl.cloudcachetci.com/cms/backend-cms/cb3224e7595011ef9bf1525400a9236a.png) для включения шифрования DRM. Установите информацию шифрования DRM.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/fc9dbbcd85f611ef852f52540075b605.png)

| Элемент конфигурации | Требуется | Описание |
| --- | --- | --- |
| DRM encryption | Нет | Следует ли включить шифрование DRM. По умолчанию отключено. Перед включением этой функции необходимо настроить информацию о ключе DRM в "DRM management". |
| Type | Да | Widevine, FairPlay или NormalAES. Для шифрования FairPlay необходимо загрузить сертификат, полученный от Apple, в ваш плеер. Подробнее см. в разделе [Obtaining a FairPlay certificate](https://www.tencentcloud.com/document/product/267/48069). |

  2.1. Вы можете переключаться между разными вкладками для просмотра требований конфигурации шифрования DRM для стандартной трансляции, трансляции с кодеком высокой скорости и трансляции только аудио.

Standard Transcoding

Top Speed Codec Transcoding

Audio-only Transcoding

![](https://staticintl.cloudcachetci.com/cms/backend-cms/2dff6b6e429611efb438525400f69702.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/ed13acd1429511ef98fd52540075b605.png)

![](https://staticintl.cloudcachetci.com/cms/backend-cms/34414a32429611ef98fd52540075b605.png)

3. После завершения конфигурации нажмите **Save**.

### Привязка доменных имен

1. Войдите в консоль CSS и перейдите в **Feature Configuration** > [Live Transcoding](https://console.tencentcloud.com/live/config/transcode).
2. Откройте окно привязки доменного имени одним из следующих способов:
  - **Прямая привязка доменного имени**: нажмите **Bind Domain Name** в верхнем левом углу.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/41691270c51b11f0a62b5254007c27c5.png)

  - **После успешного создания нового шаблона трансляции, привязка доменного имени**: [После успешной настройки шаблона трансляции](https://www.tencentcloud.com/document/product/267/48068#creating-a-transcoding-template-and-binding-a-domain) нажмите **Bind Domain Name** в диалоговом окне подсказки.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/fadd9a9dc51a11f085c7525400454e06.png)

3. В окне привязки доменного имени выберите **шаблон трансляции** и **доменное имя для воспроизведения** (можно одновременно привязать несколько доменных имен для воспроизведения), которые вы хотите привязать, и нажмите **Confirm** для завершения.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/1aac61c3c51b11f085c7525400454e06.png)

### Получение URL-адреса воспроизведения с шифрованием DRM

Только воспроизведение HLS поддерживает шифрование DRM. Используйте [Address Generator](https://console.tencentcloud.com/live/addrgenerator/addrgenerator) для создания URL-адресов воспроизведения (выберите созданный шаблон). Созданный URL-адрес HLS шифруется с помощью DRM.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/81d9762085f711ef80ff525400d5f8ef.png)

### Настройка вашего плеера

- Он должен быть оснащен [SDMC](https://india-drm-sso.sdmc.tv/applyAccount) возможностью получения и расшифровки информации о лицензии из видеоданных.
- Используйте шифрование FairPlay для плееров iOS и Widevine или NormalAES для плееров Android.
- На iOS вам необходимо запросить сертификат и загрузить его в [консоль SDMC](https://india-drm-console.sdmc.tv/licenses/drm/index).

> **Примечание:** вам нужно сначала создать аккаунт, чтобы получить доступ к консоли SDMC. Подробные инструкции по созданию аккаунта SDMC см. в разделе [Obtaining the UID and Key Information](https://www.tencentcloud.com/document/product/267/48070). Если у вас возникнут проблемы, пожалуйста, [отправьте запрос в поддержку](https://console.tencentcloud.com/workorder/category). Мы поможем вам пройти через этот процесс.


---
*Источник: [https://www.tencentcloud.com/document/product/267/48068](https://www.tencentcloud.com/document/product/267/48068)*

---
*Источник (EN): [configuring-drm-encryption.md](./configuring-drm-encryption.md)*
