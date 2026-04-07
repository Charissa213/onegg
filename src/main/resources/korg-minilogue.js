// ── Korg Minilogue – Web Synthesizer ─────────────────────────────────────────
(function () {
    'use strict';

    let audioCtx = null;

    function getAudioCtx() {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        return audioCtx;
    }

    // ── Noten: C1 t/m C4 (37 toetsen) ───────────────────────────────────────
    const NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
    const IS_BLACK   = [false,true,false,true,false,false,true,false,true,false,true,false];
    const NOTES = [];

    for (let octave = 1; octave <= 4; octave++) {
        for (let semitone = 0; semitone < 12; semitone++) {
            if (octave === 4 && semitone > 0) break;
            const midi = (octave + 1) * 12 + semitone;
            const freq = 440 * Math.pow(2, (midi - 69) / 12);
            NOTES.push({ name: NOTE_NAMES[semitone] + octave, freq, isBlack: IS_BLACK[semitone] });
        }
    }

    // ── Synthesizergeluid ─────────────────────────────────────────────────────
    function playNote(frequency) {
        const ctx = getAudioCtx();
        const now = ctx.currentTime;

        const osc1   = ctx.createOscillator();
        const osc2   = ctx.createOscillator();
        const filter = ctx.createBiquadFilter();
        const gain   = ctx.createGain();

        osc1.type = 'sawtooth';
        osc2.type = 'sawtooth';
        osc1.frequency.value = frequency;
        osc2.frequency.value = frequency * 1.006;

        filter.type            = 'lowpass';
        filter.frequency.value = Math.min(frequency * 5, 4000);
        filter.Q.value         = 4;

        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(0.35, now + 0.008);
        gain.gain.exponentialRampToValueAtTime(0.18, now + 0.15);
        gain.gain.setValueAtTime(0.18, now + 0.15);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.4);

        osc1.connect(filter); osc2.connect(filter);
        filter.connect(gain); gain.connect(ctx.destination);
        osc1.start(now); osc2.start(now);
        osc1.stop(now + 1.5); osc2.stop(now + 1.5);
    }

    // ── Noot-indicator ────────────────────────────────────────────────────────
    let indicator = null;

    function showIndicator(noteName, clientX, clientY) {
        if (!indicator) {
            indicator = document.createElement('div');
            indicator.className = 'minilogue-note-indicator';
            document.body.appendChild(indicator);
        }
        indicator.textContent = noteName;
        indicator.style.left = clientX + 'px';
        indicator.style.top  = (clientY - 50) + 'px';
        indicator.classList.remove('visible');
        void indicator.offsetWidth;
        indicator.classList.add('visible');
    }

    // ── Piano keyboard ────────────────────────────────────────────────────────
    function createKeyboard() {
        const keyboard = document.createElement('div');
        keyboard.className = 'minilogue-keyboard';

        // Bereken posities (in witte-toets-eenheden)
        let whiteCount = 0;
        const positioned = NOTES.map(note => {
            if (note.isBlack) {
                return { ...note, leftInWhites: whiteCount - 0.35 };
            } else {
                const pos = { ...note, leftInWhites: whiteCount };
                whiteCount++;
                return pos;
            }
        });

        const totalWhites = whiteCount; // 22

        function makeKey(note) {
            const key = document.createElement('div');
            key.className = 'mkey ' + (note.isBlack ? 'mkey--black' : 'mkey--white');
            key.style.left  = (note.leftInWhites / totalWhites * 100) + '%';
            key.style.width = ((note.isBlack ? 0.58 : 1) / totalWhites * 100) + '%';

            const activate = (e) => {
                playNote(note.freq);
                showIndicator(note.name, e.clientX || e.touches?.[0]?.clientX, (e.clientY || e.touches?.[0]?.clientY) - 60);
                key.classList.add('mkey--active');
            };
            const deactivate = () => key.classList.remove('mkey--active');

            key.addEventListener('mousedown', activate);
            key.addEventListener('mouseup', deactivate);
            key.addEventListener('mouseleave', deactivate);
            key.addEventListener('touchstart', (e) => { e.preventDefault(); activate(e); }, { passive: false });
            key.addEventListener('touchend', deactivate);

            return key;
        }

        // Witte toetsen eerst (achtergrond), dan zwarte (voorgrond)
        positioned.filter(n => !n.isBlack).forEach(n => keyboard.appendChild(makeKey(n)));
        positioned.filter(n =>  n.isBlack).forEach(n => keyboard.appendChild(makeKey(n)));

        document.body.appendChild(keyboard);
    }

    // ── Init ──────────────────────────────────────────────────────────────────
    document.addEventListener('DOMContentLoaded', createKeyboard);

})();
