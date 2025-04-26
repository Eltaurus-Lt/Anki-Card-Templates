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
Clarification: The copyright in this notice applies only to the above-stated section of the code. In particular, it does not extend to data contained within fields of Anki cards or any media files included in Anki decks created using this template. It also does not cover any scripts or HTML code that may be added to this HTML file (Back Template screen) by creators of derivative cards/templates. Creators are encouraged to add their own copyright statements alongside their code in a similar fashion.
-->

<script>
//generate random page id
pid = Array.from({length:16}, () => String.fromCharCode(Math.floor(Math.random() * 94) + 33)).join('');
//console.log("pageid: ", pid);
</script>

<script>
//Ratcliff-Obershelp
function stringDiff(s1, s2) {
    const n = s1.length;
    const m = s2.length;

    // Matrix of contiguous LCS lengths
    const M = Array.from({length: n + 1}, () => Array(m + 1).fill(0)); 
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (s1[i] === s2[j]) {
                M[i+1][j+1] = M[i][j] + 1;
            }
        }
    }

    function minorLCS(n1, n2, m1, m2) {
        let max = 0;
        let pos;
        for (let i = n1; i <= n2; i++) {
            for (let j = m1; j <= m2; j++) {
                const Mij = Math.min(M[i][j], j - m1 + 1, i - n1 + 1);
                if (Mij > max) {
                    max = Mij;
                    pos = [i, j];
                }
            }
        }
        return { "length": max, pos }
    }
  
    function Diff(n1, n2, m1, m2) {
      const LCS = minorLCS(n1, n2, m1, m2);
      const length0 = LCS.length;
      
      if (length0 === 0) {
        const diff1 = s1.substring(n1 - 1, n2);
        const diff2 = s2.substring(m1 - 1, m2);
        diff = '';
        if (diff2) {
          diff += '<span class="typeBad">' + htmlEscape(diff2) + '</span>';
        }
        if (diff1) {
          diff += '<span class="typeMissed">' + htmlEscape(diff1) + '</span>';
        }
        return {
          diff,
          CSlength: 0
        };
      } else {  
        const n0 = LCS.pos[0];
        const m0 = LCS.pos[1];
        const D1 = Diff(n1, n0 - length0, m1, m0 - length0);
        const D2 = Diff(n0 + 1, n2, m0 + 1, m2);
        const diff0 = '<span class="typeGood">' + htmlEscape(s1.substring(n0 - length0, n0)) + '</span>';
        return {
          diff: D1.diff + diff0 + D2.diff,
          CSlength: D1.CSlength + length0 + D2.CSlength
        }
      }
    }
  
    const D = Diff(1, n, 1, m);
    // classic similarity score: not typing a letter yields higher score than typing it incorrectly => discourages trying, not ideal
    //const score = 2 * D.CSlength / (n + m); 
    // corrected score: typing wrong letter yields the same score as skipping it
    const score = D.CSlength / Math.max(m, n);

    return { score, "CSlength": D.CSlength, "diff": D.diff };
}
</script>

<script>
//get user answer
userAns = sessionStorage.getItem("userAnswer");
if (userAns === null) {
	document.getElementsByClassName("mem-alert")[0].innerText = "#error loading answer!";
	userAns = '';
} else if (userAns.trim()) {
  if (Qmode === "tapping") {
    pressedSequence = userAns.split('|');
    userAns = pressedSequence.map(N => keyboardButtons[N - 1].innerText).join(' ');
  }
  if (Qmode === "mchoice") {
	  document.getElementsByClassName("mem-alert")[0].innerHTML = userAns; //text formatting, images and audio + latex in mcq
  } else if (!window.isMathJax) {
    setTimeout(()=>document.getElementsByClassName("mem-alert")[0].innerText = userAns, 100); // "a<b" and "b>a" in plain text
  } else {
    MJconvert(htmlEscape(userAns)).then(res => document.getElementsByClassName("mem-alert")[0].innerHTML = res);
  }
}
if (Qmode === "tapping" && userAns) { //pressedSequence can remain from previous cards
  pressedSequence.forEach((N) => tapKey(N));
}
if (typeAns?.tagName === 'INPUT') {
	typeAns.value = userAns;
	typeAns.disabled = true;
} else if (typeAns) {
	typeAns.innerHTML = '<span>' + htmlEscape(userAns) + '</span>'; //backward compatibility with stock Anki typing
}

console.log(`user answer: ${userAns} | correct answer: ${corrAns}`);
</script>

<script>
//answer comparison rules
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
	//removes spaces from the start and the end, replaces japanese and non-breaking spaces, removes repeated spaces
	return ansCleanUp(s).replace(/　/g, ' ').replace(/\s+/g, ' ');
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
diff = "";
console.log(`altertnatives: ${allAlts.join(' | ')}`);

async function setCorrectClass() {
  if (Qmode === "tapping") {
	//tapping (any kind)
    if (preTokenize(corrAns).replaceAll("　"," ") === userAns) {
      wrap.classList.add('correct');
    }
    return
  }
	if (!window.isMathJax) {
//text cf
		if (Qmode === "mchoice") {
			keyboardButtons.forEach(btn => {
				if (btn.innerHTML === userAns) {
					btn.classList.add('pressed');
					if (btn.classList.contains('correct')) {
						wrap.classList.add('correct');
					}
				}
			})

	//type-in
		} else if (cfStrings(corrAns, userAns)) {
			wrap.classList.add('correct');
		} else if (allAlts.map((altAns) => cfStrings(altAns, userAns)).includes(true)) {
			wrap.classList.add('correct');
		}
	} else {
//latex cf
	userAns = MJunwrap(userAns);
	corrAns = MJunwrap(corrAns);
		if (Qmode === "mchoice") {
			const btnPromises = [...keyboardButtons].map(async btn => {
				if (btn.innerHTML === userAns || (await cfWithMathJax(btn.innerHTML, userAns))) {
					btn.classList.add('pressed');
					if (btn.classList.contains('correct')) {
						wrap.classList.add('correct');
					}
				}
			});
			await Promise.all(btnPromises);

	//type-in
		} else if (corrAns === userAns) {
			wrap.classList.add('correct');
		} else {
			const altPromises = allAlts.map(async (altAns) => await cfWithMathJax(htmlEscape(altAns), htmlEscape(userAns)));
			
			await Promise.all(altPromises).then(results => {
				if (results.includes(true)) {
					wrap.classList.add('correct');
				}
			});
		}
	}
}
setCorrectClass().then(() => {
	if (wrap.classList.contains('correct')) {
		highlightGood();
	} else {
		highlightAgain();
		if (Qmode === "mchoice") {
				wrap.classList.add('wrong');
		} else {
	//type-in or tapping
			diff = stringDiff((Qmode !== "tapping") ? corrAns : preTokenize(corrAns).replaceAll("　"," "), userAns);
			if (diff.score > 0.67) {
				wrap.classList.add('soclose');
			} else {
				wrap.classList.add('wrong');
			}
			//spelling diffs
			const spellDiff = document.getElementById('spelldiff');
			if (spellDiff && userAns.trim()) {
				spellDiff.innerHTML = diff.diff;
			}
		}
	}
});

//timeout flip
infoOnCorrect = !!window.alwaysShowInfo; //without this redef impossible to reliably clear the hook if rated with Anki buttons
delete window.alwaysShowInfo;

flipBtn = document.getElementById('mem-flip');
function MemFlip(toInfo = false) {
	try {clearTimeout(activeTimeout)} catch (err) {};

	if (wrap.classList.contains("correct") && !toInfo && !infoOnCorrect && platform !== 'ios') {
		autorateGood();
	} else {
		putOnCD();

		wrap.classList.add("backside");
		wrap.classList.remove("frontside");
		setTimeout(()=>window.scrollTo(0, 0), 1);
		flipBtn.onclick = ()=>{
			if (wrap.classList.contains("correct")) {
				autorateGood();
			} else if (wrap.classList.contains("wrong") || wrap.classList.contains("soclose")) {
				autorateAgain();
			} else {
				console.log("the answer is not yet evaluated");
			}
		}
	}
}
flipBtn.onclick = MemFlip;

activeTimeout = setTimeout((pid0)=>{
//	console.log(pid, "|", pid0);
	if (pid !== pid0) return;
	MemFlip();
}, Math.round((window.flipDelay || 1.5) * 1000), pid);
delete window.flipDelay;

//Submit
function highlightAgain() {
	if (platform === "ankiweb") {
		const ankiwebButtons = document.querySelectorAll('.btn.btn-primary.btn-lg');
		if (ankiwebButtons.length === 4) {
			ankiwebButtons[0].classList.add('preselected');
			ankiwebButtons[0].focus();
			ankiwebButtons[0].blur();
		} else {
			console.log(`incorrect number of answer buttons (&{ankiwebButtons.length})`);
		}
	}
}
function highlightGood() {
	if (platform === "ankiweb") {
		const ankiwebButtons = document.querySelectorAll('.btn.btn-primary.btn-lg');
		if (ankiwebButtons.length === 4) {
			ankiwebButtons[2].classList.add('preselected');
			ankiwebButtons[2].focus();
			ankiwebButtons[2].blur();
		} else {
			console.log(`incorrect number of answer buttons (&{ankiwebButtons.length})`);
		}
	}
}
function autorateAgain() {
		flipBtn.onclick = null;
		if (platform === 'desk') {
			pycmd('ease1');
		} else if (platform === 'android') {
			buttonAnswerEase1();
		} else if (platform === 'ankiweb') {
			awRate(1);
		}
		console.log("🔴 autorated 'again'");
}
function autorateGood() {
		flipBtn.onclick = null;
		if (platform === 'desk') {
			pycmd('ease3');
		} else if (platform === 'android') {
			buttonAnswerEase3();
		} else if (platform === 'ankiweb') {
			awRate(3);
		}
		console.log("🟢 autorated 'good'");
}
</script>

<script>
//embedding backside audio buttons (android)
embeddedAudiosBack = [...document.querySelectorAll('audio:not(.off)')];
embeddedAudiosBack.forEach((audioL, i) => {
  const replayButtonHTML = `
    <a class="replay-button soundLink embedded" onclick="replayEmbedded(${i + embeddedAudios.length}, this)" href="../#">
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
embeddedAudios = embeddedAudios.concat(embeddedAudiosBack);

</script>
<script>
//Audio buttons animation
document.querySelectorAll('.card-content.back a.replay-button').forEach((a) => {
	if (a.classList.contains("embedded")) return;
	a.addEventListener("click", ()=>audioAnimation(a));
});
</script>

<!-- End of code by Eltaurus -->