# spotiFUCK PWA

Progressive Web App (PWA) client-side dedicata allo streaming musicale tramite API Subsonic (`v1.16.1`), progettata per offrire un'interfaccia leggera, rapida e priva di attriti rispetto all'app web completa.

> *"no fees, no advertising, no interruptions"*

---

## Caratteristiche Principali

* **Buffering e Prefetch in RAM:** Scaricamento in background della traccia successiva (fino a 2 brani in cache) tramite `Blob` tipizzati (`getMimeTypeForTrack()`) per cambi traccia istantanei e senza interruzioni su tutti i dispositivi.
* **Isolamento Sessione e Credenziali:** Utilizzo di un namespace dedicato (`pwa_sub_*`), di un Player ID separato (`spotifuck-pwa-player`) e di chiamate `fetch` con `credentials: 'omit'` per evitare conflitti di sessione con l'applicazione web principale ospitata sullo stesso dominio.
* **Scrobbling Affidabile su Last.fm:** Invio immediato dello stato *Now Playing* (`submission=false`) e registrazione dello scrobble definitivo (`submission=true`) calcolato sui metadati reali del file audio (`loadedmetadata`), con controllo anti-desincronizzazione dell'ID brano e bypass delle policy anti-tracking di Microsoft Edge (`cache: 'no-store'`).
* **Player Completo e Responsive:**
  * Mini player persistente e player a schermo intero.
  * Ricerca contestuale dinamica (per artista, album, sottocartella o brano).
  * Gestione dei preferiti sincronizzata con il server (`star` / `unstar`).
  * Modalità Shuffle, Repeat (`Off`, `All`, `One`) e integrazione nativa con la `MediaSession API` del sistema operativo.
  * Visualizzazione dei testi (`getLyrics`) e ispezione dei metatag tecnici del brano (formato, bitrate, dimensione file, anno, genere).
* **Server HTTP Locale Integrato:** Include lo script Python `spotifuck-pwa-server.py` per avviare rapidamente un server statico sulla porta `7575`.

---

## Stato Compatibilità Browser (`v3.7.2`)

| Browser | Prefetch & Buffer in RAM | Isolamento Sessione / Player | Scrobble (Album & Singoli) |
| :--- | :---: | :---: | :---: |
| **Google Chrome** | OK | OK | OK |
| **Microsoft Edge** | OK | OK | OK *(risolto in v3.7.2)* |
| **Safari (iOS / macOS)** | OK | Da rifinire *(policy ITP / cookie)* | OK |

---

## Struttura del Repository

```text
spotifuck-pwa/
├── index.html                  # Codice sorgente completo della PWA (v3.7.2)
├── spotifuck-pwa-server.py     # Server HTTP statico locale sulla porta 7575
├── README.md                   # Documentazione del progetto
├── CHANGELOG.md                # Storico delle versioni e delle modifiche
└── pwa/                        # Asset grafici e icone PWA
    ├── spotifuck_logo_mini.png
    └── spotifuck_bckgnd_w.png
```

---

## Configurazione e Avvio Locale

1. **Clona il repository:**

   ```bash
   git clone https://github.com/erickbaldi/spotifuck-pwa.git
   cd spotifuck-pwa
   ```

2. **Avvia il server Python locale** (richiede Python 3):

   ```bash
   python3 spotifuck-pwa-server.py
   ```

   Lo script imposta automaticamente la directory corrente come root del server e resta in ascolto sulla porta **`7575`**.

3. **Accedi dall'interfaccia web:**

   * Apri il browser all'indirizzo `http://localhost:7575` (oppure pubblica i file su un server web con certificato HTTPS per abilitare tutte le funzioni PWA).
   * Clicca sull'icona **Impostazioni** in alto a destra, inserisci **Nome Utente** e **Password** del server `https://erick.ns0.it` e premi **Salva e Connetti**.

4. **Installazione come App (PWA):**

   * Utilizza il banner modale **Installa Ora** alla prima apertura, oppure seleziona *Installa app* / *Aggiungi a schermata Home* dal menu del browser.

---

## Autore e Crediti

* **Sviluppatore:** [Erick](https://erickbaldi.github.io)
* **Server Subsonic:** [erick.ns0.it](https://erick.ns0.it)
* **Repository:** [github.com/erickbaldi/spotifuck-pwa](https://github.com/erickbaldi/spotifuck-pwa)