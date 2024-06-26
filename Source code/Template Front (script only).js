<script>
//determine card side
wrap = document.getElementById('backwrap');
isFrontSide = !wrap;
</script>

<script>
//determine input type
isMCh = !!document.querySelector('.card-content.mch');
</script>

<script>
//determine platform
platform = '';
if (!document.documentElement.classList.contains("mobile")) {
	platform = 'desk';
} else if (document.documentElement.classList.contains("android")) {
	//var jsApiContract = { version: "0.0.3", developer: "eltaurus@inbox.lt" };
	//var api = new AnkiDroidJS(jsApiContract);
	platform = 'android';
}
</script>

<script>
//elements
typeAns = document.getElementById('typeans'); 
hintSetting = document.getElementById('hint');
staticKeys = document.getElementById('static_keys');
randomKeys = document.getElementById('random_keys');
hintButton = document.getElementById('HintButton');
choicesSetting = document.getElementById('choices');

//const
if (hintSetting) {hintAnswer = hintSetting.innerText} else {hintAnswer = ""}
if (staticKeys) {keysString = staticKeys.innerText} else {keysString = ""}
if (randomKeys) {fillerString = randomKeys.innerText} else {fillerString = ""}
if (choicesSetting) {choices = choicesSetting.innerText.split('|').map(s => s.trim())}

if (hintButton) {hintButton.innerHTML = `<svg><path></path></svg>Hint`;}
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
	var ev = window.event || e;

	if (ev.key === 'Enter' && tabSelected !== document.activeElement) {
		//last action was NOT selecting element with Tab -> Enter=flip (prevent audio activation)
		if (document.activeElement.matches('a.replay-button.soundLink')) {
			document.activeElement.blur();
		}
		if (!isFrontSide && flipBtn && flipBtn.onclick) {				
			flipBtn.onclick();
		} else {
			flipToBack();
		}
	}

	if ("0123456789".includes(ev.key) && isMCh) {
		numkey = parseInt(ev.key);
		if (numkey == 0) {numkey = 10};
		mchoiceButtons = screenKeyboard.querySelectorAll('*');
		if (numkey <= mchoiceButtons.length) {
			mchoiceButtons[numkey - 1].onclick();
		}
	}
}
</script>

<script>
//Audio buttons animation
audioButtonsFront = document.querySelectorAll('.card-content.front a.replay-button');
audioButtonsFront.forEach((a) => {
	a.addEventListener("click", () => {
		audioButtonsFront.forEach((b) => {
			b.classList.remove('active');
		});
    a.classList.add('active');

		a.classList.remove('pulse');
		void a.offsetHeight;
		a.classList.add('pulse');
	});
});
if (audioButtonsFront && audioButtonsFront.length > 0) {
	audioButtonsFront[0].classList.add('active');
	audioButtonsFront[0].classList.add('pulse');
}
</script>

<script>
//--------------------------------------------
//on-screen keyboard | mult-choice buttons

function shuffle(arr) {
  return arr.sort(() => 0.5 - Math.random());
}

screenKeyboard = document.getElementById('scr-keyboard');
if (screenKeyboard) {
	if (isFrontSide) {
		if (fillerString && hintAnswer && !isMCh) {
			//character keys
			neededKeys = shuffle(fillerString.split('')).slice(0, 10);
			neededKeys = shuffle([... new Set([...(hintAnswer.split('')), ...neededKeys])]);
			neededKeys = neededKeys.filter(key => !keysString.includes(key));
			keysString = neededKeys.join('') + keysString;
		} else if (isMCh) {
			//multiple-choice keys
			choices = choices.filter(choice => (choice !== hintAnswer));
			choices = shuffle([... new Set(choices)]);
			choices.splice(6 - 1);
			choices = [hintAnswer, ...choices];
			shuffle(choices);
			keysString = choices.join('|');
		}

		sessionStorage.setItem("mem-keyboard", keysString);
	} else {
		keysString = sessionStorage.getItem("mem-keyboard");
		if (!keysString) {keysString = ""};
	}

	if (!isMCh) {
	  keys = keysString.split('');
	} else {
		keys = keysString.split('|');
		screenKeyboard.innerHTML = '';
	}
  keys.reverse().forEach((key)=>{
    const keyButton = document.createElement("div");
    keyButton.innerText = key;
    keyButton.classList.add('membtn');
    if (!isMCh && (key === ' ' || key === '　')) {keyButton.classList.add('space')}
    if (isMCh && key === hintAnswer) {keyButton.classList.add('correct')}
    screenKeyboard.prepend(keyButton);
  })
}




/*keyboard key functions*/
keyboardButtons = document.querySelectorAll('#scr-keyboard > *');

function flipToBack() {
	if (!isFrontSide) return;
	if (platform === 'desk') {
		pycmd("ans");
	} else if (platform === 'android') {
		showAnswer();
	}
}

function lengthOfCommonPart(str1, str2) {
	const minLength = Math.min(str1.length, str2.length);
	let i; 
	for (i = 0; str1[i] == str2[i] && i < minLength; i++) {}
	return i;
}

function androidSave() {
	sessionStorage.setItem("android-answer", typeAns.value);
}

function typeHint() {
	const correctLength = lengthOfCommonPart(typeAns.value, hintAnswer);
	if (correctLength < hintAnswer.length) {
		typeAns.value = hintAnswer.slice(0, correctLength + 1);

		androidSave();
		if (platform === 'desk') {
			typeAns.focus();
		}
	} else {
		flipToBack();
	}
}

function typeKey(keyContent) {
	const cursorStart = typeAns.selectionStart;
	const cursorEnd = typeAns.selectionEnd;
	const currentInput = typeAns.value;

	typeAns.value = currentInput.slice(0, cursorStart) + keyContent + currentInput.slice(cursorEnd);
	typeAns.setSelectionRange(cursorStart + 1, cursorStart + 1);
	
	androidSave();
	typeAns.focus();
	if (platform !== 'desk') {
		typeAns.blur();
	}
}

if (isFrontSide) {
	keyboardButtons.forEach( btn => {
		if (btn.id === 'HintButton') {
			btn.onclick = typeHint;
		} else {
			btn.onclick = ()=>{
				typeKey(btn.innerHTML);
				if (isMCh) {
					btn.classList.add('pressed');
					flipToBack();
				};
			};
		}
	})
}

if (platform === 'android') {
	typeAns.addEventListener("input", androidSave);
}
</script>