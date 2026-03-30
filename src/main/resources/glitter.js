(function () {
    /* twinkling stars */
    var stars = document.getElementById('stars');
    if (stars) {
        for (var i = 0; i < 160; i++) {
            var s = document.createElement('div');
            s.className = 'star';
            var size = Math.random() * 2.5 + 0.5;
            s.style.cssText =
                'width:' + size + 'px;height:' + size + 'px;' +
                'top:' + Math.random() * 100 + '%;' +
                'left:' + Math.random() * 100 + '%;' +
                '--dur:' + (Math.random() * 4 + 2).toFixed(2) + 's;' +
                '--delay:-' + (Math.random() * 6).toFixed(2) + 's';
            stars.appendChild(s);
        }
    }

    /* sparkle particles */
    var sp = document.getElementById('sparkles');
    var colors = ['#ffe600','#ff80c0','#80dfff','#c0ff80','#ffb347','#ee82ee'];
    if (sp) {
        for (var j = 0; j < 28; j++) {
            var el = document.createElement('div');
            el.className = 'sparkle';
            var sz = Math.random() * 14 + 6;
            el.style.cssText =
                '--size:' + sz + 'px;' +
                '--color:' + colors[Math.floor(Math.random() * colors.length)] + ';' +
                '--dur:' + (Math.random() * 1.8 + 0.8).toFixed(2) + 's;' +
                '--delay:-' + (Math.random() * 3).toFixed(2) + 's;' +
                'top:' + Math.random() * 100 + '%;' +
                'left:' + Math.random() * 100 + '%';
            sp.appendChild(el);
        }
    }
})();
