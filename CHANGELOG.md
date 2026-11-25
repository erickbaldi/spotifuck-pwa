# Changelog

Tutte le modifiche rilevanti a **spotiFUCK PWA** sono documentate in questo file.

## [v3.7.2] - Stabile e Definitiva

### Corretto
- Aggiunto `cache: 'no-store'` in `sendScrobble` (e nelle chiamate API Subsonic) per superare i blocchi anti-tracking / caching asincrona su **Microsoft Edge** durante la riproduzione di album completi.

## [v3.7.1]

### Corretto
- Aggiornata la gestione del timer di scrobble in `playTrack()` attendendo `loadedmetadata` quando `audioElement.duration` non è ancora disponibile all'avvio del `Blob`.
- Aggiunto il controllo sull'ID del brano corrente (`currentPlaylist[currentIndex]?.id === currentTrackId`) per evitare scrobble disallineati in caso di cambio traccia rapido.

## [v3.7.0] - Milestone Buffering e Prefetch

### Aggiunto
- Caricamento audio tramite `fetch(..., { credentials: 'omit' })` convertito in `Blob` con MIME type esplicito (`getMimeTypeForTrack()`) per migliorare la decodifica e ridurre i blocchi di streaming.
- Cache in memoria (`blobCache`) con prefetch in background della traccia successiva (fino a 2 elementi in RAM) e rilascio controllato tramite `URL.revokeObjectURL()`.
- Isolamento delle credenziali (`pwa_sub_user`, `pwa_sub_pass`) e identificatore player dedicato (`spotifuck-pwa-player`).
