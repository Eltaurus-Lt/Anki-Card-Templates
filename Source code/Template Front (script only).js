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