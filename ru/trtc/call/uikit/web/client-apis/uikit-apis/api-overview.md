# Обзор API

## TUICallKit (включает компоненты UI)

TUICallKit — это компонент для аудио и видеозвонков, который **включает компонент UI**. С помощью этого компонента вы можете быстро реализовать сценарий аудио и видеозвонков наподобие WhatsApp.

| API | Описание |
| --- | --- |
| [init](https://www.tencentcloud.com/document/product/647/51015#init) | Инициализация TUICallKit. |
| [calls](https://www.tencentcloud.com/document/product/647/51015#calls) | Инициировать один-к-одному или многопользовательский вызов. |
| [join](https://www.tencentcloud.com/document/product/647/51015#join) | Активно присоединиться к вызову. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/51015#setCallingBell) | Настроить пользовательский рингтон. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51015#setSelfInfo) | Установить собственное имя пользователя и аватар. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/51015#enableMuteMode) | Включить/отключить рингтон. |
| [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51015#enableFloatWindow) | Включить/отключить функцию плавающего окна. |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/51015#enableVirtualBackground) | Включить/отключить кнопку функции размытия фона. |
| [setLanguage](https://www.tencentcloud.com/document/product/647/51015#setLanguage) | Установить язык вызова для компонента TUICallKit. |
| [hideFeatureButton](https://www.tencentcloud.com/document/product/647/51015#hideFeatureButton) | Скрытая кнопка. |
| [setLocalViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setLocalViewBackgroundImage) | Установить изображение фона для интерфейса вызова локального пользователя. |
| [setRemoteViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setRemoteViewBackgroundImage) | Установить изображение фона для интерфейса вызова удаленного пользователя. |
| [setLayoutMode](https://www.tencentcloud.com/document/product/647/51015#setLayoutMode) | Установить режим компоновки интерфейса вызова. |
| [setCameraDefaultState](https://www.tencentcloud.com/document/product/647/51015#setCameraDefaultState) | Установить, открывается ли камера по умолчанию. |
| [destroyed](https://www.tencentcloud.com/document/product/647/51015#destroyed) | Уничтожить TUICallKit. |
| [getTUICallEngineInstance](https://www.tencentcloud.com/document/product/647/51015#getTUICallEngineInstance) | Получить экземпляр TUICallEngine. |

## TUICallEngine (без UI)

API TUICallEngine — это компонент для аудио и видеозвонков, который **предоставляет интерфейс без UI**. Вы можете использовать этот набор API для пользовательской инкапсуляции в соответствии с вашими бизнес-потребностями.

| API | Описание |
| --- | --- |
| [createInstance](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#.createInstance) | Создание экземпляра TUICallEngine (паттерн Singleton) |
| [destroyInstance](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#destroyInstance) | Завершение экземпляра TUICallEngine (паттерн Singleton) |
| [on](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#on) | Прослушивание событий |
| [off](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#off) | Отмена прослушивания события |
| [login](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#login) | Интерфейс входа |
| [logout](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#logout) | Интерфейс выхода |
| [setSelfInfo](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#setSelfInfo) | Настроить имя пользователя и фотографию профиля |
| [calls](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#calls) | Инициировать один-к-одному вызов |
| [join](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#join) | Активно присоединиться к вызову. |
| [accept](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#accept) | Ответить на вызов |
| [reject](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#reject) | Отклонить вызов |
| [hangup](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#hangup) | Завершить вызов |
| [startRemoteView](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#startRemoteView) | Инициировать удаленный рендеринг экрана |
| [stopRemoteView](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#stopRemoteView) | Остановить удаленный рендеринг экрана |
| [openCamera](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#openCamera) | Включить камеру |
| [closeCamera](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#closeCamera) | Выключить камеру |
| [switchCamera](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#switchCamera) | Переключение между передней и задней камерами, примечание: поддерживается только на мобильных устройствах. |
| [openMicrophone](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#openMicrophone) | Включить микрофон |
| [closeMicrophone](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#closeMicrophone) | Выключить микрофон |
| [setVideoQuality](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#setVideoQuality) | Установить качество видео |
| [getDeviceList](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#getDeviceList) | Получить список устройств |
| [switchDevice](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#switchDevice) | Переключение устройств камеры или микрофона |
| [enableMultiDeviceAbility](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#enableMultiDeviceAbility) | Включить/отключить режим входа с несколькими устройствами в TUICallEngine. |
| [setBlurBackground](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#setBlurBackground) | Переключить/установить размытие фона |
| [setVirtualBackground](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/TUICallEngine.html#setVirtualBackground) | Переключить/установить размытие фона изображения |

## Типы событий

TUICallEvent — это класс события обратного вызова, соответствующий TUICallEngine. Через этот обратный вызов вы можете прослушивать события обратного вызова, представляющие интерес.

| СОБЫТИЕ | Описание |
| --- | --- |
| [TUICallEvent.ERROR](https://www.tencentcloud.com/document/product/647/51017#error) | Во время вызова произошла ошибка. |
| [TUICallEvent.KICKED_OUT](https://www.tencentcloud.com/document/product/647/51017#kicked_out) | Получение этого события после дублирования входа указывает, что пользователь был удален из комнаты |
| [TUICallEvent.USER_ACCEPT](https://www.tencentcloud.com/document/product/647/51017#user_accept) | Если пользователь ответит, это событие будет получено.**v4.x.x устарело** |
| [TUICallEvent.USER_ENTER](https://www.tencentcloud.com/document/product/647/51017#user_enter) | Пользователь присоединился к вызову. |
| [TUICallEvent.USER_LEAVE](https://www.tencentcloud.com/document/product/647/51017#user_leave) | Пользователь покинул вызов. |
| [TUICallEvent.REJECT](https://www.tencentcloud.com/document/product/647/51017#reject) | Пользователь отклонил вызов. |
| [TUICallEvent.NO_RESP](https://www.tencentcloud.com/document/product/647/51017#no_resp) | Пользователь не ответил. |
| [TUICallEvent.LINE_BUSY](https://www.tencentcloud.com/document/product/647/51017#line_busy) | Пользователь был занят. |
| [TUICallEvent.USER_VIDEO_AVAILABLE](https://www.tencentcloud.com/document/product/647/51017#user_video_available) | Есть ли у пользователя видеопоток. |
| [TUICallEvent.USER_AUDIO_AVAILABLE](https://www.tencentcloud.com/document/product/647/51017#user_audio_available) | Есть ли у пользователя аудиопоток. |
| [TUICallEvent.USER_VOICE_VOLUME](https://www.tencentcloud.com/document/product/647/51017#user_voice_volume) | Уровни громкости всех пользователей. |
| [TUICallEvent.ON_CALL_BEGIN](https://www.tencentcloud.com/document/product/647/51017#oncallbegin) | Событие подключения вызова |
| [TUICallEvent.ON_CALL_RECEIVED](https://www.tencentcloud.com/document/product/647/51017#on_call_received) | Событие запроса вызова |
| [TUICallEvent.ON_CALL_CONNECTED](https://www.tencentcloud.com/document/product/647/51017#on_call_canceled) | Событие отсутствия подключения вызова |
| [TUICallEvent.ON_CALL_END](#calling_end) | Вызов завершен. |
| [TUICallEvent.DEVICED_UPDATED](https://www.tencentcloud.com/document/product/647/51017#deviced_updated) | Обновление списка устройств, это событие будет получено |
| [TUICallEvent.ON_USER_NETWORK_QUALITY_CHANGED](https://www.tencentcloud.com/document/product/647/51017#on_user_network_quality_changed) | События качества сети всех пользователей |

## Ссылки на документацию

- [TUICallEngine](https://www.tencentcloud.com/document/product/647/51016)
- [TUICallEvent](https://www.tencentcloud.com/document/product/647/51017)


---
*Источник: [https://trtc.io/document/51014](https://trtc.io/document/51014)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*
