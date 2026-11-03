# PRD for Beer Game

**Gruppe:** G28-gravningsmyhr  
**Emne:** IBE160 26H Programmering med KI  
**Dato:** 3. november 2026  
**Versjon:** 0.2 – revidert planleggingsutkast  
**Status:** Kravforslag. Ingen funksjoner er implementert eller testet som del av dette dokumentet.

## 1. Formål og grunnlag

Beer Game skal la en student øve på forsyningskjedestyring alene. Studenten bestiller varer i én av fire roller og ser hvordan beslutningene påvirker lager, restordre, leveranser og kostnader gjennom flere perioder. Etter spillet skal grafer og en oppsummering hjelpe studenten å undersøke bullwhip-effekten.

Dokumentet konkretiserer produktbeskrivelsen og innarbeider anbefalingene i faglærers tilbakemelding datert 6. oktober 2026. Første versjon avgrenses til solo mot regelbaserte medspillere, lagring og gjenopptak, resultatgrafer, KI-oppsummering og enkel lærervisning. Flerspiller med mennesker utsettes.

Avgrensningen er innarbeidet i produktbeskrivelsen som del av denne revisjonen på studentens bestilling. Detaljreglene er fortsatt forslag og PRD-en er ikke godkjent av faglærer. Emnets spesifikke PRD-mal og detaljerte oppgavetekst er ennå ikke tilgjengelige i dette arbeidet.

## 2. Brukere og behov

**Primærbruker:** En student i logistikk, økonomi eller forsyningskjedestyring som vil øve uten å samle fire personer. Studenten trenger forståelige spillregler, tydelige konsekvenser av egne valg og mulighet til å avbryte og fortsette senere.

**Sekundærbruker:** En lærer som vil samle studentene i en klasse og se gjennomføring og resultater. Læreren trenger en enkel oversikt, ikke et fullstendig administrasjonssystem.

**Eksempel på bruk:** Studenten starter et spill som detaljist, leser den lokale lagersituasjonen og legger inn en bestilling. Etter flere perioder oppstår restordre. Studenten fullfører spillet og bruker historikk og grafer til å undersøke om store bestillinger har forsterket svingningene oppover i kjeden.

## 3. Mål og suksesskriterier

| ID | Mål | Hvordan det kontrolleres |
|---|---|---|
| M1 | Studenten kan fullføre et solo-spill i alle fire valgbare roller | Gjennomfør ett komplett testspill per rolle |
| M2 | Spillmotoren følger dokumenterte regler | Automatiske tester mot uavhengig beregnede fasiter, inkludert restordre og ledetid |
| M3 | Et lagret spill kan gjenopptas uten endret tilstand | Sammenlign full tilstand før avbrudd og etter gjenopptak |
| M4 | Resultatene kan etterprøves | Grafpunkter, tabeller og summer samsvarer med lagret periodehistorikk |
| M5 | Studenten får en oppsummering også uten språkmodell | Test både aktiv KI-integrasjon og tydelig merket reserveoppsummering |
| M6 | Læreren kan følge egne klassers spill | Tilgangstester med to lærere og studenter i forskjellige klasser |
| M7 | Sensor kan kjøre kjerneflyten lokalt uten betalte tjenester | Følg README i et rent miljø med lokal lagring og uten API-nøkkel |

Målet i produktbeskrivelsen om at minst 80 prosent viser bedre forståelse beholdes som et framtidig evalueringsmål. Det krever et definert før- og etteropplegg og faktiske deltakere. Det skal ikke framstilles som oppnådd uten slike data.

## 4. Omfang og endringer fra produktbeskrivelsen

### Innenfor første versjon

- Registrering og innlogging i nettversjonen, med student og lærer som brukerroller.
- Solo-spill der studenten velger én rolle og de øvrige styres av dokumenterte regler.
- Fire ledd: detaljist, grossist, distributør og fabrikk.
- En fast, versjonert standardkonfigurasjon for antall perioder, etterspørsel, ledetider og kostnader.
- Validering av bestillinger og visning av lokal tilstand før beslutningen.
- Automatisk lagring av fullførte perioder og gjenopptak.
- Resultattabeller, grafer og forklaring av sentrale begreper.
- KI-generert sluttoppsummering med en regelbasert reservefunksjon.
- Enkel klasse med invitasjonskode og læreroversikt over gjennomføring og resultater.
- Lokal demonstrasjonsmodus som kan brukes uten eksterne kontoer eller hemmeligheter.

### Utenfor første versjon

Flerspiller med mennesker, sanntidssynkronisering, chat, avansert klasseadministrasjon, vurderingsbok, KI som avgjør medspillernes bestillinger, scenario-editor, mobilapp, rangeringer, avansert gjenavspilling, filimport og integrasjon med Canvas eller Moodle.

### Begrunnelse for avgrensningen

Den opprinnelige produktbeskrivelsen inkluderer flerspiller og bredere lærerstøtte. Faglærers tilbakemelding peker på samtidighet og omfang som risiko. Flerspiller flyttes derfor til en senere versjon. Lærerfunksjonene reduseres til én enkel klasseflyt og resultatoversikt. Regelbaserte medspillere gjør simuleringen rask, rimelig og mulig å teste med identiske forutsetninger. De skal merkes som regelbaserte i grensesnittet; språkmodell brukes bare til refleksjon etter spillet.

## 5. Brukerreiser og skjermbilder

### Student

1. Studenten logger inn eller åpner lokal demonstrasjonsmodus.
2. Studenten velger nytt spill, leser reglene og velger rolle. En klasse kan knyttes til spillet før start.
3. Spillbildet viser periode, lokalt lager, restordre, mottatt ordre, mottatt leveranse, varer underveis og kostnader.
4. Studenten legger inn en bestilling og bekrefter. Alle roller behandles i samme periodeovergang.
5. Neste spillbare periode vises etter vellykket lagring. Ved feil beholdes forrige bekreftede tilstand.
6. Studenten kan forlate spillet og fortsette fra siste lagrede beslutningspunkt.
7. Etter siste periode vises resultater for alle fire ledd og en oppsummering.

### Lærer

1. En bruker med lærerrolle oppretter en klasse med navn og invitasjonskode.
2. Studenten knytter et nytt spill til klassen med koden og får vite at læreren får innsyn i progresjon og resultat.
3. Læreren ser egne klasser, tilknyttede spill, gjennomførte perioder, status og kostnader.
4. Læreren åpner resultatvisningen for et spill. Læreren kan ikke endre studentens beslutninger eller spilltilstand.

### Viktigste visninger

**Oversikt:** Start nytt spill, fortsett lagrede spill og se ferdige spill. Tomtilstand forklarer hvordan første spill startes.

**Spill:** En enkel skisse av kjeden markerer studentens rolle. Beslutningsfeltet står sammen med lokale nøkkeltall og en kort forklaring av bestillingen. Full informasjon om andre ledd skjules underveis.

**Resultat:** Sammenlignbare grafer, datatabell, kostnad per ledd og oppsummering. Legender og enheter skal være tydelige. Farger skal suppleres med tekst eller linjemønster.

**Læreroversikt:** Klasser og tilhørende spill med tydelig skille mellom aktive og fullførte spill.

Detaljerte skisser og visuell utforming utarbeides i UX-fasen.

## 6. Foreslåtte spillregler

Alle tall og regler i denne delen er prosjektets forslag til en forenklet undervisningsvariant. De er ikke bekreftet mot en fasit fra emnet eller ment som en påstand om én universell Beer Game-standard. De må gjennomgås før implementering. Konfigurasjonen lagres i hvert spill med regelversjon.

### Standardparametre

| Parameter | Foreslått verdi |
|---|---|
| Perioder | 20 |
| Startlager | 12 enheter per ledd |
| Startrestordre | 0 per ledd |
| Startkø for ordre og leveranser | Tom |
| Ekstern kundeetterspørsel | 4 enheter i periode 1–4, 8 i periode 5–20 |
| Ordreforsinkelse mellom ledd | 1 periode |
| Transporttid mellom ledd | 2 perioder |
| Fabrikkens produksjonstid | 2 perioder fra produksjonsbestilling |
| Lagerkostnad | 0,50 kostnadsenheter per enhet og periode |
| Restordrekostnad | 1,00 kostnadsenhet per enhet og periode |
| Tillatt bestilling | Heltall fra 0 til 100 |

Tom startkø gir en innledende tilpasning som skal forklares for brukeren. Ved sammenligning av strategier må samme konfigurasjon brukes. Grafene skal ikke automatisk påstå bullwhip-effekt bare fordi en serie svinger.

### Periodeovergang

Starttilstanden før periode 1 har ingen kostnad og ingen bestilling. For hver periode t utføres følgende i fast rekkefølge:

1. Leveranser som forfaller i t legges til lageret. Produksjon som forfaller til fabrikken behandles på samme måte.
2. Ny etterspørsel for t mottas. Detaljisten mottar ekstern kundeetterspørsel. De øvrige leddene mottar ordrene som nedstrømsleddet la inn i t−1. Ingen innkommende ordre i periode 1 betyr 0 for disse leddene.
3. Ny etterspørsel legges til eksisterende restordre. Leveransen ut er det minste av tilgjengelig lager og samlet etterspørsel. Alt som ikke kan leveres blir stående som restordre.
4. Leveranser mellom ledd som sendes i t ankommer i t+2. Detaljistens levering til ekstern kunde regnes som fullført i t.
5. Lager- og restordrekostnad beregnes på tilstanden etter utlevering. Periodens kostnad legges til akkumulert kostnad.
6. Tilstanden etter steg 1–5 vises som et klargjort beslutningspunkt for periode t. Klargjøring beregnes uten å endre den sist bekreftede tilstanden. Studenten og medspillerne bestemmer bestillinger med bare den informasjonen som er tillatt for egen rolle. Bestillinger sendes til oppstrømsleddet for mottak i t+1. Fabrikkens beslutning blir en produksjonsbestilling som mottas i t+2.
7. Ved bekreftelse beregner serveren steg 1–6 fra sist bekreftede tilstand og validerer bestillingen og forventet versjon. Beslutninger, køer, historikk og periode lagres samlet. Neste periode kan først behandles etter at denne overgangen er bekreftet.

Alle ledd beregnes fra de samme periodeforutsetningene. Rekkefølgen leddene er lagret i skal ikke gi noen av dem tilgang til nye bestillinger fra samme periode.

**Formler for ett ledd:**

- Tilgjengelig = startlager + mottatt leveranse.
- Samlet etterspørsel = tidligere restordre + ny etterspørsel.
- Sendt = min(tilgjengelig, samlet etterspørsel).
- Sluttlager = tilgjengelig − sendt.
- Sluttrestordre = samlet etterspørsel − sendt.
- Periodekostnad = 0,50 × sluttlager + 1,00 × sluttrestordre.

Lager og restordre er aldri negative og skal ikke begge være positive etter utlevering. Kostnader lagres som heltall i hundredeler eller en tilsvarende eksakt representasjon.

### Regelbaserte medspillere

Foreslått regel bruker lagerposisjon = sluttlager + bekreftede innkommende enheter − sluttrestordre. Mållager er 12 enheter. Bestillingen er min(100, max(0, ny etterspørsel + 12 − lagerposisjon)). Fabrikken bruker samme regel for produksjon. Bekreftede innkommende enheter omfatter utsendte varer og planlagt produksjon, ikke bestillinger som ennå ikke er sendt fra leverandøren.

Regelen er en enkel pedagogisk strategi, ikke en optimaliseringsalgoritme. Parametre og regelversjon lagres slik at et spill kan gjenskapes. Medspillerne får ikke se framtidig ekstern etterspørsel eller studentens ubekreftede beslutning.

### Avslutning

Spillet stopper etter periode 20. Det er ingen ekstra tømming av kjeden. Uleverte restordre og varer underveis vises separat. De får ingen skjult sluttkostnad. Samlet kostnad er summen av bokførte periodekostnader. Resultatsiden forklarer at dette er et avgrenset læringsscenario.

### Regneeksempel for utlevering

Eksemplet gjelder ett ledd og kontrollerer bare lager, restordre og kostnader. Mottatte leveranser er oppgitte testdata, ikke et beregnet fullstendig kjedeforløp.

| Periode | Startlager | Mottatt | Ny etterspørsel | Tidligere restordre | Sendt | Sluttlager | Sluttrestordre | Kostnad |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 12 | 0 | 4 | 0 | 4 | 8 | 0 | 4,00 |
| 2 | 8 | 0 | 4 | 0 | 4 | 4 | 0 | 2,00 |
| 3 | 4 | 0 | 8 | 0 | 4 | 0 | 4 | 4,00 |
| 4 | 0 | 6 | 8 | 4 | 6 | 0 | 6 | 6,00 |
| 5 | 0 | 10 | 4 | 6 | 10 | 0 | 0 | 0,00 |

Sum kostnad er 16,00. Før spillmotoren godtas, må det i tillegg lages en uavhengig kontrollert fasit for 5–10 perioder med alle fire ledd, ordre, transport og produksjon.

## 7. Funksjonskrav og akseptansekriterier

| ID | Krav | Akseptansekriterier |
|---|---|---|
| F01 | Registrering og innlogging | Student kan registrere seg, logge inn og ut. Feil innlogging gir forståelig melding. Ingen hemmeligheter eller passord logges. |
| F02 | Tilgangskontroll | Student ser bare egne spill. Lærer ser bare spill tilknyttet egne klasser. Direkte forespørsel etter annen brukers spill avvises. |
| F03 | Nytt spill | Student velger én av fire roller og ser reglene. Start oppretter entydig spill-ID, konfigurasjon, regelversjon og starttilstand. |
| F04 | Bestilling | 0 og 100 aksepteres. Negative tall, desimaltall, tomt felt, tekst og verdier over 100 avvises uten tilstandsendring. |
| F05 | Periodebehandling | Alle ledd følger reglene i del 6. Dobbeltklikk eller gjentatt forespørsel behandler ikke samme periode flere ganger. |
| F06 | Medspillere | De tre øvrige rollene bruker samme versjonerte regel. Identisk tilstand og konfigurasjon gir identiske bestillinger. |
| F07 | Spillinformasjon | Student ser lokal tilstand og egne historiske beslutninger. Andre ledds skjulte data og framtidig etterspørsel eksponeres ikke gjennom nettversjonens spill-API. |
| F08 | Lagring og gjenopptak | Oppfriskning og ny innlogging gjenoppretter siste bekreftede tilstand, inkludert alle køer og historikk. Ved lagringsfeil kan beslutningen forsøkes igjen uten duplisering. |
| F09 | Resultater | Etter siste periode er spillet skrivebeskyttet. Tabeller og grafer viser ordre, lager, restordre og kostnad per ledd. Kostnadssummer stemmer med periodehistorikken. |
| F10 | KI-oppsummering | Oppsummering bygges fra faktiske spilldata. Den skiller observerte tall fra mulige forklaringer, og finner ikke på beslutninger eller læringsresultater. |
| F11 | Reserveoppsummering | Manglende nøkkel, tidsavbrudd eller feil gir en regelbasert oppsummering merket som dette. Spill og resultatvisning fungerer fortsatt. |
| F12 | Klasse | Lærer kan opprette klasse. Student kan knytte nytt spill til gyldig invitasjonskode. Ugyldig kode gir feil uten å endre spillet. |
| F13 | Læreroversikt | Lærer ser egne klassers spill med studentidentifikator, status, periode og kostnad og kan åpne resultater. Det gis ingen tilgang til andre klasser. |
| F14 | Lokal demonstrasjon | README gir nøyaktig oppstart av et lokalt spill med lokal database og demoidentiteter. Ingen betalte kontoer eller eksterne nøkler trengs. Demoautentisering kan ikke aktiveres i offentlig produksjonsmiljø. |

## 8. Krav til kvalitet

| ID | Krav | Kontroll |
|---|---|---|
| K01 | Spillmotoren er isolert fra visning, database og språkmodell | Kjør motorens tester uten nettverk og uten brukergrensesnitt |
| K02 | Beslutning og lagring er én konsistent overgang | Test avbrudd, gjentatt forespørsel og to åpne faner på samme spill |
| K03 | Spillet kan brukes med tastatur og har synlig fokus | Manuell gjennomgang av kjerneflyten uten mus |
| K04 | Skjemafelter har etiketter og feil forklares i tekst | Test ugyldig input og kontroll av etiketter og feilmeldinger |
| K05 | Visningen fungerer på mobil og datamaskin | Kontroller bredder på 360, 768 og 1440 piksler; tabeller kan rulles ved behov |
| K06 | En vanlig periode uten språkmodell svarer innen to sekunder i testmiljø | Mål en serie på 20 overganger og dokumenter miljø og eventuelle avvik |
| K07 | Språkmodell har endelig tidsgrense og begrenset gjenforsøk | Foreslått grense 15 sekunder per forsøk, høyst ett automatisk gjenforsøk; test reservefunksjonen |
| K08 | Kjerneflyten virker uten språkmodell | Fullfør lokalt spill og åpne resultater uten API-nøkkel |
| K09 | Feil gir forståelig melding og bevarer bekreftede data | Test nettverksfeil, lagringsfeil og utilgjengelig modell |
| K10 | README beskriver faktisk kjøring | Uavhengig oppstart etter dokumentasjonen og dokumentert resultat |

Tidsmålene er foreslåtte akseptansemål, ikke målte resultater. Teknologivalg, versjoner og endelige ytelsesgrenser avklares i arkitekturfasen.

## 9. Data, tilgang og KI-integrasjon

Løsningen trenger brukeridentitet og rolle, klasse med lærer og invitasjonskode, spill med eier og eventuell klasse, konfigurasjon, tilstand for hvert ledd, ordre- og leveransekøer, periodehistorikk og oppsummering med kilde og status.

Tilstanden skal gjøre gjenopptak mulig uten å spørre språkmodellen om tidligere hendelser. Historiske spill skal beholde sine opprinnelige regler selv om standardkonfigurasjonen senere endres.

Lærerrolle skal tildeles gjennom en kontrollert mekanisme. En bruker skal ikke kunne få innsyn i studentdata ved å velge lærerrolle selv. Konkret løsning beskrives i arkitekturen.

Språkmodellkall gjøres på serversiden med nøkkel fra miljøvariabel. Oppsummeringen trenger spillparametre og aggregerte eller relevante periodeverdier, ikke navn, e-post eller klassekode. Eksempel: «Bestillingen din økte fra X til Y i periode t» må kontrolleres mot faktiske data. Teksten skal forklare mulige mekanismer uten å slå fast årsak eller forbedret læring uten grunnlag.

Hvert spill skal gjenbruke en lagret vellykket oppsummering i stedet for å generere på hver sidevisning. Uautorisert tilgang, ubegrensede gjenforsøk og vilkårlige klientprompter skal avvises. Endelig modell, kostnadsramme, behandling av sletting og oppbevaring av studentdata må avklares før offentlig bruk med reelle deltakere.

## 10. Teknologiske føringer og åpne valg

- Vercel er publiseringsmålet i emnet. Arkitekturen skal kunne driftes der uten en uavklart ekstra hostingtjeneste.
- Databasetjeneste, rammeverk og autentiseringsløsning velges og begrunnes i arkitekturfasen. Ingen av dem regnes som allerede valgt eller installert.
- Lokal kjøring skal ha en reell lagringsløsning og demonstrasjonsdata uten gruppens private infrastruktur.
- Hemmeligheter lagres i lokale miljøfiler og Vercels miljøvariabler. Repoet får kun eksempelfil med tomme eller ufarlige verdier.
- Planen skal holdes selvstendig fra lærerens eksempelrepo. Egne valg, regler og resultater dokumenteres. Ingen dokumenter eller kode fra eksempelprosjektet kopieres inn som eget arbeid.

## 11. Testplan og sporbarhet

| Testområde | Krav | Minimum før godkjenning |
|---|---|---|
| Beregninger | F05–F06, M2 | Uavhengig kontrollert fasit for hele kjeden; lager, restordre, ordreledetid, transport, produksjon, nullbestilling og kostnadssummer |
| Inndata | F04 | Grenseverdier og ugyldige verdier, både i grensesnitt og på server |
| Persistens | F05, F08, K02 | Gjenopptak, feil ved lagring, dobbeltklikk og konkurrerende faner |
| Tilgang | F01–F02, F12–F14 | To studenter, to lærere, adskilte klasser og forsøk på direkte tilgang |
| Resultater | F09 | Grafpunkter og tabeller sammenholdes med lagret historikk og håndberegnet sum |
| KI | F10–F11, K07–K08 | Korrekt datagrunnlag; manglende nøkkel, feilrespons og tidsavbrudd; manuell kontroll av tekstens påstander |
| Brukerreise | M1, F03–F09 | Fullfør ett spill i hver rolle, inkludert avbrudd og gjenopptak |
| Brukervennlighet | K03–K05 | Tastatur, mobilbredde, tomtilstander og forståelige feilmeldinger |
| Levering | F14, K10 | Ren lokal oppstart og testkjøring etter README samt kontroll av publisert kjerneflyt |

Testresultater føres med dato, versjon, forventet og faktisk utfall. Feil som avdekkes registreres og kobles til rettingen. Denne PRD-en angir planlagte tester; den dokumenterer ingen beståtte tester.

## 12. Foreslått utviklingsrekkefølge

| Trinn | Leveranse | Ferdig når |
|---|---|---|
| 1 | Avklart PRD og revidert produktbeskrivelse | Omfang og regler er gjennomgått; uavklarte punkter er registrert |
| 2 | UX, arkitektur og stories | Hver story har krav-ID og testbare akseptansekriterier; lokal drift og Vercel er forklart |
| 3 | Spillmotor | Fullkjedefasit og meningsfulle automatiske tester stemmer |
| 4 | Lokal spillflyt og lagring | Ett helt spill kan spilles, avbrytes, gjenopptas og avsluttes |
| 5 | Resultater og oppsummering | Grafer og reserveoppsummering virker; modellintegrasjon tåler feil |
| 6 | Nettinnlogging og enkel lærerflyt | Eierskap, klasse og tilgangstester fungerer |
| 7 | Kvalitetssikring og publisering | README er prøvd, kjerneflyt er kontrollert på Vercel og adressen er dokumentert |

Trinnene er milepæler innen samme foreslåtte v1. Lærerfunksjoner er ikke fjernet fra sluttscope selv om de bygges etter kjernen. Hvis omfanget må reduseres ytterligere, skal endringen begrunnes og avklares før leveranse.

## 13. Prosess og dokumentasjon

Krav-ID-er brukes videre i epics, stories, tester og relevante endringsbeskrivelser. Arbeidet deles i faktiske avgrensede endringer med beskrivende commits. Planen oppdateres når krav eller regler endres.

KI-økter dokumenteres med oppgave, gitt kontekst, sentrale prompts, forslag som ble vurdert, studentens egne beslutninger, endringer og faktisk validering. Dokumentasjon skal være sannferdig og skrives underveis. Tidligere aktiviteter, manuelle tester eller selvstendige vurderinger skal ikke konstrueres i ettertid.

Foreslått dokumentstruktur er planlegging, beslutninger, stories og tester under en tydelig dokumentasjonsmappe, eventuelt emnets BMAD-struktur. Eksisterende dokumenter flyttes først når lenker og historikk kan ivaretas. Sesjonslogg følger repoets egne regler ved faktisk arbeid i repoet.

## 14. Åpne punkter før implementering

1. Kontroller PRD-formatet mot emnets konkrete oppgave og eventuelle BMAD-krav. Denne teksten er ikke generert gjennom en installert BMAD-arbeidsflyt.
2. Arbeidsavgrensningen er solo, regelbaserte medspillere og enkel læreroversikt. Eventuelle senere endringer dokumenteres.
3. Avklar standardparametrene, særlig antall perioder, tom startkø, transport, ordreforsinkelse og informasjon studenten kan se. Kontroller mot eventuelle Beer Game-regler i undervisningen.
4. Lag og kontroller fullkjedefasit for 5–10 perioder før spillmotoren implementeres.
5. Arkitekturforslaget beskriver Next.js og Supabase med lokal stack; valider tekniske valg i en liten oppstartsoppgave før implementering.
6. Avklar modellleverandør, kostnadsramme, oppbevaring og sletting av data.
7. Produktbeskrivelsen er oppdatert med avgrensning og navngitte alternativer. Kontroller videre at den følger faktiske endringer gjennom utviklingen.

## 15. Kilder og dokumentstatus

- Gruppens produktbeskrivelse: https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/product-brief.md
- Faglærers tilbakemelding, datert 6. oktober 2026: https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/tilbakemelding-product-brief.md
- Sensorveiledning IBE160 – Del 1 applikasjon og prosess, høst 2026, 7 sider, levert av studenten.
- Appendix A – Tool Installation and Setup Guides, 27 sider, levert av studenten. Installasjonsveiledning, ikke PRD-mal eller fastsatt arkitektur.
- Emnetekst og kunngjøringer levert av studenten, inkludert PRD-påminnelse 2. november og Vercel-kunngjøring 29. oktober 2026.

PRD-en er utarbeidet med KI-støtte i denne økten. Foreslåtte regler og prioriteringer er utkast til studentens vurdering. Revisjonen omfatter planleggingsdokumenter i en egen GitHub-gren. Appkode, installasjon og publisering inngår ikke i denne dokumentleveransen.