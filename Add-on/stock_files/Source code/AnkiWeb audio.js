(()=>{

  function createAudioButton(onclickFunction) {
    const btnL = document.createElement("a");
    btnL.classList.add("replay-button", "soundLink");
    btnL.setAttribute('draggable', false);
    btnL.innerHTML = `<svg class="playImage" viewBox="0 0 64 64" version="1.1" width="40px" height="40px"><circle cx="32" cy="32" r="29" fill="#fff" stroke="#414141"></circle><path fill="#414141" d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z"></path></svg>`;
    btnL.href = "../#";
    btnL.onclick = onclickFunction;
    return btnL;
  }

  document.querySelectorAll("audio").forEach(audioL => {
    audioL.parentNode.replaceChild(createAudioButton(() => audioL.play()), audioL);
  });


  // AnkiWeb TTS

  const qaL = document.querySelector('#qa_box #qa');
  if (!qaL) return;

  const TTSRegex = /\[anki:tts([^\]]*)\]([^\[]*)\[\/anki:tts\]/g;
  function parseTTSAttrs(attr_string) {
    const attrs = {};
    attr_string.trim().split(/\s+/).forEach(attr => {
        const [key, value] = attr.split('=');
        if (key && value) attrs[key] = value;
    });
    return attrs;
  }

  const walker = document.createTreeWalker(qaL, NodeFilter.SHOW_TEXT, null);
  const textNodes = [];
  while (walker.nextNode()) {
    textNodes.push(walker.currentNode);
  }

  for (const textNode of textNodes) {
    const text = textNode.nodeValue;
    let lastIndex = 0, match;
    const frag = document.createDocumentFragment();
    TTSRegex.lastIndex = 0;

    while ((match = TTSRegex.exec(text))) {
      if (match.index > lastIndex) {
        frag.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
      }
      const attrs = parseTTSAttrs(match[1]);
      const word = match[2];
      frag.appendChild(createAudioButton(()=>{
        const ut = new SpeechSynthesisUtterance(word);
        ut.lang = attrs["lang"]?.replace('_','-') || "en-US";
        window.speechSynthesis.speak(ut);
      }));
      lastIndex = TTSRegex.lastIndex;
    }
    if (lastIndex < text.length) {
      frag.appendChild(document.createTextNode(text.slice(lastIndex)));
    }
    if (frag.childNodes.length) {
      textNode.parentNode.replaceChild(frag, textNode);
    }
  }

})();