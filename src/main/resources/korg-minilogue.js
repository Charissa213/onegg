// ── Korg Minilogue – Web Synthesizer ─────────────────────────────────────────
// Web Audio API: sawtooth oscillatoren + lowpass filter + ADSR envelope

(function () {
    'use strict';

    let audioCtx = null;

    function getAudioCtx() {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
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
            const midi = (octave + 1) * 12 + semitone; // C1 = MIDI 24
            const freq = 440 * Math.pow(2, (midi - 69) / 12);
            NOTES.push({ name: NOTE_NAMES[semitone] + octave, freq, isBlack: IS_BLACK[semitone] });
        }
    }

    // ── Synthesizergeluid ─────────────────────────────────────────────────────
    function playNote(frequency) {
        const ctx = getAudioCtx();
        const now = ctx.currentTime;

        // Twee oscillatoren met lichte detune → rijker analoog geluid
        const osc1   = ctx.createOscillator();
        const osc2   = ctx.createOscillator();
        const filter = ctx.createBiquadFilter();
        const gain   = ctx.createGain();

        osc1.type = 'sawtooth';
        osc2.type = 'sawtooth';
        osc1.frequency.value = frequency;
        osc2.frequency.value = frequency * 1.006; // detune

        // Lowpass filter (analoge karakter)
        filter.type            = 'lowpass';
        filter.frequency.value = Math.min(frequency * 5, 4000);
        filter.Q.value         = 4;

        // ADSR
        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(0.35, now + 0.008);       // Attack
        gain.gain.exponentialRampToValueAtTime(0.18, now + 0.15);   // Decay → Sustain
        gain.gain.setValueAtTime(0.18, now + 0.15);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.4);  // Release

        osc1.connect(filter);
        osc2.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);

        osc1.start(now);
        osc2.start(now);
        osc1.stop(now + 1.5);
        osc2.stop(now + 1.5);
    }

    // ── Toetsenbord mapping ───────────────────────────────────────────────────
    // Minilogue afbeelding 1000×1330px:
    //   - Toetsen starten op ~y = 82% van de afbeeldinghoogte
    //   - Toetsen lopen van x ≈ 3% tot x ≈ 97%
    const KEYS_Y_START = 0.82;
    const KEYS_X_START = 0.03;
    const KEYS_X_END   = 0.97;

    function xToNote(relX) {
        const clamped = Math.max(0, Math.min(1,
            (relX - KEYS_X_START) / (KEYS_X_END - KEYS_X_START)
        ));
        return NOTES[Math.min(Math.floor(clamped * NOTES.length), NOTES.length - 1)];
    }

    // ── Noot-indicator (zweeft bij klik) ─────────────────────────────────────
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
        void indicator.offsetWidth; // force reflow
        indicator.classList.add('visible');
    }

    // ── Initialisatie ─────────────────────────────────────────────────────────
    document.addEventListener('DOMContentLoaded', function () {
        const img = document.querySelector('.instrument-detail__img--minilogue');
        if (!img) return;

        img.style.cursor = 'crosshair';

        img.addEventListener('click', function (e) {
            // getBoundingClientRect geeft de volledige img-positie terug,
            // ook het gedeelte dat boven de viewport is geclipped (negatieve top).
            const rect = img.getBoundingClientRect();
            const relX = (e.clientX - rect.left) / rect.width;
            const relY = (e.clientY - rect.top)  / rect.height;

            // Buiten het toetsenbordgebied? Negeer.
            if (relY < KEYS_Y_START) return;

            const note = xToNote(relX);
            playNote(note.freq);
            showIndicator(note.name, e.clientX, e.clientY);

            // Visuele flash op de afbeelding
            img.classList.add('key-pressed');
            setTimeout(() => img.classList.remove('key-pressed'), 100);
        });
    });

})();

