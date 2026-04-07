# Просмотр аудитории

В этом руководстве описано, как интегрировать страницу просмотра аудитории, позволяющую пользователям смотреть прямую трансляцию хоста, присоединяться в качестве сооведущего, просматривать детали живой комнаты, проверять онлайн-аудиторию, отправлять подарки, ставить лайки трансляциям и взаимодействовать через живые комментарии.

## Предпросмотр функций

Страница просмотра аудитории включает поведение и стили по умолчанию из коробки. Если эти значения по умолчанию не полностью соответствуют вашим требованиям, вы можете настроить пользовательский интерфейс в соответствии с вашими потребностями.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8a8d9605eaeb11f09965525400370dda.png)

## Быстрая интеграция

### Шаг 1: Активирование сервиса

Обратитесь к документации [Активирование сервиса](https://www.tencentcloud.com/document/product/647/60033), чтобы включить **пробную версию** или активировать пакет **Pro Edition**.

### Шаг 2: Интеграция кода

См. [Подготовка](https://www.tencentcloud.com/document/product/647/77112) для получения инструкций по интеграции TUILiveKit.

Убедитесь, что ваш проект включает react-native-safe-area-context. Если нет, установите его с помощью:

```
yarn add react-native-safe-area-context
```

### Шаг 3: Добавление страницы просмотра аудитории

`react-native-tuikit-live` предоставляет полный пользовательский интерфейс со стороны аудитории и бизнес-логику для прямой трансляции. Чтобы отобразить страницу просмотра аудитории, настройте точку входа для вызова `LiveAudiencePage` на основе вашей бизнес-логики, а затем выполните следующие шаги для навигации на страницу просмотра аудитории:

> **Примечание:** В этом примере используется `useState` для простого переключения страниц. Для производственных приложений рекомендуется использовать библиотеки навигации, такие как React Navigation, для управления страницами. Чтобы понять, как интегрировать библиотеки навигации, обратитесь к [официальной документации React Navigation](https://reactnavigation.org/).

```
/** * Простой пример навигации - управление переходами между страницами с помощью useState */import React, { useState } from 'react';import { View, Button, StyleSheet } from 'react-native';import { SafeAreaProvider } from 'react-native-safe-area-context';import { LiveAudiencePage } from 'react-native-tuikit-live';import { useLiveListState } from 'react-native-tuikit-atomic-x';type PageType = 'home' | 'liveAudience' | 'liveEnd';function MyApp() {  // В реальных сценариях liveID обычно получается из:  // 1. Параметров при входе в прямую трансляцию из списка трансляций  // 2. Параметров маршрута  // 3. Ответа API сервера  // Здесь '1234' используется в качестве примера  const liveID = '1234'  const { joinLive } = useLiveListState(liveID)  const [currentPage, setCurrentPage] = useState<PageType>('home');  const [endedLiveID, setEndedLiveID] = useState<string>('');  // Навигация на страницу просмотра аудитории  const handleJumpLiveAudience = async () => {    await joinLive({      liveID,      onSuccess: () => {        setCurrentPage('liveAudience');      },      onError: (error) => {        console.error('Failed to join live room:', error);        // Обработать ошибку, например, уведомить пользователя      }    })  };  // Возврат со страницы просмотра аудитории  const handleBackFromAudience = () => {    setCurrentPage('home');  };  // Завершить прямую трансляцию  const handleEndLive = (liveID?: string) => {    setEndedLiveID(liveID || '');    setCurrentPage('liveEnd');  };  return (    <SafeAreaProvider>      {currentPage === 'home' && (        <View style={styles.container}>          <Button title="Enter Audience View" onPress={handleJumpLiveAudience} />        </View>      )}      {currentPage === 'liveAudience' && (        <LiveAudiencePage          onBack={handleBackFromAudience}          onEndLive={handleEndLive}        />      )}      {currentPage === 'liveEnd' && (        <View style={styles.container}>          <Button title="Return to Home" onPress={() => setCurrentPage('home')} />        </View>      )}    </SafeAreaProvider>  );}const styles = StyleSheet.create({  container: {    flex: 1,    justifyContent: 'center',    alignItems: 'center',  },});export default MyApp;
```

## Настройка макета пользовательского интерфейса

`TUILiveKit` поддерживает обширную настройку страницы просмотра аудитории, поэтому вы можете адаптировать функции и стили в соответствии с требованиями вашего бизнеса.

### Настройка значков

Все значки, используемые `TUILiveKit`, находятся в каталоге `tuikit-atomic-x/src/static/images`. Ниже приведены некоторые примеры. Чтобы обновить значок, просто замените соответствующий файл в этом каталоге.

| **Путь значка** | **Описание** |
| --- | --- |
| /static/images/dashboard.png | Значок «Панель управления» в нижней панели действий |
| /static/images/link-guest.png | Значок «Подать заявку на сооведущего» в нижней панели действий |
| /static/images/live-gift.png | Значок «Подарок» в нижней панели действий |
| /static/images/live-like.png | Значок «Лайк» в нижней панели действий |
| /static/images/close.png | Значок «Покинуть живую комнату» в верхней панели действий |

После обновления значков пересоберите и запустите приложение, чтобы увидеть изменения.

### Настройка текстов

Весь текст пользовательского интерфейса в TUILiveKit управляется централизованно. Чтобы обновить любой текст, отредактируйте соответствующие json-файлы в каталоге `tuikit-atomic-x/src/locales/`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/afd77cedeaeb11f09d62525400ecee81.png)

- `zh.json` - текст на китайском языке
- `en.json` - текст на английском языке

После редактирования пересоберите и запустите приложение, чтобы применить обновления.

### Добавление кнопки

Чтобы добавить кнопку **Лайк** в верхний левый угол видеоплощади, отредактируйте `live/src/pages/LiveAudience/index.tsx` и вставьте следующий код:

```
<View style={{ flex: 1 }}>  {/* ...другое содержимое... */}    <View     style={{      position: 'absolute',      top: 100,      left: 15,      width: 100,      height: 30,      backgroundColor: 'rgba(0, 0, 0, 0.3)',      borderRadius: 22.5,      flexDirection: 'row',      justifyContent: 'center',      alignItems: 'center',    }}  >      {/* Замените адрес изображения на ваши ресурсы */}    <Image      style={{ width: 18, height: 18 }}      source={require('/static/images/gift_heart0.png')}      resizeMode="contain"    />    <Text style={{ color: '#fff', fontSize: 12 }}>8888</Text>  </View></View>
```

Результат:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/27c3b51eea2811f0885152540097cba1.png)

### Скрытие кнопки

Чтобы скрыть кнопку, закомментируйте соответствующий блок кода. Следующий код показывает, как скрыть кнопку **Подарок**:

```
{/* <TouchableOpacity    style={styles.actionBtn}    onPress={showGiftPicker}    activeOpacity={0.7}>    <Image      source={require('react-native-tuikit-atomic-x/src/static/images/live-gift.png')}      style={styles.actionBtnIcon}      resizeMode="contain"    />    </TouchableOpacity> */}
```

## Следующие шаги

Вы интегрировали функцию просмотра аудитории. Далее вы можете добавить такие функции, как **Запуск трансляции хостом** и **Список трансляций**. Дополнительные сведения см. в таблице ниже:

| **Функция** | **Описание** | **Руководство по интеграции** |
| --- | --- | --- |
| **Запуск трансляции хостом** | Полный рабочий процесс для запуска трансляции хостом, включая подготовку перед трансляцией и взаимодействие после трансляции | [Запуск трансляции хостом](https://www.tencentcloud.com/document/product/647/77116) |
| **Список трансляций** | Отображает интерфейс списка трансляций и функции, включая список и детали комнаты | [Список трансляций](https://www.tencentcloud.com/document/product/647/77118) |

## Часто задаваемые вопросы

## Живые комментарии, отправленные другими членами аудитории, не видны?

- Причина 1: Проверьте подключение к сети, чтобы убедиться, что устройство аудитории подключено к сети.
- Причина 2: Аудитория была отключена хостом и не может отправлять живые комментарии.
- Причина 3: Живой комментарий содержит заблокированные ключевые слова. Убедитесь, что комментарий соответствует правилам живой комнаты.

### Как отобразить уровни аудитории?

Если вам нужно показать уровни аудитории, вставьте соответствующий элемент в нужное место. Например, чтобы отобразить уровни аудитории в списке аудитории, найдите код отображения информации об аудитории в компоненте `tuikit-atomic-x/src/components/LiveAudienceList.tsx` и добавьте код отображения уровня аудитории:

```
<View style={styles.audienceInfo}>    .......   {/* Уровень аудитории */}   <Text style={styles.audienceLevel}>{level}</Text>    <View style={styles.audienceAvatarContainer}>        <Image source={{ uri: avatarURL }} style={styles.audienceAvatar} />    </View></View>
```


---
*Источник: [https://trtc.io/document/77117](https://trtc.io/document/77117)*

---
*Источник (EN): [audience-watching.md](./audience-watching.md)*
