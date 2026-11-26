# Changelog

## [v3.7.3] - 2026-11-26
### Added
- Aggiunto nelle Impostazioni il box **Condividi App** con QR code per `https://erick.ns0.it/pwa`, pulsante **Copia link** e condivisione tramite Web Share API (**Condividi**).
- Sincronizzato il tasto/gesture **Indietro** di Android e iOS con la navigazione interna dell'app (`history.pushState` e `popstate`) per chiudere overlay/viste o risalire tra le cartelle invece di uscire dalla PWA.

### Changed
- Rinominata la vista principale e la radice di navigazione da `Libreria Musicale` ad **`ARTISTI`**.
- Aggiunto il link al repository GitHub (`https://github.com/erickbaldi/spotifuck-pwa`) come ultima voce dell'elenco informazioni nel box *About*.

### Fixed
- Verificato il caricamento della PWA e degli asset statici sotto `https://erick.ns0.it/pwa/` dietro reverse proxy Nginx preservando la struttura single-file senza Service Worker.

## [v3.7.2]
### Fixed
- Stabilizzazione riproduzione, prefetch e gestione scrobble su Chrome, Edge e Safari.
