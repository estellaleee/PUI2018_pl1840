# Idea
you should say why this is interesting and why you would think that. what do you mean se=pend more time? the duration of the trip? the total number of hours per person? confusing

# Null hypothesis
Here you need to clarify: more time per ride or more time altogether? it does not make nuch sense to do altogether cause the 
number of rides is vastly different!

Otherwise the NH is consistent with the idea


# Formula
does not render. I know mine did not either, but you do not need tocontinue perpetrating my mistakes, do you??
ok in content though

# Data
the data is not processed correctly. For what I can tell you extracted the fraction of trips on a given day of the week by user type.
you counted the trips, which does not at all get to the answer of who spends more time. 
to answer who spends more time you need the start time and end time, take the difference, 
that is your trip duratin (pr maybe that is already in the data)
then you need to group that by user type (not day of the week cause thst does not fall in your questino at all!) 

if you want to answer a question abot overall time spent on bike then you need to .sum() that, not .count() that,
if you want to answer a question abot time per ride you need to then divide that nunmber by the number you have now, the number of rides total by user type

but now you have two absolute numbers, and you cannot do statistics measuring absolute numbers! you need to measure statistics to do statistics, mean, median, standard deviation etc.

so do not SUM to get the total duration, but take the mean of duration by user type, and its stndard deviation. that is the data you need to do the test 

# Test

this is a difference between means of samples, so the t test would work. however the distributions are not Gaussian. the t-test assumes Gaussianity and your distributions are not Gaussian. a non parametric test for difference of means is the Mann-Whitney U test (https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1b-statistical-methods/parametric-nonparametric-tests) since the samples is large, the t-test may be ok
here is a list of assumptions the t-test makes https://www.investopedia.com/ask/answers/073115/what-assumptions-are-made-when-conducting-ttest.asp
