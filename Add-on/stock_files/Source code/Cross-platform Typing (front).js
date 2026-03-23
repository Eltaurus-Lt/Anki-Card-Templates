if (!window.backside) { // prevent execution on the back side

  // parsing and saving expected answer
  const expAnsL = document.getElementById('expans');
  const expAns = expAnsL?.innerText.trim();
  sessionStorage.setItem("card::expectedAnswer", expAnsL.innerText || "");

  // saving typed answer
  const typeAnsL = document.getElementById('typeans');
  function storeAnswer(typeAns = "") {
	  if (!typeAns && typeAnsL) {typeAns = typeAnsL.value};
  	sessionStorage.setItem("card::typedAnswer", typeAns);
  }

  storeAnswer(); // clean up the storage after previous card
  sessionStorage.setItem("card::input", "typing"); // saving the front-side input method

  if (typeAnsL) {
    typeAnsL.addEventListener('input', (ev) => {storeAnswer();});
    if (!!window.qa_box) { // AnkiWeb
      setTimeout(()=>{ document.activeElement.blur(); typeAnsL.focus(); }, 100); // focus the typing field
    }
  }
}