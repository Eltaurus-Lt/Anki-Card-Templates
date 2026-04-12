(()=>{

  const audioHTML = `<svg class="playImage" viewBox="0 0 64 64" version="1.1" width="40px" height="40px"><circle cx="32" cy="32" r="29" fill="#fff" stroke="#414141"></circle><path fill="#414141" d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z"></path></svg>`;

  document.querySelectorAll("audio").forEach(audioL => {
    const linkL = document.createElement("a");
    linkL.classList.add("replay-button", "soundLink");
    linkL.setAttribute('draggable', false);
    linkL.innerHTML = audioHTML;

    linkL.href = "../#";
    linkL.onclick = () => audioL.play();

    audioL.parentNode.replaceChild(linkL, audioL);
  });


  // AnkiWeb TTS

  function parseTTSAttrs(attr_string) {
    const attrs = {};
    attr_string.trim().split(/\s+/).forEach(attr => {
        const [key, value] = attr.split('=');
        if (key && value) attrs[key] = value;
    });
    return attrs;
  }

  function sanitizeStr(str) {
    return str.replace(/['"]/g, "");
  }

  function TTS2asvg(htmlContent) {
    const TTSRegex = /\[anki:tts([^\]]*)\]([^\[]*)\[\/anki:tts\]/g;
    return htmlContent.replace(TTSRegex, (_, attr_string, word) => {
      const attrs = parseTTSAttrs(attr_string);
      const lang = attrs["lang"]?.replace('_','-') || "en-US";
      return `<a class="replay-button soundLink" onclick="const ut = new SpeechSynthesisUtterance('${sanitizeStr(word)}');ut.lang='${sanitizeStr(lang)}';window.speechSynthesis.speak(ut);" href="../#">${audioHTML}</a>`;
    });
  }

  const qaL = document.querySelector('#qa_box #qa');
  if (!qaL) return;
  qaL.innerHTML = TTS2asvg(qaL.innerHTML);

})();