# Настройка эффектов

Tencent Effect SDK предлагает **эффекты красоты**, **фильтры** и **специальные эффекты**. Для фильтров и специальных эффектов необходимо сначала получить список материалов и настроить их в SDK, указав идентификатор эффекта.

## Красота

Вы можете передать параметры красоты во время инициализации. Вы также можете вызвать метод `setBeautify` SDK для установки эффектов красоты.

- В настоящее время SDK поддерживает следующие эффекты красоты:

```
type BeautifyOptions = {  whiten?: number, // The brightening effect. Value range: 0-1.  dermabrasion?: number // The smooth skin effect. Value range: 0-1.  lift?: number // The slim face effect. Value range: 0-1.  shave?: number // The face width. Value range: 0-1.  eye?: number // The big eyes effect. Value range: 0-1.  chin?: number // The chin effect. Value range: 0-1.// The following parameters are only available in version 1.0.11 and above  darkCircle?: number; // The dark circle effect. Value range: 0-1.  nasolabialFolds?: number; // The nasolabial folds effect. Value range: 0-1.  cheekbone?: number; // The cheek bone effect. Value range: 0-1.  head?: number; // The head effect. Value range: 0-1.  eyeBrightness?: number; // The eye brightness effect. Value range: 0-1.  lip?: number; // The lip effect. Value range: 0-1.  forehead?: number; // The forehead effect. Value range: 0-1.  nose?: number; // The nose effect. Value range: 0-1.  usm?: number; // The distinct effect. Value range: 0-1.}
```

- Вызовите метод `setBeautify` SDK для установки эффектов красоты:

```
sdk.setBeautify({  whiten: 0.2,  dermabrasion: 0,  lift: 0.3,  shave:0.1,  eye: 0.9,  chin: 0,  …})
```

## Фильтры

Учитывая относительно высокую стоимость разработки фильтров, мы предлагаем встроенные фильтры, которые вы можете использовать непосредственно.

1. Получите встроенный список фильтров:

```
const filterList = await sdk.getCommonFilter()
```

2. Установите фильтр:

```
sdk.setFilter(filterList[0].EffectId, 0.5)
```

## Специальные эффекты

Вы можете использовать встроенные эффекты SDK или эффекты, которые вы настроили в [консоли RT-Cube](https://console.tencentcloud.com/xmagic/creator). Чтобы узнать, как настраивать эффекты, пожалуйста, [свяжитесь с нами](https://trtc.io/contact).

```
// Get the built-in effects// By default, both makeup effects and stickers are returned. You can also use the `Label` parameter to specify the category of materials to return.const presetEffectList = await sdk.getEffectList({    Type: 'Preset'    // Label: ['Sticker'] (Return only stickers)})// Get the custom effectsconst customEffectList = await sdk.getEffectList({    Type: 'Custom'})// Pass in the request parameters of `getEffectList`const lipList = await sdk.getEffectList({    PageNumber: 0,    PageSize: 10,    Name: '',    Label: ['Lip makeup'], // Specify the specific type of materials to return    Type: 'Custom'})const eyeList = await sdk.getEffectList({    PageNumber: 0,    PageSize: 10,    Name: '',    Label: ['Eye makeup'], // Specify the category of resources to return    Type: 'Custom'})// Use an effectsdk.setEffect([lipList[0].EffectId, eyeList[0].EffectId])// Specify the effect to use and the strength of the effectsdk.setEffect([{    id: lipList[0].EffectId,    intensity: 0.5}, {    id: eyeList[0].EffectId,    intensity: 0.7})// Set only the filter strengthsdk.setEffect([{    id: lipList[0].EffectId,    intensity: 0.5,    filterIntensity: 0}, {    id: eyeList[0].EffectId,    intensity: 0.7,    filterIntensity: 1})
```

> **Примечание:** При настройке специального эффекта вы можете добавить фильтр к эффекту. В таких случаях вы можете использовать `filterIntensity` для отдельной регулировки силы фильтра.

## Отключение обнаружения

Расходы на производительность при обнаружении ИИ высоки. Чтобы снизить потребление ресурсов, SDK автоматически отключает обнаружение ИИ, когда эффекты не используются, и снова включает обнаружение ИИ при применении эффектов.

```
// Clear all effect settings to disable AI detectionsdk.setBeautify({    whiten: 0,    dermabrasion: 0,    lift: 0,    shave:0,    eye: 0,    chin: 0,    … // reset all parameters to 0})sdk.setEffect('')
```


---
*Источник: [https://trtc.io/document/54291](https://trtc.io/document/54291)*

---
*Источник (EN): [configuring-effects.md](./configuring-effects.md)*
