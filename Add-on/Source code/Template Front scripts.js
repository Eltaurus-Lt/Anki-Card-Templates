<!--
This section (up until the line containing "End of code by Eltaurus") is part of the Anki Card Type template.
Source: github.com/Eltaurus-Lt/Anki-Card-Templates

Copyright (C) 2023-2025 Eltaurus
Contact: 
    Email: Eltaurus@inbox.lt
    GitHub: github.com/Eltaurus-Lt
    Anki Forums: forums.ankiweb.net/u/Eltaurus

This template is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This template is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this template. If not, see <http://www.gnu.org/licenses/>.

You are free to use this template to create your own Anki cards and decks, modify the code, and openly share the derivative works, provided that this copyright notice and similar notices in other parts remain intact (as covered by section 7b of the GPLv3 license). 
Clarification: The copyright in this notice applies only to the above-stated section of the code. In particular, it does not extend to data contained within fields of Anki cards or any media files included in Anki decks created using this template. It also does not cover any scripts or HTML code that may be added to this HTML file (Front Template screen) by creators of derivative cards/templates. Creators are encouraged to add their own copyright statements alongside their code in a similar fashion.
-->

<script>
//determine card side
wrap = document.getElementById('backwrap');
isFrontSide = !wrap;
if (isFrontSide) {
  console.log("------------- card -------------");
} else {
  console.log(" - - - - - -  back  - - - - - - ");
}
</script>

<script>
//determine input flags
cardContF = document.querySelector(".card-content.front");
Qmode = cardContF.getAttribute("mode") || (cardContF.classList.contains("mch") ? "mchoice" : "typing");
isMathJax = cardContF.classList.contains("eq");
</script>

<script>
//determine platform
platform = '';
if (!!document.getElementById('qa_box')) {
  platform = 'ankiweb';
} else if (!document.documentElement.classList.contains("mobile")) {
	platform = 'desk';
} else if (document.documentElement.classList.contains("android")) {
	//var jsApiContract = { version: "0.0.3", developer: "eltaurus@inbox.lt" };
	//var api = new AnkiDroidJS(jsApiContract);
	platform = 'android';
} else {
	platform = 'ios';
}
console.log("platform: ", platform);
</script>

<script>
//prevent ankiweb's default autorate with number keys
if (platform === 'ankiweb' && !window.awKeyBlocker) {
  awKeyBlocker = document.addEventListener("keyup", (event) => {
    if (!"1234".includes(event.key)) return;
    event.stopImmediatePropagation();
    event.preventDefault();
  }, true);
}
//prevent ankiweb from autofocusing "show answer" and rate buttons
if (platform === 'ankiweb' && !window.observer) {
  window.observer = new MutationObserver(() => {
    document.querySelectorAll('[autofocus]').forEach((L) => {
      L.removeAttribute('autofocus');
      L.blur();
    });
  });

  observer.observe(document.body, { childList: true, subtree: true });
};

//ankiweb rate function
function awRate(ease) {
	const ankiwebButtons = document.querySelectorAll('.btn.btn-primary.btn-lg');
	if (ankiwebButtons.length === 4) {
		ankiwebButtons[ease - 1].click();
	} else {
		console.log(`incorrect number of answer buttons (&{ankiwebButtons.length})`);
	}
}
</script>

<script>
//block key presses immediately after page loading
function putOnCD() {
  ongcd = true;
  setTimeout(()=>{ongcd = false}, 400);
}
if (isFrontSide) putOnCD();
</script>

<script>
function htmlEscape(string) {
  return string.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll("'", '&#39;').replaceAll('"', '&quot;');
}

function htmlUnEscape(string) {
  return string.replaceAll('&lt;', '<').replaceAll('&gt;', '>').replaceAll('&#39;', "'").replaceAll('&quot;', '"').replaceAll('&amp;', '&');
}

function ansCleanUp(ansString) {
  return ansString?.replaceAll("&nbsp;", " ")?.replaceAll(" \n", " ").replaceAll("\n ", " ").replaceAll("\n", " ")?.trim();
}

function preTokenize(ans) {
  return ans.replaceAll('?',' ?').replace(/\u0020+/g, ' ');
}
</script>

<script>
//elements
typeAns = document.getElementById('typeans');
tapAnsArea = document.querySelector(".mem-typing");
screenKeyboard = document.getElementById('scr-keyboard');
hintButton = document.getElementById('HintButton');
embeddedAudios = [...document.querySelectorAll('audio')];
</script>

<script>
function audioAnimation(aL) {
	if (!aL) return;
	aL.classList.remove('loading');
	aL.classList.remove('failed');
	document.querySelectorAll('.card-content a.replay-button').forEach((b) => {
		b.classList.remove('active');
	});
	aL.classList.add('active');
	aL.classList.remove('pulse');
	void aL.offsetHeight;
	aL.classList.add('pulse');
}

function replayEmbedded(i, aL, retry = 50) { //for embedded audio tags (ankiweb)
  if (!embeddedAudios[i]) return;
  embeddedAudios.forEach(audioL => audioL.pause());
  embeddedAudios[i].currentTime = 0;
  embeddedAudios[i].play().then(()=>{
    audioAnimation(aL);
  }).catch((err) => {
    if (err.name === "NotAllowedError" || err.message.includes("user didn't interact")) {
      console.warn('awaits interaction');

      const interactions = ["click", "keydown"];
      const handler = ()=> {
        console.log('interaction detected');
        interactions.forEach(evt => document.removeEventListener(evt, handler));
        replayEmbedded(i, aL, retry - 1);
      }
      interactions.forEach(event => {
          document.addEventListener(event, handler);
      });

    } else {
      console.warn(`playback error (${err})`);
      aL.classList.add('loading');
      if (retry > 0) {
        setTimeout(()=>replayEmbedded(i, aL, retry - 1), 100); 
      } else {
        console.warn('max retry attempts exceeded');
        aL.classList.remove('loading');
        aL.classList.add('failed');
      }
    }
  });
}

//embedding audio buttons
embeddedAudios.forEach((audioL, i) => {
  const replayButtonHTML = `
    <a class="replay-button soundLink embedded" onclick="replayEmbedded(${i}, this)" href="../#">
      <svg class="playImage" viewBox="0 0 64 64" version="1.1">
        <circle cx="32" cy="32"></circle>
        <path></path>
      </svg>
    </a>
  `;
  
  const tempL = document.createElement('div');
  tempL.innerHTML = replayButtonHTML.trim();
  
  audioL.parentNode.insertBefore(tempL.firstChild, audioL.nextSibling);

  //move audio tag outside
  cardContF.appendChild(audioL);
  audioL.classList.add('off');
});

</script>

<script>
//MathJax
function MJwrap(latexString) {
  if ((latexString.startsWith("\\\x28") && latexString.endsWith("\\\x29")) || !latexString) {
    return latexString;
  }
  return "\\\x28" + latexString + "\\\x29";
}

function MJunwrap(latexString) {
  if (latexString.startsWith("\\\x28") && latexString.endsWith("\\\x29")) {
    return latexString.slice(2, -2);
  }
  return latexString;
}

async function MJconvert(latexString) {
  if (!window.MathJax) {
    console.log("MathJax not found");
    return latexString;
  }
  if (latexString.includes("mjx-container")) {
    return latexString;
  }
  const latexL = document.createElement('div');
  latexL.innerHTML = MJwrap(latexString);
  await MathJax.typesetPromise([latexL]);

  return latexL.innerHTML;
}

async function cfWithMathJax(sQ, sA) {
  const mathJaxRegex = /<mjx-container[^>]*>/g;

  return sQ.replace(mathJaxRegex, '') === sA.replace(mathJaxRegex, '') || (await MJconvert(sQ)).replace(mathJaxRegex, '') === sA.replace(mathJaxRegex, '') || (await MJconvert(sQ)).replace(mathJaxRegex, '') === (await MJconvert(sA)).replace(mathJaxRegex, '');
}
</script>

<script>
function storeAnswer(ans = "") {
	if (!ans && typeAns) {ans = typeAns.value};
	sessionStorage.setItem("userAnswer", ans);
}

if (isFrontSide) {
	storeAnswer("");
}
</script>

<script>
//determine the correct answer
corrAnsL = document.getElementById('correctAnswer');
</script>
<script>
//cloze
clozes = corrAnsL.querySelectorAll(".cloze");
if (clozes.length > 0) {
  corrAnsL.innerHTML = [...clozes].map(L => L.getAttribute("data-cloze")).join(Qmode !== "tapping" ? ", " : " ");
  let inactCloze = corrAnsL.querySelector("span.cloze-inactive");
  while (inactCloze) { // remove inactive nested clozes
    const frag = document.createDocumentFragment();
    while (inactCloze.firstChild) { frag.appendChild(inactCloze.firstChild); }
    corrAnsL.replaceChild(frag, inactCloze);
    inactCloze = corrAnsL.querySelector("span.cloze-inactive");
  }
}
</script>
<script>
corrAns = ansCleanUp(Qmode === "tapping" ? corrAnsL?.innerHTML.replaceAll("　", " ").replaceAll("&nbsp;", "　") : corrAnsL?.innerHTML) || ""; //including alts

//extract primary, excluding alts
try {
	const tempL = document.createElement('div');
	tempL.innerHTML = corrAns;
	tempL.querySelectorAll('[part="alt"], .alt').forEach((L) => {L.remove();});
	corrAns = (Qmode !== "mchoice") ? tempL.innerText : tempL.innerHTML;
	corrAns = corrAns.trim();
	tempL.remove();
} catch (err) {}

inlnAlts = corrAns.split(/[;；]/).map(ansCleanUp);

hintAns = ansCleanUp(inlnAlts[0]);
if (isMathJax) {
	hintAns = MJunwrap(hintAns);
	if (Qmode === "mchoice") {
		inlnAlts = [corrAns]; //otherwise is split at ';' in '&gt;', '&lt;', etc.
	}
}

//determine alt answers
partAlts = [];
try {
	const altsString = [...corrAnsL.querySelectorAll('[part="alt"], .alt')].map(L => L.innerText).join('|');
	partAlts = altsString ? altsString.split('|').map(ansCleanUp) : [];
} catch (err) {}

allAlts = [...inlnAlts, ...partAlts];
</script>

<script>
//consts
keysString = document.getElementById('static_keys')?.innerText || "";
fillerString = document.getElementById('random_keys')?.innerText || "";
choices = document.getElementById('choices')?.innerHTML.split('|').map(ansCleanUp) || '';
</script>

<script>
//keyboard navigation
tabSelected = null;
document.onkeyup = function (e) {
	var ev = window.event || e;
	
	if (ev.key === 'Tab') {
		tabSelected = document.activeElement;
	}
}

document.onkeydown = function (e) {
	if (window.ongcd) {console.log("on cd");return;}
	var ev = window.event || e;

	if (ev.key === 'Enter' && (tabSelected !== document.activeElement || tabSelected?.id === 'typeans')) {
		//last action was NOT selecting element with Tab -> Enter=flip (prevent audio activation)
		if (document.activeElement.matches('a.replay-button.soundLink')) {
			document.activeElement.blur();
		}
		if (!isFrontSide) {
			if (flipBtn && flipBtn.onclick) {
				flipBtn.onclick();
			}
		} else {
			flipToBack();
		}
	}

	if (!isFrontSide && ev.code === 'Space') {
		if (wrap.classList.contains("backside")) {
			return;
		}
		e.preventDefault();
		MemFlip(true);
	}

	if (isFrontSide && "1234567890".includes(ev.key) && (Qmode === "mchoice" || Qmode === "tapping")) {
		if (cardContF && !cardContF.classList.contains("nkeys")) {
			cardContF.classList.add("nkeys");
		} else {
			let numkey = parseInt(ev.key);
			if (numkey == 0) {numkey = 10};
			if (numkey <= keyboardButtons.length) {
				if (Qmode === "mchoice" || !keyboardButtons[numkey - 1].classList.contains("pressed")) {
					keyboardButtons[numkey - 1].onclick();
				} else {
					untapKey(numkey);
				}
			}
		}
	}

	if (!isFrontSide && "1234".includes(ev.key)) {
		if (platform === "desk") {
			pycmd('ease' + ev.key);
		} else if (platform === "ankiweb") {
			awRate(ev.key);
		}
	}
}
</script>

<script>
function androidAutoplay(chosenAudio, retry = 100) {
	if (retry <= 0) {
		chosenAudio.classList.add('failed');
		return;
	}
	if (window.open(chosenAudio.href) !== null) { // audio played successfully
		audioAnimation(chosenAudio);
	} else { // audio is not yet available
		chosenAudio.classList.add('loading');
		setTimeout(()=>{
			androidAutoplay(chosenAudio, retry - 1);
		}, 10);
	}
}
</script>

<script>
//Audio buttons animation
audioButtonsFront = cardContF.querySelectorAll('a.replay-button');

audioButtonsFront.forEach((a) => {
	if (a.classList.contains("embedded")) return;
	a.addEventListener("click", ()=>audioAnimation(a));
});

//autoplay Q audio
audioButtonsQ = cardContF.querySelectorAll('.mem-question a.replay-button');
if (audioButtonsQ && audioButtonsQ.length > 0) {
	//choose audio for Q
	chosen_i = Math.floor(Math.random() * audioButtonsQ.length);
	const chosenAudio = audioButtonsQ[chosen_i];
	chosenAudio.classList.add("chosen");
	if (chosenAudio.onclick) {
		chosenAudio.click();
	} else { // AnkiDroid #18235 bug
		androidAutoplay(chosenAudio);
	}
}
</script>


<script>
//on-screen keyboard | mult-choice buttons | tapping buttons

function shuffle(arr) {
  return arr.sort(() => 0.5 - Math.random());
}

if (screenKeyboard) {
	if (isFrontSide) {
		if (Qmode === "typing" && fillerString && corrAns) {
			if (typeof window.randomKeysN !== 'number') {randomKeysN = 10} //fallback
			neededKeys = shuffle(fillerString.split('')).slice(0, randomKeysN);
			neededKeys = shuffle([... new Set([...(corrAns.split('')), ...neededKeys])]);
			neededKeys = neededKeys.filter(key => !keysString.includes(key));
			keysString = neededKeys.join('') + keysString;
		} else if (Qmode === "mchoice") {
			choices = choices.filter(choice => (choice !== corrAns && !!choice));
			choices = shuffle([... new Set(choices)]);
			choices.splice((window.mchOptionsN || 6) - 1);
			choices = [corrAns, ...choices];
			shuffle(choices);
			keysString = choices.join('|');
		} else if (Qmode === "tapping") {
			tokens = preTokenize(corrAns).split(' ').map(token => token.trim());
			shuffle(tokens);
     keysString = tokens.join(' ');
		}

		sessionStorage.setItem("card-keyboard", keysString);
	} else {
		keysString = sessionStorage.getItem("card-keyboard") || "";
	}

	if (Qmode === "typing") {
	  keys = keysString.split('');
	} else if (Qmode === "mchoice") {
		keys = keysString ? keysString.split('|') : [];
		screenKeyboard.innerHTML = '';
	} else if (Qmode === "tapping") {
		keys = keysString ? keysString.split(' ') : [];
		keys = keys.map(key => key.replaceAll("　"," "));
		screenKeyboard.innerHTML = '';
	} else {
		keys = [];
		screenKeyboard.innerHTML = '';
	}

  keys.slice().reverse().forEach((key)=>{
    const keyButton = document.createElement("div");
    if (Qmode === "mchoice") {
      keyButton.innerHTML = key;
    } else if (Qmode === "tapping") {
      keyButton.innerText = key;
    } else {
      keyButton.innerText = key; // (Qmode === "typing")
    }
    keyButton.classList.add('membtn');
    if (Qmode === "typing" && (key === ' ' || key === '　')) {keyButton.classList.add('space')}
    if (Qmode === "mchoice") {
      if (key === corrAns || allAlts.includes(key)) {
        keyButton.classList.add('correct')
      } else if (isMathJax && MJwrap(key) === corrAns) {
        keyButton.classList.add('correct')
      } else if (isMathJax) {
        allAlts.map(async (altAns) => cfWithMathJax(altAns, key).then((res) => {
          if (res) {keyButton.classList.add('correct')}
        }));
      }
    }
    screenKeyboard.prepend(keyButton);
  })
} 
</script>

<script>
delete window.randomKeysN;
delete window.mchOptionsN;
</script>

<script>
/*keyboard key functions*/
keyboardButtons = screenKeyboard.querySelectorAll('.membtn');

function flipToBack() {
	if (!isFrontSide) return;
	if (platform === 'desk') {
		pycmd("ans");
	} else if (platform === 'android') {
		showAnswer();
	} else if (platform === 'ankiweb') {
		const ankiwebButtons = document.querySelectorAll('.btn.btn-primary.btn-lg');
		if (ankiwebButtons.length === 1) {
			ankiwebButtons[0].click();
		} else {
			console.log(ankiwebButtons.length < 1 ? "can't flip to back: ankiweb button not found" : "can't flip to back: can't single out the ankiweb button");
		}
	}
	console.log('flip');
}

function lengthOfCommonPart(str1, str2) {
	const minLength = Math.min(str1.length, str2.length);
	let i; 
	for (i = 0; str1[i] == str2[i] && i < minLength; i++) {}
	return i;
}

function updInput(inputValue, cursorPos = null) {
	if (!typeAns) return;

	typeAns.value = inputValue;
	typeAns.setSelectionRange(cursorPos || inputValue.length, cursorPos || inputValue.length);

	storeAnswer();

	typeAns.focus(); // Android quirk (doesn't seem to update cursor position without this)
	if (platform !== 'desk') {
		typeAns.blur();
	}
}

function typeHint() {
	if (!hintAns || !typeAns) return;
	const tempAns = window.isMathJax && typeAns.value.startsWith('\\\x28') ? typeAns.value.slice(2) : typeAns.value;
	const correctLength = lengthOfCommonPart(tempAns, hintAns);

	if (correctLength < hintAns.length) {
		updInput(hintAns.slice(0, correctLength + 1));

	} else if (typeAns.value.length > correctLength) {
		updInput(hintAns);

	} else {
		flipToBack();
	}
}

function typeKey(keyContent) {
	if (!typeAns) return;
	const cursorStart = typeAns.selectionStart;
	const cursorEnd = typeAns.selectionEnd;
	const currentInput = typeAns.value;

	updInput(currentInput.slice(0, cursorStart) + htmlUnEscape(keyContent) + currentInput.slice(cursorEnd), cursorStart + 1);
}

function updTappedAnswer() {
  const tappedWords = tapAnsArea.querySelectorAll(".membtn");

  storeAnswer([...tappedWords].map(btn => btn.getAttribute("origin")).join("|"));
  //storeAnswer([...tappedWords].map(btn => btn.innerText).join(" "));
}

function untapKey(N) {
  if (!tapAnsArea) return;

  tapAnsArea.querySelector(`[origin="${N}"]`)?.onclick();
}

function tapKey(N, dynamic = false) {
  if (!tapAnsArea || !keyboardButtons || N > keyboardButtons.length || keyboardButtons[N - 1].classList.contains("pressed")) return;

  keyboardButtons[N - 1].classList.add("pressed");

  const tappedWordL = document.createElement("div");
  tappedWordL.classList.add('membtn');
  tappedWordL.innerText = keys[N - 1];
  tappedWordL.setAttribute("origin", N);
  tapAnsArea.append(tappedWordL);

  if (!dynamic) return;
  
  tappedWordL.onclick = ()=>{
    tappedWordL.remove();
    keyboardButtons[N - 1].classList.remove("pressed");
    updTappedAnswer();
  }

  updTappedAnswer();
}

if (isFrontSide) {
	keyboardButtons.forEach( btn => {
		if (btn.id === 'HintButton') {
			btn.onclick = typeHint;
		} else if (Qmode === "mchoice") {
			btn.onclick = ()=>{
				if (btn.classList.contains('pressed')) {
					storeAnswer("");
					btn.classList.remove('pressed');
				} else {
					storeAnswer(btn.innerHTML);
					keyboardButtons.forEach((b) => {
						b.classList.remove('pressed');
					});
					btn.classList.add('pressed');
				}
				flipToBack();
			};
		} else if (Qmode === "typing" && typeAns) {
			btn.onclick = ()=>{
				typeKey(btn.innerHTML); //innerText does not work for space
			};
		} else if (Qmode === "tapping") {
			const N = 1 + Array.prototype.indexOf.call(btn.parentNode.children, btn);
			btn.onclick = ()=>tapKey(N, true);
		}
	});

	if (typeAns) {
		typeAns.addEventListener('input', (event) => {storeAnswer();});
		if (platform === 'ankiweb') {
			setTimeout(()=>{
				document.activeElement.blur();
				typeAns.focus();
			}, 25);
		}
	}
}
</script>

<script>
//iOS AnkiWeb + embedded audio svg paths

rootStyles = getComputedStyle(document.documentElement);
memPlayPath = rootStyles.getPropertyValue('--mem-play').trim().replace(/^path\(["']?|["']?\)$/g, '');
document.querySelectorAll('svg.playImage path').forEach(path =>{
if (path.getAttribute('d')) return;
  path.setAttribute('d', memPlayPath);
});
</script>
<!-- End of code by Eltaurus -->