function extractLevelN(namestring) {
  return /^L0*(\d+)\./.exec(namestring)?.[1];
}

function stripNumbering(namestring) {
  return namestring.replace(/^L?(\d+\.)+\s*/g, "");
}

function retry(imgL) {
  if (imgL.src.endsWith('.jpg')) {
    imgL.src = imgL.src.slice(0,-4) + '.png';
  } else {
    imgL.remove();
  }
}
function thumbHTML(deckname) {
  return `<img src='_thumb_${deckname}.jpg' class="deckthumb" onerror="retry(this)"\>`;
}

window.addEventListener('load', function () {
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