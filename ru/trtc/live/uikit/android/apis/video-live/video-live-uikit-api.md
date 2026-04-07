# API Live UIKit для видео

## Введение в API

VideoLiveKit — это компонент прямой трансляции с **пользовательским интерфейсом**. Используя API VideoLiveKit, вы можете быстро реализовать сценарий онлайн-трансляции с помощью простых интерфейсов. Если вы хотите протестировать и отладить интерактивную прямую трансляцию, обратитесь к [Запуск демонстрации](https://www.tencentcloud.com/document/product/647/60454#). Если вы хотите интегрировать нашу функцию непосредственно в ваш проект, прочитайте [Быстрая интеграция (TUILiveKit)](https://www.tencentcloud.com/document/product/647/60037#).

## Обзор API

| **API** | **Описание** |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/61638#d147f174-e55a-4ba2-bbaf-2792c9419650) | Создать экземпляр VideoLiveKit (Singleton Pattern) |
| [startLive](https://www.tencentcloud.com/document/product/647/61638#c6f79ba4-2dc1-4d65-82b3-e52d3ef28f2f) | Начать трансляцию в прямом эфире с использованием roomId. |
| [joinLive](https://www.tencentcloud.com/document/product/647/61638#34d62c35-ff96-4250-be5a-a518ed341a5d) | Присоединиться к трансляции в прямом эфире с использованием roomId. |

## Детали API

### createInstance

Получить экземпляр VideoLiveKit.

```
static VideoLiveKit createInstance(Context context)
```

**Параметры:**

| **Параметр** | **Тип** | **Описание** | **Значение по умолчанию** | **Значение** |
| --- | --- | --- | --- | --- |
| context | Context | Обязательно | - | Объект контекста Android |

**Возвращаемое значение:** VideoLiveKit

### startLive

Начать трансляцию в прямом эфире с использованием roomId.

```
void startLive(String roomId);
```

**Параметры:**

| **Параметр** | **Тип** | **Описание** | **Значение по умолчанию** | **Значение** |
| --- | --- | --- | --- | --- |
| roomId | String | Обязательно | - | ID комнаты трансляции в прямом эфире |

**Возвращаемое значение:** void

### joinLive

Присоединиться к трансляции в прямом эфире с использованием roomId.

```
void joinLive(String roomId);
```

**Параметры:**

| **Параметр** | **Тип** | **Описание** | **Значение по умолчанию** | **Значение** |
| --- | --- | --- | --- | --- |
| roomId | String | Обязательно | - | ID комнаты трансляции в прямом эфире |

**Возвращаемое значение:** void


---
*Источник: [https://trtc.io/document/61638](https://trtc.io/document/61638)*

---
*Источник (EN): [video-live-uikit-api.md](./video-live-uikit-api.md)*
