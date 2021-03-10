
```{r}
setwd ("C:\\Users\\shotg\\Documents\\School Work\\Spring 2020\\Stat 550; Applied Probability\\Homework\\Homework 4")
```
# Modify CoinFlip.R

# CoinFlip.R
# Trial
# trial <- sample(0:1,3,replace=TRUE)
# Success
# if (sum(trial)==3) 1 else 0
# Replication
# n <- 10000 # Number of repetitions
# simlist <- numeric(n) # Initialize vector
# for (i in 1:n) {
#  trial <- sample(0:1, 3, replace=TRUE)
#  success <- if (sum(trial)==3) 1 else 0
#  simlist[i] <- success }
# mean(simlist) # Proportion of trials with 3 heads

# 1.41
CoinFlip4 = function(n)
{
  flip = matrix(sample(0:1, 4*n, replace = TRUE), nrow = 4, byrow = FALSE)
  total = flip[1,1:n] + flip[2,1:n] + flip[3,1:n] + flip[4,1:n]
  mean(total == 1)
}

# 1.42
Divisible4710 = function(n)
{
  num = sample(1:5000, n, replace = TRUE)
  mean(num%%4==0|num%%7==0|num%%10==0)
}

# 1.43
SumTo8 = function(n)
{
  rolls = matrix(sample(1:6, 2*n, replace = TRUE), nrow = 2, byrow = FALSE)
  total = rolls[1,1:n] + rolls[2,1:n]
  mean(total >= 8)
}

# 1.44
TetraDice = function(n)
{
  rolls = matrix(sample(1:4, 5*n, replace = TRUE), nrow = 5, byrow = FALSE)
  success = numeric(n)
  for(i in 1:n)
  {
    success[i] = if(2 %in% rolls[1:5,i]) 1 else 0
  }
  mean(success)
}

n = 100000

CoinFlip4(n)

Divisible4710(n)

SumTo8(n)

TetraDice(n)
