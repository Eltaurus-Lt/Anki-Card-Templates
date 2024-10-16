# Anki Card Templates

## Memrise Template v4.2

This card template recreates the Memrise interface to make Anki more accessible for ex-Memrise users and everyone else, who finds default Anki cards too intimidating. The functionality includes **type-in** and **multiple-choice** questions (with plain and formatted text, **images**, animated gifs, etc.), **automatic answer grading** with card's **full-info screen** after answer submission, the option to specify **alternative answers** for each card, **audio** questions with interactive buttons, **on-screen keyboard** with the **hint button**, and [more](#themes). It works with every [Anki app on each platform](https://apps.ankiweb.net/) (all **desktop** apps, **Android's** [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki), and [AnkiMobile](https://apps.apple.com/us/app/ankimobile-flashcards/id373493387) for **iOS***):

<sup>*there are some (non-breaking) differences in how the template looks and works on iOS</sup>

![General overview](https://github.com/user-attachments/assets/35bb4ea5-2e2d-42bd-88e5-bbc4207b38da)

### 💡 Quick start

>---
>1. Download the template from [AnkiWeb](https://ankiweb.net/shared/info/510199145) or [release page](https://github.com/Eltaurus-Lt/Anki-Card-Templates/releases/tag/v4.2) and open the `Memrise… .apkg` file with Anki
>2. Use `Memrise (Lτ) Preset […] v4.2` Note Type when making new cards (via **`Add`** → …) or importing a spreadsheet (`File`→`Import` → … [full guide](https://github.com/Eltaurus-Lt/CourseDump2022?tab=readme-ov-file#-importing-into-anki))
>3. On Android also enable `Type answer into the card` (app settings ⚙️ → `Advanced` → `Type answer into the card` → switch **ON**)
>
>Enabling Multiple-Choice cards (Optional):
>
>4. Install [the support addon](https://ankiweb.net/shared/info/884199977) on a desktop Anki:
     `Tools` → `Add-ons` → `Get Add-ons` → Paste "884199977" → `Ok` → Restart Anki
>5. Open **`Browse`** window → Select multiple (**at least two**) Cards in the table 🖱️ → Right Click 🖱️ → `Fill Choices` → `Ok`
>6. To make Multiple-Choice cards available on mobile: **`Sync`** in Anki desktop → **`Sync`** in your mobile Anki app
>---

If you require any help with this, please feel free to leave a comment in [this Anki Forum thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233).
Feedback and feature suggestions are also very much appreciated.

---

### Themes

In addition to replicating the existing Memrise functionality listed at the beginning, the template also implements several features retired from Memrise, such as highlighting **answer corrections** (look for the "You wrote:" line on the screenshots above), or never supported by Memrise, such as **tab-navigation** over a card's interface, ability to view full card's info even when the submitted answer is correct (press `Space`), and a dedicated **Dark theme**. In addition to that, the template has several **other color schemes** to control the appearance of the cards (they are also easily customizable, so everyone can create their personal color scheme):
<!-- fuzzy answer matching | timers, mems... -->

![Color Schemes](https://github.com/user-attachments/assets/5bedf070-0002-405b-bcf3-6210f6321917)

<!-- provides easy ways of customizing a lot of interface attributes and review parameters -->

### LaTeX

One more feature to mention is the **LaTeX support** (in both **type-in** and **multiple-choice** questions). It is enabled separately (LaTeX and Memrise syntax do not mix well), and in type-in questions shows both: the converted equations form of the typed answer and the corrections for typos in its source:

![LaTeX](https://github.com/user-attachments/assets/e8831bf0-a43d-4d78-8b25-ed835c8e21d5)



&nbsp;  
<details>
<summary>More screenshots</summary>
 
![Audio question](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/58fe1cd2-02de-4e16-b5c2-ee5d240307ae)
![Multiple-choice question](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/548a2f2a-ca68-41fd-94fa-150b90662552)
![Images](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/e12a8648-8b2a-4af0-a4cb-93a29ad61a6b) 
![On-screen keyboard](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/cfc7895a-4911-4e04-8084-7a65f3a555f5)
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

### Corrections and changes

This template does not use any of the original Memrise code and is written from scratch with only references to such things as measurements, colors, and fonts. It is designed to have the simplest possible HTML code in order to facilitate further [customization](#Customization). This simplicity also helps avoid many visual bugs and other issues present in the original Memrise layout:

><details>
><summary><b>List of fixed Memrise interface issues</b></summary>
> 
>> All screenshots and recordings are marked by the respective logos:
>> 
>> ![ank_s](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/99799137-a232-42d0-8321-d11cacd00fcd) - **Anki**
>> 
>> ![mem_s](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/f5fd82ba-c612-44a5-8f34-e10c946d680f) - **Memrise**
>&nbsp;
> 
> 1. Elements jumping on answer submission
> 
> ![Submit jitter (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/7c6a4ff3-05f6-4c9a-83ec-288584e65697)
>&nbsp;
>
> 2. Cropped text labels 
>
> ![Fonts cropping (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/2bec6453-353b-4c5c-9cef-b34592bb9457)
>&nbsp;
>
>3. Audio icons blurring on hover
>
> ![Audio blurring (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/7f04ce9e-3ec7-46f6-a418-21354b962c49)
>&nbsp;
> 
> 4. Added keyboard navigation for audio buttons
>
> ![Keyboard navigation (Anki)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/ff7cb131-a234-4b40-b01c-5d7894c382c7)
>&nbsp;
> 
> 5. On-screen keyboard buttons response to clicks:
>
> ![Button clicks (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/954d1852-ca73-43b3-b188-5cc3ec701305)
>&nbsp;
>
> 6. Keyboard character alignment improved (text baseline instead of bounding box center):
>
> ![Keys centering (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/107f4c4f-7a81-4d77-b33b-f76fee53e213)
>&nbsp;
>
> 7. Aliasing artefacts in the corners of buttons:
>
> ![Aliasing (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/85f11f4e-c6ee-429d-b462-149b9d6c907b)
>&nbsp;
>
> 8. The pressed multiple-choice button stays pressed instead of jittering back:
> 
> ![Multiple-choice click (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/74e1c2f1-d4ae-4e13-9210-bc7b33705654)
>&nbsp;
>
> 9. Color scheme is consistent (the graying-out effect is removed, the correct and pressed buttons are recolored to match the good and bad answers in typing questions):
>
> ![Color scheme (Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/1ff3e975-98b7-4267-b492-eecbaa75f149)
>
> ![Color scheme (Anki)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/99f50d23-2d68-4715-b8af-846747b7a07c)
>&nbsp;
>
> 10. Multiple-choice number labels centering:
> 
> ![Multiple-Choice labels (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/be7b7a63-71e5-429e-87f5-e54e34ba0c56)
>&nbsp;
>
> 11. Multiple-choice questions are ensured to have only unique options, unlike their implementation at Memrise:
>
> ![Choice is not an option (Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/532d3665-5dce-4614-a119-9b8908ab3c46)
>
> 12. Audio buttons do not use raster assets, which reduces size, improves image sharpness, and keeps the code self-contained. Also, icons for audio questions do not scale up to comically large sizes on wide monitors.
>
> ![Audio button blurring](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/34a32bdc-e2c4-49c4-92c6-49af8fb71040)
>
></details>

There is also an [interactive online demo](https://codepen.io/Eltaurus/full/mdaMQby) to get a first-hand impression of the functionality before downloading anything (this demo is not updated as regularly as the template itself – only some of the oldest features of the template are represented).

### Customization

*Comprehensive instructions will be posted here when ready.*

Meanwhile, you can find tips on various customization aspects in the following posts:

1. [Setting up the on-screen keyboard, creating Multiple-choice cards](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/54?u=eltaurus) (alternatively: [disabling the on-screen keyboard](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/97?u=eltaurus))
2. [Adding new fields and more card types (testing directions) per note, customizing displayed field labels](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/31?u=eltaurus) ([brief description of the default field roles](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/75?u=eltaurus))
3. [Bigger font size for specified fields](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/90?u=eltaurus), [disabling specific card elements](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/97?u=eltaurus)
4. [Adding Extra fields on the back of a card, changing testing direction](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/6?u=eltaurus)
5. [Showing info screen after correct answers](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/70?u=eltaurus) (alternative: [preventing auto flip on correct answers and displaying extra info on answer screen](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/20?u=eltaurus)), [showing the top extra field on narrow screens](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/81?u=eltaurus) ([additional tweaks](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/83?u=eltaurus))
6. [Changing text colors for the template and card content](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/49?u=eltaurus) ([making a button for coloring text on AnkiDroid](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/51?u=eltaurus))
7. [Making Cloze Deletion cards](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/18?u=eltaurus) (older version of the template)

Any questions regarding other ways of customization and requests for clarification of the above points are always welcome in [the same thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233).

*Please keep in mind, that all changes on the "Styling" tab, as well as the the ones made to JavaScript code, will have to be manually reimplemented when updating to future template versions*

<details>
<summary>🚧</summary>
The main file is `Memrise Templates (Lτ) v2.3.apkg`. Opening it with Anki adds `Memrise Templates (Lτ) v2.3` Note Type, which can then be used to create new cards, change Note Type of existing ones, or import external spreadsheets.
<br><sub>Both, the deck and the single card in it, which are imported with the Note Type, serve only as its holders and can be deleted right away.</sub>

- Memrise vs Anki
  -  Note vs Card
  -  Note Type settings = course settings | Card Type settings = level settings)
- Adding Note Type
- Adding Card Type
  - text and labels
  - changing question | converting to Audio/image
  - changing answer | converting to MCh
  - conditions
- Editing Note Fields (Memrise columns)
  - Adding (New {{Extra}} | {{Notes}})
  - Renaming 
- keyboard
- classes: off | memblob | large
</details>

- Converting from other Note Types

If you have cards in your collection, that were previously created with other templates, and you want to convert them to this one, after downloading and importing the latest `.akpg` deck follow these steps:

1. In your Anki open the Browser by clicking on **`Browse`** button in the top center menu
2. In the left tab scroll down and open the `Note Types` category
3. Click on the name of a Note Type you want to convert
4. Click on any of the cards displayed in the table, then press `Ctrl + A` to select all of them
5. In the top menu go to `Notes` -> `Change Note Type`
6. In the top right dialog of Note Type conversion select the Memrise template you want to use
7. Check the mapping of the Current fields to the New ones
8. Press `Save`

<sub>Same steps can be taken to update from older versions of the Memrise Template. In that case, fields on the left and on the right in step 7 should be identical.</sub>

### Downloading courses from Memrise

The template can be used for Memrise courses imported into Anki with [this extension](https://github.com/Eltaurus-Lt/CourseDump2022)

### Copyright notice

Copyright © 2023-2024 Eltaurus

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

### Support

If you found this template useful, please consider supporting the development by rating it on AnkiWeb or buying a coffee:

<a href="https://ankiweb.net/shared/info/510199145" target="_blank"><img src="https://i.imgur.com/CoCMk2T.png" alt="Rate on AnkiWeb"  style="height: 37px"></a>
&nbsp;
<a href="https://www.buymeacoffee.com/eltaurus" target="_blank"><img src="https://i.imgur.com/XQvdocZ.png" alt="Buy me a Coffee"  style="height: 37px"></a>
