# TUILiveLayoutManager

Copyright (c) 2024 Tencent. All rights reserved.

Модуль:   TUILiveLayoutManager @ TUIKitEngine

API для украшения трансляции

**TUILiveLayoutManager**

## TUILiveLayoutObserver

| Список функций | Описание |
| --- | --- |
| [onLiveVideoLayoutChanged](https://www.tencentcloud.com/document/product/647/69267#b14e71e05f158078257d550657844e88) | Произошли изменения макета трансляции |

## TUILiveLayoutManager

| Список функций | Описание |
| --- | --- |
| [addObserver](https://www.tencentcloud.com/document/product/647/69267#671b0fad38ffd4d3a962589f5146025a) | Добавить обратный вызов события |
| [removeObserver](https://www.tencentcloud.com/document/product/647/69267#907d7e4c59a653984e8555fdc5159039) | Удалить обратный вызов события |

## onLiveVideoLayoutChanged

**Произошли изменения макета трансляции**

```
OnLiveVideoLayoutChanged onLiveVideoLayoutChanged = (String roomId, String layoutInfo) {};
```

| Параметр | Описание |
| --- | --- |
| roomId | ID комнаты |
| layoutInfo | Последняя информация макета изображения |

## addObserver

**Добавить обратный вызов события**

```
 void addObserver(TUILiveLayoutObserver observer);
```

| Параметр | Описание |
| --- | --- |
| observer | Прослушиваемые экземпляры |

## removeObserver

**Удалить обратный вызов события**

```
 void removeObserver(TUILiveLayoutObserver observer);
```

| Параметр | Описание |
| --- | --- |
| observer | Прослушиваемые экземпляры |


---
*Источник: [https://trtc.io/document/69267](https://trtc.io/document/69267)*

---
*Источник (EN): [tuilivelayoutmanager.md](./tuilivelayoutmanager.md)*
