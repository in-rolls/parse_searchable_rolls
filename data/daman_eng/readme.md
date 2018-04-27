## Daman and Diu

Basic descriptive statistics about the data. And sanity checks.


```r
daman <- readr::read_csv("daman.csv")
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
nrow(daman)
```

```
## [1] 116464
```

Unique Values in Sex:


```r
# Unique values in sex
table(daman$sex)
```

```
## 
## Female   Male 
##  57832  58632
```

Summary of Age:


```r
# Age
summary(daman$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##     0.0    25.0    34.0    36.8    45.0   116.0
```

Check if 0 and missing age is from problem in the electoral roll:


```r
daman[which(daman$age == 0), c("id", "filename")]
```

```
## # A tibble: 8 x 2
##   id         filename   
##   <chr>      <chr>      
## 1 PJG2381820 eng_020.pdf
## 2 PJG2979730 eng_135.pdf
## 3 PJG2933471 eng_135.pdf
## 4 PJG2412302 eng_017.pdf
## 5 PJG2464469 eng_035.pdf
## 6 PJG2191534 eng_015.pdf
## 7 PJG2547586 eng_045.pdf
## 8 PJG2410017 eng_066.pdf
```

No. of characters in ID:

```r
# Length of ID
table(nchar(daman$id))
```

```
## 
##      4      5      6      7      8      9     10     11     13     14 
##     12     67     51    113    120     10 114471      9      1      3 
##     15     16     17 
##      5    452     11
```

Number of characters in pin code:


```r
table(nchar(daman$pin_code))
```

```
## 
##      6 
## 116464
```

Are IDs duplicated?


```r
length(unique(daman$id))
```

```
## [1] 114936
```

```r
nrow(daman)
```

```
## [1] 116464
```


```r
# Net electors
sum(with(daman, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 116464
```

```r
nrow(daman)
```

```
## [1] 116464
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(daman$elector_name))
```

```
## 
##    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17 
##    1   44  141  216  222  457 1005 2227 3940 4982 4972 4718 4299 4236 4748 
##   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32 
## 5482 6541 6959 7134 7000 7123 7268 7673 7318 6180 4462 3005 1728  963  569 
##   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47 
##  359  174  100   47   41   34   22   18   20    8    3    5    5    6    2 
##   48   49   51   52   54 
##    1    2    1    1    2
```

```r
daman[which(nchar(daman$elector_name) < 4), "filename"]
```

```
## # A tibble: 1 x 1
##   filename   
##   <chr>      
## 1 eng_119.pdf
```

Does district have a number?

```r
sum(grepl('[0-9]', daman$district))
```

```
## [1] 0
```

Basic admin. units:

```r
table(daman$parl_constituency)
```

```
## < table of extent 0 >
```

```r
table(daman$ac_name)
```

```
## 
## 1 - Daman & Diu (General) 
##                    116464
```

```r
table(daman$police_station)
```

```
## 
## DAMAN   DIU 
## 79211 37253
```

```r
table(daman$mandal)
```

```
## < table of extent 0 >
```

```r
table(daman$district)
```

```
## 
## DAMAN   DIU 
## 79211 37253
```

```r
table(daman$main_town)
```

```
## 
##   BHENSLORE    BHIMPORE  BUCHARWADA      DABHEL     DALWADA   DAMANWADA 
##        1371        3601        2787       10180        1584        2938 
##       DEVKA         DIU     DUNETHA     GHOGHLA     JAMPORE JANI VANKAD 
##        1751        7983        4672       11636        1262        1258 
##    KACHIGAM     KADAIYA   MAGARWADA      MARWAD  MOTI DAMAN  NAILAPARDI 
##        3149        2397        3438        1402        4780         912 
##  NANI DAMAN    PARIYARI     PATLARA  RINGANWADA    SAUDWADI   VANAKBARA 
##       25538         951        3705        1075        5583        7129 
##     VARKUND    ZOLAWADI 
##        3247        2135
```
