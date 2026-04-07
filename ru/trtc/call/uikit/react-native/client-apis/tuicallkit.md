# TUICallKit

## TUICallKit API

TUICallKit API — это **интерфейс с включённым пользовательским интерфейсом** для компонента аудио- и видеовызова. Используя API TUICallKit, вы можете быстро реализовать сценарий аудио- и видеовызова, похожий на WeChat, через простые интерфейсы. Для получения более подробных инструкций по интеграции см. раздел Быстрый доступ к TUICallKit.

## API TUICallKit

| API | Описание |
| --- | --- |
| [login](https://www.tencentcloud.com/document/product/647/66842#93b6b48b-6ced-41f6-9efe-3c99ac82a7cc) | Вход в систему. |
| [logout](https://www.tencentcloud.com/document/product/647/66842#34205667-e433-4e42-80fb-ca9d0fc256c7) | Выход из системы. |
| [calls](https://www.tencentcloud.com/document/product/647/66842#184a66f0-1280-4575-89a1-409f4f64aa3b) | Инициировать один-на-один или многопользовательский вызов. |
| [call](https://www.tencentcloud.com/document/product/647/66842#call_param) | Для выполнения один-на-один вызова, поддерживает пользовательский ID комнаты, тайм-аут вызова, содержимое автономной отправки и многое другое. |
| [groupCall](https://www.tencentcloud.com/document/product/647/66842#groupcall) | Для выполнения группового вызова, поддерживает пользовательский ID комнаты, тайм-аут вызова, содержимое автономной отправки и многое другое. |
| [joinInGroupCall](https://www.tencentcloud.com/document/product/647/66842#joiningroupcall) | Присоединиться к групповому вызову. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/66842#93d9981e-20e0-4619-b01b-ae0b9edc85a5) | Пользовательский рингтон. |
| [setSelfInfo](#1e1b351d-802a-45ec-ae9f-0a06bc1a1187) | Установить аватар и ник пользователя. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/66842#f437b400-a478-4446-a060-ae2283af3a38) | Установить, включить ли режим отключения звука. |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/66842#48143cfb-18bc-4b06-b4bc-6fd8214f15d4) | Включить/отключить рингтон. |
| [setScreenOrientation](https://www.tencentcloud.com/document/product/647/66842#1f6205a6-9ef8-42aa-9143-697476ad4478) | Установить ориентацию экрана. |
| [on](https://www.tencentcloud.com/document/product/647/66842#41ad2909-fce1-4b6e-8a0c-2a4a982bc6ae) | Прослушивать события TUICallKit |
| [off](https://www.tencentcloud.com/document/product/647/66842#ce43fcef-252e-4ab2-bd0e-175fc4847b54) | Отменить прослушивание событий TUICallKit |

## Подробное описание API

### login

Вход в систему. Этот шаг критически важен. Только после успешного входа вы сможете нормально использовать различные функции, предоставляемые TUICallKit.

```
TUICallKit.login(  {    sdkAppId: 0,    userId: '',    userSig: '',  },  (res) => {    console.log('login success');  },   (errCode, errMsg) => {     console.log('login error');   });
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| sdkAppId | Number | Уникальный идентификатор SDKAppID для приложения аудио- и видеосвязи, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| userId | String | Пользователи определяют собственный ID пользователя на основе своего бизнеса. Может содержать только буквы (a-z, A-Z), цифры (0-9), подчёркивания и дефисы. |
| userSig | String | SDKSecretKey для приложения аудио- и видеосвязи, созданного в [консоли Tencent RTC](https://console.trtc.io/). |

### logout

Выход из системы. После выхода из системы события TUICallKit не будут прослушиваться.

```
TUICallKit.login(  (res) => {    console.log('login success', res);  },   (errCode, errMsg) => {     console.log('login error', errCode, errMsg);   });
```

### calls

Инициировать один-на-один или многопользовательский вызов.

```
TUICallKit.calls(  {    userIdList: userIDList,    mediaType: MediaType.Audio,    callParams: {      offlinePushInfo: {        title: '',        desc: '',      },    },  },  () => {    console.log('calls success');  },  () => {    console.log('calls error');  });
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| userIdList | Array<String> | ID целевых пользователей. |
| mediaType | [MediaType](https://www.tencentcloud.com/document/product/647/66840#fb7a5c31-59f7-421a-a743-a08ac55305d8) | Тип носителя для вызова, например видеовызов, голосовой вызов. MediaType.Audio: голосовой вызов. MediaType.Video: видеовызов. |
| callParams | [callParams](https://www.tencentcloud.com/document/product/647/66840#7c505b92-4c45-43cd-a254-cbce7809a746) | параметры расширения вызова включают номер комнаты, тайм-аут приглашения на вызов, пользовательское содержимое автономной отправки и т. д. |

### call

Выполнить телефонный вызов (вызов 1 на 1), поддерживает пользовательский номер комнаты, тайм-аут приглашения на вызов, содержимое автономной отправки и многое другое.

```
TUICallKit.call(  {    userId: calleeID,    mediaType: MediaType.Audio,    callParams: {      offlinePushInfo: {        title: '',        desc: '',      },    },  },  () => {    console.log('call success');  },  () => {    console.log('call error');  });
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | userId целевого пользователя |
| mediaType | [MediaType](https://www.tencentcloud.com/document/product/647/66840#fb7a5c31-59f7-421a-a743-a08ac55305d8) | Тип носителя для вызова, например видеовызов, голосовой вызов. MediaType.Audio: голосовой вызов. MediaType.Video: видеовызов. |
| callParams | [callParams](https://www.tencentcloud.com/document/product/647/66840#7c505b92-4c45-43cd-a254-cbce7809a746) | параметры расширения вызова включают номер комнаты, тайм-аут приглашения на вызов, пользовательское содержимое автономной отправки и т. д. |

### groupCall

Инициировать групповую коммуникацию.

```
TUICallKit.groupCall(  {    userIdList: userIDList,    mediaType: MediaType.Audio,    groupId: '',  },  (res) => {    console.log('groupCall success', res);  },  (errCode, errMsg) => {    console.log('groupCall error', errCode, errMsg);  });
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | Array<String> | ID целевых пользователей. |
| mediaType | [MediaType](https://www.tencentcloud.com/document/product/647/66840#fb7a5c31-59f7-421a-a743-a08ac55305d8) | Тип носителя для вызова, например видеовызов, голосовой вызов. MediaType.Audio: голосовой вызов. MediaType.Video: видеовызов. |
| callParams | [callParams](https://www.tencentcloud.com/document/product/647/66840#7c505b92-4c45-43cd-a254-cbce7809a746) | параметры расширения вызова, например номер комнаты, тайм-аут приглашения на вызов, пользовательское содержимое автономной отправки и т. д. |

### joinInGroupCall

Присоединиться к существующему аудио-видео вызову в группе.

```
TUICallKit.joinInGroupCall(  {    roomId: '',    groupId: '',    mediaType: '',  });
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | [RoomId](https://www.tencentcloud.com/document/product/647/66840#280a991e-d6a9-4194-9c98-ab703173227f) | ID аудио-видео комнаты для этого вызова |
| groupId | String | ID группы, связанной с этим групповым вызовом |
| mediaType | [MediaType](https://www.tencentcloud.com/document/product/647/66840#fb7a5c31-59f7-421a-a743-a08ac55305d8) | Тип носителя для вызова, например видеовызов, голосовой вызов |

### setCallingBell

Установить пользовательский рингтон входящего вызова.

- Ввод ограничен адресом локального файла в формате MP3. Необходимо убедиться, что приложение имеет доступ к этому каталогу файлов.
- Используйте метод import для импорта файла рингтона.
- Чтобы сбросить рингтон, передайте пустую строку для `filePath`.

```
var filePath: string = '';TUICallKit.setCallingBell(filePath);
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| filePath | String | Адрес файла рингтона |

### setSelfInfo

Этот API используется для установки псевдонима и фотографии профиля. Псевдоним не может превышать 500 байт, а фотография профиля задаётся URL-адресом.

```
 var nickname: string = 'user'; var avatar: string = ''; TUICallKit.setSelfInfo(nickname, userAvatar,  (res) => {    console.log('groupCall success', res);  },  (errCode, errMsg) => {    console.log('groupCall error', errCode, errMsg);  } );
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| nickname | string | Имена целевых пользователей. |
| avatar | string | Аватар целевого пользователя. |

### enableMuteMode

Включить/отключить рингтон. После включения рингтон не будет воспроизводиться при получении запроса вызова.

```
Boolean enable = trueTUICallKit.enableMuteMode(enable);
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| enable | Boolean | Включить/отключить рингтон. По умолчанию false. |

### enableVirtualBackground

Включить/отключить функцию размытого фона. Вызвав интерфейс, вы можете отобразить кнопку функции размытого фона в пользовательском интерфейсе и нажать кнопку, чтобы напрямую включить функцию размытого фона.

```
Boolean enable = trueTUICallKit.enableVirtualBackground(enable);
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| enable | Boolean | enable = true Показать кнопку размытого фона. enable = false Не показывать кнопку размытого фона. |

### setScreenOrientation

Установить режим отображения экрана.

```
Number orientation = 0TUICallKit.setScreenOrientation(orientation);
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| orientation | Number | orientation = 0 : Портретное отображение. orientation = 1 : Альбомное отображение. orientation = 2 : Автоматически выбрать лучший режим отображения на основе текущего состояния устройства. |

### on

Вы можете прослушивать события TUICallKit, используя примерный код ниже. Для получения подробной информации о событиях см. раздел [TUICallEvent](https://www.tencentcloud.com/document/product/647/66841#tuicallevent-api-.E7.AE.80.E4.BB.8B).

```
TUICallKit.on(TUICallEvent.onCallReceived, (res: any) => {  console.log('onUserReject userId=' + res.userId);});
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| type | String | Для событий, которые вы прослушиваете с помощью TUICallKit, см. список событий в [TUICallEvent](https://www.tencentcloud.com/document/product/647/66841#tuicallevent-api-.E7.AE.80.E4.BB.8B). |
| params | Any | Информация, передаваемая событием, см. подробности в [TUICallEvent](https://www.tencentcloud.com/document/product/647/66841#tuicallevent-api-.E7.AE.80.E4.BB.8B). |

### off

Вы можете использовать следующий примерный код, чтобы отменить прослушивание событий TUICallKit.

```
TUICallKit.off(TUICallEvent.onCallReceived);
```


---
*Источник: [https://trtc.io/document/66842](https://trtc.io/document/66842)*

---
*Источник (EN): [tuicallkit.md](./tuicallkit.md)*
