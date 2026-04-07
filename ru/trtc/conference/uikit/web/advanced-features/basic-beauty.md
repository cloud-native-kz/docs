# Основная красота

TUIRoomKit представляет функцию базовой красоты, которая позволяет пользователям оптимизировать эффекты шлифовки, отбеливания и румянца при проведении многопользовательских конференций, улучшая визуальный опыт видеоконференций и добавляя им интерес. В этой статье подробно описано, как использовать эту функцию в компонентах TUIRoomKit.

## Эффекты интеграции

После интеграции функции базовой красоты в компонент TUIRoomKit отображение выглядит следующим образом:

| **Отключить**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/14aa8e517c7811ef82535254002693fd.png) | **Сглаживание**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5b998c627c7811efb9d8525400f69702.png) |
| --- | --- |
| **Отбеливание**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/91ae28f97c7811efa87e52540055f650.png) | **Румянец**![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9f5d03ce7c7811ef852f52540075b605.png) |

## Условия подготовки

Перед использованием функций базовой красоты, предоставляемых Tencent Cloud, необходимо перейти в консоль и включить услугу многопользовательской конференции для приложения. Конкретные шаги см. в разделе [Включение услуги](https://www.tencentcloud.com/document/product/647/59973#da1ae48d-e664-4486-bb5c-ed5aa89a8180).

## Включение базовой красоты

> **Примечание:** **В настоящее время H5 не поддерживается, только для Web PC. Требуется TUIRoomKit v2.6.2 и выше.**

Схема UI TUIRoomKit поддерживает установку базовой красоты по умолчанию. Если вам не нужно показывать функцию базовой красоты, вы можете скрыть UI базовой красоты следующим кодом:

Vue3

Vue2

```
import { conference, FeatureButton } from '@tencentcloud/roomkit-web-vue3';conference.hideFeatureButton(FeatureButton.BasicBeauty);
```

```
import { conference, FeatureButton } from '@tencentcloud/roomkit-web-vue2.7';conference.hideFeatureButton(FeatureButton.BasicBeauty);
```

## Часто задаваемые вопросы

### Нет отклика или задержка при включении базовой красоты?

При плохом качестве сети файл модели базовой красоты может не загрузиться, что может привести к невозможности открыть базовую красоту.

### Можно ли отключить камеру и при этом включить базовую красоту?

Нельзя.


---
*Источник: [https://trtc.io/document/64689](https://trtc.io/document/64689)*

---
*Источник (EN): [basic-beauty.md](./basic-beauty.md)*
