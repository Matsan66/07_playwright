## 📊 Status Veckouppgift 7 Playwright


Här nedan presenteras en översikt över statusen på lösande av uppgfterna.

| Uppgift                      | Status |
|:-----------------------------|:------:|
| 1. Diskutera i grupp         |   🟢   |
| 2. Öva på regex              |   🟡   |
| 3. Öva på user stories       |   🔴   |
| 4. Öva på E2E test           |   🔴   |


## 1️⃣ Diskutera i grupp

1a Vilka strängar matchas av det reguljära uttrycket: "ab"?  
Svar: C. sabotör

1b  Betrakta uttrycket "nisse". Vad skriver jag för att matcha både "Nisse", "NISSE" och "nisse"?  
Svar: /nisse/gmi

1c Vilka strängar matchas av "a*n"?  
Svar: Endast "an" om inte /g läggs till för att hitta alla träffar.

1d Vilka strängar matchas av "[ae]n" ?  
Svar: "inconsequential"

1e Vilka strängar matchas av "je.+e"?
Svar: "jeppe" och "je je"


1f Vilka strängar matchas av "\san?\s"  
Svar: "    an   na   an   " och "be a darling"

1g Skriv ner med egna ord, vad följande uttryck matchar. "Strängar som innehåller…"    
A. line och lines  
B. Strängar som börjar med ett eller flera "a" och slutar med "ö"  
C. En eller flera vokaler  
D. Måste börja med 1 - 9 därefter valfritt antal siffror i spannet 0 - 9  
E. Fyra siffror - Två siffror - Två siffror (typ: 1970-12-10)  


2a Betrakta https://lejonmanen.github.io/agile-helper/ . Skriv en user story som beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".

````
som användare av agile-helper  
vill jag kunna läsa om hur man gör en "sprint retroactive"  
så att jag kan avsluta en sprint på rätt sätt
````

2b Skriv ner ett testscenario för user storyn. Använd en punktlista. Fundera särskilt på vad som ska testas implicit (I) och explicit (E).
```
1. Öppna hemsidan (I)
2. Klicka på knappen med texten "sista" (I)
3. Klicka på knappen som innehåller texten "Sprint retroactive" (I)
4. Kontrollera att rubriken "Sprint retroactive" är synlig (E)
```

3 Titta på kodexemplet från lektionen. Skriv upp allt du är osäker på och diskutera i grupp, eller fråga om på nästa lektion.  

#### Inga frågor


## 2️⃣ Diskutera i grupp

1a Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter: "Fiskarna som jag fångade var 55 cm långa."  
```
\d+,?\d+\s(?i)cm
```
1b Denna gången vill vi veta om det finns två längder.  
```
\d+,?\d+\s+cm.*?\d+,?\d+\s+cm
```
1c Längderna ska vara samma enhet. "Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."  
```
(\d+(?:,\d+)?)\s*(cm|m)
```
2 Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"  
```
^[1-9]\d{2}\s\d{2}$  
```
3 Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.  
```
^\d{4}-\d{2}-\d{2}$
```
4 Skriv ett regex som matchar ett pengavärde i siffror.  
```
\d+\skr
```
5a Skriv ett regex som matchar en e-postadress (användarnamn@server.domän).  
```
[a-öA-Ö0-9.-]+.?[a-öA-Ö]*?@[a-öA-Ö0-9.-]+[a-öA-Ö0-9]+
```
5b Gör ett regex som matchar en komplett e-postadress enligt specifikationen i artikeln.  
```
^[a-z0-9]+(?:[._-][a-z0-9]+)*@[a-z0-9]+(?:-[a-z0-9]+)*\.[a-z]{2,}$
```

## 3️⃣ Öva på user stories

## 4️⃣ Öva på E2E test