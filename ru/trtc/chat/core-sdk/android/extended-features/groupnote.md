# GroupNote

### Особенности плагина

Начиная с версии 7.1, можно интегрировать плагин группового пасьянса `TUIGroupNotePlugin`. Это библиотека пользовательского интерфейса с закрытым исходным кодом, которая зависит от `TUIChat`. После интеграции плагина можно инициировать групповые занятия пасьянсом непосредственно в `TUIChat`.

### Интеграция для Android

`TUIGroupNotePlugin` — это плагин с закрытым исходным кодом, который необходимо интегрировать через gradle. Найдите build.gradle приложения и добавьте зависимость плагина голосования в секцию dependencies.

Классическая версия

```
  dependencies {    ...  # Integrate the chat feature.  api project(':tuichat')  ...  # Integrate solitaire plugin, which is supported starting from version 7.1.  api "com.tencent.imsdk:tuigroupnote-plugin:7.3.4358"  ...}
```

### Интеграция для iOS

`TUIGroupNotePlugin`, как и обычные компоненты TUIKit, можно быстро интегрировать через CocoaPods. Подробные инструкции по интеграции можно найти в [Интеграция основных функций](https://trtc.io/zh/document/60521).

Для плагина пасьянса нужно добавить всего одну строку в Podfile для завершения интеграции:

Классическая версия

```
# Uncomment the next line to define a global platform for your project# ...  # Integrate the chat feature.  pod 'TUIChat/UI_Classic'   ...  # Integrate solitaire plugin, which is supported starting from version 7.1.  pod 'TUIGroupNotePlugin'  ...end
```

> **Примечание** `TUIGroupNotePlugin` зависит от `TUIChat`. Интеграция только `TUIGroupNotePlugin` вызовет аномалии функций, и интерфейс пасьянса не будет отображаться нормально. `TUIGroupNotePlugin` поддерживается начиная с версии 7.1. Для использования плагина пасьянса обновите `TUIChat` до версии 7.1 или более поздней.


---
*Источник: [https://trtc.io/document/67615](https://trtc.io/document/67615)*

---
*Источник (EN): [groupnote.md](./groupnote.md)*
