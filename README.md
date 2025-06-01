# Memrise Template v5.0

This template recreates the Memrise experience to make Anki more accessible for ex-Memrise users and everyone who finds the default Anki Cards too intimidating. It also restores several features [retired from Memrise](#spelling-diffs) and adds many that [Memrise never had](#other). The functionality covers all [types of questions](#question-types): **text**, **images**, **audio**, and **cloze deletions**; as well as all the [input methods](#input-methods): **typing**, **multiple-choice**, and **tapping**. Typing includes the **on-screen keyboard**, the **hint button**, and the **spelling diffs** (Memrise's "You wrote: ...") after answering a Card. Multiple-choice supports **images**, choices can be [**generated automatically**](#automatically-filling-choice-fields-for-multiple-choice-cards), and edited manually. Answers for either input method are **graded automatically**, taking **alternative answers** and optional parts separated by `;` and `()` into account. Automatic ratings can be [manually overruled](#keyboard-navigation) in case of an erroneous question or an inconsequential typo in the answer. The template works with **every** [Anki app on each platform](https://apps.ankiweb.net/)\* in **offline mode** and can also be used **online** in **any web browser** to review cards directly on [**AnkiWeb**](#ankiweb) without an installed app\*\* (all listed functions work the same way, no exceptions). The template additionally supports [**LaTeX**](#latex) (MathJax) equations, [**Dark mode**](#dark-mode-and-themes), multiple color [**themes**](#dark-mode-and-themes), and a variety of [other customization options](#customization).

![Overview](https://github.com/user-attachments/assets/67a6462c-a6b0-4da3-8d3c-7fbc9308e777)

<sup>*This includes the main **Desktop** app, [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki) for **Android**, and [AnkiMobile](https://apps.apple.com/us/app/ankimobile-flashcards/id373493387) for **iOS**. There are some (non-breaking) differences in how the template looks and works in the iPhone app — if anyone wishes to participate in testing to help in fixing the remaining discrepancies, please get [in contact](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233)</sup>
<br>
<sup>**A (desktop) app is required for the first-time setup</sup>

## 💡 Quick start

>---
>1. Download the template from [AnkiWeb](https://ankiweb.net/shared/info/510199145) or [release page](https://github.com/Eltaurus-Lt/Anki-Card-Templates/releases/tag/v5.0) and open the `Memrise… .apkg` file with Anki
>2. Use `Memrise (Lτ) Preset […] v5.0` Note Type when making new cards (via **`Add`** → …) or importing a spreadsheet (`File`→`Import` → … [full guide](https://github.com/Eltaurus-Lt/CourseDump2022?tab=readme-ov-file#-importing-into-anki))
>3. On Android, enable `Type answer into the card` (app settings ⚙️ → `Advanced` → `Type answer into the card` → toggle **ON**)
>
>Generating Multiple-Choice Cards (Optional):
>
>4. In the desktop Anki, install [the support addon](https://ankiweb.net/shared/info/884199977) (`Tools` → `Add-ons` → `Get Add-ons` → Paste "884199977" → `Ok` → Restart Anki)
>5. Open **`Browse`** window → Select several cards in the table 🖱️ → Right Click 🖱️ → `Fill Choices` → `Ok`
>6. To make the Multiple-Choice Cards available on mobile and AnkiWeb: **`Sync`** Anki desktop to AnkiWeb → **`Sync`** in your mobile Anki app
>---

If you require any help with any of the steps, please feel free to leave a comment in [the Anki Forum thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233).
Feedback and feature suggestions are also very much appreciated.


&nbsp;


## Question types

The template allows all three types of [Fields](#3-adding-new-fields) from Memrise — **Text**, **Audio**, and **Images** — to be used as questions. They will look and function in the same way, including the audio button animations. On top of that, the template supports all the standard Anki features: using bold, italic, colored, and otherwise **formatted text**, **lists**, **hyperlinks**, [**math equations**](https://docs.ankiweb.net/math.html), any [combination of the above](https://us1.discourse-cdn.com/flex002/uploads/anki2/original/3X/7/9/79c9034fcf01c01225bb2ec3fff6d0180babc395.png), and also making [cloze-deletion questions](#cloze-deletion).

![Questions](https://github.com/user-attachments/assets/cc5597b6-996c-4768-9ffc-f3d0b26c352d)

All the options can be used without any additional setup — the template auto-adjusts to the type of data placed in the [question Field](#4-changing-the-question-field). However, to keep the collection organized and easily manageable and to simplify [adding new Card Types](#1-making-new-card-types) for more directions of testing, it is a good idea to label data properly and place each piece into its dedicated [Field](#3-adding-new-fields). To change which Field will be presented as a prompt on questions, refer [to the instructions in this section](#4-changing-the-question-field).

### Cloze deletion

[Cloze deletion](https://docs.ankiweb.net/editing.html#cloze-deletion) is a special type of question made from text, in which a certain fragment is omitted and the answer is expected to fill the gap. A piece of text can have multiple parts clozed and turned into individual questions. This makes cloze deletion well-suited for creating an unlimited number of [Cards](#key-concepts-anki-vs-memrise) from a single [Note/Sentence](#key-concepts-anki-vs-memrise).

![Cloze deletion](https://github.com/user-attachments/assets/fedb78fe-1032-46c1-b8b8-8e19850b4f7b)

Because of the differences from regular Notes in Card generation conditions (Cards are created based on the number of clozes instead of a predefined set of [Card Types](#1-making-new-card-types)), cloze deletion in Anki requires using special cloze [Note Types](#key-concepts-anki-vs-memrise). The cloze version of the template is called "Memrise (Lτ) Cloze Template v..." and is included in the [shared deck](https://ankiweb.net/shared/info/510199145).

Cloze deletion questions are compatible with all the [input methods](#-input-methods).

<details>
  <summary>Usage tips:</summary>

> 1. cloze 🚧
> 2. hint 🚧
> 3. multiple clozes 🚧
> 4. same clozes 🚧
> 5. nested clozes 🚧

</details>

## Input methods

The template allows making Anki Cards with all three types of tests available on Memrise: Typing, Multiple-Choice, and Tapping. Cards with each method are [added](#1-making-new-card-types) and [removed](#2-removing-existing-card-types) independently, making any combination of enabled input methods and [testing directions](#5-changing-the-answer-field) possible (in contrast to Memrise, where multiple-choice tests cannot be avoided).

![Inputs](https://github.com/user-attachments/assets/1748bb8c-55e5-49a8-a199-9cd5f98056ff)

**Typing** method includes [customizable on-screen keyboard](#7-on-screen-keyboard-layout) to make it easier to type on mobile devices or use languages not installed on the system. The keyboard contains the Memrise hint button, which removes incorrectly typed parts of the answer and reveals the correct answer one character at a time. If it is not needed, the hint button (or the on-screen keyboard as a whole) can be [disabled](#10-disabling-individual-elements).
**Multiple-choice** tests are generated based on the contents of [the specified choices Field](#5-changing-the-answer-field). For maximum effectiveness, the choices can be edited manually (e.g., by appending the typed answer each time a sibling Typing Card is answered incorrectly), or [filled automatically](#automatically-filling-choice-fields-for-multiple-choice-cards) using [the support Add-on](#the-support-add-on). In the current version, multiple-choice Cards will not function properly with Audio choices (this feature is in [the prototype phase](https://github.com/Eltaurus-Lt/Anki-Card-Templates/issues/20#issuecomment-2846107995) and will be implemented if people keep requesting it). All other kinds of choices — Text, **Images**, **Formatted HTML**, **[LaTeX Equations](#latex)**, etc. — are fully supported.
**Tapping** tests are generated from [the specified sentence Field](#5-changing-the-answer-field), splitting the contents into individual buttons at each `space` character. To force several words into a single button, non-breaking space (HTML code `&nbsp;`) can be used to separate them in the Field's contents instead (this will not affect the other input methods).

### Spelling diffs

Cards with typing and tapping inputs, when answered incorrectly, will also show **spelling diffs** — the exact places where something is missing or input redundantly in the submitted answer (A feature no longer present on Memrise):

![spelldiff](https://github.com/user-attachments/assets/b4de830a-38cf-47f2-887f-0f4014aacc00)

## Dark mode and Themes

The template provides a dedicated **Dark mode**, which the original Memrise site does not have. In addition, there are several completely **new color themes** [designed as alternatives](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/163#p-147991-h-1-template-themes-2) for the Memrise's yellowish palette. Each comes with both light and dark variants:

![Color Schemes](https://github.com/user-attachments/assets/5bedf070-0002-405b-bcf3-6210f6321917)
<details>
<summary><b>Full table</b></summary>

  ![atlas](https://github.com/user-attachments/assets/f40f7834-ed8b-4eb8-936f-6aff874680d5)

</details>

The choice between the light and dark modes is defined by the respective Anki app setting, while a color theme is [selected individually for each Card Type](#11-selecting-a-theme). The latter can be used to color-code different types of questions within the same Deck/Course, or to distinguish between different Courses, Languages, Topics, etc.
To make Cards even more personalized, [more themes can be created](#advanced) using a set of rules defined in the template.

## LaTeX

Anki [provides](https://docs.ankiweb.net/math.html) the ability to use LaTeX (MathJax) equations in Card Fields out of the box. The template builds upon this feature, allowing users to enter mathematical expressions with [each of the input methods](#input-methods), automatically converting and rating submitted answers. For typing and tapping Cards, the info screen shows both the typeset equation and the [spelling diff](#spelling-diffs) for LaTeX source code:

![LaTeX](https://github.com/user-attachments/assets/e8831bf0-a43d-4d78-8b25-ed835c8e21d5)

LaTeX evaluation is a [**separate mode enabled in Card settings**](#6-changing-the-input-method). In this mode, the template decides the correctness of formulaic answers based on the MathJax-converted result, permitting inconsequential differences in equation typesetting, such as omitting delimiters or swapping the order of subscript and superscript of a variable. Because LaTeX syntax implies the use of brackets, commas, semicolons, and other special characters, which is different from the [Memrise punctuation rules](https://memrise.zendesk.com/hc/en-us/articles/360015886897-A-Guide-to-Typing-Tests-Tapping-Tests-and-Memrise-Punctuation), this mode is not suited for evaluating regular answers and should be reserved for Cards with equation answers only.

## AnkiWeb

[AnkiWeb](https://ankiweb.net/decks) is a companion site for Anki apps. By itself, it provides only the rudimentary functionality for reviews: there are no buttons for audio (it is embedded as bare HTML tags), no audio autoplay, even basic typing, offered by stock Anki Cards, is not supported.

This template patches all these issues, having the necessary Anki methods reimplemented within itself. It makes the **Cards fully cross-platform**, with all the [input methods](#input-methods) (including typing), interactive audio buttons, autoplay, [spelling diffs](#spelling-diffs), the on-screen keyboard, and everything else, available in any web browser on any operating system:

![AnkiWeb in desktop and mobile browsers (Firefox, Chrome, and Safari)](https://github.com/user-attachments/assets/20ce6f93-bb86-4ef6-b3eb-60019ff36e6f)

With AnkiWeb as a full-fledged option for reviewing Cards, you can study on a device without an installed Anki app, like a school machine, by simply logging into the site [AnkiWeb](https://ankiweb.net/decks).
On mobile, using AnkiWeb instead of an app can serve as a means to save storage (at the expense of internet traffic and loading times). For iPhones, it provides a way to avoid the limitations of the AnkiMobile app, such as the [inability to auto-submit multiple-choice answers](https://forums.ankiweb.net/t/trigger-show-answer-fliptoback-in-javascript/36643/4?u=eltaurus), or the slight layout and styling differences. AnkiWeb can also serve as a free substitute for the paid AnkiMobile.

When reviewing Cards in a browser, the exterior interface will be adjusted using the template styles. In particular, the `Show Answer` and the rate buttons will have the Memrise look (similar to the `Next` / `I don't know` / `Check Answer` button), with the rate button suggested by the template's auto-rating algorithm highlighted:

![auto rating](https://github.com/user-attachments/assets/a4638db3-4774-4baf-879a-adf133c06168)

## Other

<!-- fuzzy answer matching | timers -->

In addition to introducing the [Dark mode, color Themes](#dark-mode-and-themes), [LaTeX support](#latex), and restoring the [spelling diffs feature](#spelling-diffs), the template has a few other improvements over the Memrise site.

### Keyboard navigation

With the help of the [complementary Add-on](#the-support-add-on), the template supports Memrise keyboard shortcuts, combining them with the Anki ones and adding a few shortcuts of its own, to make all the features accessible on desktop without a mouse. Depending on the context, `Enter` is used to submit an answer, flip to the info screen, or flip to the next Card, automatically rating the submitted answer either "Again" or "Good" (Memrise shortcut replacing Anki's default `Enter` = rate "Good"). On the front side of a Card, number keys `1`–`0` can be used to answer multiple-choice and tapping questions (Memrise shortcuts), while on the back, the numbers `1`–`4` manually rate a Card "Again", "Hard", "Good", or "Easy", overruling any automatically assigned rating (Anki shortcut). If a Card, by accident, is rated incorrectly, `Ctrl+Z`\*\*\* can be used to go back and redo the Card (Anki shortcut). When a correct answer is submitted, the default Memrise behaviour would be to automatically flip to the next Card, skipping the info screen. In the template, the `Space` key can be used to show the info screen regardless of the answer correctness (original Template shortcut replacing Anki's default `Space` = rate "Good"). `Tab` can be used to cycle through audio buttons on the info screen (Anki shortcut). When an audio button is selected using `Tab` (marked by a circular outline), pressing `Enter` replays the audio (original Template shortcut), instead of invoking any of the Memrise actions described previously:

![Keyboard navigation (Anki)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/ff7cb131-a234-4b40-b01c-5d7894c382c7)

Alternatively, `R` can be used to replay all audio (Anki shortcut). Also, `D` (Anki shortcut) can be used to get from reviewing back to the main Deck selection screen (if no typing input is active), while `Tab` and `Enter` (Anki shortcuts) can be used to navigate between the Decks.

<sup>***Note that `Ctrl+Z`, as well as the `R` and `D` shortcuts, are listed here for general information. They are provided by the Anki desktop app, and not by the template itself. As such, they will not work on [AnkiWeb](#AnkiWeb). But all the other listed shortcuts, including the number keys, will</sup>

### Custom parameters

Several parameters, which on Memrise were strictly dictated by the site, are exposed and available for manual adjustments. This includes the number of columns and maximum number of choices in multiple-choice Cards, the ability to avoid multiple-choice questions altogether, the number of keys in a randomly-selected on-screen keyboard, the option to enable/disable the Hint button, the option to display the Audio question button in a reasonable size (active in the template by default, but can be reverted back to the original Memrise behavior), and the delay between submitting an answer and the automatic Card flip. There is also an option to display the info screen after each Card by default, without having to [press `Space`](#keyboard-navigation) after correct answers.

### Mems

Not exactly a feature of the template itself, but with Anki's ability to [store any kind of data in any Field](#key-concepts-anki-vs-memrise), it is easy to put images and story mnemonics (formerly known as "Mems" on Memrise), as well as notes of any other kind, into your Cards. Instructions for adding more Fields to the template (for any purpose) are presented in the [respective customization section](#3-adding-new-fields).

### Layout without visual bugs

This template does not use any of the original Memrise code and is written from scratch with only references to such things as measurements, colors, and fonts. It is designed to have the simplest possible HTML code in order to facilitate further [customization](#Customization). This simplicity also allows for avoiding visual bugs and layout issues, of which there are plenty in the original Memrise interface:

><details>
><summary><b>List of fixed issues</b></summary>
> 
>> All screenshots and recordings are marked by the respective logos:
>> 
>> ![ank_s](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/99799137-a232-42d0-8321-d11cacd00fcd) - **Anki**
>> 
>> ![mem_s](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/f5fd82ba-c612-44a5-8f34-e10c946d680f) - **Memrise**
>&nbsp;
> 
> 1. Elements jitter on the answer submission
> 
>> ![Submit jitter (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/7c6a4ff3-05f6-4c9a-83ec-288584e65697)
>&nbsp;
>
> 2. Cropped text labels 
>
>> ![Fonts cropping (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/2bec6453-353b-4c5c-9cef-b34592bb9457)
>&nbsp;
>
>3. Audio icons blurring on hover
>
>> ![Audio blurring (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/7f04ce9e-3ec7-46f6-a418-21354b962c49)
>&nbsp;
> 
> 4. On-screen keyboard buttons respond to clicks:
>
>> ![Button clicks (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/954d1852-ca73-43b3-b188-5cc3ec701305)
>&nbsp;
>
> 5. Keyboard character alignment improved (text baseline instead of bounding box center):
>
>> ![Keys centering (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/107f4c4f-7a81-4d77-b33b-f76fee53e213)
>&nbsp;
>
> 6. Aliasing artefacts in the corners of buttons:
>
>> ![Aliasing (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/85f11f4e-c6ee-429d-b462-149b9d6c907b)
>&nbsp;
>
> 7. The pressed multiple-choice button stays pressed instead of jittering back:
> 
>> ![Multiple-choice click (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/74e1c2f1-d4ae-4e13-9210-bc7b33705654)
>&nbsp;
>
> 8. Color scheme is consistent (the graying-out effect is removed, the correct and pressed buttons are recolored to match the good and bad answers in typing questions):
>
>> ![Color scheme (Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/1ff3e975-98b7-4267-b492-eecbaa75f149)
>>
>> ![Color scheme (Anki)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/99f50d23-2d68-4715-b8af-846747b7a07c)
>&nbsp;
>
> 9. Multiple-choice number labels centering:
> 
>> ![Multiple-Choice labels (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/be7b7a63-71e5-429e-87f5-e54e34ba0c56)
>&nbsp;
>
> 10. Multiple-choice questions are ensured to have unique options, unlike their implementation at Memrise:
>
>> ![Choice is not an option (Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/532d3665-5dce-4614-a119-9b8908ab3c46)
>&nbsp;
>
> 11. Audio buttons do not use raster assets, which reduces size, improves image sharpness, and keeps the code self-contained. Also, icons for audio questions do not scale up to comically large sizes on wide monitors.
>
>> ![Audio button blurring](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/34a32bdc-e2c4-49c4-92c6-49af8fb71040)
>&nbsp;
>
> 12. The keyboard in tapping questions does not jitter on the first input. Also, the tapping buttons visibly respond to key presses:
> 
>> ![Tapping buttons jitter and responsiveness](https://github.com/user-attachments/assets/e6816ff6-e2c6-45f4-a485-e777119c47b8)
>
></details>

There is also an [interactive online demo](https://codepen.io/Eltaurus/full/mdaMQby) to get a first-hand impression of the functionality before downloading anything (this demo is not updated as regularly as the template itself – only some of the oldest features of the template are represented).

<details>
<summary>More screenshots</summary>
 
![Audio question](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/58fe1cd2-02de-4e16-b5c2-ee5d240307ae)
![Multiple-choice question](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/548a2f2a-ca68-41fd-94fa-150b90662552)
![On-screen keyboard](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/cfc7895a-4911-4e04-8084-7a65f3a555f5)
![Images](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/e12a8648-8b2a-4af0-a4cb-93a29ad61a6b)
![Multiple-choice question](https://github.com/user-attachments/assets/43e4be88-91f8-4575-881a-122bfcb62fa0)
![Spelling corrections](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/9f30fdeb-57c8-4d04-b086-07d211b99ce0)
![Hint button](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/6dbd8da4-e322-4c4b-bd5a-4a744ba5e8e2)
![Dark theme (multiple-choice)](https://github.com/user-attachments/assets/7e918a3c-365d-4f05-917a-ee9066f37644)
![Dark theme (type-in, audio)](https://github.com/user-attachments/assets/9340eff2-eb93-452f-8f5a-51abde3cb86e)

</details>

<details>
<summary>Memrise vs Anki template (side-by-side comparison)</summary>
 <p align="middle">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/9c93a367-1ec6-4818-bb50-d84ccf543c0a" title="Anki" style="width: 43%; box-shadow: 10px 5px 5px black;">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/411a99b6-0e71-4dc5-91b7-cbb3008040a1" title="Memrise" style="width: 48%">
</p>

<p align="middle">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/cbe21000-4519-43ab-b74b-a1c35dd1a363" title="Anki" style="width: 43%">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/7e0d7f4e-34e2-4db9-b034-07f0490ba5f4" title="Memrise" style="width: 48%">
</p>

<p align="middle">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/0aca8cd7-260c-4049-9bc5-1efe9a24e915" title="Anki" style="width: 43%">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/c7446347-0b12-427d-97b8-bdc0b899a715" title="Memrise" style="width: 48%">
</p>
</details>

&nbsp;  

## The support Add-on

The support add-on provides functionality that makes it easier to set-up [multiple-choice cards](#automatically-filling-choice-fields-for-multiple-choice-cards), edit Notes with [alternative answers](#formatting-alternative-answers), and also enables using standard Memrise shortcuts when reviewing Cards on desktop.

### Installation

The automatic install from AnkiWeb is covered in [the Quick Start](#-quick-start) guide. This is a recommended method, as it will also allow receiving the add-on updates automatically.
<details>
  <summary>If you wish to install the add-on manually instead (to make your adjustments to the add-on, without getting them overwritten by the auto-updates, for example):</summary>

> 1. Open Anki "addons21" folder:
> 
>    &nbsp;&nbsp;1.1. In the main Anki window, click `Tools` → `Add-ons` in the menu at the top
>
>    &nbsp;&nbsp;1.2. Click `View Files` in the right bottom corner (without selecting any specific add-on!)
>
>    (or open it directly in explorer: e.g., default path on windows is `C:\Users\%username%\AppData\Roaming\Anki2\addons21`)
>      
> 2. Copy the "Add-on" folder from this repo into the "addons21" folder
> 3. Rename the copied folder appropriately
> 4. Restart Anki

</details>

### Automatically filling choice fields for multiple-choice Cards

> 1. Select several Notes in [the Card Editor](#relevant-anki-windows) (to be used as each other's incorrect answers; if you need to cross-fill all Cards in a certain Deck, for example: click the name of the Deck on the left, then any Card in the appeared table and press `Ctrl + A` to select all)
> 2. Right-click (or go to either `Cards` or `Notes` menus at the top)
> 3. Select `Fill Choices`   
> 4. Specify the Fields in the appeared window accordingly and press `Ok`

### Formatting alternative answers

Just like the original Memrise site, the template supports specifying multiple Alts (alternative translations, spellings, meanings, readings, etc.) for any Field. During reviews, when a Field with Alts is tested on, any one of them will be automatically accepted as an equally correct answer. To show the full range of potential answers, Alts for [the question Field](#question-types) are also displayed on the info screen with a smaller and fainter font, right below the main value (this can also be [enabled for any other Field](#advanced) on either the Front or the Back of a Card). While the add-on is not at all required for setting and using Alts, it makes working with them more convenient. With the add-on [installed](#installation), the Alts in [the Card Editor](#relevant-anki-windows) will be displayed in the same distinct style as they appear on the Cards, and the Editor itself is augmented with two additional tools for marking and clearing Alts, removing any need for editing HTML code manually.

- To add an Alt to a Field which only has the main word:

  &nbsp;1. Move the text cursor to the end of the Field's content
  
  &nbsp;2. Click the "Format as Alt" button on the toolbar (shortcut Alt+A)
  
  &nbsp;3. Proceed to typing Alts, separating them with the pipe character `|` (spaces can be added for readability)

- To convert an existing part of a Field's content into an Alt:

  &nbsp;1. Select the relevant text

  &nbsp;2. Click the "Format as Alt" button on the toolbar (shortcut Alt+A)

- To clean all Alt formatting from a Field:

  &nbsp;1. Put the text cursor anywhere inside the field

  &nbsp;2. Click the "Erase Alt formatting" button on the toolbar (shortcut Alt+X)

The latter only removes the formatting, while keeping the content of Alt sections themselves and merging it back into the main part (this can be used to reset Alt formatting and redo it from scratch if anything goes wrong)

<details>
  <summary>Editing Alts manually:</summary>

>
> 1. In [the Card Editor](#relevant-anki-windows) open HTML code by pressing the `<>` icon in the top right corner of the Field
> 2. To add an Alt section, make a `<div>` element with the "alt" class and the Alts typed put inside and separated with `|`:
>     ```
>     <div class="alt">
>          alt1 | alt2 | alt3 ...
>     </div>
>     ```
> 3. To remove an Alt, simply delete the `<div>`, moving the contents as necessary
> 4. To hide an Alt section from presentation (similarly to how prefixing an Alt with `_` works on Memrise), add the ["off" class](#10-disabling-individual-elements) to the `<div>`
>
</details>

Keep in mind that [Fill Choices](#automatically-filling-choice-fields-for-multiple-choice-cards) function ignores Alts and generates choices based on the main content only. Multiple-choice Cards themselves, however, do account for Alts in [the answer field](5-changing-the-answer-field), making it possible to create questions with several different correct choices.

### Memrise keyboard shortcuts

By default, the desktop Anki app uses the number keys '1–4' to rate Cards from `Again` to `Easy`, while on Memrise, the numbers are used as hotkeys when answering multiple-choice and tapping questions. Anki also interprets both `Enter` and `Space` as rating a Card `Good`. In contrast, the template uses `Enter` for multiple purposes: to flip the Card to the info screen, to autorate a Card `Good` or `Again` and move to the next one (all depending on whether the submitted answer is correct and what is currently displayed on the screen, exactly like Memrise), or playback an audio (when it is selected using `Tab`). Meanwhile, the `Space` is used to show the Card's info screen regardless of whether the submitted answer is correct or not.

To allow the template to use the shortcuts in the Memrise way, the original Anki shortcuts have to be unbound. If you only using Note Types made from the Memrise template, simply installing the support Add-on will make everything work by default — there is no need for any additional adjustments. However, if you are using other Note Types, losing the ability to use Anki shortcuts might be undesirable. There are two ways to deal with this issue:

<details>
  <summary>Modify all the other Note Types to handle key (recommended):</summary>

> This is the recommended way because it preserves all the functionality for both Memrise and non-Memrise Note Types. On the downside, if you have many non-Memrise Card Types, initial setup (and also the modifications for each time a new Card Type is added, e.g., when importing a shared Deck from AnkiWeb) might require a lot of manual work. It also might not be as straightforward if a Note Type that requires modification already uses keyboard events (see instructions below).
>
> If you choose to follow this route:
> 1. Open a non-Memrise Card in [the Card Type editor](#relevant-anki-windows)
> 2. Verify that the Card doesn't define its own keyboard shortcuts by looking for "document.onkeydown" with the search bar in both the Front Template and the Back Template tabs. If nothing is found, it is safe to proceed (this should be true in most cases, in particular, it is for all the stock Anki Note Types). If, however, the function is detected, the code below should be carefully merged with the already present on the Card (feel free to leave a question in [the forum thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233) if you need help with such modification or are in doubt).
> 3. Put the following piece of code at the end of the Front Template:
> 
>    ```
>    <script>
>    document.onkeydown = function (e) {
>    	var ev = window.event || e;
>    	if (ev.key === 'Enter' || (ev.code === 'Space' && document.activeElement.tagName.toLowerCase() !== 'input')) {
>    		try {
>    			pycmd("ans");
>    		} catch(err) {}
>    	}
>    }
>    </script>
>    ```
> 4. Similarly, put the following code at the end of the Back Template:
> 
>    ```
>    <script>
>    document.onkeydown = function (e) {
>    	var ev = window.event || e;
>    	if (ev.key === 'Enter' || ev.code === 'Space') {
>    		try {
>    			pycmd('ease3');
>    		} catch(err) {}
>    	}
>    	if ("1234".includes(ev.key)) {
>    		try {
>    			pycmd('ease' + ev.key);
>    		} catch(err) {}
>    	}
>    }
>    </script>
>    ```
> 5. Repeat the steps for all Card Types
> 6. Click `Save`
> 7. Repeat all the previous steps for each non-Memrise Note Type that needs the Anki shortcuts to be restored

</details>

<details>
  <summary>Revert to default Anki shortcuts:</summary>

> This will restore the default Anki shortcut functionality for all Note Types at once (including the Memrise Note Types, rendering the Memrise shortcuts for answering and auto-rating unusable). This can be done for each key individually, so you can choose to revert the number keys to the default Anki behavior for all Cards, while keeping the `Enter` and `Space` keys for auto-rating answers on Memrise Cards, for example.
>
> To make the adjustment:
> 1. Open Anki Add-on manager: click `Tools` in the top menu of the main window → `Add-ons`
> 2. Select the `Memrise Cards Lt` add-on in the list
> 3. Press `Config` in the bottom left (or double-click the name of the add-on)
> 4. Delete the lines containing the keys you wish to restore
> 5. Click `Ok` and close the Add-on manager
> 6. Restart Anki

</details>

&nbsp;  

## Key concepts (Anki vs Memrise)

When starting with Anki, it is a good idea to get a hold of its key concepts first. You can read about them [in the manual](https://docs.ankiweb.net/getting-started.html#key-concepts), but if you are coming from Memrise (especially if you have edited a community course there), it might be easier to understand those by analogy: 

 - **Note Types = Databases**

    Like Databases on Memrise, Note Types are the highest-order concept in Anki. Generally speaking, each Note Type corresponds to a different Language or a Discipline. To use [the provided Memrise template](#-quick-start) effectively, it's recommended to take one of its Note Types as a base, make a copy for each studied topic, and then customize all the specific properties described below (Fields, Card Types, etc.), adjusting the created Note Types to fit their intended purposes.
   
 - **Fields = Database (Level) columns**

    Also like Databases on Memrise, each Note Type in Anki has its own set of Fields ("Learnable", "Definition", "Audio", ...). On Memrise, each Column had to be set up to one of the three types of content: Text, Audio, or Images. Anki Fields are more general in that regard, and do not inherently differ from each other — any Field can contain any type of content: all kinds of text (plain/rich, bold/italic, colored, formatted, including lists, hyperlinks, math equations, etc.), media (audio, images, and also video), or any mix of the above. It is, nevertheless, still a good idea to keep things organized and split data into different Fields properly: this will keep even large collections of Notes manageable and make the Note Type flexible and easily customizable.
  
 - **Notes = Database words**

    In Anki, after a Note Type is set up, new Notes can be [added manually](https://docs.ankiweb.net/editing.html#adding-cards-and-notes), [imported from a spreadsheet](https://github.com/Eltaurus-Lt/CourseDump2022?tab=readme-ov-file#3-importing-the-spreadsheet), or generated automatically from all kinds of web content, using such tools as [Yomitan](https://yomitan.wiki/). On Memrise, if your Course was designed to test on the same Database Words in different directions (e.g. "word"→"translation", "translation"→"word", etc.), you would have to split the tests into different Levels and then manually append new entry to each Level every time the Database gets updated. Anki generates all needed Cards (tests) automatically based on predefined rules (see Card Types below) each time a new Note is added, so there is no need for any extra steps.

 - **Cards = Level Words**
 
    Memrise terminology might be confusing here because it refers to Database entries and Level entries both as "Words", even though a single Database Word can correspond to several Level "Words" (for tests in different directions). In this regard, Anki Cards serve the same role as Memrise Level Words: presenting separate questions generated (automatically) from the same data (stored as a single Note). This is not limited to testing directions, however, but also encompasses different inputs (enabling Typing and Tapping tests in Memrise Level Column settings) and the addition of Audio Cards (a global course setting on Memrise): each of those gets a separate Card with its own review history, which means that if, for example, you recognize a word in text much better than by hearing it, the associated Audio Cards will start appearing during reviews more often than the text ones.

 - **Cards Types**
 
    As mentioned previously, Card Types are the Anki way of handling the generation of multiple questions per Note, which does not have a single Memrise analogue, but rather serves as a unification of several scattered Memrise settings and provides a level of automation unavailable on Memrise in the first place. Each Card Type represents a certain combination of testing direction, question type, input mode, as well as other similar settings (keyboard layout, theme, etc.), allowing for a detailed configuration of any such combination.
   
   Like Fields, Card Types are a property of Note Types: for each Note made using a certain Note Type, one Card of each Card Type specified in this Note Type's settings gets generated.
 
 - **Decks = Categories/Courses/Levels**

    On Memrise, Words are organized into three levels of hierarchy: the top one is Categories (dropdown menu on a course selection screen), which contain separate Courses, which, in turn, might (or might not) be subdivided into Levels containing individual Words. In Anki, Cards are gathered in Decks, with Decks and Cards acting practically the same way as Folders and Files in a filesystem. Decks can be nested inside each other to make any type of hierarchical structure, including the Memrise three-level system (and any other system with more/less/variable-number-of levels of subdivision). With nested decks, the reviews can be performed for a top-level deck as a whole or for any specific subdeck, if required.
    
    *Notes are not explicitly placed in any Deck or anywhere else in particular; instead, they are accessed only via their respective Cards (each Note always has at least one Card generated from it). Cards made from the same Note can be distributed over different Decks and vice-versa: one deck can contain Cards of different Card- and Note Types (in contrast to Memrise, where Levels can only contain Words with the same set of Fields and same testing direction).


As a recap, and a rule of thumb: **each** Memrise setting has an analogue in Anki, with Level and Level Column settings typically being represented by Card Type settings, while global (Database and Course) settings have their equivalents in the Note Type settings. If you have any further questions, feel free to drop them in [the template forum thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233).

&nbsp;  

## Customization

This section provides detailed instructions for customizing the Memrise template using the desktop Anki app. While it is possible to make all the adjustments in a mobile app as well, the touchscreen interface is not well-suited for any elaborate editing. For this reason, the recommended way is to make all the changes from the desktop app and then [Sync](https://docs.ankiweb.net/syncing.html) to distribute them to mobile apps.

### Relevant Anki windows

Basic ways of accessing the common Anki windows for various customization options. For detailed steps on each action, see the further instructions below.
 
> <details>
> <summary>Card Browser:</summary>
>      
> >
> > To view Cards in your collection, click the `Browse` button in the top center menu. 
> > 
> > Use `Cards`/`Notes` toggle to switch between displaying individual Cards or showing them as a single Note as a whole.
> > Subsets of Cards can be filtered out by using the [Search bar](https://docs.ankiweb.net/searching.html) at the top, or by clicking on any of the filters on the left side, which can be used to show all Cards from a certain Deck or Note Type; by Tag, Flag, or a review data (e.g., Cards that were learned today); or any combination of the above (use `Shift`, `Ctrl`, and `Alt` to combine, intersect, and negate queries).
> </details>
> 
> <details>
> <summary>Note Editor:</summary>
>  
> > Editor is a part of [the Card Browser](#relevant-anki-windows), displayed when a single Card or Note is selected in the table. It allows modifying the content of any of the Note's Fields and, above the Fields, it has a toolbar, providing some basic editing tools.
> 
> </details>
> 
> <details>
> <summary>Note Type manager:</summary> 
> 
> >
> > click `Tools`→`Manage Note Types` in the top menu of the main Anki window
> > 
> > OR
> > 
> > click `Notes`→`Manage Note Types` in the top menu of [the Card Browser](#relevant-anki-windows) window
> >
> </details>
> 
> <details>
> <summary>Field editor:</summary> 
>  
> > select the Note Type in [the Note Type manager](#relevant-anki-windows) and click `Fields` button on the right
> > 
> > OR 
> > 
> > with any Card of the Note Type selected in [the Card Browser](#relevant-anki-windows), click the `Fields` button on [the Note Editor](#relevant-anki-windows) toolbar
> </details>
>  
> <details>
> <summary>Card Type editor:</summary>     
>  
> > select the Note Type in [the Note Type manager](#relevant-anki-windows) and click `Cards` button on the right
> >  
> > OR 
> >  
> > with any Card of the Note Type selected in [the Card Browser](#relevant-anki-windows), click the `Cards` button on [the Note Editor](#relevant-anki-windows) toolbar
> > 
> > You can switch between different Card Types from the dropdown list at the top. Each Card Type consists of the templates for the Front and the Back sides of a card (switched by a radio button on the left, the Styling tab available there as the third radio button option is shared between all Card Types of the selected Note Type)
> </details>

### Editing Note Types

> #### 1. Making a new Note Type based on the Memrise template
> 
>   The Memrise template is designed to be cloned into different Note Types, each of which can then be further customized to better fit each Language and Discipline studied
> 
> <details>
>   <summary>step-by-step:</summary>
>      
> >   1. Open [the Note Type manager](#relevant-anki-windows)
> >   2. Click `Add` button on the left side of the window
> >   3. Select `Clone: Memrise (Lτ) Template v...` for making a standard Note Type or `Clone: Memrise (Lτ) Cloze Template v...` for Cloze Deletion (or any of the `...Preset...` Note Types, if fitting)
> >   4. Click `Ok`
> >   5. Enter the desired name for the new Note Type, like "Memrise (Lτ) Japanese", or "Memrise (Lτ) History" (it is recommended to keep "Memrise (Lτ) " as a prefix, for update purposes and full supporting add-on functionality)
> >   6. Click `Ok`
> >   7. Customize [Fields](#2-renaming-and-reordering-fields) and [Card Types](#editing-card-types) of the created Note Type
> 
> </details>
> 
> #### 2. Renaming and reordering Fields
> 
> The default Field names of the Memrise template can be renamed to better reflect the content of each Note Type (e.g., "Learnable" might be renamed to "Japanese", "Definition" to "English", etc.). 
> 
> <details>
>   <summary>step-by-step:</summary>
>      
> >   1. Open [the Field editor](#relevant-anki-windows)
> >   2. The Fields can be renamed and reordered using the buttons on the right side (reordering fields here only affects their displayed order in [the Note Editor](#relevant-anki-windows), not how they are presented on the Cards during reviews!)
> >   4. Click `Save`
> >   5. Open [the Card Type editor](#relevant-anki-windows)
> >   6. If you renamed a Field, look for `<label>OldFieldName</label>` on the Front and the Back of each Card Type and rename these text labels to match the new name of the Field
> >   7. Click `Save`
> 
> </details>
> 
> #### 3. Adding new Fields
> 
> New Fields can be added to serve as auxiliary background information, or to be used in extra Card Types for more testing directions
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> >   0. [Sync](https://docs.ankiweb.net/syncing.html) all devices to make sure all reviews and other changes made their way to the desktop app (otherwise they will be overwritten by this edit)
> >   1. Open [the Field editor](#relevant-anki-windows)
> >   2. Add new Fields using the buttons on the right side
> >      If you are adding a Field to store choices for Multiple-Choice Cards, make sure to tick the "Exclude from unqualified searches" checkbox on, and (optional) "Collapse by default" (if you don't plan on editing this Field manually often)
> >   3. Click `Save`
> >   4. [Sync](https://docs.ankiweb.net/syncing.html) in the desktop app, selecting `Upload to AnkiWeb`, then Sync on a mobile app, choosing to keep the `AnkiWeb` version of the collection
> >
> >   The newly added Fields will only be visible from [the Card Editor](#relevant-anki-windows) by default (which can be useful by itself for Fields like "Notes" and such). If you want the Cards to show the info from this Field during reviews, it should be inserted into the Card template in the respective place:
> > 
> >   5. Open [the Card Type editor](#relevant-anki-windows)
> >   6. Add the new Field as one of the [extra Fields](#8-extra-fields) on the info screen, or use it as a [question](#4-changing-the-question-field) or an [answer](#5-changing-the-answer-field) on some of the Card Types.
> >   7. Click `Save`
>     
> </details>
> 
> 
> #### 4. Converting Notes to a different Type
> 
> Notes can be converted from one Note Type to another after creation. This can be used to upgrade from [older versions of the template](#5-checking-the-template-version) or to convert Notes initially made from a completely different template into the Memrise template (without recreating the Notes from scratch and without losing Card review history).
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> >   0. Make sure the new Note Type has enough [Fields](#3-adding-new-fields) and [Card Types](#1-making-new-card-types) to keep all needed information from the old Note Type (if not, add them using the linked instructions first)
> >   1. Open [the Card Browser](#relevant-anki-windows)
> >   2. Select the Notes that need to be converted (e.g., if you need to convert all Notes from a certain Deck: click the name of the Deck on the left, then any Card in the appeared table and press `Ctrl + A` to select all)
> >   3. In the top menu, click `Notes`→`Change Note Type`
> >   4. Select the new Note Type in the top dropdown list
> >   5. Set up the mapping between the Fields and Card Types of the old Note Type into the new
> >   6. Click `Save`
> 
> </details>
> 
> #### 5. Checking the template version
> 
> While the shared deck includes the version in the names of each template and preset Note Type, this part can be dropped when renaming a new Note Type or no longer correctly represents the contents of the Note Type if it has been updated. A more robust reference (important for [the support add-on](#the-support-add-on) as well) can be viewed when editing a Note Type in [the Card Type editor](#relevant-anki-windows), at the top of the Styling tab.

### Editing Card Types

> #### 1. Making new Card Types
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> > 0. [Sync](https://docs.ankiweb.net/syncing.html) all devices to make sure all reviews and other changes made their way to the desktop app (otherwise they will be overwritten by this edit)
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. In the `Options` menu at the very top right corner (next to the dropdown list of the Card Types), select `Add Card Type`
> > 3. Click `Yes`, and then `Yes` again, to confirm there are no unsynced changes left on other devices
> > 4. [Rename](#3-renaming-card-types) the created Card Type using the same `Options` menu
> > 5. Set [the question](#4-changing-the-question-field), [the answer](#5-changing-the-answer-field), [the input method](#6-changing-the-input-method), etc.
> > 6. Click `Save`
> > 7. [Sync](https://docs.ankiweb.net/syncing.html) in the desktop app, selecting `Upload to AnkiWeb`, then Sync on a mobile app, choosing to keep the `AnkiWeb` version of the collection
> 
> </details>
> 
> #### 2. Removing existing Card Types
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> > 0. [Sync](https://docs.ankiweb.net/syncing.html) all devices to make sure all reviews and other changes made their way to the desktop app (otherwise they will be overwritten by this edit)
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Select the Type of Cards you wish to remove from the `Card Type: ` dropdown list at the top
> > 3. In the `Options` menu to the right of the `Card Type: ` dropdown list, select `Remove Card Type` (keep in mind that all Cards of this Type and their review history will be permanently deleted! If that is undesired, consider [suspending](https://docs.ankiweb.net/studying.html#editing-and-more) all Cards of this Type instead)
> > 4. Click `Yes`, and then `Yes` again, to confirm there are no unsynced changes left on other devices
> > 5. Click `Save`
> > 6. [Sync](https://docs.ankiweb.net/syncing.html) in the desktop app, selecting `Upload to AnkiWeb`, then Sync on a mobile app, choosing to keep the `AnkiWeb` version of the collection
> 
> </details>
> 
> #### 3. Renaming Card Types
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. In the `Options` menu at the very top right corner (next to the dropdown list of the Card Types), select `Rename Card Type`
> > 3. Enter the desired name for this Type of Cards (e.g., "Listening Comprehension" or "Pronunciation"), and click `Ok`
> > 4. Click `Save`
> 
> </details>
> 
> #### 4. Changing the question Field
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. In the dropdown `Card Type: ` list at the top, select the Type of Cards you wish to modify (you can [add a new Card Type](#-1-making-new-card-types) for this purpose)
> > 3. On the Front side template, find the question section (you can search for "mem-question" using the search bar), and change the name of the Field in double curly brackets to the Field you wish to use as a question instead:
> > 4. Likewise, replace the name of the old question Field at the beginning and the end of the HTML section with the new question Field (keeping the preceding `#` and `/` characters)
> > 
> >     <sub>This tells Anki that the specified Field is essential for the current Type of Cards, so that the Notes, that do not have the required data, will not have Cards of this Type being generated. For example, if you use {{Audio}} Field as the question, some Notes might not have audio recordings, which would make their audio Cards appear empty were it not for this setting.</sub>
> > 5. (Optional) In the same way, replace the old question Field and its text label where they appear on the Back template, if you want the info screen to display it accordingly (Memrise does this for all question Fields except audio). You might also want to adjust the [Extra info](#8-extra-fields) blocks, removing the Field that is now used as the question from there, and making a new extra info block from the old question Field.
> > 6. Click `Save`
> 
> </details>
> 
> #### 5. Changing the answer Field
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. In the dropdown `Card Type: ` list at the top, select the Type of Cards you wish to modify (you can [add a new Card Type](#-1-making-new-card-types) for this purpose)
> > 3. On the Front side template, find the "id=correctAnswer" element and change the name of the Field inside to the Field you wish to use as the answer to the Card:
> > 4. For Multiple-choice Cards, replace, similarly, the Field specified in the "id=choices" element with the Field which will be used as [the source of incorrect choices](#6-changing-the-input-method)
> > 5. For Typing Cards, change the text label inside the "mem-typing" element to correctly reflect the expected input:
> > 6. Replace the name of the old answer Field at the beginning and the end of the HTML section with the new answer Field (keeping the preceding `#` and `/` characters). For Multiple-choice, do the same for the choices Field as well.
> > 
> >     <sub>This tells Anki that the specified Field is essential for the current Type of Cards, so that the Notes, that do not have the required data, will not have Cards of this Type being generated. For example, the Notes with words spelled entirely in kana would not have anything to be learned from a Card Type that is supposed to test on kanji reading. The same goes for multiple-choice Cards, which do not have a single incorrect choice to make the test meaningful.</sub>
> > 7. On the Back side template, replace the old answer Field ("Learnable", by default) and its text label with the new one. You might also want to adjust the [Extra info](#8-extra-fields) blocks, removing the Field that is now used as the answer from there, and putting the old answer Field as a new extra info block.
> > 8. Click `Save`
> 
> </details>
> 
> #### 6. Changing the input method
> 
> <details>
>   <summary>Changing input method to Typing:</summary>
> 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. In the dropdown `Card Type: ` list at the top, select the Type of Cards you wish to convert into Typing Card (you can [add a new Card Type](#-1-making-new-card-types) for this purpose)
> > 3. Change the mode to set on the Front side template to "typing" (you can look for "mode=" using the search bar)
> > 4. Adjust [the on-screen keyboard layout](7-on-screen-keyboard-layout) to match the kind of material being tested in the Card Type
> > 5. [Disable](#10-disabling-specific-elements) the Hint button (search for "HintButton") if needed
> > 6. On the Back side template, [disable](#10-disabling-specific-elements) the spelling diff element (search for "spelldiff") if needed
> > 7. Click `Save`
> 
> </details>
>   
> <details>
>   <summary>Changing input method to Multiple-Choice:</summary>
> 
> > 1. Multiple-choice cards require a source of words (images/equations/...) to be used as incorrect choices in the test. Those choices are stored in separate Fields on each Note (e.g., Field "Choices" in the default setup). If you want a Note Type to have several Multiple-Choice Card Types, first make sure to [create enough Choice Fields](#3-adding-new-fields) first (e.g., "Choices English", "Choices Deutsch", "Image Choices", etc.)
> > 2. Populate the choices Fields. This can be done manually in [the Card Editor](#relevant-anki-windows) (to ensure each Field contains only those choices that can be reasonably mistaken for the correct answer, making the Cards more effective), or [filled automatically](#automatically-filling-choice-fields-for-multiple-choice-cards) (for a quick and easy setup). The choices can also be edited afterwards at any point, e.g., after you fail a typing Card during review, the incorrectly typed answer can be added to the list of choices to make the multiple-choice Card helpful in recognizing it.
> > 3. Open [the Card Type editor](#relevant-anki-windows)
> > 4. In the dropdown `Card Type: ` list at the top, select the Type of Cards you wish to convert into multiple-choice Cards
> > 5. Change the mode to set on the Front side template to "mchoice" (you can look for "mode=" using the search bar)
> > 6. Add or remove "nkeys" from the class list in the same line, depending on whether you'd like the number labels on the buttons to be always shown (default Memrise behavior is achieved by **having** the "nkeys" class)
> > 7. Verify that the correct choice Field is specified in the "id=choices" element
> > 8. Click `Save`
> 
> </details>
> 
> <details>
>   <summary>Changing input method to Tapping:</summary>
> 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. In the dropdown `Card Type: ` list at the top, select the Type of Cards you wish to modify
> > 3. Change the mode to set on the Front side template to "tapping" (you can look for "mode=" using the search bar)
> > 4. Add or remove "nkeys" from the class list in the same line, depending on whether you'd like the number labels on the buttons to be always shown (default Memrise behavior is achieved by **not having** the "nkeys" class)
> > 5. On the Back side template, [disable](#10-disabling-specific-elements) the spelling diff element (search for "spelldiff") if needed
> > 6. Click `Save`
> 
> </details>
> 
> <details>
>   <summary>Changing input method on a Cloze template:</summary>
> 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Since cloze templates do not actually have separate Card Types (the number of Cards generated from a Note depends on the number of clozes it has), all the settings described previously should be implemented based on clozes' ordinal numbers. For example, to make the first card use multiple-choice input, the second one – typing input, the third – tapping, and the fourth – typing again, the following code should be put as the "mode" parameter:
> >     ```
> >     mode="{{#c1}}mchoice{{/c1}}{{#c2}}typing{{/c2}}{{#c3}}tapping{{/c3}}{{#c4}}typing{{/c4}}"
> >     ```
> > 3. If you are using multiple-choice for clozes with different types of content, make sure to make the appropriate number of [choices Fields](#3-adding-new-fields), and set them up in the ["choices" element](#5-changing-the-answer-field) accordingly. For example:
> >     ```
> >     <data id="choices">{{#c1}}{{Choices Years}}{{/c1}}{{#c3}}{{Choices Years}}{{/c3}}{{#c4}}{{Choices Personalities}}{{/c4}}{{#c6}}{{Choices Countries}}{{/c6}}</data>
> >     ```
> > 4. Other parameters, like "nkeys" (see changing input to multiple-choice and tapping), [keyboard](#7-on-screen-keyboard-layout), [theme](#11-selecting-a-theme), etc., can be set up similarly
> > 5. Click `Save`
> > 6. When making a Note with the Cloze Note Type, nested clozes can be used to generate several questions with different input methods for the same clozed parts. For example, putting the following into the cloze Field:
> >     ```
> >     {{c1::{{c2::word}}}} other text {{c3::{{c4::clozed phrase}}}}
> >     ```
> >     with the setup from step 2, will generate four Cards: a multiple-choice Card plus a typing Card for the "word" and a tapping Card plus a typing Card for the "clozed phrase".
> >
> >     Also, clozes do not necessarily have to be numbered sequentially: some can be skipped when needed, and the grouping can vary from Note to Note. For example, using
> >     ```
> >     {{c1:::word}} other text {{c4::clozed phrase}}
> >     ```
> >     will only generate a multiple-choice Card for the "word" and a typing Card for the "clozed phrase", while
> >     ```
> >     other text {{c1::{{c3::{{c4::clozed phrase}}}}}}}
> >     ```
> >     will generate a multiple-choice Card, a tapping Card, and a typing Card for the same "clozed phrase".
> >    
> >     This can be taken advantage of by preparing a Note Type which will contain templates for every possibly useful combination of parameters, and then, on each specific Note, only utilizing those cloze numbers that correspond to the types of questions the Note needs to have generated.
> </details>
> 
> <details>
>   <summary>Enabling LaTeX mode:</summary>
> 
> > [This mode](#latex) should be used whenever the [**answer Field**](#5-changing-the-answer-field) for a Card contains a LaTeX expression (not when the equation is presented as a [question](#question-types) and the Card expects you to answer with the plain-text name of the formula, for example). It functions as a complementary setting to any of the [answer input methods](#input-methods). A typing Card in the LaTeX mode expects the equation source code to be entered during reviews (enclosing `\(` and `\)` can be freely omitted). The typed answer is then automatically converted and compared to the original formula in the Card's answer Field. 
> >
> > Steps to enable the LaTeX mode:
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Add "eq" to the list of classes for the front container element (similarly to the "nkeys" attribute for multiple-choice and tapping inputs above):
> >     ```html
> >     <div class="card-content front eq" ...
> >     ```
> > 3. Repeat this for other Types of Cards if necessary
> > 4. Click `Save`
> 
> </details>
> 
> 
> 
> #### 7. On-screen keyboard layout
> 
> There are two ways of customizing the keyboard layout (analogous to Memrise's "Keyboard Characters" and "predefined keyboard" settings). Either one can be used on its own, or the two can be combined for a more intricate setup. This is a per-Card-Type setting (similar to how on Memrise it is defined per Level Column) so that Cards testing the same Notes in different directions can have separate layouts.
> 
> <details>
>   <summary>Static layout ("Keyboard Characters"):</summary>
> 
> > All static characters will always appear on each Card of this type in the same order they are specified. This can be useful for adding special characters (such as letters with diacritics) to supplement a physical keyboard that doesn’t have them, or for emulating a whole keyboard for a language not installed on your machine. To set it up:
> > 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Enter the desired characters into the "static_keys" setting element at the top of the Front Template, e.g.:
> >    ```html
> >    <setting id="static_keys">äéöüß</setting>
> >    ```
> > 3. Repeat this for other Types of Cards if necessary
> > 4. Click `Save`
> 
> </details>
> 
> <details>
>   <summary>Randomizing characters ("predefined keyboard"):</summary>
> 
> > This setting is supposed to represent the alphabet (or a subset of the most frequently used characters) of a given language / digits (for numeric questions) / common LaTeX characters (for [typesetting formuli](#latex)) / etc. 
> > When at least a single character is defined in this setting, the on-screen keyboard layout will be populated with all characters necessary to spell the correct answer + several unique characters selected from this set (all mixed together and presented in a randomized order to spoil the answer as little as possible). This option can be used to make Cards self-sufficient – every expected answer will be possible to type using on-screen elements alone, without having redundant characters taking up screen space (might be convenient for mobile devices). To set it up:
> > 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Enter the desired characters into the "random_keys" setting element at the top of the Front Template, e.g.:
> >    ```html
> >    <setting id="random_keys">αβγδεζηθικλμνξοπρστυφχψω</setting>
> >    ```
> > 3. Repeat this for other Types of Cards if necessary
> > 4. Click `Save`
> 
> </details>
> 
> Clearing both sets of characters practically disables the on-screen keyboard. To turn the keyboard off without deleting these settings completely (in case they might become useful in the future), use [special "off" class](#10-disabling-individual-elements) instead.
> 
> #### 8. Extra Fields
> 
> On Mermrise, Columns with the "Always Show" property are displayed on the info screen after incorrect answers. In the Anki template, this can be configured not just for each Field but also for each Card Type individually.
>     
> <details>
>   <summary>step-by-step:</summary>
>
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Put the following block of code on the Back Template among other similar-looking blocks (replacing "ExtraField" in all four instances with the name of the Field you are inserting):
> >       ```html
> > 		          {{#ExtraField}}
> > 			          <div class="mem-field no-alts">
> > 			          	<label>ExtraField</label>
> > 			          	<h4>{{ExtraField}}</h4>      
> > 			          </div>
> > 		          {{/ExtraField}}
> >       ```
> > 3. Repeat this for other Types of Cards if necessary
> > 4. Click `Save`
> </details>
>
> The extra Fields on the info screen can also be freely removed, reordered, or copied to the front side in a similar way.
> 
> Additionally, Memrise displays the first extra Field with the "Always Show" property on the front side after an answer is submitted (when viewed in a wide enough window). In this template, the displayed Field can be picked independently of any other conditions (or, conversely, [disabled](#10-disabling-individual-elements)).
>
> <details>
>   <summary>step-by-step:</summary>
>
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Find the following piece of code on the Front Template:
> >       ```html
> >       {{#Extra}}
> >       	<div class="front-extra no-alts">
> >       		<label>Extra</label>
> >       		<span>{{Extra}}</span>
> >       	</div>
> >       {{/Extra}}
> >       ```
> >       (if the template was modified before, some other Field might be in place of "Extra" – the most reliable way to quickly identify the code is to look for "front-extra" using the search bar)
> > 3. Change the "Extra" (or the other Field taking the role) to the name of the Field you would like to see in its place (in all four instances!)
> > 4. Click `Save`
> </details>
> 
> #### 9. Text prompt
> 
> On Memrise, above each question, a bit of text is displayed to indicate what kind of action is expected from a user. Those prompts only depend on the input method of the test, and, as such, are repetitive and not helpful after the first couple of tests. While the template is set up to reproduce the Memrise behavior by default, it leaves a lot of room for customization. You can remove a text prompt altogether or make it more informative by providing instructions specific to each Card Type, such as "Type the pronunciation for the word" or "Pick the composer of the musical piece" (might be especially useful if your Cards are made to be [shared with other people](https://docs.ankiweb.net/contrib)). If your Notes contain very diverse material, the prompt can even be [made into a separate Field](3-adding-new-fields) and set on a Note-to-Note basis.
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> > 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Look for the text of the current prompt on the Front Template ("Pick the correct answer", "Choose the answer you hear", etc.)
> > 3. Rewrite the prompt as necessary (HTML can be used for rich text formatting)
> > 4. Click `Save`
> </details>
>
> #### 10. Disabling individual elements
> 
> The layout for the template is designed to be as flexible as possible. All the elements on the Card can be freely rearranged, copied, and, if necessary, deleted. It is better to use the latter sparingly, however. If there are elements on the Card you don't need and would prefer not to be displayed during reviews, there is a simple non-disruptive way of removing them without losing the original code. This will preserve the opportunity to easily bring any element back at any moment, e.g., when you are cloning a Card Type and need a full template to customize it for the new role.
>
> <details>
>   <summary>step-by-step:</summary>
> 
> > 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Locate the element in the template and add "off" (all lowercase) to the list of its classes. For example, to disable the [on-screen keyboard](7-on-screen-keyboard-layout) as a whole:
> >    ```
> >    <div id="scr-keyboard" class="off">
> >    ```
> >    If the element already has other classes, separate "off" with spaces (order of classes does not matter). For example, to disable the Hint button:
> >    ```
> >    <div id="HintButton" class="membtn off">...
> >    ```
> >    The same goes for elements on the Back side, e.g., the spelling diff element:
> >    ```
> >    <span id="spelldiff" class="off"></span>
> >    ```
> > 3. Repeat this for other Types of Cards if necessary
> > 4. Click `Save`
> 
> </details>   
> 
> #### 11. Selecting a theme
> 
> Each Card Type can be set to be displayed in a certain color theme. This can be used to color-code different types of questions, Note Types made for different subjects, or to select a more pleasing theme than the default "MemRise" for all Cards in general.
> 
> <details>
>   <summary>step-by-step:</summary>
> 
> > 
> > 1. Open [the Card Type editor](#relevant-anki-windows)
> > 2. Similarly to [changing input method](6-changing-the-input-method), locate the front container element on the Front Template (look for "theme=" using the search bar), and put in the name of the selected [theme](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/163?u=eltaurus) as the value for the attribute. For example, to use the "AnkiRise" theme:
> >    ```
> >    <div class="card-content front" theme="AnkiRise" mode="typing">
> >    ```
> > 3. Repeat this for other Types of Cards if necessary
> > 4. Click `Save`
> 
> The full list of available themes and instructions for composing a new one from scratch can be found in [this post](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/163?u=eltaurus). Every theme has both light and dark modes, which are automatically selected depending on the global Anki preference.
> 
> </details>

### Advanced

Additional tips on various customization aspects can be found in these older forum posts:

1. [Setting up the on-screen keyboard, creating Multiple-choice cards](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/54?u=eltaurus) (alternatively: [disabling the on-screen keyboard](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/97?u=eltaurus))
2. [Adding new fields and more card types (testing directions) per note, customizing displayed field labels](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/31?u=eltaurus) ([brief description of the default field roles](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/75?u=eltaurus))
3. [Bigger font size for specified fields](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/90?u=eltaurus), [disabling specific card elements](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/97?u=eltaurus)
4. [Adding Extra fields on the back of a card, changing testing direction](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/6?u=eltaurus)
5. [Showing info screen after correct answers](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/70?u=eltaurus) (alternative: [preventing auto flip on correct answers and displaying extra info on answer screen](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/20?u=eltaurus)), [showing the top extra field on narrow screens](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/81?u=eltaurus) ([additional tweaks](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/83?u=eltaurus))
6. [Changing text colors for the template and card content](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/49?u=eltaurus) ([making a button for coloring text on AnkiDroid](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/51?u=eltaurus))
7. [Making Cloze Deletion cards](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/18?u=eltaurus) (older version of the template)

Any questions regarding other ways of customization and requests for clarification of the above points are always welcome in [the same thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233).



&nbsp;  

## Converting Courses from Memrise

The template is designed to work well with the Memrise community Courses downloaded using [this extension](https://github.com/Eltaurus-Lt/CourseDump2022).
Instructions for importing the downloaded data into Anki using the Memrise template can be found in [this section](https://github.com/Eltaurus-Lt/CourseDump2022?tab=readme-ov-file#-importing-into-anki).

&nbsp;  

## Copyright notice

Copyright © 2023-2025 Eltaurus

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

## Support

If you found this template useful, please consider supporting the development by rating it on AnkiWeb or buying a coffee:

<a href="https://ankiweb.net/shared/info/510199145" target="_blank"><img src="https://i.imgur.com/CoCMk2T.png" alt="Rate on AnkiWeb"  style="height: 37px"></a>
&nbsp;
<a href="https://www.buymeacoffee.com/eltaurus" target="_blank"><img src="https://i.imgur.com/XQvdocZ.png" alt="Buy me a Coffee"  style="height: 37px"></a>
