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
## [1] 935352
```

Unique Values in Sex:


```r
# Unique values in sex
table(puducherry$sex)
```

```
## 
##       Female         Male Third Gender 
##       492125       443143           84
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
##      9     10     12     16     17     18 
##      5 615323     19 310180   9824      1
```

Number of characters in pin code:


```r
table(nchar(puducherry$pin_code))
```

```
## 
##      6 
## 935352
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
## [1] 935352
```


```r
# Net electors
sum(with(puducherry, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 884934
```

```r
nrow(puducherry)
```

```
## [1] 935352
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(puducherry$elector_name))
```

```
## 
##      3      4      5      6      7      8      9     10     11     12 
##   1640  25924  47206  80534 111082  90931 117150 106523 101603  77499 
##     13     14     15     16     17     18     19     20     21     22 
##  53651  28624  20038  14335  11104   9099   7883   6635   5732   4426 
##     23     24     25     26     27     28     29     30     31     32 
##   3465   2595   1942   1478   1119    778    641    515    299    240 
##     33     34     35     36     37     38     39     40     41     42 
##    170    152    105     92     51     32     28     15      6      6 
##     43     44 
##      3      1
```

```r
puducherry[which(nchar(puducherry$elector_name) < 4), c("id", "filename")]
```

```
## # A tibble: 1,640 x 2
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
## # ... with 1,630 more rows
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
##               935352
```

```r
table(puducherry$ac_name)
```

```
## 
##           1 . MANNADIPET (GEN)       10 . KAMARAJ NAGAR (GEN) 
##                          29540                          33504 
##             11 . LAWSPET (GEN)             12 . KALAPET (GEN) 
##                          30359                          31842 
##          13 . MUTHIALPET (GEN)          14 . RAJ BHAVAN (GEN) 
##                          28846                          25632 
##             15 . OUPALAM (GEN)          16 . ORLEAMPETH (GEN) 
##                          26764                          23864 
##          17 . NELLITHOPE (GEN)         18 . MUDALIARPET (GEN) 
##                          32295                          33276 
##         19 . ARIANKUPPAM (GEN)         2 . THIRUBHUVANAI (SC) 
##                          36538                          30415 
##            20 . MANAVELY (GEN)              21 . EMBALAM (SC) 
##                          31760                          31743 
##          22 . NETTAPAKKAM (SC)              23 . BAHOUR (GEN) 
##                          30848                          27997 
##            24 . NEDUNGADU (SC)         25 . THIRUNALLAR (GEN) 
##                          25478                          29089 
##      26 . KARAIKAL NORTH (GEN)      27 . KARAIKAL SOUTH (GEN) 
##                          33390                          31602 
## 28 . NERAVY-T.R.PATTINAM (GEN)                29 . MAHE (GEN) 
##                          29572                          30509 
##               3 . OUSSUDU (SC)               30 . YANAM (GEN) 
##                          28576                          35788 
##             4 . MANGALAM (GEN)            5 . VILLIANUR (GEN) 
##                          35452                          37736 
##            6 . OZHUKARAI (GEN)           7 . KADIRGAMAM (GEN) 
##                          38052                          32202 
##         8 . INDIRA NAGAR (GEN)       9 . THATTANCHAVADY (GEN) 
##                          33477                          29206
```

```r
table(puducherry$police_station)
```

```
## 
##   Ambagarathur O.P.         Ariankuppam              Bahour 
##                7305               36018               25295 
##            Cotchery     Danvantri Nagar Dariyalathippa O.P. 
##               19189               60888                6974 
##        Grand Bazaar             Kalapet            Karaikal 
##               36619               15858               56360 
##  Karayamputhur O.P.       Katterikuppam       Kirumampakkam 
##                6512                9132               20559 
##        Korkadu O.P.             Lawspet     Madukkarai O.P. 
##               13276               59139                9363 
##                Mahe       Mangalam O.P.        Mettupalayam 
##               10524               17931               33891 
##         Mudaliarpet          Muthialpet           Neduncadu 
##               57578               25602               10676 
##              Neravy         Nettapakkam          Odiansalai 
##               16925               15583               20813 
##           Orleanpet             Palloor      Pandakkal O.P. 
##               47389               15389                4596 
##      Reddiarpalayam      Sedarapet O.P.    Solai Nagar O.P. 
##               46826                4878               17737 
##       Thavalakuppam        Thirubuvanai         Thirukkanur 
##               20949               27615               23208 
##         Thirunallar       Thirupattinam           Villenour 
##               21784               16892               67265 
##               Yanam 
##               28814
```

```r
table(puducherry$mandal)
```

```
## 
##      Bahour    Karaikal        Mahe    Oulgaret  Puducherry Thirunallar 
##       90588       94564       30509      228642      244343       54567 
##   Villianur       Yanam 
##      156351       35788
```

```r
table(puducherry$district)
```

```
## 
##   Karaikal Puducherry 
##     149131     786221
```

```r
table(puducherry$main_town)
```

```
## 
##               Abishegapakkam                    Agraharam 
##                         4897                         3694 
##                Akkaraivattam                   Alankuppam 
##                         3231                         3545 
##                Amankoilpathu                 Ambagarathur 
##                         5015                         4590 
##               Ambedkar Nagar                Ammaiyar Koil 
##                         1771                         2677 
##               Andhoniar Koil               Andiyarpalayam 
##                         2971                         2759 
##                   Anna Nagar                 Ariyankuppam 
##                         5050                         6378 
##            Ariyankuppam West                       Ariyur 
##                         5391                         6507 
##              Arumparthapuram                  Ashok Nagar 
##                         9910                         5634 
##                Bahour (East)                Bahour (West) 
##                         3864                         4984 
##          Bharathidasan Nagar                  Brindavanam 
##                         3542                         6602 
##                Calve College                   Cassukadai 
##                          646                         5371 
##                    Cathedral           Chalakkara (North) 
##                         2116                         2911 
##           Chalakkara (South)                 Cherukallayi 
##                         2184                          877 
##                    Chettipet                  Chinnakadai 
##                         2515                         1236 
##                  Choodikotta                  Colas Nagar 
##                          709                         4347 
##                 Debbessanpet      Dhanvantri Nagar JIPMER 
##                         1039                         1075 
##                  Dharmapuram                   Dharmapuri 
##                         4952                         5766 
##                   Earipakkam                     Edatheru 
##                         2201                          936 
##            Ellapillaichavadi                      Embalam 
##                         5986                         3708 
##                     Farampet                    Giriumpet 
##                         4573                         6974 
##                Goubert Nagar                   Govindapet 
##                         4703                         3092 
##      Govt. Quarters, Lawspet                 Ilango Nagar 
##                         4033                         3538 
##                 Indira Nagar                Jawahar Nagar 
##                         6446                         4710 
##                 Kadersulthan                  Kadhirkamam 
##                         3823                         4602 
##               Kakkayanthoppe          Kalitheerthalkuppam 
##                         7522                         5992 
##                  Kalmandabam                Kamaraj Nagar 
##                         6399                         3335 
##            Kanagachettikulam                  Kanakalapet 
##                         2430                         3284 
##                    Kanuvepet             Karikkalampakkam 
##                         2808                         4883 
##               Kariyamanikkam Kariyamputhur Panayadikuppam 
##                         2833                         4125 
##                Karukkangkudi               Karuvadikuppam 
##                         2199                         8406 
##                Katterikuppam                 Keerapalayam 
##                         4011                         9129 
##                   Keezhaiyur               Keezhakasukudy 
##                         2791                         4387 
##                  Keezhamanai               Kirambuthottam 
##                         1951                         3006 
##                Kirumampakkam                     Kodathur 
##                         4631                         2599 
##                    Koilpathu                  Kolathumedu 
##                         7540                         2050 
##                    Kombakkam                  Koodapakkam 
##                         5368                         4856 
##                      Korkadu                   Kothukulam 
##                         2389                         2510 
##                   Kottaimedu           Kottucherry (East) 
##                         8956                         4628 
##           Kottucherry (West)               Koundanpalayam 
##                         1528                         4761 
##                 Krishnavaram           Kudierruppupalayam 
##                         2821                         3025 
##                  Kunichampet                Kurinji Nagar 
##                         4210                         8401 
##                 Kurumbagaram                   Kurumbapet 
##                         2393                         6322 
##                 Kurusukuppam                 Kuruvinatham 
##                         5867                         4700 
##                Kuyavar Nagar                      Lawspet 
##                         5608                         4953 
##                    Madhagadi                 Madhagadipet 
##                         2759                         4652 
##                    Madhakoil             Madukarai (East) 
##                         1703                         4734 
##             Madukarai (West)                 Maideenpalli 
##                         2131                         4455 
##                     Manamedu                      Manapet 
##                         2387                         4525 
##                     Manaveli                     Mangalam 
##                        20895                         3499 
##                    Manjakkal                   Mannadipet 
##                         1576                         3330 
##                 Meenatchipet                 Melakasakudi 
##                         5448                         3298 
##                    Mettacuru                  Mudaliarpet 
##                         5609                         4071 
##                      Mundock                Murungapakkam 
##                         1326                         6977 
##             Muthialpet(East)               Muthirapalayam 
##                         3809                         7367 
##                Nadesan Nagar               Nainarmandapam 
##                         4822                        12323 
##                    Nallambal                    Nallavadu 
##                         2715                         3402 
##                    Nedungadu                   Nellithope 
##                         3937                         5575 
##                Neravy (East)                Neravy (West) 
##                         1130                         3814 
##                Nethaji Nagar                  Nettapakkam 
##                         6099                         4150 
##                     Odiampet                    Oduthurai 
##                         6276                         4245 
##                    Orleanpet                     Oulgaret 
##                         3828                        11585 
##                 Paidikondala              Pakkamudayanpet 
##                         4150                         4695 
##         Palloor (North-East)         Palloor (South-East) 
##                         3175                         3137 
##         Palloor (South-West)          Palloor(North-West) 
##                         2061                         2209 
##              Pandakkal-South             Pandakkal Centre 
##                         1896                         2618 
##              Pandakkal North                  Pannithittu 
##                         1978                         2793 
##                     Parakkal                  Parikkalpet 
##                         2703                         2862 
##    Parimala Mudaliar Thottam                     Pedapudi 
##                         3119                         2130 
##                   Periapalli        Periya Kalapet (East) 
##                         3150                         1759 
##        Periya Kalapet (West)                Periyar Nagar 
##                         5364                         5444 
##                 Perumal Koil               Pethuchettipet 
##                         1533                        11371 
##                       Pettai               Pillai Thottam 
##                         2441                         4755 
##                Pillaichavady              Pillaiyarkuppam 
##                         6305                         3784 
##                    Pillaraya               Pillayarkuppam 
##                         2631                         4069 
##                     Ponpethi               Pooranankuppam 
##                         1048                         3336 
##                       Poovam             Poraiyur Agharam 
##                         2358                         3638 
##                  Pudhukuppam                  Pudupalayam 
##                         1720                         4902 
##           Puliankottai Salai                Rainbow Nagar 
##                         3721                        12993 
##                   Raj Bhavan                 Rajaji Nagar 
##                         1473                         8063 
##            Ramakrishna Nagar               Reddiarpalayam 
##                         4351                        11847 
##                 Sakthi Nagar           Samipillai Thottam 
##                         5863                         6075 
##          Sandhai Pudhukuppam                Sanyasikuppam 
##                         2001                         1653 
##                        Saram                Sathamangalam 
##                         4499                         3431 
##                    Sedarapet                    Seliamedu 
##                         4878                         3949 
##                     Sellipet                       Sellur 
##                         2117                         3628 
##    Sembiapalayam (Nathamedu)                       Sethur 
##                         2296                         2976 
##                Shanmugapuram                Sivaranthagam 
##                        11344                         2360 
##                  Solai Nagar                Sooramangalam 
##                         5954                         2498 
##               Sooriyankuppam                     Sorakudi 
##                         1911                         4332 
##                      Sorapet                   Sulthanpet 
##                         4174                         6792 
##                   Suthukkeni        T.R. Pattinam (North) 
##                         3120                         6007 
##        T.R. Pattinam (South)                   Thalatheru 
##                         5471                         2825 
##               Thattanchavady                Thavalakuppam 
##                         4836                         4002 
##                Thengaithittu                    Thilaspet 
##                         4354                         4876 
##       Thimmanayakkan Palayam                Thirubhuvanai 
##                         2553                         6871 
##                  Thirukanchi                  Thirukkanur 
##                         3095                         4263 
##              Thirumudi Nagar          Thirunallar (North) 
##                         3607                         4022 
##          Thirunallar (South)          Thiruvalluvar Nagar 
##                         2186                         8961 
##            Thiruvandaar Koil               Thiruvettakudy 
##                         4956                         2292 
##               Thondamanatham                   Uruvaiyaru 
##                         3934                         5546 
##                 V.O.C. Nagar  Vadhanur-Puranasingupalayam 
##                         4323                         3491 
##                 Vaithikuppam                    Valatheru 
##                         5916                         5447 
##                      Valavil           Vamba Keerapalayam 
##                         1149                         5395 
##                    Vanarapet                      Vanjore 
##                         5391                         1687 
##                  Varichikudy          Veemacoundanpalayam 
##                         3996                         4855 
##               Veerampattinam                    Veeraveli 
##                         5074                         2382 
##             Viduthalai Nagar                    Villianur 
##                         4211                        10472 
##                 Vinoba Nagar                  Vishnalayam 
##                         6851                          972 
##                  Vizhidhiyur                   Water Tank 
##                         2554                         2956
```
