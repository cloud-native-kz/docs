# Запуск демонстрации

Этот документ описывает, как быстро запустить демонстрацию Chat и испытать отправку текстовых, голосовых и видеосообщений.

## Быстрое знакомство

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1974df05adb411f0a0a052540099c741.png)

Перед локальной интеграцией мы подготовили [демонстрацию](https://trtc.io/demo/homepage/#/detail?scene=messenger), которую вы можете попробовать онлайн.

## Предварительные требования

### Включение сервиса

1. Войдите в [консоль Chat](https://console.trtc.io/), перейдите на страницу **управления приложениями** и нажмите **Создать новое приложение**. Если у вас уже есть приложение, вы можете пропустить процесс создания приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2882e3e3adb411f08bcc5254007c27c5.png)

2. На странице **управления приложениями** получите SDKAppID и информацию о ключе из столбца SDKAppID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/27e7d9bdadb411f09b75525400bf7822.png)

> **Примечание:** Просмотр информации о ключе требует проверки личности. Информация о ключе является конфиденциальной информацией. Чтобы предотвратить несанкционированное использование, храните ее в безопасности и избегайте утечек.

3. [Перейдите на страницу управления пользователями](https://console.trtc.io/chat/account-management), создайте 2–3 тестовых аккаунта для опробования возможностей чата C2C и группового чата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/27ca22a6adb411f0a68e5254001c06ec.png)

4. Информация userSig. Нажмите [Консоль Chat > Инструменты разработки > Инструмент userSig](https://console.trtc.io/usersig), заполните созданный userID для генерации userSig.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2f29a385c07911f0b4a7525400454e06.png)

### Требования к среде разработки

- React^18.2 || React^19.0.0
- TypeScript
- Node.js >= v18 (рекомендуется: текущая стабильная версия LTS v22.x)
- npm (версия должна соответствовать версии Node.js)
- Git

## Этапы операции

### Получение демонстрации

```
# Запустите код в CLI$ git clone https://github.com/Tencent-RTC/TUIKit_React.git# Перейдите в проект$ cd ./TUIKit_React/demos/rtcube-vite-react# Установите зависимости демонстрации и соберите chat-uikit-react$ npm install
```

### Запуск демонстрации

> **Примечание:** Правильный метод выдачи UserSig — интегрировать код расчета UserSig на ваш сервер и предоставить API, ориентированный на приложение. Когда требуется UserSig, ваше приложение может инициировать запрос к бизнес-серверу для получения динамического UserSig. Для получения дополнительной информации см. [Генерация UserSig на сервере](https://www.tencentcloud.com/document/product/1047/34385).

> **Примечание:** Для соблюдения авторских прав на дизайн эмодзи, проект демонстрации Chat/TUIKit не включает вырезанные элементы больших эмодзи. Пожалуйста, замените их на собственные дизайны или другие пакеты эмодзи, на которые у вас есть авторские права, перед официальным запуском для коммерческого использования. **Показанный ниже пакет эмодзи по умолчанию защищен авторским правом Tencent RTC**, вы можете перейти на [Chat Pro Plus Edition и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro) для использования его бесплатно. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fa73da7661f111f091585254001c06ec.png)

```
# Запустите проектnpm run dev
```

После запуска программы нажмите на карточку "Experience Chat" для входа на страницу входа. Введите полученные SDKAppID, userID и secretKey для опробования функции чата.

## Опробование одноранового чата

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/43baddd5b63711f0a808525400bf7822.png)

## Интеграция Chat-Uikit-React

Если вы хотите интегрировать chat-uikit-react в ваш проект, перейдите на [Интеграция chat-uikit-react](https://www.tencentcloud.com/zh/document/product/1047/50055).

## Обмен и обратная связь

Присоединитесь к [группе технического обмена Telegram](https://t.me/tencent_imsdk) или [группе общения WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik), чтобы получить поддержку профессиональных инженеров и решить ваши проблемы.


---
*Источник: [https://trtc.io/document/45912](https://trtc.io/document/45912)*

---
*Источник (EN): [run-demo.md](./run-demo.md)*
