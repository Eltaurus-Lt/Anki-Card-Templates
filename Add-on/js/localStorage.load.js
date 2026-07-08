window.__localStorage_isLoading = true; // prevent triggering the save callback while loading
try {
    const localStorage_json = document.getElementById('localStorage-old').textContent;
    Object.entries(JSON.parse(localStorage_json)).forEach(([key, value]) => {
        localStorage.setItem(key, value);
    });
} catch(e) {
    console.error("localStorage load error ", e);
} finally {
    window.__localStorage_isLoading = false;
}
