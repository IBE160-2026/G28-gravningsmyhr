# Refleksjonsrapport - Programmering med KI

**Lesestatus:** KI-assistert utkast til studentens gjennomlesing. Rapporten følger den mottatte malen. Beskrivelser av utført arbeid bygger på samtalen, repoet og dokumenterte tester. Personlige erfaringer er avgrenset til det studenten faktisk har oppgitt. De analytiske vurderingene og anbefalingene er forslag som studenten må vurdere før innlevering. Rapporten er ikke levert i Canvas.

## 1. Gruppeinformasjon

**Gruppenavn:** G28-gravningsmyhr  
**Gruppemedlem:** Andreas Iden-Gravningsmyhr – andreas.iden-gravningsmyhr@himolde.no  
**Dato:** 03.11.2026  
**Prosjekt:** Beer Game  
**Nettside:** https://g28-gravningsmyhr.vercel.app/  
**GitHub:** https://github.com/IBE160-2026/G28-gravningsmyhr

## 2. Utviklingsprosessen

### 2.1 Oversikt over prosjektet

Prosjektet er en nettbasert læringssimulering av en forsyningskjede med fire roller: detaljist, grossist, distributør og fabrikk. Brukeren velger én rolle og bestiller varer gjennom tjue perioder. De øvrige rollene styres av faste bestillingsregler. Lager, restordre, transport og kostnader oppdateres ved hver bekreftet periode. Etter avslutning vises grafer, historikk og en oppsummering. En enkel lærerfunksjon knytter spill til klasser og gir læreren innsyn i gjennomføring og resultater.

Hovedmålet er at en student skal kunne utforske forsyningskjeder alene og undersøke hvordan bestillinger og forsinkelser påvirker resultatene. Spillet kan brukes til å diskutere bullwhip-effekten. Vi har ikke målt læringsutbytte eller vist at appen gir bedre forståelse enn andre undervisningsformer. Målet i produktbeskrivelsen om forbedret forståelse er derfor fortsatt et evalueringsmål, ikke et oppnådd resultat.

### 2.2 Arbeidsmetodikk

Det er ett dokumentert gruppemedlem. Det var derfor ingen fordeling mellom flere studenter. Arbeidsdelingen gikk mellom meg som bestiller og beslutningstaker og KI-agenten som utførte mye av det tekniske arbeidet. Jeg ba om hjelp, ga tilgang til dokumenter og skjermbilder, fulgte opp spørsmål og gjennomførte kontooppsett og publiseringssteg etter veiledning. KI-agenten skrev planleggingsdokumenter, kode, tester og dokumentasjonsutkast og utførte nettleserkontroller.

GitHub ble brukt til versjonering og deling av prosjektet. Den første samlede endringen lå i en egen gren og ble presentert som en pull request. Jeg fulgte veiledningen og bekreftet fletting til main. Senere rettelser ble lagt direkte i main og utløste publisering gjennom Vercel. Historikken er konsentrert til en intensiv arbeidsøkt. Den bør ikke framstilles som jevn utvikling over hele semesteret. Teams er omtalt i emnet, men er ikke dokumentert som samarbeidsverktøy for denne gjennomføringen.

### 2.3 Teknologi og verktøy

Frontend er HTML, CSS og JavaScript uten egen byggeprosess. Backend er Python med standardbibliotekets HTTP-server. Lokal lagring bruker SQLite. Den publiserte løsningen bruker PostgreSQL i Supabase gjennom psycopg. Vercel kjører serverkoden og henter endringer fra GitHub. Automatiske tester bruker Python unittest, og GitHub Actions kjører testene i et separat miljø.

KI-arbeidet ble utført i Codex gjennom denne samtalen, med filverktøy, GitHub-tilkobling og nettleserverktøy. Det er ikke dokumentert at prosjektet ble implementert i Claude Code. En valgfri Claude-integrasjon finnes i appkoden, men er ikke aktivert. Planleggingsrekkefølgen følger deler av BMAD-tankegangen med brief, PRD, arkitektur og oppgaver. Det er ikke kjørt en full installert BMAD-arbeidsflyt, og dokumentasjonen skal ikke gi inntrykk av det.

### 2.4 Utviklingsfaser

**Fase 1: Planlegging**

Utgangspunktet var en produktbeskrivelse og faglærers tilbakemelding. Læreren anbefalte mindre omfang, studenten som primærbruker, tydelige spillregler og regelbaserte medspillere. KI-agenten undersøkte repoet og utarbeidet en PRD med funksjonskrav, kvalitetskrav og testbare akseptansekriterier. Deretter kom tekstlige skjermskisser, arkitekturforslag og tretten utviklingsoppgaver. Flerspiller med mennesker ble utsatt. Lærerfunksjonene ble redusert til klasse og resultatoversikt.

PRD-en fastsatte et forslag til tjue perioder, startlager tolv, etterspørsel fire og deretter åtte, ordreledetid én periode og transport og produksjon to perioder. Dette er prosjektets undervisningsvariant. Reglene er ikke kontrollert mot en særskilt fasit fra emnet. Den første beskrivelsen av periodegrensen var uklar. Den ble presisert slik at studenten ser et klargjort beslutningspunkt, mens endringene først lagres når bestillingen bekreftes.

**Fase 2: Utvikling**

KI-agenten laget først spillmotor og lagring, deretter innlogging, tilgangskontroll, grensesnitt og resultater. Kontoer ble sikret med passordhashing og tidsbegrensede sesjoner. Bestillinger ble validert, og kommando-ID og versjonskontroll skulle hindre at en gjentatt forespørsel registrerer en periode to ganger. Oppsummeringen ble laget slik at appen fungerer uten språkmodellnøkkel.

Det foreløpige Next.js-forslaget ble erstattet av Python og JavaScript for enklere lokal kjøring. KI-agenten testet beregninger og brukerflyt, mens jeg opprettet Supabase-prosjekt og Vercel-prosjekt etter skjermbildebasert veiledning. Første publisering viste en tjenestefeil. Etter en endring i avhengighetsdeklarasjonen fungerte databasen. Sluttkontrollen utvidet testene til nitten og omfattet fire fulle spill på nett, lokal lærerflyt, breddeprøver og tastatur.

Sentrale brukerprompter var «sett i gang», «kan du gjøre alt dette for meg» og «fortsett - gjør alt ferdig». Disse korte bestillingene fungerte fordi samtalen allerede inneholdt prosjektinformasjon. Vedlegget om prosess og prompter beskriver alle dokumenterte hovedsteg i den tilgjengelige historikken. Det er et rekonstruert register over faktiske steg, ikke en full eksport av alle tidligere økter eller KI-verktøyenes interne instruksjoner. Manglende promptgrunnlag er uttrykkelig markert.

Sluttkontrollen undersøkte også om dokumentasjonen fortsatt beskrev den faktiske appen. Det opprinnelige forslaget inneholdt funksjoner og teknologi som senere ble endret. Derfor ble README, PRD og produktbeskrivelse supplert med leveransevalg. En fungerende app og en korrekt rapport er to ulike leveranser: testing av koden fanger ikke automatisk opp misvisende formuleringer i dokumentene. Den mottatte rapportmalen utløste derfor denne egne revisjonen av teksten og strukturen.

## 3. Utfordringer og løsninger

### 3.1 Tekniske utfordringer

**Utfordring 1: Publisert side uten fungerende database**

Problem: Vercel rapporterte vellykket publisering, men appen viste en tjenestefeil før innlogging. Dette avdekket forskjellen mellom et vellykket bygg og en fungerende løsning.

Løsning: Databasepakken ble lagt eksplisitt til i pyproject.toml, og feilhåndteringen fikk ufarlige feilkategorier. Etter ny publisering fungerte registrering, lagring og gjenopptak. Den opprinnelige serverfeilen ble ikke bekreftet fra rå serverlogger. Det er derfor mest presist å si at endringen ble fulgt av en fungerende tilkobling.

KI sin rolle: Agenten undersøkte kode og publisert side, foreslo rettingen og kontrollerte resultatet. Det var også agenten som hadde laget det første oppsettet. Hendelsen viser hvorfor eget KI-generert arbeid trenger kontroll etter publisering.

**Utfordring 2: Korrekte periodeoverganger og gjentatte forespørsler**

Problem: Varer, etterspørsel og bestillinger oppstår på forskjellige tidspunkt. Feil rekkefølge kan forskyve leveranser. Dobbeltklikk eller to faner kan dessuten forsøke å oppdatere samme spill.

Løsning: Spillmotoren ble isolert fra visning og database. Testene kontrollerer ordre, transport og produksjon hver for seg. Transaksjoner og forventet versjon sikrer samlet lagring. En egen HTTP-test sendte to konkurrerende bestillinger; bare én ble akseptert. Et separat regneoppsett krysskontrollerte åtte perioder for fire roller.

KI sin rolle: Agenten foreslo strukturen og skrev begge beregningene og testene. Siden samme type verktøy bidro til begge, er krysskontrollen nyttig, men ikke like sterk som en uavhengig fagpersons vurdering.

**Utfordring 3: Begrenset nettlesertilgang**

Problem: Verktøyet kunne ikke alltid bekrefte nettadressen i Brave og stoppet styringen. Dette hindret direkte gjennomføring av flere konto- og publiseringssteg.

Løsning: Jeg delte skjermbilder og utførte klikkene etter veiledning. Senere ble appen testet gjennom en annen tilgjengelig nettleserflate. Arbeidet fortsatte uten å omgå verktøyets sikkerhetsstopp.

KI sin rolle: Agenten tolket skjermbildene og ga konkrete instruksjoner. Begrensningen viste at tilgangen til verktøy kan være like avgjørende som modellens evne til å foreslå en løsning.

### 3.2 Samarbeidsutfordringer

Jeg har ikke oppgitt samarbeidsproblemer og har ikke opplevd arbeidet som vanskelig. Det finnes heller ingen dokumenterte konflikter mellom gruppemedlemmer. Rapporten skal derfor ikke finne på slike utfordringer for å fylle malen.

Samarbeidet med KI krevde likevel tydelige statusavklaringer. Underveis ble «laget», «testet», «publisert» og «klart til innlevering» brukt om ulike tilstander. En app kunne være publisert uten fungerende database, og en rapport kunne være skrevet uten at den faktiske malen var lest. Leveransestatusen ble derfor samlet i et eget dokument som skiller ferdige kontroller, avgrensninger og åpne punkter.

### 3.3 KI-spesifikke utfordringer

KI kunne fylle hull med rimelige, men ikke bekreftede antakelser. Eksempler er foreslåtte spillparametre og antakelsen om at innleveringen ville finnes under Vurderinger i Canvas. Da skjermbildet viste en karakteroversikt uten oppgaver, måtte veiledningen korrigeres. Slike forslag må skilles fra faktiske emnekrav.

Det oppstod også avvik mellom plan og implementering. Teknologistakken ble endret, og ekte KI-oppsummering ble utsatt etter mitt valg om gratis løsning. Dokumentasjonen ble oppdatert for å vise disse avvikene. En rapport som bare gjentok den første planen, ville ha beskrevet funksjoner som ikke var levert.

## 4. Kritisk vurdering av KI sin påvirkning

### 4.1 Fordeler med KI-assistanse

**Effektivitet og produktivitet:** KI håndterte mange sammenhengende oppgaver: krav, programkode, tester, dokumentasjon og feilsøking. Publiseringsveiledningen brøt opp komplekse oppsett i konkrete handlinger. Det finnes ingen måling av spart tid eller kontrollgruppe uten KI, så en prosentvis effektivitetsgevinst ville vært udokumentert. Den synlige fordelen er bredden i arbeidet som faktisk ble utført.

**Læring og forståelse:** Min uttalte erfaring er at KI kan gjøre svært mye når modellene er avanserte nok. Prosessen ga samtidig konkrete eksempler på GitHub-fletting, miljøvariabler og forskjellen mellom publisering og fungerende drift. Dette er eksponering for arbeidsmåter; det dokumenterer ikke at jeg selvstendig kan forklare eller gjennomføre alle delene uten hjelp.

**Kvalitet på koden:** Agenten delte spillmotoren fra brukergrensesnittet og la til relevante tester. Under sluttkontrollen ble databaseforbindelsen sikret mot å bli stående åpen ved initialiseringsfeil. Graflegenden fikk samme linjemønstre som grafene. Dette er konkrete forbedringer, men kvaliteten bygger på etterprøvbare resultater, ikke på at koden er skrevet av en avansert modell.

### 4.2 Begrensninger og ulemper

**Kvalitet og pålitelighet:** Den første publiseringen fungerte ikke, og enkelte beskrivelser måtte revideres. Testene dekker sentrale tilfeller, men det er ikke gjort en full tilgjengelighetsrevisjon, omfattende lasttest eller uavhengig sikkerhetsgjennomgang. At nitten tester består betyr at disse testtilfellene virker, ikke at alle mulige feil er utelukket.

**Avhengighet og forståelse:** KI gjorde mye av den tekniske vurderingen. Det gir en risiko for at jeg godtar resultatet uten tilstrekkelig egen forståelse. Dokumentasjonen viser foreløpig mest agentutført testing og mine valg og oppsettshandlinger. For å redusere avhengigheten bør jeg selv prøve kjernen, følge én periodeberegning og kunne forklare hvordan et spill lagres. Slike egne kontroller må dokumenteres når de er gjort.

**Kreativitet og problemløsning:** KI foreslo mye av løsningsrommet og kan dermed ha styrt prosjektet mot vanlige mønstre. Det er ikke dokumentert at jeg opplevde redusert kreativitet. En relevant risiko er likevel at ferdige forslag gjør det mindre naturlig å undersøke alternative løsninger. Å be om alternativer og sammenligne dem mot krav kan motvirke dette uten å øke omfanget unødvendig.

Et annet pålitelighetsspørsmål gjelder hva testene faktisk sammenligner. I de fire offentlige spillene bestilte studenten fire enheter i hver periode. Sluttkostnadene for hele kjeden var 754, 3820, 10232 og 17600, avhengig av rollen. Verdiene samsvarte med lokale beregninger. Dette viser reproduksjon av bestemte forløp, ikke at strategien er god. Et høyt kostnadsresultat kan være et gyldig utfall av reglene og bør ikke automatisk tolkes som en programfeil. Samtidig kan samsvar mellom to kjøringer ikke alene bekrefte at selve reglene er faglig riktige.

### 4.3 Sammenligning: Med og uten KI

Uten KI måtte kode, tester og dokumentasjon vært skrevet gjennom andre arbeidsformer. Det ville trolig krevd mer direkte programmeringsarbeid og oppslag, men det finnes ikke grunnlag for å tallfeste tidsforskjellen. Jeg kan heller ikke dokumentere at sluttresultatet ville blitt bedre eller dårligere.

Manuelt arbeid kunne gitt mer trening i syntaks og feilsøking fordi hvert problem måtte bearbeides direkte. Samtidig kunne et mindre omfang blitt nødvendig. Med KI ble en større del av arbeidet flyttet til bestilling, oppfølging og vurdering. Sammenligningen handler derfor både om arbeidsmengde og om hvilke ferdigheter som faktisk trenes.

### 4.4 Samlet vurdering

KI har vært en positiv faktor for gjennomføringen av dette prosjektet: den publiserte appen, testene og dokumentasjonen viser konkrete leveranser. Den viktigste reservasjonen er at gjennomføringsevne og selvstendig kompetanse ikke er det samme. Et resultat kan være nyttig selv om studenten fortsatt trenger å utvikle forståelsen av hvordan det virker.

Min erfaring om betydningen av avanserte modeller er et viktig utgangspunkt. Prosjektet gir også grunn til å vektlegge kontekst, gode krav, tilgjengelige verktøy og kontroll. Modellen trengte både lærerens tilbakemelding og informasjon fra repo og skjermbilder. Modellstyrke alene var ikke nok til å sikre en riktig førstegangsleveranse.

## 5. Etiske implikasjoner

### 5.1 Ansvar og eierskap

Ansvar for å vurdere og levere prosjektet ligger fortsatt hos studenten. At en agent skriver koden, gjør ikke testresultater eller sikkerhetsvalg selvforklarende. En sentral kvalitetsoppgave er å koble krav til kontroller og være åpen om hvilke kontroller som mangler.

Opphavsrett og intellektuell eiendom er ikke juridisk avklart gjennom dette prosjektet. KI-generering bør ikke forstås som garanti for at alt innhold er originalt eller fritt for tredjepartsrettigheter. Eksempelprosjektet fra læreren ble ikke kopiert inn som eget arbeid. Avhengigheters lisenser og eventuelle gjenbrukte ressurser må vurderes før videre distribusjon eller kommersiell bruk. Dette er et åpent kontrollpunkt, ikke en rettslig konklusjon.

### 5.2 Transparens

Det bør framgå at KI har skrevet betydelige deler av både appen og rapportutkastet. Repoet inneholder planlegging, beslutninger, tester og logger. Denne rapporten skiller mellom mine oppsettshandlinger, mine uttalte erfaringer og agentens arbeid. Slik kan en leser vurdere hva dokumentasjonen faktisk viser.

Manglende åpenhet ville gitt et misvisende bilde av selvstendig programmering og kvalitetssikring. Det gjelder også å framstille automatiske tester som egne manuelle prøver eller å beskrive en lang, jevn utviklingsprosess som ikke er dokumentert. Presise avgrensninger gjør vurderingsgrunnlaget mer troverdig, også når de viser svakheter ved prosessen.

### 5.3 Påvirkning på læring og kompetanse

KI kan gjøre det enklere å komme fra idé til fungerende produkt, men også gjøre det mulig å hoppe over forståelsesarbeid. Dersom studenten bare ber agenten fortsette, kan ferdigheter i feilsøking, datamodellering og kildevurdering bli mindre øvd. Dette er en risiko, ikke et målt resultat om min kompetanse.

En bedre balanse er å bruke KI som utfører og forklarer, samtidig som studenten gjennomfører utvalgte kontroller selv. I dette prosjektet kan det være å regne ut lager og restordre i én periode, prøve ugyldig input og forklare hvorfor to samtidige bestillinger ikke skal gi to nye perioder. Slike oppgaver er små nok til å være realistiske og konkrete nok til å avdekke misforståelser.

### 5.4 Arbeidsmarkedet

En mulig utvikling er at flere oppgaver i IT blir organisert rundt spesifikasjon, gjennomgang og integrasjon av KI-genererte bidrag. Prosjektet viser et eksempel på at én agent kan utføre flere typer teknisk arbeid. Det gir ikke grunnlag for sikre prognoser om antall jobber eller hvilke yrker som forsvinner.

En rimelig vurdering er at evnen til å formulere problemer og kontrollere resultater blir viktig når produksjon av kode blir lettere. Domeneforståelse, sikkerhet, kommunikasjon og ansvarlig drift kan ikke vurderes bare ut fra hvor raskt kode produseres. Rapporten dokumenterer ingen bestemt personlig karriereplan; disse punktene er forslag til refleksjon om framtidige kompetansebehov.

### 5.5 Datasikkerhet og personvern

Jeg delte emneinformasjon, prosjektfiler, offentlige repoopplysninger og skjermbilder med KI. Databasens tilkoblingsinformasjon med passord ble også delt i samtalen. Det var unødvendig for vanlig veiledning. Passordet gjengis ikke i rapporten eller promptvedlegget. Rotasjon og privat oppdatering i Vercel er fortsatt ikke bekreftet.

Hendelsen viser at sikkerhet gjelder mer enn hva som committes. Hemmeligheter bør ikke deles i chat eller skjermbilder når veiledning kan gis uten dem. Appens kontoer og lærerinnsyn gir også behov for dataminimering og tilgangskontroll. Testene brukte fiktive identiteter. Før bruk med reelle studenter må oppbevaring, sletting og kontoforvaltning avklares, særlig fordi selvbetjent sletting og passordgjenoppretting mangler.

## 6. Teknologiske implikasjoner

### 6.1 Kodekvalitet og vedlikehold

KI-generert kode kan være ryddig, men trenger en struktur som andre kan forstå. Her ligger spillreglene i en separat modul, mens tilgang, lagring og presentasjon håndteres andre steder. Det gjør det lettere å teste beregningene uten nettverk og å finne hvilke deler som påvirkes av en endring.

En bevisst begrensning er at databasen lagrer én samlet tilstand. Det gjør transaksjoner enkle, men kan gi kø når flere brukere arbeider samtidig. Et valgfritt modellkall holder også låsen mens det venter på svar. Ved større bruk bør lagringen normaliseres og langsomme oppgaver skilles ut. Vedlikehold krever derfor forståelse av avveiningene, ikke bare en modell som kan skrive nye funksjoner.

Kontoenes livsløp er et annet vedlikeholdsbehov. Appen har registrering og innlogging, men mangler e-postverifisering, passordgjenoppretting og selvbetjent sletting. Disse manglene stanser ikke nødvendigvis en demonstrasjon med fiktive kontoer, men får betydning dersom appen tas i bruk i undervisning med reelle personer. Videreutviklingen bør derfor ikke bare handle om flere spillfunksjoner. Den må også omfatte hvordan brukere får hjelp, hvordan data fjernes, og hvordan endringer kan testes uten å forstyrre eksisterende spill.

### 6.2 Standarder og beste praksis

KI fulgte ikke automatisk alle ønskede arbeidsprinsipper. Det første arkitekturforslaget ble ikke den implementerte løsningen, og publiseringsoppsettet måtte korrigeres. Prosessen startet heller ikke med en komplett, installert BMAD-flyt eller en uavhengig kontroll av alle spillreglene. Dokumentene er derfor oppdatert med hva som faktisk ble gjort.

Samtidig er flere nyttige praksiser tatt i bruk: versjonering, tester, miljøvariabler, inputvalidering og tilgangskontroll på serveren. De må vurderes i sammenheng. En test som bare bekrefter samme antakelse som implementasjonen kan gi falsk trygghet. Det separate regneoppsettet og prøvene mot den publiserte appen utvider kontrollen, men erstatter ikke faglig vurdering eller full gjennomgang av sikkerhet.

### 6.3 Fremtidig utvikling

Videre arbeid bør prioritere forståelse og robusthet før flere funksjoner. Aktuelle forbedringer er tydeligere kontoforvaltning, en mer skalerbar datamodell og bekreftelse av spillreglene mot undervisningen. Ekte KI-refleksjon kan vurderes senere, men bør da ha en konkret nytte som veier opp for kostnad, usikker tekst og ekstern databehandling.

For KI-assistert utvikling generelt anbefales korte arbeidssteg med synlige ferdigkriterier. Agenten bør vise hva som er endret og hvordan det er kontrollert. Studenten bør kunne utfordre antakelser og be om en forklaring på konsekvensene av valgene. Et slikt samarbeid bruker modellens kapasitet uten å gjøre selvsikre formuleringer til erstatning for belegg.

## 7. Konklusjon og læring

### 7.1 Viktigste lærdommer

1. Avanserte KI-modeller kan utføre svært mye av et utviklingsprosjekt. Dette er min tydeligste uttalte erfaring fra arbeidet.
2. Publisering er ikke det samme som fungerende drift. Database og faktisk brukerflyt måtte kontrolleres etter at Vercel viste vellykket deploy.
3. Modell, kontekst, prompt og verktøy virker sammen. Lærerens tilbakemelding og skjermbilder var nødvendig informasjon for videre arbeid.
4. Kvalitetskontroll må være konkret: faste forventningsverdier, tilgangsforsøk og komplette spill sier mer enn en generell påstand om at løsningen virker.
5. KI-bruk må dokumenteres ærlig, med tydelig skille mellom agentens arbeid og studentens egne erfaringer og kontroller.

Punkt to til fem er analytiske læringspunkter utledet av prosjektforløpet og må gjennomgås av studenten. De er ikke dokumentasjon på at jeg allerede behersker alle områdene selvstendig.

### 7.2 Hva ville dere gjort annerledes?

En anbefalt forbedring ved en ny start er å lese rapportmalen og avklare innleveringskrav før implementeringen. I dette arbeidet kom den faktiske refleksjonsmalen sent, og første rapportutkast var derfor for kort og manglet flere emner. En annen forbedring er å kontrollere spillreglene og en liten beregningsfasit før motoren bygges.

Det ville også vært nyttig med flere eksplisitte gjennomganger der studenten forklarer og prøver det som er laget. Teknologistakken bør bestemmes gjennom en liten oppstartsvalidering og dokumenteres før større implementering. Prompter og faktiske beslutninger bør lagres underveis, slik at prosessbeskrivelsen i mindre grad må rekonstrueres fra samtale og commits etterpå.

### 7.3 Anbefalinger

Til andre studenter er anbefalingen å gi KI et tydelig problem, realistisk omfang og konkrete kriterier for hva som skal virke. Be om at usikre antakelser markeres, og kontroller dem mot emnets egne kilder. Bruk versjonering til å gjøre endringer gjennomgåbare, og unngå å samle hele prosessen i en udokumentert opplasting.

Test både vanlig bruk og feiltilfeller. Bruk fiktive data og hold nøkler utenfor samtaler og repo. Avslutt ikke ved en grønn publiseringsmelding: prøv innlogging, lagring, gjenopptak og resultater. Les til slutt dokumentasjonen og kontroller at den beskriver den leverte løsningen, også funksjoner som er utsatt eller endret.

En praktisk anbefaling er å beholde en kort oversikt over hva som faktisk er kontrollert ved hver leveranse. Dersom en test ikke er kjørt, bør den stå åpen framfor å beskrives som sannsynligvis i orden. Det samme gjelder dokumenter som ennå ikke er lest. Oversikten gjør det lettere å velge neste handling og hindrer at samtalens framdrift i seg selv blir tatt som bevis for at prosjektet er ferdig.

### 7.4 Personlig refleksjon individuelt

**Andreas Iden-Gravningsmyhr:** Jeg har ikke opplevd noe som vanskelig i dette arbeidet. Det jeg selv har uttrykt at jeg har lært, er at KI kan gjøre det aller meste når man har avanserte nok modeller. Prosjektet har vist meg en arbeidsform der jeg kan beskrive hva jeg ønsker, følge veiledning og få utført omfattende teknisk arbeid.

Samtidig har jeg ikke oppgitt en selvstendig gjennomgang av kildekoden eller egne komplette spilltester. Rapporten skal derfor ikke gi inntrykk av at dette allerede er gjort. Før innlevering må jeg lese rapporten, prøve appen selv og ta stilling til de analytiske vurderingene. Det er en nødvendig forskjell mellom å ha fått en løsning laget og å kunne stå inne for beskrivelsen av den.

## 8. Vedlegg valgfritt

- [Arbeidssteg og sentrale prompter](https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/docs/prosess-og-prompter.md).
- [Kildekode og README](https://github.com/IBE160-2026/G28-gravningsmyhr).
- [Testresultater](https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/docs/testing.md) og [separat regnegrunnlag](https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/docs/reference-extended.md).
- [PRD](https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/docs/planning/prd.md), [arkitekturbeslutninger](https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/docs/implementation.md) og [leveransestatus](https://github.com/IBE160-2026/G28-gravningsmyhr/blob/main/docs/leveransestatus.md).
- Rapportmalen reflection-report-template (1).md, levert av studenten 3. november 2026.

Malen oppgir forventet lengde 3000–5000 ord. Den oppgir ikke innleveringssted eller frist. Oppgaven er ikke innlevert, og det foreligger ingen faglærergodkjenning av rapporten eller den avgrensede løsningen.

**Ordantall:** Omtrent 3296 ord i del 2–7, inkludert underoverskrifter. Gruppeinformasjon og vedlegg er ikke medregnet.
