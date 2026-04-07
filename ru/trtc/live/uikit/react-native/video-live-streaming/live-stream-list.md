# Список прямых трансляций

В этом руководстве показано, как быстро интегрировать страницу списка прямых трансляций, что позволит пользователям просматривать доступные прямые трансляции и предпросмотр сведений о прямой комнате.

## Предпросмотр функций

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/32729347eaee11f09d62525400ecee81.png)

## Быстрая интеграция

### Шаг 1. Активируйте сервис

Обратитесь к документу [Активировать сервис](https://www.tencentcloud.com/document/product/647/60033), чтобы включить **пробную версию** или активировать пакет **Pro Edition**.

### Шаг 2. Интеграция кода

См. раздел [Подготовка](https://www.tencentcloud.com/document/product/647/77112) для получения инструкций по интеграции TUILiveKit.

Убедитесь, что установлен `react-native-safe-area-context`. Если он отсутствует, установите его с помощью:

```
yarn add react-native-safe-area-context
```

### Шаг 3. Добавьте страницу списка прямых трансляций

TUILiveKit предоставляет готовый к использованию интерфейс и бизнес-логику для списка прямых трансляций в сценариях живого потокового вещания. Просто настройте точку входа для вызова LiveListPage в соответствии с вашей бизнес-логикой, а затем выполните следующие шаги для навигации на страницу списка прямых трансляций.

> **Примечание:** В этом примере используется `useState` для демонстрации простого переключения страниц. Для производственных приложений рекомендуется использовать библиотеки навигации, такие как React Navigation, для управления страницами. Чтобы понять, как интегрировать библиотеки навигации, обратитесь к [официальной документации React Navigation](https://reactnavigation.org/).

```
/** * Simple navigation example - using useState to manage page transitions */import React, { useState } from 'react';import { View, Button, StyleSheet } from 'react-native';import { SafeAreaProvider } from 'react-native-safe-area-context';import { LiveListPage } from 'react-native-tuikit-live';type PageType = 'home' | 'liveList' | 'liveEnd' | 'liveAudience';function MyApp() {  const [currentPage, setCurrentPage] = useState<PageType>('home');  // Navigate to the Live Stream List page  const handleJumpLiveList = async () => {    setCurrentPage('liveList');  };  // Return from the Live Stream List page  const handleBackFromLiveList = () => {    setCurrentPage('home');  };  return (    <SafeAreaProvider>      {currentPage === 'home' && (        <View style={styles.container}>          <Button title="Go to Live Stream List" onPress={handleJumpLiveList} />        </View>      )}      {currentPage === 'liveList' && (        <LiveListPage          onBack={handleBackFromLiveList}        />      )}      {currentPage === 'liveEnd' && (        <View style={styles.container}>          <Button title="Back to Home" onPress={() => setCurrentPage('home')} />        </View>      )}    </SafeAreaProvider>  );}const styles = StyleSheet.create({  container: {    flex: 1,    justifyContent: 'center',    alignItems: 'center',  },});export default MyApp;
```

## Настройка макета интерфейса

`TUILiveKit` поддерживает гибкую настройку функций и внешнего вида страницы списка прямых трансляций, позволяя адаптировать макет в соответствии с требованиями вашего бизнеса.

### Отрегулируйте количество прямых комнат на строку

Вы можете установить количество прямых комнат в каждой строке, изменив счет элементов в файле `tuikit-atomic-x/src/components/LiveList.tsx`. Конфигурация по умолчанию выглядит следующим образом:

```
const CARD_WIDTH = (SCREEN_WIDTH - CONTAINER_PADDING * 2 - CARD_GAP) / 2; // two per line// Group the live stream list with two elements per lineconst groupedLiveList = useMemo(() => {  const groups: LiveInfoParam[][] = [];  for (let i = 0; i < filteredLiveList.length; i += 2) {    groups.push(filteredLiveList.slice(i, i + 2));  }  return groups;}, [filteredLiveList]);
```

Чтобы показать одну прямую комнату на строку, обновите логику следующим образом:

```
const CARD_WIDTH = (SCREEN_WIDTH - CONTAINER_PADDING * 2); // one per lineconst groupedLiveList = useMemo(() => {  const groups: LiveInfoParam[][] = [];  for (let i = 0; i < filteredLiveList.length; i += 1) { // change 2 to 1    groups.push(filteredLiveList.slice(i, i + 1)); // change 2 to 1  }  return groups;}, [filteredLiveList]);
```

Результирующий интерфейс выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/686d5798eaef11f0bfd65254001d6acc.png)

## Далее

Вы успешно интегрировали функцию **Список прямых трансляций**. Чтобы продолжить, добавьте возможности **трансляции хоста** и **просмотра аудитории**. Подробнее см. в таблице ниже:

| **Функция** | **Описание** | **Руководство по интеграции** |
| --- | --- | --- |
| **Трансляция хоста** | Реализует полный рабочий процесс трансляции хоста, включая подготовку перед трансляцией и интерактивные функции после начала трансляции. | [Трансляция хоста](https://www.tencentcloud.com/document/product/647/77116) |
| **Просмотр аудитории** | Позволяет членам аудитории войти в прямую комнату хоста и смотреть трансляцию, поддерживая совместное ведение гостя, сведения о прямой комнате, список онлайн-аудитории и живые комментарии. | [Просмотр аудитории](https://www.tencentcloud.com/document/product/647/77117) |

## Часто задаваемые вопросы

### Почему страница списка прямых трансляций пуста после интеграции?

Если страница списка прямых трансляций пуста, убедитесь, что вы выполнили [шаги входа](https://www.tencentcloud.com/document/product/647/77112#6a6a267e-3585-43ae-a3a6-fd2e2e6930ba). Для тестирования используйте два устройства: запустите прямую трансляцию на одном устройстве в качестве хоста и используйте другое устройство для открытия страницы списка прямых трансляций и просмотра доступных прямых комнат.


---
*Источник: [https://trtc.io/document/77118](https://trtc.io/document/77118)*

---
*Источник (EN): [live-stream-list.md](./live-stream-list.md)*
