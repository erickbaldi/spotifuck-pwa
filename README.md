# spotiFUCK PWA

Progressive Web App (PWA) client-side dedicata allo streaming musicale tramite API Subsonic (`v1.16.1`), progettata per offrire un'interfaccia leggera, rapida e priva di attriti rispetto all'app web completa.

> *"no fees, no advertising, no interruptions"*

## Funzionalità Principali

- **Buffering e Prefetch in RAM:** Scaricamento in background fino a 2 brani successivi come `Blob` tipizzati per cambi traccia rapidi senza attese di rete.
- **Isolamento Sessione e Credenziali:** Namespace dedicato (`pwa_sub_*`), Player ID separato (`spotifuck-pwa-player`) e `credentials: 'omit'` per limitare interferenze con la web app principale.
- **Scrobbling e Stato Player:** Invio stato *Now Playing* (`submission=false`) e scrobble (`submission=true`) basato su metadati audio reali (`loadedmetadata`), con controllo del brano attivo.
- **Player Completo:** Mini player, player a schermo intero, ricerca contestuale, preferiti (`star`/`unstar`), shuffle, repeat (`off` / `all` / `one`), testi (`getLyrics`) e ispezione metatag.
- **Server Locale Integrato:** Script Python (`spotifuck-pwa-server.py`) per servire i file della cartella del progetto sulla porta `7575`.

## Stato Compatibilità Browser (Milestone `v3.7.2`)

| Browser | Prefetch & Buffer | Isolamento Sessione / Player | Scrobble (Album & Singoli) |
| :--- | :---: | :---: | :---: |
| **Google Chrome** | OK | OK | OK |
| **Microsoft Edge** | OK | OK | OK (risolto in `v3.7.2`) |
| **Safari (iOS / macOS)** | OK | Da rifinire (policy ITP / cookie) | OK |

## Configurazione e Avvio

1. Avvia il server locale dalla cartella del progetto (richiede Python 3):
   ```bash
   python3 spotifuck-pwa-server.py
