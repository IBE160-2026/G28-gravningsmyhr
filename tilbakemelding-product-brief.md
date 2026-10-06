# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G28 – G28-gravningsmyhr |
| **Product brief** | `product-brief.md` (commit `815296d`) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

## Samlet vurdering

- **Godt utgangspunkt med justeringer.** Gruppen kan gå videre og innarbeide punktene under.

Vi har vurdert `product-brief.md` i repoets rot. Dere har valgt samme tema som faglærers eksempelprosjekt (https://github.com/IBE160-2026/beergame). Det er lov å bruke eksempelet som inspirasjon, men vær klar over at sensor vil se begge repoene. Det blir derfor ekstra viktig at deres egne valg, avgrensninger og prosess kommer tydelig fram, og at dere ikke kopierer dokumenter eller kode fra eksempelrepoet.

**Det som er bra:**

1. Suksesskriteriene er konkrete og funksjonelle, for eksempel «En bruker kan fullføre et spill med AI i de øvrige rollene», «Bestillinger, lager, restordre, leveranser og kostnader beregnes og vises korrekt» og «Spillstatus bevares ved avbrudd». De kan nesten direkte bli testtilfeller. Dere skiller også ærlig mellom disse og målet om 80 % bedre forståelse.
2. Briefen er kort, ryddig og på norsk, med en tydelig kjerneflyt: velg rolle, bestill gjennom flere perioder, se grafer over bullwhip-effekten og få en AI-oppsummering av egne beslutninger.

**De viktigste endringene:**

1. Omfanget i «Innenfor første versjon» er stort. Det omfatter innlogging, flerspiller med mennesker og/eller AI, lærerfunksjoner med klasser og progresjon, lagring, visualisering og AI-oppsummering. Flerspiller med mennesker krever sanntid og samtidighet, og er det mest risikable. Gjør solo mot AI til kjernen i v1.
2. Spesifiser spillreglene og parameterne i v1: antall perioder, ledetid, kostnad per enhet på lager og i restordre, og etterspørselsmønster. Uten dette kan dere ikke kontrollere at beregningene er «korrekte», slik suksesskriteriet krever.
3. Beskriv hvem som er primærbruker for v1. Nå er det studenter, lærere og individuelle brukere, og læreren har en egen funksjonsflate. Velg studenten som primærbruker og gjør læreren sekundær.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Vanskelig**

**Sammenlignbart med:** 3) KI-styrt simulering av prosjektledelse (vanskelig). Begge er simuleringer der beregninger over flere perioder må stemme, med KI-støtte og resultatvisning. Avgrenset til solo mot AI med enkel lærervisning, ligger prosjektet nærmere middels.

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | høy | Lager, restordre, leveranser med ledetid, bestillinger og kostnader for fire roller per periode. Logikken er velkjent, men må stemme nøyaktig. |
| Datamodell – antall entiteter og relasjoner mellom dem | middels | Bruker, spill, rolle/spiller, periode-tilstand per rolle, bestillinger, klasse og lærer. |
| Brukere, roller og innlogging | middels | Registrering og innlogging med to roller (student og lærer). |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | middels | AI-medspillere og AI-oppsummering. Medspillerne kan gjerne være regelbaserte (for eksempel en enkel bestillingsregel) i stedet for språkmodell. Det er billigere, raskere og lettere å teste. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | lav | Bare språkmodell for oppsummeringen. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | høy | Flerspiller med mennesker betyr at fire personer må bestille i samme periode og vente på hverandre. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | lav | Ingen filhåndtering i v1. |
| Sikkerhet og personvern | lav | Studentkontoer og spilldata. Lærerens innsyn i studentenes progresjon krever tilgangskontroll. |

**Hva vanskelighetsgraden betyr for dere:**

- _Vanskelig:_ Et vanskelig prosjekt gir større mulighet for toppkarakter, men også større risiko. Definer en minimal versjon som sikkert kan bli ferdig, og legg resten i tydelige trinn etterpå. For dere er en god minimal versjon: solo-spill mot regelbaserte AI-medspillere, lagring og gjenopptak, grafer og AI-oppsummering.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | risiko | Solo-spill med lagring, grafer og AI-oppsummering er realistisk. Flerspiller med mennesker og fulle lærerfunksjoner i tillegg er neppe det. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | OK | Gode suksesskriterier og tydelig avgrensning mot «Utenfor første versjon». Spillreglene må konkretiseres i PRD. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | En vanlig webapp med database og grafer er godt egnet. Sanntidsflerspiller (WebSocket) er mer krevende. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | risiko | Dere kan kontrollere beregningene hvis dere regner ut noen perioder for hånd eller i regneark først. Uten det blir det vanskelig å vite om simuleringen stemmer. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | OK | Spillmotoren er ideell for enhetstester: gitt bestillinger og etterspørsel, så skal lager, restordre og kostnad etter periode N være X. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | risiko | Ikke omtalt. Med regelbaserte medspillere trengs språkmodellen bare til oppsummeringen. Lag en reserve-oppsummering eller mock når nøkkel mangler. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | risiko | Hvis medspillerne bruker språkmodell, blir det mange kall per spill (tre roller × mange perioder). Det gir kostnad og ventetid. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Flytt flerspiller med mennesker til trinn 2 eller «Utenfor første versjon». V1 blir da solo mot AI, med lagring, gjenopptak, grafer og AI-oppsummering.
2. Forenkle lærerstøtten i v1 til en enkel oversikt over spill og resultater for studentene i en klasse. La medspillerne være regelbaserte, med mulighet for språkmodell senere.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | Klart hva appen er (nettbasert Beer Game med AI-medspillere) og hvilket læringsproblem den løser (å forstå bullwhip-effekten). |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | OK | Konkret om fire roller som må fylles samtidig, fravær og manuell sammenstilling. Det kunne gjerne vært koblet til egne erfaringer fra logistikkfag. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | OK | Beskriver spillbildet, grafene og oppsummeringen fra brukerens side, uten teknologidetaljer. |
| What Makes This Different – er vurderingen ærlig og realistisk? | Juster | Det finnes flere gratis digitale Beer Game-versjoner. Nevn dem, og forklar hva dere gjør annerledes. Vurderingen blir mer troverdig når alternativene er navngitt. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Juster | Tre målgrupper. Gjør studenten til primærbruker i v1 og beskriv én konkret brukssituasjon, for eksempel en student som øver alene før eksamen i logistikk. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | OK | Seks funksjonelle kriterier som kan testes. Presiser «beregnes korrekt» med et regneeksempel når reglene er fastsatt. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Juster | Det er tydelig hva som er ute, men «innenfor» er for stort. Flytt flerspiller med mennesker og mer avansert lærerstøtte ut av v1. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | OK | Flere simuleringer og integrasjon med læringsplattformer er tydelig plassert i fremtiden. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Juster | Briefen er et godt grunnlag. Siden temaet er det samme som i faglærers eksempel, må deres egen sporbare prosess fra brief til kode vises tydelig. Kom i gang med BMAD-strukturen og PRD. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Juster | Kjerneflyten er tydelig, og spillmotoren gir reell funksjonalitet. Reduser omfanget rundt flerspiller og lærer. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | OK | Godt utgangspunkt. Lag et regneark med fasit for 5–10 perioder som grunnlag for tester av spillmotoren. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Spillbilde og resultatgrafer er nevnt. Skisser de to–tre viktigste skjermbildene: bestilling per periode, oversikt over kjeden og resultat med oppsummering. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | OK | Teknologi er bevisst utsatt til arkitekturen. Hold spillmotoren som en egen, testbar modul. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Planlegg lokal kjøring med lokal database og fungerende spill uten nøkkel. Bare oppsummeringen bør trenge språkmodell. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Flytt briefen inn i en planleggingsmappe (for eksempel `_bmad-output/planning-artifacts/briefs/`), og hold API-nøkler i `.env` som ikke committes. |

## 3. Neste steg for gruppen

1. Oppdater Scope: v1 = solo mot regelbaserte AI-medspillere, lagring og gjenopptak, grafer, AI-oppsummering og enkel lærervisning. Flerspiller med mennesker flyttes til trinn 2.
2. Skriv ned spillreglene og standardparameterne, og regn ut et eksempelspill for hånd eller i regneark som fasit.
3. Velg studenten som primærbruker, navngi eksisterende digitale versjoner under «What Makes This Different», og gå videre til PRD.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
