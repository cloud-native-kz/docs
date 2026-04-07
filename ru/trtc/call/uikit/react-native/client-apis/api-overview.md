# Обзор API

## TUICallKit (включая интерфейс UI)

## API-интерфейсы TUICallKit

UICallKit API позволяет быстро реализовать сценарий аудио- и видеозвонков, подобный WeChat, благодаря простым интерфейсам.

| API | Описание |
| --- | --- |
| [login](https://www.tencentcloud.com/document/product/647/66842#93b6b48b-6ced-41f6-9efe-3c99ac82a7cc) | Вход в систему. |
| [logout](https://www.tencentcloud.com/document/product/647/66842#34205667-e433-4e42-80fb-ca9d0fc256c7) | Выход из системы. |
| [calls](https://www.tencentcloud.com/document/product/647/66842#184a66f0-1280-4575-89a1-409f4f64aa3b) | Инициирование звонка один-на-один или многосторонего звонка. |
| [call](https://www.tencentcloud.com/document/product/647/66842#call_param) | Совершение звонка один-на-один, поддерживает пользовательский ID комнаты, тайм-аут вызова, содержание офлайн-уведомления и другое. |
| [groupCall](https://www.tencentcloud.com/document/product/647/66842#groupcall) | Совершение группового звонка, поддерживает пользовательский ID комнаты, тайм-аут вызова, содержание офлайн-уведомления и другое. |
| [joinInGroupCall](https://www.tencentcloud.com/document/product/647/66842#joiningroupcall) | Присоединение к групповому звонку. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/66842#93d9981e-20e0-4619-b01b-ae0b9edc85a5) | Настройка мелодии звонка пользователя. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/66842#f437b400-a478-4446-a060-ae2283af3a38) | Включение/отключение мелодии звонка. |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/66842#48143cfb-18bc-4b06-b4bc-6fd8214f15d4) | Включение/отключение функции размытого фона. |
| [setScreenOrientation](https://www.tencentcloud.com/document/product/647/66842#1f6205a6-9ef8-42aa-9143-697476ad4478) | Установка ориентации экрана. |
| [on](https://www.tencentcloud.com/document/product/647/66842#41ad2909-fce1-4b6e-8a0c-2a4a982bc6ae) | Прослушивание событий TUICallKit. |
| [off](https://www.tencentcloud.com/document/product/647/66842#ce43fcef-252e-4ab2-bd0e-175fc4847b54) | Отмена прослушивания событий TUICallKit. |

## TUICallEvent

TUICallEvent — это класс события обратного вызова, соответствующий TUICallKit. Благодаря этому обратному вызову вы можете прослушивать интересующие вас события обратного вызова.

| Событие | Описание |
| --- | --- |
| [TUICallEvent.onError](https://www.tencentcloud.com/document/product/647/66841#error) | Обратный вызов ошибки при звонке. |
| [TUICallEvent.onCallReceived](https://www.tencentcloud.com/document/product/647/66841#6b3c4385-acfb-478f-ad96-fe5310133b08) | Обратный вызов при получении запроса на звонок. |
| [TUICallEvent.onCallCancelled](https://www.tencentcloud.com/document/product/647/66841#06a7a696-ca1b-4b4e-ba01-ee9e2efeb732) | Обратный вызов при отмене звонка. |
| [TUICallEvent.onCallBegin](https://www.tencentcloud.com/document/product/647/66841#9918ea17-7900-4d01-9672-1f0e06f5e260) | Обратный вызов при подключении звонка. |
| [TUICallEvent.onCallEnd](https://www.tencentcloud.com/document/product/647/66841#0f575468-4d5e-4c27-9d6e-0ce85de0c77a) | Обратный вызов при завершении звонка. |
| [TUICallEvent.onUserReject](https://www.tencentcloud.com/document/product/647/66841#095f6da9-4668-4084-b44a-a2a59314d249) | Обратный вызов при отклонении пользователем звонка. |
| [TUICallEvent.onUserNoResponse](https://www.tencentcloud.com/document/product/647/66841#2586c3d6-3902-4948-b988-74789b5a4759) | Обратный вызов при отсутствии ответа пользователя. |
| [TUICallEvent.onUserLineBusy](https://www.tencentcloud.com/document/product/647/66841#fa1c55d7-48a2-4cd3-a38c-9e81f082e68e) | Обратный вызов при занятости линии пользователя. |
| [TUICallEvent.onUserJoin](https://www.tencentcloud.com/document/product/647/66841#7b551600-44c5-4683-90b7-25a3b243d12e) | Обратный вызов при присоединении пользователя к звонку. |
| [TUICallEvent.onUserLeave](https://www.tencentcloud.com/document/product/647/66841#fc8bb8d0-7665-4962-acc9-eea9bd1fe7db) | Пользователь покинул звонок. |
| [TUICallEvent.onCallMediaTypeChanged](https://www.tencentcloud.com/document/product/647/66841#31432c9e-4801-427f-b9de-64af29bb132d) | Обратный вызов при изменении типа медиа звонка. |
| [TUICallEvent.onKickedOffline](https://www.tencentcloud.com/document/product/647/66841#f690f3cf-5ce7-4322-9310-f5b099e97b0c) | Текущий пользователь отключен в офлайн-режиме. |
| [TUICallEvent.onUserSigExpired](https://www.tencentcloud.com/document/product/647/66841#b648078a-9d21-4b8e-bfe7-5d530d7af018) | Билет истек во время онлайн-сессии. |
| [TUICallEvent.onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/66841#b3e6f255-610d-405c-8b78-0619941be48d) | Наличие видеопотока у пользователя. |
| [TUICallEvent.onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/66841#3ca13720-a03e-4fb6-9fd0-de547be0ff4f) | Наличие аудиопотока у пользователя. |
| [TUICallEvent.onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/66841#e613c8b7-1114-4471-a8cd-54001c4ce2fb) | Уровни громкости всех пользователей. |
| [TUICallEvent.onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/66841#dc08307d-9fe7-4b95-9ca8-431730d1f60d) | Качество сети всех пользователей. |

## TUICallEngine (без UI)

`TUICallEngine` — это компонент аудио- и видеозвонков, который **не включает элементы пользовательского интерфейса**. Если `TUICallKit` не отвечает вашим требованиям, вы можете использовать API-интерфейсы `TUICallEngine` для настройки вашего проекта.

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/67600#b7284179-8663-4c7d-89a7-6f094af16616) | Создание экземпляра `TUICallEngine` (режим одноэкземпляра). |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/67600#de1c7b92-0a92-49b8-99ab-785e36c9e64a) | Завершение экземпляра `TUICallEngine` (режим одноэкземпляра). |
| [login](https://www.tencentcloud.com/document/product/647/67600#dc857e4b-4458-4046-ab13-2da3cd59b7a8) | Аутентификация основных возможностей аудио- и видеозвонков. |
| [on](https://www.tencentcloud.com/document/product/647/67600#481db1ba-bb8c-4298-a692-281c0b4471a6) | Регистрация слушателя событий. |
| [off](https://www.tencentcloud.com/document/product/647/67600#8dee85b0-3967-464a-b4e9-cd594164f81a) | Отмена регистрации слушателя событий. |
| [call](https://www.tencentcloud.com/document/product/647/67600#ae7d1ece-ba62-426d-9a33-42b2e21def3e) | Совершение звонка один-на-один. |
| [accept](https://www.tencentcloud.com/document/product/647/67600#59e19c12-1f02-43e6-991e-e86471c67f41) | Принятие звонка. |
| [reject](https://www.tencentcloud.com/document/product/647/67600#737fb419-4944-4adc-96c0-d18ed4a429c5) | Отклонение звонка. |
| [ignore](https://www.tencentcloud.com/document/product/647/67600#73d1e436-238f-47ac-a07d-e0db3b029f5e) | Игнорирование звонка. |
| [hangup](https://www.tencentcloud.com/document/product/647/67600#d8a7dd6b-3b95-403a-97fe-ed68eb6f225d) | Завершение звонка. |
| [switchCallMediaType](https://www.tencentcloud.com/document/product/647/67600#417d1d5b-da7d-48d1-b935-39f2083f37d8) | Изменение типа звонка, например, с видеозвонка на аудиозвонок. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/67600#35dae00f-9958-461c-a2e1-fee9c46f7a5f) | Подписка на видеопоток удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/67600#0491e355-52fb-4f31-89d4-4a927666c91d) | Отписка от видеопотока удаленного пользователя. |
| [openCamera](https://www.tencentcloud.com/document/product/647/67600#c5c6d48f-e43b-4783-9f6a-66f3463799ef) | Включение камеры. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/67600#2de922a4-584f-40c7-aa31-be722cfc36e6) | Переключение между фронтальной и задней камерами. |
| [closeCamera](https://www.tencentcloud.com/document/product/647/67600#856c0993-1baa-4fc4-b030-e92dd981c927) | Отключение камеры. |
| [openMicrophone](https://www.tencentcloud.com/document/product/647/67600#0b0d9f9f-bf30-4a4d-a04a-740ee893f333) | Включение микрофона. |
| [closeMicrophone](https://www.tencentcloud.com/document/product/647/67600#44408d8a-5a20-46b3-9113-769ee604fd23) | Отключение микрофона. |
| [selectAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/67600#754db95b-b121-441c-824d-e2b843549858) | Выбор устройства воспроизведения звука (наушники или динамик). |
| [setVideoRenderParams](https://www.tencentcloud.com/document/product/647/67600#593170ad-f21c-46fb-ad11-e2cd46c3c119) | Установка режима рендеринга видеоизображения. |
| [setVideoEncoderParams](https://www.tencentcloud.com/document/product/647/67600#e3c90891-f93a-431e-8b16-2fbfc31b5f4f) | Установка параметров кодирования видеокодера. |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/67600#353aabf6-bf08-4bc2-a396-8c5820898bd2) | Установка уровня красоты, поддержка отключения красоты по умолчанию. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/67600#8ed81cdd-05c9-4c46-ae3d-ba6055dcfc68) | Установка псевдонима и фотографии профиля. |
| [enableMultiDeviceAbility](https://www.tencentcloud.com/document/product/647/67600#a6408ab6-9e50-4dea-9c26-cf3d9b552084) | Установка возможности входа с нескольких устройств для `TUICallEngine`. |


---
*Источник: [https://trtc.io/document/66843](https://trtc.io/document/66843)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*
