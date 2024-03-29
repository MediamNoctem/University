# Exercise 1
table1 <- read.csv(file = 'C:/Users/romAn/OneDrive/Documents/GitHub/R/file3-1.csv');table1

library(RODBC)
channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/file3-1.xls')
table2 <- sqlFetch(channel,'����1');table2
odbcClose(channel)

# Exercise 2
library(RODBC)
channel <- odbcConnectExcel2007('C:/Users/romAn/OneDrive/Documents/GitHub/R/file3-2.xls')
table <- sqlFetch(channel,'����1');table
odbcClose(channel)

'����:'
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
boxplot(table[,2:11], col = viridis(10), xlab = '��� 1. �������� � �������� �������')
hist(table$�������, col = viridis(10), xlab = '��� 2. ����������� � �������� ������ "�������"')

# Exercise 3
table[order(table$���),]

# Exercise 4
# 1
sub1 <- subset(table,table$�����_������_�_�����_���� > 7);sub1
dim(sub1)

'����:'
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

boxplot(sub1[2:11], col = viridis(10), xlab = '��� 3. �������� � �������� ������� ��� �������, ��� "����� ������ � ����� ����" > 7')
hist(sub1$�����_����, col = viridis(10), xlab = '��� 4. ����������� � �������� ������ "����� ����" ��� �������, ��� "����� ������ � ����� ����" > 7')

# 2
sub2 <- subset(table,table$��������������_�����_�_���_���_������� < 7);sub2
dim(sub2)

'����:'
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

boxplot(sub2[2:11], col = viridis(10), xlab = '��� 5. �������� � �������� ������� ��� �������, ��� "�������������� ����� � ��� ��� �������" < 7')
hist(sub1$��������_����, col = viridis(10), xlab = '��� 6. ����������� � �������� ������ "�������� ����" ��� �������, ��� "�������������� ����� � ��� ��� �������" < 7')
