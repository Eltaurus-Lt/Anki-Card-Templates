// This script is part of the Lt-Cards Add-on for Anki.
// Source: github.com/Eltaurus-Lt/Anki-Card-Templates
// 
// Copyright © 2026 Eltaurus
// Contact: 
//     Email: Eltaurus@inbox.lt
//     GitHub: github.com/Eltaurus-Lt
//     Anki Forums: forums.ankiweb.net/u/Eltaurus
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// See the GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.

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
