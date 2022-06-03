# Exercise 1
table1 <- read.csv(file = 'C:/Users/romAn/OneDrive/Documents/GitHub/R/file3-1.csv');table1

library(RODBC)
channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/file3-1.xls')
table2 <- sqlFetch(channel,'Лист1');table2
odbcClose(channel)

# Exercise 2
library(RODBC)
channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/file3-2.xls')
table <- sqlFetch(channel,'Лист1');table
odbcClose(channel)

'Мода:'
v1 <- apply(table[2:11],2,table)
name <- names(v1)

i <- 1

while (i < length(table[1,])) {
  m <- max(v1[[i]])
  s <- as.integer(names(v1[[i]][v1[[i]]== m]))
  
  print(name[i])
  print(s)
  
  i <- i + 1
}

apply(table[2:11],2,summary)
apply(table[2:11],2,var)
apply(table[2:11],2,sd)
apply(table[2:11],2,function(x) max(x)-min(x))
apply(table[2:11],2,IQR)

library('viridis')
boxplot(table[,2:11], col = viridis(10), xlab = 'Рис 1. Боксплот с оценками фильмов')
hist(table$Матрица, col = viridis(10), xlab = 'Рис 2. Гистограмма с оценками фильма "Матрица"')

# Exercise 3
table[order(table$Имя),]

# Exercise 4
# 1
sub1 <- subset(table,table$Гарри_Поттер_и_Кубок_Огня > 7);sub1
dim(sub1)

'Мода:'
v1 <- apply(sub1[2:11],2,table)
name <- names(v1)

i <- 1

while (i < length(sub1[1,])) {
  m <- max(v1[[i]])
  s <- as.integer(names(v1[[i]][v1[[i]]== m]))
  
  print(name[i])
  print(s)
  
  i <- i + 1
}

apply(sub1[2:11],2,summary)
apply(sub1[2:11],2,var)
apply(sub1[2:11],2,sd)
apply(sub1[2:11],2,function(x) max(x)-min(x))
apply(sub1[2:11],2,IQR)

boxplot(sub1[2:11], col = viridis(10), xlab = 'Рис 3. Боксплот с оценками фильмов при условии, что "Гарри Поттер и Кубок Огня" > 7')
hist(sub1$Песнь_моря, col = viridis(10), xlab = 'Рис 4. Гистограмма с оценками фильма "Песнь моря" при условии, что "Гарри Поттер и Кубок Огня" > 7')

# 2
sub2 <- subset(table,table$Фантастические_твари_и_где_они_обитают < 7);sub2
dim(sub2)

'Мода:'
v1 <- apply(sub2[2:11],2,table)
name <- names(v1)

i <- 1

while (i < length(sub2[1,])) {
  m <- max(v1[[i]])
  s <- as.integer(names(v1[[i]][v1[[i]]== m]))
  
  print(name[i])
  print(s)
  
  i <- i + 1
}

apply(sub2[2:11],2,summary)
apply(sub2[2:11],2,var)
apply(sub2[2:11],2,sd)
apply(sub2[2:11],2,function(x) max(x)-min(x))
apply(sub2[2:11],2,IQR)

boxplot(sub2[2:11], col = viridis(10), xlab = 'Рис 5. Боксплот с оценками фильмов при условии, что "Фантастические твари и где они обитают" < 7')
hist(sub1$Крестный_отец, col = viridis(10), xlab = 'Рис 6. Гистограмма с оценками фильма "Крестный отец" при условии, что "Фантастические твари и где они обитают" < 7')
