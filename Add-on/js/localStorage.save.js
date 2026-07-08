(() => {
    function localStorage_save() {
        if (window.__localStorage_isLoading) return;
        try {
            var localStorage_json = JSON.stringify(localStorage);
            if (typeof pycmd !== 'undefined') {
                pycmd("save_localStorage::" + localStorage_json);
            }
        } catch(err) {
            console.error("localStorage listener error: ", err);
        }
    };

    var originalSetItem = localStorage.setItem;
    localStorage.setItem = function(key, value) {
        originalSetItem.apply(this, arguments);
        localStorage_save();
    };

    var originalRemoveItem = localStorage.removeItem;
    localStorage.removeItem = function(key) {
        originalRemoveItem.apply(this, arguments);
        localStorage_save();
    };

    var originalClear = localStorage.clear;
    localStorage.clear = function() {
        originalClear.apply(this, arguments);
        localStorage_save();
    };
})();
