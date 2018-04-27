## Dadra and Nagar Haveli

Basic descriptive statistics about the data. And sanity checks.


```r
dadra <- readr::read_csv("dadra.csv")
```

```
## Parsed with column specification:
## cols(
##   .default = col_character(),
##   number = col_integer(),
##   age = col_integer(),
##   part_no = col_integer(),
##   year = col_integer(),
##   net_electors_male = col_integer(),
##   net_electors_female = col_integer(),
##   net_electors_total = col_integer()
## )
```

```
## See spec(...) for full column specifications.
```

Number of rows:


```r
nrow(dadra)
```

```
## [1] 217840
```

Unique Values in Sex:


```r
# Unique values in sex
table(dadra$sex)
```

```
## 
## Female   Male 
## 100464 117376
```

Summary of Age:


```r
# Age
summary(dadra$age)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   18.00   28.00   36.00   39.17   47.00  107.00
```

No. of characters in ID:

```r
# Length of ID
table(nchar(dadra$id))
```

```
## 
##      4      7     10     11 
##      1      1 217837      1
```

Number of characters in pin code:


```r
table(nchar(dadra$pin_code))
```

```
## < table of extent 0 >
```


```r
# Net electors
sum(with(dadra, rowSums(cbind(net_electors_male, net_electors_female), na.rm = T) == net_electors_total), na.rm = T)
```

```
## [1] 217840
```

```r
nrow(dadra)
```

```
## [1] 217840
```

No. of characters in elector name and checks around that:

```r
## Checks that succeeded
table(nchar(dadra$elector_name))
```

```
## 
##     1     2     3     4     5     6     7     8     9    10    11    12 
##     1    19   162  3229  8831 10660  9127  8709  9150 11931 11742 12861 
##    13    14    15    16    17    18    19    20    21    22    23    24 
## 17121 21953 25583 25350 16813 11108  6753  3933  1812   643   208   104 
##    25    26    27 
##    25     9     3
```

```r
dadra[which(nchar(dadra$elector_name) < 4), "filename"]
```

```
## # A tibble: 182 x 1
##    filename        
##    <chr>           
##  1 eng_main_222.pdf
##  2 eng_main_036.pdf
##  3 eng_main_036.pdf
##  4 eng_main_036.pdf
##  5 eng_main_036.pdf
##  6 eng_main_036.pdf
##  7 eng_main_159.pdf
##  8 eng_main_252.pdf
##  9 eng_main_132.pdf
## 10 eng_main_132.pdf
## # ... with 172 more rows
```

Basic admin. units:

```r
table(dadra$police_station)
```

```
## < table of extent 0 >
```

```r
table(dadra$mandal)
```

```
## < table of extent 0 >
```

```r
table(dadra$district)
```

```
## < table of extent 0 >
```

```r
table(dadra$main_town)
```

```
## < table of extent 0 >
```
