//generate random page id
pid = Array.from({length:16}, () => String.fromCharCode(Math.floor(Math.random() * 94) + 33)).join('');
//console.log("pageid: ", pid);

// extract answers
typeAns = document.getElementById('typeans'); 

correctAnswerFull = [...typeAns.querySelectorAll("br ~ br ~ span")].map(e => e.innerText).join('');
if (!correctAnswerFull && typeAns) { //typed answer is correct or no typed answer
	correctAnswerFull = typeAns.innerText;
}
typedAnswer = [...typeAns.querySelectorAll("span:not(.typeMissed, br ~ span)")].map(e => e.innerText).join('');
typedCorrect = [...typeAns.querySelectorAll("span.typeGood:not(br ~ span)")].map(e => e.innerText).join('');
typedErrors = [...typeAns.querySelectorAll("span:is(.typeBad, .typeMissed):not(br ~ span)")].map(e => e.innerText).join(''); //exception: = '' if no typed answer

console.log(correctAnswerFull, "|", typedAnswer, "（", typedCorrect, "|", typedErrors, "）"); 
document.getElementsByClassName("mem-alert")[0].innerText = typedAnswer;

//answer processing
function rmEnc(s) {
	//removes parts enclosed in the innermost parentheses
	return s.replace(/\([^()]*\)/g, '');
}
function rmEncAll(s) {
	//remove everything between first and last brackets
	return s.replace(/\(.*\)/g, '');
}
function rmBrac(s) {
	//removes parantheses, keeping the contents
	return s.replace(/[()]/g, '');
}
function rmPunc(s) {
	//removes other punctuation
	return s.replace(/[.,\/#?!$%\^&\'"*;:{}=\-_`~　…～－。、・？！＠＃＄％＾＆＊（）]/g, '');
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
wrap = document.getElementById('backwrap');
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

//submit
function autorateAgain() {
		flipBtn.onclick = null;
		pycmd('ease1');
		console.log("autorated 'again'");
}
function autorateGood() {
		flipBtn.onclick = null;
		pycmd('ease3');
		console.log("autorated 'good'");
}

//Enter hotkey
document.onkeydown = function (e) {
	var ev = window.event || e;

	if (flipBtn && ev.key === 'Enter' && flipBtn.onclick) {
		flipBtn.onclick();
	}
}
