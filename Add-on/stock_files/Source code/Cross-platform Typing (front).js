if (!window.answer) { // prevent execution on the back side

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

  function ShowAnswer() {
    if (!!window.pycmd) { // desktop
      pycmd("ans");
    } else if (!!window.showAnswer) { // AnkiDroid
      showAnswer();
    } else if (!!window.qa_box) { // AnkiWeb
      document.querySelector('.btn.btn-primary.btn-lg').click();
    }
  }

  if (typeAnsL) {
    typeAnsL.addEventListener('input', (ev) => {
      storeAnswer();
    });
    typeAnsL.addEventListener('keydown', (ev) => {
      if (event.key === "Enter") {
        ShowAnswer();
      }
    });
    if (!!window.qa_box) { // AnkiWeb
      setTimeout( () => {  // re-focus the typing field
        document.activeElement.blur();
        typeAnsL.focus();
      }, 100);
    }
  }
}