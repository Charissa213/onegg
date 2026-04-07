// ── tour.js – Google Calendar → Tour dates ───────────────
(function () {
    'use strict';

    // ── !! Vul dit in !! ──────────────────────────────────
    // Stap 1: Google Calendar publiek maken (Instellingen → Toegang)
    // Stap 2: API key aanmaken op console.cloud.google.com
    //         (beperk tot "Google Calendar API" + jouw domein)
    // Stap 3: Calendar ID vinden in Instellingen → Agenda integreren
    const CALENDAR_ID = 'JOUW_CALENDAR_ID@group.calendar.google.com';
    const API_KEY     = 'JOUW_API_KEY';
    // ─────────────────────────────────────────────────────

    const list   = document.getElementById('tourList');
    const loader = document.getElementById('tourLoader');
    const empty  = document.getElementById('tourEmpty');

    if (!list) return;

    // ── Helpers ───────────────────────────────────────────
    const DAYS   = ['ZO','MA','DI','WO','DO','VR','ZA'];
    const MONTHS = ['JAN','FEB','MRT','APR','MEI','JUN',
                    'JUL','AUG','SEP','OKT','NOV','DEC'];

    function formatDate(str) {
        // dateTime of date (all-day)
        const d = new Date(str);
        return `${DAYS[d.getDay()]} ${String(d.getDate()).padStart(2,'0')} ${MONTHS[d.getMonth()]} ${d.getFullYear()}`;
    }

    function getTicketUrl(description) {
        if (!description) return null;
        const m = description.match(/https?:\/\/[^\s<"]+/);
        return m ? m[0] : null;
    }

    function renderEvent(ev) {
        const start      = ev.start.dateTime || ev.start.date;
        const dateLabel  = formatDate(start);
        const title      = ev.summary  || 'Onegg live';
        const location   = ev.location || '';
        const ticketUrl  = getTicketUrl(ev.description);

        // "Venue, City" → splitsen op komma
        const parts  = location.split(',').map(s => s.trim());
        const venue  = parts[0] || title;
        const city   = parts.slice(1).join(', ');

        const ticketHtml = ticketUrl
            ? `<a class="tour-date__ticket"
                  href="${ticketUrl}"
                  target="_blank"
                  rel="noopener noreferrer">Tickets →</a>`
            : `<span class="tour-date__ticket tour-date__ticket--soon">Binnenkort</span>`;

        return `
        <div class="tour-date">
            <span class="tour-date__date">${dateLabel}</span>
            <div class="tour-date__info">
                <span class="tour-date__venue">${venue}</span>
                ${city ? `<span class="tour-date__location">${city}</span>` : ''}
            </div>
            ${ticketHtml}
        </div>`;
    }

    // ── Fetch events ──────────────────────────────────────
    async function loadDates() {
        const now = new Date().toISOString();
        const url = 'https://www.googleapis.com/calendar/v3/calendars/'
            + encodeURIComponent(CALENDAR_ID)
            + '/events?key=' + API_KEY
            + '&timeMin=' + encodeURIComponent(now)
            + '&orderBy=startTime'
            + '&singleEvents=true'
            + '&maxResults=20';

        try {
            const res  = await fetch(url);
            if (!res.ok) throw new Error('API ' + res.status);
            const data = await res.json();

            loader.classList.add('is-hidden');

            if (!data.items || data.items.length === 0) {
                empty.classList.add('is-visible');
                return;
            }

            list.innerHTML = data.items.map(renderEvent).join('');

        } catch (err) {
            console.warn('Tour dates ophalen mislukt:', err);
            loader.classList.add('is-hidden');
            empty.classList.add('is-visible');
        }
    }

    loadDates();

}());

