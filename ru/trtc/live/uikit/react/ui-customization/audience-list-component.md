# Компонент списка аудитории

Это руководство показывает, как интегрировать **компонент списка аудитории (LiveAudienceList)** в вашу приложение. Вы можете быстро добавить наш готовый компонент, используя приведенные ниже примеры, или полностью настроить его стили и макет, следуя разделу кастомизации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/05202123117011f18bc5525400074c32.png)

## Основные возможности

| **Категория функции** | **Конкретные возможности** |
| --- | --- |
| **Отображение аудитории в реальном времени** | Отображает текущий список зрителей в прямой трансляции в реальном времени, показывая аватары и никнеймы. Это дает ведущим четкое представление о том, кто смотрит, и помогает им понять состав своей аудитории. |
| **Адаптивный дизайн** | Включает отдельные макеты пользовательского интерфейса для настольных и мобильных устройств. Компонент автоматически адаптируется к различным размерам экрана, обеспечивая согласованный опыт на всех платформах. |
| **Настраиваемый пользовательский интерфейс** | Предлагает гибкие механизмы слотов для настройки значков аудитории, стилей аватаров и других элементов пользовательского интерфейса. Адаптируйте список аудитории в соответствии с требованиями вашего бренда и дизайна. |

## Интеграция компонента

### Шаг 1: Предварительные требования

Перед быстрой интеграцией обратитесь к [Подготовке](https://www.tencentcloud.com/document/product/647/77813), чтобы соответствовать соответствующей конфигурации среды и активировать соответствующие услуги.

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

### Шаг 3: Интеграция компонента списка аудитории

Импортируйте и используйте **компонент списка аудитории** в вашем проекте. Скопируйте следующий пример кода, чтобы отобразить список аудитории прямой трансляции.

AudienceList.tsx

AudienceList.module.scss

```
import React from "react";import { useUIKit } from "@tencentcloud/uikit-base-component-react";import { useLiveAudienceState, LiveAudienceList } from "tuikit-atomicx-react";import styles from "./AudienceList.module.scss";const AudienceList: React.FC = () => {  const { t } = useUIKit();  const { audienceCount } = useLiveAudienceState();  return (    <div className={styles.livePlayer__audienceList}>      <div className={styles.livePlayer__audienceListTitle}>        <span>{t('live_player_view.audience_list_title')} </span>        <span className={styles.livePlayer__audienceCount}>({audienceCount})</span>      </div>      <div className={styles.livePlayer__audienceListContent}>        <LiveAudienceList height="100%" />      </div>    </div>  );};export default AudienceList;
```

```
.livePlayer__audienceList {  display: flex;  flex-direction: column;  flex-shrink: 0;  height: 30%;  padding: 8px;  background: var(--uikit-bg-color-operate);  .livePlayer__audienceListTitle {    padding: 12px 0;    border-bottom: 1px solid var(--uikit-stroke-color-primary);    @include text-size-16;  }  .livePlayer__audienceCount {    font-weight: 400;    color: var(--uikit-text-color-secondary);  }  .livePlayer__audienceListContent {    flex: 1;    overflow: hidden;  }}
```

## Кастомизация компонента

### Свойства компонента

#### Свойства LiveAudienceList

| **Свойство** | **Тип** | **Значение по умолчанию** | **Требуется** | **Описание** |
| --- | --- | --- | --- | --- |
| children | (params: { audience: AudienceInfo; }) => React.ReactNode | - | Нет | Пользовательский рендерер значка аудитории (например, значки роли, маркеры идентификации). Отображается между аватаром и никнеймом |
| className | String | - | Нет | Пользовательское имя класса CSS |
| style | CSSProperties | - | Нет | Пользовательский стиль CSS |
| height | String | - | Нет | Высота списка аудитории |

#### Тип данных AudienceInfo

| **Свойство** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| userId | String | - | ID аудитории |
| userName | String | - | Имя аудитории (никнейм) |
| avatarUrl | String | - | URL аватара аудитории |
| userRole | Number | 2 | Роль аудитории0: Владелец прямой трансляции1: Администратор прямой трансляции2: Обычная аудитория |
| isMessageDisabled | Boolean | false | Отключено ли отправка текстовых сообщений и эмодзи |
| joinedTimestamp | Number | 0 | Время присоединения аудитории к прямой трансляции |
| customInfo | Record<String, any> | - | Пользовательские свойства пользователя |

### Пример: пользовательские значки аудитории

```
import { LiveAudienceList } from 'tuikit-atomicx-react';import type { AudienceInfo } from 'tuikit-atomicx-react';// Пользовательские свойства компонента, должны совпадать с дочерними свойствами компонента LiveAudienceListinterface CustomAudienceProps {  params: {audience: AudienceInfo} }// Пользовательский компонент пользователя, отобразить роль пользователяconst CustomAudience: React.FC<CustomAudienceProps> = ({ params }) => {  return (    <div className="custom-audience-item">      {        params.audience.userRole === 2 ? "[Audience]" : (params.audience.userRole === 1 ? "[Admin]" : "[Host]")      }    </div>  );};const LivePlayer: React.FC<LivePlayerProps> = ({ className }) => {  return (    <div className={`${styles.livePlayer} ${className || ''}`}>          <div className={styles.livePlayer__audienceListContent}>            {/* Установите свойства height, className, style */}            <LiveAudienceList height="100%" className="my-class-name" style={{backgroundColor: "transparent"}}>              {(params) => <CustomAudience params={params} />} {/* Используйте пользовательский компонент на странице проигрывателя список аудитории для отображения роли пользователя */}            </LiveAudienceList>          </div>    </div>  );};
```

## Следующие шаги

После интеграции компонента списка аудитории вы можете добавить дополнительные функции, такие как **отправка подарков при прямой трансляции** и **сообщения чата**. Ознакомьтесь с приведенными ниже руководствами, чтобы продолжить создание вашего опыта прямой трансляции.

| **Функция** | **Описание** | **Руководство интеграции** |
| --- | --- | --- |
| **Компонент подарков при прямой трансляции** | Отображает каталог подарков, поддерживает отправку подарков и анимации подарков. | [Компонент подарков при прямой трансляции (Web React)](https://www.tencentcloud.com/document/product/647/77819) |
| **Компонент чата с завесой** | Поддерживает отправку, получение и отображение текстовых сообщений и эмодзи. | [Компонент чата с завесой (Web React)](https://www.tencentcloud.com/document/product/647/77817) |


---
*Источник: [https://trtc.io/document/77812](https://trtc.io/document/77812)*

---
*Источник (EN): [audience-list-component.md](./audience-list-component.md)*
