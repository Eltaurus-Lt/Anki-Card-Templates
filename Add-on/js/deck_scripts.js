// This script is part of the Lt-Cards Add-on for Anki.
// Source: github.com/Eltaurus-Lt/Anki-Card-Templates
// 
// Copyright © 2026 Eltaurus
// Contact: 
//     Email: Eltaurus@inbox.lt
//     GitHub: github.com/Eltaurus-Lt
//     Anki Forums: forums.ankiweb.net/u/Eltaurus
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// See the GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.

function extractLevelN(namestring) {
  return /^L0*(\d+)\./.exec(namestring)?.[1];
}

function stripNumbering(namestring) {
  return namestring.replace(/^L?(\d+\.)+\s*/g, "");
}

function retry(imgL) {
  const extList = configLt["thumbnail extensions"] || ['jpg', 'png', 'jpeg'];
  const currentExt = imgL.src.split('.').pop();
  const i = extList.indexOf(currentExt) + 1;
  if (i < extList.length) {
    imgL.src = imgL.src.slice(0, -currentExt.length) + extList[i];
  } else {
    imgL.remove();
  }
}
function thumbHTML(deckname) {
  return `<img src='_thumb_${deckname}.jpg' height="0" width="0" onload="this.classList.add('deckthumb');this.removeAttribute('height');this.removeAttribute('width')" onerror="retry(this)"\>`;
}

// get add-on config
const configLt = JSON.parse(document.getElementById('lt-config')?.getAttribute('data-config') || "{}");
window.addEventListener('DOMContentLoaded', function () {

  // main deck screen
  document.querySelectorAll('a.deck').forEach(deckL => {
    const deckname = deckL.innerText;
    const strippedName = stripNumbering(deckname);
    const levelN = extractLevelN(deckname);
    if (levelN) {
      deckL.classList.add('mem-level');
      deckL.setAttribute("data-levelN", levelN);
      deckL.innerHTML = strippedName;
    } else {
      if (strippedName !== deckname) {
        deckL.classList.add('numbered');
      }
      deckL.innerHTML = thumbHTML(strippedName) + strippedName;
    }
  });

  // overview
  const headerL = document.querySelector('body > center > h3');
  if (headerL) {
    let isNumbered = false;
     headerL.innerHTML = headerL.innerText.split("::").map(subname => {
      const levelN = extractLevelN(subname);
      const strippedName = stripNumbering(subname);
      isNumbered = isNumbered || (strippedName !== subname);
      if (levelN) {
        return `<span class='sublevel' data-levelN="${levelN}">${strippedName}</span>`;
      } else {
        return `${thumbHTML(strippedName)}<span class='subdeck'>${strippedName}</span>`;
      }
    }).join('<span class="divider">::</span>');
    if (isNumbered) {
      headerL.classList.add('numbered');
    }
  }
});