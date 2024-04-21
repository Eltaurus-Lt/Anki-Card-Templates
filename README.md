# Anki Card Templates

## Memrise

This card template replicates the Memrise interface to make Anki more accessible for ex-Memrise users. The functionality includes **typing-in** and **multiple-choice** questions, **automatic answer grading** with the **info screen** on failed cards, **image** and **audio** cards (buttons fully animated), **on-screen keyboard** with the **hint button**, and more. It works on **desktop** as well as in **mobile app***:
<!-- fuzzy answer matching, spelling corrections, tab navigation | timers, mems... -->
<sub>*tested on Android (AnkiDroid app), some features might not fully function on iPhones (AnkiMobile app)</sub>

![desk1](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/822a733c-ac84-4a16-8b86-f0c121b4dc67)
![and1](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/b6877ffd-e9c6-45eb-9c31-32afe443348d)
![desk2](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/e5797c48-01b7-40a4-bd27-47ab4999a4fd)
![and2](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/87ea2dec-0bbb-4056-9b7b-de4a9e5b36bb)
![desk3](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/b67a861f-2aba-45f0-befd-14f0aa14ce31)
![and3](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/5e912b59-38ef-4e38-9ae5-a6bbe52e1e65)


&nbsp;  


<details>
<summary>More comparison screenshots</summary>
 <p align="middle">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/9c93a367-1ec6-4818-bb50-d84ccf543c0a" title="Anki" style="width: 43%">
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

This template does not use any of the original Memrise code and is written from scratch with only references to such things as measurements, colors, and fonts. It is designed to have the simplest possible HTML code in order to facilitate further [customization](#Customization), which also helps avoid many visual bugs and present in the original Memrise layout:





><details>
><summary><b>Memrise vs Anki template</b></summary>
> 
>> All screenshots and recordings are marked by the respective logos:
>> 
>> ![ank_s](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/99799137-a232-42d0-8321-d11cacd00fcd) - **Anki**
>> 
>> ![mem_s](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/f5fd82ba-c612-44a5-8f34-e10c946d680f) - **Memrise**
>&nbsp;
> ### List of corrected Memrise issues:  
> 
> 1. Elements jumping on answer submission
> 
> ![Submit jitter (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/7c6a4ff3-05f6-4c9a-83ec-288584e65697)
>&nbsp;
>
> 2. Cropped fonts 
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
> 7. Aliasing artifacts in the corners of buttons:
>
> ![Aliasing (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/85f11f4e-c6ee-429d-b462-149b9d6c907b)
>&nbsp;
>
> 8. The pressed multiple-choice button stays pressed instead of jittering back:
> 
> ![Multiple-choice click (Anki vs Memrise)](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/74e1c2f1-d4ae-4e13-9210-bc7b33705654)
>&nbsp;
>
> 9. Color scheme is consistensy (the graying-out effect is removed, the correct and pressed buttons are recolored to match the good and bad answers in typing questions):
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
></details>

There is also an [interactive online demo](https://codepen.io/Eltaurus/full/mdaMQby) to get a first-hand impression of the functionality without downloading anything.

### 💡 Quick start

>---  
>1. Open `Memrise Templates (Lτ) v3.32.apkg` with Anki
>2. Use `Memrise (Lτ) Preset [Translation+Listenting | Typing+MultipleChoice] v3.32` Note Type when making new cards, or [importing courses from Memrise](https://github.com/Eltaurus-Lt/CourseDump2022?tab=readme-ov-file#importing-into-anki)
>
>Enabling Multiple-Choice cards (Optional):
>
>3. Instal the support addon in desktop Anki:
     `Tools` → `Add-ons` → `Get Add-ons` → Paste "884199977" → `Ok` → Restart Anki
>4. Open **`Browse`** window → Select Cards in the table -> Right Click 🖱️ → `Fill Choices` → `Ok`
>5. To make Multiple-Choice cards available in the app: **`Sync`** in Anki desktop → **`Sync`** in AnkiDroid
>---

### Customization

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

- Converting Note type

If you have cards in your collection, that are using an older version of the template, and you want to upgrade them to the latest one, after downloading and importing the current `.akpg` deck follow these steps:

1. In your Anki open the Browser by clicking on `Browse` button in the top center menu
2. In the left tab scroll down and open the `Note Types` category
3. Click on the older version of `Memrise Template (Lτ) ...` you were using before
4. Click on any of the cards displayed in the table, then press `Ctrl + A` to select all of them
5. In the top menu go to `Notes` -> `Change Note Type`
6. In the top right dialog of Notetype conversion select the new version of the Notetype
7. Check the mapping of the Current fields to the New ones (if you didn't change anything in your template, all names should be the same on both sides)
8. Press `Save`

<sub>Same steps can be taken to update the version of the Memrise Template</sub>
</details>

### Extra

The template can be downloaded either from this page or from [AnkiWeb](https://ankiweb.net/shared/info/510199145)

The template can be used for Memrise courses imported into Anki with [this extension](https://github.com/Eltaurus-Lt/CourseDump2022)

### Discussion

If you have any questions about the template (how to adapt it for a certain course, modify to create reverse cards, make additional extra fields, change default settings, etc.) or simply want to discuss its further development, please feel free to leave a comment in [this Anki Forums thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233) or in the issues section of this repository.
