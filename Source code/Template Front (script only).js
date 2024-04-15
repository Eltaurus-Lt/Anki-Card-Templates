<script>
//determine card side
wrap = document.getElementById('backwrap');
isFrontSide = !wrap;
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

//const
if (hintSetting) {hintAnswer = hintSetting.innerText} else {hintAnswer = ""}
if (staticKeys) {keysString = staticKeys.innerText} else {keysString = ""}
if (randomKeys) {fillerString = randomKeys.innerText} else {fillerString = ""}

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

	if (ev.key === 'Enter' && tabSelected !== document.activeElement) {//last action was NOT selecting element with Tab -> Enter=flip (prevent audio activation)
		if (document.activeElement.matches('a.replay-button.soundLink')) {
			document.activeElement.blur();
		}
		if (flipBtn &&  flipBtn.onclick) {				
			flipBtn.onclick();
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
//on-screen keyboard | mutl-choice buttons

function shuffle(arr) {
  return arr.sort(() => 0.5 - Math.random());
}

screenKeyboard = document.getElementById('scr-keyboard');
if (screenKeyboard) {
	if (isFrontSide) {
		if (fillerString && hintAnswer) {
			neededKeys = shuffle(fillerString.split('')).slice(0, 10);
			neededKeys = shuffle([... new Set([...(hintAnswer.split('')), ...neededKeys])]);
			neededKeys = neededKeys.filter(key => !keysString.includes(key));
			keysString = neededKeys.join('') + keysString;
		}

		sessionStorage.setItem("mem-keyboard", keysString);
	} else {
		keysString = sessionStorage.getItem("mem-keyboard");
		if (!keysString) {keysString = ""};
	}

  keys = keysString.split('');
  keys.reverse().forEach((key)=>{
    const keyButton = document.createElement("div");
    keyButton.innerText = key;
    keyButton.classList.add('membtn');
    if (key === ' ' || key === '　') {keyButton.classList.add('space')}
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
		typeAns.focus();
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
}

if (isFrontSide) {
	keyboardButtons.forEach( btn => {
		if (btn.id === 'HintButton') {
			btn.onclick = typeHint;
		} else {
			btn.onclick = ()=>{
			typeKey(btn.innerHTML);
			btn.classList.contains('mchoice') ? flipToBack() : {};
			};
		}
	})
}

if (platform === 'android') {
	typeAns.addEventListener("input", androidSave);
}
</script>