# Список контактов

Данная статья поможет вам создать интерфейс списка контактов.

## Демонстрация

Если вы ранее не добавляли контакты, загруженный интерфейс списка контактов будет пустым. После добавления контактов они будут отображаться в списке интерфейса, как показано ниже:

| Пустой список контактов | Заполненный список контактов |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eb7b432d2d4b11ef9130525400bf8054.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eba18bda2d4b11efa01d5254005235d8.png) |

## Требования к среде разработки

- Android Studio-Giraffe
- Gradle-7.2
- Android Gradle Plugin Version-7.0.0
- kotlin-gradle-plugin-1.5.31

## Предусловия

Перед созданием интерфейса убедитесь, что вы выполнили следующие 4 пункта:

1. Создали приложение в консоли.
2. Создали несколько учетных записей пользователей в консоли.
3. Интегрировали `TUIKit` или `TUIContact`.
4. Вызвали API `TUILogin` `login` для входа в компонент.

> **Примечание:** все компоненты используют этот API входа. Выполняйте вход только один раз при каждом запуске приложения. Убедитесь в успешном входе перед продолжением; рекомендуется выполнить следующие действия в обратном вызове успешного входа.

Если вы не выполнили вышеуказанные 4 шага, сначала обратитесь к соответствующим шагам в [Начало работы](https://www.tencentcloud.com/document/product/1047/60520), иначе у вас могут возникнуть проблемы при реализации следующих функций.

Если вы уже выполнили все пункты, продолжайте читать ниже.

## Пошаговые инструкции

Для интеграции интерфейса контактов просто встройте соответствующий Fragment списка контактов в ваш Activity.

Файл макета MainActivity:

```
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <FrameLayout
        android:id="@+id/contact_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>

</FrameLayout>
```

Файл Java MainActivity:

Минималистичная версия

Классическая версия

```
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
        TUIContactMinimalistFragment fragment = new TUIContactMinimalistFragment();
        getSupportFragmentManager()
                .beginTransaction()
                .add(R.id.contact_view, fragment)
                .commitAllowingStateLoss();
    }
}
```

```
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
        TUIContactFragment fragment = new TUIContactFragment();
        getSupportFragmentManager()
                .beginTransaction()
                .add(R.id.contact_view, fragment)
                .commitAllowingStateLoss();
    }
}
```

Функции интерфейса контактов разделены следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ebaab1582d4b11ef918f52540005b090.png)

`TUIContact` по умолчанию обрабатывает действия клика в этом интерфейсе следующим образом:

| Действие | Эффект |
| --- | --- |
| Клик по `Новые контакты` | Отобразить ожидающие запросы дружбы |
| Клик по `Групповые чаты` | Отобразить все групповые чаты текущей учетной записи |
| Клик по `Список заблокированных` | Отобразить список заблокированных пользователей текущей учетной записи |
| Клик по аватару контакта | Перейти в интерфейс управления контактом |
| Клик по знаку `+` в верхней правой части интерфейса | Открыть всплывающее меню с опциями `Добавить в контакты` и `Добавить группу` |

## Дополнительные практики

Вы можете локально [запустить исходный код TUIKitDemo](https://www.tencentcloud.com/document/product/1047/45914) для изучения дополнительных примеров реализации интерфейса.

## Свяжитесь с нами

Если у вас есть вопросы по этой статье, присоединяйтесь к [группе технической поддержки Telegram](https://t.me/+EPk6TMZEZMM5OGY1), где вы получите надежную техническую поддержку.


---
*Источник: [https://trtc.io/document/61218](https://trtc.io/document/61218)*

---
*Источник (EN): [contact-list.md](./contact-list.md)*
