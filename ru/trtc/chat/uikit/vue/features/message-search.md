# Поиск сообщений

## **Внешний вид функции**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d848c7121cea11efbfc25254003441b1.png)

## ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d8fb4b0b1cea11ef8f53525400fa9af4.png)

## Интеграция с включённым интерфейсом

### Быстрая интеграция облачного поиска сообщений

Web&H5 Vue2&Vue3

Uniapp Vue2&Vue3

#### Шаг 1. Интегрируйте TUIKit

- Если **@tencentcloud/chat-uikit-vue ≥ 2.0.0** не интегрирован, следуйте [руководству по быстрой интеграции TUIKit для Vue2 и Vue3](https://trtc.io/document/58644?platform=web&product=chat).

#### Шаг 2. Активируйте плагин облачного поиска через консоль

> **Примечание:** Каждый плагин можно опробовать бесплатно в течение 7 дней один раз. После завершения пробного периода услуга будет отключена. Поэтому вам необходимо заранее приобрести плагин. Во время пробного периода можно искать только содержимое сообщений, созданных после включения функции облачного поиска; исторические сообщения недоступны для поиска. После приобретения плагина исторические сообщения будут автоматически синхронизированы и станут доступны для поиска.

#### Шаг 3. Найдите своё первое сообщение

После завершения [руководства по быстрой интеграции TUIKit для Vue2 и Vue3 — Шаг 6. Отправьте своё первое сообщение](https://trtc.io/document/58644?platform=web&product=chat#.E6.AD.A5.E9.AA.A47.EF.BC.9A.E5.8F.91.E9.80.81.E6.82.A8.E7.9A.84.E7.AC.AC.E4.B8.80.E6.9D.A1.E6.B6.88.E6.81.AF) найдите только что отправленное сообщение.

#### Шаг 1. Интегрируйте TUIKit

- Если **@tencentcloud/chat-uikit-uniapp ≥ 2.0.6** не интегрирован, следуйте [руководству по быстрой интеграции TUIKit для Uniapp](https://www.tencentcloud.com/zh/document/product/1047/58649).

#### Шаг 2. Активируйте плагин облачного поиска через консоль

> **Примечание:** Каждый плагин можно опробовать бесплатно в течение 7 дней один раз. После завершения пробного периода услуга будет отключена. Поэтому вам необходимо заранее приобрести плагин. Во время пробного периода можно искать только содержимое сообщений, созданных после включения функции облачного поиска; исторические сообщения недоступны для поиска. После приобретения плагина исторические сообщения будут автоматически синхронизированы и станут доступны для поиска.

#### Шаг 3. Найдите своё первое сообщение

После завершения [руководства по быстрой интеграции TUIKit для Uniapp — Шаг 6. Отправьте своё первое сообщение](https://www.tencentcloud.com/zh/document/product/1047/58649#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E8.BF.90.E8.A1.8C.E6.95.88.E6.9E.9C) найдите только что отправленное сообщение.

### **Независимое введение облачного поиска сообщений**

> **Примечание:** На шаге [Быстрая интеграция облачного поиска сообщений](https://trtc.io/document/60748?platform=web&product=chat#2d8e717e-68ad-437c-adf4-2c6938e51315) выше все функции облачного поиска сообщений введены по умолчанию, поэтому независимое введение не требуется. Если вы хотите независимо ввести <TUISearch> для облачного поиска сообщений, см. следующее руководство.

Web&H5 Vue2&Vue3

Uniapp Vue2&Vue3

#### Предварительные условия

- Если **@tencentcloud/chat-uikit-vue ≥ 2.0.0** не интегрирован, следуйте [руководству по быстрой интеграции TUIKit для Vue2 и Vue3](https://trtc.io/document/58644?platform=web&product=chat).

#### Введение **<TUISearch>**

На странице `.vue`, где вам нужна функция **облачного поиска сообщений**, введите **<TUISearch>**.

##### Описание параметров **<TUISearch>**

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| searchType | String | global: глобальный поиск (по умолчанию) |
|   |   | conversation: поиск в беседе |

##### Отображение эффекта **<TUISearch>**

| <TUISearch searchType="global" /> | <TUISearch searchType="conversation" /> |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d8658f691cea11efb2fd525400f57d1f.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d851abb11cea11ef8e50525400562f24.png) |

##### **Использование TUISearch**

```
import { TUISearch } from "@tencentcloud/chat-uikit-vue";// Глобальный поиск<TUISearch searchType="global" />// Поиск в беседе<TUISearch searchType="conversation" />
```

##### **Удаление введённого по умолчанию TUISearch**

TUIKit поставляется с интегрированным `<TUISearch>` по умолчанию. Если вы предпочитаете не использовать метод интеграции по умолчанию, вы можете закомментировать `<TUISearch>` в `TUIKit/index.vue`.

**Uniapp TUISearch поддерживает два метода интеграции: компонент и страница.**

#### Предварительные условия

- Если **@tencentcloud/chat-uikit-uniapp ≥ 2.0.6** не интегрирован, следуйте [руководству по быстрой интеграции TUIKit для Uniapp](https://www.tencentcloud.com/zh/document/product/1047/58649#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E8.BF.90.E8.A1.8C.E6.95.88.E6.9E.9C).

Введение на основе компонента

Введение на основе страницы

На странице `.vue`, где вам нужна функция **облачного поиска сообщений**, введите **<TUISearch>**.

##### Описание параметров **<TUISearch>**

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| searchType | String | global: глобальный поиск |
|   |   | conversation: поиск в беседе (по умолчанию) |

##### Отображение эффекта **<TUISearch>**

| <TUISearch searchType="global" /> | <TUISearch searchType="conversation" /> |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d9b8e4441cea11ef92fe525400dbceb9.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d8bffa261cea11efbfc25254003441b1.png) |

##### **Использование TUISearch**

```
// Ниже приведён только пример пути. Замените его на путь вашего проекта.import { TUISearch } from "/TUIKit/components/TUISearch/index.vue";// Глобальный поиск<TUISearch searchType="global" />// Поиск в беседе<TUISearch searchType="conversation" />
```

##### **Удаление введённого по умолчанию TUISearch**

TUIKit поставляется с интегрированным `<TUISearch>` по умолчанию. Если вы предпочитаете не использовать метод интеграции по умолчанию, вы можете закомментировать `<TUISearch>` в `TUIKit/components/TUIConversation/index.vue`.

##### **Добавление страницы TUISearch в pages.json**

```
{  "pages": [    ...,    {      "path": "TUIKit/components/TUISearch/index",      "style": {        "navigationBarTitleText": "Chat records"      }    }  ],  ...}
```

##### **Навигация на страницу TUISearch**

```
uni.navigateTo({   url: "/TUIKit/components/TUISearch/index",});
```

### **Продвинутое руководство**

#### **Добавление типов поиска сообщений**

| Исходный список типов глобального поиска сообщений | Список типов глобального поиска сообщений после добавления |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d8ed03431cea11efba53525400c60541.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d8fc84641cea11efb25c5254003359ae.png) |

Расположение директории: `src/TUIKit/components/TUISearch/search-type-list.ts`

`searchMessageTypeList` содержит все определения на вкладке типов поиска сообщений. Чтобы добавить типы поиска сообщений, не определённые в `searchMessageTypeList`, следуйте структуре ниже, чтобы добавить их в `searchMessageTypeList`:

```
[keyName: string]: {    key: string; // Задаёт ключ типа поиска сообщения, который должен быть уникальным.    label: string; // Задаёт метку для отображения типа поиска сообщения.    value: Array<string>; // Задаёт фактический список поиска для типа поиска сообщения. };  // Например, для поиска пользовательских сообщенийexport const searchMessageTypeList = {    ...    customMessage: {      key: "customMessage", // Задаёт ключ типа поиска сообщения, который должен быть уникальным.      label: "Custom", // Задаёт метку для отображения типа поиска сообщения.      value: [TUIChatEngine.TYPES.MSG_CUSTOM], // Задаёт фактический список поиска для типа поиска сообщения.    }};
```

Поскольку TUIKit использует i18next для интернационализации, если вы хотите добавить новую метку, добавьте соответствующие международные записи в `src/TUIKit/locales/zh_cn/TUISearch.ts` и `src/TUIKit/locales/en/TUISearch.ts` для перевода.

Чтобы добавить тип, определённый в `searchMessageTypeList`, к **списку типов глобального поиска сообщений** или **списку типов поиска сообщений в беседе**, вам просто нужно добавить его `key` к `globalSearchTypeKeys` или `conversationSearchTypeKeys`.

```
// Например, чтобы применить вновь определённый customMessage к списку типов глобального поиска сообщенийexport const globalSearchTypeKeys = [..., "customMessage"];// Например, чтобы применить вновь определённый customMessage к списку типов поиска сообщений в беседеexport const conversationSearchTypeKeys = [..., "customMessage"];
```

#### **Добавление диапазона времени для облачного поиска сообщений**

| Исходный список диапазонов времени глобального поиска | Список диапазонов времени глобального поиска после добавления |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d848f3331cea11efbfc25254003441b1.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d881fb011cea11efb25c5254003359ae.png) |

Расположение директории: `src/TUIKit/components/TUISearch/search-time-list.ts`

`searchMessageTimeList` содержит все определения на вкладке диапазона времени поиска. Чтобы добавить типы диапазонов времени поиска, не определённые в `searchMessageTimeList`, следуйте структуре ниже, чтобы добавить их в `searchMessageTimeList`:

```
[keyName: string]: {    key: string; // Задаёт ключ диапазона времени поиска сообщения, который должен быть уникальным.    label: string; // Задаёт метку для отображения диапазона времени поиска сообщения.    value: {       timePosition: number; // Задаёт начальную позицию для диапазона времени поиска сообщения. Значение по умолчанию — 0, что означает поиск с текущего времени.      timePeriod: number; // Задаёт диапазон времени для поиска в обратном направлении от timePosition.    };};  // Например, для поиска сообщений в диапазоне времени последних 2 днейexport const searchMessageTimeList = {   ...   twoDay: {      key: "twoDay", // Задаёт ключ диапазона времени поиска сообщения, который должен быть уникальным.      label: "Two days", // Задаёт метку для отображения диапазона времени поиска сообщения.      value: {        timePosition: 0, // Задаёт начальную позицию для диапазона времени поиска сообщения. Значение по умолчанию — 0, что означает поиск с текущего времени.        timePeriod: 2 * oneDay; // Задаёт диапазон времени для поиска в обратном направлении от timePosition.      },  },};
```

Поскольку TUIKit использует i18next для интернационализации, если вы хотите добавить новую метку, добавьте соответствующие международные записи в `src/TUIKit/locales/zh_cn/TUISearch.ts` и `src/TUIKit/locales/en/TUISearch.ts` для перевода.


---
*Источник: [https://trtc.io/document/60748](https://trtc.io/document/60748)*

---
*Источник (EN): [message-search.md](./message-search.md)*
