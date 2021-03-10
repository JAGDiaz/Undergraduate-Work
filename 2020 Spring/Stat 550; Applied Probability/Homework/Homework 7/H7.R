coincidence=function(n,m)
{
  `%!in%` <- Negate(`%in%`)
  v = replicate(n, if(TRUE %!in% (1:m == sample(1:m,m))) 1 else 0)
  return(1-mean(v))
}
coincidence(10000,10000)

DiceGame=function(n)
{
  rolls = sample(1:6, n, replace = TRUE)
  distrib = c(0,0,0)
  for(i in 1:n)
  {
    if(rolls[i] == 6)
    {
      rolls[i] = 24
      distrib[3] = distrib[3] + 1
    }
    else if(rolls[i] %in% c(4,5))
    {
      rolls[i] = 0
      distrib[2] = distrib[2] + 1
    }
    else
    {
      rolls[i] = -10
      distrib[1] = distrib[1] + 1
    }
  }
  return(list("rolls" = rolls, "distrib" = distrib))
}
result = DiceGame(10000)
rolls = result$rolls
distrib = result$distrib
winnings = c(-10, 0, 24)
par(mar=c(10,5,10,5))
barplot(distrib, main = "Frequency of outcomes per 1000 games",names.arg = winnings)

mean(rolls)
var(rolls)

