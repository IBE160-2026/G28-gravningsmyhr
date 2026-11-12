# Tilbakemelding på PRD

| | |
|---|---|
| **Gruppe** | G28 – G28-gravningsmyhr |
| **PRD vurdert** | `docs/planning/prd.md` (ingen frontmatter; status i teksten: «Kravgrunnlag», versjon 0.2; sist endret 2026-11-03, commit 49d72b0) |
| **Dato** | 2026-11-12 |
| **Type** | Formativ tilbakemelding, ikke karakter |

## 1. Samlet inntrykk

PRD-en har substans: spillreglene er konkrete, det finnes et regneeksempel som stemmer, og kravene har akseptansekriterier som i stor grad kan bli testtilfeller. Største risiko er at dokumentet ikke har én sannhet om hva som er v1. Toppnotatet sier at KI-oppsummering (F10) er utsatt, mens resten av PRD-en fortsatt beskriver den som en del av leveransen. Læringsmålet (å undersøke bullwhip-effekten) har heller ingen krav som kan testes.

## 2. Dette fungerer godt

- **Regler som kan kontrolleres.** §6 har parametertabell, fast rekkefølge i periodeovergangen, formler og et regneeksempel («Sum kostnad er 16,00»). Jeg har regnet gjennom eksemplet, og det stemmer. Kravet om fullkjedefasit før spillmotoren godtas er den riktige kvalitetssikringen.
- **Ærlig om hva som er forslag.** «Alle tall og regler i denne delen er prosjektets forslag … ikke bekreftet mot en fasit» og «Denne PRD-en … dokumenterer ingen beståtte tester» gir et sannferdig grunnlag. Målene i §3 har en kolonne for «Hvordan det kontrolleres».
- **KI og kostnad er tenkt gjennom.** K07 (15 sekunder, ett gjenforsøk), K08/F11 (kjerneflyt og reserveoppsummering uten nøkkel), og §9 (lagre vellykket oppsummering, ingen klientprompter, ingen persondata til modellen). Dette er sjelden så konkret i PRD-er på dette nivået.

## 3. Oversikt per dimensjon

| Dimensjon | Vurdering | Kort begrunnelse |
|---|---|---|
| Beslutningsklarhet | god | Avgrensning og begrunnelse (§4) er tydelige, men beslutningen om F10 ligger i et toppnotat og er ikke ført inn i scope. |
| Substans | sterk | Konkrete regler, tall og fasit. Ingen pynte-personas eller boilerplate-NFR-er. |
| Strategisk sammenheng | god | Tydelig kjerne (solo, regelbasert, gjenopptak, resultater), men ingen krav måler det pedagogiske målet bullwhip. |
| Testbarhet | god | F04, F05, F08 og K-kravene er testbare. F01, F07, F09, F10 og F13 bruker uttrykk som «forståelig», «viser» og «finner ikke på». |
| Scope og avgrensning | god | «Utenfor første versjon» er eksplisitt. V1 er likevel stor (innlogging, klasser, lærervisning, Vercel) for en liten gruppe, og F10 er endret uten å oppdatere scope. |
| Brukbarhet for neste fase | god | §11 kobler krav til tester, og ID-ene er stabile. Mangler glossar, og informasjon per rolle er udefinert. |
| Formtilpasning | god | Dokumentet er tilpasset en simulering. Brukerreisene har ingen ID-er eller navngitt hovedperson. §14 sier selv at dokumentet ikke er laget med en BMAD-arbeidsflyt. |

## 4. Viktigste forbedringer

### 4.1 Én sannhet om F10 og F11
- **Alvorlighet:** høy
- **Hvor:** toppnotatet («F10 … er utsatt, mens F11 er aktiv løsning») mot §4 («KI-generert sluttoppsummering med en regelbasert reservefunksjon»), M5, K07 og §12 trinn 5.
- **Problem og hvorfor det betyr noe:** Stories og tester som hentes fra PRD-en vil lage KI-arbeid som gruppen har valgt bort. «Beslutning etter implementering» hører dessuten ikke hjemme i et kravdokument som kalles «Kravgrunnlag».
- **Forslag:** Før beslutningen inn i §4: «Innenfor v1: regelbasert oppsummering (F11). Utenfor v1: språkmodell-oppsummering (F10), fordi nøkkel, kostnad og kontroll av påstander ikke er avklart.» Flytt leveransestatus til `leveransestatus.md`, og la PRD-en vise endringen i en kort endringslogg.

### 4.2 Gi bullwhip-målet et testbart krav
- **Alvorlighet:** høy
- **Hvor:** §1 «hjelpe studenten å undersøke bullwhip-effekten»; F09 «viser ordre, lager, restordre og kostnad».
- **Problem og hvorfor det betyr noe:** Ingen FR eller M sier hva studenten faktisk skal kunne se. Uten det blir grafene pynt, og UX og tester mangler et mål.
- **Forslag:** «F09b: Resultatsiden viser for hvert ledd variansen i egne bestillinger delt på variansen i kundeetterspørselen. *Konsekvenser:* verdien for hvert ledd stemmer med en håndberegnet verdi for fasitspillet; ved null varians i etterspørselen vises «ikke beregnet», ikke feil; teksten påstår ikke bullwhip om forholdstallet er under 1.»

### 4.3 Skriv om vage akseptansekriterier
- **Alvorlighet:** medium
- **Hvor:** F10 «Den skiller observerte tall fra mulige forklaringer, og finner ikke på beslutninger»; F01 «forståelig melding»; F09 «viser».
- **Problem og hvorfor det betyr noe:** En tester kan ikke avgjøre om dette er oppfylt, så det blir ikke et testtilfelle.
- **Forslag (hvis F10 gjeninnføres):** «Hvert tall i teksten finnes i periodehistorikken for spillet; testen kjører med en mock-modell som returnerer et falskt tall, og dette fanges og erstattes av reserveoppsummeringen.» Gjør tilsvarende for F01 (f.eks. fast feilmeldingstekst per feiltype).

### 4.4 Definer informasjon per rolle
- **Alvorlighet:** medium
- **Hvor:** §6 trinn 6 «bare den informasjonen som er tillatt for egen rolle»; F07; åpent punkt 3.
- **Problem og hvorfor det betyr noe:** Dette styrer skjermbildet, API-et, tilgangstestene og medspillerregelen, men er ikke avgjort.
- **Forslag:** En tabell «Rolle × synlig informasjon» (eget lager, restordre, innkommende ordre denne perioden, egne leveranser underveis, egne tidligere bestillinger) og en linje om hva som aldri vises.

### 4.5 Legg til et kort glossar
- **Alvorlighet:** medium
- **Hvor:** hele dokumentet. Ledd, rolle, spiller og medspiller brukes om samme eller nærliggende ting. Det samme gjelder bestilling og ordre, samt oppsummering, KI-oppsummering og reserveoppsummering.
- **Problem og hvorfor det betyr noe:** Ulik bruk gir ulike navn i kode, databasefelt og stories.
- **Forslag:** 8–10 termer, for eksempel «Ledd – ett av fire steg i kjeden (detaljist, grossist, distributør, fabrikk). Rolle – ledd som studenten styrer. Medspiller – ledd styrt av regelen i §6.»

## 5. Mekaniske funn

- ID-ene F01–F14, M1–M7 og K01–K10 er sammenhengende, og §11 refererer riktig til dem. Lenkene til `../implementation.md`, `../testing.md` og `../leveransestatus.md` løser seg.
- Brukerreiser (§5) har ingen ID-er (UJ-1 …) og ingen navngitt hovedperson. FR-ene viser ikke til brukerreise eller mål, bare via §11.
- §10 sier at ingen teknologi er valgt, mens §14 punkt 5 nevner Next.js og Supabase. Presiser hva som er forslag og hva som er bundet (Vercel).
- Ingen `[ASSUMPTION]`-merking. Ordet «foreslått» brukes konsekvent i stedet, og det fungerer. Det finnes ingen motmål (f.eks. at bullwhip-påstander ikke skal overdrives) blant M-ene.
- Eksempeltabellen i §6 bruker etterspørsel 4, 4, 8, 8, 4, som ikke samsvarer med standardparametrene (4 i 1–4, 8 i 5–20). Det er forklart som testdata, men sett en markering ved tabellen.

## 6. Før dere går videre

**Må avklares nå:** (1) F10/F11 i scope (4.1). (2) Informasjon per rolle (4.4). (3) Fullkjedefasit for 5–10 perioder, slik §14 punkt 4 selv krever. (4) Hva «bullwhip» betyr som måltall (4.2).
**Kan vente:** modellleverandør, kostnadsramme og sletting av data (kun relevant hvis F10 kommer tilbake), samt eksakte ytelsesgrenser.

**Oppfølging av tilbakemelding på product brief:** ja. Solo mot regelbaserte medspillere, parametre og regneeksempel, studenten som primærbruker, lokal kjøring uten nøkkel og reserveoppsummering er alle fulgt opp. Fullkjedefasit er planlagt, men ikke vist.

## 7. Refleksjonsspørsmål

1. Parameterne i §6 (lagerkostnad 0,50, restordre 1,00, transport 2 perioder) er merket som forslag. Hvordan kontrollerte dere dem mot emnets Beer Game-regler, og hva har dere endret etter KI-forslagene?
2. Dere valgte regelbasert oppsummering i stedet for språkmodell. Hvordan sikrer dere at PRD, tester og ferdig app sier det samme om dette valget, og hvordan ville dere kontrollert en KI-tekst mot spilldataene?

_Vurdert mot kvalitetsrubrikken i bmad-prd. Dette er veiledning, ikke sensur._
