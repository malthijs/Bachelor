[*toetsen stappenplan*]
1. Formuleer H₀ en Hₐ
2. Kies α
3. Bepaal steekproefgrootte n
4. Bereken kritieke gebied OF overschrijdingskans p
5. Bepaal uitkomst steekproef (H₀ behouden of verwerpen)
6. Formuleer conclusie

[*welke toets*]
Een "response variable" is een afhankelijke variabele dat onderzocht
of gemeten wordt. Het gaat altijd gepaard met één of meer
onafhankelijke "explanatory variable(s)" die het beïnvloeden.

CI = Confidence Interval

[*numerical response variable*]
Numerical explanatory variable(s)
- Correlation/regression

Categorical explanatory variable(s)
- 1 group
normal: CI for μ using t
not normal: transform then...

- 2 groups
independent
normal: CI for μ₁ - μ₂ using t
not normal: Wilcoxon-Mann-Whitney or transform then...

dependent
normal: CI for μₚ using paired t
not normal: Wilcoxon Signed-Rank test or Sign test or transform
then...

- 3 or more independent groups
normal:
common σ: ANOVA
uncommon σ: Kruskal-Wallis or transform then...

not normal: Kruskal-Wallis or transform then...

[*categorical response variable*]
Numerical explanatory variable(s)
- Logistic regression

Categorical explanatory variable(s)
- 1 group
yes/no:
n large: CI for p using Z
n small: Binomial

many categories: Chi-square goodness-of-fit

- 2 groups
2 levels each:
independent samples: Chi-square independence test for 2 x 2 or
                     Fisher's exact test
dependent samples: McNemar's test

Many levels each; independent samples: Chi-square independence test
for r x k

[*normale verdeling*]
- Gaussverdeling of klokkromme
- Continue verdeling: elke waarde is mogelijk
Als er nauwkeurig genoeg gemeten is
- Kans wordt bepaald door middel van oppervlakte

Is symmetrisch
Kans = 1 = 100 %

Dichtheidsfunctie
Afhankelijk van verwachtingswaarde μ en standaarddeviatie σ

Oppervlakte onder de grafiek van de dichtheidsfunctie geeft de
kans aan

Grote σ = brede curve
Kleine σ = hoge curve

Door μ te veranderen wordt de curve naar rechts of links verplaatst

Vallen samen:
- Mediaan
- Modus
- Verwachtingswaarde

Notatie: Y ~ N(μ , σ)
Betekenis: Data Y volgt een normaalverdeling met μ = ... en σ = ...

Kans = integraal van dichtheidsfunctie
Dat is lastig!

Omzetten van normaalverdeling naar standaard normaalverdeling
Bepaling z-score

Z ~ N(μ = 0, σ = 1)
Kans aflezen in tabel!

In R hoeft een normaalverdeling niet omgezet te worden naar een
standaard normaalverdeling

* voorbeeld *
pnorm(q = 90, mean = 83, sd = 6) = 0.878 = 87.8%

[*standaardisering*]
Z = (y - μ)/σ

Z aflezen in tabel = z-score
y = grenswaarde
μ = verwachtingswaarde
σ = standaarddeviatie

[*steekproefgemiddelden*]
De standaarddeviatie van steekproefwaarnemingen is
een factor √(n) kleiner dan de standaarddeviatie
van individuele waarnemingen:

σₓ = σ/√(n)     Wortel-n-wet

Gemiddelden van groepen hebben een kleinere maten
van spreiding dan individuele waarnemingen

[*voorspellingsintervallen*]
Data is normaal verdeeld indien:
- 68.26 % ligt binnen ± 1 SD
- 95.44 % ligt binnen ± 2 SD
- 99.74 % ligt binnen ± 3 SD

[*normal probability plots*]
Volgt data wel of niet een normaalverdeling?

X-as: verwachte waarden
Y-as: geobserveerde waarden

* voorbeeld *
lengte_vrouwen <- c(61, 62.5, 63, 64, 64.5, 65,
                    66.5, 67, 68, 68.5, 70.5)
qqnorm(lengte_vrouwen)

Rechte lijn?
Is een normaalverdeling
Anders niet

Waarom is dit belangrijk?
Voor veel testen (b.v. t-test en ANOVA) is het
een voorwaarde dat de data die geanalyseerd wordt
normaal verdeeld is.

Wat als data niet normaal verdeeld is?
- transformeren van de data (soms kan dat niet)
- andere statistische test gebruiken

Probleem!
Het is soms moeilijk om visueel m.b.v. normal probability plots te
bepalen of een verdeling normaal is of niet-normaal

[*Shapiro-Wilk test*]
Statistische toets die op basis van getallen aangeeft of data
normaal of niet-normaal verdeeld is

Stappenplan:
1. H₀: data is normaal verdeeld. Hₐ: data is niet-normaal verdeeld
2. kies α = 0.05
3. R: shapiro.test(x)
4. vergelijk p-waarde met α

* voorbeeld *
shapiro.test(lengte_vrouwen)

p-waarde = 0.9833
α = 0.05

p > α
Conclusie: data is normaal verdeeld
