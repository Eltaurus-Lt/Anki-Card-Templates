//not up to date!
<script>
//generate random page id
pid = Array.from({length:16}, () => String.fromCharCode(Math.floor(Math.random() * 94) + 33)).join('');
//console.log("pageid: ", pid);

// extract answers
correctNodes = [...typeAns.querySelectorAll("br ~ br ~ span")];
typedNodes = [...typeAns.querySelectorAll("span:not(.typeMissed, br ~ span)")];

correctAnswerFull = correctNodes.map(e => e.innerText).join('');
if (!correctAnswerFull && typeAns) { //typed answer is correct or no typed answer
	correctAnswerFull = typeAns.innerText;
}
typedAnswer = typedNodes.map(e => e.innerText).join('');
typedCorrect = [...typeAns.querySelectorAll("span.typeGood:not(br ~ span)")].map(e => e.innerText).join('');
typedErrors = [...typeAns.querySelectorAll("span:is(.typeBad, .typeMissed):not(br ~ span)")].map(e => e.innerText).join(''); //exception: = '' if no typed answer

console.log(correctAnswerFull, "|", typedAnswer, "（", typedCorrect, "|", typedErrors, "）"); 
androidAnswer = sessionStorage.getItem("android-answer");
if (platform === 'android' && androidAnswer) {
	typedAnswer = androidAnswer;
	typeAns.innerHTML = '<span>' + androidAnswer + '</span>';
}
document.getElementsByClassName("mem-alert")[0].innerText = typedAnswer;

//answer processing
function rmEnc(s) {
	//removes parts enclosed in the innermost parentheses
	return s.replace(/\x28[^()]*\x29/g, '');
}
function rmEncAll(s) {
	//remove everything between first and last brackets
	return s.replace(/\x28.*\x29/g, '');
}
function rmBrac(s) {
	//removes parentheses, keeping the contents
	return s.replace(/[()]/g, '');
}
function rmPunc(s) {
	//removes other punctuation
	return s.replace(/[.,\/#?!$%\^&\'"*;:{}=\-_`~　…〜～－。、・？！＠＃＄％＾＆＊（）]/g, '');
}
function rmSpaces(s) {
	//removes spaces from the start and the end, replaces japanese spaces, removes repeated spaces
	return s.trim().replace(/　/g, ' ').replace(/\s+/g, ' ');
}
function cfStrings(sQ, sA) {
 //unify case and remove punctuation
	var sq = rmSpaces(rmPunc(sQ.toLowerCase()));
	var sa = rmSpaces(rmPunc(sA.toLowerCase()));

	if (sq == sa) {
		return true;
	}
	if (rmSpaces(rmEnc(rmEnc(sq))) == sa) {
		return true;
	}
	if (rmSpaces(rmBrac(sq)) == sa) {
		return true;
	}
	return false;
}

//A (B) -> {〃, A, A B}
//A; B -> {〃, A, B}
//A; B (C) -> {〃, A, B, B C, B (C)}
//todo?A (B; C) -> {〃, A B, A C}

// grade answer
if (cfStrings(correctAnswerFull, typedAnswer)) {
	wrap.classList.add('correct');
} else if (correctAnswerFull.split(/[;；]/).map((correctAnswer) => cfStrings(correctAnswer, typedAnswer)).includes(true)) {
	wrap.classList.add('correct');
} else if (typedErrors.length <= 0.5 * correctAnswerFull.length && typedCorrect.length >= (1 - 0.5) * correctAnswerFull.length) {
	wrap.classList.add('soclose');
} else {
	wrap.classList.add('wrong');	
}

//timeout flip
flipBtn = document.getElementById('mem-flip');
function MemFlip() {
	try {clearTimeout(activeTimeout)} catch (err) {};

	if (wrap.classList.contains("correct")) {
		autorateGood();
	} else {
		wrap.classList.add("backside");
		wrap.classList.remove("frontside");
		flipBtn.onclick = autorateAgain;
	}
}
flipBtn.onclick = MemFlip;

activeTimeout = setTimeout((pid0)=>{
//	console.log(pid, "|", pid0);
	if (pid !== pid0) return;
	MemFlip();
}, 1500, pid);

//Submit
function autorateAgain() {
		flipBtn.onclick = null;
		if (platform === 'desk') {
			pycmd('ease1');
		} else if (platform === 'android') {
			buttonAnswerEase1();
		}
		console.log("autorated 'again'");
}
function autorateGood() {
		flipBtn.onclick = null;
		if (platform === 'desk') {
			pycmd('ease3');
		} else if (platform === 'android') {
			buttonAnswerEase3();
		}
		console.log("autorated 'good'");
}

if (isMCh) {
	keyboardButtons.forEach( btn => {
		if (btn.innerText === typedAnswer) {
			btn.classList.add('pressed');
		}
	})
}


//Audio buttons animation
audioButtons = document.querySelectorAll('.card-content.back a.replay-button');
audioButtons.forEach((a) => {
	a.addEventListener("click", () => {
		audioButtons.forEach((b) => {
			b.classList.remove('active');
		});
    a.classList.add('active');

		a.classList.remove('pulse');
		void a.offsetHeight;
		a.classList.add('pulse');
	});
});

//spelling cf. highlights
function isGood(list, index) {
	return (index < list.length && list[index].classList.contains('typeGood'));
}
if (correctNodes.length > 0) {
	let mergedNodes = [];
	function mergeNode(list, index) {
		if(index < list.length) {
			mergedNodes.push(list[index]);
		}
	}
	for (	i = j = 0; (i < correctNodes.length || j < typedNodes.length) && i < 1000 && j < 1000; ) {
		if (isGood(correctNodes, i)) {
			mergeNode(typedNodes,j);//all good || bad(redundant)
			if (isGood(typedNodes, j)) {//all good
				i++;
			} else if (j >= typedNodes.length) {i++;}//failsafe
			j++;
		} else {
			if (!isGood(typedNodes, j)) {
				mergeNode(typedNodes,j);//bad(wrong) || bad(redundant-end) || missing-end
				j++;
			} else if (i >= correctNodes.length) {j++;}//failsafe
			mergeNode(correctNodes,i);//missing || bad(wrong) || bad(redundant-end)
			i++;
		}
	}
	
	const spellcheckHighlights = document.getElementById('spellcheck');
	if (spellcheckHighlights && !isMCh) {
		spellcheckHighlights.innerHTML = mergedNodes.map(node => node.outerHTML).join('');
	}
}

</script>