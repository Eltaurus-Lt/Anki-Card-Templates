# Anki Card Templates

## Memrise

This template emulates the Memrise interface for Anki cards, including automatic grading of answers, fuzzy string matching, animated audio buttons, and the extra info screen shown after wrong answers:

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

&nbsp;  
&nbsp;  

This template also avoids layout bugs prominent in the original design, such as:

- Elements jumping on answer submission

![jitter](https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/7c6a4ff3-05f6-4c9a-83ec-288584e65697)

- Cropped fonts and blurring of audio icons on hover
<p align="middle">
  <img src="https://github.com/Eltaurus-Lt/Anki-Card-Templates/assets/93875472/2bc1f512-f796-45a4-a108-0dc117a6e200">
</p>


### Usage

The main file is `Memrise Templates (Lτ) v2.3.apkg`. Opening it with Anki adds `Memrise Templates (Lτ) v2.3` Note Type, which can then be used to create new cards, change Note Type of existing ones, or import external spreadsheets.
<br><sub>Both, the deck and the single card in it, which are imported with the Note Type, serve only as its holders and can be deleted right away.</sub>

### Updating

If you have cards in your collection, that are using an older version of the template, and you want to upgrade them to the latest one, after downloading and importing the current `.akpg` deck follow these steps:

1. In your Anki open the Browser by clicking on `Browse` button in the top center menu
2. In the left tab scroll down and open the `Note Types` category
3. Click on the older version of `Memrise Template (Lτ) ...` you were using before
4. Click on any of the cards displayed in the table, then press `Ctrl + A` to select all of them
5. In the top menu go to `Notes` -> `Change Note Type`
6. In the top right dialog of Notetype conversion select the new version of the Notetype
7. Check the mapping of the Current fields to the New ones (if you didn't change anything in your template, all names should be the same on both sides)
8. Press `Save`

<sub>Same steps can be used to convert existing cards from any other Note Type to this Memrise Template</sub>

### Extra

The template can be downloaded either from this page or from [AnkiWeb](https://ankiweb.net/shared/info/510199145)

Separate parts of the source code for use in your own card templates can be found in the `Source code` folder.

For trying out the template without downloading any files, an interactive demo is available on [CodePen](https://codepen.io/Eltaurus/full/mdaMQby)

The template can be used for Memrise courses imported into Anki with [this extension](https://github.com/Eltaurus-Lt/CourseDump2022)

### Discussion

If you have any questions about the template (how to adapt it for a certain course, modify to create reverse cards, make additional extra fields, change default settings, etc.) or simply want to discuss its further development, please feel free to leave a comment in [this Anki Forums thread](https://forums.ankiweb.net/t/memrise-card-template-support-thread/34233) or in the issues section of this repository.
