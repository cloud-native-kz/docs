# Часто задаваемые вопросы

### Ошибка выполнения: "does not provide an export named 'createBlock' "?

Если после выполнения описанных выше действий возникает следующая ошибка, убедитесь, что версия vite заблокирована ниже 3.0.0, а версия vue — ниже 3.4.9.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f0a852d21bf911ef8a48525400762795.png)

Причина в том, что шаблон проекта electron поддерживает версии vite, указанные ниже 3.0.0, но свойства в версии vue 3.4.9 и выше требуют обновления версии vite для поддержки. Проблема была отправлена в официальный репозиторий vue: [https://github.com/vuejs/core/issues/10177](https://github.com/vuejs/core/issues/10177).

### совместима ли trtc-electron-sdk с официальной версией Electron v12.0.1?

Да, trtc-electron-sdk не зависит от собственного SDK electron, поэтому не существует связанных зависимостей версий.


---
*Источник: [https://trtc.io/document/57419](https://trtc.io/document/57419)*

---
*Источник (EN): [faqs.md](./faqs.md)*
