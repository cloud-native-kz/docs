# TUICallKit

## API TUICallKit

`TUICallKit` — это компонент аудио/видео звонков, который **включает элементы пользовательского интерфейса**. Вы можете использовать его API для быстрой реализации приложения аудио/видео звонков, похожего на WeChat. Инструкции по интеграции см. в разделе [Интеграция TUICallKit](https://www.tencentcloud.com/document/product/647/54896).

## Обзор API

| API | Описание |
| --- | --- |
| [login](#login) | Вход в систему |
| [logout](#logout) | Выход из системы |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54906#setSelfInfo) | Устанавливает никнейм пользователя и фото профиля. |
| [calls](https://www.tencentcloud.com/document/product/647/54906#calls) | Начать звонок. |
| [join](https://www.tencentcloud.com/document/product/647/54906#join) | Присоединиться к звонку. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/54906#enableMuteMode) | Устанавливает, включать ли режим отключения звука. |
| [enableFloatWindow](https://www.tencentcloud.com/document/product/647/54906#enableFloatWindow) | Устанавливает, включать ли плавающие окна. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/54906#setCallingBell) | Пользовательский рингтон. |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/54906#enableVirtualBackground) | Включить/выключить функцию виртуального фона |

## Подробности

### login

```
Future<TUIResult> login(int sdkAppId, String userId, String userSig)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| sdkAppId | int | SDKAppID пользователя |
| userId | String | ID пользователя, строковый тип, может содержать только буквы английского алфавита (a-z и A-Z), цифры (0-9), дефисы (-) и подчеркивания (_). |
| userSig | String | Подпись пользователя. UserSig получается путем шифрования информации, такой как sdkAppId и userId, с использованием SDKSecretKey ([Метод расчета подписи](https://www.tencentcloud.com/document/product/647/35166)). Она служит в качестве билета для аутентификации, позволяя Tencent Cloud определить, авторизован ли текущий пользователь на использование услуг TRTC. |
| возвращаемое значение | [TUIResult](https://www.tencentcloud.com/document/product/647/54909#TUIResult) | Содержит информацию о коде и сообщении: код пуст ("") означает, что вызов успешен; код не пуст ("") означает, что вызов не удался, см. сообщение для причины ошибки |

### logout

```
Future<void> logout()
```

### setSelfInfo

Этот API используется для установки псевдонима и фото профиля. Псевдоним не может превышать 500 байт, а фото профиля указывается URL-адресом.

```
Future<TUIResult> setSelfInfo(String nickname, String avatar)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| nickName | String | Никнейм. |
| avatar | String | Фото профиля. |
| возвращаемое значение | [TUIResult](https://www.tencentcloud.com/document/product/647/54909#TUIResult) | Содержит информацию о коде и сообщении: код пуст ("") означает, что вызов успешен; код не пуст ("") означает, что вызов не удался, см. сообщение для причины ошибки |

### calls

Инициировать звонок. **Поддерживается в версии 2.9+.**

```
Future<TUIResult> calls(List<String> userIdList, TUICallMediaType mediaType, TUICallParams params)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | ID целевых пользователей. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип звонка, который может быть видео или аудио. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | **Опционально** Расширенные параметры звонка, такие как номер комнаты, время ожидания приглашения на звонок, офлайн-отправка пользовательского содержимого и т. д. |

### join

Активно присоединиться к звонку. **Поддерживается в версии 2.9+.**

```
Future<void> join(String callId)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный ID для этого звонка. |

### enableMuteMode

Этот API используется для установки того, включать ли режим отключения звука.

```
Future<void> enableMuteMode(bool enable)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| enable | bool | Включить и выключить отключение звука; true означает включить отключение звука |

### enableFloatWindow

Этот API используется для установки того, включать ли плавающие окна. Значение по умолчанию — `false`, кнопка плавающего окна в верхнем левом углу представления вызова скрыта. Если установить значение `true`, кнопка станет видимой.

```
Future<void> enableFloatWindow(bool enable)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| enable | bool | Значение по умолчанию — false, кнопка плавающего окна в верхнем левом углу представления вызова скрыта. Если установить значение true, кнопка станет видимой. |

### setCallingBell

Пользовательский рингтон.

```
Future<void> setCallingBell(String assetName)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| assetName | String | Путь к файлу рингтона. Файл рингтона должен быть добавлен в ресурсы assets основного проекта. |

### enableVirtualBackground

Включить/выключить функцию виртуального фона. После включения функции виртуального фона на UI можно отобразить кнопку функции размытого фона. Нажатие кнопки напрямую включит функцию размытого фона.

```
Future<void> enableVirtualBackground(bool enable)
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| enable | bool | Включить, выключить отключение звука; true означает, что отключение звука включено |

## Устаревшие интерфейсы

### call

Этот API используется для выполнения (одноранговых) звонков.

> **Примечание:** Этот интерфейс устарел в версии 2.9+. Рекомендуется использовать интерфейс calls вместо него.

```
Future<void> call(String userId, TUICallMediaType callMediaType, [TUICallParams? params])
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | `Тип звонка, который может быть видео или аудио.` |

### groupCall

Этот API используется для выполнения группового звонка.

> **Примечание:** Этот интерфейс устарел в версии 2.9+. Рекомендуется использовать интерфейс calls вместо него.

```
Future<void> groupCall(String groupId, List<String> userIdList, TUICallMediaType callMediaType,[TUICallParams? params])
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | List<String> | ID целевых пользователей. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | `Тип звонка, который может быть видео или аудио.` |

### joinInGroupCall

Этот API используется для присоединения к групповому звонку. Перед выполнением группового звонка необходимо сначала создать IM группу.

> **Примечание:** Этот интерфейс устарел в версии 2.9+. Рекомендуется использовать интерфейс join вместо него.

```
Future<void> joinInGroupCall(TUIRoomId roomId, String groupId, TUICallMediaType callMediaType)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomID](https://www.tencentcloud.com/document/product/647/54909#TUIRoomId) | ID комнаты. |
| groupId | String | ID группы. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | `Тип звонка, который может быть видео или аудио.` |


---
*Источник: [https://trtc.io/document/54906](https://trtc.io/document/54906)*

---
*Источник (EN): [tuicallkit.md](./tuicallkit.md)*
