// ── media.js – Instagram feed loader & entrance animatie ─
(function () {
    'use strict';

    const loader = document.getElementById('mediaLoader');
    const wrap   = document.getElementById('mediaFeedWrap');

    if (!loader || !wrap) return;

    function showFeed() {
        loader.classList.add('is-hidden');
        wrap.classList.add('is-visible');
    }

    // Methode 1: Behold dispatcht 'beholdLoaded' op de widget div
    const widgetEl = wrap.querySelector('[id^="behold-widget-"]');
    if (widgetEl) {
        widgetEl.addEventListener('beholdLoaded', showFeed, { once: true });
    }

    // Methode 2: MutationObserver — zodra Behold afbeeldingen injecteert
    const observer = new MutationObserver(function () {
        if (wrap.querySelector('img')) {
            showFeed();
            observer.disconnect();
        }
    });
    observer.observe(wrap, { childList: true, subtree: true });

    // Methode 3: timeout fallback na 8 seconden
    setTimeout(function () {
        if (!wrap.classList.contains('is-visible')) {
            showFeed();
        }
    }, 8000);

}());

