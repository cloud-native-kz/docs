# Компонент Barrage

В этом руководстве рассказывается об интеграции **Chat Component**, который включает **Message List Component (BarrageList)** и **Message Input Component (BarrageInput)**. Вы можете быстро добавить наши предварительно созданные компоненты, используя примеры ниже, или полностью настроить их стили и макет, следуя разделу настройки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1052e4dc117011f18bc5525400074c32.png)

## Структура компонента

| **Название компонента** | **Описание** |
| --- | --- |
| **Barrage Message Component (BarrageList)** | Обрабатывает отображение сообщений чата в реальном времени и управление ими, включая **отображение сообщений, группировку по времени, взаимодействие с пользователями и адаптивные макеты**. |
| **Message Input Component (BarrageInput)** | Предоставляет возможности редактирования богатого текста и отправки сообщений, включая **средство выбора эмодзи, ограничение количества символов, управление состоянием и кроссплатформенную поддержку** для беспрепятственного обмена сообщениями. |

## Интеграция компонента

### Шаг 1: Предварительные требования

Перед интеграцией компонента обратитесь к [Руководству подготовки](https://www.tencentcloud.com/document/product/647/77813) для настройки вашей среды и активации необходимых сервисов.

### Шаг 2: Установка зависимостей

npm

pnpm

yarn

```
npm install tuikit-atomicx-react @tencentcloud/uikit-base-component-react --savenpm install sass --save-dev
```

```
pnpm add tuikit-atomicx-react @tencentcloud/uikit-base-component-reactpnpm add sass --dev
```

```
yarn add tuikit-atomicx-react @tencentcloud/uikit-base-component-reactyarn add sass --dev
```

### Шаг 3: Интеграция компонента Barrage

Импортируйте и используйте **компонент живого баража** в вашем проекте. Вы можете напрямую скопировать следующий пример кода в свой проект для отображения полного **компонента сообщений баража** и **компонента ввода сообщений** в прямой трансляции.

MessageList.tsx

MessageList.module.scss

```
import React from "react";import { useUIKit } from "@tencentcloud/uikit-base-component-react";import { BarrageList, BarrageInput } from "tuikit-atomicx-react";import styles from "./MessageList.module.scss";const MessageList: React.FC = () => {  const { t } = useUIKit();    return (    <div className={styles.livePlayer__messageList}>      <div className={styles.livePlayer__messageListTitle}>        <span>{t('live_player_view.message_list_title')}</span>      </div>      <div className={styles.livePlayer__messageListContent}>        <BarrageList />        <BarrageInput />      </div>    </div>  );};export default MessageList;
```

```
.livePlayer__messageList {  display: flex;  flex-direction: column;  flex: 1 0 auto;  margin-top: 8px;  padding: 8px;  background: var(--uikit-bg-color-operate);  .livePlayer__messageListTitle {    padding: 12px 0;    border-bottom: 1px solid var(--uikit-stroke-color-primary);    @include text-size-16;  }  .livePlayer__messageListContent {    display: flex;    flex: 1;    flex-direction: column;  }}
```

## 

## Настройка

Компонент сообщений баража и компонент ввода сообщений предоставляют богатые атрибуты Props для настройки функциональности и отображения пользовательского интерфейса.

### Barrage Message Component (BarrageList)

| **Props** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| Message | Component |  IBarrageMessageComponentProps | Пользовательский рендеринг компонента сообщения. |
| containerStyle | CSSProperties | - | Пользовательский стиль контейнера списка сообщений. |
| itemStyle | CSSProperties | - | Пользовательский стиль одного элемента сообщения. |
| height | String | - | Высота компонента, поддерживает единицы CSS. |
| style | CSSProperties | - | Пользовательский стиль корневого элемента. |
| className | String | - | Пользовательское имя класса CSS, установленное на корневом узле DOM компонента. |

### Message Input Component (BarrageInput)

| **Название Props** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| containerClass | String | '' | Пользовательское имя класса CSS контейнера. |
| containerStyle | CSSProperties | {} | Пользовательский встроенный стиль контейнера. |
| width | String | - | Ширина компонента, поддерживает единицы CSS. |
| height | String | - | Высота компонента, поддерживает единицы CSS. |
| minHeight | String | '40px' | Минимальная высота компонента, поддерживает единицы CSS. |
| maxHeight | String | '140px' | Максимальная высота компонента, поддерживает единицы CSS. |
| placeholder | String | - | Текст-подсказка поля ввода. |
| disabled | Boolean | false | Отключить ли поле ввода. |
| autoFocus | Boolean | true | Автоматически ли фокусировать поле ввода. |
| maxLength | Number | 80 | Максимальное ограничение количества символов для содержимого ввода. |
| onFocus | () => void | - | Обработчик события фокуса поля ввода. |
| onBlur | () => void | - | Обработчик события потери фокуса поля ввода. |

#### Примеры

**Настройка стилей и размеров**

```
// Message List<BarrageList  className="custom-barrage-list-name"  style={{backgroundColor: "#FFFFFF"}}  containerStyle={{backgroundColor: "#999999"}}  itemStyle={{backgroundColor: "#000000"}}  height="200px" />// Message Input<BarrageInput   className="custom-barrage-input-name"  autoFocus  disabled={false}  width="100%"  height="100px"  placeholder="Enter barrage message"  />
```

**Пользовательское сообщение**

```
import React from 'react';import { BarrageList } from 'tuikit-atomicx-react';import type { Barrage } from 'tuikit-atomicx-react';interface ICustomMessageComponentProps {  message: Barrage;  isLastInChunk?: boolean;  style?: React.CSSProperties;}const CustomMessage: React.FC<ICustomMessageComponentProps> = ({ message }) => {  return (    <div className="my-message-item">      {message.sender.userName}: {message.textContent}    </div>  );};// Use custom message component in the message list<BarrageList  Message={CustomMessage}/>
```

## Следующие шаги

После интеграции компонента чата вы можете добавить дополнительные функции, такие как **отправка подарков** и **списки зрителей**. Ознакомьтесь с руководствами ниже, чтобы продолжить создание вашего опыта прямой трансляции.

| **Функция** | **Описание** | **Руководство интеграции** |
| --- | --- | --- |
| **Live Gift Component** | Отображает каталог подарков, поддерживает отправку подарков и анимацию подарков. | [Live Gift Component (Web React)](https://www.tencentcloud.com/document/product/647/77819) |
| **Audience List Component** | Отображает текущих зрителей в комнате прямой трансляции. | [Audience List Component (Web React)](https://www.tencentcloud.com/document/product/647/77812) |


---
*Источник: [https://trtc.io/document/77817](https://trtc.io/document/77817)*

---
*Источник (EN): [barrage-component.md](./barrage-component.md)*
