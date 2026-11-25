# spotiFUCK PWA

Progressive Web App (PWA) client-side dedicata allo streaming musicale tramite API Subsonic (`v1.16.1`), progettata per offrire un'interfaccia leggera, rapida e priva di attriti rispetto all'app web completa.

> *"no fees, no advertising, no interruptions"*

## Funzionalità Principali

- **Buffering e Prefetch in RAM:** Scaricamento in background fino a 2 brani successivi come `Blob` tipizzati per cambi traccia rapidi senza attese di rete.
- **Isolamento Sessione e Credenziali:** Namespace dedicato (`pwa_sub_*`), Player ID separato (`spotifuck-pwa-player`) e `credentials: 'omit'` per limitare interferenze con la web app principale.
- **Scrobbling e Stato Player:** Invio stato *Now Playing* (`submission=false`) e scrobble (`submission=true`) basato su metadati audio reali (`loadedmetadata`), con controllo del brano attivo.
- **Player Completo:** Mini player, player a schermo intero, ricerca contestuale, preferiti (`star`/`unstar`), shuffle, repeat (`off` / `all` / `one`), testi (`getLyrics`) e ispezione metatag.

## Stato Compatibilità Browser (Milestone `v3.7.2`)

| Browser | Prefetch & Buffer | Isolamento Sessione / Player | Scrobble (Album & Singoli) |
| :--- | :---: | :---: | :---: |
| **Google Chrome** | OK | OK | OK |
| **Microsoft Edge** | OK | OK | OK (risolto in `v3.7.2`) |
| **Safari (iOS / macOS)** | OK | Da rifinire (policy ITP / cookie) | OK |

## Configurazione e Avvio

1. Apri l'applicazione tramite un web server locale o HTTPS (necessario per il comportamento completo da PWA).
2. Vai su **Impostazioni** (`icona ingranaggio`), inserisci **Nome Utente** e **Password** per il server `https://erick.ns0.it` e salva.
3. Per installarla sulla schermata Home: usa **Installa Ora** (quando disponibile) oppure il menu del browser (*Aggiungi a schermata Home* / *Installa app*).

## Autore e Crediti

- Sviluppato da **Erick** ([erickbaldi.github.io](https://erickbaldi.github.io))
- Server di riferimento: [erick.ns0.it](https://erick.ns0.it)
