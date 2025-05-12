# Anki Card Templates

## Memrise Template v5.0

This Anki [Note Type](#key-concepts-anki-vs-memrise) template recreates the Memrise interface to make Anki more accessible for ex-Memrise users and everyone else who finds the default Anki cards too intimidating. It also restores several features retired from Memrise and adds some that Memrise never had. The functionality covers all types of questions: **text** (including rich text and **cloze deletions**), **images** (including animated gifs), **audio** (with fully interactive buttons), as well as any type of input:  **type-in** (with an **on-screen keyboard**, the **hint button**, and **spelling diffs** shown on the info screen), **multiple-choice** (including images; options can be generated automatically or set up manually), and **tapping**. Answers are **graded automatically** (taking **alternative answers** and optional parts separated by `;` and `()` into account), keeping the option for manual grading as well. The template works with **every** [Anki app on each platform](https://apps.ankiweb.net/) (the **desktop** app, **Android's** [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki), and [AnkiMobile](https://apps.apple.com/us/app/ankimobile-flashcards/id373493387) for **iOS**\*) in **offline mode** and can be used reviewing cards **online** directly from the **AnkiWeb** [website](https://ankiweb.net/decks) in **any browser** without an installed app\*\* (all listed functions work the same way, no exceptions). The template additionally supports **LaTeX** (MathJax) equations, **Dark mode**, multiple **themes**, and a large variety of other customization options.

<sup>*There are some (non-breaking) differences in how the template looks and works on iOS. If anyone wishes to participate in testing to help iron out the remaining discrepancies, please get [in contact](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233)</sup>
<br>
<sup>**A desktop app will still be required for a one-time setup</sup>

![main](https://github.com/user-attachments/assets/13d0b023-a26b-46b0-9485-224c10881e7e)


### 💡 Quick start

>---
>1. Download the template from [AnkiWeb](https://ankiweb.net/shared/info/510199145) or [release page](https://github.com/Eltaurus-Lt/Anki-Card-Templates/releases/tag/v5.0) and open the `Memrise… .apkg` file with Anki
>2. Use `Memrise (Lτ) Preset […] v5.0` Note Type when making new cards (via **`Add`** → …) or importing a spreadsheet (`File`→`Import` → … [full guide](https://github.com/Eltaurus-Lt/CourseDump2022?tab=readme-ov-file#-importing-into-anki))
>3. On Android, additionally enable `Type answer into the card` (app settings ⚙️ → `Advanced` → `Type answer into the card` → switch **ON**)
>
>Generating Multiple-Choice cards (Optional):
>
>4. Install [the support addon](https://ankiweb.net/shared/info/884199977) on a desktop Anki:
     `Tools` → `Add-ons` → `Get Add-ons` → Paste "884199977" → `Ok` → Restart Anki
>5. Open **`Browse`** window → Select several cards in the table 🖱️ → Right Click 🖱️ → `Fill Choices` → `Ok`
>6. To make Multiple-Choice cards available on mobile and AnkiWeb: **`Sync`** Anki desktop to AnkiWeb → **`Sync`** in your mobile Anki app
>---

If you require any help with any of the steps, please feel free to leave a comment in [the Anki Forum thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233).
Feedback and feature suggestions are also very much appreciated.

---

### Question types

Text, audio, images, and LaTeX equations can all be used as a question prompt with any of the basic template versions without any additional setup - the default template automatically adjusts itself to the type of data placed in the "Definition" field. However, to keep your collection organized and easily manageable (and also to add more card types with different directions of testing), it is a good idea to label things properly and place each piece of data into its dedicated field (the instructions for all the necessary steps are provided in the [customization](#Customization) section below).

[Close deletion](https://docs.ankiweb.net/editing.html#cloze-deletion) is a distinct sort of [Note Types](https://docs.ankiweb.net/getting-started.html#note-types) in Anki, used to generate an arbitrary number of cards from the same piece of text. They are made from a separate Note Type template ("Memrise (Lτ) Cloze Template v..." included in the shared deck):




### Input modes




### Themes

**Dark mode**. In addition to that, the template has several **other color themes** to control the appearance of the cards (they are also easily customizable, so everyone can create their personal color scheme):
<!-- fuzzy answer matching | timers, mems... -->

![Color Schemes](https://github.com/user-attachments/assets/5bedf070-0002-405b-bcf3-6210f6321917)

### LaTeX

One more feature to mention is the **LaTeX support** (in both **type-in** and **multiple-choice** questions). It is enabled separately (LaTeX and Memrise syntax do not mix well), and in type-in questions shows both: the converted equations form of the typed answer and the corrections for typos in its source:

![LaTeX](https://github.com/user-attachments/assets/e8831bf0-a43d-4d78-8b25-ed835c8e21d5)


### Other

**spelling diffs**, **tab-navigation**, ability to view full card's info even when the submitted answer is correct (press `Space`), provides ways of customizing interface attributes and review parameters (such as adjusting the maximum number of choices on a multiple-choice card).


&nbsp;  
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
> 4. Added keyboard navigation for audio buttons
>
>> ![Keyboard navigation (Anki)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/ff7cb131-a234-4b40-b01c-5d7894c382c7)
>&nbsp;
> 
> 5. On-screen keyboard buttons respond to clicks:
>
>> ![Button clicks (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/954d1852-ca73-43b3-b188-5cc3ec701305)
>&nbsp;
>
> 6. Keyboard character alignment improved (text baseline instead of bounding box center):
>
>> ![Keys centering (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/107f4c4f-7a81-4d77-b33b-f76fee53e213)
>&nbsp;
>
> 7. Aliasing artefacts in the corners of buttons:
>
>> ![Aliasing (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/85f11f4e-c6ee-429d-b462-149b9d6c907b)
>&nbsp;
>
> 8. The pressed multiple-choice button stays pressed instead of jittering back:
> 
>> ![Multiple-choice click (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/74e1c2f1-d4ae-4e13-9210-bc7b33705654)
>&nbsp;
>
> 9. Color scheme is consistent (the graying-out effect is removed, the correct and pressed buttons are recolored to match the good and bad answers in typing questions):
>
>> ![Color scheme (Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/1ff3e975-98b7-4267-b492-eecbaa75f149)
>>
>> ![Color scheme (Anki)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/99f50d23-2d68-4715-b8af-846747b7a07c)
>&nbsp;
>
> 10. Multiple-choice number labels centering:
> 
>> ![Multiple-Choice labels (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/be7b7a63-71e5-429e-87f5-e54e34ba0c56)
>&nbsp;
>
> 11. Multiple-choice questions are ensured to have unique options, unlike their implementation at Memrise:
>
>> ![Choice is not an option (Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/532d3665-5dce-4614-a119-9b8908ab3c46)
>&nbsp;
>
> 12. Audio buttons do not use raster assets, which reduces size, improves image sharpness, and keeps the code self-contained. Also, icons for audio questions do not scale up to comically large sizes on wide monitors.
>
>> ![Audio button blurring](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/34a32bdc-e2c4-49c4-92c6-49af8fb71040)
>&nbsp;
>
> 13. The keyboard in tapping questions does not jitter on the first input. Also, the tapping buttons visibly respond to key presses:
> 
>> ![Tapping buttons jitter and responsiveness](https://github.com/user-attachments/assets/e6816ff6-e2c6-45f4-a485-e777119c47b8)
>
></details>

There is also an [interactive online demo](https://codepen.io/Eltaurus/full/mdaMQby) to get a first-hand impression of the functionality before downloading anything (this demo is not updated as regularly as the template itself – only some of the oldest features of the template are represented).

### Key concepts (Anki vs Memrise)

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

### Customization

This section provides detailed instructions for customizing the Memrise template using the desktop Anki app. While it is possible to make most of the adjustments in a mobile app as well, the touchscreen interface is not well-suited for any elaborate editing. For this reason, the recommended way is to make all the changes from the desktop app and then [Sunc](https://docs.ankiweb.net/syncing.html) to distribute them to mobile apps.

#### Relevant Anki windows

Basic ways of accessing the common Anki windows for various customization options. For detailed steps on each action, see the further instructions below.
 
<details>
<summary>Card Browser:</summary>
     
>
> To view Cards in your collection, click the `Browse` button in the top center menu. 
> 
> Use `Cards`/`Notes` toggle to switch between displaying individual Cards or showing them as a single Note as a whole.
> Subsets of Cards can be filtered out by using the [Search bar](https://docs.ankiweb.net/searching.html) at the top, or by clicking on any of the filters on the left side, which can be used to show all Cards from a certain Deck or Note Type; by Tag, Flag, or a review data (e.g., Cards that were learned today); or any combination of the above (use `Shift`, `Ctrl`, and `Alt` to combine, intersect, and negate queries).
</details>

<details>
<summary>Note Editor:</summary>
 
> Editor is a part of [the Card Browser](#relevant-anki-windows), displayed when a single Card or Note is selected in the table. It allows modifying the content of any of the Note's Fields and, above the Fields, it has a toolbar, providing some basic editing tools.

</details>

<details>
<summary>Note Type manager:</summary> 

>
> click `Tools`→`Manage Note Types` in the top menu of the main Anki window
> 
> OR
> 
> click `Notes`→`Manage Note Types` in the top menu of [the Card Browser](#relevant-anki-windows) window
>
</details>

<details>
<summary>Field editor:</summary> 
 
> select the Note Type in [the Note Type manager](#relevant-anki-windows) and click `Fields` button on the right
> 
> OR 
> 
> with any Card of the Note Type selected in [the Card Browser](#relevant-anki-windows), click the `Fields` button on [the Note Editor](#relevant-anki-windows) toolbar
</details>
 
<details>
<summary>Card Type editor:</summary>     
 
> select the Note Type in [the Note Type manager](#relevant-anki-windows) and click `Cards` button on the right
>  
> OR 
>  
> with any Card of the Note Type selected in [the Card Browser](#relevant-anki-windows), click the `Cards` button on [the Note Editor](#relevant-anki-windows) toolbar
> 
> You can switch between different Card Types from the dropdown list at the top. Each Card Type consists of the templates for the Front and the Back sides of a card (switched by a radio button on the left, the Styling tab available there as the third radio button option is shared between all Card Types of the selected Note Type)
</details>

#### Editing Note Types

##### 1. Making a new Note Type based on the Memrise template

  The Memrise template is designed to be cloned into different Note Types, each of which can then be further customized to better fit each Language and Discipline studied

<details>
  <summary>step-by-step:</summary>
     
>   1. Open [the Note Type manager](#relevant-anki-windows)
>   2. Click `Add` button on the left side of the window
>   3. Select `Clone: Memrise (Lτ) Template v...` for making a standard Note Type or `Clone: Memrise (Lτ) Cloze Template v...` for Cloze Deletion (or any of the `...Preset...` Note Types, if fitting)
>   4. Click `Ok`
>   5. Enter the desired name for the new Note Type, e.g. `Memrise (Lτ) Japanese`, or `Memrise (Lτ) History` (it is recommended to keep `Memrise (Lτ) ` as a prefix, for update purposes and full supporting add-on functionality)
>   6. Click `Ok`
>   7. Go on to customizing [Fields](#2-renaming-fields-and-adding-new-fields) and [Card Types] of the created Note Type

</details>

##### 2. Renaming Fields and adding new Fields

The default Field names of the Memrise template can be renamed to better reflect the content of each Note Type (e.g. "Learnable" might be renamed to "Japanese", "Definition" to "English", etc.). New Fields can also be added to serve as auxiliary background information, or to be used in extra Card Types for more testing directions

<details>
  <summary>step-by-step:</summary>
     
>   1. Open [the Field editor](#relevant-anki-windows)
>   2. The Fields can be renamed, reordered, or added using the buttons on the right side (reordering fields here only affects their displayed order in [the Note Editor](#relevant-anki-windows), not how they are presented on the Cards during reviews!)
>   3. Click 'Save'
>   4. Open [the Card Type editor](#relevant-anki-windows)
>   5. If you renamed a preexisting Field, look for `<label>OldFieldName</label>` on the Front and the Back of each Card Type and rename those text labels to match the new name of the Field
>   6. If you added a new Field, it should also be inserted somewhere on the Card template to be visible when a Card is reviewed. For example, to add it as another [extra Field] on the info screen, put the code below (changing the "NewFieldName" accordingly) next to the similar blocks on the Back of each Card Type you want the Field to be displayed on:
> 
>       ```html
> 		          {{#NewFieldName}}
> 			          <div class="mem-field no-alts">
> 			          	<label>NewFieldName</label>
> 			          	<h4>{{NewFieldName}}</h4>      
> 			          </div>
> 		          {{/NewFieldName}}
>       ```
>   7. Click 'Save'
    
</details>


##### 3. Converting Notes to a different Type

Notes can be converted from one Note Type to another after creation. This can be used to upgrade from [older versions of the template](#4-checking-the-template-version) or to convert Notes initially made from a completely different template into the Memrise template (without recreating the Notes from scratch and without losing Card review history).

<details>
  <summary>step-by-step:</summary>

>   0. Make sure the new Note Type has enough [Fields](#2-renaming-fields-and-adding-new-fields) and [Card Types](#adding-removing-and-renaming-card-types) to keep all needed information from the old Note Type (if not, add them using the linked instructions first)
>   1. Open [the Card Browser](#relevant-anki-windows)
>   2. Select the Notes that need to be converted (e.g., if you need to convert all Notes from a certain Deck, click the name of the Deck on the left and press `Ctrl + A`)
>   3. In the top menu, click `Notes`→`Change Note Type`
>   4. Select the new Note Type in the top dropdown list
>   5. Set up the mapping between the Fields and Card Types of the old Note Type into the new
>   6. Click `Save`

</details>

##### 4. Checking the template version

While the shared deck includes the version in the names of each template and preset Note Type, this part can be dropped when renaming a new Note Type or no longer correctly represents the contents of the Note Type if it has been updated. A more robust reference (important for the support add-on as well) can be viewed when editing a Note Type in [the Card Type editor](#relevant-anki-windows), at the top of the Styling tab.

#### Editing Card Types

##### 1. Making new Card Types

<details>
  <summary>step-by-step:</summary>

> 0. [Sync](https://docs.ankiweb.net/syncing.html) all devices to make sure all reviews and other changes made their way to the desktop app (otherwise they will be overwritten by this edit)
> 1. Open [the Card Type editor](#relevant-anki-windows)
> 2. In the `Options` menu at the very top right corner (next to the dropdown list of the Card Types), select `Add Card Type`
> 3. Click `Yes`, and then `Yes` again, to confirm there are no unsynced changes left on other devices
> 4. [Rename](#3-renaming-card-types) the created Card Type using the same `Options` menu
> 5. Set [the question](#4-changing-the-question-field), [the answer](#5-changing-the-answer-field), [the input method](#6-changing-the-input-method), etc.
> 6. Click `Save`
> 7. [Sync](https://docs.ankiweb.net/syncing.html) in the desktop app, selecting `Upload to AnkiWeb`, then Sync on a mobile app, choosing to keep the `AnkiWeb` version of the collection

</details>

##### 2. Removing existing Card Types

<details>
  <summary>step-by-step:</summary>

> 0. [Sync](https://docs.ankiweb.net/syncing.html) all devices to make sure all reviews and other changes made their way to the desktop app (otherwise they will be overwritten by this edit)
> 1. Open [the Card Type editor](#relevant-anki-windows)
> 2. Select the Type of Cards you wish to remove from the `Card Type: ` dropdown list at the top
> 3. In the `Options` menu to the right of the `Card Type: ` dropdown list, select `Remove Card Type` (keep in mind that all Cards of this Type and their review history will be permanently deleted! If that is undesired, consider [suspending](https://docs.ankiweb.net/studying.html#editing-and-more) all Cards of this Type instead)
> 4. Click `Yes`, and then `Yes` again, to confirm there are no unsynced changes left on other devices
> 5. Click `Save`
> 6. [Sync](https://docs.ankiweb.net/syncing.html) in the desktop app, selecting `Upload to AnkiWeb`, then Sync on a mobile app, choosing to keep the `AnkiWeb` version of the collection

</details>

##### 3. Renaming Card Types

<details>
  <summary>step-by-step:</summary>

> 1. Open [the Card Type editor](#relevant-anki-windows)
> 2. In the `Options` menu at the very top right corner (next to the dropdown list of the Card Types), select `Rename Card Type`
> 3. Enter the desired name for this Type of Cards (e.g., "Listening Comprehension" or "Pronunciation"), and click `Ok`
> 4. Click `Save`

</details>

##### 4. Changing the question Field

<details>
  <summary>step-by-step:</summary>

> 1. Open [the Card Type editor](#relevant-anki-windows)
> 2. In the dropdown `Card Type: ` list at the top, select the Type of Cards you wish to modify
> 3. On the Front side template, find the question section (you can search for "mem-question" using the search bar), and change the name of the Field in double curly brackets to the Field you wish to use as a question instead:
> 4. Likewise, replace the name of the old question Field at the beginning and the end of the HTML section with the new question Field (keeping the preceding `#` and `/` characters)
> 
>     <sub>This tells Anki that the specified Field is essential for the current Type of Cards, so that the Notes, that do not have the required data, will not have Cards of this Type being generated. For example, if you use {{Audio}} Field as the question, some Notes might not have audio recordings, which would make their audio Cards appear empty if it were not for this setting.</sub>
> 5. (Optional) In the same way, replace the old question Field and its text label where they appear on the Back template, if you want the info screen to display it accordingly. You might also want to adjust the [Extra info](#8-extra-fields-displayed-on-the-info-screen) blocks, removing the Field that is now used as the question from there, and making a new extra info block from the old question Field.
> 6. Click `Save`

</details>

##### 5. Changing the answer Field

<details>
  <summary>step-by-step:</summary>

> 1. Open [the Card Type editor](#relevant-anki-windows)
> 2. In the dropdown `Card Type: ` list at the top, select the Type of Cards you wish to modify
> 3. On the Front side template, find the "id=correctAnswer" element and change the name of the Field inside to the Field you wish to use as the answer to the Card:
> 4. For Multiple-choice Cards, replace, similarly, the Field specified in the "id=choices" element with the Field which will be used as [the source of incorrect choices](#6-changing-the-input-method)
> 5. For Typing Cards, change the text label inside the "mem-typing" element to correctly reflect the expected input:
> 6. Replace the name of the old answer Field at the beginning and the end of the HTML section with the new answer Field (keeping the preceding `#` and `/` characters). For Multiple-choice, do the same for the choices Field as well.
> 
>     <sub>This tells Anki that the specified Field is essential for the current Type of Cards, so that the Notes, that do not have the required data, will not have Cards of this Type being generated. For example, the Notes with words spelled entirely in kana would not have anything to be learned from a Card Type that is supposed to test on kanji reading. The same goes for multiple-choice Cards, which do not have a single incorrect choice to make the test meaningful.</sub>
> 7. On the Back side template, replace the old answer Field ("Learnable", by default) and its text label with the new one. You might also want to adjust the [Extra info](#8-extra-fields-displayed-on-the-info-screen) blocks, removing the Field that is now used as the answer from there, and putting the old answer Field as a new extra info block.
> 8. Click `Save`

</details>

🚧🚧🚧

##### 6. Changing the input method

<details>
  <summary>Changing input method to Typing:</summary>

  0. Open the [Card template editor] for the version of the template you are trying to modify
</details>
  
<details>
  <summary>Changing input method to Multiple-Choice:</summary>

  0. Open the [Card template editor] for the version of the template you are trying to modify
</details>

<details>
  <summary>Changing input method to Tapping:</summary>

  0. Open the [Card template editor] for the version of the template you are trying to modify
</details>

<details>
  <summary>Changing input method on a Cloze template:</summary>

  0. Open the [Card template editor] for the version of the template you are trying to modify
</details>

<details>
  <summary>Enabling Math mode:</summary>

  0. Open the [Card template editor] for the version of the template you are trying to modify
</details>

##### 7. On-screen keyboard layout

##### 8. Extra Fields displayed on the info screen

##### 9. Prompt and the frontside Extra field

##### 10. Disabling specific elements

Things like the on-screen keyboard, the hint button, spelling diffs, and anything else

##### 11. Selecting a theme

#### Advanced

Additional tips on various customization aspects can be found in these older forum posts:

1. [Setting up the on-screen keyboard, creating Multiple-choice cards](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/54?u=eltaurus) (alternatively: [disabling the on-screen keyboard](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/97?u=eltaurus))
2. [Adding new fields and more card types (testing directions) per note, customizing displayed field labels](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/31?u=eltaurus) ([brief description of the default field roles](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/75?u=eltaurus))
3. [Bigger font size for specified fields](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/90?u=eltaurus), [disabling specific card elements](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/97?u=eltaurus)
4. [Adding Extra fields on the back of a card, changing testing direction](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/6?u=eltaurus)
5. [Showing info screen after correct answers](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/70?u=eltaurus) (alternative: [preventing auto flip on correct answers and displaying extra info on answer screen](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/20?u=eltaurus)), [showing the top extra field on narrow screens](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/81?u=eltaurus) ([additional tweaks](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/83?u=eltaurus))
6. [Changing text colors for the template and card content](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/49?u=eltaurus) ([making a button for coloring text on AnkiDroid](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/51?u=eltaurus))
7. [Making Cloze Deletion cards](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233/18?u=eltaurus) (older version of the template)

Any questions regarding other ways of customization and requests for clarification of the above points are always welcome in [the same thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233).



### Downloading courses from Memrise

The template can be used for Memrise courses imported into Anki with [this extension](https://github.com/Eltaurus-Lt/CourseDump2022)

### Copyright notice

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

### Support

If you found this template useful, please consider supporting the development by rating it on AnkiWeb or buying a coffee:

<a href="https://ankiweb.net/shared/info/510199145" target="_blank"><img src="https://i.imgur.com/CoCMk2T.png" alt="Rate on AnkiWeb"  style="height: 37px"></a>
&nbsp;
<a href="https://www.buymeacoffee.com/eltaurus" target="_blank"><img src="https://i.imgur.com/XQvdocZ.png" alt="Buy me a Coffee"  style="height: 37px"></a>
