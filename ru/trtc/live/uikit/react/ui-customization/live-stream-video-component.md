# Компонент трансляции видео в прямом эфире

Данное руководство содержит подробное введение в **компонент Live Video (LiveView)**. Вы можете напрямую интегрировать готовый компонент в ваш существующий проект, используя примеры в этой статье, или глубоко настроить стили и макеты в соответствии с вашими потребностями, следуя разделу о настройке компонента в документации.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dda8efe7116f11f1a751525400380f7d.png)

## Основные возможности

| **Категория функций** | **Специальные возможности** |
| --- | --- |
| **Интеллектуальное переключение потоков** | LiveView может автоматически переключаться между типами потоков в зависимости от текущей роли пользователя (зритель или соведущий). Режим зрителя: компонент воспроизводит видеопотоки с минимальной задержкой, обеспечивая плавный просмотр для миллионов зрителей и значительно снижая затраты на полосу пропускания. Режим соведущего: компонент автоматически переключается на потоки звука/видео в реальном времени, обеспечивая задержку на уровне миллисекунд и гарантируя плавное взаимодействие между пользователями в режиме соведущего. |
| **Настраиваемый интерфейс** | Для удовлетворения различных бизнес-сценариев LiveView предоставляет пользовательские слоты UI компонента, позволяя полностью контролировать область видеопотока соведущих, переписывать отображение его UI и гибко определять аватар, ник, статус и другую информацию соведущих, легко создавая уникальный визуальный опыт, соответствующий стилю вашего бренда. |

## Интеграция компонента

### Шаг 1: Предварительные требования

Перед интеграцией необходимо обратиться к [Подготовка (Web React)](https://www.tencentcloud.com/document/product/647/77813) для активации сервиса и интеграции SDK.

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

### Шаг 3: Присоединение к комнате прямой трансляции

Импортируйте и используйте компонент **LiveView** в вашем проекте. Вы можете напрямую скопировать следующий пример кода в ваш проект, чтобы просматривать видео прямой трансляции соответствующей комнаты трансляции.

LivePlayer.tsx

LivePlayer.module.scss

```
import React, { useCallback, useEffect } from "react";import { MessageBox, Dialog, UIKitProvider } from "@tencentcloud/uikit-base-component-react";import TUIRoomEngine, { TUIRoomEvents } from "@tencentcloud/tuiroom-engine-js";import { LiveView, LiveListEvent, useLiveListState, useRoomEngine } from "tuikit-atomicx-react";import styles from "./LivePlayer.module.scss";interface LivePlayerProps {  className?: string;  liveId?: string;}const LivePlayer: React.FC<LivePlayerProps> = ({ className }) => {  const roomEngine = useRoomEngine();  const { currentLive, joinLive, subscribeEvent, unsubscribeEvent } = useLiveListState();  useEffect(() => {    if (!currentLive?.liveId) {      joinLive({ liveId: ''});   // Enter the live room ID you want to join, which can also be an external component parameter or URL parameter, etc.    }  }, [currentLive?.liveId, joinLive]);  const handleAutoPlayFailed = useCallback(() => {    MessageBox.alert({      content: 'Content is ready, click the [Play] button to start playback',      confirmText: 'Play',      showClose: false,      modal: false,    });  }, []);  const handleKickedOutOfLive = useCallback(() => {    Dialog.open({      content: 'You have been kicked out of the live room',      confirmText: 'Confirm',      className: styles.livePlayer__liveDialog,      showCancel: false,      showClose: false,      modal: true,      center: true,      onConfirm: () => {        Dialog.close();        // You can add your own business logic here, such as redirecting to the home page or live list page      },      onClose: () => {        // You can add your own business logic here, such as redirecting to the home page or live list page      },    });  }, []);  const handleLiveEnded = useCallback(() => {    Dialog.open({      content: 'The live has ended',      confirmText: 'Confirm',      className: styles.livePlayer__liveDialog,      showCancel: false,      showClose: false,      modal: true,      center: true,      onConfirm: () => {        Dialog.close();        // You can add your own business logic here, such as redirecting to the home page or live list page      },      onClose: () => {        // You can add your own business logic here, such as redirecting to the home page or live list page      },    });  }, []);  // Setup event listeners  useEffect(() => {    if (roomEngine.instance) {      roomEngine.instance.on(TUIRoomEvents.onAutoPlayFailed, handleAutoPlayFailed);    } else {      TUIRoomEngine.once("ready", () => {        roomEngine.instance?.on(TUIRoomEvents.onAutoPlayFailed, handleAutoPlayFailed);      });    }    subscribeEvent(LiveListEvent.ON_LIVE_ENDED, handleLiveEnded);    subscribeEvent(LiveListEvent.ON_KICKED_OUT_OF_LIVE, handleKickedOutOfLive);    return () => {      roomEngine.instance?.off(TUIRoomEvents.onAutoPlayFailed, handleAutoPlayFailed);      unsubscribeEvent(LiveListEvent.ON_LIVE_ENDED, handleLiveEnded);      unsubscribeEvent(LiveListEvent.ON_KICKED_OUT_OF_LIVE, handleKickedOutOfLive);    };  }, [handleAutoPlayFailed, handleLiveEnded, handleKickedOutOfLive, roomEngine.instance, subscribeEvent, unsubscribeEvent]);  return (    <UIKitProvider theme="dark">      <div className={`${styles.livePlayer} ${className || ''}`}>        <LiveView />      </div>    </UIKitProvider>  );};export default LivePlayer;
```

```
@mixin scrollbar {  &::-webkit-scrollbar {    width: 6px;    background: transparent;  }  &::-webkit-scrollbar-track {    background: transparent;  }  &::-webkit-scrollbar-thumb {    background: var(--uikit-color-gray-3);    border-radius: 3px;    border: 2px solid transparent;    background-clip: padding-box;    &:hover {      background: var(--uikit-color-gray-3);    }  }}.livePlayer {  display: flex;  width: 100%;  height: 100%;  border-radius: 8px;  overflow: hidden;  @include scrollbar;}.livePlayer__liveDialog {  text-align: center;}
```

## Следующие шаги

После интеграции компонента трансляции видео вам может потребоваться продолжить интеграцию функций, таких как **подарки в прямом эфире, список зрителей, чат с сообщениями**. Вы можете обратиться к документам руководства в таблице ниже, чтобы продолжить интеграцию этих функций.

| **Функция** | **Описание** | **Руководство по интеграции** |
| --- | --- | --- |
| **Компонент Live Gift** | Отображение настроенного списка подарков, поддержка отправки подарков и воспроизведения подарков. | [Компонент Live Gift (Web React)](https://www.tencentcloud.com/document/product/647/77819) |
| **Компонент списка зрителей** | Отображение информации о зрителях в текущей комнате прямой трансляции. | [Компонент списка зрителей (Web React)](https://www.tencentcloud.com/document/product/647/77812) |
| **Компонент чата с сообщениями** | Поддержка отправки, получения и отображения текстовых сообщений и эмодзи. | [Компонент чата с сообщениями (Web React)](https://www.tencentcloud.com/document/product/647/77817) |


---
*Источник: [https://trtc.io/document/77811](https://trtc.io/document/77811)*

---
*Источник (EN): [live-stream-video-component.md](./live-stream-video-component.md)*
