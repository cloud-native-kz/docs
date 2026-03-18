# Пользовательский рингтон

Этот раздел описывает, как заменить рингтон входящего звонка в TUICallKit. Рингтон входящего звонка включает **рингтон приложения** и **рингтон офлайн-уведомления**.

## Установка рингтона приложения

Существует два способа установки рингтона приложения:

#### 1. Замена аудиофайла

Если вы интегрируете компонент TUICallKit через зависимость исходного кода, вы можете заменить аудиофайлы в папке [tuicallkit-kt/src/main/res/raw](https://github.com/Tencent-RTC/TUICallKit/tree/main/Android), чтобы настроить рингтон.

| Имя файла | Применение |
| --- | --- |
| phone_dialing.mp3 | Рингтон при инициировании вызова |
| phone_ringing.mp3 | Рингтон при получении вызова |

#### 2. Вызов интерфейса setCallingBell

Вы также можете настроить рингтон входящего звонка через интерфейс [setCallingBell](https://www.tencentcloud.com/document/product/647/51005#setcallingbell).

Kotlin

Java

```
TUICallKit.createInstance(context).setCallingBell(filePath)
```

```
TUICallKit.createInstance(context).setCallingBell(filePath);
```

## Установка режима без звука

Если телефон не должен издавать звук, вы можете включить режим без звука, используя интерфейс [enableMuteMode](https://www.tencentcloud.com/document/product/647/51005#enablemutemode).

Kotlin

Java

```
TUICallKit.createInstance(context).enableMuteMode(true)
```

```
TUICallKit.createInstance(context).enableMuteMode(true);
```

## Установка рингтона офлайн-уведомления

Для настройки рингтона офлайн-уведомления см.: [Настройка рингтона входящего звонка FCM офлайн-уведомления](https://www.tencentcloud.com/document/product/647/50999#909f9f70-6480-405b-86b9-6c18c0c695e6).


---
*Источник: [https://trtc.io/document/59845](https://trtc.io/document/59845)*

---
*Источник (EN): [custom-ringtone.md](./custom-ringtone.md)*
