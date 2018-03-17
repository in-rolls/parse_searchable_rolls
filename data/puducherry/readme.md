## Puducherry

Basic descriptive statistics about the data. And sanity checks.


```r
puducherry <- readr::read_csv("puducherry.csv")
```

```
## Parsed with column specification:
## cols(
##   .default = col_character(),
##   number = col_integer(),
##   age = col_integer(),
##   part_no = col_integer(),
##   year = col_integer(),
##   pin_code = col_integer(),
##   net_electors_male = col_integer(),
##   net_electors_female = col_integer(),
##   net_electors_third_gender = col_integer(),
##   net_electors_total = col_integer()
## )
```

```
## See spec(...) for full column specifications.
```

Number of rows:


```r
nrow(puducherry)
```

```
## [1] 1870704
```

Unique Values in Sex:


```r
# Unique values in sex
table(puducherry$sex)
```

```
## 
##       Female         Male Third Gender 
##       984250       886286          168
```

Summary of Age:


```r
# Age
summary(puducherry$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   19.00   31.00   41.00   42.74   53.00  109.00
```

Check if 0 and missing age is from problem in the electoral roll:


```r
puducherry[which(puducherry$age == 1), c("id", "filename")]
```

```
## # A tibble: 0 x 2
## # ... with 2 variables: id <chr>, filename <chr>
```

No. of characters in ID:

```r
# Length of ID
table(nchar(puducherry$id))
```

```
## 
##       9      10      12      16      17      18 
##      10 1230646      38  620360   19648       2
```

Number of characters in pin code:


```r
table(nchar(puducherry$pin_code))
```

```
## 
##       6 
## 1870704
```

Are IDs duplicated?


```r
length(unique(puducherry$id))
```

```
## [1] 935351
```

```r
nrow(puducherry)
```

```
## [1] 1870704
```


```r
# Net electors
sum(with(puducherry, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 1769868
```

```r
nrow(puducherry)
```

```
## [1] 1870704
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(puducherry$elector_name))
```

```
## 
##      3      4      5      6      7      8      9     10     11     12 
##   3280  51848  94412 161068 222164 181862 234300 213046 203206 154998 
##     13     14     15     16     17     18     19     20     21     22 
## 107302  57248  40076  28670  22208  18198  15766  13270  11464   8852 
##     23     24     25     26     27     28     29     30     31     32 
##   6930   5190   3884   2956   2238   1556   1282   1030    598    480 
##     33     34     35     36     37     38     39     40     41     42 
##    340    304    210    184    102     64     56     30     12     12 
##     43     44 
##      6      2
```

```r
puducherry[which(nchar(puducherry$elector_name) < 4), c("id", "filename")]
```

```
## # A tibble: 3,280 x 2
##    id               filename     
##    <chr>            <chr>        
##  1 KXX0226290       eng_22_20.pdf
##  2 AJJ0079186       eng_22_20.pdf
##  3 KXX0218743       eng_22_20.pdf
##  4 TNV0103093       eng_27_27.pdf
##  5 TNV0006254       eng_27_27.pdf
##  6 URI0067637       eng_25_28.pdf
##  7 KCR0193672       eng_28_31.pdf
##  8 NPX0082446       eng_28_31.pdf
##  9 PY/01/015/063676 eng_01_32.pdf
## 10 DGL0189365       eng_01_32.pdf
## # ... with 3,270 more rows
```

Does district have a number?

```r
sum(grepl('[0-9]', puducherry$district))
```

```
## [1] 0
```

Basic admin. units:

```r
table(puducherry$parl_constituency)
```

```
## 
## 01. PUDUCHERRY (GEN) 
##              1870704
```

```r
table(puducherry$ac_name)
```

```
## 
##           1 . MANNADIPET (GEN)       10 . KAMARAJ NAGAR (GEN) 
##                          59080                          67008 
##             11 . LAWSPET (GEN)             12 . KALAPET (GEN) 
##                          60718                          63684 
##          13 . MUTHIALPET (GEN)          14 . RAJ BHAVAN (GEN) 
##                          57692                          51264 
##             15 . OUPALAM (GEN)          16 . ORLEAMPETH (GEN) 
##                          53528                          47728 
##          17 . NELLITHOPE (GEN)         18 . MUDALIARPET (GEN) 
##                          64590                          66552 
##         19 . ARIANKUPPAM (GEN)         2 . THIRUBHUVANAI (SC) 
##                          73076                          60830 
##            20 . MANAVELY (GEN)              21 . EMBALAM (SC) 
##                          63520                          63486 
##          22 . NETTAPAKKAM (SC)              23 . BAHOUR (GEN) 
##                          61696                          55994 
##            24 . NEDUNGADU (SC)         25 . THIRUNALLAR (GEN) 
##                          50956                          58178 
##      26 . KARAIKAL NORTH (GEN)      27 . KARAIKAL SOUTH (GEN) 
##                          66780                          63204 
## 28 . NERAVY-T.R.PATTINAM (GEN)                29 . MAHE (GEN) 
##                          59144                          61018 
##               3 . OUSSUDU (SC)               30 . YANAM (GEN) 
##                          57152                          71576 
##             4 . MANGALAM (GEN)            5 . VILLIANUR (GEN) 
##                          70904                          75472 
##            6 . OZHUKARAI (GEN)           7 . KADIRGAMAM (GEN) 
##                          76104                          64404 
##         8 . INDIRA NAGAR (GEN)       9 . THATTANCHAVADY (GEN) 
##                          66954                          58412
```

```r
table(puducherry$police_station)
```

```
## 
##   Ambagarathur O.P.         Ariankuppam              Bahour 
##               14610               72036               50590 
##            Cotchery     Danvantri Nagar Dariyalathippa O.P. 
##               38378              121776               13948 
##        Grand Bazaar             Kalapet            Karaikal 
##               73238               31716              112720 
##  Karayamputhur O.P.       Katterikuppam       Kirumampakkam 
##               13024               18264               41118 
##        Korkadu O.P.             Lawspet     Madukkarai O.P. 
##               26552              118278               18726 
##                Mahe       Mangalam O.P.        Mettupalayam 
##               21048               35862               67782 
##         Mudaliarpet          Muthialpet           Neduncadu 
##              115156               51204               21352 
##              Neravy         Nettapakkam          Odiansalai 
##               33850               31166               41626 
##           Orleanpet             Palloor      Pandakkal O.P. 
##               94778               30778                9192 
##      Reddiarpalayam      Sedarapet O.P.    Solai Nagar O.P. 
##               93652                9756               35474 
##       Thavalakuppam        Thirubuvanai         Thirukkanur 
##               41898               55230               46416 
##         Thirunallar       Thirupattinam           Villenour 
##               43568               33784              134530 
##               Yanam 
##               57628
```

```r
table(puducherry$mandal)
```

```
## 
##      Bahour    Karaikal        Mahe    Oulgaret  Puducherry Thirunallar 
##      181176      189128       61018      457284      488686      109134 
##   Villianur       Yanam 
##      312702       71576
```

```r
table(puducherry$district)
```

```
## 
##   Karaikal Puducherry 
##     298262    1572442
```

```r
table(puducherry$main_town)
```

```
## 
##               Abishegapakkam                    Agraharam 
##                         9794                         7388 
##                Akkaraivattam                   Alankuppam 
##                         6462                         7090 
##                Amankoilpathu                 Ambagarathur 
##                        10030                         9180 
##               Ambedkar Nagar                Ammaiyar Koil 
##                         3542                         5354 
##               Andhoniar Koil               Andiyarpalayam 
##                         5942                         5518 
##                   Anna Nagar                 Ariyankuppam 
##                        10100                        12756 
##            Ariyankuppam West                       Ariyur 
##                        10782                        13014 
##              Arumparthapuram                  Ashok Nagar 
##                        19820                        11268 
##                Bahour (East)                Bahour (West) 
##                         7728                         9968 
##          Bharathidasan Nagar                  Brindavanam 
##                         7084                        13204 
##                Calve College                   Cassukadai 
##                         1292                        10742 
##                    Cathedral           Chalakkara (North) 
##                         4232                         5822 
##           Chalakkara (South)                 Cherukallayi 
##                         4368                         1754 
##                    Chettipet                  Chinnakadai 
##                         5030                         2472 
##                  Choodikotta                  Colas Nagar 
##                         1418                         8694 
##                 Debbessanpet      Dhanvantri Nagar JIPMER 
##                         2078                         2150 
##                  Dharmapuram                   Dharmapuri 
##                         9904                        11532 
##                   Earipakkam                     Edatheru 
##                         4402                         1872 
##            Ellapillaichavadi                      Embalam 
##                        11972                         7416 
##                     Farampet                    Giriumpet 
##                         9146                        13948 
##                Goubert Nagar                   Govindapet 
##                         9406                         6184 
##      Govt. Quarters, Lawspet                 Ilango Nagar 
##                         8066                         7076 
##                 Indira Nagar                Jawahar Nagar 
##                        12892                         9420 
##                 Kadersulthan                  Kadhirkamam 
##                         7646                         9204 
##               Kakkayanthoppe          Kalitheerthalkuppam 
##                        15044                        11984 
##                  Kalmandabam                Kamaraj Nagar 
##                        12798                         6670 
##            Kanagachettikulam                  Kanakalapet 
##                         4860                         6568 
##                    Kanuvepet             Karikkalampakkam 
##                         5616                         9766 
##               Kariyamanikkam Kariyamputhur Panayadikuppam 
##                         5666                         8250 
##                Karukkangkudi               Karuvadikuppam 
##                         4398                        16812 
##                Katterikuppam                 Keerapalayam 
##                         8022                        18258 
##                   Keezhaiyur               Keezhakasukudy 
##                         5582                         8774 
##                  Keezhamanai               Kirambuthottam 
##                         3902                         6012 
##                Kirumampakkam                     Kodathur 
##                         9262                         5198 
##                    Koilpathu                  Kolathumedu 
##                        15080                         4100 
##                    Kombakkam                  Koodapakkam 
##                        10736                         9712 
##                      Korkadu                   Kothukulam 
##                         4778                         5020 
##                   Kottaimedu           Kottucherry (East) 
##                        17912                         9256 
##           Kottucherry (West)               Koundanpalayam 
##                         3056                         9522 
##                 Krishnavaram           Kudierruppupalayam 
##                         5642                         6050 
##                  Kunichampet                Kurinji Nagar 
##                         8420                        16802 
##                 Kurumbagaram                   Kurumbapet 
##                         4786                        12644 
##                 Kurusukuppam                 Kuruvinatham 
##                        11734                         9400 
##                Kuyavar Nagar                      Lawspet 
##                        11216                         9906 
##                    Madhagadi                 Madhagadipet 
##                         5518                         9304 
##                    Madhakoil             Madukarai (East) 
##                         3406                         9468 
##             Madukarai (West)                 Maideenpalli 
##                         4262                         8910 
##                     Manamedu                      Manapet 
##                         4774                         9050 
##                     Manaveli                     Mangalam 
##                        41790                         6998 
##                    Manjakkal                   Mannadipet 
##                         3152                         6660 
##                 Meenatchipet                 Melakasakudi 
##                        10896                         6596 
##                    Mettacuru                  Mudaliarpet 
##                        11218                         8142 
##                      Mundock                Murungapakkam 
##                         2652                        13954 
##             Muthialpet(East)               Muthirapalayam 
##                         7618                        14734 
##                Nadesan Nagar               Nainarmandapam 
##                         9644                        24646 
##                    Nallambal                    Nallavadu 
##                         5430                         6804 
##                    Nedungadu                   Nellithope 
##                         7874                        11150 
##                Neravy (East)                Neravy (West) 
##                         2260                         7628 
##                Nethaji Nagar                  Nettapakkam 
##                        12198                         8300 
##                     Odiampet                    Oduthurai 
##                        12552                         8490 
##                    Orleanpet                     Oulgaret 
##                         7656                        23170 
##                 Paidikondala              Pakkamudayanpet 
##                         8300                         9390 
##         Palloor (North-East)         Palloor (South-East) 
##                         6350                         6274 
##         Palloor (South-West)          Palloor(North-West) 
##                         4122                         4418 
##              Pandakkal-South             Pandakkal Centre 
##                         3792                         5236 
##              Pandakkal North                  Pannithittu 
##                         3956                         5586 
##                     Parakkal                  Parikkalpet 
##                         5406                         5724 
##    Parimala Mudaliar Thottam                     Pedapudi 
##                         6238                         4260 
##                   Periapalli        Periya Kalapet (East) 
##                         6300                         3518 
##        Periya Kalapet (West)                Periyar Nagar 
##                        10728                        10888 
##                 Perumal Koil               Pethuchettipet 
##                         3066                        22742 
##                       Pettai               Pillai Thottam 
##                         4882                         9510 
##                Pillaichavady              Pillaiyarkuppam 
##                        12610                         7568 
##                    Pillaraya               Pillayarkuppam 
##                         5262                         8138 
##                     Ponpethi               Pooranankuppam 
##                         2096                         6672 
##                       Poovam             Poraiyur Agharam 
##                         4716                         7276 
##                  Pudhukuppam                  Pudupalayam 
##                         3440                         9804 
##           Puliankottai Salai                Rainbow Nagar 
##                         7442                        25986 
##                   Raj Bhavan                 Rajaji Nagar 
##                         2946                        16126 
##            Ramakrishna Nagar               Reddiarpalayam 
##                         8702                        23694 
##                 Sakthi Nagar           Samipillai Thottam 
##                        11726                        12150 
##          Sandhai Pudhukuppam                Sanyasikuppam 
##                         4002                         3306 
##                        Saram                Sathamangalam 
##                         8998                         6862 
##                    Sedarapet                    Seliamedu 
##                         9756                         7898 
##                     Sellipet                       Sellur 
##                         4234                         7256 
##    Sembiapalayam (Nathamedu)                       Sethur 
##                         4592                         5952 
##                Shanmugapuram                Sivaranthagam 
##                        22688                         4720 
##                  Solai Nagar                Sooramangalam 
##                        11908                         4996 
##               Sooriyankuppam                     Sorakudi 
##                         3822                         8664 
##                      Sorapet                   Sulthanpet 
##                         8348                        13584 
##                   Suthukkeni        T.R. Pattinam (North) 
##                         6240                        12014 
##        T.R. Pattinam (South)                   Thalatheru 
##                        10942                         5650 
##               Thattanchavady                Thavalakuppam 
##                         9672                         8004 
##                Thengaithittu                    Thilaspet 
##                         8708                         9752 
##       Thimmanayakkan Palayam                Thirubhuvanai 
##                         5106                        13742 
##                  Thirukanchi                  Thirukkanur 
##                         6190                         8526 
##              Thirumudi Nagar          Thirunallar (North) 
##                         7214                         8044 
##          Thirunallar (South)          Thiruvalluvar Nagar 
##                         4372                        17922 
##            Thiruvandaar Koil               Thiruvettakudy 
##                         9912                         4584 
##               Thondamanatham                   Uruvaiyaru 
##                         7868                        11092 
##                 V.O.C. Nagar  Vadhanur-Puranasingupalayam 
##                         8646                         6982 
##                 Vaithikuppam                    Valatheru 
##                        11832                        10894 
##                      Valavil           Vamba Keerapalayam 
##                         2298                        10790 
##                    Vanarapet                      Vanjore 
##                        10782                         3374 
##                  Varichikudy          Veemacoundanpalayam 
##                         7992                         9710 
##               Veerampattinam                    Veeraveli 
##                        10148                         4764 
##             Viduthalai Nagar                    Villianur 
##                         8422                        20944 
##                 Vinoba Nagar                  Vishnalayam 
##                        13702                         1944 
##                  Vizhidhiyur                   Water Tank 
##                         5108                         5912
```
