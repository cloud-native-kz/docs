# Шаг 1: Установка Chat SDK

В этом документе описывается, как быстро интегрировать Chat SDK в ваш проект Windows.

## Требования к окружению

- Операционная система: Windows 7 или более поздняя версия.
- Среда разработки: Visual Studio 2010 или более поздняя версия. Рекомендуется Visual Studio 2019.

## Интеграция Chat SDK

Ниже описывается, как интегрировать SDK в проект Visual Studio 2019 путем создания простого проекта MFC.

### Шаг 1. Загрузка Chat SDK

Загрузите Chat SDK для Windows [здесь](https://github.com/TencentCloud/TIMSDK/tree/master/Windows/IMSDK) и распакуйте архив. Для удобства вы можете переименовать его в "ImSDK". Он содержит следующие компоненты:

| Имя директории | Описание |
| --- | --- |
| c_include | Файлы заголовков C API |
| cpp_include | Файлы заголовков C++ API |
| shared_lib\\Win32 | **32-битный режим Release**, использующий опцию /MT для связывания файлов библиотеки. |
| shared_lib\\Win64 | **64-битный режим Release**, использующий опцию /MT для связывания файлов библиотеки. |

### Шаг 2. Создание проекта

Откройте Visual Studio и создайте приложение MFC с названием "IMDemo". Если приложение MFC не входит в первые варианты, вы можете найти его, используя поиск шаблонов в верхней части.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ada8dbd247d811ef9b7d525400fdb830.png)

Для быстрой интеграции выберите относительно простой тип **Dialog based** на странице **Application Type** мастера. Остальные параметры конфигурации оставьте по умолчанию.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ca6f6ee947d811ef92e952540055f650.png)

### Шаг 3. Копирование файлов

Скопируйте папку SDK, полученную после распаковки (папку "ImSDK", полученную на [шаге 1](https://www.tencentcloud.com/document/product/1047/34310#step-1.-download-the-im-sdk)), в директорию, где расположена папка `IMDemo.vcxproj`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/894b6993499411ef9bf1525400a9236a.png)

### Шаг 4. Изменение конфигурации проекта

SDK предоставляет 32-битные и 64-битные статические библиотеки в режиме **Release**, требующие специальной конфигурации. Откройте страницу свойств IMDemo, выберите **Solution Explorer**, щелкните правой кнопкой мыши `IMDemo` и выберите **Properties**.

Далее приводится пример для **32-битного режима Release**:

1. Добавление директории включаемых файлов.
 Перейдите в **C/C++** > **General** > **Additional Include Directories** и добавьте директорию заголовков SDK для C `$(ProjectDir)ImSDK\\c_include`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/90d2e6f8499411ef998b525400f69702.png)

2. Добавление директории библиотек.
 Перейдите в **Linker** > **General** > **Additional Library Directories** и добавьте директорию библиотеки SDK `$(ProjectDir)ImSDK\\shared_lib\\Win32`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c6970319499411ef8357525400bdab9d.png)

3. Добавление файла библиотеки.
 Перейдите в **Linker** > **Input** > **Additional Dependencies** и добавьте файл библиотеки SDK `ImSDK.lib`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a7eca1e7499411efbaba525400d5f8ef.png)

4. Копирование файла DLL в директорию выполнения.
 Перейдите в **Build Events** > **Pre-Build Event** > **Command Line**, введите `xcopy /E /Y "$(ProjectDir)ImSDK\\shared_lib\\Win32" "$(OutDir)"` и скопируйте динамическую библиотеку `ImSDK.dll` в выходную директорию проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5f65d4fd47d911ef8866525400bdab9d.png)

5. Указание формата кодировки исходного файла.
Файл заголовков SDK использует формат кодировки UTF-8, тогда как некоторые компиляторы компилируют исходные файлы в формате кодировки системы по умолчанию. Это может привести к ошибке компиляции. Установите этот параметр, чтобы инструктировать компиляторы компилировать исходные файлы с использованием кодировки UTF-8.
Перейдите в **C/C++** > **Command Line** > **Additional Options** и введите `/source-charset:.65001`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6db9620247d911ef8f89525400d5f8ef.png)

Большинство настроек для **64-битного режима Release** аналогичны настройкам для **32-битного режима Release**. Различие заключается в директории библиотеки SDK следующим образом:

1. Добавление директории библиотек.
- Перейдите в **Linker** > **General** > **Additional Library Directories** и добавьте директорию библиотеки SDK `$(ProjectDir)ImSDK\\shared_lib\\Win64`.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7e53500347d911ef8866525400bdab9d.png)

2. Копирование файла DLL в директорию выполнения.
- В режиме **Release** перейдите в **Build Events** > **Pre-Build Event** > **Command Line**, введите `xcopy /E /Y "$(ProjectDir)ImSDK\\shared_lib\\Win64" "$(OutDir)"` и скопируйте динамическую библиотеку `ImSDK.dll` в выходную директорию проекта.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8fcea99347d911ef91895254002693fd.png)

### Шаг 5. Вывод номера версии Chat SDK

- В файле `IMDemoDlg.cpp` добавьте включение файла заголовка:

```
#include "TIMCloud.h"
```

- В файле `IMDemoDlg.cpp` найдите функцию `CIMDemoDlg::OnInitDialog` и добавьте следующий тестовый код перед `return`:

```
SetWindowText(L"IMDemo");CString szText;szText.Format(L"SDK version: %hs", TIMGetSDKVersion());CWnd* pStatic = GetDlgItem(IDC_STATIC);pStatic->SetWindowTextW(szText);
```

- Нажмите **F5** для выполнения кода и вывода номера версии SDK.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7111425447da11ef92e952540055f650.png)

## Часто задаваемые вопросы

- Если происходит следующая ошибка, проверьте, была ли правильно добавлена директория файла заголовка SDK согласно предыдущей конфигурации проекта:

```
fatal error C1083: unable to open the header file: "TIMCloud.h": No such file or directory
```

- Если происходит следующая ошибка, проверьте, были ли правильно добавлены директория библиотеки SDK и файл библиотеки согласно предыдущей конфигурации проекта:

```
LINK : fatal error LNK1104: Unable to open the `ImSDK.lib` file.
```

```
error LNK2019: Unresolved external symbol `__imp__TIMGetSDKVersion`, referenced in the `"protected: virtual int __thiscall CIMDemoDlg::OnInitDialog(void)" (?OnInitDialog@CIMDemoDlg@@MAEHXZ)` function
```

- Если происходит ошибка, проверьте, был ли скопирован DLL-файл SDK в директорию выполнения, как описано в шаге конфигурации проекта выше.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fc0d4df2222011ee909c525400cea498.png)


---
*Источник: [https://trtc.io/document/34310](https://trtc.io/document/34310)*

---
*Источник (EN): [step-1-install-chat-sdk.md](./step-1-install-chat-sdk.md)*
