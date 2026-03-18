# Просмотр результатов задач

### Как получить метаданные медиа?

Подробную информацию см. в разделе [DescribeMediaMetaData](https://intl.cloud.tencent.com/document/product/1041/37461).

### Могу ли я запросить недавно завершённые задачи с помощью `ScrollToken`?

> **Примечание:** параметр флага пагинации `ScrollToken` используется при постраничном запросе ваших данных. Если невозможно запросить все задачи в одном запросе, API вернёт `ScrollToken`, который следует передать в следующий запрос, чтобы он начался со записи, следующей за `ScrollToken`.

### Как запросить список задач?

Подробные инструкции см. в документации API [DescribeTasks](https://intl.cloud.tencent.com/document/product/1041/33643).

### В каком порядке возвращаются задачи?

Возвращаемые задачи сортируются по **времени создания**. Дополнительную информацию см. в [DescribeTasks](https://intl.cloud.tencent.com/document/product/1041/33643).

### Как добавить анимированные водяные знаки?

Преобразуйте анимированные изображения в формат APNG и добавьте их в качестве водяных знаков в параметрах рабочего процесса.

### Как изменить шаблон водяного знака?

Подробную информацию см. в документации API [ModifyWatermarkTemplate](https://intl.cloud.tencent.com/document/product/1041/33646).

### Как связать MPS с бакетами COS?

При настройке рабочего процесса выберите триггер-бакет, и видео, загруженные в выбранный бакет, будут обработаны автоматически. Дополнительную информацию см. в разделе [Управление рабочими процессами](https://intl.cloud.tencent.com/document/product/1041/33485).

### Результаты OCR генерируются для кадра видео. Как мне получить нужный кадр?

1. Запишите временную точку, в которой генерируются результаты OCR.
2. Передайте временную точку в параметр запроса `ProcessMedia`: [MediaProcessTaskInput](https://intl.cloud.tencent.com/document/product/1041/33640) > [SnapshotByTimeOffsetTaskInput](https://intl.cloud.tencent.com/document/product/1041/33690).

### Как запросить статистические данные?

Вы можете войти в [консоль Media Processing Service](https://console.tencentcloud.com/mps/statistics?tab=transcode) и нажать **Статистика использования**. На этой странице представлены подробные статистические данные.


---
*Источник: [https://www.tencentcloud.com/document/product/1041/43058](https://www.tencentcloud.com/document/product/1041/43058)*

---
*Источник (EN): [task-result-viewing.md](./task-result-viewing.md)*
