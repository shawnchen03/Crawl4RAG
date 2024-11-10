

# Bundle: finance_articles

# Finance Articles Collection

## Table of Contents

### General
- [Towards Data Science](#towards-data-science)
- [Towards Data Science](#towards-data-science)
- [Towards Data Science](#towards-data-science)

---

# General

## Towards Data Science

Source: https://medium.com/towards-data-science/the-statistical-significance-scam-db904be36714
Date fetched: 2024-11-10T01:45:17.300885

---

Title: The Statistical Significance Scam - Towards Data Science

URL Source: https://medium.com/towards-data-science/the-statistical-significance-scam-db904be36714

Published Time: 2024-11-09T12:02:00.274Z

Markdown Content:
A detailed look into the flaws of science’s favorite tool
---------------------------------------------------------

[![Image 1: Cai Parry-Jones](https://miro.medium.com/v2/da:true/resize:fill:88:88/0*GWV4mbIw3Ex5l9PC)](https://medium.com/@caiparryjones96?source=post_page---byline--db904be36714--------------------------------)

[![Image 2: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--db904be36714--------------------------------)

![Image 3: a white dice with blue dots on it](https://miro.medium.com/v2/resize:fit:700/1*fUigVfmuyNJLUFY6m-lZUw.jpeg)

source: [unsplash.com](https://unsplash.com/)

Statistical significance is like the drive-thru of the research world. Roll up to the study, grab your “significance meal,” and boom — you’ve got a tasty conclusion to share with all your friends. And it isn’t just convenient for the reader, it makes researchers’ lives easier too. Why make the hard sell when you can say two words instead?

But there’s a catch.

Those fancy equations and nitty-gritty details we’ve conveniently avoided? They’re the real meat of the matter. And when researchers and readers rely too heavily on one statistical tool, we can end up making a whopper of a mistake, like the one that nearly broke the laws of physics.

In 2011, physicists at the renowned CERN laboratory announced a shocking discovery: [neutrinos could travel faster than the speed of light](https://www.science.org/content/article/neutrinos-travel-faster-light-according-one-experiment). The finding threatened to overturn Einstein’s theory of relativity, a cornerstone of modern physics. The researchers were confident in their results, passing physics’ rigorous statistical significance threshold of 99.9999998%. Case closed, right?

Not quite. As other scientists scrutinized the experiment, they found flaws in the methodology and ultimately [could not replicate the results](https://www.nbcnews.com/id/wbna46760561). The original finding, despite its impressive “statistical significance,” turned out to be false.

In this article, we’ll delve into four critical reasons why you shouldn’t instinctively trust a statistically significant finding. Moreover, why you shouldn’t habitually discard non-statistically significant results.

TL;DR
-----

The four key flaws of statistical significance:

1.  **It’s made up**: The statistical significance/non-significance line is all too often plucked out of thin air, or lazily taken from the general line of 95% confidence.
2.  **It doesn’t mean what (most) people think it means**: Statistical significance does not mean ‘There is Y% chance X is true’.
3.  **It’s easy to hack (and frequently is)**: Randomness is frequently labeled statistically significant due to mass experiments.
4.  **It’s nothing to do with how important the result is**: Statistical significance is not related to the significance of the difference.

Flaw 1: It’s made up
--------------------

Statistical significance is simply a line in the sand humans have created with _zero_ mathematical support. Think about that for a second. Something that is generally thought of as an objective measure is, at its core, entirely subjective.

The mathematical part is provided one step before deciding on the significance, via a numerical measure of confidence. The most common form used in [hypothesis testing](https://www.scribbr.com/statistics/hypothesis-testing/) is called the [p-value](https://www.scribbr.com/statistics/p-value/). This provides the actual mathematical probability that the test data results were not simply due to randomness.

For example, a p-value of 0.05 means there’s a 5% chance of seeing these data points (or more extreme) due to random chance, or that we are 95% confident the result wasn’t due to chance. For example, suppose you believe a coin is unfair in favour of heads i.e. the probability of landing on heads is greater than 50%. You toss the coin 5 times and it lands on heads each time. There’s a 1/2 x 1/2 x 1/2 x 1/2 x 1/2 = 3.1% chance that it happened simply because of chance, if the coin was fair.

But is this enough to say it’s statistically significant? It depends who you ask.

Often, whoever is in charge of determining where the line of significance will be drawn in the sand has more influence on whether a result is significant than the underlying data itself.

Given this subjective final step, often in my own analysis I’d provide the reader of the study with the level of confidence percentage, rather than the binary significance/non-significance result. The final step is simply too opinion-based.

**Sceptic**: “_But there are standards in place for determining statistical significance._”

I hear the argument a lot in response to my argument above (I talk about this quite a bit — much to the delight of my academic researcher girlfriend). To which, I respond with something like:

**Me**: “_Of course, if there is a specific standard you must adhere to, such as for regulatory or academic journal publishing reasons, then you have no choice but to follow the standard. But if that isn’t the case then there’s no reason not to._”

**Sceptic**: “_But there is a general standard. It’s 95% confidence._”

At that point in the conversation I try my best not to roll my eyes. Deciding your test’s statistical significance point is 95%, simply because that is the norm, is frankly lazy. It doesn’t take into account the context of what is being tested.

In my day job, if I see someone using the 95% significance threshold for an experiment without a contextual explanation, it raises a red flag. It suggests that the person either doesn’t understand the implications of their choice or doesn’t care about the specific business needs of the experiment.

An example can best explain why this is so important.

Suppose you work as a data scientist for a tech company, and the UI team want to know, “Should we use the color red or blue for our ‘subscribe’ button to maximise out Click Through Rate (CTR)?”. The UI team favour neither color, but must choose one by the end of the week. After some A/B testing and statistical analysis we have our results:

![Image 4: a blue button with red text and a red button with blue text](https://miro.medium.com/v2/resize:fit:700/1*A9Ww6nQvuY8eag5cfrBvZw.png)

Image created by the author.

The follow-the-standards data scientist may come back to the UI team announcing, “_Unfortunately, the experiment found no statistically significant difference between the click-through rate of the red and blue button._”

This is a horrendous analysis, purely due to the final subjective step. Had the data scientist taken the initiative to understand the context, critically, that ‘the UI team favour neither color, but must choose one by the end of the week’, then she should have set the significance point at a very high p-value, arguably 1.0 i.e. the statistical analysis doesn’t matter, the UI team are happy to pick whichever color had the highest CTR.

Given the risk that data scientists and the like may not have the full context to determine the best point of significance, it’s better (and simpler) to give the responsibility to those who have the full business context — in this example, the UI team. In other words, the data scientist should have announced to the UI team, “_The experiment resulted with the blue button receiving a higher click-through rate, with a confidence of 94% that this wasn’t attributed to random chance._” The final step of determining significance should be made by the UI team. Of course, this doesn’t mean the data scientist shouldn’t educate the team on what “c_onfidence of 94%”_ means, as well as clearly explaining _why_ the statistical significance is best left to them.

Flaw 2: It doesn’t mean what (most) people think it means
---------------------------------------------------------

Let’s assume we live in a slightly more perfect world, where point one is no longer an issue. The line in the sand figure is always perfect, huzza! Say we want to run an experiment, with the the significance line set at 99% confidence. Some weeks pass and at last we have our results and the statistical analysis finds that it’s statistically significant, huzza again!.. But what does that actually mean?

Common belief, in the case of hypothesis testing, is that there is a 99% chance that the hypothesis is correct. This is painfully wrong. All it means is there is a 1% chance of observing data this extreme or more extreme by randomness _for this experiment_.

Statistical significance doesn’t take into account whether the experiment itself is accurate. Here are some examples of things statistical significance can’t capture:

*   Sampling quality: The population sampled could be biased or unrepresentative.
*   Data quality: Measurement errors, missing data, or other data quality issues aren’t addressed.
*   Assumption validity: The statistical test’s assumptions (like normality, independence) could be violated.
*   Study design quality: Poor experimental controls, not controlling for confounding variables, testing multiple outcomes without adjusting significance levels.

Coming back to the example mentioned in the introduction. After failures to independently replicate the initial finding, physicists of the original 2011 experiment announced they had found a bug in their measuring device’s master clock i.e. data quality issue, which resulted in a full retraction of their initial study.

The next time you hear a statistically significant discovery that goes against common belief, don’t be so quick to believe it.

Flaw 3: It’s easy to hack (and frequently is)
---------------------------------------------

Given statistical significance is all about how likely something may have occurred due to randomness, an experimenter who is more interested in achieving a statistical significant result than uncovering the truth can quite easily game the system.

The odds of rolling two ones from two dice is (1/6 × 1/6) = 1/36, or 2.8%; a result so rare it would be classified as statistically significant by many people. But what if I throw more than two dice? Naturally, the odds of at least two ones will rise:

*   3 dice: ≈ 7.4%
*   4 dice: ≈ 14.4%
*   5 dice: ≈ 23%
*   6 dice: ≈ 32.4%
*   7 dice: ≈ 42%
*   8 dice: ≈ 51%
*   12 dice: ≈ 80%\*

> \*At least two dice rolling a **one** is the equivalent of: 1 (i.e. 100%, certain), minus the probability of rolling zero **ones,** minus the probability of rolling only one **one**
> 
> P(zero **ones**) = (5/6)^n
> 
> P(exactly one **one**) = n \* (1/6) \* (5/6)^(n-1)
> 
> n is the number of dice
> 
> So the complete formula is: **1 — (5/6)^n — n\*(1/6)\*(5/6)^(n-1)**

Let’s say I run a simple experiment, with an initial theory that **one** is more likely than other numbers to be rolled. I roll 12 dice of different colors and sizes. Here are my results:

![Image 5: a set of dominoes in different colors](https://miro.medium.com/v2/resize:fit:700/1*y8j26EpfI1iKs9uMJFZnew.png)

Image created by the author.

Unfortunately, my (calculated) hopes of getting at least two **ones** have been dashed… Actually, now that I think of it, I didn’t really want two ones. I was more interested in the odds of big red dice. I believe there is a high chance of getting sixes from them. Ah! Looks like my theory is correct, the two big red dice have rolled sixes! There is only a 2.8% chance of this happening by chance. Very interesting. I shall now write a paper on my findings and aim to publish it in an academic journal that accepts my result as statistically significant.

This story may sound far-fetched, but the reality isn’t as distant from this as you’d expect, especially in the highly regarded field of academic research. In fact, this sort of thing happens frequently enough to make a name for itself, [p-hacking](https://statisticsbyjim.com/hypothesis-testing/p-hacking/#:~:text=P%20hacking%20is%20the%20manipulation,the%20integrity%20of%20scientific%20research.).

If you’re surprised, delving into the academic system will clarify why practices that seem abominable to the scientific method occur so frequently within the realm of science.

Academia is exceptionally difficult to have a successful career in. For example, In STEM subjects only [0.45% of PhD students become professors](https://occamstypewriter.org/athenedonald/2014/02/08/thinking-about-the-pipeline/). Of course, some PhD students don’t want an academic career, but the majority do (67% according to [this](https://www.hepi.ac.uk/wp-content/uploads/2020/07/HEPI-Policy-Note-25_PhD-students-careers_FINAL.pdf) survey). So, roughly speaking, you have a 1% chance of making it as a professor if you have completed a PhD and want to make academia your career. Given these odds you need think of yourself as quite exceptional, or rather, you need other people to think that, since you can’t hire yourself. So, how is exceptional measured?

Perhaps unsurprisingly, the most important measure of an academic’s success is their [research impact](https://www.lib.ncsu.edu/measuring-research-impact/your-impact#:~:text=Research%20impact%20is%20often%20measured,index%2C%20and%20journal%20impact%20factors.). Common measures of author impact include the h-index, g-index and i10-index. What they all have in common is they’re heavily focused on citations i.e. how many times has their published work been mentioned in other published work. Knowing this, if we want to do well in academia, we need to focus on publishing research that’s likely to get citations.

You’re far [more likely to be cited if you publish your work in a highly rated academic journal](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24810#:~:text=There%20is%20strong%20evidence%20from,tend%20to%20be%20more%20cited.). And, since [88% of top journal papers are statistically significant](https://pubmed.ncbi.nlm.nih.gov/19892276/), you’re far more likely to get accepted into these journals if your research is statistically significant. This pushes a lot of well-meaning, but career-driven, academics down a slippery slope. They start out with a scientific methodology for producing research papers like so:

But end up warping their methodology to look scientific on the surface — but really, they’ve thrown proper scientific methods out the window:

Given the decision diagrams have the researcher writing the paper _after_ discovering a significant result, there’s no evidence for the journal reviewer to criticise the experiment for p-hacking.

That’s the theory anyway. But does it really happen all that often in reality?

The answer is a resounding yes. In fact, the [majority of scientific research is unreproducible by fellow academics](https://www.bbc.co.uk/news/science-environment-39054778). Unreproducible means a research paper attempts to copy another research paper’s experiment, but ends up with statistically unexpected results. Often finding a statistically significant result in the original paper was statistically insignificant in the replication, or in [some instances](https://journals.sagepub.com/doi/full/10.1177/1745691616652873) statistically significant in the opposite direction!

Flaw 4: It’s nothing to do with how important the result is
-----------------------------------------------------------

Finally, statistical significance doesn’t care about the scale of the difference.

Think about it this way — statistical significance basically just tells you “hey, this difference probably isn’t due to random chance” but says nothing about whether the difference actually matters in the real world.

Let’s say you test a new medication and find it reduces headache pain by 0.0001% compared to a placebo. If you run this test on millions of people, that tiny difference might be statistically significant, since your sample size is massive. But… who cares about a 0.0001% reduction in pain? That’s meaningless in practical terms!

On the other hand, you might find a drug that reduces pain by 5%, but there hasn’t been a large experiment to demonstrate statistical significance. It’s likely there are many examples of this in medicine because if the drug in question is cheap there is no incentive for pharmaceutical companies to run the experiment since large scale medical testing is expensive.

This is why it’s important to look at effect size (how big the difference is) separately from statistical significance. In the real world, you want both — a difference that’s unlikely to be random _and_ big enough to actually matter.

An example of this mistake happening time and time again is when there is a (statistically significant) discovery in carcinogens i.e. something that causes cancer. A 2015 Guardian [article](https://www.theguardian.com/society/2015/oct/26/bacon-ham-sausages-processed-meats-cancer-risk-smoking-says-who) said:

> “Bacon, ham and sausages rank alongside cigarettes as a major cause of cancer, the World Health Organisation has said, placing cured and processed meats in the same category as asbestos, alcohol, arsenic and tobacco.”

This is straight up misinformation. Indeed, bacon, ham and sausages are in the same category as asbestos, alcohol, arsenic and tobacco. However, the categories do not denote the scale of the effect of the carcinogens, rather, how confident the World Health Organisation is that these items are carcinogens i.e. statistical significance.

The scale of the cancer cases caused by processed meat is questionable, since there haven’t been any Randomized Controlled Trials (RCT). One of the most damning research in favour of processed meat causing cancer is a 2020 observational (think correlation, not causation) [study](https://academic.oup.com/ije/article/49/5/1540/5894731?login=false) in the UK. It found that people eating over 79 grams per day on average of red and processed meat had a 32% increased risk of bowel cancer compared to people eating less than 11 grams per day on average.

However, to understand the true risk we need to understand the number of people who are at risk of bowel cancer. For every 10,000 people on the study who ate less than 11 grams of processed and red meat a day, 45 were diagnosed with bowel cancer, while it was 59 from those eating 79 grams of processed and red meat a day. That’s an extra 14 extra cases of bowel cancer per 10,000 people, or 0.14%. The survivability in the UK of bowel cancer is [53%](https://www.cancerresearchuk.org/health-professional/cancer-statistics/statistics-by-cancer-type/bowel-cancer), so a rough estimate of carcinogens in processed meat killing you is 0.07%.

Compare this to another substance The Guardian mention, tobacco. [Cancer Research](https://www.cancerresearchuk.org/health-professional/cancer-statistics/risk/tobacco#heading-Zero) say:

> “Tobacco is the largest preventable cause of cancer and death in the UK. And one of the largest preventable causes of illness and death in the world. Tobacco caused an estimated 75,800 deaths in the UK in 2021 — around a tenth (11%) of all deaths from all causes.”

First of all, wow. Don’t smoke.

Secondly, the death rate of cancer caused by tobacco is 11%/0.07% = **157** times greater than processed meat! Coming back to the quotation in the article, “Bacon, ham and sausages rank alongside cigarettes as a major cause of cancer”. Simply, fake news.

Summary
-------

In conclusion, while statistical significance has a place in validating quantitative research, it’s crucial to understand its severe limitations.

As readers, we have a responsibility to approach claims of statistical significance with a critical eye. The next time you encounter a study or article touting a “statistically significant” finding, take a moment to ask yourself:

1.  Is the significance threshold appropriate for the context?
2.  How robust was the study design and data collection process?
3.  Could the researchers have engaged in p-hacking or other questionable practices?
4.  What is the practical significance of the effect size?

By asking these questions and demanding more nuanced discussions around statistical significance, we can help promote a more responsible and accurate use of the tool.

Over-time analysis
------------------

I actually think the main reason statistical significance has gained such over prominence is because of the name. People associate “statistical” with mathematical and objective, and “significance” with, well, significant. I hope this article has persuaded you that these associations are merely fallacies.

If the scientific and wider community wanted to deal with the over prominence issue, they should seriously consider simply renaming “statistical significance”. Perhaps “chance-threshold test” or “Non-random confidence”. Then again, this would lose its Big Mac convenience.


## Visual Content Analysis

### Image Analysis
Title: The Statistical Significance Scam - Towards Data Science

URL Source: https://medium.com/towards-data-science/the-statistical-significance-scam-db904be36714

Published Time: 2024-11-09T12:02:00.274Z

Markdown Content:
A detailed look into the flaws of science’s favorite tool
---------------------------------------------------------

[![Image 1: Cai Parry-Jones](https://miro.medium.com/v2/da:true/resize:fill:88:88/0*GWV4mbIw3Ex5l9PC)](https://medium.com/@caiparryjones96?source=post_page---byline--db904be36714--------------------------------)

[![Image 2: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--db904be36714--------------------------------)

![Image 3: a white dice with blue dots on it](https://miro.medium.com/v2/resize:fit:700/1*fUigVfmuyNJLUFY6m-lZUw.jpeg)

source: [unsplash.com](https://unsplash.com/)

Statistical significance is like the drive-thru of the research world. Roll up to the study, grab your “significance meal,” and boom — you’ve got a tasty conclusion to share with all your friends. And it isn’t just convenient for the reader, it makes researchers’ lives easier too. Why make the hard sell when you can say two words instead?

But there’s a catch.

Those fancy equations and nitty-gritty details we’ve conveniently avoided? They’re the real meat of the matter. And when researchers and readers rely too heavily on one statistical tool, we can end up making a whopper of a mistake, like the one that nearly broke the laws of physics.

In 2011, physicists at the renowned CERN laboratory announced a shocking discovery: [neutrinos could travel faster than the speed of light](https://www.science.org/content/article/neutrinos-travel-faster-light-according-one-experiment). The finding threatened to overturn Einstein’s theory of relativity, a cornerstone of modern physics. The researchers were confident in their results, passing physics’ rigorous statistical significance threshold of 99.9999998%. Case closed, right?

Not quite. As other scientists scrutinized the experiment, they found flaws in the methodology and ultimately [could not replicate the results](https://www.nbcnews.com/id/wbna46760561). The original finding, despite its impressive “statistical significance,” turned out to be false.

In this article, we’ll delve into four critical reasons why you shouldn’t instinctively trust a statistically significant finding. Moreover, why you shouldn’t habitually discard non-statistically significant results.

TL;DR
-----

The four key flaws of statistical significance:

1.  **It’s made up**: The statistical significance/non-significance line is all too often plucked out of thin air, or lazily taken from the general line of 95% confidence.
2.  **It doesn’t mean what (most) people think it means**: Statistical significance does not mean ‘There is Y% chance X is true’.
3.  **It’s easy to hack (and frequently is)**: Randomness is frequently labeled statistically significant due to mass experiments.
4.  **It’s nothing to do with how important the result is**: Statistical significance is not related to the significance of the difference.

Flaw 1: It’s made up
--------------------

Statistical significance is simply a line in the sand humans have created with _zero_ mathematical support. Think about that for a second. Something that is generally thought of as an objective measure is, at its core, entirely subjective.

The mathematical part is provided one step before deciding on the significance, via a numerical measure of confidence. The most common form used in [hypothesis testing](https://www.scribbr.com/statistics/hypothesis-testing/) is called the [p-value](https://www.scribbr.com/statistics/p-value/). This provides the actual mathematical probability that the test data results were not simply due to randomness.

For example, a p-value of 0.05 means there’s a 5% chance of seeing these data points (or more extreme) due to random chance, or that we are 95% confident the result wasn’t due to chance. For example, suppose you believe a coin is unfair in favour of heads i.e. the probability of landing on heads is greater than 50%. You toss the coin 5 times and it lands on heads each time. There’s a 1/2 x 1/2 x 1/2 x 1/2 x 1/2 = 3.1% chance that it happened simply because of chance, if the coin was fair.

But is this enough to say it’s statistically significant? It depends who you ask.

Often, whoever is in charge of determining where the line of significance will be drawn in the sand has more influence on whether a result is significant than the underlying data itself.

Given this subjective final step, often in my own analysis I’d provide the reader of the study with the level of confidence percentage, rather than the binary significance/non-significance result. The final step is simply too opinion-based.

**Sceptic**: “_But there are standards in place for determining statistical significance._”

I hear the argument a lot in response to my argument above (I talk about this quite a bit — much to the delight of my academic researcher girlfriend). To which, I respond with something like:

**Me**: “_Of course, if there is a specific standard you must adhere to, such as for regulatory or academic journal publishing reasons, then you have no choice but to follow the standard. But if that isn’t the case then there’s no reason not to._”

**Sceptic**: “_But there is a general standard. It’s 95% confidence._”

At that point in the conversation I try my best not to roll my eyes. Deciding your test’s statistical significance point is 95%, simply because that is the norm, is frankly lazy. It doesn’t take into account the context of what is being tested.

In my day job, if I see someone using the 95% significance threshold for an experiment without a contextual explanation, it raises a red flag. It suggests that the person either doesn’t understand the implications of their choice or doesn’t care about the specific business needs of the experiment.

An example can best explain why this is so important.

Suppose you work as a data scientist for a tech company, and the UI team want to know, “Should we use the color red or blue for our ‘subscribe’ button to maximise out Click Through Rate (CTR)?”. The UI team favour neither color, but must choose one by the end of the week. After some A/B testing and statistical analysis we have our results:

![Image 4: a blue button with red text and a red button with blue text](https://miro.medium.com/v2/resize:fit:700/1*A9Ww6nQvuY8eag5cfrBvZw.png)

Image created by the author.

The follow-the-standards data scientist may come back to the UI team announcing, “_Unfortunately, the experiment found no statistically significant difference between the click-through rate of the red and blue button._”

This is a horrendous analysis, purely due to the final subjective step. Had the data scientist taken the initiative to understand the context, critically, that ‘the UI team favour neither color, but must choose one by the end of the week’, then she should have set the significance point at a very high p-value, arguably 1.0 i.e. the statistical analysis doesn’t matter, the UI team are happy to pick whichever color had the highest CTR.

Given the risk that data scientists and the like may not have the full context to determine the best point of significance, it’s better (and simpler) to give the responsibility to those who have the full business context — in this example, the UI team. In other words, the data scientist should have announced to the UI team, “_The experiment resulted with the blue button receiving a higher click-through rate, with a confidence of 94% that this wasn’t attributed to random chance._” The final step of determining significance should be made by the UI team. Of course, this doesn’t mean the data scientist shouldn’t educate the team on what “c_onfidence of 94%”_ means, as well as clearly explaining _why_ the statistical significance is best left to them.

Flaw 2: It doesn’t mean what (most) people think it means
---------------------------------------------------------

Let’s assume we live in a slightly more perfect world, where point one is no longer an issue. The line in the sand figure is always perfect, huzza! Say we want to run an experiment, with the the significance line set at 99% confidence. Some weeks pass and at last we have our results and the statistical analysis finds that it’s statistically significant, huzza again!.. But what does that actually mean?

Common belief, in the case of hypothesis testing, is that there is a 99% chance that the hypothesis is correct. This is painfully wrong. All it means is there is a 1% chance of observing data this extreme or more extreme by randomness _for this experiment_.

Statistical significance doesn’t take into account whether the experiment itself is accurate. Here are some examples of things statistical significance can’t capture:

*   Sampling quality: The population sampled could be biased or unrepresentative.
*   Data quality: Measurement errors, missing data, or other data quality issues aren’t addressed.
*   Assumption validity: The statistical test’s assumptions (like normality, independence) could be violated.
*   Study design quality: Poor experimental controls, not controlling for confounding variables, testing multiple outcomes without adjusting significance levels.

Coming back to the example mentioned in the introduction. After failures to independently replicate the initial finding, physicists of the original 2011 experiment announced they had found a bug in their measuring device’s master clock i.e. data quality issue, which resulted in a full retraction of their initial study.

The next time you hear a statistically significant discovery that goes against common belief, don’t be so quick to believe it.

Flaw 3: It’s easy to hack (and frequently is)
---------------------------------------------

Given statistical significance is all about how likely something may have occurred due to randomness, an experimenter who is more interested in achieving a statistical significant result than uncovering the truth can quite easily game the system.

The odds of rolling two ones from two dice is (1/6 × 1/6) = 1/36, or 2.8%; a result so rare it would be classified as statistically significant by many people. But what if I throw more than two dice? Naturally, the odds of at least two ones will rise:

*   3 dice: ≈ 7.4%
*   4 dice: ≈ 14.4%
*   5 dice: ≈ 23%
*   6 dice: ≈ 32.4%
*   7 dice: ≈ 42%
*   8 dice: ≈ 51%
*   12 dice: ≈ 80%\*

> \*At least two dice rolling a **one** is the equivalent of: 1 (i.e. 100%, certain), minus the probability of rolling zero **ones,** minus the probability of rolling only one **one**
> 
> P(zero **ones**) = (5/6)^n
> 
> P(exactly one **one**) = n \* (1/6) \* (5/6)^(n-1)
> 
> n is the number of dice
> 
> So the complete formula is: **1 — (5/6)^n — n\*(1/6)\*(5/6)^(n-1)**

Let’s say I run a simple experiment, with an initial theory that **one** is more likely than other numbers to be rolled. I roll 12 dice of different colors and sizes. Here are my results:

![Image 5: a set of dominoes in different colors](https://miro.medium.com/v2/resize:fit:700/1*y8j26EpfI1iKs9uMJFZnew.png)

Image created by the author.

Unfortunately, my (calculated) hopes of getting at least two **ones** have been dashed… Actually, now that I think of it, I didn’t really want two ones. I was more interested in the odds of big red dice. I believe there is a high chance of getting sixes from them. Ah! Looks like my theory is correct, the two big red dice have rolled sixes! There is only a 2.8% chance of this happening by chance. Very interesting. I shall now write a paper on my findings and aim to publish it in an academic journal that accepts my result as statistically significant.

This story may sound far-fetched, but the reality isn’t as distant from this as you’d expect, especially in the highly regarded field of academic research. In fact, this sort of thing happens frequently enough to make a name for itself, [p-hacking](https://statisticsbyjim.com/hypothesis-testing/p-hacking/#:~:text=P%20hacking%20is%20the%20manipulation,the%20integrity%20of%20scientific%20research.).

If you’re surprised, delving into the academic system will clarify why practices that seem abominable to the scientific method occur so frequently within the realm of science.

Academia is exceptionally difficult to have a successful career in. For example, In STEM subjects only [0.45% of PhD students become professors](https://occamstypewriter.org/athenedonald/2014/02/08/thinking-about-the-pipeline/). Of course, some PhD students don’t want an academic career, but the majority do (67% according to [this](https://www.hepi.ac.uk/wp-content/uploads/2020/07/HEPI-Policy-Note-25_PhD-students-careers_FINAL.pdf) survey). So, roughly speaking, you have a 1% chance of making it as a professor if you have completed a PhD and want to make academia your career. Given these odds you need think of yourself as quite exceptional, or rather, you need other people to think that, since you can’t hire yourself. So, how is exceptional measured?

Perhaps unsurprisingly, the most important measure of an academic’s success is their [research impact](https://www.lib.ncsu.edu/measuring-research-impact/your-impact#:~:text=Research%20impact%20is%20often%20measured,index%2C%20and%20journal%20impact%20factors.). Common measures of author impact include the h-index, g-index and i10-index. What they all have in common is they’re heavily focused on citations i.e. how many times has their published work been mentioned in other published work. Knowing this, if we want to do well in academia, we need to focus on publishing research that’s likely to get citations.

You’re far [more likely to be cited if you publish your work in a highly rated academic journal](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24810#:~:text=There%20is%20strong%20evidence%20from,tend%20to%20be%20more%20cited.). And, since [88% of top journal papers are statistically significant](https://pubmed.ncbi.nlm.nih.gov/19892276/), you’re far more likely to get accepted into these journals if your research is statistically significant. This pushes a lot of well-meaning, but career-driven, academics down a slippery slope. They start out with a scientific methodology for producing research papers like so:

But end up warping their methodology to look scientific on the surface — but really, they’ve thrown proper scientific methods out the window:

Given the decision diagrams have the researcher writing the paper _after_ discovering a significant result, there’s no evidence for the journal reviewer to criticise the experiment for p-hacking.

That’s the theory anyway. But does it really happen all that often in reality?

The answer is a resounding yes. In fact, the [majority of scientific research is unreproducible by fellow academics](https://www.bbc.co.uk/news/science-environment-39054778). Unreproducible means a research paper attempts to copy another research paper’s experiment, but ends up with statistically unexpected results. Often finding a statistically significant result in the original paper was statistically insignificant in the replication, or in [some instances](https://journals.sagepub.com/doi/full/10.1177/1745691616652873) statistically significant in the opposite direction!

Flaw 4: It’s nothing to do with how important the result is
-----------------------------------------------------------

Finally, statistical significance doesn’t care about the scale of the difference.

Think about it this way — statistical significance basically just tells you “hey, this difference probably isn’t due to random chance” but says nothing about whether the difference actually matters in the real world.

Let’s say you test a new medication and find it reduces headache pain by 0.0001% compared to a placebo. If you run this test on millions of people, that tiny difference might be statistically significant, since your sample size is massive. But… who cares about a 0.0001% reduction in pain? That’s meaningless in practical terms!

On the other hand, you might find a drug that reduces pain by 5%, but there hasn’t been a large experiment to demonstrate statistical significance. It’s likely there are many examples of this in medicine because if the drug in question is cheap there is no incentive for pharmaceutical companies to run the experiment since large scale medical testing is expensive.

This is why it’s important to look at effect size (how big the difference is) separately from statistical significance. In the real world, you want both — a difference that’s unlikely to be random _and_ big enough to actually matter.

An example of this mistake happening time and time again is when there is a (statistically significant) discovery in carcinogens i.e. something that causes cancer. A 2015 Guardian [article](https://www.theguardian.com/society/2015/oct/26/bacon-ham-sausages-processed-meats-cancer-risk-smoking-says-who) said:

> “Bacon, ham and sausages rank alongside cigarettes as a major cause of cancer, the World Health Organisation has said, placing cured and processed meats in the same category as asbestos, alcohol, arsenic and tobacco.”

This is straight up misinformation. Indeed, bacon, ham and sausages are in the same category as asbestos, alcohol, arsenic and tobacco. However, the categories do not denote the scale of the effect of the carcinogens, rather, how confident the World Health Organisation is that these items are carcinogens i.e. statistical significance.

The scale of the cancer cases caused by processed meat is questionable, since there haven’t been any Randomized Controlled Trials (RCT). One of the most damning research in favour of processed meat causing cancer is a 2020 observational (think correlation, not causation) [study](https://academic.oup.com/ije/article/49/5/1540/5894731?login=false) in the UK. It found that people eating over 79 grams per day on average of red and processed meat had a 32% increased risk of bowel cancer compared to people eating less than 11 grams per day on average.

However, to understand the true risk we need to understand the number of people who are at risk of bowel cancer. For every 10,000 people on the study who ate less than 11 grams of processed and red meat a day, 45 were diagnosed with bowel cancer, while it was 59 from those eating 79 grams of processed and red meat a day. That’s an extra 14 extra cases of bowel cancer per 10,000 people, or 0.14%. The survivability in the UK of bowel cancer is [53%](https://www.cancerresearchuk.org/health-professional/cancer-statistics/statistics-by-cancer-type/bowel-cancer), so a rough estimate of carcinogens in processed meat killing you is 0.07%.

Compare this to another substance The Guardian mention, tobacco. [Cancer Research](https://www.cancerresearchuk.org/health-professional/cancer-statistics/risk/tobacco#heading-Zero) say:

> “Tobacco is the largest preventable cause of cancer and death in the UK. And one of the largest preventable causes of illness and death in the world. Tobacco caused an estimated 75,800 deaths in the UK in 2021 — around a tenth (11%) of all deaths from all causes.”

First of all, wow. Don’t smoke.

Secondly, the death rate of cancer caused by tobacco is 11%/0.07% = **157** times greater than processed meat! Coming back to the quotation in the article, “Bacon, ham and sausages rank alongside cigarettes as a major cause of cancer”. Simply, fake news.

Summary
-------

In conclusion, while statistical significance has a place in validating quantitative research, it’s crucial to understand its severe limitations.

As readers, we have a responsibility to approach claims of statistical significance with a critical eye. The next time you encounter a study or article touting a “statistically significant” finding, take a moment to ask yourself:

1.  Is the significance threshold appropriate for the context?
2.  How robust was the study design and data collection process?
3.  Could the researchers have engaged in p-hacking or other questionable practices?
4.  What is the practical significance of the effect size?

By asking these questions and demanding more nuanced discussions around statistical significance, we can help promote a more responsible and accurate use of the tool.

Over-time analysis
------------------

I actually think the main reason statistical significance has gained such over prominence is because of the name. People associate “statistical” with mathematical and objective, and “significance” with, well, significant. I hope this article has persuaded you that these associations are merely fallacies.

If the scientific and wider community wanted to deal with the over prominence issue, they should seriously consider simply renaming “statistical significance”. Perhaps “chance-threshold test” or “Non-random confidence”. Then again, this would lose its Big Mac convenience.


---

## Towards Data Science

Source: https://medium.com/towards-data-science/normalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75
Date fetched: 2024-11-10T01:45:40.778436

---

Title: Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric

URL Source: https://medium.com/towards-data-science/normalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75

Published Time: 2024-10-15T20:44:51.473Z

Markdown Content:
Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric | by Saankhya Mondal | Oct, 2024 | Towards Data Science
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F437b03529f75&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 1](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric
==========================================================================

NDCG — the rank-aware metric for evaluating recommendation systems
------------------------------------------------------------------

[![Image 2: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:88:88/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=post_page---byline--437b03529f75--------------------------------)

[Saankhya Mondal](https://saankhya.medium.com/?source=post_page---byline--437b03529f75--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--byline--437b03529f75---------------------post_header-----------)

Published in

[Towards Data Science](https://towardsdatascience.com/?source=post_page---byline--437b03529f75--------------------------------)

·

10 min read

·

Oct 15, 2024

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---header_actions--437b03529f75---------------------clap_footer-----------)

305

6

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=---header_actions--437b03529f75---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=---header_actions--437b03529f75---------------------post_audio_button-----------)

Share

Recommendation systems are everywhere. Since you’re reading this article, there’s a good chance Medium recommended it on your feed. This article will explore NDCG — Normalized Discounted Cumulative Gain, the rank-aware metric for evaluating any recommendation system model.

![Image 4: social media marketing concept with social icons and icons](https://miro.medium.com/v2/resize:fit:700/0*U7MA1X95LAKAdchq)

Image AI-Generated using Gemini

What are Recommendation Systems?
================================

Recommendation systems help users discover relevant items like products, profiles, posts, videos, ads, or information based on their preferences or behavior. These platforms handle millions of items, and displaying the most relevant ones is key to boosting user engagement and business metrics. Companies such as Amazon, LinkedIn, Twitter, Instagram, Reddit, Spotify, YouTube, Netflix, Medium, and Quora use recommendation systems in their apps.

These systems are typically two-stage systems consisting of a retrieval model followed by a ranking model. The retrieval model funnels down the most relevant items from millions of items based on a similarity metric and passes them to the ranking model. The ranking model ranks the items on a more granular level.

Create an account to read the full story.


---------------------------------------------

The author made this story available to Medium members only.  
If you’re new to Medium, create a new account to read this story on us.

[Continue in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F437b03529f75&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=regwall&source=-----437b03529f75---------------------post_regwall-----------)

Or, continue in mobile web

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75%3Fsource%3D-----437b03529f75---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----437b03529f75---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75%3Fsource%3D-----437b03529f75---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----437b03529f75---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75%3Fsource%3D-----437b03529f75---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----437b03529f75---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=-----437b03529f75---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--437b03529f75---------------------clap_footer-----------)

305

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--437b03529f75---------------------clap_footer-----------)

305

6

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=---footer_actions--437b03529f75---------------------bookmark_footer-----------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--437b03529f75---------------------follow_profile-----------)

[Published in Towards Data Science ---------------------------------](https://towardsdatascience.com/?source=post_page---post_publication_info--437b03529f75--------------------------------)

[761K Followers](https://medium.com/followers?source=post_page---post_publication_info--437b03529f75--------------------------------)

·[Last published 16 hours ago](https://medium.com/core-ai-for-any-rummy-variant-4ff414da1703?source=post_page---post_publication_info--437b03529f75--------------------------------)

Your home for data science. A publication sharing concepts, ideas and codes.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--437b03529f75---------------------follow_profile-----------)

[![Image 7: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:96:96/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=post_page---post_author_info--437b03529f75--------------------------------)

[![Image 8: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:128:128/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=post_page---post_author_info--437b03529f75--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--437b03529f75---------------------follow_profile-----------)

[Written by Saankhya Mondal --------------------------](https://saankhya.medium.com/?source=post_page---post_author_info--437b03529f75--------------------------------)

[525 Followers](https://saankhya.medium.com/followers?source=post_page---post_author_info--437b03529f75--------------------------------)

·[86 Following](https://medium.com/@saankhya/following?source=post_page---post_author_info--437b03529f75--------------------------------)

Data Scientist @ Meesho, M. Tech in AI, IISc, Bengaluru.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--437b03529f75---------------------follow_profile-----------)

More from Saankhya Mondal and Towards Data Science
--------------------------------------------------

![Image 9: Kickstart Your Data Science Journey —  A  Guide for Aspiring Data Scientists](https://miro.medium.com/v2/resize:fit:679/1*o06jXpJ_dMBlIwnR1P7XwQ.png)

[![Image 10: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists --------------------------------------------------------------------------- ### Key Technical Skills You Need to Kick-start Your Career in Data Science](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

3d ago

[300 10](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----437b03529f75----0-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

![Image 11: What Did I Learn from Building LLM Applications in 2024? — Part 1](https://miro.medium.com/v2/resize:fit:679/1*oEXNPL3qOT_XHdJnDUJDcQ.jpeg)

[![Image 12: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[What Did I Learn from Building LLM Applications in 2024? — Part 1 ----------------------------------------------------------------- ### An engineer’s journey to building LLM-native applications](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

5d ago

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----437b03529f75----1-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

![Image 13: Preference Alignment for Everyone!](https://miro.medium.com/v2/resize:fit:679/1*cbLNScjpzOf80TRVme0VZA.png)

[![Image 14: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

1d ago

[171 2](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2563cec4d10e&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpreference-alignment-for-everyone-2563cec4d10e&source=-----437b03529f75----2-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

![Image 15: Game Theory, Part 1 — The Prisoner’s Dilemma Problem](https://miro.medium.com/v2/resize:fit:679/0*mWNHxZMOZ8NhYPnt)

[![Image 16: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[Game Theory, Part 1 — The Prisoner’s Dilemma Problem ---------------------------------------------------- ### Game theory is prevalent in real-life scenarios and decision-making](https://medium.com/game-theory-part-1-the-prisoners-dilemma-problem-18b216d3b523?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

Oct 22

[113 2](https://medium.com/game-theory-part-1-the-prisoners-dilemma-problem-18b216d3b523?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F18b216d3b523&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fgame-theory-part-1-the-prisoners-dilemma-problem-18b216d3b523&source=-----437b03529f75----3-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

[See all from Saankhya Mondal](https://saankhya.medium.com/?source=post_page-----437b03529f75--------------------------------)

[See all from Towards Data Science](https://towardsdatascience.com/?source=post_page-----437b03529f75--------------------------------)

Recommended from Medium
-----------------------

![Image 17: Kickstart Your Data Science Journey —  A  Guide for Aspiring Data Scientists](https://miro.medium.com/v2/resize:fit:679/1*o06jXpJ_dMBlIwnR1P7XwQ.png)

[![Image 18: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Saankhya Mondal](https://saankhya.medium.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists --------------------------------------------------------------------------- ### Key Technical Skills You Need to Kick-start Your Career in Data Science](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

3d ago

[300 10](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----437b03529f75----0-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 19: Hang On, What’s Survival Analysis?](https://miro.medium.com/v2/resize:fit:679/1*syQ_0hAZc6gXTe4eE1mcUw.png)

[![Image 20: Klaviyo Engineering](https://miro.medium.com/v2/resize:fill:20:20/1*j4dmkFrmjReKmnzOhAy3BQ.png)](https://klaviyo.tech/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Klaviyo Engineering](https://klaviyo.tech/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Steven Her](https://medium.com/@steven.her?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Hang On, What’s Survival Analysis? ---------------------------------- ### This was a new area for the two of us, so we decided to write a post to help others in the same spot.](https://klaviyo.tech/hang-on-whats-survival-analysis-d56c2b39a593?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Jun 13

[278](https://klaviyo.tech/hang-on-whats-survival-analysis-d56c2b39a593?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd56c2b39a593&operation=register&redirect=https%3A%2F%2Fklaviyo.tech%2Fhang-on-whats-survival-analysis-d56c2b39a593&source=-----437b03529f75----1-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

Lists
-----

[![Image 21](https://miro.medium.com/v2/resize:fill:48:48/0*r4yjMpEmqzHCUvWC.jpg) ![Image 22](https://miro.medium.com/v2/resize:fill:48:48/1*bv2KUVNLi2sFNjBTdoBmWw.png) ![Image 23](https://miro.medium.com/v2/resize:fill:48:48/0*zsngbTOmFCy6sUCx.jpeg) Predictive Modeling w/ Python ----------------------------- 20 stories·1647 saves](https://medium.com/@ben.putney/list/predictive-modeling-w-python-e3668ea008e1?source=read_next_recirc-----437b03529f75--------------------------------)

[![Image 24: Principal Component Analysis for ML](https://miro.medium.com/v2/resize:fill:48:48/1*swd_PY6vTCyPnsgBYoFZfA.png) ![Image 25: Time Series Analysis](https://miro.medium.com/v2/resize:fill:48:48/1*8sSAHftNwd_RNJ3k4VA0pA.png) ![Image 26: deep learning cheatsheet for beginner](https://miro.medium.com/v2/resize:fill:48:48/1*uNyD4yNMH-DnOel1wzxOOA.png) Practical Guides to Machine Learning ------------------------------------ 10 stories·2007 saves](https://destingong.medium.com/list/practical-guides-to-machine-learning-a877c2a39884?source=read_next_recirc-----437b03529f75--------------------------------)

[![Image 27](https://miro.medium.com/v2/resize:fill:48:48/1*zPtGTCNOwu1p3kzn_sZFVQ.png) ![Image 28](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*kQIvhDkl0ixPpv4z) ![Image 29](https://miro.medium.com/v2/resize:fill:48:48/1*ERYx0IB1pN-5ZX98cKAoUw.png) General Coding Knowledge ------------------------ 20 stories·1712 saves](https://eddiebarth.medium.com/list/general-coding-knowledge-f2d429d4f0cd?source=read_next_recirc-----437b03529f75--------------------------------)

[![Image 30](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*gzCeWxDtGmD23QR5) ![Image 31](https://miro.medium.com/v2/resize:fill:48:48/1*di4WDrnS1F6_p9GWnxvPmg.png) ![Image 32](https://miro.medium.com/v2/resize:fill:48:48/1*PzJLbFrFtNkqPsxielO8zA.jpeg) Coding & Development -------------------- 11 stories·891 saves](https://medium.com/@jscribes/list/coding-development-e360d380bb82?source=read_next_recirc-----437b03529f75--------------------------------)

![Image 33: Causal Inference: an Overview](https://miro.medium.com/v2/resize:fit:679/1*XFK9jlzFyHpg7mpJb_UrNA.png)

[![Image 34: Level Up Coding](https://miro.medium.com/v2/resize:fill:20:20/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Arthur Mello](https://medium.com/@arthurmello_?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Causal Inference: an Overview ----------------------------- ### Find out when correlation actually means causation](https://levelup.gitconnected.com/causal-inference-an-overview-1254f5654b01?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Oct 13

[188 1](https://levelup.gitconnected.com/causal-inference-an-overview-1254f5654b01?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1254f5654b01&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fcausal-inference-an-overview-1254f5654b01&source=-----437b03529f75----0-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 35: Python is No More The King of Data Science](https://miro.medium.com/v2/resize:fit:679/1*uiA0nCufUQs-K64ebSUhew.jpeg)

[![Image 36: Stackademic](https://miro.medium.com/v2/resize:fill:20:20/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Oct 23

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----437b03529f75----1-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 37: Exploring Causal Decision Theory Approach with Quantile Regression](https://miro.medium.com/v2/resize:fit:679/0*4gnIT2zaaLiDVeph)

[![Image 38: Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://pub.towardsai.net/?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Towards AI](https://pub.towardsai.net/?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Shenggang Li](https://medium.com/@datalev?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Exploring Causal Decision Theory Approach with Quantile Regression ------------------------------------------------------------------ ### Using AI and Causal Decision Theory to Prioritize Restocking: Balancing Demand, Inventory Risk, and Product Importance](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

5d ago

[157 2](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa301f6028c73&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fexploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73&source=-----437b03529f75----2-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 39: Using Autoencoders to Reduce Embedding Dimensions with Matryoshka Representation Learning](https://miro.medium.com/v2/resize:fit:679/1*yuVzMhCJyDENbyhwAsrkwA.png)

[![Image 40: AI SageScribe](https://miro.medium.com/v2/resize:fill:20:20/1*ozpm5as9nAOk1kAoi6xvkA.jpeg)](https://medium.com/@aisagescribe?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[AI SageScribe](https://medium.com/@aisagescribe?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Using Autoencoders to Reduce Embedding Dimensions with Matryoshka Representation Learning ----------------------------------------------------------------------------------------- ### In the ever-evolving field of machine learning and artificial intelligence, managing high-dimensional data efficiently is a persistent…](https://medium.com/@aisagescribe/using-autoencoders-to-reduce-embedding-dimensions-with-matryoshka-representation-learning-9f48ef269b18?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Oct 14

[8](https://medium.com/@aisagescribe/using-autoencoders-to-reduce-embedding-dimensions-with-matryoshka-representation-learning-9f48ef269b18?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9f48ef269b18&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aisagescribe%2Fusing-autoencoders-to-reduce-embedding-dimensions-with-matryoshka-representation-learning-9f48ef269b18&source=-----437b03529f75----3-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

[See more recommendations](https://medium.com/?source=post_page-----437b03529f75--------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----437b03529f75--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----437b03529f75--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----437b03529f75--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----437b03529f75--------------------------------)

[Press](https://medium.com/towards-data-science/pressinquiries@medium.com?source=post_page-----437b03529f75--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----437b03529f75--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----437b03529f75--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----437b03529f75--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----437b03529f75--------------------------------)

[Teams](https://medium.com/business?source=post_page-----437b03529f75--------------------------------)


## Visual Content Analysis

### Image Analysis
Title: Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric

URL Source: https://medium.com/towards-data-science/normalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75

Published Time: 2024-10-15T20:44:51.473Z

Markdown Content:
Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric | by Saankhya Mondal | Oct, 2024 | Towards Data Science
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F437b03529f75&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 1](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric
==========================================================================

NDCG — the rank-aware metric for evaluating recommendation systems
------------------------------------------------------------------

[![Image 2: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:88:88/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=post_page---byline--437b03529f75--------------------------------)

[Saankhya Mondal](https://saankhya.medium.com/?source=post_page---byline--437b03529f75--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--byline--437b03529f75---------------------post_header-----------)

Published in

[Towards Data Science](https://towardsdatascience.com/?source=post_page---byline--437b03529f75--------------------------------)

·

10 min read

·

Oct 15, 2024

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---header_actions--437b03529f75---------------------clap_footer-----------)

305

6

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=---header_actions--437b03529f75---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=---header_actions--437b03529f75---------------------post_audio_button-----------)

Share

Recommendation systems are everywhere. Since you’re reading this article, there’s a good chance Medium recommended it on your feed. This article will explore NDCG — Normalized Discounted Cumulative Gain, the rank-aware metric for evaluating any recommendation system model.

![Image 4: social media marketing concept with social icons and icons](https://miro.medium.com/v2/resize:fit:700/0*U7MA1X95LAKAdchq)

Image AI-Generated using Gemini

What are Recommendation Systems?
================================

Recommendation systems help users discover relevant items like products, profiles, posts, videos, ads, or information based on their preferences or behavior. These platforms handle millions of items, and displaying the most relevant ones is key to boosting user engagement and business metrics. Companies such as Amazon, LinkedIn, Twitter, Instagram, Reddit, Spotify, YouTube, Netflix, Medium, and Quora use recommendation systems in their apps.

These systems are typically two-stage systems consisting of a retrieval model followed by a ranking model. The retrieval model funnels down the most relevant items from millions of items based on a similarity metric and passes them to the ranking model. The ranking model ranks the items on a more granular level.

Create an account to read the full story.


---------------------------------------------

The author made this story available to Medium members only.  
If you’re new to Medium, create a new account to read this story on us.

[Continue in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F437b03529f75&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=regwall&source=-----437b03529f75---------------------post_regwall-----------)

Or, continue in mobile web

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75%3Fsource%3D-----437b03529f75---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----437b03529f75---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75%3Fsource%3D-----437b03529f75---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----437b03529f75---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75%3Fsource%3D-----437b03529f75---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----437b03529f75---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=-----437b03529f75---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--437b03529f75---------------------clap_footer-----------)

305

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--437b03529f75---------------------clap_footer-----------)

305

6

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=---footer_actions--437b03529f75---------------------bookmark_footer-----------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--437b03529f75---------------------follow_profile-----------)

[Published in Towards Data Science ---------------------------------](https://towardsdatascience.com/?source=post_page---post_publication_info--437b03529f75--------------------------------)

[761K Followers](https://medium.com/followers?source=post_page---post_publication_info--437b03529f75--------------------------------)

·[Last published 16 hours ago](https://medium.com/core-ai-for-any-rummy-variant-4ff414da1703?source=post_page---post_publication_info--437b03529f75--------------------------------)

Your home for data science. A publication sharing concepts, ideas and codes.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--437b03529f75---------------------follow_profile-----------)

[![Image 7: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:96:96/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=post_page---post_author_info--437b03529f75--------------------------------)

[![Image 8: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:128:128/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=post_page---post_author_info--437b03529f75--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--437b03529f75---------------------follow_profile-----------)

[Written by Saankhya Mondal --------------------------](https://saankhya.medium.com/?source=post_page---post_author_info--437b03529f75--------------------------------)

[525 Followers](https://saankhya.medium.com/followers?source=post_page---post_author_info--437b03529f75--------------------------------)

·[86 Following](https://medium.com/@saankhya/following?source=post_page---post_author_info--437b03529f75--------------------------------)

Data Scientist @ Meesho, M. Tech in AI, IISc, Bengaluru.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--437b03529f75---------------------follow_profile-----------)

More from Saankhya Mondal and Towards Data Science
--------------------------------------------------

![Image 9: Kickstart Your Data Science Journey —  A  Guide for Aspiring Data Scientists](https://miro.medium.com/v2/resize:fit:679/1*o06jXpJ_dMBlIwnR1P7XwQ.png)

[![Image 10: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists --------------------------------------------------------------------------- ### Key Technical Skills You Need to Kick-start Your Career in Data Science](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

3d ago

[300 10](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=author_recirc-----437b03529f75----0---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----437b03529f75----0-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

![Image 11: What Did I Learn from Building LLM Applications in 2024? — Part 1](https://miro.medium.com/v2/resize:fit:679/1*oEXNPL3qOT_XHdJnDUJDcQ.jpeg)

[![Image 12: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[What Did I Learn from Building LLM Applications in 2024? — Part 1 ----------------------------------------------------------------- ### An engineer’s journey to building LLM-native applications](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

5d ago

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----437b03529f75----1---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----437b03529f75----1-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

![Image 13: Preference Alignment for Everyone!](https://miro.medium.com/v2/resize:fit:679/1*cbLNScjpzOf80TRVme0VZA.png)

[![Image 14: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

1d ago

[171 2](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----437b03529f75----2---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2563cec4d10e&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpreference-alignment-for-everyone-2563cec4d10e&source=-----437b03529f75----2-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

![Image 15: Game Theory, Part 1 — The Prisoner’s Dilemma Problem](https://miro.medium.com/v2/resize:fit:679/0*mWNHxZMOZ8NhYPnt)

[![Image 16: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

by

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[Game Theory, Part 1 — The Prisoner’s Dilemma Problem ---------------------------------------------------- ### Game theory is prevalent in real-life scenarios and decision-making](https://medium.com/game-theory-part-1-the-prisoners-dilemma-problem-18b216d3b523?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

Oct 22

[113 2](https://medium.com/game-theory-part-1-the-prisoners-dilemma-problem-18b216d3b523?source=author_recirc-----437b03529f75----3---------------------09a333b9_0892_420e_96cb_74124aff8f19-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F18b216d3b523&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fgame-theory-part-1-the-prisoners-dilemma-problem-18b216d3b523&source=-----437b03529f75----3-----------------bookmark_preview----09a333b9_0892_420e_96cb_74124aff8f19-------)

[See all from Saankhya Mondal](https://saankhya.medium.com/?source=post_page-----437b03529f75--------------------------------)

[See all from Towards Data Science](https://towardsdatascience.com/?source=post_page-----437b03529f75--------------------------------)

Recommended from Medium
-----------------------

![Image 17: Kickstart Your Data Science Journey —  A  Guide for Aspiring Data Scientists](https://miro.medium.com/v2/resize:fit:679/1*o06jXpJ_dMBlIwnR1P7XwQ.png)

[![Image 18: Towards Data Science](https://miro.medium.com/v2/resize:fill:20:20/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Saankhya Mondal](https://saankhya.medium.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists --------------------------------------------------------------------------- ### Key Technical Skills You Need to Kick-start Your Career in Data Science](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

3d ago

[300 10](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----437b03529f75----0-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 19: Hang On, What’s Survival Analysis?](https://miro.medium.com/v2/resize:fit:679/1*syQ_0hAZc6gXTe4eE1mcUw.png)

[![Image 20: Klaviyo Engineering](https://miro.medium.com/v2/resize:fill:20:20/1*j4dmkFrmjReKmnzOhAy3BQ.png)](https://klaviyo.tech/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Klaviyo Engineering](https://klaviyo.tech/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Steven Her](https://medium.com/@steven.her?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Hang On, What’s Survival Analysis? ---------------------------------- ### This was a new area for the two of us, so we decided to write a post to help others in the same spot.](https://klaviyo.tech/hang-on-whats-survival-analysis-d56c2b39a593?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Jun 13

[278](https://klaviyo.tech/hang-on-whats-survival-analysis-d56c2b39a593?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd56c2b39a593&operation=register&redirect=https%3A%2F%2Fklaviyo.tech%2Fhang-on-whats-survival-analysis-d56c2b39a593&source=-----437b03529f75----1-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

Lists
-----

[![Image 21](https://miro.medium.com/v2/resize:fill:48:48/0*r4yjMpEmqzHCUvWC.jpg) ![Image 22](https://miro.medium.com/v2/resize:fill:48:48/1*bv2KUVNLi2sFNjBTdoBmWw.png) ![Image 23](https://miro.medium.com/v2/resize:fill:48:48/0*zsngbTOmFCy6sUCx.jpeg) Predictive Modeling w/ Python ----------------------------- 20 stories·1647 saves](https://medium.com/@ben.putney/list/predictive-modeling-w-python-e3668ea008e1?source=read_next_recirc-----437b03529f75--------------------------------)

[![Image 24: Principal Component Analysis for ML](https://miro.medium.com/v2/resize:fill:48:48/1*swd_PY6vTCyPnsgBYoFZfA.png) ![Image 25: Time Series Analysis](https://miro.medium.com/v2/resize:fill:48:48/1*8sSAHftNwd_RNJ3k4VA0pA.png) ![Image 26: deep learning cheatsheet for beginner](https://miro.medium.com/v2/resize:fill:48:48/1*uNyD4yNMH-DnOel1wzxOOA.png) Practical Guides to Machine Learning ------------------------------------ 10 stories·2007 saves](https://destingong.medium.com/list/practical-guides-to-machine-learning-a877c2a39884?source=read_next_recirc-----437b03529f75--------------------------------)

[![Image 27](https://miro.medium.com/v2/resize:fill:48:48/1*zPtGTCNOwu1p3kzn_sZFVQ.png) ![Image 28](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*kQIvhDkl0ixPpv4z) ![Image 29](https://miro.medium.com/v2/resize:fill:48:48/1*ERYx0IB1pN-5ZX98cKAoUw.png) General Coding Knowledge ------------------------ 20 stories·1712 saves](https://eddiebarth.medium.com/list/general-coding-knowledge-f2d429d4f0cd?source=read_next_recirc-----437b03529f75--------------------------------)

[![Image 30](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*gzCeWxDtGmD23QR5) ![Image 31](https://miro.medium.com/v2/resize:fill:48:48/1*di4WDrnS1F6_p9GWnxvPmg.png) ![Image 32](https://miro.medium.com/v2/resize:fill:48:48/1*PzJLbFrFtNkqPsxielO8zA.jpeg) Coding & Development -------------------- 11 stories·891 saves](https://medium.com/@jscribes/list/coding-development-e360d380bb82?source=read_next_recirc-----437b03529f75--------------------------------)

![Image 33: Causal Inference: an Overview](https://miro.medium.com/v2/resize:fit:679/1*XFK9jlzFyHpg7mpJb_UrNA.png)

[![Image 34: Level Up Coding](https://miro.medium.com/v2/resize:fill:20:20/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Arthur Mello](https://medium.com/@arthurmello_?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Causal Inference: an Overview ----------------------------- ### Find out when correlation actually means causation](https://levelup.gitconnected.com/causal-inference-an-overview-1254f5654b01?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Oct 13

[188 1](https://levelup.gitconnected.com/causal-inference-an-overview-1254f5654b01?source=read_next_recirc-----437b03529f75----0---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1254f5654b01&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fcausal-inference-an-overview-1254f5654b01&source=-----437b03529f75----0-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 35: Python is No More The King of Data Science](https://miro.medium.com/v2/resize:fit:679/1*uiA0nCufUQs-K64ebSUhew.jpeg)

[![Image 36: Stackademic](https://miro.medium.com/v2/resize:fill:20:20/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Oct 23

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----437b03529f75----1---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----437b03529f75----1-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 37: Exploring Causal Decision Theory Approach with Quantile Regression](https://miro.medium.com/v2/resize:fit:679/0*4gnIT2zaaLiDVeph)

[![Image 38: Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://pub.towardsai.net/?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

In

[Towards AI](https://pub.towardsai.net/?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

by

[Shenggang Li](https://medium.com/@datalev?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Exploring Causal Decision Theory Approach with Quantile Regression ------------------------------------------------------------------ ### Using AI and Causal Decision Theory to Prioritize Restocking: Balancing Demand, Inventory Risk, and Product Importance](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

5d ago

[157 2](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----437b03529f75----2---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa301f6028c73&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fexploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73&source=-----437b03529f75----2-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

![Image 39: Using Autoencoders to Reduce Embedding Dimensions with Matryoshka Representation Learning](https://miro.medium.com/v2/resize:fit:679/1*yuVzMhCJyDENbyhwAsrkwA.png)

[![Image 40: AI SageScribe](https://miro.medium.com/v2/resize:fill:20:20/1*ozpm5as9nAOk1kAoi6xvkA.jpeg)](https://medium.com/@aisagescribe?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[AI SageScribe](https://medium.com/@aisagescribe?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[Using Autoencoders to Reduce Embedding Dimensions with Matryoshka Representation Learning ----------------------------------------------------------------------------------------- ### In the ever-evolving field of machine learning and artificial intelligence, managing high-dimensional data efficiently is a persistent…](https://medium.com/@aisagescribe/using-autoencoders-to-reduce-embedding-dimensions-with-matryoshka-representation-learning-9f48ef269b18?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

Oct 14

[8](https://medium.com/@aisagescribe/using-autoencoders-to-reduce-embedding-dimensions-with-matryoshka-representation-learning-9f48ef269b18?source=read_next_recirc-----437b03529f75----3---------------------04514852_6477_4af4_94e5_2b4168863ddd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9f48ef269b18&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aisagescribe%2Fusing-autoencoders-to-reduce-embedding-dimensions-with-matryoshka-representation-learning-9f48ef269b18&source=-----437b03529f75----3-----------------bookmark_preview----04514852_6477_4af4_94e5_2b4168863ddd-------)

[See more recommendations](https://medium.com/?source=post_page-----437b03529f75--------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----437b03529f75--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----437b03529f75--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----437b03529f75--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----437b03529f75--------------------------------)

[Press](https://medium.com/towards-data-science/pressinquiries@medium.com?source=post_page-----437b03529f75--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----437b03529f75--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----437b03529f75--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----437b03529f75--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----437b03529f75--------------------------------)

[Teams](https://medium.com/business?source=post_page-----437b03529f75--------------------------------)


---

## Towards Data Science

Source: https://medium.com/towards-data-science/to-index-or-not-to-index-8be32ad45cae
Date fetched: 2024-11-10T01:46:01.687769

---

Title: To Index or Not to Index - Towards Data Science

URL Source: https://medium.com/towards-data-science/to-index-or-not-to-index-8be32ad45cae

Published Time: 2024-11-08T01:41:43.286Z

Markdown Content:
To Index or Not to Index. Leverage SQL indexing to speed up your… | by Christopher Karg | Nov, 2024 | Towards Data Science
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

To Index or Not to Index
========================

Leverage SQL indexing to speed up your queries. Learn when to index, when not to, and how indexing works under the hood.
------------------------------------------------------------------------------------------------------------------------

[![Image 2: Christopher Karg](https://miro.medium.com/v2/resize:fill:88:88/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=post_page---byline--8be32ad45cae--------------------------------)

[Christopher Karg](https://medium.com/@christopher_karg?source=post_page---byline--8be32ad45cae--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5fbda6d16c39&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=post_page-5fbda6d16c39--byline--8be32ad45cae---------------------post_header-----------)

2 days ago

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=---header_actions--8be32ad45cae---------------------clap_footer-----------)

181

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=---header_actions--8be32ad45cae---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=---header_actions--8be32ad45cae---------------------post_audio_button-----------)

![Image 4: a field with a frosty morning](https://miro.medium.com/v2/resize:fit:700/1*r_TJZMdbJdCdhCY_yONmGQ.jpeg)

source: [https://www.pexels.com/photo/serene-autumn-morning-landscape-in-misty-meadow-29231560/](https://www.pexels.com/photo/serene-autumn-morning-landscape-in-misty-meadow-29231560/)

SQL indexing is a term often thrown around in data circles — you may have heard phrases like “just apply an index”. It is also a question often asked in interviews — “what steps can take to improve query times on table X?”. It is something that is syntactically easy to implement but I have found not much attention is paid to what actually happens under the hood. In this article I aim to do just that by using a relational MySQL Database (DB). I will cover what an index is, how to implement it, how it works under the hood, along with some considerations of when not to use indexes. As with many technologies, even SQL indexes have their trade-offs.

In my examples I use a simple MySQL container from Docker. I do not cover how this works but feel free to reach out if you have any questions. I will show the code I use to populate the DB in this article for you to adapt for your own use case and experiment yourself.

I start off with a high-level overview. The more granular detail is later on in the article. As such, I hope I can provide valuable insights to a wide readership of varying technical inclinations. If you’re like me you’ll find the visualisations in…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae%3Fsource%3D-----8be32ad45cae---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----8be32ad45cae---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae%3Fsource%3D-----8be32ad45cae---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----8be32ad45cae---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae%3Fsource%3D-----8be32ad45cae---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----8be32ad45cae---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=-----8be32ad45cae---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=---footer_actions--8be32ad45cae---------------------clap_footer-----------)

181

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=---footer_actions--8be32ad45cae---------------------clap_footer-----------)

181

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=---footer_actions--8be32ad45cae---------------------bookmark_footer-----------)

[![Image 5: Christopher Karg](https://miro.medium.com/v2/resize:fill:144:144/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=post_page---post_author_info--8be32ad45cae--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5fbda6d16c39&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=post_page-5fbda6d16c39--post_author_info--8be32ad45cae---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fe862d75fcc20&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&newsletterV3=5fbda6d16c39&newsletterV3Id=e862d75fcc20&user=Christopher+Karg&userId=5fbda6d16c39&source=---post_author_info--8be32ad45cae---------------------subscribe_user-----------)

[Written by Christopher Karg ---------------------------](https://medium.com/@christopher_karg?source=post_page---post_author_info--8be32ad45cae--------------------------------)

·Writer for

Data | Cybersecurity | Career

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5fbda6d16c39&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=post_page-5fbda6d16c39--post_author_info--8be32ad45cae---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fe862d75fcc20&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&newsletterV3=5fbda6d16c39&newsletterV3Id=e862d75fcc20&user=Christopher+Karg&userId=5fbda6d16c39&source=---post_author_info--8be32ad45cae---------------------subscribe_user-----------)

![Image 7: Run LLM inference using Apple Hardware](https://miro.medium.com/v2/resize:fit:679/1*-WLPm5NrQ03RDIaoJo22hw.jpeg)

[![Image 8: Christopher Karg](https://miro.medium.com/v2/resize:fill:20:20/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Christopher Karg](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Run LLM inference using Apple Hardware -------------------------------------- ### Unlock Apple GPU Power for LLM Inference with MLX](https://medium.com/run-llm-inference-using-apple-hardware-00a4a5d455b7?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

Jan 30

[251](https://medium.com/run-llm-inference-using-apple-hardware-00a4a5d455b7?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F00a4a5d455b7&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Frun-llm-inference-using-apple-hardware-00a4a5d455b7&source=-----8be32ad45cae----0-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----8be32ad45cae----1-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[171 2](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2563cec4d10e&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpreference-alignment-for-everyone-2563cec4d10e&source=-----8be32ad45cae----2-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

![Image 13: How to efficiently fine-tune your own open-source LLM using novel techniques — code provided](https://miro.medium.com/v2/resize:fit:679/1*gySZCCVBWTArCt6rUfZWEA.jpeg)

[![Image 14: Christopher Karg](https://miro.medium.com/v2/resize:fill:20:20/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Christopher Karg](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[How to efficiently fine-tune your own open-source LLM using novel techniques — code provided -------------------------------------------------------------------------------------------- ### In this article I tune a base LLama2 LLM to output SQL code. I use Parameter Efficient Fine-Tuning Techniques to optimise the process.](https://medium.com/how-to-efficiently-fine-tune-your-own-open-source-llm-using-novel-techniques-code-provided-03a4e67d1b48?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

Dec 15, 2023

[405 2](https://medium.com/how-to-efficiently-fine-tune-your-own-open-source-llm-using-novel-techniques-code-provided-03a4e67d1b48?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F03a4e67d1b48&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-efficiently-fine-tune-your-own-open-source-llm-using-novel-techniques-code-provided-03a4e67d1b48&source=-----8be32ad45cae----3-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[See all from Christopher Karg](https://medium.com/@christopher_karg?source=post_page-----8be32ad45cae--------------------------------)

![Image 15: 12 Production-Grade Python Code Styles I’ve Picked Up From Work](https://miro.medium.com/v2/resize:fit:679/1*5llI8jewhOwDTGzh_r5ObQ.png)

[![Image 16: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[12 Production-Grade Python Code Styles I’ve Picked Up From Work --------------------------------------------------------------- ### Read Free…](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

Nov 2

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----8be32ad45cae----0-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 17: A figure showing x and y values in a 2 dimensional space, with blue dots representing the data points, and a red straight line crossing the points, capturing the linear relationship of x and y values](https://miro.medium.com/v2/resize:fit:679/1*MXP0q7fM2KiJQcjJhbTLyw.png)

[![Image 18: Elisa Yao](https://miro.medium.com/v2/resize:fill:20:20/1*IS2tUmtvNtk3E-IPXJA0lw.jpeg)](https://medium.com/@yqelisa?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Elisa Yao](https://medium.com/@yqelisa?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Predict Housing Price using Linear Regression in Python ------------------------------------------------------- ### A walk-through of cost computation, gradient descent, and regularization using Boston Housing dataset](https://medium.com/predict-housing-price-using-linear-regression-in-python-bfc0fcfff640?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[194 2](https://medium.com/predict-housing-price-using-linear-regression-in-python-bfc0fcfff640?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbfc0fcfff640&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpredict-housing-price-using-linear-regression-in-python-bfc0fcfff640&source=-----8be32ad45cae----1-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 31: 8 Uncommon but Extremely Useful Python Libraries for 2025](https://miro.medium.com/v2/resize:fit:679/0*9Ul-pCYCWMLJ9huk)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Python in Plain English](https://python.plainenglish.io/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[8 Uncommon but Extremely Useful Python Libraries for 2025 --------------------------------------------------------- ### You’ll regret not knowing this earlier](https://python.plainenglish.io/8-uncommon-but-extremely-useful-python-libraries-for-2025-0d5752acf9fa?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[249 2](https://python.plainenglish.io/8-uncommon-but-extremely-useful-python-libraries-for-2025-0d5752acf9fa?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F0d5752acf9fa&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F8-uncommon-but-extremely-useful-python-libraries-for-2025-0d5752acf9fa&source=-----8be32ad45cae----0-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 33: How I Am Using a Lifetime 100% Free Server](https://miro.medium.com/v2/resize:fit:679/1*BqVsCBa2mLv1UWQrdhjX5w.png)

[![Image 34: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[How I Am Using a Lifetime 100% Free Server ------------------------------------------ ### Get a server with 24 GB RAM + 4 CPU + 200 GB Storage + Always Free](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----8be32ad45cae----1-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 35: I used OpenAI’s o1 model to develop a trading strategy. It is DESTROYING the market](https://miro.medium.com/v2/resize:fit:679/1*MuD60qiJYZ1GJSSraELZpg.png)

[![Image 36: Austin Starks](https://miro.medium.com/v2/resize:fill:20:20/1*dfww62lW8x8sVZNbLx5aCA.jpeg)](https://medium.com/@austin-starks?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Austin Starks](https://medium.com/@austin-starks?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[DataDrivenInvestor](https://medium.datadriveninvestor.com/?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[I used OpenAI’s o1 model to develop a trading strategy. It is DESTROYING the market ----------------------------------------------------------------------------------- ### It literally took one try. I was shocked.](https://medium.datadriveninvestor.com/i-used-openais-o1-model-to-develop-a-trading-strategy-it-is-destroying-the-market-576a6039e8fa?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

Sep 15

[5.7K 144](https://medium.datadriveninvestor.com/i-used-openais-o1-model-to-develop-a-trading-strategy-it-is-destroying-the-market-576a6039e8fa?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F576a6039e8fa&operation=register&redirect=https%3A%2F%2Fmedium.datadriveninvestor.com%2Fi-used-openais-o1-model-to-develop-a-trading-strategy-it-is-destroying-the-market-576a6039e8fa&source=-----8be32ad45cae----2-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 37: How Hard is the Math Problem in Good Will Hunting?](https://miro.medium.com/v2/resize:fit:679/1*VlYbb3Mxmy_uTXsusPabew.png)

[![Image 38: Cole Frederick](https://miro.medium.com/v2/resize:fill:20:20/1*KMtMs-6WXNWqWvrCIYdfJw.png)](https://colefp.medium.com/?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Cole Frederick](https://colefp.medium.com/?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Science Spectrum](https://medium.com/science-spectrum?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[How Hard is the Math Problem in Good Will Hunting? -------------------------------------------------- ### This excellent film also has some fun math to go with it!](https://medium.com/science-spectrum/how-hard-is-the-math-problem-in-good-will-hunting-76e4cb00b6f9?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[660 9](https://medium.com/science-spectrum/how-hard-is-the-math-problem-in-good-will-hunting-76e4cb00b6f9?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F76e4cb00b6f9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fscience-spectrum%2Fhow-hard-is-the-math-problem-in-good-will-hunting-76e4cb00b6f9&source=-----8be32ad45cae----3-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

## Visual Content Analysis

### Image Analysis
Title: To Index or Not to Index - Towards Data Science

URL Source: https://medium.com/towards-data-science/to-index-or-not-to-index-8be32ad45cae

Published Time: 2024-11-08T01:41:43.286Z

Markdown Content:
To Index or Not to Index. Leverage SQL indexing to speed up your… | by Christopher Karg | Nov, 2024 | Towards Data Science
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

To Index or Not to Index
========================

Leverage SQL indexing to speed up your queries. Learn when to index, when not to, and how indexing works under the hood.
------------------------------------------------------------------------------------------------------------------------

[![Image 2: Christopher Karg](https://miro.medium.com/v2/resize:fill:88:88/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=post_page---byline--8be32ad45cae--------------------------------)

[Christopher Karg](https://medium.com/@christopher_karg?source=post_page---byline--8be32ad45cae--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5fbda6d16c39&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=post_page-5fbda6d16c39--byline--8be32ad45cae---------------------post_header-----------)

2 days ago

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=---header_actions--8be32ad45cae---------------------clap_footer-----------)

181

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=---header_actions--8be32ad45cae---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=---header_actions--8be32ad45cae---------------------post_audio_button-----------)

![Image 4: a field with a frosty morning](https://miro.medium.com/v2/resize:fit:700/1*r_TJZMdbJdCdhCY_yONmGQ.jpeg)

source: [https://www.pexels.com/photo/serene-autumn-morning-landscape-in-misty-meadow-29231560/](https://www.pexels.com/photo/serene-autumn-morning-landscape-in-misty-meadow-29231560/)

SQL indexing is a term often thrown around in data circles — you may have heard phrases like “just apply an index”. It is also a question often asked in interviews — “what steps can take to improve query times on table X?”. It is something that is syntactically easy to implement but I have found not much attention is paid to what actually happens under the hood. In this article I aim to do just that by using a relational MySQL Database (DB). I will cover what an index is, how to implement it, how it works under the hood, along with some considerations of when not to use indexes. As with many technologies, even SQL indexes have their trade-offs.

In my examples I use a simple MySQL container from Docker. I do not cover how this works but feel free to reach out if you have any questions. I will show the code I use to populate the DB in this article for you to adapt for your own use case and experiment yourself.

I start off with a high-level overview. The more granular detail is later on in the article. As such, I hope I can provide valuable insights to a wide readership of varying technical inclinations. If you’re like me you’ll find the visualisations in…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae%3Fsource%3D-----8be32ad45cae---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----8be32ad45cae---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae%3Fsource%3D-----8be32ad45cae---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----8be32ad45cae---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae%3Fsource%3D-----8be32ad45cae---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----8be32ad45cae---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=-----8be32ad45cae---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=---footer_actions--8be32ad45cae---------------------clap_footer-----------)

181

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=---footer_actions--8be32ad45cae---------------------clap_footer-----------)

181

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8be32ad45cae&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&source=---footer_actions--8be32ad45cae---------------------bookmark_footer-----------)

[![Image 5: Christopher Karg](https://miro.medium.com/v2/resize:fill:144:144/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=post_page---post_author_info--8be32ad45cae--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5fbda6d16c39&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=post_page-5fbda6d16c39--post_author_info--8be32ad45cae---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fe862d75fcc20&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&newsletterV3=5fbda6d16c39&newsletterV3Id=e862d75fcc20&user=Christopher+Karg&userId=5fbda6d16c39&source=---post_author_info--8be32ad45cae---------------------subscribe_user-----------)

[Written by Christopher Karg ---------------------------](https://medium.com/@christopher_karg?source=post_page---post_author_info--8be32ad45cae--------------------------------)

·Writer for

Data | Cybersecurity | Career

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5fbda6d16c39&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&user=Christopher+Karg&userId=5fbda6d16c39&source=post_page-5fbda6d16c39--post_author_info--8be32ad45cae---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fe862d75fcc20&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fto-index-or-not-to-index-8be32ad45cae&newsletterV3=5fbda6d16c39&newsletterV3Id=e862d75fcc20&user=Christopher+Karg&userId=5fbda6d16c39&source=---post_author_info--8be32ad45cae---------------------subscribe_user-----------)

![Image 7: Run LLM inference using Apple Hardware](https://miro.medium.com/v2/resize:fit:679/1*-WLPm5NrQ03RDIaoJo22hw.jpeg)

[![Image 8: Christopher Karg](https://miro.medium.com/v2/resize:fill:20:20/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Christopher Karg](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Run LLM inference using Apple Hardware -------------------------------------- ### Unlock Apple GPU Power for LLM Inference with MLX](https://medium.com/run-llm-inference-using-apple-hardware-00a4a5d455b7?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

Jan 30

[251](https://medium.com/run-llm-inference-using-apple-hardware-00a4a5d455b7?source=author_recirc-----8be32ad45cae----0---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F00a4a5d455b7&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Frun-llm-inference-using-apple-hardware-00a4a5d455b7&source=-----8be32ad45cae----0-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----8be32ad45cae----1---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----8be32ad45cae----1-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[171 2](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----8be32ad45cae----2---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2563cec4d10e&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpreference-alignment-for-everyone-2563cec4d10e&source=-----8be32ad45cae----2-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

![Image 13: How to efficiently fine-tune your own open-source LLM using novel techniques — code provided](https://miro.medium.com/v2/resize:fit:679/1*gySZCCVBWTArCt6rUfZWEA.jpeg)

[![Image 14: Christopher Karg](https://miro.medium.com/v2/resize:fill:20:20/1*IOKAD707flZwbmv1mQYnCw.jpeg)](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[Christopher Karg](https://medium.com/@christopher_karg?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[How to efficiently fine-tune your own open-source LLM using novel techniques — code provided -------------------------------------------------------------------------------------------- ### In this article I tune a base LLama2 LLM to output SQL code. I use Parameter Efficient Fine-Tuning Techniques to optimise the process.](https://medium.com/how-to-efficiently-fine-tune-your-own-open-source-llm-using-novel-techniques-code-provided-03a4e67d1b48?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

Dec 15, 2023

[405 2](https://medium.com/how-to-efficiently-fine-tune-your-own-open-source-llm-using-novel-techniques-code-provided-03a4e67d1b48?source=author_recirc-----8be32ad45cae----3---------------------78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F03a4e67d1b48&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-efficiently-fine-tune-your-own-open-source-llm-using-novel-techniques-code-provided-03a4e67d1b48&source=-----8be32ad45cae----3-----------------bookmark_preview----78c31fe2_d1f3_42cc_b479_b809a1a0cf12-------)

[See all from Christopher Karg](https://medium.com/@christopher_karg?source=post_page-----8be32ad45cae--------------------------------)

![Image 15: 12 Production-Grade Python Code Styles I’ve Picked Up From Work](https://miro.medium.com/v2/resize:fit:679/1*5llI8jewhOwDTGzh_r5ObQ.png)

[![Image 16: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[12 Production-Grade Python Code Styles I’ve Picked Up From Work --------------------------------------------------------------- ### Read Free…](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

Nov 2

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----8be32ad45cae----0-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 17: A figure showing x and y values in a 2 dimensional space, with blue dots representing the data points, and a red straight line crossing the points, capturing the linear relationship of x and y values](https://miro.medium.com/v2/resize:fit:679/1*MXP0q7fM2KiJQcjJhbTLyw.png)

[![Image 18: Elisa Yao](https://miro.medium.com/v2/resize:fill:20:20/1*IS2tUmtvNtk3E-IPXJA0lw.jpeg)](https://medium.com/@yqelisa?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Elisa Yao](https://medium.com/@yqelisa?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Predict Housing Price using Linear Regression in Python ------------------------------------------------------- ### A walk-through of cost computation, gradient descent, and regularization using Boston Housing dataset](https://medium.com/predict-housing-price-using-linear-regression-in-python-bfc0fcfff640?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[194 2](https://medium.com/predict-housing-price-using-linear-regression-in-python-bfc0fcfff640?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbfc0fcfff640&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpredict-housing-price-using-linear-regression-in-python-bfc0fcfff640&source=-----8be32ad45cae----1-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 31: 8 Uncommon but Extremely Useful Python Libraries for 2025](https://miro.medium.com/v2/resize:fit:679/0*9Ul-pCYCWMLJ9huk)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Python in Plain English](https://python.plainenglish.io/?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[8 Uncommon but Extremely Useful Python Libraries for 2025 --------------------------------------------------------- ### You’ll regret not knowing this earlier](https://python.plainenglish.io/8-uncommon-but-extremely-useful-python-libraries-for-2025-0d5752acf9fa?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[249 2](https://python.plainenglish.io/8-uncommon-but-extremely-useful-python-libraries-for-2025-0d5752acf9fa?source=read_next_recirc-----8be32ad45cae----0---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F0d5752acf9fa&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F8-uncommon-but-extremely-useful-python-libraries-for-2025-0d5752acf9fa&source=-----8be32ad45cae----0-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 33: How I Am Using a Lifetime 100% Free Server](https://miro.medium.com/v2/resize:fit:679/1*BqVsCBa2mLv1UWQrdhjX5w.png)

[![Image 34: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[How I Am Using a Lifetime 100% Free Server ------------------------------------------ ### Get a server with 24 GB RAM + 4 CPU + 200 GB Storage + Always Free](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----8be32ad45cae----1---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----8be32ad45cae----1-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 35: I used OpenAI’s o1 model to develop a trading strategy. It is DESTROYING the market](https://miro.medium.com/v2/resize:fit:679/1*MuD60qiJYZ1GJSSraELZpg.png)

[![Image 36: Austin Starks](https://miro.medium.com/v2/resize:fill:20:20/1*dfww62lW8x8sVZNbLx5aCA.jpeg)](https://medium.com/@austin-starks?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Austin Starks](https://medium.com/@austin-starks?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[DataDrivenInvestor](https://medium.datadriveninvestor.com/?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[I used OpenAI’s o1 model to develop a trading strategy. It is DESTROYING the market ----------------------------------------------------------------------------------- ### It literally took one try. I was shocked.](https://medium.datadriveninvestor.com/i-used-openais-o1-model-to-develop-a-trading-strategy-it-is-destroying-the-market-576a6039e8fa?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

Sep 15

[5.7K 144](https://medium.datadriveninvestor.com/i-used-openais-o1-model-to-develop-a-trading-strategy-it-is-destroying-the-market-576a6039e8fa?source=read_next_recirc-----8be32ad45cae----2---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F576a6039e8fa&operation=register&redirect=https%3A%2F%2Fmedium.datadriveninvestor.com%2Fi-used-openais-o1-model-to-develop-a-trading-strategy-it-is-destroying-the-market-576a6039e8fa&source=-----8be32ad45cae----2-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

![Image 37: How Hard is the Math Problem in Good Will Hunting?](https://miro.medium.com/v2/resize:fit:679/1*VlYbb3Mxmy_uTXsusPabew.png)

[![Image 38: Cole Frederick](https://miro.medium.com/v2/resize:fill:20:20/1*KMtMs-6WXNWqWvrCIYdfJw.png)](https://colefp.medium.com/?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[Cole Frederick](https://colefp.medium.com/?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

in

[Science Spectrum](https://medium.com/science-spectrum?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[How Hard is the Math Problem in Good Will Hunting? -------------------------------------------------- ### This excellent film also has some fun math to go with it!](https://medium.com/science-spectrum/how-hard-is-the-math-problem-in-good-will-hunting-76e4cb00b6f9?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[660 9](https://medium.com/science-spectrum/how-hard-is-the-math-problem-in-good-will-hunting-76e4cb00b6f9?source=read_next_recirc-----8be32ad45cae----3---------------------24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F76e4cb00b6f9&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fscience-spectrum%2Fhow-hard-is-the-math-problem-in-good-will-hunting-76e4cb00b6f9&source=-----8be32ad45cae----3-----------------bookmark_preview----24961f96_291f_4ad9_b17f_bd3cf50ddba1-------)


---



# Bundle: finance_articles

# Finance Articles Collection

## Table of Contents

### General
- [Stackademic](#stackademic)
- [Stackademic](#stackademic)
- [Python In Plain English](#python-in-plain-english)

---

# General

## Stackademic

Source: https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3
Date fetched: 2024-11-10T01:46:36.364574

---

Title: Python is No More The King of Data Science - Stackademic

URL Source: https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3

Published Time: 2024-10-23T03:28:34.197Z

Markdown Content:
Python is No More The King of Data Science | by Abdur Rahman | Oct, 2024 | Stackademic
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Python is No More The King of Data Science
==========================================

5 Reasons Why Python is Losing Its Crown
----------------------------------------

[![Image 2: Abdur Rahman](https://miro.medium.com/v2/resize:fill:88:88/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=post_page---byline--476f1e3191b3--------------------------------)

[![Image 3: Stackademic](https://miro.medium.com/v2/resize:fill:48:48/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=post_page---byline--476f1e3191b3--------------------------------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=post_page---byline--476f1e3191b3--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--byline--476f1e3191b3---------------------post_header-----------)

[Stackademic](https://blog.stackademic.com/?source=post_page---byline--476f1e3191b3--------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstackademic%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=---header_actions--476f1e3191b3---------------------clap_footer-----------)

4.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=---header_actions--476f1e3191b3---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=---header_actions--476f1e3191b3---------------------post_audio_button-----------)

![Image 4: a cartoon of a king sitting on a throne](https://miro.medium.com/v2/resize:fit:700/1*uiA0nCufUQs-K64ebSUhew.jpeg)

AI Generated using Ideogram 2.0

Non-member? Read it [_here_](https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3?sk=1ade22551310fc165a94c8af6c8093d5) for free

If you are reading this, then there is a high chance that Python is your go-to language when anyone talks about data science, and honestly, no one can argue with that. Python has remained the king of the Data Science Kingdom because of its excellent libraries, such as `Numpy`, `Pandas` and `scikit-learn`.

But if something has always been on top, that does not mean that it is safe up there forever. You hear whispers; you see the rise of new languages — maybe you’re wondering,

> Is Python’s time running out?

Okay, before you throw your Jupyter notebook on my face, let me make something very clear: I do think Python is the GOAT. I don’t deny that. Yet, it doesn’t come without flaws either. It might not lose its place in one night, but there are cracks forming.

> **Edit:** Hey everyone, this article reflects my **personal opinion**, and I fully respect that others may disagree. Healthy debate is welcome — after all, different perspectives are what drive progress!

Alright, so let’s see 5 reasons that suggest Python isn’t going to stay on top forever!

1\. Performance Bottlenecks: Python’s…
--------------------------------------

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3%3Fsource%3D-----476f1e3191b3---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----476f1e3191b3---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3%3Fsource%3D-----476f1e3191b3---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----476f1e3191b3---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3%3Fsource%3D-----476f1e3191b3---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----476f1e3191b3---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----476f1e3191b3---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstackademic%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--476f1e3191b3---------------------clap_footer-----------)

4.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstackademic%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--476f1e3191b3---------------------clap_footer-----------)

4.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=---footer_actions--476f1e3191b3---------------------bookmark_footer-----------)

[![Image 5: Abdur Rahman](https://miro.medium.com/v2/resize:fill:144:144/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=post_page---post_author_info--476f1e3191b3--------------------------------)

[![Image 6: Stackademic](https://miro.medium.com/v2/resize:fill:64:64/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=post_page---post_author_info--476f1e3191b3--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--476f1e3191b3---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--476f1e3191b3---------------------subscribe_user-----------)

[Stackademic](https://blog.stackademic.com/?source=post_page---post_author_info--476f1e3191b3--------------------------------)

𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐚𝐧𝐝 𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐊𝐧𝐨𝐰𝐥𝐞𝐝𝐠𝐞 𝐄𝐯𝐞𝐫𝐲𝐝𝐚𝐲 | 𝐏𝐲𝐭𝐡𝐨𝐧 𝐢𝐬 ❤️ | 𝐌𝐮𝐬𝐥𝐢𝐦 | #𝐢𝐬𝐭𝐚𝐧𝐝𝐰𝐢𝐭𝐡𝐩𝐚𝐥𝐞𝐬𝐭𝐢𝐧𝐞🍉

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--476f1e3191b3---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--476f1e3191b3---------------------subscribe_user-----------)

More from Abdur Rahman and Stackademic
--------------------------------------

![Image 7: 20 Python Scripts To Automate Your Daily Tasks](https://miro.medium.com/v2/resize:fit:679/1*iGrbJxU6oV3q7LeNV28gWg.jpeg)

[![Image 8: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[20 Python Scripts To Automate Your Daily Tasks ---------------------------------------------- ### A must-have collection for every developer](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

Oct 7

[2.3K 22](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----476f1e3191b3----0-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

![Image 9: 20 Git Command-Line Tricks Every Developer Should Know](https://miro.medium.com/v2/resize:fit:679/1*lyEwUyQSkpm0rb4yvn80qA.png)

[![Image 10: Crafting-Code](https://miro.medium.com/v2/resize:fill:20:20/1*CyROwr3ZEi4KqVBfjqHHeg.png)](https://medium.com/@craftingcode?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Crafting-Code](https://medium.com/@craftingcode?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[20 Git Command-Line Tricks Every Developer Should Know ------------------------------------------------------ ### Git Smarter, Code Faster](https://medium.com/20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

Oct 9

[1.4K 20](https://medium.com/20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbf817e83d6b9&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9&source=-----476f1e3191b3----1-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

![Image 11: Title Image](https://miro.medium.com/v2/resize:fit:679/0*02Rxo8X6uaLmkCX3.png)

[![Image 12: Madza](https://miro.medium.com/v2/resize:fill:20:20/1*SCx6IqmQJAzddxnBTcXlFg.png)](https://madzadev.medium.com/?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Madza](https://madzadev.medium.com/?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[16 Open-Source Projects to Improve Your Developer Workflow 👨‍💻🔥 ------------------------------------------------------------------](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[783 9](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffdd3b8c16e57&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57&source=-----476f1e3191b3----2-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

![Image 13: 10 AI-Powered Python Libraries to Boost Your Next Project](https://miro.medium.com/v2/resize:fit:679/1*isqWuyZYRx2-sbFIuLwUJg.jpeg)

[![Image 14: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[10 AI-Powered Python Libraries to Boost Your Next Project --------------------------------------------------------- ### From “Eh, pretty cool” to “Wow, how’d you do that?!”](https://python.plainenglish.io/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[1K 3](https://python.plainenglish.io/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fac74d614e3b8&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8&source=-----476f1e3191b3----3-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[See all from Abdur Rahman](https://medium.com/@abdur-rahman?source=post_page-----476f1e3191b3--------------------------------)

[See all from Stackademic](https://blog.stackademic.com/?source=post_page-----476f1e3191b3--------------------------------)

[![Image 16: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----476f1e3191b3----0-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

![Image 17: Can you solve this famous interview question?](https://miro.medium.com/v2/resize:fit:679/1*ojvznevS00pnY77w0jnxPg.jpeg)

[![Image 18: Paolo Molignini, PhD](https://miro.medium.com/v2/resize:fill:20:20/1*G00MhBr4w2Ja-mXFgZ6g1Q.jpeg)](https://medium.com/@moligninip?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Paolo Molignini, PhD](https://medium.com/@moligninip?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Puzzle Sphere](https://medium.com/puzzle-sphere?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Can you solve this famous interview question? --------------------------------------------- ### 100 passengers, 100 seats — but the first one sits randomly! What’s the chance the last passenger ends up in their own seat? Find out here!](https://medium.com/puzzle-sphere/can-you-solve-this-famous-interview-question-91d0db846935?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

Oct 5

[2.1K 57](https://medium.com/puzzle-sphere/can-you-solve-this-famous-interview-question-91d0db846935?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F91d0db846935&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fpuzzle-sphere%2Fcan-you-solve-this-famous-interview-question-91d0db846935&source=-----476f1e3191b3----1-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[![Image 28](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*UeZPcm_AcNpatRN4) ![Image 29](https://miro.medium.com/v2/resize:fill:48:48/1*sg3I6-CAKFnt7HZQQqFNJw.png) ![Image 30](https://miro.medium.com/v2/resize:fill:48:48/1*Rt9RS9ES0tDnXZ-8t5ZOyA.png) Natural Language Processing --------------------------- 1801 stories·1412 saves](https://medium.com/@AMGAS14/list/natural-language-processing-0a856388a93a?source=read_next_recirc-----476f1e3191b3--------------------------------)

![Image 31: 20 Python Scripts To Automate Your Daily Tasks](https://miro.medium.com/v2/resize:fit:679/1*iGrbJxU6oV3q7LeNV28gWg.jpeg)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[20 Python Scripts To Automate Your Daily Tasks ---------------------------------------------- ### A must-have collection for every developer](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

Oct 7

[2.3K 22](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----476f1e3191b3----0-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

![Image 33: How Old Is Your Body? Stand On One Leg and Find Out](https://miro.medium.com/v2/resize:fit:679/1*GZmK6Wv4dD6dqpzf8Ydzsg.jpeg)

[![Image 34: F. Perry Wilson, MD MSCE](https://miro.medium.com/v2/resize:fill:20:20/1*7hsQz8sWZ4sNZCOfTIBvhQ.jpeg)](https://fperrywilson.medium.com/?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[F. Perry Wilson, MD MSCE](https://fperrywilson.medium.com/?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[How Old Is Your Body? Stand On One Leg and Find Out --------------------------------------------------- ### According to new research, the time you can stand on one leg is the best marker of physical aging.](https://fperrywilson.medium.com/how-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[10.6K 221](https://fperrywilson.medium.com/how-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffcf8241107da&operation=register&redirect=https%3A%2F%2Ffperrywilson.medium.com%2Fhow-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da&source=-----476f1e3191b3----1-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

![Image 35: A MacBook](https://miro.medium.com/v2/resize:fit:679/0*ibammcgaL-gMehSK)

[![Image 36: Andrew Zuo](https://miro.medium.com/v2/resize:fill:20:20/1*FZEG_DxaZ4g-w10VST7WGg.jpeg)](https://andrewzuo.com/?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Andrew Zuo](https://andrewzuo.com/?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Mac O’Clock](https://medium.com/macoclock?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[The M4 MacBook Pro Makes Me Want To Buy A Windows Laptop --------------------------------------------------------](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[918 70](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8f81e91c7622&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmacoclock%2Fthe-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622&source=-----476f1e3191b3----2-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[![Image 38: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----476f1e3191b3----3-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

## Visual Content Analysis

### Image Analysis
Title: Python is No More The King of Data Science - Stackademic

URL Source: https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3

Published Time: 2024-10-23T03:28:34.197Z

Markdown Content:
Python is No More The King of Data Science | by Abdur Rahman | Oct, 2024 | Stackademic
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Python is No More The King of Data Science
==========================================

5 Reasons Why Python is Losing Its Crown
----------------------------------------

[![Image 2: Abdur Rahman](https://miro.medium.com/v2/resize:fill:88:88/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=post_page---byline--476f1e3191b3--------------------------------)

[![Image 3: Stackademic](https://miro.medium.com/v2/resize:fill:48:48/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=post_page---byline--476f1e3191b3--------------------------------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=post_page---byline--476f1e3191b3--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--byline--476f1e3191b3---------------------post_header-----------)

[Stackademic](https://blog.stackademic.com/?source=post_page---byline--476f1e3191b3--------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstackademic%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=---header_actions--476f1e3191b3---------------------clap_footer-----------)

4.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=---header_actions--476f1e3191b3---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=---header_actions--476f1e3191b3---------------------post_audio_button-----------)

![Image 4: a cartoon of a king sitting on a throne](https://miro.medium.com/v2/resize:fit:700/1*uiA0nCufUQs-K64ebSUhew.jpeg)

AI Generated using Ideogram 2.0

Non-member? Read it [_here_](https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3?sk=1ade22551310fc165a94c8af6c8093d5) for free

If you are reading this, then there is a high chance that Python is your go-to language when anyone talks about data science, and honestly, no one can argue with that. Python has remained the king of the Data Science Kingdom because of its excellent libraries, such as `Numpy`, `Pandas` and `scikit-learn`.

But if something has always been on top, that does not mean that it is safe up there forever. You hear whispers; you see the rise of new languages — maybe you’re wondering,

> Is Python’s time running out?

Okay, before you throw your Jupyter notebook on my face, let me make something very clear: I do think Python is the GOAT. I don’t deny that. Yet, it doesn’t come without flaws either. It might not lose its place in one night, but there are cracks forming.

> **Edit:** Hey everyone, this article reflects my **personal opinion**, and I fully respect that others may disagree. Healthy debate is welcome — after all, different perspectives are what drive progress!

Alright, so let’s see 5 reasons that suggest Python isn’t going to stay on top forever!

1\. Performance Bottlenecks: Python’s…
--------------------------------------

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3%3Fsource%3D-----476f1e3191b3---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----476f1e3191b3---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3%3Fsource%3D-----476f1e3191b3---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----476f1e3191b3---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3%3Fsource%3D-----476f1e3191b3---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----476f1e3191b3---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----476f1e3191b3---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstackademic%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--476f1e3191b3---------------------clap_footer-----------)

4.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fstackademic%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--476f1e3191b3---------------------clap_footer-----------)

4.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=---footer_actions--476f1e3191b3---------------------bookmark_footer-----------)

[![Image 5: Abdur Rahman](https://miro.medium.com/v2/resize:fill:144:144/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=post_page---post_author_info--476f1e3191b3--------------------------------)

[![Image 6: Stackademic](https://miro.medium.com/v2/resize:fill:64:64/1*U-kjsW7IZUobnoy1gAp1UQ.png)](https://blog.stackademic.com/?source=post_page---post_author_info--476f1e3191b3--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--476f1e3191b3---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--476f1e3191b3---------------------subscribe_user-----------)

[Stackademic](https://blog.stackademic.com/?source=post_page---post_author_info--476f1e3191b3--------------------------------)

𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐚𝐧𝐝 𝐒𝐡𝐚𝐫𝐢𝐧𝐠 𝐊𝐧𝐨𝐰𝐥𝐞𝐝𝐠𝐞 𝐄𝐯𝐞𝐫𝐲𝐝𝐚𝐲 | 𝐏𝐲𝐭𝐡𝐨𝐧 𝐢𝐬 ❤️ | 𝐌𝐮𝐬𝐥𝐢𝐦 | #𝐢𝐬𝐭𝐚𝐧𝐝𝐰𝐢𝐭𝐡𝐩𝐚𝐥𝐞𝐬𝐭𝐢𝐧𝐞🍉

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--476f1e3191b3---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--476f1e3191b3---------------------subscribe_user-----------)

More from Abdur Rahman and Stackademic
--------------------------------------

![Image 7: 20 Python Scripts To Automate Your Daily Tasks](https://miro.medium.com/v2/resize:fit:679/1*iGrbJxU6oV3q7LeNV28gWg.jpeg)

[![Image 8: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[20 Python Scripts To Automate Your Daily Tasks ---------------------------------------------- ### A must-have collection for every developer](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

Oct 7

[2.3K 22](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----476f1e3191b3----0---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----476f1e3191b3----0-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

![Image 9: 20 Git Command-Line Tricks Every Developer Should Know](https://miro.medium.com/v2/resize:fit:679/1*lyEwUyQSkpm0rb4yvn80qA.png)

[![Image 10: Crafting-Code](https://miro.medium.com/v2/resize:fill:20:20/1*CyROwr3ZEi4KqVBfjqHHeg.png)](https://medium.com/@craftingcode?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Crafting-Code](https://medium.com/@craftingcode?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[20 Git Command-Line Tricks Every Developer Should Know ------------------------------------------------------ ### Git Smarter, Code Faster](https://medium.com/20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

Oct 9

[1.4K 20](https://medium.com/20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9?source=author_recirc-----476f1e3191b3----1---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbf817e83d6b9&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9&source=-----476f1e3191b3----1-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

![Image 11: Title Image](https://miro.medium.com/v2/resize:fit:679/0*02Rxo8X6uaLmkCX3.png)

[![Image 12: Madza](https://miro.medium.com/v2/resize:fill:20:20/1*SCx6IqmQJAzddxnBTcXlFg.png)](https://madzadev.medium.com/?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Madza](https://madzadev.medium.com/?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[16 Open-Source Projects to Improve Your Developer Workflow 👨‍💻🔥 ------------------------------------------------------------------](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[783 9](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----476f1e3191b3----2---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffdd3b8c16e57&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57&source=-----476f1e3191b3----2-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

![Image 13: 10 AI-Powered Python Libraries to Boost Your Next Project](https://miro.medium.com/v2/resize:fit:679/1*isqWuyZYRx2-sbFIuLwUJg.jpeg)

[![Image 14: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[10 AI-Powered Python Libraries to Boost Your Next Project --------------------------------------------------------- ### From “Eh, pretty cool” to “Wow, how’d you do that?!”](https://python.plainenglish.io/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[1K 3](https://python.plainenglish.io/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----476f1e3191b3----3---------------------ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fac74d614e3b8&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8&source=-----476f1e3191b3----3-----------------bookmark_preview----ba6d15dc_dc21_48aa_9eae_bd73069827b1-------)

[See all from Abdur Rahman](https://medium.com/@abdur-rahman?source=post_page-----476f1e3191b3--------------------------------)

[See all from Stackademic](https://blog.stackademic.com/?source=post_page-----476f1e3191b3--------------------------------)

[![Image 16: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----476f1e3191b3----0-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

![Image 17: Can you solve this famous interview question?](https://miro.medium.com/v2/resize:fit:679/1*ojvznevS00pnY77w0jnxPg.jpeg)

[![Image 18: Paolo Molignini, PhD](https://miro.medium.com/v2/resize:fill:20:20/1*G00MhBr4w2Ja-mXFgZ6g1Q.jpeg)](https://medium.com/@moligninip?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Paolo Molignini, PhD](https://medium.com/@moligninip?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Puzzle Sphere](https://medium.com/puzzle-sphere?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Can you solve this famous interview question? --------------------------------------------- ### 100 passengers, 100 seats — but the first one sits randomly! What’s the chance the last passenger ends up in their own seat? Find out here!](https://medium.com/puzzle-sphere/can-you-solve-this-famous-interview-question-91d0db846935?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

Oct 5

[2.1K 57](https://medium.com/puzzle-sphere/can-you-solve-this-famous-interview-question-91d0db846935?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F91d0db846935&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fpuzzle-sphere%2Fcan-you-solve-this-famous-interview-question-91d0db846935&source=-----476f1e3191b3----1-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[![Image 28](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*UeZPcm_AcNpatRN4) ![Image 29](https://miro.medium.com/v2/resize:fill:48:48/1*sg3I6-CAKFnt7HZQQqFNJw.png) ![Image 30](https://miro.medium.com/v2/resize:fill:48:48/1*Rt9RS9ES0tDnXZ-8t5ZOyA.png) Natural Language Processing --------------------------- 1801 stories·1412 saves](https://medium.com/@AMGAS14/list/natural-language-processing-0a856388a93a?source=read_next_recirc-----476f1e3191b3--------------------------------)

![Image 31: 20 Python Scripts To Automate Your Daily Tasks](https://miro.medium.com/v2/resize:fit:679/1*iGrbJxU6oV3q7LeNV28gWg.jpeg)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[20 Python Scripts To Automate Your Daily Tasks ---------------------------------------------- ### A must-have collection for every developer](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

Oct 7

[2.3K 22](https://medium.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=read_next_recirc-----476f1e3191b3----0---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----476f1e3191b3----0-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

![Image 33: How Old Is Your Body? Stand On One Leg and Find Out](https://miro.medium.com/v2/resize:fit:679/1*GZmK6Wv4dD6dqpzf8Ydzsg.jpeg)

[![Image 34: F. Perry Wilson, MD MSCE](https://miro.medium.com/v2/resize:fill:20:20/1*7hsQz8sWZ4sNZCOfTIBvhQ.jpeg)](https://fperrywilson.medium.com/?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[F. Perry Wilson, MD MSCE](https://fperrywilson.medium.com/?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[How Old Is Your Body? Stand On One Leg and Find Out --------------------------------------------------- ### According to new research, the time you can stand on one leg is the best marker of physical aging.](https://fperrywilson.medium.com/how-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[10.6K 221](https://fperrywilson.medium.com/how-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da?source=read_next_recirc-----476f1e3191b3----1---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffcf8241107da&operation=register&redirect=https%3A%2F%2Ffperrywilson.medium.com%2Fhow-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da&source=-----476f1e3191b3----1-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

![Image 35: A MacBook](https://miro.medium.com/v2/resize:fit:679/0*ibammcgaL-gMehSK)

[![Image 36: Andrew Zuo](https://miro.medium.com/v2/resize:fill:20:20/1*FZEG_DxaZ4g-w10VST7WGg.jpeg)](https://andrewzuo.com/?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Andrew Zuo](https://andrewzuo.com/?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Mac O’Clock](https://medium.com/macoclock?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[The M4 MacBook Pro Makes Me Want To Buy A Windows Laptop --------------------------------------------------------](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[918 70](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----476f1e3191b3----2---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8f81e91c7622&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmacoclock%2Fthe-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622&source=-----476f1e3191b3----2-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[![Image 38: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----476f1e3191b3----3---------------------bf6dd282_c137_4692_8fa0_a361a833f2e9-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----476f1e3191b3----3-----------------bookmark_preview----bf6dd282_c137_4692_8fa0_a361a833f2e9-------)


---

## Stackademic

Source: https://medium.com/stackademic/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63
Date fetched: 2024-11-10T01:47:14.195053

---

Title: 20 Python Scripts To Automate Your Daily Tasks - Stackademic

URL Source: https://medium.com/stackademic/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63

Published Time: 2024-10-07T03:18:42.230Z

20 Python Scripts To Automate Your Daily Tasks
==============================================

A must-have collection for every developer
------------------------------------------

2.3K

22

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=---header_actions--4c6f4b15fe63---------------------post_audio_button-----------)

![Image 4: a man is sitting in front of a computer](https://miro.medium.com/v2/resize:fit:700/1*iGrbJxU6oV3q7LeNV28gWg.jpeg)

AI generated Image

Not a member yet, read it [_here_](https://medium.com/stackademic/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?sk=3dbcee612f6e06225dd660e4a669bd7f)_._

I assume you have been coding in Python for a while and you think you are pretty good at it. Or you still just navigate the endless stream of StackOverflow pages. Either way I can bet that you are craving for scripts that’ll make you look like a coding wizard.

I have got 20 Python scripts that’ll have you impressing your colleagues, automating the un-automatable, and solving problems you didn’t even know you had.

Let’s get to it!

1\. File Duplication Finder (Save Your Hard Drive’s Life)
---------------------------------------------------------

You ever look at your hard drive and wonder, _Why do I only have 100MB left?_ File duplicates. They’re sneaky. Here’s a script to find and delete them:

import os  
import hashlib  
  
def hash\_file(filename):  
    h = hashlib.md5()  
    with open(filename, 'rb') as file:  
        while chunk := file.read(8192):  
            h.update(chunk)  
    return h.hexdigest()  
  
def find\_duplicates(folder):  
    hashes = {}  
    for dirpath, \_, filenames in os.walk(folder):  
        for f in filenames:  
            full\_path = os.path.join(dirpath, f)  
            file\_hash = hash\_file(full\_path)  
            if file\_hash in…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63%3Fsource%3D-----4c6f4b15fe63---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----4c6f4b15fe63---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63%3Fsource%3D-----4c6f4b15fe63---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----4c6f4b15fe63---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63%3Fsource%3D-----4c6f4b15fe63---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----4c6f4b15fe63---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----4c6f4b15fe63---------------------post_regwall-----------)

2.3K

2.3K

22

[![Image 8: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[4.1K 22](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----4c6f4b15fe63----0-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 10: Crafting-Code](https://miro.medium.com/v2/resize:fill:20:20/1*CyROwr3ZEi4KqVBfjqHHeg.png)](https://medium.com/@craftingcode?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Crafting-Code](https://medium.com/@craftingcode?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[1.4K 20](https://medium.com/20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbf817e83d6b9&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9&source=-----4c6f4b15fe63----1-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 12: Madza](https://miro.medium.com/v2/resize:fill:20:20/1*SCx6IqmQJAzddxnBTcXlFg.png)](https://madzadev.medium.com/?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Madza](https://madzadev.medium.com/?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[16 Open-Source Projects to Improve Your Developer Workflow 👨‍💻🔥 ------------------------------------------------------------------](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[783 9](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffdd3b8c16e57&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57&source=-----4c6f4b15fe63----2-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 14: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[1K 3](https://python.plainenglish.io/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fac74d614e3b8&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8&source=-----4c6f4b15fe63----3-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 16: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----4c6f4b15fe63----0-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 18: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[4.1K 22](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----4c6f4b15fe63----1-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 25](https://miro.medium.com/v2/resize:fill:48:48/1*I2o9__q4g1dzbcH9XRqcRg.png) ![Image 26](https://miro.medium.com/v2/resize:fill:48:48/0*F6q2BN7oddumBDGY.png) ![Image 27](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*dT68KKwa4mw4ShQJ) ChatGPT prompts --------------- 50 stories·2189 saves](https://medium.com/@nicholas.michael.janulewicz/list/chatgpt-prompts-b4c47b8e12ee?source=read_next_recirc-----4c6f4b15fe63--------------------------------)

[![Image 28](https://miro.medium.com/v2/resize:fill:48:48/1*vzu3JPzaq2EZKTZNY9BhLA.png) ![Image 29: AI-generated image of a cute tiny robot in the backdrop of ChatGPT’s logo](https://miro.medium.com/v2/resize:fill:48:48/1*lEmL62oZdrOOWIzAAFKiFg.jpeg) ![Image 30](https://miro.medium.com/v2/resize:fill:48:48/1*i2zLIwC9mftamP1dbciCeQ.jpeg) ChatGPT ------- 21 stories·864 saves](https://medium.com/@m.wasalski/list/chatgpt-3742c7a4727d?source=read_next_recirc-----4c6f4b15fe63--------------------------------)

[![Image 32: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----4c6f4b15fe63----0-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 34: Andrew Zuo](https://miro.medium.com/v2/resize:fill:20:20/1*FZEG_DxaZ4g-w10VST7WGg.jpeg)](https://andrewzuo.com/?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Andrew Zuo](https://andrewzuo.com/?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Mac O’Clock](https://medium.com/macoclock?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[The M4 MacBook Pro Makes Me Want To Buy A Windows Laptop --------------------------------------------------------](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[918 70](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8f81e91c7622&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmacoclock%2Fthe-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622&source=-----4c6f4b15fe63----1-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 36: F. Perry Wilson, MD MSCE](https://miro.medium.com/v2/resize:fill:20:20/1*7hsQz8sWZ4sNZCOfTIBvhQ.jpeg)](https://fperrywilson.medium.com/?source=read_next_recirc-----4c6f4b15fe63----2---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[10.6K 221](https://fperrywilson.medium.com/how-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da?source=read_next_recirc-----4c6f4b15fe63----2---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffcf8241107da&operation=register&redirect=https%3A%2F%2Ffperrywilson.medium.com%2Fhow-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da&source=-----4c6f4b15fe63----2-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 38: Paolo Molignini, PhD](https://miro.medium.com/v2/resize:fill:20:20/1*G00MhBr4w2Ja-mXFgZ6g1Q.jpeg)](https://medium.com/@moligninip?source=read_next_recirc-----4c6f4b15fe63----3---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Puzzle Sphere](https://medium.com/puzzle-sphere?source=read_next_recirc-----4c6f4b15fe63----3---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[2.1K 57](https://medium.com/puzzle-sphere/can-you-solve-this-famous-interview-question-91d0db846935?source=read_next_recirc-----4c6f4b15fe63----3---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F91d0db846935&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fpuzzle-sphere%2Fcan-you-solve-this-famous-interview-question-91d0db846935&source=-----4c6f4b15fe63----3-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

## Visual Content Analysis

### Image Analysis
Title: 20 Python Scripts To Automate Your Daily Tasks - Stackademic

URL Source: https://medium.com/stackademic/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63

Published Time: 2024-10-07T03:18:42.230Z

20 Python Scripts To Automate Your Daily Tasks
==============================================

A must-have collection for every developer
------------------------------------------

2.3K

22

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=---header_actions--4c6f4b15fe63---------------------post_audio_button-----------)

![Image 4: a man is sitting in front of a computer](https://miro.medium.com/v2/resize:fit:700/1*iGrbJxU6oV3q7LeNV28gWg.jpeg)

AI generated Image

Not a member yet, read it [_here_](https://medium.com/stackademic/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?sk=3dbcee612f6e06225dd660e4a669bd7f)_._

I assume you have been coding in Python for a while and you think you are pretty good at it. Or you still just navigate the endless stream of StackOverflow pages. Either way I can bet that you are craving for scripts that’ll make you look like a coding wizard.

I have got 20 Python scripts that’ll have you impressing your colleagues, automating the un-automatable, and solving problems you didn’t even know you had.

Let’s get to it!

1\. File Duplication Finder (Save Your Hard Drive’s Life)
---------------------------------------------------------

You ever look at your hard drive and wonder, _Why do I only have 100MB left?_ File duplicates. They’re sneaky. Here’s a script to find and delete them:

import os  
import hashlib  
  
def hash\_file(filename):  
    h = hashlib.md5()  
    with open(filename, 'rb') as file:  
        while chunk := file.read(8192):  
            h.update(chunk)  
    return h.hexdigest()  
  
def find\_duplicates(folder):  
    hashes = {}  
    for dirpath, \_, filenames in os.walk(folder):  
        for f in filenames:  
            full\_path = os.path.join(dirpath, f)  
            file\_hash = hash\_file(full\_path)  
            if file\_hash in…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63%3Fsource%3D-----4c6f4b15fe63---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----4c6f4b15fe63---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63%3Fsource%3D-----4c6f4b15fe63---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----4c6f4b15fe63---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63%3Fsource%3D-----4c6f4b15fe63---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----4c6f4b15fe63---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----4c6f4b15fe63---------------------post_regwall-----------)

2.3K

2.3K

22

[![Image 8: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[4.1K 22](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----4c6f4b15fe63----0---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----4c6f4b15fe63----0-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 10: Crafting-Code](https://miro.medium.com/v2/resize:fill:20:20/1*CyROwr3ZEi4KqVBfjqHHeg.png)](https://medium.com/@craftingcode?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Crafting-Code](https://medium.com/@craftingcode?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[1.4K 20](https://medium.com/20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9?source=author_recirc-----4c6f4b15fe63----1---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbf817e83d6b9&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-git-command-line-tricks-every-developer-should-know-bf817e83d6b9&source=-----4c6f4b15fe63----1-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 12: Madza](https://miro.medium.com/v2/resize:fill:20:20/1*SCx6IqmQJAzddxnBTcXlFg.png)](https://madzadev.medium.com/?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Madza](https://madzadev.medium.com/?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[16 Open-Source Projects to Improve Your Developer Workflow 👨‍💻🔥 ------------------------------------------------------------------](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[783 9](https://medium.com/16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57?source=author_recirc-----4c6f4b15fe63----2---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffdd3b8c16e57&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F16-open-source-projects-to-improve-your-developer-workflow-fdd3b8c16e57&source=-----4c6f4b15fe63----2-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 14: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[1K 3](https://python.plainenglish.io/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----4c6f4b15fe63----3---------------------c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fac74d614e3b8&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8&source=-----4c6f4b15fe63----3-----------------bookmark_preview----c9c7a878_4daf_4f5f_a53a_a546378b20ec-------)

[![Image 16: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----4c6f4b15fe63----0-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 18: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[4.1K 22](https://medium.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----4c6f4b15fe63----1-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 25](https://miro.medium.com/v2/resize:fill:48:48/1*I2o9__q4g1dzbcH9XRqcRg.png) ![Image 26](https://miro.medium.com/v2/resize:fill:48:48/0*F6q2BN7oddumBDGY.png) ![Image 27](https://miro.medium.com/v2/da:true/resize:fill:48:48/0*dT68KKwa4mw4ShQJ) ChatGPT prompts --------------- 50 stories·2189 saves](https://medium.com/@nicholas.michael.janulewicz/list/chatgpt-prompts-b4c47b8e12ee?source=read_next_recirc-----4c6f4b15fe63--------------------------------)

[![Image 28](https://miro.medium.com/v2/resize:fill:48:48/1*vzu3JPzaq2EZKTZNY9BhLA.png) ![Image 29: AI-generated image of a cute tiny robot in the backdrop of ChatGPT’s logo](https://miro.medium.com/v2/resize:fill:48:48/1*lEmL62oZdrOOWIzAAFKiFg.jpeg) ![Image 30](https://miro.medium.com/v2/resize:fill:48:48/1*i2zLIwC9mftamP1dbciCeQ.jpeg) ChatGPT ------- 21 stories·864 saves](https://medium.com/@m.wasalski/list/chatgpt-3742c7a4727d?source=read_next_recirc-----4c6f4b15fe63--------------------------------)

[![Image 32: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----4c6f4b15fe63----0---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----4c6f4b15fe63----0-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 34: Andrew Zuo](https://miro.medium.com/v2/resize:fill:20:20/1*FZEG_DxaZ4g-w10VST7WGg.jpeg)](https://andrewzuo.com/?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Andrew Zuo](https://andrewzuo.com/?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Mac O’Clock](https://medium.com/macoclock?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[The M4 MacBook Pro Makes Me Want To Buy A Windows Laptop --------------------------------------------------------](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[918 70](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----4c6f4b15fe63----1---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8f81e91c7622&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmacoclock%2Fthe-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622&source=-----4c6f4b15fe63----1-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 36: F. Perry Wilson, MD MSCE](https://miro.medium.com/v2/resize:fill:20:20/1*7hsQz8sWZ4sNZCOfTIBvhQ.jpeg)](https://fperrywilson.medium.com/?source=read_next_recirc-----4c6f4b15fe63----2---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[10.6K 221](https://fperrywilson.medium.com/how-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da?source=read_next_recirc-----4c6f4b15fe63----2---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffcf8241107da&operation=register&redirect=https%3A%2F%2Ffperrywilson.medium.com%2Fhow-old-is-your-body-stand-on-one-leg-and-find-out-fcf8241107da&source=-----4c6f4b15fe63----2-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)

[![Image 38: Paolo Molignini, PhD](https://miro.medium.com/v2/resize:fill:20:20/1*G00MhBr4w2Ja-mXFgZ6g1Q.jpeg)](https://medium.com/@moligninip?source=read_next_recirc-----4c6f4b15fe63----3---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[Puzzle Sphere](https://medium.com/puzzle-sphere?source=read_next_recirc-----4c6f4b15fe63----3---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[2.1K 57](https://medium.com/puzzle-sphere/can-you-solve-this-famous-interview-question-91d0db846935?source=read_next_recirc-----4c6f4b15fe63----3---------------------07812d43_c32a_44f4_9157_b661645fc254-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F91d0db846935&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fpuzzle-sphere%2Fcan-you-solve-this-famous-interview-question-91d0db846935&source=-----4c6f4b15fe63----3-----------------bookmark_preview----07812d43_c32a_44f4_9157_b661645fc254-------)


---

## Python In Plain English

Source: https://medium.com/python-in-plain-english/5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180
Date fetched: 2024-11-10T01:47:48.705495

---

Title: 5 Overrated Python Libraries (And What You Should Use Instead)

URL Source: https://medium.com/python-in-plain-english/5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180

Markdown Content:
5 Overrated Python Libraries (And What You Should Use Instead) | by Abdur Rahman | Nov, 2024 | Python in Plain English
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

5 Overrated Python Libraries (And What You Should Use Instead)
==============================================================

Traditional Devs, Look Away — This One’s Not for You!
-----------------------------------------------------

[![Image 3: Python in Plain English](https://miro.medium.com/v2/resize:fill:48:48/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---byline--106bd9ded180--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--byline--106bd9ded180---------------------post_header-----------)

[Python in Plain English](https://python.plainenglish.io/?source=post_page---byline--106bd9ded180--------------------------------)

Nov 3, 2024

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=---header_actions--106bd9ded180---------------------clap_footer-----------)

1.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=---header_actions--106bd9ded180---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=---header_actions--106bd9ded180---------------------post_audio_button-----------)

![Image 4](https://miro.medium.com/v2/resize:fit:1000/1*fX-RNRwwSujOY05gXdoAlQ.jpeg)

> **Not a member, yet? Read it free** [**_here_**](https://medium.com/@abdur-rahman/5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180?sk=ffa347734cb26468c24d29021c9dc5e9)

Python’s vast ecosystem of libraries can feel like an amusement park for developers. With so many flashy rides, err, libraries to choose from, it’s easy to get swept up in the hype. But some libraries get more attention than they deserve. Whether they’re overhyped by “hot takes” on social media or just suffer from outdated design, a few commonly recommended tools aren’t always the best options out there. So, let’s take a look at some of Python’s most overrated libraries — and I’ll share alternatives that might actually serve you better.

> **Note:** This doesn’t mean these libraries aren’t valuable — quite the opposite! But for specific tasks, there are lighter, faster options that can do the trick just as well, sometimes even better.

1\. **Requests (Yes, Really!)**
===============================

Look, there is nothing inherently wrong with `Requests`. It’s intuitive, it has a great API, and it’s practically the mascot of Python HTTP libraries. But it’s overkill for when you just need to make simple GET/POST requests, and it will lag in environments where you want asynchronous performance.

**Why It’s Overrated:**
-----------------------

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180%3Fsource%3D-----106bd9ded180---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----106bd9ded180---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180%3Fsource%3D-----106bd9ded180---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----106bd9ded180---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180%3Fsource%3D-----106bd9ded180---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----106bd9ded180---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=-----106bd9ded180---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--106bd9ded180---------------------clap_footer-----------)

1.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--106bd9ded180---------------------clap_footer-----------)

1.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=---footer_actions--106bd9ded180---------------------bookmark_footer-----------)

[![Image 6: Python in Plain English](https://miro.medium.com/v2/resize:fill:64:64/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---post_author_info--106bd9ded180--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--106bd9ded180---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--106bd9ded180---------------------subscribe_user-----------)

[Python in Plain English](https://python.plainenglish.io/?source=post_page---post_author_info--106bd9ded180--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--106bd9ded180---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--106bd9ded180---------------------subscribe_user-----------)

More from Abdur Rahman and Python in Plain English
--------------------------------------------------

[![Image 8: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----106bd9ded180----0-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

![Image 9: Why PyMuPDF4LLM is the Best Tool for Extracting Data from PDFs (Even if You Didn’t Know You Needed…](https://miro.medium.com/v2/resize:fit:679/0*_h8XywGiTHmSkmmU)

[![Image 10: Anoop Maurya](https://miro.medium.com/v2/resize:fill:20:20/1*GpLTfdPuDfw-8acfG4GhZg.jpeg)](https://medium.com/@mauryaanoop3?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Anoop Maurya](https://medium.com/@mauryaanoop3?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Why PyMuPDF4LLM is the Best Tool for Extracting Data from PDFs (Even if You Didn’t Know You Needed… --------------------------------------------------------------------------------------------------- ### Stuck behind a paywall? Read for Free!](https://medium.com/why-pymupdf4llm-is-the-best-tool-for-extracting-data-from-pdfs-even-if-you-didnt-know-you-needed-7bff75313691?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[1.5K 15](https://medium.com/why-pymupdf4llm-is-the-best-tool-for-extracting-data-from-pdfs-even-if-you-didnt-know-you-needed-7bff75313691?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7bff75313691&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Fwhy-pymupdf4llm-is-the-best-tool-for-extracting-data-from-pdfs-even-if-you-didnt-know-you-needed-7bff75313691&source=-----106bd9ded180----1-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[![Image 12: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[10 AI-Powered Python Libraries to Boost Your Next Project --------------------------------------------------------- ### From “Eh, pretty cool” to “Wow, how’d you do that?!”](https://medium.com/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[1K 3](https://medium.com/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fac74d614e3b8&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8&source=-----106bd9ded180----2-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[![Image 14: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[20 Python Scripts To Automate Your Daily Tasks ---------------------------------------------- ### A must-have collection for every developer](https://blog.stackademic.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[2.3K 22](https://blog.stackademic.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----106bd9ded180----3-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[See all from Python in Plain English](https://python.plainenglish.io/?source=post_page-----106bd9ded180--------------------------------)

[![Image 16: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----106bd9ded180----0-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[![Image 18: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----106bd9ded180----1-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----106bd9ded180----0-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[![Image 34: Andrew Zuo](https://miro.medium.com/v2/resize:fill:20:20/1*FZEG_DxaZ4g-w10VST7WGg.jpeg)](https://andrewzuo.com/?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Andrew Zuo](https://andrewzuo.com/?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Mac O’Clock](https://medium.com/macoclock?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[The M4 MacBook Pro Makes Me Want To Buy A Windows Laptop --------------------------------------------------------](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[918 70](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

![Image 35: Debugging in Python: Replace print() with ic() and Do It Like a Pro](https://miro.medium.com/v2/resize:fit:679/1*7DsQClQ1Ya7M5Svsl6aSKw.png)

[![Image 36: Kevin Meneses González](https://miro.medium.com/v2/resize:fill:20:20/1*bHVCf4ViLpIXBD3h66bwwA.png)](https://medium.com/@kevinmenesesgonzalez?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Kevin Meneses González](https://medium.com/@kevinmenesesgonzalez?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[The Pythoneers](https://medium.com/pythoneers?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Debugging in Python: Replace print() with ic() and Do It Like a Pro ------------------------------------------------------------------- ### Introduction:](https://medium.com/pythoneers/debugging-in-python-replace-print-with-ic-and-do-it-like-a-pro-18f330c863cb?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[306 2](https://medium.com/pythoneers/debugging-in-python-replace-print-with-ic-and-do-it-like-a-pro-18f330c863cb?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F18f330c863cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fpythoneers%2Fdebugging-in-python-replace-print-with-ic-and-do-it-like-a-pro-18f330c863cb&source=-----106bd9ded180----2-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

![Image 37: The PDF Extraction Revolution: Why PymuPDF4llm is Your New Best Friend (and LlamaParse is Crying)](https://miro.medium.com/v2/resize:fit:679/0*1PQz2rhOIopPlzvo)

[![Image 38: Richardson Gunde](https://miro.medium.com/v2/resize:fill:20:20/1*tp2uj3tur89cbR2GW0SrDQ.png)](https://medium.com/@honeyricky1m3?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Richardson Gunde](https://medium.com/@honeyricky1m3?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[AI Advances](https://ai.gopubby.com/?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[The PDF Extraction Revolution: Why PymuPDF4llm is Your New Best Friend (and LlamaParse is Crying) ------------------------------------------------------------------------------------------------- ### Hey there, data-loving friends! Ready for some serious AI magic? Picture this: you’re knee-deep in PDFs, trying to extract information for…](https://ai.gopubby.com/the-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[847 11](https://ai.gopubby.com/the-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe57882dee7f8&operation=register&redirect=https%3A%2F%2Fai.gopubby.com%2Fthe-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8&source=-----106bd9ded180----3-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

## Visual Content Analysis

### Image Analysis
Title: 5 Overrated Python Libraries (And What You Should Use Instead)

URL Source: https://medium.com/python-in-plain-english/5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180

Markdown Content:
5 Overrated Python Libraries (And What You Should Use Instead) | by Abdur Rahman | Nov, 2024 | Python in Plain English
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

5 Overrated Python Libraries (And What You Should Use Instead)
==============================================================

Traditional Devs, Look Away — This One’s Not for You!
-----------------------------------------------------

[![Image 3: Python in Plain English](https://miro.medium.com/v2/resize:fill:48:48/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---byline--106bd9ded180--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--byline--106bd9ded180---------------------post_header-----------)

[Python in Plain English](https://python.plainenglish.io/?source=post_page---byline--106bd9ded180--------------------------------)

Nov 3, 2024

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=---header_actions--106bd9ded180---------------------clap_footer-----------)

1.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=---header_actions--106bd9ded180---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=---header_actions--106bd9ded180---------------------post_audio_button-----------)

![Image 4](https://miro.medium.com/v2/resize:fit:1000/1*fX-RNRwwSujOY05gXdoAlQ.jpeg)

> **Not a member, yet? Read it free** [**_here_**](https://medium.com/@abdur-rahman/5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180?sk=ffa347734cb26468c24d29021c9dc5e9)

Python’s vast ecosystem of libraries can feel like an amusement park for developers. With so many flashy rides, err, libraries to choose from, it’s easy to get swept up in the hype. But some libraries get more attention than they deserve. Whether they’re overhyped by “hot takes” on social media or just suffer from outdated design, a few commonly recommended tools aren’t always the best options out there. So, let’s take a look at some of Python’s most overrated libraries — and I’ll share alternatives that might actually serve you better.

> **Note:** This doesn’t mean these libraries aren’t valuable — quite the opposite! But for specific tasks, there are lighter, faster options that can do the trick just as well, sometimes even better.

1\. **Requests (Yes, Really!)**
===============================

Look, there is nothing inherently wrong with `Requests`. It’s intuitive, it has a great API, and it’s practically the mascot of Python HTTP libraries. But it’s overkill for when you just need to make simple GET/POST requests, and it will lag in environments where you want asynchronous performance.

**Why It’s Overrated:**
-----------------------

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180%3Fsource%3D-----106bd9ded180---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----106bd9ded180---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180%3Fsource%3D-----106bd9ded180---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----106bd9ded180---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180%3Fsource%3D-----106bd9ded180---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----106bd9ded180---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=-----106bd9ded180---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--106bd9ded180---------------------clap_footer-----------)

1.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=---footer_actions--106bd9ded180---------------------clap_footer-----------)

1.1K

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F106bd9ded180&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&source=---footer_actions--106bd9ded180---------------------bookmark_footer-----------)

[![Image 6: Python in Plain English](https://miro.medium.com/v2/resize:fill:64:64/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---post_author_info--106bd9ded180--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--106bd9ded180---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--106bd9ded180---------------------subscribe_user-----------)

[Python in Plain English](https://python.plainenglish.io/?source=post_page---post_author_info--106bd9ded180--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F7d16279b0e18&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&user=Abdur+Rahman&userId=7d16279b0e18&source=post_page-7d16279b0e18--post_author_info--106bd9ded180---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F844f13e47e8e&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F5-overrated-python-libraries-and-what-you-should-use-instead-106bd9ded180&newsletterV3=7d16279b0e18&newsletterV3Id=844f13e47e8e&user=Abdur+Rahman&userId=7d16279b0e18&source=---post_author_info--106bd9ded180---------------------subscribe_user-----------)

More from Abdur Rahman and Python in Plain English
--------------------------------------------------

[![Image 8: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=author_recirc-----106bd9ded180----0---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----106bd9ded180----0-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

![Image 9: Why PyMuPDF4LLM is the Best Tool for Extracting Data from PDFs (Even if You Didn’t Know You Needed…](https://miro.medium.com/v2/resize:fit:679/0*_h8XywGiTHmSkmmU)

[![Image 10: Anoop Maurya](https://miro.medium.com/v2/resize:fill:20:20/1*GpLTfdPuDfw-8acfG4GhZg.jpeg)](https://medium.com/@mauryaanoop3?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Anoop Maurya](https://medium.com/@mauryaanoop3?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Why PyMuPDF4LLM is the Best Tool for Extracting Data from PDFs (Even if You Didn’t Know You Needed… --------------------------------------------------------------------------------------------------- ### Stuck behind a paywall? Read for Free!](https://medium.com/why-pymupdf4llm-is-the-best-tool-for-extracting-data-from-pdfs-even-if-you-didnt-know-you-needed-7bff75313691?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[1.5K 15](https://medium.com/why-pymupdf4llm-is-the-best-tool-for-extracting-data-from-pdfs-even-if-you-didnt-know-you-needed-7bff75313691?source=author_recirc-----106bd9ded180----1---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7bff75313691&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Fwhy-pymupdf4llm-is-the-best-tool-for-extracting-data-from-pdfs-even-if-you-didnt-know-you-needed-7bff75313691&source=-----106bd9ded180----1-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[![Image 12: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Python in Plain English](https://python.plainenglish.io/?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[10 AI-Powered Python Libraries to Boost Your Next Project --------------------------------------------------------- ### From “Eh, pretty cool” to “Wow, how’d you do that?!”](https://medium.com/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[1K 3](https://medium.com/10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8?source=author_recirc-----106bd9ded180----2---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fac74d614e3b8&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2F10-ai-powered-python-libraries-to-boost-your-next-project-ac74d614e3b8&source=-----106bd9ded180----2-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[![Image 14: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[Stackademic](https://blog.stackademic.com/?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[20 Python Scripts To Automate Your Daily Tasks ---------------------------------------------- ### A must-have collection for every developer](https://blog.stackademic.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[2.3K 22](https://blog.stackademic.com/20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63?source=author_recirc-----106bd9ded180----3---------------------7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6f4b15fe63&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2F20-python-scripts-that-will-give-you-superpowers-4c6f4b15fe63&source=-----106bd9ded180----3-----------------bookmark_preview----7e610b24_1e23_4deb_9f2c_d25902afc686-------)

[See all from Python in Plain English](https://python.plainenglish.io/?source=post_page-----106bd9ded180--------------------------------)

[![Image 16: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----106bd9ded180----0-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[![Image 18: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbd241e3a347a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40harendra21%2Fhow-i-am-using-a-lifetime-100-free-server-bd241e3a347a&source=-----106bd9ded180----1-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----106bd9ded180----0---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----106bd9ded180----0-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[![Image 34: Andrew Zuo](https://miro.medium.com/v2/resize:fill:20:20/1*FZEG_DxaZ4g-w10VST7WGg.jpeg)](https://andrewzuo.com/?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Andrew Zuo](https://andrewzuo.com/?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Mac O’Clock](https://medium.com/macoclock?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[The M4 MacBook Pro Makes Me Want To Buy A Windows Laptop --------------------------------------------------------](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[918 70](https://medium.com/macoclock/the-m4-macbook-pro-makes-me-want-to-buy-a-windows-laptop-8f81e91c7622?source=read_next_recirc-----106bd9ded180----1---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

![Image 35: Debugging in Python: Replace print() with ic() and Do It Like a Pro](https://miro.medium.com/v2/resize:fit:679/1*7DsQClQ1Ya7M5Svsl6aSKw.png)

[![Image 36: Kevin Meneses González](https://miro.medium.com/v2/resize:fill:20:20/1*bHVCf4ViLpIXBD3h66bwwA.png)](https://medium.com/@kevinmenesesgonzalez?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Kevin Meneses González](https://medium.com/@kevinmenesesgonzalez?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[The Pythoneers](https://medium.com/pythoneers?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Debugging in Python: Replace print() with ic() and Do It Like a Pro ------------------------------------------------------------------- ### Introduction:](https://medium.com/pythoneers/debugging-in-python-replace-print-with-ic-and-do-it-like-a-pro-18f330c863cb?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[306 2](https://medium.com/pythoneers/debugging-in-python-replace-print-with-ic-and-do-it-like-a-pro-18f330c863cb?source=read_next_recirc-----106bd9ded180----2---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F18f330c863cb&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fpythoneers%2Fdebugging-in-python-replace-print-with-ic-and-do-it-like-a-pro-18f330c863cb&source=-----106bd9ded180----2-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)

![Image 37: The PDF Extraction Revolution: Why PymuPDF4llm is Your New Best Friend (and LlamaParse is Crying)](https://miro.medium.com/v2/resize:fit:679/0*1PQz2rhOIopPlzvo)

[![Image 38: Richardson Gunde](https://miro.medium.com/v2/resize:fill:20:20/1*tp2uj3tur89cbR2GW0SrDQ.png)](https://medium.com/@honeyricky1m3?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[Richardson Gunde](https://medium.com/@honeyricky1m3?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[AI Advances](https://ai.gopubby.com/?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[The PDF Extraction Revolution: Why PymuPDF4llm is Your New Best Friend (and LlamaParse is Crying) ------------------------------------------------------------------------------------------------- ### Hey there, data-loving friends! Ready for some serious AI magic? Picture this: you’re knee-deep in PDFs, trying to extract information for…](https://ai.gopubby.com/the-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[847 11](https://ai.gopubby.com/the-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8?source=read_next_recirc-----106bd9ded180----3---------------------970a4a0c_13f0_4005_a482_50bb57d434a7-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe57882dee7f8&operation=register&redirect=https%3A%2F%2Fai.gopubby.com%2Fthe-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8&source=-----106bd9ded180----3-----------------bookmark_preview----970a4a0c_13f0_4005_a482_50bb57d434a7-------)


---



# Bundle: finance_articles

# Finance Articles Collection

## Table of Contents

### General
- [Towards Data Science](#towards-data-science)
- [Towards Data Science](#towards-data-science)
- [The Data Entrepreneurs](#the-data-entrepreneurs)

---

# General

## Towards Data Science

Source: https://medium.com/towards-data-science/understanding-llms-from-scratch-using-middle-school-math-e602d27ec876
Date fetched: 2024-11-10T01:48:53.174411

---

Title: LLMs from Scratch Using Middle School Math | Towards Data Science

URL Source: https://medium.com/towards-data-science/understanding-llms-from-scratch-using-middle-school-math-e602d27ec876

Markdown Content:
A self-contained, full explanation to inner workings of an LLM
--------------------------------------------------------------

[![Image 1: Rohit Patel](https://miro.medium.com/v2/resize:fill:88:88/1*ECmWr6Z-ToM5JE-h8ywyLQ.jpeg)](https://rohit-patel.medium.com/?source=post_page---byline--e602d27ec876--------------------------------)

In this article, we talk about how Large Language Models (LLMs) work, from scratch — assuming only that you know how to add and multiply two numbers. The article is meant to be fully self-contained. We start by building a simple Generative AI on pen and paper, and then walk through everything we need to have a firm understanding of modern LLMs and the Transformer architecture. The article will strip out all the fancy language and jargon in ML and represent everything simply as they are: numbers. We will still call out what things are called to tether your thoughts when you read jargon-y content.

Going from addition/multiplication to the most advanced AI models today without assuming other knowledge or referring to other sources means we cover a LOT of ground. This is NOT a toy LLM explanation — a determined person can theoretically recreate a modern LLM from all the information here. I have cut out every word/line that was unnecessary and as such this article isn’t really meant to be browsed.

What will we cover?
-------------------

1.  A simple neural network
2.  How are these models trained?
3.  How does all this generate language?
4.  What makes LLMs work so well?
5.  Embeddings
6.  Sub-word tokenizers
7.  Self-attention
8.  Softmax
9.  Residual connections
10.  Layer Normalization
11.  Dropout
12.  Multi-head attention
13.  Positional embeddings
14.  The GPT architecture
15.  The transformer architecture

Let’s dive in.

The first thing to note is that neural networks can only take numbers as inputs and can only output numbers. No exceptions. The art is in figuring out how to feed your inputs as numbers, interpreting the output numbers in a way that achieves your goals. And finally, building neural nets that will take the inputs you provide and give you the outputs you want (given the interpretation you chose for these outputs). Let’s walk through how we get from adding and multiplying numbers to things like [Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/).

A simple neural network:
------------------------

Let’s work through a simple neural network that can classify an object:

*   **Object data available:** Dominant color (RGB) & Volume (in milli-liters)
*   **Classify into**: Leaf OR Flower

Here’s what the data for a leaf and a sunflower can look like:

![Image 3: a table showing the number of leaves and flowers](https://miro.medium.com/v2/resize:fit:700/1*ymWXxVf7N4-Ps-62Cih2XQ.png)

Image by author

Let’s now build a neural net that does this classification. We need to decide on input/output interpretations. Our inputs are already numbers, so we can feed them directly into the network. Our outputs are two objects, leaf and flower which the neural network cannot output. Let’s look at a couple of schemes we can use here:

*   We can make the network output a single number. And if the number is positive we say it’s a leaf and if it is negative we say it’s a flower
*   OR, we can make the network output two numbers. We interpret the first one as a number for leaf and second one as the number for flower and we will say that the selection is whichever number is larger

Both schemes allow the network to output number(s) that we can interpret as leaf or flower. Let’s pick the second scheme here because it generalizes well to other things we will look at later. And here’s a neural network that does the classification using this scheme. Let’s work through it:

![Image 4: a sunflower with a number of sunflowers](https://miro.medium.com/v2/resize:fit:700/1*D-e4rt_QBPp1fMY5OseJiQ.png)

Image by author

Blue circle like so: (32 \* 0.10) **+** (107 \* -0.29) **+** (56 \* -0.07) **+** (11.2 \* 0.46) = **— 26.6**

Some jargon:

**_Neurons/nodes_**: The numbers in the circles

**_Weights_**: The colored numbers on the lines

**_Layers_**: A collection of neurons is called a layer. You could think of this network as having 3 layers: Input layer with 4 neurons, Middle layer with 3 neurons, and the Output layer with 2 neurons.

To calculate the prediction/output from this network (called a “**forward pass**”), you start from the left. We have the data available for the neurons in the Input layer. To move “forward” to the next layer, you multiply the number in the circle with the weight for the corresponding neuron pairing and you add them all up. We demonstrate blue and orange circle math above. Running the whole network we see that the first number in the output layer comes out higher so we interpret it as “network classified these (RGB,Vol) values as leaf”. A well trained network can take various inputs for (RGB,Vol) and correctly classify the object.

The model has no notion of what a leaf or a flower is, or what (RGB,Vol) are. It has a job of taking in exactly 4 numbers and giving out exactly 2 numbers. It is our interpretation that the 4 input numbers are (RGB,Vol) and it is also our decision to look at the output numbers and infer that if the first number is larger it’s a leaf and so on. And finally, it is also up to us to choose the right weights such that the model will take our input numbers and give us the right two numbers such that when we interpret them we get the interpretation we want.

An interesting side effect of this is that you can take the same network and instead of feeding RGB,Vol feed other 4 numbers like cloud cover, humidity etc.. and interpret the two numbers as “Sunny in an hour” or “Rainy in an hour” and then if you have the weights well calibrated you can get the exact same network to do two things at the same time — classify leaf/flower and predict rain in an hour! The network just gives you two numbers, whether you interpret it as classification or prediction or something else is entirely up to you.

Stuff left out for simplification (feel free to ignore without compromising comprehensibility):

*   **Activation layer**: A critical thing missing from this network is an “activation layer”. That’s a fancy word for saying that we take the number in each circle and apply a nonlinear function to it (**RELU** is a common function where you just take the number and set it to zero if it is negative, and leave it unchanged if it is positive). So basically in our case above, we would take the middle layer and replace the two numbers (-26.6 and -47.1) with zeros before we proceed further to the next layer. Of course, we would have to re-train the weights here to make the network useful again. Without the activation layer all the additions and multiplications in the network can be collapsed to a single layer. In our case, you could write the green circle as the sum of RGB directly with some weights and you would not need the middle layer. It would be something like (0.10 \* -0.17 + 0.12 \* 0.39–0.36 \* 0.1) \* R + (-0.29 \* -0.17–0.05 \* 0.39–0.21 \* 0.1) \* G …and so on. This is usually not possible if we have a nonlinearity there. This helps networks deal with more complex situations.
*   **Bias:** Networks will usually also contain another number associated with each node, this number is simply added to the product to calculate the value of the node and this number is called the “bias”. So if the bias for the top blue node was 0.25 then the value in the node would be: (32 \* 0.10) + (107 \* -0.29) + (56 \* -0.07) + (11.2 \* 0.46) **\+ 0.25** \= — 26.35. The word parameters is usually used to refer to all these numbers in the model that are not neurons/nodes.
*   **Softmax:** We don’t usually interpret the output layer directly as shown in our models. We convert the numbers into probabilities (i.e. make it so that all numbers are positive and add up to 1). If all the numbers in the output layer were already positive one way you could achieve this is by dividing each number by the sum of all numbers in the output layer. Though a “softmax” function is normally used which can handle both positive and negative numbers.

How are these models trained?
-----------------------------

In the example above, we magically had the weights that allowed us to put data into the model and get a good output. But how are these weights determined? The process of setting these weights (or “parameters”) is called “**training the model**”, and we need some training data to train the model.

Let’s say we have some data where we have the inputs and we already know if each input corresponds to leaf or flower, this is our “**training data**” and since we have the leaf/flower label for each set of (R,G,B,Vol) numbers, this is “**labeled data**”.

Here’s how it works:

*   Start with a random numbers, i.e. set each parameter/weight to a random number
*   Now, we know that when we input the data corresponding to the leaf (R=32, G=107, B=56, Vol=11.2). Suppose we want a larger number for leaf in the output layer. Let’s say we want the number corresponding to leaf as 0.8 and the one corresponding to flower as 0.2 (as shown in example above, but these are illustrative numbers to demonstrate training, in reality we would not want 0.8 and 0.2. In reality these would be probabilities, which they are not here, and we would them to be 1 and 0)
*   We know the numbers we want in the output layer, and the numbers we are getting from the randomly selected parameters (which are different from what we want). So for all the neurons in the output layer, let’s take the difference between the number we want and the number we have. Then add up the differences. E.g., if the output layer is 0.6 and 0.4 in the two neurons, then we get: (0.8–0.6)=0.2 and (0.2–0.4)= -0.2 so we get a total of 0.4 (ignoring minus signs before adding). We can call this our “**loss**”. Ideally we want the loss to be close to zero, i.e. we want to “**minimize the loss**”.
*   Once we have the loss, we can slightly change each parameter to see if increasing or decreasing it will increase the loss or decrease it. This is called the “**gradient**” of that parameter. Then we can move each of the parameters by a small amount in the direction where the loss goes down (the direction of the gradient). Once we have moved all the parameters slightly, the loss should be lower
*   Keep repeating the process and you will reduce the loss, and eventually have a set of weights/parameters that are “**trained**”. This whole process is called “**gradient descent**”.

Couple of notes:

*   You often have multiple training examples, so when you change the weights slightly to minimize the loss for one example it might make the loss worse for another example. The way to deal with this is to define loss as average loss over all the examples and then take gradient over that average loss. This reduces the average loss over the entire training data set. Each such cycle is called an “**epoch**”. Then you can keep repeating the epochs thus finding weights that reduce average loss.
*   We don’t actually need to “move weights around” to calculate the gradient for each weight — we can just infer it from the formula (e.g. if the weight is 0.17 in the last step, and the value of neuron is positive, and we want a larger number in output we can see that increasing this number to 0.18 will help).

In practice, training deep networks is a hard and complex process because gradients can easily spiral out of control, going to zero or infinity during training (called “vanishing gradient” and “exploding gradient” problems). The simple definition of loss that we talked about here is perfectly valid, but rarely used as there are better functional forms that work well for specific purposes. With modern models containing billions of parameters, training a model requires massive compute resources which has its own problems (memory limitations, parallelization etc.)

How does all this help generate language?
-----------------------------------------

Remember, neural nets take in some numbers, do some math based on the trained parameters, and give out some other numbers. Everything is about interpretation and training the parameters (i.e. setting them to some numbers). If we can interpret the two numbers as “leaf/flower” or “rain or sun in an hour”, we can also interpret them as “next character in a sentence”.

But there are more than 2 letters in English, and so we must expand the number of neurons in the output layer to, say, the 26 letters in the English language (let’s also throw in some symbols like space, period etc..). Each neuron can correspond to a character and we look at the (26 or so) neurons in the output layer and say that the character corresponding to the highest numbered neuron in the output layer is the output character. Now we have a network that can take some inputs and output a character.

What if we replace the input in our network with these characters: “Humpty Dumpt” and asked it to output a character and interpreted it as the “Network’s suggestion of the next character in the sequence that we just entered”. We can probably set the weights well enough for it to output “y” — thereby completing “Humpty Dumpty”. Except for one problem, how do we input these lists of characters in the network? Our network only accepts numbers!!

One simple solution is to assign a number to each character. Let’s say a=1, b=2 and so on. Now we can input “humpty dumpt” and train it to give us “y”. Our network looks something like this:

![Image 5: a diagram showing the different types of networks](https://miro.medium.com/v2/resize:fit:700/1*XPyJ-V0vbPv6EDwFpk7KYQ.png)

Image by author

Ok, so now we can predict one character ahead by providing the network a list of characters. We can use this fact to build a whole sentence. For example, once we have the “y” predicted, we can append that “y” to the list of characters we have and feed it to the network and ask it to predict the next character. And if well trained it should give us a space, and so on and so forth. By the end, we should be able to recursively generate “Humpty Dumpty sat on a wall”. We have Generative AI. Moreover, **_we now have a network capable of generating language!_** Now, nobody ever actually puts in randomly assigned numbers and we will see more sensible schemes down the line. If you cannot wait, feel free to check out the one-hot encoding section in the appendix.

Astute readers will note that we can’t actually input “Humpty Dumpty” into the network since the way the diagram is, it only has 12 neurons in the input layer one for each character in “humpty dumpt” (including the space). So how can we put in the “y” for the next pass. Putting a 13th neuron there would require us to modify the entire network, that’s not workable. The solution is simple, let’s kick the “h” out and send the 12 most recent characters. So we would be sending “umpty dumpty” and the network will predict a space. Then we would input “mpty dumpty “ and it will produce an s and so on. It looks something like this:

![Image 6: a diagram showing the different types of inputs](https://miro.medium.com/v2/resize:fit:700/1*0_tSCfEAL9NIK8U95Q-6Vg.png)

Image by author

We’re throwing away a lot of information in the last line by feeding the model only “ sat on the wal”. So what do the latest and greatest networks of today do? More or less exactly that. The length of inputs we can put into a network is fixed (determined by the size of the input layer). This is called “context length” — the context that is provided to the network to make future predictions. Modern networks can have very large context lengths (several thousand words) and that helps. There are some ways of inputting infinite length sequences but the performance of those methods, while impressive, has since been surpassed by other models with large (but fixed) context length.

One other thing careful readers will notice is that we have different interpretations for inputs and outputs for the same letters! For example, when inputting “h” we are simply denoting it with the number 8 but on the output layer we are not asking the model to output a single number (8 for “h”, 9 for “i” and so on..) instead we are are asking the model to output 26 numbers and then we see which one is the highest and then if the 8th number is highest we interpret the output as “h”. Why don’t we use the same, consistent, interpretation on both ends? We could, it’s just that in the case of language, freeing yourself to choose between different interpretations gives you a better chance of building better models. And it just so happens that the most effective currently known interpretations for the input and output are different. In-fact, the way we are inputting numbers in this model is not the best way to do it, we will look at better ways to do that shortly.

What makes large language models work so well?
----------------------------------------------

Generating “Humpty Dumpty sat on a wall” character-by-character is a far cry from what modern LLMs can do. There are a number of differences and innovations that get us from the simple generative AI that we discussed above to the human-like bot. Let’s go through them:

Embeddings
----------

Remember we said that the way that we are inputting characters into the model isn’t the best way to do it. We just arbitrarily selected a number for each character. What if there were better numbers we could assign that would make it possible for us to train better networks? How do we find these better numbers? Here’s a clever trick:

When we trained the models above, the way we did it was by moving around weights and seeing that gives us a smaller loss in the end. And then slowly and recursively changing the weights. At each turn we would:

*   Feed in the inputs
*   Calculate the output layer
*   Compare it to the output we ideally want and calculate the average loss
*   Adjust the weights and start again

In this process, the inputs are fixed. This made sense when inputs were (RGB, Vol). But the numbers we are putting in now for a,b,c etc.. are arbitrarily picked by us. What if at every iteration in addition to moving the weights around by a bit we also moved the input around and see if we can get a lower loss by using a different number to represent “a” and so on? We are definitely reducing the loss and making the model better (that’s the direction we moved a’s input in, by design). Basically, apply gradient descent not just to the weights but also the number representations for the inputs since they are arbitrarily picked numbers anyway. This is called an “**embedding**”. It is a mapping of inputs to numbers, and as you just saw, it needs to be trained. The process of training an embedding is much like that of training a parameter. One big advantage of this though is that once you train an embedding you can use it in another model if you wish. Keep in mind that you will consistently use the same embedding to represent a single token/character/word.

We talked about embeddings that are just one number per character. However, in reality embeddings have more than one number. That’s because it is hard to capture the richness of concept by a single number. If we look at our leaf and flower example, we have four numbers for each object (the size of the input layer). Each of these four numbers conveyed a property and the model was able to use all of them to effectively guess the object. If we had only one number, say the red channel of the color, it might have been a lot harder for the model. We’re trying to capture human language here — we’re going to need more than one number.

So instead of representing each character by a single number, maybe we can represent it by multiple numbers to capture the richness? Let’s assign a bunch of numbers to each character. Let’s call an ordered collection of numbers a “vector” (ordered as in each number has a position, and if we swap position of two numbers it gives us a different vector. This was the case with our leaf/flower data, if we swapped the R and G numbers for the leaf, we would get a different color, it would not be the same vector anymore). The length of a vector is simply how many numbers it contains. We’ll assign a vector to each character. Two questions arise:

*   If we have a vector assigned to each character instead of a number, how do we now feed “humpty dumpt” to the network? The answer is simple. Let’s say we assigned a vector of 10 numbers to each character. Then instead of the input layer having 12 neurons we would just put 120 neurons there since each of the 12 characters in “humpty dumpt” has 10 numbers to input. Now we just put the neurons next to each other and we are good to go
*   How do we find these vectors? Thankfully, we just learned how to train embedding numbers. Training an embedding vector is no different. You now have 120 inputs instead of 12 but all you are doing is moving them around to see how you can minimize loss. And then you take the first 10 of those and that’s the vector corresponding to “h” and so on.

All the embedding vectors must of course be the same length, otherwise we would not have a way of entering all the character combinations into the network. E.g. “humpty dumpt” and in the next iteration “umpty dumpty” — in both cases we are entering 12 characters in the network and if each of the 12 characters was not represented by vectors of length 10 we won’t be able to reliably feed them all into a 120-long input layer. Let’s visualize these embedding vectors:

![Image 7: a diagram showing the different numbers of the number of rows](https://miro.medium.com/v2/resize:fit:421/1*lZOR8fNDEWHxUhLCSB-67A.png)

Image by author

Let’s call an ordered collection of same-sized vectors a matrix. This matrix above is called an **embedding matrix**. You tell it a column number corresponding to your letter and looking at that column in the matrix will give you the vector that you are using to represent that letter. This can be applied more generally for embedding any arbitrary collection of things — you would just need to have as many columns in this matrix as the things you have.

Subword Tokenizers
------------------

So far, we have been working with characters as the basic building blocks of language. This has its limitations. The neural network weights have to do a lot of the heavy lifting where they must make sense of certain sequences of characters (i.e. words) appearing next to each other and then next to other words. What if we directly assigned embeddings to words and made the network predict the next word. The network doesn’t understand anything more than numbers anyway, so we can assign a 10-length vector to each of the words “humpty”, “dumpty”, “sat”, “on” etc.. and then we just feed it two words and it can give us the next word. “**Token**” is the term for a single unit that we embed and then feed to the model. Our models so far were using characters as tokens, now we are proposing to use entire words as a token (you can of course use entire sentences or phrases as tokens if you like).

Using word tokenization has one profound effect on our model. There are more than 180K words in the English language. Using our output interpretation scheme of having a neuron per possible output we need hundreds of thousands of neurons in the output layer insead of the 26 or so. With the size of the hidden layers needed to achieve meaningful results for modern networks, this issue becomes less pressing. What is however worth noting is that since we are treating each word separately, and we are starting with a random number embeddings for each — very similar words (e.g. “cat” and “cats”) will start with no relationship. You would expect that embeddings for the two words should be close to each other — which undoubtedly the model will learn. But, can we somehow use this obvious similarity to get a jumpstart and simplify matters?

Yes we can. The most common embedding scheme in language models today is something where you break words down into subwords and then embed them. In the cat example, we would break down cats into two tokens “cat” and ”s”. Now it is easier for the model to understand the concept of “s” followed by other familiar words and so on. This also reduces the number of tokens we need ([sentencpiece](https://github.com/google/sentencepiece) is a common tokenizer with vocab size options in tens of thousands vs hundreds of thousands of words in english). A tokenizer is something that takes you input text (e.g. “Humpty Dumpt”) and splits it into the tokens and gives you the corresponding numbers that you need to look up the embedding vector for that token in the embedding matrix. For example, in case of “humpty dumpty” if we’re using character level tokenizer and we arranged our embedding matrix as in the picture above, then the tokenizer will first split humpty dumpt into characters \[‘h’,’u’,…’t’\] and then give you back the numbers \[8,21,…20\] because you need to look up the 8th column of the embedding matrix to get the embedding vector for ‘h’ (embedding vector is what you will feed into the model, not the number 8, unlike before). The arrangement of the columns in the matrix is completely irrelevant, we could assign any column to ‘h’ and as long as we look up the same vector every time we input ‘h’ we should be good. Tokenizers just give us an arbitrary (but fixed) number to make lookup easy. The main task we need them for really is splitting the sentence in tokens.

With embeddings and subword tokenization, a model could look something like this:

![Image 8: a diagram showing the different types of networks](https://miro.medium.com/v2/resize:fit:700/1*VGNZ1Zighiek1sAMdiZCaw.png)

Image by author

The next few sections deal with more recent advances in language modeling, and the ones that made LLMs as powerful as they are today. However, to understand these there are a few basic math concepts you need to know. Here are the concepts:

*   Matrices and matrix multiplication
*   General concept of functions in mathematics
*   Raising numbers to powers (e.g. a3 = a\*a\*a)
*   Sample mean, variance, and standard deviation

I have added summaries of these concepts in the appendix.

Self Attention
--------------

So far we have seen only one simple neural network structure (called feedforward network), one which contains a number of layers and each layer is fully connected to the next (i.e., there is a line connecting any two neurons in consecutive layers), and it is only connected to the next layer (e.g. no lines between layer 1 and layer 3 etc..). However, as you can imagine there is nothing stopping us from removing or making other connections. Or even making more complex structures. Let’s explore a particularly important structure: self-attention.

If you look at the structure of human language, the next word that we want to predict will depend on all the words before. However, they may depend on some words before them to a greater degree than others. For example, if we are trying to predict the next word in “Damian had a secret child, a girl, and he had written in his will that all his belongings, along with the magical orb, will belong to \_\_\_\_”. This word here could be “her” or “him” and it depends specifically on a much earlier word in the sentence: _girl/boy_.

The good news is, our simple feedforward model connects to all the words in the context, and so it can learn the appropriate weights for important words, But here’s the problem, the weights connecting specific positions in our model through feed forward layers are fixed (for every position). If the important word was always in the same position, it would learn the weights appropriately and we would be fine. However, the relevant word to the next prediction could be anywhere in the system. We could paraphrase that sentence above and when guessing “her vs his”, one very important word for this prediction would be boy/girl no matter where it appeared in that sentence. So, we need weights that depend not only on the position but also on the content in that position. How do we achieve this?

Self attention does something like adding up the embedding vectors for each of the words, but instead of directly adding them up it applies some weights to each. So if the embedding vectors for humpty,dumpty, sat are x1, x2, x3 respectively, then it will multiply each one with a weight (a number) before adding them up. Something like output = 0.5 x1 + 0.25 x2 + 0.25 x3 where output is the self-attention output. If we write the weights as u1, u2, u3 such that output = u1x1+u2x2+u3x3 then how do we find these weights u1, u2, u3?

Ideally, we want these weights to be dependent on the vector we are adding — as we saw some may be more important than others. But important to whom? To the word we are about to predict. So we also want the weights to depend on the word we are about to predict. Now that’s an issue, we of course don’t know the word we are about to predict before we predict it. So, self attention uses the word immediately preceding the word we are about to predict, i.e., the last word in the sentence available (I don’t really know why this and why not something else, but a lot of things in deep learning are trial and error and I suspect this works well).

Great, so we want weights for these vectors, and we want each weight to depend on the word that we are aggregating and word immediately preceding the one we are going to predict. Basically, we want a function u1 = F(x1, x3) where x1 is the word we will weight and x3 is the last word in the sequence we have (assuming we have only 3 words). Now, a straightforward way of achieving this is to have a vector for x1 (let’s call it k1) and a separate vector for x3 (let’s call it q3) and then simply take their dot product. This will give us a number and it will depend on both x1 and x3. How do we get these vectors k1 and q3? We build a tiny single layer neural network to go from x1 to k1 (or x2 to k2, x3 to k3 and so on). And we build another network going from x3 to q3 etc… Using our matrix notation, we basically come up with weight matrices Wk and Wq such that k1 = Wkx1 and q1 =Wqx1 and so on. Now we can take a dot product of k1 and q3 to get a scalar, so u1 = F(x1,x3) = Wkx1 **·** Wqx3.

One additional thing that happens in self-attention is that we don’t directly take the weighted sum of the embedding vectors themselves. Instead, we take the weighted sum of some “value” of that embedding vector, which is obtained by another small single layer network. What this means is similar to k1 and q1, we also now have a v1 for the word x1 and we obtain it through a matrix Wv such that v1=Wvx1. This v1 is then aggregated. So it all looks something like this if we only have 3 words and we are trying to predict the fourth:

![Image 9: self-adjusted outputs with a humpy](https://miro.medium.com/v2/resize:fit:700/1*oETLwMpxy3oH_B9pN-xLcg.png)

Self attention. Image by author

The plus sign represents a simple addition of the vectors, implying they have to have the same length. One last modification not shown here is that the scalars u1, u2, u3 etc.. won’t necessarily add up to 1. If we need them to be weights, we should make them add up. So we will apply a familiar trick here and use the softmax function.

This is self-attention. There is also cross-attention where you can have the q3 come from the last word, but the k’s and the v’s can come from another sentence altogether. This is for example valuable in translation tasks. Now we know what attention is.

This whole thing can now be put in a box and be called a “self attention block”. Basically, this self attention block takes in the embedding vectors and spits out a single output vector of any user-chosen length. This block has three parameters, Wk,Wq,Wv — it doesn’t need to be more complicated than that. There are many such blocks in the machine learning literature, and they are usually represented by boxes in diagrams with their name on it. Something like this:

![Image 10: a diagram showing the different types of blocks](https://miro.medium.com/v2/resize:fit:700/1*OgcRxWyftIXN8WbQw_-QKg.png)

Image by author

One of the things that you will notice with self-attention is that the position of things so far does not seem relevant. We are using the same W’s across the board and so switching Humpty and Dumpty won’t really make a difference here — all numbers will end up being the same. This means that while attention can figure out what to pay attention to, this won’t depend on word position. However, we do know that word positions are important in english and we can probably improve performance by giving the model some sense of a word’s position.

And so, when attention is used, we don’t often feed the embedding vectors directly to the self attention block. We will later see how “positional encoding” is added to embedding vectors before feeding to attention blocks.

_Note for the pre-initiated_: Those for whom this isn’t the first time reading about self-attention will note that we are not referencing any K and Q matrices, or applying masks etc.. That is because those things are implementation details arising out of how these models are commonly trained. A batch of data is fed and the model is simultaneously trained to predict dumpty from humpty, sat from humpty dumpty and so on. This is a matter of gaining efficiency and does not affect interpretation or even model outputs, and we have chosen to omit training efficiency hacks here.

Softmax
-------

We talked briefly about softmax in the very first note. Here’s the problem softmax is trying to solve: In our output interpretation we have as many neurons as the options from which we want the network to select one. And we said that we are going to interpret the network’s choice as the highest value neuron. Then we said we are going to calculate loss as the difference between the value that network provides, and an ideal value we want. But what’s that ideal value we want? We set it to 0.8 in the leaf/flower example. But why 0.8? Why no 5, or 10, or 10 million? The higher the better for that training example. Ideally we want infinity there! Now that would make the problem intractable — all loss would be infinite and our plan of minimizing loss by moving around parameters (remember “gradient descent”) fails. How do we deal with this?

One simple thing we can do is cap the values we want. Let’s say between 0 and 1? This would make all loss finite, but now we have the issue of what happens when the network overshoots. Let’s say it outputs (5,1) for (leaf,flower) in one case, and (0,1) in another. The first case made the right choice but the loss is worse! Ok, so now we need a way to also convert the outputs of the last layer in (0,1) range so that it preserves the order. We could use any function (a “**function**” in mathematics is simply a mapping of one number to another — in goes one number, out comes another — it’s rule based in terms of what will be output for a given input) here to get the job done. One possible option is the logistic function (see graph below) which maps all numbers to numbers between (0,1) and preserves the order:

![Image 11: linear function for h - i](https://miro.medium.com/v2/resize:fit:700/1*jSyo_owKB-tfTrPXV2giKg.png)

Image by author

Now, we have a number between 0 and 1 for each of the neurons in the last layer and we can calculate loss by setting the correct neuron to 1, others to 0 and taking the difference of that from what the network provides us. This will work, but can we do better?

Going back to our “Humpty dumpty” example, let’s say we are trying to generate dumpty character-by-character and our model makes a mistake when predicting “m” in dumpty. Instead of giving us the last layer with “m” as the highest value, it gives us “u” as the highest value but “m” is a close second.

Now we can continue with “duu” and try to predict next character and so on, but the model confidence will be low because there are not that many good continuations from “humpty duu..”. On the other hand, “m” was a close second, so we can also give “m” a shot, predict the next few characters, and see what happens? Maybe it gives us a better overall word?

So what we are talking about here is not just blindly selecting the max value, but trying a few. What’s a good way to do it? Well we have to assign a chance to each one — say we will pick the top one with 50%, second one with 25% and so on. That’s a good way to do it. But maybe we would want the chance to be dependent on the underlying model predictions. If the model predicts values for m and u to be really close to each other here (compared to other values) — then maybe a close 50–50 chance of exploring the two is a good idea?

So we need a nice rule that takes all these numbers and converts them into chances. That’s what softmax does. It is a generalization of the logistic function above but with additional features. If you give it 10 arbitrary numbers — it will give you 10 outputs, each between 0 and 1 and importantly, all 10 adding up to 1 so that we can interpret them as chance. You will find softmax as the last layer in nearly every language model.

Residual connections
--------------------

We have slowly changed our visualization of networks as the sections progress. We are now using boxes/blocks to denote certain concepts. This notation is useful in denoting a particularly useful concept of residual connections. Let’s look at residual connection combined with a self-attention block:

![Image 12: a diagram of a self-blocking system](https://miro.medium.com/v2/resize:fit:700/1*270MXDfslVtvmBjShHL2hQ.png)

A residual connection. Image by author

Note that we put “Input” and “Output” as boxes to make things simpler, but these are still basically just a collection of neurons/numbers same as shown above.

So what’s going on here? We are basically taking the output of self-attention block and before passing it to the next block, we are adding to it the original Input. First thing to note is that this would require that the dimensions of the self-attention block output must now be the same as that of the input. This is not a problem since as we noted the self-attention output is determined by the user. But why do this? We won’t get into all the details here but the key thing is that as networks get deeper (more layers between input and output) it gets increasingly harder to train them. Residual connections have been shown to help with these training challenges.

Layer Normalization
-------------------

Layer normalization is a fairly simple layer that takes the data coming into the layer and normalizes it by subtracting the mean and dividing it by standard deviation (maybe a bit more, as we see below). For example, if we were to apply layer normalization immediately after the input, it would take all the neurons in the input layer and then it would calculate two statistics: their mean and their standard deviation. Let’s say the mean is M and the standard deviation is S then what layer norm is doing is taking each of these neurons and replacing it with (x-M)/S where x denotes any given neuron’s original value.

Now how does this help? It basically stabilizes the input vector and helps with training deep networks. One concern is that by normalizing inputs, are we removing some useful information from them that may be helpful in learning something valuable about our goal? To address this, the layer norm layer has a scale and a bias parameter. Basically, for each neuron you just multiply it with a scalar and then add a bias to it. These scalar and bias values are parameters that can be trained. This allows the network to learn some of the variation that may be valuable to the predictions. And since these are the only parameters, the LayerNorm block doesn’t have a lot of parameters to train. The whole thing looks something like this:

![Image 13: a diagram of a layer nomination block](https://miro.medium.com/v2/resize:fit:700/1*Zd-PvX2cYslEyrjL6MVnzA.png)

Layer Normalization. Image by author

The Scale and Bias are trainable parameters. You can see that layer norm is a relatively simple block where each number is only operated on pointwise (after the initial mean and std calculation). Reminds us of the activation layer (e.g. RELU) with the key difference being that here we have some trainable parameters (albeit lot fewer than other layers because of the simple pointwise operation).

Standard deviation is a statistical measure of how spread out the values are, e.g., if the values are all the same you would say the standard deviation is zero. If, in general, each value is really far from the mean of these very same values, then you will have a high standard deviation. The formula to calculate standard deviation for a set of numbers, a1, a2, a3…. (say N numbers) goes something like this: subtract the mean (of these numbers) from each of the numbers, then square the answer for each of N numbers. Add up all these numbers and then divide by N. Now take a square root of the answer.

Note for the pre-initiated: Experienced ML professionals will note that there is no discussion of batch norm here. In-fact, we haven’t even introduced the concept of batches in this article at all. For the most part, I believe batches are another training accelerant not related to the understanding of core concepts (except perhaps batch norm which we do not need here).

Dropout
-------

Dropout is a simple but effective method to avoid model overfitting. Overfitting is a term for when you train the model on your training data, and it works well on that dataset but does not generalize well to the examples the model has not seen. Techniques that help us avoid overfitting are called “**regularization techniques**”, and dropout is one of them.

If you train a model, it might make errors on the data and/or overfit it in a particular way. If you train another model, it might do the same, but in a different way. What if you trained a number of these models and averaged the outputs? These are typically called “**ensemble** **models**” because they predict the outputs by combining outputs from an ensemble of models, and ensemble models generally perform better than any of the individual models.

In neural networks, you could do the same. You could build multiple (slightly different) models and then combine their outputs to get a better model. However, this can be computationally expensive. Dropout is a technique that doesn’t quite build ensemble models but does capture some of the essence of the concept.

The concept is simple, by inserting a dropout layer during training what you are doing is randomly deleting a certain percentage of the direct neuron connections between the layers that dropout is inserted. Considering our initial network and inserting a Dropout layer between the input and the middle layer with 50% dropout rate can look something like this:

![Image 14: a diagram of a sunflower and a sunflower](https://miro.medium.com/v2/resize:fit:700/1*j0oKuXvH7kfrIpIfXE03VA.png)

![Image 15: a diagram showing the arrow pointing to the right](https://miro.medium.com/v2/resize:fit:700/1*UodvtsDn5z73Cp578XOoVw.png)

![Image 16: a diagram of a sunflower and its leaves](https://miro.medium.com/v2/resize:fit:700/1*qHPSwQmV3sfvKT5pG4TEJw.png)

Image by author

Now, this forces the network to train with a lot of redundancy. Essentially, you are training a number of different models at the same time — but they share weights.

Now for making inferences, we could follow the same approach as an ensemble model. We could make multiple predictions using dropouts and then combine them. However, since that is computationally intensive — and since our models share common weights — why don’t we just do a prediction using all the weights (so instead of using 50% of the weights at a time we use all at the same time). This should give us some approximation of what an ensemble will provide.

One issue though: the model trained with 50% of the weights will have very different numbers in the middle neurons than one using all the weights. What we want is more ensemble style averaging here. How do we do this? Well, a simple way is to simply take all the weights and multiply them by 0.5 since we are now using twice as many weights. This is what Droput does during inference. It will use the full network with all the weights and simply multiply the weights with (1- p) where p is the deletion probability. And this has been shown to work rather well as a regularization technique.

Multi-head Attention
--------------------

This is the key block in the transformer architecture. We’ve already seen what an attention block is. Remember that the output of an attention block was determined by the user and it was the length of v’s. What a multi-attention head is basically you run several attention heads in parallel (they all take the same inputs). Then we take all their outputs and simply concatenate them. It looks something like this:

![Image 17: a diagram showing the different types of data](https://miro.medium.com/v2/resize:fit:700/1*BmZd8SIDEQu7r5_R7y54kQ.png)

Multi-head attention. Image by author

Keep in mind the arrows going from v1 -\> v1h1 are linear layers — there’s a matrix on each arrow that transforms. I just did not show them to avoid clutter.

What is going on here is that we are generating the same key, query and values for each of the heads. But then we are basically applying a linear transformation on top of that (separately to each k,q,v and separately for each head) before we use those k,q,v values. This extra layer did not exist in self attention.

A side note is that to me, this is a slightly surprising way of creating a multi-headed attention. For example, why not create separate Wk,Wq,Wv matrices for each of the heads rather than adding a new layer and sharing these weights. Let me know if you know — I really have no idea.

Positional encoding and embedding
---------------------------------

We briefly talked about the motivation for using positional encoding in the self-attention section. What are these? While the picture shows positional encoding, using a positional embedding is more common than using an encoding. As such we talk about a common positional embedding here but the appendix also covers positional encoding used in the original paper. A positional embedding is no different than any other embedding except that instead of embedding the word vocabulary we will embed numbers 1, 2, 3 etc. So this embedding is a matrix of the same length as word embedding, and each column corresponds to a number. That’s really all there is to it.

The GPT architecture
--------------------

Let’s talk about the GPT architecture. This is what is used in most GPT models (with variation across). If you have been following the article thus far, this should be fairly trivial to understand. Using the box notation, this is what the architecture looks like at high level:

![Image 18: a diagram of a process for a transducer](https://miro.medium.com/v2/resize:fit:700/0*U9mQKCWiyakNVwxU)

The GPT Architecture. Image by author

At this point, other than the “GPT Transformer Block” all the other blocks have been discussed in great detail. The + sign here simply means that the two vectors are added together (which means the two embeddings must be the same size). Let’s look at this GPT Transformer Block:

![Image 19: the transformation book for gtf](https://miro.medium.com/v2/resize:fit:700/1*Mq4hBZcKPL9GALPSSQG9Xg.png)

And that’s pretty much it. It is called “transformer” here because it is derived from and is a type of transformer — which is an architecture we will look at in the next section. This doesn’t affect understanding as we’ve already covered all the building blocks shown here before. Let’s recap everything we’ve covered so far building up to this GPT architecture:

*   We saw how neural nets take numbers and output other numbers and have weights as parameters which can be trained
*   We can attach interpretations to these input/output numbers and give real world meaning to a neural network
*   We can chain neural networks to create bigger ones, and we can call each one a “block” and denote it with a box to make diagrams easier. Each block still does the same thing, take in a bunch of numbers and output other bunch of numbers
*   We learned a lot of different types of blocks that serve different purposes
*   GPT is just a special arrangement of these blocks that is shown above with an interpretation that we discussed in Part 1

Modifications have been made over time to this as companies have built up to powerful modern LLMs, but the basic remains the same.

Now, this GPT transformer is actually what is called a “decoder” in the original transformer paper that introduced the transformer architecture. Let’s take a look at that.

The transformer architecture
----------------------------

This is one of the key innovations driving rapid acceleration in the capabilities of language models recently. Transformers not only improved the prediction accuracy, they are also easier/more efficient than previous models (to train), allowing for larger model sizes. This is what the GPT architecture above is based on.

If you look at GPT architecture, you can see that it is great for generating the next word in the sequence. It fundamentally follows the same logic we discussed in Part 1. Start with a few words and then continue generating one at a time. But, what if you wanted to do translation. What if you had a sentence in german (e.g. “Wo wohnst du?” = “Where do you live?”) and you wanted to translate it to english. How would we train the model to do this?

Well, first thing we would need to do is figure out a way to input german words. Which means we have to expand our embedding to include both german and english. Now, I guess here is a simply way of inputting the information. Why don’t we just concatenate the german sentence at the beginning of whatever so far generated english is and feed it to the context. To make it easier for the model, we can add a separator. This would look something like this at each step:

![Image 20: a diagram showing the different ways to say the word](https://miro.medium.com/v2/resize:fit:700/1*psIz3-v2dMfI3SMsFQjRPQ.png)

Image by author

This will work, but it has room for improvement:

*   If the context length is fixed, sometimes the original sentence is lost
*   The model has a lot to learn here. Two languages simultaneously, but also to know that <SEP\> is the separator token where it needs to start translating
*   You are processing the entire german sentence, with different offsets, for each word generation. This means there will be different internal representations of the same thing and the model should be able to work through it all for translation

Transformer was originally created for this task and consists of an “encoder” and a “decoder” — which are basically two separate blocks. One block simply takes the german sentence and gives out an intermediate representation (again, bunch of numbers, basically) — this is called the encoder.

The second block generates words (we’ve seen a lot of this so far). The only difference is that in addition to feeding it the words generated so far we also feed it the encoded german (from the encoder block) sentence. So as it is generating language, it’s context is basically all the words generated so far, plus the german. This block is called the decoder.

Each of these encoders and decoders consist of a few blocks, notably the attention block sandwiched between other layers. Let’s look at the illustration of a transformer from the paper “Attention is all you need” and try to understand it:

![Image 21: a diagram showing the process of a video processing system](https://miro.medium.com/v2/resize:fit:683/1*uPwJ24na4D_ECHBv1Lg5Fg.png)

Image from Vaswani et al. (2017)

The vertical set of blocks on the left is called the “encoder” and the ones to the right is called the “decoder”. Let’s go over and understand anything that we have not already covered before:

_Recap on how to read the diagram:_ Each of the boxes here is a block that takes in some inputs in the form of neurons, and spits out a set of neurons as output that can then either be processed by the next block or interpreted by us. The arrows show where the output of a block is going. As you can see, we will often take the output of one block and feed it in as input into multiple blocks. Let’s go through each thing here:

Feed forward: A feedforward network is one that does not contain cycles. Our original network in section 1 is a feed forward. In-fact, this block uses very much the same structure. It contains two linear layers, each followed by a RELU (see note on RELU in first section) and a dropout layer. Keep in mind that this feedforward neetwork applies to each position independently. What this means is that the information on position 0 has a feedforward network, and on position 1 has one and so on.. But the neurons from position x do not have a linkage to the feedforward network of position y. This is important because if we did not do this, it would allow the network to cheat during training time by looking forward.

_Cross-attention:_ You will notice that the decoder has a multi-head attention with arrows coming from the encoder. What is going on here? Remember the value, key, query in self-attention and multi-head attention? They all came from the same sequence. The query was just from the last word of the sequence in-fact. So what if we kept the query but fetched the value and key from a completely different sequence altogether? That is what is happening here. The value and key come from the output of the encoder. Nothing has changed mathematically except where the inputs for key and value are coming from now.

_Nx_: The Nx here simply represents that this block is chain-repeated N times. So basically you are stacking the block back-to-back and passing the input from the previous block to the next one. This is a way to make the neural network deeper. Now, looking at the diagram there is room for confusion about how the encoder output is fed to the decoder. Let’s say N=5. Do we feed the output of each encoder layer to the corresponding decoder layer? No. Basically you run the encoder all the way through once and only once. Then you just take that representation and feed the same thing to every one of the 5 decoder layers.

_Add & Norm block_: This is basically the same as below (guess the authors were just trying to save space)

![Image 22: layer norm diagram](https://miro.medium.com/v2/resize:fit:681/0*sXvYIassJutgqw5W)

Image by author

Everything else has already been discussed. Now you have a complete explanation of the transformer architecture building up from simple sum and product operations and fully self contained! You know what every line, every sum, every box and word means in terms of how to build them from scratch. Theoretically, these notes contain what you need to code up the transformer from scratch. In-fact, if you are interested [this repo](https://github.com/karpathy/nanoGPT) does that for the GPT architecture above.

Appendix
--------

Matrix Multiplication
---------------------

We introduced vectors and matrices above in the context of embeddings. A matrix has two dimensions (number or rows and columns). A vector can also be thought of as a matrix where one of the dimensions equals one. Product of two matrices is defined as:

![Image 23: a diagram showing the structure of a dna](https://miro.medium.com/v2/resize:fit:700/0*woel5Da5Z22EmiGx)

Image by author

Dots represent multiplication. Now let’s take a second look at the calculation of blue and organic neurons in the very first picture. If we write the weights as a matrix and the inputs as vectors, we can write the whole operation in the following way:

![Image 24: a diagram showing the number of numbers in a matrix](https://miro.medium.com/v2/resize:fit:466/0*yn1TPuxw_QqnD93k)

Image by author

If the weight matrix is called “W” and the inputs are called “x” then Wx is the result (the middle layer in this case). We can also transpose the two and write it as xW — this is a matter of preference.

Standard deviation
------------------

We use the concept of standard deviation in the Layer Normalization section. Standard deviation is a statistical measure of how spread out the values are (in a set of numbers), e.g., if the values are all the same you would say the standard deviation is zero. If, in general, each value is really far from the mean of these very same values, then you will have a high standard deviation. The formula to calculate standard deviation for a set of numbers, a1, a2, a3…. (say N numbers) goes something like this: subtract the mean (of these numbers) from each of the numbers, then square the answer for each of N numbers. Add up all these numbers and then divide by N. Now take a square root of the answer.

Positional Encoding
-------------------

We talked about positional embedding above. A positional encoding is simply a vector of the same length as the word embedding vector, except it is not an embedding in the sense that it is not trained. We simply assign a unique vector to every position e.g. a different vector for position 1 and different one for position 2 and so on. A simple way of doing this is to make the vector for that position simply full of the position number. So the vector for position 1 would be \[1,1,1…1\] for 2 would be \[2,2,2…2\] and so on (remember length of each vector must match embedding length for addition to work). This is problematic because we can end up with large numbers in vectors which creates challenges during training. We can, of course, normalize these vectors by dividing every number by the max of position, so if there are 3 words total then position 1 is \[.33,.33,..,.33\] and 2 is \[.67, .67, ..,.67\] and so on. This has the problem now that we are constantly changing the encoding for position 1 (those numbers will be different when we feed 4 word sentence as input) and it creates challenges for the network to learn. So here, we want a scheme that allocates a unique vector to each position, and the numbers don’t explode. Basically if the context length is d (i.e., maximum number of tokens/words that we can feed into the network for predicting next token/word, see discussion in “how does it all generate language?” section) and if the length of the embedding vector is 10 (say), then we need a matrix with 10 rows and d columns where all the columns are unique and all the numbers lie between 0 and 1. Given that there are infinitely many numbers between zero and 1, and the matrix is finitely sized, this can be done in many ways.

The approach used in the “Attention is all you need” paper goes something like this:

*   Draw 10 sin curves each being si(p) = sin (p/10000(i/d)) (that’s 10k to power i/d)
*   Fill the encoding matrix with numbers such that (i,p)th number is si(p), e.g., for position 1 the 5th element of the encoding vector is s5(1)=sin (1/10000(5/d))

Why choose this method? By changing the power on 10k you are changing the amplitude of the sine function when viewed on the p-axis. And if you have 10 different sine functions with 10 different amplitudes, then it will be a long time before you get a repetition (i.e. all 10 values are the same) for changing values of p. And this helps give us unique values. Now, the actual paper uses both sine and cosine functions and the form of encoding is: si(p) = sin (p/10000(i/d)) if i is even and si(p) = cos(p/10000(i/d)) if i is odd.


## Visual Content Analysis

### Image Analysis
Title: LLMs from Scratch Using Middle School Math | Towards Data Science

URL Source: https://medium.com/towards-data-science/understanding-llms-from-scratch-using-middle-school-math-e602d27ec876

Markdown Content:
A self-contained, full explanation to inner workings of an LLM
--------------------------------------------------------------

[![Image 1: Rohit Patel](https://miro.medium.com/v2/resize:fill:88:88/1*ECmWr6Z-ToM5JE-h8ywyLQ.jpeg)](https://rohit-patel.medium.com/?source=post_page---byline--e602d27ec876--------------------------------)

In this article, we talk about how Large Language Models (LLMs) work, from scratch — assuming only that you know how to add and multiply two numbers. The article is meant to be fully self-contained. We start by building a simple Generative AI on pen and paper, and then walk through everything we need to have a firm understanding of modern LLMs and the Transformer architecture. The article will strip out all the fancy language and jargon in ML and represent everything simply as they are: numbers. We will still call out what things are called to tether your thoughts when you read jargon-y content.

Going from addition/multiplication to the most advanced AI models today without assuming other knowledge or referring to other sources means we cover a LOT of ground. This is NOT a toy LLM explanation — a determined person can theoretically recreate a modern LLM from all the information here. I have cut out every word/line that was unnecessary and as such this article isn’t really meant to be browsed.

What will we cover?
-------------------

1.  A simple neural network
2.  How are these models trained?
3.  How does all this generate language?
4.  What makes LLMs work so well?
5.  Embeddings
6.  Sub-word tokenizers
7.  Self-attention
8.  Softmax
9.  Residual connections
10.  Layer Normalization
11.  Dropout
12.  Multi-head attention
13.  Positional embeddings
14.  The GPT architecture
15.  The transformer architecture

Let’s dive in.

The first thing to note is that neural networks can only take numbers as inputs and can only output numbers. No exceptions. The art is in figuring out how to feed your inputs as numbers, interpreting the output numbers in a way that achieves your goals. And finally, building neural nets that will take the inputs you provide and give you the outputs you want (given the interpretation you chose for these outputs). Let’s walk through how we get from adding and multiplying numbers to things like [Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/).

A simple neural network:
------------------------

Let’s work through a simple neural network that can classify an object:

*   **Object data available:** Dominant color (RGB) & Volume (in milli-liters)
*   **Classify into**: Leaf OR Flower

Here’s what the data for a leaf and a sunflower can look like:

![Image 3: a table showing the number of leaves and flowers](https://miro.medium.com/v2/resize:fit:700/1*ymWXxVf7N4-Ps-62Cih2XQ.png)

Image by author

Let’s now build a neural net that does this classification. We need to decide on input/output interpretations. Our inputs are already numbers, so we can feed them directly into the network. Our outputs are two objects, leaf and flower which the neural network cannot output. Let’s look at a couple of schemes we can use here:

*   We can make the network output a single number. And if the number is positive we say it’s a leaf and if it is negative we say it’s a flower
*   OR, we can make the network output two numbers. We interpret the first one as a number for leaf and second one as the number for flower and we will say that the selection is whichever number is larger

Both schemes allow the network to output number(s) that we can interpret as leaf or flower. Let’s pick the second scheme here because it generalizes well to other things we will look at later. And here’s a neural network that does the classification using this scheme. Let’s work through it:

![Image 4: a sunflower with a number of sunflowers](https://miro.medium.com/v2/resize:fit:700/1*D-e4rt_QBPp1fMY5OseJiQ.png)

Image by author

Blue circle like so: (32 \* 0.10) **+** (107 \* -0.29) **+** (56 \* -0.07) **+** (11.2 \* 0.46) = **— 26.6**

Some jargon:

**_Neurons/nodes_**: The numbers in the circles

**_Weights_**: The colored numbers on the lines

**_Layers_**: A collection of neurons is called a layer. You could think of this network as having 3 layers: Input layer with 4 neurons, Middle layer with 3 neurons, and the Output layer with 2 neurons.

To calculate the prediction/output from this network (called a “**forward pass**”), you start from the left. We have the data available for the neurons in the Input layer. To move “forward” to the next layer, you multiply the number in the circle with the weight for the corresponding neuron pairing and you add them all up. We demonstrate blue and orange circle math above. Running the whole network we see that the first number in the output layer comes out higher so we interpret it as “network classified these (RGB,Vol) values as leaf”. A well trained network can take various inputs for (RGB,Vol) and correctly classify the object.

The model has no notion of what a leaf or a flower is, or what (RGB,Vol) are. It has a job of taking in exactly 4 numbers and giving out exactly 2 numbers. It is our interpretation that the 4 input numbers are (RGB,Vol) and it is also our decision to look at the output numbers and infer that if the first number is larger it’s a leaf and so on. And finally, it is also up to us to choose the right weights such that the model will take our input numbers and give us the right two numbers such that when we interpret them we get the interpretation we want.

An interesting side effect of this is that you can take the same network and instead of feeding RGB,Vol feed other 4 numbers like cloud cover, humidity etc.. and interpret the two numbers as “Sunny in an hour” or “Rainy in an hour” and then if you have the weights well calibrated you can get the exact same network to do two things at the same time — classify leaf/flower and predict rain in an hour! The network just gives you two numbers, whether you interpret it as classification or prediction or something else is entirely up to you.

Stuff left out for simplification (feel free to ignore without compromising comprehensibility):

*   **Activation layer**: A critical thing missing from this network is an “activation layer”. That’s a fancy word for saying that we take the number in each circle and apply a nonlinear function to it (**RELU** is a common function where you just take the number and set it to zero if it is negative, and leave it unchanged if it is positive). So basically in our case above, we would take the middle layer and replace the two numbers (-26.6 and -47.1) with zeros before we proceed further to the next layer. Of course, we would have to re-train the weights here to make the network useful again. Without the activation layer all the additions and multiplications in the network can be collapsed to a single layer. In our case, you could write the green circle as the sum of RGB directly with some weights and you would not need the middle layer. It would be something like (0.10 \* -0.17 + 0.12 \* 0.39–0.36 \* 0.1) \* R + (-0.29 \* -0.17–0.05 \* 0.39–0.21 \* 0.1) \* G …and so on. This is usually not possible if we have a nonlinearity there. This helps networks deal with more complex situations.
*   **Bias:** Networks will usually also contain another number associated with each node, this number is simply added to the product to calculate the value of the node and this number is called the “bias”. So if the bias for the top blue node was 0.25 then the value in the node would be: (32 \* 0.10) + (107 \* -0.29) + (56 \* -0.07) + (11.2 \* 0.46) **\+ 0.25** \= — 26.35. The word parameters is usually used to refer to all these numbers in the model that are not neurons/nodes.
*   **Softmax:** We don’t usually interpret the output layer directly as shown in our models. We convert the numbers into probabilities (i.e. make it so that all numbers are positive and add up to 1). If all the numbers in the output layer were already positive one way you could achieve this is by dividing each number by the sum of all numbers in the output layer. Though a “softmax” function is normally used which can handle both positive and negative numbers.

How are these models trained?
-----------------------------

In the example above, we magically had the weights that allowed us to put data into the model and get a good output. But how are these weights determined? The process of setting these weights (or “parameters”) is called “**training the model**”, and we need some training data to train the model.

Let’s say we have some data where we have the inputs and we already know if each input corresponds to leaf or flower, this is our “**training data**” and since we have the leaf/flower label for each set of (R,G,B,Vol) numbers, this is “**labeled data**”.

Here’s how it works:

*   Start with a random numbers, i.e. set each parameter/weight to a random number
*   Now, we know that when we input the data corresponding to the leaf (R=32, G=107, B=56, Vol=11.2). Suppose we want a larger number for leaf in the output layer. Let’s say we want the number corresponding to leaf as 0.8 and the one corresponding to flower as 0.2 (as shown in example above, but these are illustrative numbers to demonstrate training, in reality we would not want 0.8 and 0.2. In reality these would be probabilities, which they are not here, and we would them to be 1 and 0)
*   We know the numbers we want in the output layer, and the numbers we are getting from the randomly selected parameters (which are different from what we want). So for all the neurons in the output layer, let’s take the difference between the number we want and the number we have. Then add up the differences. E.g., if the output layer is 0.6 and 0.4 in the two neurons, then we get: (0.8–0.6)=0.2 and (0.2–0.4)= -0.2 so we get a total of 0.4 (ignoring minus signs before adding). We can call this our “**loss**”. Ideally we want the loss to be close to zero, i.e. we want to “**minimize the loss**”.
*   Once we have the loss, we can slightly change each parameter to see if increasing or decreasing it will increase the loss or decrease it. This is called the “**gradient**” of that parameter. Then we can move each of the parameters by a small amount in the direction where the loss goes down (the direction of the gradient). Once we have moved all the parameters slightly, the loss should be lower
*   Keep repeating the process and you will reduce the loss, and eventually have a set of weights/parameters that are “**trained**”. This whole process is called “**gradient descent**”.

Couple of notes:

*   You often have multiple training examples, so when you change the weights slightly to minimize the loss for one example it might make the loss worse for another example. The way to deal with this is to define loss as average loss over all the examples and then take gradient over that average loss. This reduces the average loss over the entire training data set. Each such cycle is called an “**epoch**”. Then you can keep repeating the epochs thus finding weights that reduce average loss.
*   We don’t actually need to “move weights around” to calculate the gradient for each weight — we can just infer it from the formula (e.g. if the weight is 0.17 in the last step, and the value of neuron is positive, and we want a larger number in output we can see that increasing this number to 0.18 will help).

In practice, training deep networks is a hard and complex process because gradients can easily spiral out of control, going to zero or infinity during training (called “vanishing gradient” and “exploding gradient” problems). The simple definition of loss that we talked about here is perfectly valid, but rarely used as there are better functional forms that work well for specific purposes. With modern models containing billions of parameters, training a model requires massive compute resources which has its own problems (memory limitations, parallelization etc.)

How does all this help generate language?
-----------------------------------------

Remember, neural nets take in some numbers, do some math based on the trained parameters, and give out some other numbers. Everything is about interpretation and training the parameters (i.e. setting them to some numbers). If we can interpret the two numbers as “leaf/flower” or “rain or sun in an hour”, we can also interpret them as “next character in a sentence”.

But there are more than 2 letters in English, and so we must expand the number of neurons in the output layer to, say, the 26 letters in the English language (let’s also throw in some symbols like space, period etc..). Each neuron can correspond to a character and we look at the (26 or so) neurons in the output layer and say that the character corresponding to the highest numbered neuron in the output layer is the output character. Now we have a network that can take some inputs and output a character.

What if we replace the input in our network with these characters: “Humpty Dumpt” and asked it to output a character and interpreted it as the “Network’s suggestion of the next character in the sequence that we just entered”. We can probably set the weights well enough for it to output “y” — thereby completing “Humpty Dumpty”. Except for one problem, how do we input these lists of characters in the network? Our network only accepts numbers!!

One simple solution is to assign a number to each character. Let’s say a=1, b=2 and so on. Now we can input “humpty dumpt” and train it to give us “y”. Our network looks something like this:

![Image 5: a diagram showing the different types of networks](https://miro.medium.com/v2/resize:fit:700/1*XPyJ-V0vbPv6EDwFpk7KYQ.png)

Image by author

Ok, so now we can predict one character ahead by providing the network a list of characters. We can use this fact to build a whole sentence. For example, once we have the “y” predicted, we can append that “y” to the list of characters we have and feed it to the network and ask it to predict the next character. And if well trained it should give us a space, and so on and so forth. By the end, we should be able to recursively generate “Humpty Dumpty sat on a wall”. We have Generative AI. Moreover, **_we now have a network capable of generating language!_** Now, nobody ever actually puts in randomly assigned numbers and we will see more sensible schemes down the line. If you cannot wait, feel free to check out the one-hot encoding section in the appendix.

Astute readers will note that we can’t actually input “Humpty Dumpty” into the network since the way the diagram is, it only has 12 neurons in the input layer one for each character in “humpty dumpt” (including the space). So how can we put in the “y” for the next pass. Putting a 13th neuron there would require us to modify the entire network, that’s not workable. The solution is simple, let’s kick the “h” out and send the 12 most recent characters. So we would be sending “umpty dumpty” and the network will predict a space. Then we would input “mpty dumpty “ and it will produce an s and so on. It looks something like this:

![Image 6: a diagram showing the different types of inputs](https://miro.medium.com/v2/resize:fit:700/1*0_tSCfEAL9NIK8U95Q-6Vg.png)

Image by author

We’re throwing away a lot of information in the last line by feeding the model only “ sat on the wal”. So what do the latest and greatest networks of today do? More or less exactly that. The length of inputs we can put into a network is fixed (determined by the size of the input layer). This is called “context length” — the context that is provided to the network to make future predictions. Modern networks can have very large context lengths (several thousand words) and that helps. There are some ways of inputting infinite length sequences but the performance of those methods, while impressive, has since been surpassed by other models with large (but fixed) context length.

One other thing careful readers will notice is that we have different interpretations for inputs and outputs for the same letters! For example, when inputting “h” we are simply denoting it with the number 8 but on the output layer we are not asking the model to output a single number (8 for “h”, 9 for “i” and so on..) instead we are are asking the model to output 26 numbers and then we see which one is the highest and then if the 8th number is highest we interpret the output as “h”. Why don’t we use the same, consistent, interpretation on both ends? We could, it’s just that in the case of language, freeing yourself to choose between different interpretations gives you a better chance of building better models. And it just so happens that the most effective currently known interpretations for the input and output are different. In-fact, the way we are inputting numbers in this model is not the best way to do it, we will look at better ways to do that shortly.

What makes large language models work so well?
----------------------------------------------

Generating “Humpty Dumpty sat on a wall” character-by-character is a far cry from what modern LLMs can do. There are a number of differences and innovations that get us from the simple generative AI that we discussed above to the human-like bot. Let’s go through them:

Embeddings
----------

Remember we said that the way that we are inputting characters into the model isn’t the best way to do it. We just arbitrarily selected a number for each character. What if there were better numbers we could assign that would make it possible for us to train better networks? How do we find these better numbers? Here’s a clever trick:

When we trained the models above, the way we did it was by moving around weights and seeing that gives us a smaller loss in the end. And then slowly and recursively changing the weights. At each turn we would:

*   Feed in the inputs
*   Calculate the output layer
*   Compare it to the output we ideally want and calculate the average loss
*   Adjust the weights and start again

In this process, the inputs are fixed. This made sense when inputs were (RGB, Vol). But the numbers we are putting in now for a,b,c etc.. are arbitrarily picked by us. What if at every iteration in addition to moving the weights around by a bit we also moved the input around and see if we can get a lower loss by using a different number to represent “a” and so on? We are definitely reducing the loss and making the model better (that’s the direction we moved a’s input in, by design). Basically, apply gradient descent not just to the weights but also the number representations for the inputs since they are arbitrarily picked numbers anyway. This is called an “**embedding**”. It is a mapping of inputs to numbers, and as you just saw, it needs to be trained. The process of training an embedding is much like that of training a parameter. One big advantage of this though is that once you train an embedding you can use it in another model if you wish. Keep in mind that you will consistently use the same embedding to represent a single token/character/word.

We talked about embeddings that are just one number per character. However, in reality embeddings have more than one number. That’s because it is hard to capture the richness of concept by a single number. If we look at our leaf and flower example, we have four numbers for each object (the size of the input layer). Each of these four numbers conveyed a property and the model was able to use all of them to effectively guess the object. If we had only one number, say the red channel of the color, it might have been a lot harder for the model. We’re trying to capture human language here — we’re going to need more than one number.

So instead of representing each character by a single number, maybe we can represent it by multiple numbers to capture the richness? Let’s assign a bunch of numbers to each character. Let’s call an ordered collection of numbers a “vector” (ordered as in each number has a position, and if we swap position of two numbers it gives us a different vector. This was the case with our leaf/flower data, if we swapped the R and G numbers for the leaf, we would get a different color, it would not be the same vector anymore). The length of a vector is simply how many numbers it contains. We’ll assign a vector to each character. Two questions arise:

*   If we have a vector assigned to each character instead of a number, how do we now feed “humpty dumpt” to the network? The answer is simple. Let’s say we assigned a vector of 10 numbers to each character. Then instead of the input layer having 12 neurons we would just put 120 neurons there since each of the 12 characters in “humpty dumpt” has 10 numbers to input. Now we just put the neurons next to each other and we are good to go
*   How do we find these vectors? Thankfully, we just learned how to train embedding numbers. Training an embedding vector is no different. You now have 120 inputs instead of 12 but all you are doing is moving them around to see how you can minimize loss. And then you take the first 10 of those and that’s the vector corresponding to “h” and so on.

All the embedding vectors must of course be the same length, otherwise we would not have a way of entering all the character combinations into the network. E.g. “humpty dumpt” and in the next iteration “umpty dumpty” — in both cases we are entering 12 characters in the network and if each of the 12 characters was not represented by vectors of length 10 we won’t be able to reliably feed them all into a 120-long input layer. Let’s visualize these embedding vectors:

![Image 7: a diagram showing the different numbers of the number of rows](https://miro.medium.com/v2/resize:fit:421/1*lZOR8fNDEWHxUhLCSB-67A.png)

Image by author

Let’s call an ordered collection of same-sized vectors a matrix. This matrix above is called an **embedding matrix**. You tell it a column number corresponding to your letter and looking at that column in the matrix will give you the vector that you are using to represent that letter. This can be applied more generally for embedding any arbitrary collection of things — you would just need to have as many columns in this matrix as the things you have.

Subword Tokenizers
------------------

So far, we have been working with characters as the basic building blocks of language. This has its limitations. The neural network weights have to do a lot of the heavy lifting where they must make sense of certain sequences of characters (i.e. words) appearing next to each other and then next to other words. What if we directly assigned embeddings to words and made the network predict the next word. The network doesn’t understand anything more than numbers anyway, so we can assign a 10-length vector to each of the words “humpty”, “dumpty”, “sat”, “on” etc.. and then we just feed it two words and it can give us the next word. “**Token**” is the term for a single unit that we embed and then feed to the model. Our models so far were using characters as tokens, now we are proposing to use entire words as a token (you can of course use entire sentences or phrases as tokens if you like).

Using word tokenization has one profound effect on our model. There are more than 180K words in the English language. Using our output interpretation scheme of having a neuron per possible output we need hundreds of thousands of neurons in the output layer insead of the 26 or so. With the size of the hidden layers needed to achieve meaningful results for modern networks, this issue becomes less pressing. What is however worth noting is that since we are treating each word separately, and we are starting with a random number embeddings for each — very similar words (e.g. “cat” and “cats”) will start with no relationship. You would expect that embeddings for the two words should be close to each other — which undoubtedly the model will learn. But, can we somehow use this obvious similarity to get a jumpstart and simplify matters?

Yes we can. The most common embedding scheme in language models today is something where you break words down into subwords and then embed them. In the cat example, we would break down cats into two tokens “cat” and ”s”. Now it is easier for the model to understand the concept of “s” followed by other familiar words and so on. This also reduces the number of tokens we need ([sentencpiece](https://github.com/google/sentencepiece) is a common tokenizer with vocab size options in tens of thousands vs hundreds of thousands of words in english). A tokenizer is something that takes you input text (e.g. “Humpty Dumpt”) and splits it into the tokens and gives you the corresponding numbers that you need to look up the embedding vector for that token in the embedding matrix. For example, in case of “humpty dumpty” if we’re using character level tokenizer and we arranged our embedding matrix as in the picture above, then the tokenizer will first split humpty dumpt into characters \[‘h’,’u’,…’t’\] and then give you back the numbers \[8,21,…20\] because you need to look up the 8th column of the embedding matrix to get the embedding vector for ‘h’ (embedding vector is what you will feed into the model, not the number 8, unlike before). The arrangement of the columns in the matrix is completely irrelevant, we could assign any column to ‘h’ and as long as we look up the same vector every time we input ‘h’ we should be good. Tokenizers just give us an arbitrary (but fixed) number to make lookup easy. The main task we need them for really is splitting the sentence in tokens.

With embeddings and subword tokenization, a model could look something like this:

![Image 8: a diagram showing the different types of networks](https://miro.medium.com/v2/resize:fit:700/1*VGNZ1Zighiek1sAMdiZCaw.png)

Image by author

The next few sections deal with more recent advances in language modeling, and the ones that made LLMs as powerful as they are today. However, to understand these there are a few basic math concepts you need to know. Here are the concepts:

*   Matrices and matrix multiplication
*   General concept of functions in mathematics
*   Raising numbers to powers (e.g. a3 = a\*a\*a)
*   Sample mean, variance, and standard deviation

I have added summaries of these concepts in the appendix.

Self Attention
--------------

So far we have seen only one simple neural network structure (called feedforward network), one which contains a number of layers and each layer is fully connected to the next (i.e., there is a line connecting any two neurons in consecutive layers), and it is only connected to the next layer (e.g. no lines between layer 1 and layer 3 etc..). However, as you can imagine there is nothing stopping us from removing or making other connections. Or even making more complex structures. Let’s explore a particularly important structure: self-attention.

If you look at the structure of human language, the next word that we want to predict will depend on all the words before. However, they may depend on some words before them to a greater degree than others. For example, if we are trying to predict the next word in “Damian had a secret child, a girl, and he had written in his will that all his belongings, along with the magical orb, will belong to \_\_\_\_”. This word here could be “her” or “him” and it depends specifically on a much earlier word in the sentence: _girl/boy_.

The good news is, our simple feedforward model connects to all the words in the context, and so it can learn the appropriate weights for important words, But here’s the problem, the weights connecting specific positions in our model through feed forward layers are fixed (for every position). If the important word was always in the same position, it would learn the weights appropriately and we would be fine. However, the relevant word to the next prediction could be anywhere in the system. We could paraphrase that sentence above and when guessing “her vs his”, one very important word for this prediction would be boy/girl no matter where it appeared in that sentence. So, we need weights that depend not only on the position but also on the content in that position. How do we achieve this?

Self attention does something like adding up the embedding vectors for each of the words, but instead of directly adding them up it applies some weights to each. So if the embedding vectors for humpty,dumpty, sat are x1, x2, x3 respectively, then it will multiply each one with a weight (a number) before adding them up. Something like output = 0.5 x1 + 0.25 x2 + 0.25 x3 where output is the self-attention output. If we write the weights as u1, u2, u3 such that output = u1x1+u2x2+u3x3 then how do we find these weights u1, u2, u3?

Ideally, we want these weights to be dependent on the vector we are adding — as we saw some may be more important than others. But important to whom? To the word we are about to predict. So we also want the weights to depend on the word we are about to predict. Now that’s an issue, we of course don’t know the word we are about to predict before we predict it. So, self attention uses the word immediately preceding the word we are about to predict, i.e., the last word in the sentence available (I don’t really know why this and why not something else, but a lot of things in deep learning are trial and error and I suspect this works well).

Great, so we want weights for these vectors, and we want each weight to depend on the word that we are aggregating and word immediately preceding the one we are going to predict. Basically, we want a function u1 = F(x1, x3) where x1 is the word we will weight and x3 is the last word in the sequence we have (assuming we have only 3 words). Now, a straightforward way of achieving this is to have a vector for x1 (let’s call it k1) and a separate vector for x3 (let’s call it q3) and then simply take their dot product. This will give us a number and it will depend on both x1 and x3. How do we get these vectors k1 and q3? We build a tiny single layer neural network to go from x1 to k1 (or x2 to k2, x3 to k3 and so on). And we build another network going from x3 to q3 etc… Using our matrix notation, we basically come up with weight matrices Wk and Wq such that k1 = Wkx1 and q1 =Wqx1 and so on. Now we can take a dot product of k1 and q3 to get a scalar, so u1 = F(x1,x3) = Wkx1 **·** Wqx3.

One additional thing that happens in self-attention is that we don’t directly take the weighted sum of the embedding vectors themselves. Instead, we take the weighted sum of some “value” of that embedding vector, which is obtained by another small single layer network. What this means is similar to k1 and q1, we also now have a v1 for the word x1 and we obtain it through a matrix Wv such that v1=Wvx1. This v1 is then aggregated. So it all looks something like this if we only have 3 words and we are trying to predict the fourth:

![Image 9: self-adjusted outputs with a humpy](https://miro.medium.com/v2/resize:fit:700/1*oETLwMpxy3oH_B9pN-xLcg.png)

Self attention. Image by author

The plus sign represents a simple addition of the vectors, implying they have to have the same length. One last modification not shown here is that the scalars u1, u2, u3 etc.. won’t necessarily add up to 1. If we need them to be weights, we should make them add up. So we will apply a familiar trick here and use the softmax function.

This is self-attention. There is also cross-attention where you can have the q3 come from the last word, but the k’s and the v’s can come from another sentence altogether. This is for example valuable in translation tasks. Now we know what attention is.

This whole thing can now be put in a box and be called a “self attention block”. Basically, this self attention block takes in the embedding vectors and spits out a single output vector of any user-chosen length. This block has three parameters, Wk,Wq,Wv — it doesn’t need to be more complicated than that. There are many such blocks in the machine learning literature, and they are usually represented by boxes in diagrams with their name on it. Something like this:

![Image 10: a diagram showing the different types of blocks](https://miro.medium.com/v2/resize:fit:700/1*OgcRxWyftIXN8WbQw_-QKg.png)

Image by author

One of the things that you will notice with self-attention is that the position of things so far does not seem relevant. We are using the same W’s across the board and so switching Humpty and Dumpty won’t really make a difference here — all numbers will end up being the same. This means that while attention can figure out what to pay attention to, this won’t depend on word position. However, we do know that word positions are important in english and we can probably improve performance by giving the model some sense of a word’s position.

And so, when attention is used, we don’t often feed the embedding vectors directly to the self attention block. We will later see how “positional encoding” is added to embedding vectors before feeding to attention blocks.

_Note for the pre-initiated_: Those for whom this isn’t the first time reading about self-attention will note that we are not referencing any K and Q matrices, or applying masks etc.. That is because those things are implementation details arising out of how these models are commonly trained. A batch of data is fed and the model is simultaneously trained to predict dumpty from humpty, sat from humpty dumpty and so on. This is a matter of gaining efficiency and does not affect interpretation or even model outputs, and we have chosen to omit training efficiency hacks here.

Softmax
-------

We talked briefly about softmax in the very first note. Here’s the problem softmax is trying to solve: In our output interpretation we have as many neurons as the options from which we want the network to select one. And we said that we are going to interpret the network’s choice as the highest value neuron. Then we said we are going to calculate loss as the difference between the value that network provides, and an ideal value we want. But what’s that ideal value we want? We set it to 0.8 in the leaf/flower example. But why 0.8? Why no 5, or 10, or 10 million? The higher the better for that training example. Ideally we want infinity there! Now that would make the problem intractable — all loss would be infinite and our plan of minimizing loss by moving around parameters (remember “gradient descent”) fails. How do we deal with this?

One simple thing we can do is cap the values we want. Let’s say between 0 and 1? This would make all loss finite, but now we have the issue of what happens when the network overshoots. Let’s say it outputs (5,1) for (leaf,flower) in one case, and (0,1) in another. The first case made the right choice but the loss is worse! Ok, so now we need a way to also convert the outputs of the last layer in (0,1) range so that it preserves the order. We could use any function (a “**function**” in mathematics is simply a mapping of one number to another — in goes one number, out comes another — it’s rule based in terms of what will be output for a given input) here to get the job done. One possible option is the logistic function (see graph below) which maps all numbers to numbers between (0,1) and preserves the order:

![Image 11: linear function for h - i](https://miro.medium.com/v2/resize:fit:700/1*jSyo_owKB-tfTrPXV2giKg.png)

Image by author

Now, we have a number between 0 and 1 for each of the neurons in the last layer and we can calculate loss by setting the correct neuron to 1, others to 0 and taking the difference of that from what the network provides us. This will work, but can we do better?

Going back to our “Humpty dumpty” example, let’s say we are trying to generate dumpty character-by-character and our model makes a mistake when predicting “m” in dumpty. Instead of giving us the last layer with “m” as the highest value, it gives us “u” as the highest value but “m” is a close second.

Now we can continue with “duu” and try to predict next character and so on, but the model confidence will be low because there are not that many good continuations from “humpty duu..”. On the other hand, “m” was a close second, so we can also give “m” a shot, predict the next few characters, and see what happens? Maybe it gives us a better overall word?

So what we are talking about here is not just blindly selecting the max value, but trying a few. What’s a good way to do it? Well we have to assign a chance to each one — say we will pick the top one with 50%, second one with 25% and so on. That’s a good way to do it. But maybe we would want the chance to be dependent on the underlying model predictions. If the model predicts values for m and u to be really close to each other here (compared to other values) — then maybe a close 50–50 chance of exploring the two is a good idea?

So we need a nice rule that takes all these numbers and converts them into chances. That’s what softmax does. It is a generalization of the logistic function above but with additional features. If you give it 10 arbitrary numbers — it will give you 10 outputs, each between 0 and 1 and importantly, all 10 adding up to 1 so that we can interpret them as chance. You will find softmax as the last layer in nearly every language model.

Residual connections
--------------------

We have slowly changed our visualization of networks as the sections progress. We are now using boxes/blocks to denote certain concepts. This notation is useful in denoting a particularly useful concept of residual connections. Let’s look at residual connection combined with a self-attention block:

![Image 12: a diagram of a self-blocking system](https://miro.medium.com/v2/resize:fit:700/1*270MXDfslVtvmBjShHL2hQ.png)

A residual connection. Image by author

Note that we put “Input” and “Output” as boxes to make things simpler, but these are still basically just a collection of neurons/numbers same as shown above.

So what’s going on here? We are basically taking the output of self-attention block and before passing it to the next block, we are adding to it the original Input. First thing to note is that this would require that the dimensions of the self-attention block output must now be the same as that of the input. This is not a problem since as we noted the self-attention output is determined by the user. But why do this? We won’t get into all the details here but the key thing is that as networks get deeper (more layers between input and output) it gets increasingly harder to train them. Residual connections have been shown to help with these training challenges.

Layer Normalization
-------------------

Layer normalization is a fairly simple layer that takes the data coming into the layer and normalizes it by subtracting the mean and dividing it by standard deviation (maybe a bit more, as we see below). For example, if we were to apply layer normalization immediately after the input, it would take all the neurons in the input layer and then it would calculate two statistics: their mean and their standard deviation. Let’s say the mean is M and the standard deviation is S then what layer norm is doing is taking each of these neurons and replacing it with (x-M)/S where x denotes any given neuron’s original value.

Now how does this help? It basically stabilizes the input vector and helps with training deep networks. One concern is that by normalizing inputs, are we removing some useful information from them that may be helpful in learning something valuable about our goal? To address this, the layer norm layer has a scale and a bias parameter. Basically, for each neuron you just multiply it with a scalar and then add a bias to it. These scalar and bias values are parameters that can be trained. This allows the network to learn some of the variation that may be valuable to the predictions. And since these are the only parameters, the LayerNorm block doesn’t have a lot of parameters to train. The whole thing looks something like this:

![Image 13: a diagram of a layer nomination block](https://miro.medium.com/v2/resize:fit:700/1*Zd-PvX2cYslEyrjL6MVnzA.png)

Layer Normalization. Image by author

The Scale and Bias are trainable parameters. You can see that layer norm is a relatively simple block where each number is only operated on pointwise (after the initial mean and std calculation). Reminds us of the activation layer (e.g. RELU) with the key difference being that here we have some trainable parameters (albeit lot fewer than other layers because of the simple pointwise operation).

Standard deviation is a statistical measure of how spread out the values are, e.g., if the values are all the same you would say the standard deviation is zero. If, in general, each value is really far from the mean of these very same values, then you will have a high standard deviation. The formula to calculate standard deviation for a set of numbers, a1, a2, a3…. (say N numbers) goes something like this: subtract the mean (of these numbers) from each of the numbers, then square the answer for each of N numbers. Add up all these numbers and then divide by N. Now take a square root of the answer.

Note for the pre-initiated: Experienced ML professionals will note that there is no discussion of batch norm here. In-fact, we haven’t even introduced the concept of batches in this article at all. For the most part, I believe batches are another training accelerant not related to the understanding of core concepts (except perhaps batch norm which we do not need here).

Dropout
-------

Dropout is a simple but effective method to avoid model overfitting. Overfitting is a term for when you train the model on your training data, and it works well on that dataset but does not generalize well to the examples the model has not seen. Techniques that help us avoid overfitting are called “**regularization techniques**”, and dropout is one of them.

If you train a model, it might make errors on the data and/or overfit it in a particular way. If you train another model, it might do the same, but in a different way. What if you trained a number of these models and averaged the outputs? These are typically called “**ensemble** **models**” because they predict the outputs by combining outputs from an ensemble of models, and ensemble models generally perform better than any of the individual models.

In neural networks, you could do the same. You could build multiple (slightly different) models and then combine their outputs to get a better model. However, this can be computationally expensive. Dropout is a technique that doesn’t quite build ensemble models but does capture some of the essence of the concept.

The concept is simple, by inserting a dropout layer during training what you are doing is randomly deleting a certain percentage of the direct neuron connections between the layers that dropout is inserted. Considering our initial network and inserting a Dropout layer between the input and the middle layer with 50% dropout rate can look something like this:

![Image 14: a diagram of a sunflower and a sunflower](https://miro.medium.com/v2/resize:fit:700/1*j0oKuXvH7kfrIpIfXE03VA.png)

![Image 15: a diagram showing the arrow pointing to the right](https://miro.medium.com/v2/resize:fit:700/1*UodvtsDn5z73Cp578XOoVw.png)

![Image 16: a diagram of a sunflower and its leaves](https://miro.medium.com/v2/resize:fit:700/1*qHPSwQmV3sfvKT5pG4TEJw.png)

Image by author

Now, this forces the network to train with a lot of redundancy. Essentially, you are training a number of different models at the same time — but they share weights.

Now for making inferences, we could follow the same approach as an ensemble model. We could make multiple predictions using dropouts and then combine them. However, since that is computationally intensive — and since our models share common weights — why don’t we just do a prediction using all the weights (so instead of using 50% of the weights at a time we use all at the same time). This should give us some approximation of what an ensemble will provide.

One issue though: the model trained with 50% of the weights will have very different numbers in the middle neurons than one using all the weights. What we want is more ensemble style averaging here. How do we do this? Well, a simple way is to simply take all the weights and multiply them by 0.5 since we are now using twice as many weights. This is what Droput does during inference. It will use the full network with all the weights and simply multiply the weights with (1- p) where p is the deletion probability. And this has been shown to work rather well as a regularization technique.

Multi-head Attention
--------------------

This is the key block in the transformer architecture. We’ve already seen what an attention block is. Remember that the output of an attention block was determined by the user and it was the length of v’s. What a multi-attention head is basically you run several attention heads in parallel (they all take the same inputs). Then we take all their outputs and simply concatenate them. It looks something like this:

![Image 17: a diagram showing the different types of data](https://miro.medium.com/v2/resize:fit:700/1*BmZd8SIDEQu7r5_R7y54kQ.png)

Multi-head attention. Image by author

Keep in mind the arrows going from v1 -\> v1h1 are linear layers — there’s a matrix on each arrow that transforms. I just did not show them to avoid clutter.

What is going on here is that we are generating the same key, query and values for each of the heads. But then we are basically applying a linear transformation on top of that (separately to each k,q,v and separately for each head) before we use those k,q,v values. This extra layer did not exist in self attention.

A side note is that to me, this is a slightly surprising way of creating a multi-headed attention. For example, why not create separate Wk,Wq,Wv matrices for each of the heads rather than adding a new layer and sharing these weights. Let me know if you know — I really have no idea.

Positional encoding and embedding
---------------------------------

We briefly talked about the motivation for using positional encoding in the self-attention section. What are these? While the picture shows positional encoding, using a positional embedding is more common than using an encoding. As such we talk about a common positional embedding here but the appendix also covers positional encoding used in the original paper. A positional embedding is no different than any other embedding except that instead of embedding the word vocabulary we will embed numbers 1, 2, 3 etc. So this embedding is a matrix of the same length as word embedding, and each column corresponds to a number. That’s really all there is to it.

The GPT architecture
--------------------

Let’s talk about the GPT architecture. This is what is used in most GPT models (with variation across). If you have been following the article thus far, this should be fairly trivial to understand. Using the box notation, this is what the architecture looks like at high level:

![Image 18: a diagram of a process for a transducer](https://miro.medium.com/v2/resize:fit:700/0*U9mQKCWiyakNVwxU)

The GPT Architecture. Image by author

At this point, other than the “GPT Transformer Block” all the other blocks have been discussed in great detail. The + sign here simply means that the two vectors are added together (which means the two embeddings must be the same size). Let’s look at this GPT Transformer Block:

![Image 19: the transformation book for gtf](https://miro.medium.com/v2/resize:fit:700/1*Mq4hBZcKPL9GALPSSQG9Xg.png)

And that’s pretty much it. It is called “transformer” here because it is derived from and is a type of transformer — which is an architecture we will look at in the next section. This doesn’t affect understanding as we’ve already covered all the building blocks shown here before. Let’s recap everything we’ve covered so far building up to this GPT architecture:

*   We saw how neural nets take numbers and output other numbers and have weights as parameters which can be trained
*   We can attach interpretations to these input/output numbers and give real world meaning to a neural network
*   We can chain neural networks to create bigger ones, and we can call each one a “block” and denote it with a box to make diagrams easier. Each block still does the same thing, take in a bunch of numbers and output other bunch of numbers
*   We learned a lot of different types of blocks that serve different purposes
*   GPT is just a special arrangement of these blocks that is shown above with an interpretation that we discussed in Part 1

Modifications have been made over time to this as companies have built up to powerful modern LLMs, but the basic remains the same.

Now, this GPT transformer is actually what is called a “decoder” in the original transformer paper that introduced the transformer architecture. Let’s take a look at that.

The transformer architecture
----------------------------

This is one of the key innovations driving rapid acceleration in the capabilities of language models recently. Transformers not only improved the prediction accuracy, they are also easier/more efficient than previous models (to train), allowing for larger model sizes. This is what the GPT architecture above is based on.

If you look at GPT architecture, you can see that it is great for generating the next word in the sequence. It fundamentally follows the same logic we discussed in Part 1. Start with a few words and then continue generating one at a time. But, what if you wanted to do translation. What if you had a sentence in german (e.g. “Wo wohnst du?” = “Where do you live?”) and you wanted to translate it to english. How would we train the model to do this?

Well, first thing we would need to do is figure out a way to input german words. Which means we have to expand our embedding to include both german and english. Now, I guess here is a simply way of inputting the information. Why don’t we just concatenate the german sentence at the beginning of whatever so far generated english is and feed it to the context. To make it easier for the model, we can add a separator. This would look something like this at each step:

![Image 20: a diagram showing the different ways to say the word](https://miro.medium.com/v2/resize:fit:700/1*psIz3-v2dMfI3SMsFQjRPQ.png)

Image by author

This will work, but it has room for improvement:

*   If the context length is fixed, sometimes the original sentence is lost
*   The model has a lot to learn here. Two languages simultaneously, but also to know that


### Image Analysis
is the separator token where it needs to start translating
*   You are processing the entire german sentence, with different offsets, for each word generation. This means there will be different internal representations of the same thing and the model should be able to work through it all for translation

Transformer was originally created for this task and consists of an “encoder” and a “decoder” — which are basically two separate blocks. One block simply takes the german sentence and gives out an intermediate representation (again, bunch of numbers, basically) — this is called the encoder.

The second block generates words (we’ve seen a lot of this so far). The only difference is that in addition to feeding it the words generated so far we also feed it the encoded german (from the encoder block) sentence. So as it is generating language, it’s context is basically all the words generated so far, plus the german. This block is called the decoder.

Each of these encoders and decoders consist of a few blocks, notably the attention block sandwiched between other layers. Let’s look at the illustration of a transformer from the paper “Attention is all you need” and try to understand it:

![Image 21: a diagram showing the process of a video processing system](https://miro.medium.com/v2/resize:fit:683/1*uPwJ24na4D_ECHBv1Lg5Fg.png)

Image from Vaswani et al. (2017)

The vertical set of blocks on the left is called the “encoder” and the ones to the right is called the “decoder”. Let’s go over and understand anything that we have not already covered before:

_Recap on how to read the diagram:_ Each of the boxes here is a block that takes in some inputs in the form of neurons, and spits out a set of neurons as output that can then either be processed by the next block or interpreted by us. The arrows show where the output of a block is going. As you can see, we will often take the output of one block and feed it in as input into multiple blocks. Let’s go through each thing here:

Feed forward: A feedforward network is one that does not contain cycles. Our original network in section 1 is a feed forward. In-fact, this block uses very much the same structure. It contains two linear layers, each followed by a RELU (see note on RELU in first section) and a dropout layer. Keep in mind that this feedforward neetwork applies to each position independently. What this means is that the information on position 0 has a feedforward network, and on position 1 has one and so on.. But the neurons from position x do not have a linkage to the feedforward network of position y. This is important because if we did not do this, it would allow the network to cheat during training time by looking forward.

_Cross-attention:_ You will notice that the decoder has a multi-head attention with arrows coming from the encoder. What is going on here? Remember the value, key, query in self-attention and multi-head attention? They all came from the same sequence. The query was just from the last word of the sequence in-fact. So what if we kept the query but fetched the value and key from a completely different sequence altogether? That is what is happening here. The value and key come from the output of the encoder. Nothing has changed mathematically except where the inputs for key and value are coming from now.

_Nx_: The Nx here simply represents that this block is chain-repeated N times. So basically you are stacking the block back-to-back and passing the input from the previous block to the next one. This is a way to make the neural network deeper. Now, looking at the diagram there is room for confusion about how the encoder output is fed to the decoder. Let’s say N=5. Do we feed the output of each encoder layer to the corresponding decoder layer? No. Basically you run the encoder all the way through once and only once. Then you just take that representation and feed the same thing to every one of the 5 decoder layers.

_Add & Norm block_: This is basically the same as below (guess the authors were just trying to save space)

![Image 22: layer norm diagram](https://miro.medium.com/v2/resize:fit:681/0*sXvYIassJutgqw5W)

Image by author

Everything else has already been discussed. Now you have a complete explanation of the transformer architecture building up from simple sum and product operations and fully self contained! You know what every line, every sum, every box and word means in terms of how to build them from scratch. Theoretically, these notes contain what you need to code up the transformer from scratch. In-fact, if you are interested [this repo](https://github.com/karpathy/nanoGPT) does that for the GPT architecture above.

Appendix
--------

Matrix Multiplication
---------------------

We introduced vectors and matrices above in the context of embeddings. A matrix has two dimensions (number or rows and columns). A vector can also be thought of as a matrix where one of the dimensions equals one. Product of two matrices is defined as:

![Image 23: a diagram showing the structure of a dna](https://miro.medium.com/v2/resize:fit:700/0*woel5Da5Z22EmiGx)

Image by author

Dots represent multiplication. Now let’s take a second look at the calculation of blue and organic neurons in the very first picture. If we write the weights as a matrix and the inputs as vectors, we can write the whole operation in the following way:

![Image 24: a diagram showing the number of numbers in a matrix](https://miro.medium.com/v2/resize:fit:466/0*yn1TPuxw_QqnD93k)

Image by author

If the weight matrix is called “W” and the inputs are called “x” then Wx is the result (the middle layer in this case). We can also transpose the two and write it as xW — this is a matter of preference.

Standard deviation
------------------

We use the concept of standard deviation in the Layer Normalization section. Standard deviation is a statistical measure of how spread out the values are (in a set of numbers), e.g., if the values are all the same you would say the standard deviation is zero. If, in general, each value is really far from the mean of these very same values, then you will have a high standard deviation. The formula to calculate standard deviation for a set of numbers, a1, a2, a3…. (say N numbers) goes something like this: subtract the mean (of these numbers) from each of the numbers, then square the answer for each of N numbers. Add up all these numbers and then divide by N. Now take a square root of the answer.

Positional Encoding
-------------------

We talked about positional embedding above. A positional encoding is simply a vector of the same length as the word embedding vector, except it is not an embedding in the sense that it is not trained. We simply assign a unique vector to every position e.g. a different vector for position 1 and different one for position 2 and so on. A simple way of doing this is to make the vector for that position simply full of the position number. So the vector for position 1 would be \[1,1,1…1\] for 2 would be \[2,2,2…2\] and so on (remember length of each vector must match embedding length for addition to work). This is problematic because we can end up with large numbers in vectors which creates challenges during training. We can, of course, normalize these vectors by dividing every number by the max of position, so if there are 3 words total then position 1 is \[.33,.33,..,.33\] and 2 is \[.67, .67, ..,.67\] and so on. This has the problem now that we are constantly changing the encoding for position 1 (those numbers will be different when we feed 4 word sentence as input) and it creates challenges for the network to learn. So here, we want a scheme that allocates a unique vector to each position, and the numbers don’t explode. Basically if the context length is d (i.e., maximum number of tokens/words that we can feed into the network for predicting next token/word, see discussion in “how does it all generate language?” section) and if the length of the embedding vector is 10 (say), then we need a matrix with 10 rows and d columns where all the columns are unique and all the numbers lie between 0 and 1. Given that there are infinitely many numbers between zero and 1, and the matrix is finitely sized, this can be done in many ways.

The approach used in the “Attention is all you need” paper goes something like this:

*   Draw 10 sin curves each being si(p) = sin (p/10000(i/d)) (that’s 10k to power i/d)
*   Fill the encoding matrix with numbers such that (i,p)th number is si(p), e.g., for position 1 the 5th element of the encoding vector is s5(1)=sin (1/10000(5/d))

Why choose this method? By changing the power on 10k you are changing the amplitude of the sine function when viewed on the p-axis. And if you have 10 different sine functions with 10 different amplitudes, then it will be a long time before you get a repetition (i.e. all 10 values are the same) for changing values of p. And this helps give us unique values. Now, the actual paper uses both sine and cosine functions and the form of encoding is: si(p) = sin (p/10000(i/d)) if i is even and si(p) = cos(p/10000(i/d)) if i is odd.


---

## Towards Data Science

Source: https://medium.com/towards-data-science/how-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322
Date fetched: 2024-11-10T01:49:51.510196

---

Title: How to Query a Knowledge Graph with LLMs using gRAG | Towards Data Science

URL Source: https://medium.com/towards-data-science/how-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322

Markdown Content:
How to Query a Knowledge Graph with LLMs using gRAG | Towards Data Science
===============
 

[Mastodon](https://me.dm/@cristianleo)

How to Query a Knowledge Graph with LLMs Using gRAG
===================================================

Google, Microsoft, LinkedIn, and many more tech companies are using Graph RAG. Why? Let’s understand it by building one from scratch.
-------------------------------------------------------------------------------------------------------------------------------------

[![Image 2: Cristian Leo](https://miro.medium.com/v2/da:true/resize:fill:88:88/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=post_page---byline--38bfac47a322--------------------------------)

[Cristian Leo](https://medium.com/@cristianleo120?source=post_page---byline--38bfac47a322--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc24a3d106811&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=post_page-c24a3d106811--byline--38bfac47a322---------------------post_header-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=---header_actions--38bfac47a322---------------------clap_footer-----------)

371

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&source=---header_actions--38bfac47a322---------------------bookmark_footer-----------)

![Image 4: a light bulb with a light bulb and a network of connected dots](https://miro.medium.com/v2/resize:fit:700/0*UeZPcm_AcNpatRN4)

Image illustrating a knowledge graph with interconnected nodes and edges against a tech-inspired gradient background — Image generated by the author using DALL-E

You may not realize it, but you’ve been interacting with Knowledge Graphs (KGs) more frequently than you might think. They’re the technology behind many modern search engines, Retrieval-Augmented Generation (RAG) systems for Large Language Models (LLMs), and various query tools. But what exactly are Knowledge Graphs, and why are they so integral to these technologies? Let’s delve into it.

Introduction to Knowledge Graphs
================================

A Knowledge Graph (KG) is a structured representation of information that captures real-world entities and the relationships between them. Imagine a network where each point represents an entity — such as a product, person, or concept — and the lines connecting them represent the relationships they share. This interconnected web allows for a rich semantic understanding of data, where the focus isn’t just on individual pieces of information but on how these pieces relate to one another.

Nodes
-----

At the heart of a knowledge graph are nodes (entities). To illustrate this, let’s consider building a…

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&source=-----38bfac47a322---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=---footer_actions--38bfac47a322---------------------clap_footer-----------)

371

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=---footer_actions--38bfac47a322---------------------clap_footer-----------)

371

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&source=---footer_actions--38bfac47a322---------------------bookmark_footer-----------)

[![Image 5: Cristian Leo](https://miro.medium.com/v2/da:true/resize:fill:144:144/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=post_page---post_author_info--38bfac47a322--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc24a3d106811&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=post_page-c24a3d106811--post_author_info--38bfac47a322---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F5a6c71c2b112&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&newsletterV3=c24a3d106811&newsletterV3Id=5a6c71c2b112&user=Cristian+Leo&userId=c24a3d106811&source=---post_author_info--38bfac47a322---------------------subscribe_user-----------)

Data Scientist @ Amazon with a passion about recreating all the popular machine learning algorithm from scratch.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc24a3d106811&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=post_page-c24a3d106811--post_author_info--38bfac47a322---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F5a6c71c2b112&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&newsletterV3=c24a3d106811&newsletterV3Id=5a6c71c2b112&user=Cristian+Leo&userId=c24a3d106811&source=---post_author_info--38bfac47a322---------------------subscribe_user-----------)

![Image 7: Keep the Gradients Flowing](https://miro.medium.com/v2/resize:fit:679/0*Kw95j1z9pkvdFV-J)

[![Image 8: Cristian Leo](https://miro.medium.com/v2/resize:fill:20:20/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Cristian Leo](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Keep the Gradients Flowing -------------------------- ### Optimizing Sparse Neural Networks: Understanding Gradient Flow for Faster Training, and Better Performance in Deep Learning Models.](https://medium.com/keep-the-gradients-flowing-5b9bf0098e3d?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[276 3](https://medium.com/keep-the-gradients-flowing-5b9bf0098e3d?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F5b9bf0098e3d&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkeep-the-gradients-flowing-5b9bf0098e3d&source=-----38bfac47a322----0-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----38bfac47a322----1-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2563cec4d10e&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpreference-alignment-for-everyone-2563cec4d10e&source=-----38bfac47a322----2-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

![Image 13: Why Every Data Scientist Should Code in C++](https://miro.medium.com/v2/resize:fit:679/0*lHNVNTxHiaBmSxQY)

[![Image 14: Cristian Leo](https://miro.medium.com/v2/resize:fill:20:20/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Cristian Leo](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Why Every Data Scientist Should Code in C++ ------------------------------------------- ### Why Google, FaceBook, and Microsoft prefer C++ for AI projects, and why you should learn it as a Data Scientist.](https://levelup.gitconnected.com/why-every-data-scientist-should-code-in-c-fe9b5a8ea805?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[313 4](https://levelup.gitconnected.com/why-every-data-scientist-should-code-in-c-fe9b5a8ea805?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffe9b5a8ea805&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fwhy-every-data-scientist-should-code-in-c-fe9b5a8ea805&source=-----38bfac47a322----3-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

![Image 15: Building Knowledge Graphs with LLM Graph Transformer](https://miro.medium.com/v2/resize:fit:679/0*KHns0-DJoCjfzxyr)

[![Image 16: Tomaz Bratanic](https://miro.medium.com/v2/resize:fill:20:20/1*SnWQP0l4Vg9577WAErbjfw.jpeg)](https://bratanic-tomaz.medium.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Tomaz Bratanic](https://bratanic-tomaz.medium.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Building Knowledge Graphs with LLM Graph Transformer ---------------------------------------------------- ### A deep dive into LangChain’s implementation of graph construction with LLMs](https://medium.com/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[492 4](https://medium.com/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa91045c49b59&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-knowledge-graphs-with-llm-graph-transformer-a91045c49b59&source=-----38bfac47a322----0-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

![Image 17: Using Neo4j features to Explain the Impact of Staged Addition to Knowledge Graph Construction](https://miro.medium.com/v2/resize:fit:679/1*cqaI_VuBY4SGmJJcMrTYuw.jpeg)

[![Image 18: Kennedy Selvadurai, PhD](https://miro.medium.com/v2/resize:fill:20:20/1*LfIBSgoAH4dnQKuhNgoRlQ.jpeg)](https://medium.com/@heelara?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Kennedy Selvadurai, PhD](https://medium.com/@heelara?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[AI Advances](https://ai.gopubby.com/?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Using Neo4j features to Explain the Impact of Staged Addition to Knowledge Graph Construction --------------------------------------------------------------------------------------------- ### Could ease of KG handling of LlamaIndex and advanced exploration afforded by Neo4j solve LLM hallucination?](https://ai.gopubby.com/impact-of-staged-addition-to-knowledge-graph-construction-and-querying-af944ea15329?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[150](https://ai.gopubby.com/impact-of-staged-addition-to-knowledge-graph-construction-and-querying-af944ea15329?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Faf944ea15329&operation=register&redirect=https%3A%2F%2Fai.gopubby.com%2Fimpact-of-staged-addition-to-knowledge-graph-construction-and-querying-af944ea15329&source=-----38bfac47a322----1-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[![Image 25](https://miro.medium.com/v2/resize:fill:48:48/1*Fwpkf8H5PwNrzSzMYUFjjA.png) ![Image 26](https://miro.medium.com/v2/resize:fill:48:48/1*G49cai7vIuhFeSwb4LCuSQ.jpeg) ![Image 27](https://miro.medium.com/v2/resize:fill:48:48/1*HlJ2e41GVVzzjWYiX0dU1g.png) data science and AI ------------------- 40 stories·279 saves](https://medium.com/@grexe/list/data-science-and-ai-35d21381d956?source=read_next_recirc-----38bfac47a322--------------------------------)

![Image 31: Reality meet expectations in AI… sometime](https://miro.medium.com/v2/resize:fit:679/1*q-aW8C1MOZMlgJueLOT1hg.png)

[![Image 32: Fabio Matricardi](https://miro.medium.com/v2/resize:fill:20:20/1*p4ShYlP7zymOUeIZ5DSbfg.png)](https://medium.com/@fabio.matricardi?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Fabio Matricardi](https://medium.com/@fabio.matricardi?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Reality meet expectations in AI… sometime ----------------------------------------- ### SmolLM2–1.7B-instruct is exactly as announced: good, accurate, slim and fast](https://blog.stackademic.com/reality-meet-expectations-in-ai-sometime-c1dff6301836?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[217 4](https://blog.stackademic.com/reality-meet-expectations-in-ai-sometime-c1dff6301836?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc1dff6301836&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Freality-meet-expectations-in-ai-sometime-c1dff6301836&source=-----38bfac47a322----0-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

![Image 33: LongRAG: Giving AI a Bigger Net to Catch More Fish in the Sea of Information](https://miro.medium.com/v2/resize:fit:679/1*Nt5TRh0ooDkgmibMlA1Srg.png)

[![Image 34: Florian June](https://miro.medium.com/v2/resize:fill:20:20/1*DmQ3DH2JeAJquvhT_tjVCw.jpeg)](https://medium.com/@florian_algo?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Florian June](https://medium.com/@florian_algo?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Generative AI](https://generativeai.pub/?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[LongRAG: Giving AI a Bigger Net to Catch More Fish in the Sea of Information ---------------------------------------------------------------------------- ### In my previous article, I introduced whether RAG would become obsolete due to long-context LLMs. Today, let’s look at how to apply…](https://generativeai.pub/longrag-giving-ai-a-bigger-net-to-catch-more-fish-in-the-sea-of-information-7ecdd63f330d?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[116](https://generativeai.pub/longrag-giving-ai-a-bigger-net-to-catch-more-fish-in-the-sea-of-information-7ecdd63f330d?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7ecdd63f330d&operation=register&redirect=https%3A%2F%2Fgenerativeai.pub%2Flongrag-giving-ai-a-bigger-net-to-catch-more-fish-in-the-sea-of-information-7ecdd63f330d&source=-----38bfac47a322----1-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[![Image 36: Shenggang Li](https://miro.medium.com/v2/resize:fill:20:20/1*knqQWkDF7J-gf_A5p7ew5g.png)](https://medium.com/@datalev?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Shenggang Li](https://medium.com/@datalev?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Towards AI](https://pub.towardsai.net/?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[157 2](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa301f6028c73&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fexploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73&source=-----38bfac47a322----2-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

![Image 37: GPT-5 is finally here — What To Expect and What Not To Expect](https://miro.medium.com/v2/resize:fit:679/0*WS8GaZ6iL7VsWAgM)

[![Image 38: Don Lim](https://miro.medium.com/v2/resize:fill:20:20/1*SkAt7uMC11I7WgRXlBMiPA.jpeg)](https://medium.com/@don-lim?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Don Lim](https://medium.com/@don-lim?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[GPT-5 is finally here — What To Expect and What Not To Expect ------------------------------------------------------------- ### Microsoft engineers are preparing to host Orion (GPT-5) on Azure as early as November 2024.](https://medium.com/@don-lim/gpt-5-is-finally-here-what-to-expect-and-what-not-to-expect-9f90e5362408?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[466 7](https://medium.com/@don-lim/gpt-5-is-finally-here-what-to-expect-and-what-not-to-expect-9f90e5362408?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9f90e5362408&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40don-lim%2Fgpt-5-is-finally-here-what-to-expect-and-what-not-to-expect-9f90e5362408&source=-----38bfac47a322----3-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

## Visual Content Analysis

### Image Analysis
Title: How to Query a Knowledge Graph with LLMs using gRAG | Towards Data Science

URL Source: https://medium.com/towards-data-science/how-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322

Markdown Content:
How to Query a Knowledge Graph with LLMs using gRAG | Towards Data Science
===============
 

[Mastodon](https://me.dm/@cristianleo)

How to Query a Knowledge Graph with LLMs Using gRAG
===================================================

Google, Microsoft, LinkedIn, and many more tech companies are using Graph RAG. Why? Let’s understand it by building one from scratch.
-------------------------------------------------------------------------------------------------------------------------------------

[![Image 2: Cristian Leo](https://miro.medium.com/v2/da:true/resize:fill:88:88/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=post_page---byline--38bfac47a322--------------------------------)

[Cristian Leo](https://medium.com/@cristianleo120?source=post_page---byline--38bfac47a322--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc24a3d106811&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=post_page-c24a3d106811--byline--38bfac47a322---------------------post_header-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=---header_actions--38bfac47a322---------------------clap_footer-----------)

371

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&source=---header_actions--38bfac47a322---------------------bookmark_footer-----------)

![Image 4: a light bulb with a light bulb and a network of connected dots](https://miro.medium.com/v2/resize:fit:700/0*UeZPcm_AcNpatRN4)

Image illustrating a knowledge graph with interconnected nodes and edges against a tech-inspired gradient background — Image generated by the author using DALL-E

You may not realize it, but you’ve been interacting with Knowledge Graphs (KGs) more frequently than you might think. They’re the technology behind many modern search engines, Retrieval-Augmented Generation (RAG) systems for Large Language Models (LLMs), and various query tools. But what exactly are Knowledge Graphs, and why are they so integral to these technologies? Let’s delve into it.

Introduction to Knowledge Graphs
================================

A Knowledge Graph (KG) is a structured representation of information that captures real-world entities and the relationships between them. Imagine a network where each point represents an entity — such as a product, person, or concept — and the lines connecting them represent the relationships they share. This interconnected web allows for a rich semantic understanding of data, where the focus isn’t just on individual pieces of information but on how these pieces relate to one another.

Nodes
-----

At the heart of a knowledge graph are nodes (entities). To illustrate this, let’s consider building a…

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&source=-----38bfac47a322---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=---footer_actions--38bfac47a322---------------------clap_footer-----------)

371

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=---footer_actions--38bfac47a322---------------------clap_footer-----------)

371

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F38bfac47a322&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&source=---footer_actions--38bfac47a322---------------------bookmark_footer-----------)

[![Image 5: Cristian Leo](https://miro.medium.com/v2/da:true/resize:fill:144:144/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=post_page---post_author_info--38bfac47a322--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc24a3d106811&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=post_page-c24a3d106811--post_author_info--38bfac47a322---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F5a6c71c2b112&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&newsletterV3=c24a3d106811&newsletterV3Id=5a6c71c2b112&user=Cristian+Leo&userId=c24a3d106811&source=---post_author_info--38bfac47a322---------------------subscribe_user-----------)

Data Scientist @ Amazon with a passion about recreating all the popular machine learning algorithm from scratch.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc24a3d106811&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&user=Cristian+Leo&userId=c24a3d106811&source=post_page-c24a3d106811--post_author_info--38bfac47a322---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F5a6c71c2b112&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-query-a-knowledge-graph-with-llms-using-grag-38bfac47a322&newsletterV3=c24a3d106811&newsletterV3Id=5a6c71c2b112&user=Cristian+Leo&userId=c24a3d106811&source=---post_author_info--38bfac47a322---------------------subscribe_user-----------)

![Image 7: Keep the Gradients Flowing](https://miro.medium.com/v2/resize:fit:679/0*Kw95j1z9pkvdFV-J)

[![Image 8: Cristian Leo](https://miro.medium.com/v2/resize:fill:20:20/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Cristian Leo](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Keep the Gradients Flowing -------------------------- ### Optimizing Sparse Neural Networks: Understanding Gradient Flow for Faster Training, and Better Performance in Deep Learning Models.](https://medium.com/keep-the-gradients-flowing-5b9bf0098e3d?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[276 3](https://medium.com/keep-the-gradients-flowing-5b9bf0098e3d?source=author_recirc-----38bfac47a322----0---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F5b9bf0098e3d&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkeep-the-gradients-flowing-5b9bf0098e3d&source=-----38bfac47a322----0-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----38bfac47a322----1---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----38bfac47a322----1-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----38bfac47a322----2---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2563cec4d10e&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fpreference-alignment-for-everyone-2563cec4d10e&source=-----38bfac47a322----2-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

![Image 13: Why Every Data Scientist Should Code in C++](https://miro.medium.com/v2/resize:fit:679/0*lHNVNTxHiaBmSxQY)

[![Image 14: Cristian Leo](https://miro.medium.com/v2/resize:fill:20:20/0*vXUpsKuv7A7DlqP0)](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Cristian Leo](https://medium.com/@cristianleo120?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[Why Every Data Scientist Should Code in C++ ------------------------------------------- ### Why Google, FaceBook, and Microsoft prefer C++ for AI projects, and why you should learn it as a Data Scientist.](https://levelup.gitconnected.com/why-every-data-scientist-should-code-in-c-fe9b5a8ea805?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[313 4](https://levelup.gitconnected.com/why-every-data-scientist-should-code-in-c-fe9b5a8ea805?source=author_recirc-----38bfac47a322----3---------------------e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ffe9b5a8ea805&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fwhy-every-data-scientist-should-code-in-c-fe9b5a8ea805&source=-----38bfac47a322----3-----------------bookmark_preview----e012fd79_a726_497f_b2b3_a4b8c54897bd-------)

![Image 15: Building Knowledge Graphs with LLM Graph Transformer](https://miro.medium.com/v2/resize:fit:679/0*KHns0-DJoCjfzxyr)

[![Image 16: Tomaz Bratanic](https://miro.medium.com/v2/resize:fill:20:20/1*SnWQP0l4Vg9577WAErbjfw.jpeg)](https://bratanic-tomaz.medium.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Tomaz Bratanic](https://bratanic-tomaz.medium.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Building Knowledge Graphs with LLM Graph Transformer ---------------------------------------------------- ### A deep dive into LangChain’s implementation of graph construction with LLMs](https://medium.com/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[492 4](https://medium.com/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa91045c49b59&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-knowledge-graphs-with-llm-graph-transformer-a91045c49b59&source=-----38bfac47a322----0-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

![Image 17: Using Neo4j features to Explain the Impact of Staged Addition to Knowledge Graph Construction](https://miro.medium.com/v2/resize:fit:679/1*cqaI_VuBY4SGmJJcMrTYuw.jpeg)

[![Image 18: Kennedy Selvadurai, PhD](https://miro.medium.com/v2/resize:fill:20:20/1*LfIBSgoAH4dnQKuhNgoRlQ.jpeg)](https://medium.com/@heelara?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Kennedy Selvadurai, PhD](https://medium.com/@heelara?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[AI Advances](https://ai.gopubby.com/?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Using Neo4j features to Explain the Impact of Staged Addition to Knowledge Graph Construction --------------------------------------------------------------------------------------------- ### Could ease of KG handling of LlamaIndex and advanced exploration afforded by Neo4j solve LLM hallucination?](https://ai.gopubby.com/impact-of-staged-addition-to-knowledge-graph-construction-and-querying-af944ea15329?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[150](https://ai.gopubby.com/impact-of-staged-addition-to-knowledge-graph-construction-and-querying-af944ea15329?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Faf944ea15329&operation=register&redirect=https%3A%2F%2Fai.gopubby.com%2Fimpact-of-staged-addition-to-knowledge-graph-construction-and-querying-af944ea15329&source=-----38bfac47a322----1-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[![Image 25](https://miro.medium.com/v2/resize:fill:48:48/1*Fwpkf8H5PwNrzSzMYUFjjA.png) ![Image 26](https://miro.medium.com/v2/resize:fill:48:48/1*G49cai7vIuhFeSwb4LCuSQ.jpeg) ![Image 27](https://miro.medium.com/v2/resize:fill:48:48/1*HlJ2e41GVVzzjWYiX0dU1g.png) data science and AI ------------------- 40 stories·279 saves](https://medium.com/@grexe/list/data-science-and-ai-35d21381d956?source=read_next_recirc-----38bfac47a322--------------------------------)

![Image 31: Reality meet expectations in AI… sometime](https://miro.medium.com/v2/resize:fit:679/1*q-aW8C1MOZMlgJueLOT1hg.png)

[![Image 32: Fabio Matricardi](https://miro.medium.com/v2/resize:fill:20:20/1*p4ShYlP7zymOUeIZ5DSbfg.png)](https://medium.com/@fabio.matricardi?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Fabio Matricardi](https://medium.com/@fabio.matricardi?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Reality meet expectations in AI… sometime ----------------------------------------- ### SmolLM2–1.7B-instruct is exactly as announced: good, accurate, slim and fast](https://blog.stackademic.com/reality-meet-expectations-in-ai-sometime-c1dff6301836?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[217 4](https://blog.stackademic.com/reality-meet-expectations-in-ai-sometime-c1dff6301836?source=read_next_recirc-----38bfac47a322----0---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc1dff6301836&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Freality-meet-expectations-in-ai-sometime-c1dff6301836&source=-----38bfac47a322----0-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

![Image 33: LongRAG: Giving AI a Bigger Net to Catch More Fish in the Sea of Information](https://miro.medium.com/v2/resize:fit:679/1*Nt5TRh0ooDkgmibMlA1Srg.png)

[![Image 34: Florian June](https://miro.medium.com/v2/resize:fill:20:20/1*DmQ3DH2JeAJquvhT_tjVCw.jpeg)](https://medium.com/@florian_algo?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Florian June](https://medium.com/@florian_algo?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Generative AI](https://generativeai.pub/?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[LongRAG: Giving AI a Bigger Net to Catch More Fish in the Sea of Information ---------------------------------------------------------------------------- ### In my previous article, I introduced whether RAG would become obsolete due to long-context LLMs. Today, let’s look at how to apply…](https://generativeai.pub/longrag-giving-ai-a-bigger-net-to-catch-more-fish-in-the-sea-of-information-7ecdd63f330d?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[116](https://generativeai.pub/longrag-giving-ai-a-bigger-net-to-catch-more-fish-in-the-sea-of-information-7ecdd63f330d?source=read_next_recirc-----38bfac47a322----1---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7ecdd63f330d&operation=register&redirect=https%3A%2F%2Fgenerativeai.pub%2Flongrag-giving-ai-a-bigger-net-to-catch-more-fish-in-the-sea-of-information-7ecdd63f330d&source=-----38bfac47a322----1-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[![Image 36: Shenggang Li](https://miro.medium.com/v2/resize:fill:20:20/1*knqQWkDF7J-gf_A5p7ew5g.png)](https://medium.com/@datalev?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Shenggang Li](https://medium.com/@datalev?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Towards AI](https://pub.towardsai.net/?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[157 2](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----38bfac47a322----2---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa301f6028c73&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fexploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73&source=-----38bfac47a322----2-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

![Image 37: GPT-5 is finally here — What To Expect and What Not To Expect](https://miro.medium.com/v2/resize:fit:679/0*WS8GaZ6iL7VsWAgM)

[![Image 38: Don Lim](https://miro.medium.com/v2/resize:fill:20:20/1*SkAt7uMC11I7WgRXlBMiPA.jpeg)](https://medium.com/@don-lim?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[Don Lim](https://medium.com/@don-lim?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[GPT-5 is finally here — What To Expect and What Not To Expect ------------------------------------------------------------- ### Microsoft engineers are preparing to host Orion (GPT-5) on Azure as early as November 2024.](https://medium.com/@don-lim/gpt-5-is-finally-here-what-to-expect-and-what-not-to-expect-9f90e5362408?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[466 7](https://medium.com/@don-lim/gpt-5-is-finally-here-what-to-expect-and-what-not-to-expect-9f90e5362408?source=read_next_recirc-----38bfac47a322----3---------------------a5e8a73d_ba23_4577_a9b6_da571786e55d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9f90e5362408&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40don-lim%2Fgpt-5-is-finally-here-what-to-expect-and-what-not-to-expect-9f90e5362408&source=-----38bfac47a322----3-----------------bookmark_preview----a5e8a73d_ba23_4577_a9b6_da571786e55d-------)


---

## The Data Entrepreneurs

Source: https://medium.com/the-data-entrepreneurs/i-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377
Date fetched: 2024-11-10T01:50:51.254036

---

Title: I Built an AI App in 4 Days — here’s how I did it | by Shaw Talebi | The Data Entrepreneurs

URL Source: https://medium.com/the-data-entrepreneurs/i-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377

Published Time: 2024-10-30T18:08:44.118Z

Markdown Content:
I Built an AI App in 4 Days — here’s how I did it | by Shaw Talebi | The Data Entrepreneurs
===============
 

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

**I Built an AI App in 4 Days** — H**ere’s How I Did It.**
==========================================================

(as a data scientist with no web dev experience)
------------------------------------------------

[![Image 2: Shaw Talebi](https://miro.medium.com/v2/resize:fill:88:88/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=post_page---byline--2eb805783377--------------------------------)

[![Image 3: The Data Entrepreneurs](https://miro.medium.com/v2/da:true/resize:fill:48:48/1*pT7NF0Az25U4oiAEoUJzww.gif)](https://medium.com/the-data-entrepreneurs?source=post_page---byline--2eb805783377--------------------------------)

[Shaw Talebi](https://medium.com/@shawhin?source=post_page---byline--2eb805783377--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff3998e1cd186&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=post_page-f3998e1cd186--byline--2eb805783377---------------------post_header-----------)

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=post_page---byline--2eb805783377--------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fthe-data-entrepreneurs%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=---header_actions--2eb805783377---------------------clap_footer-----------)

807

24

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=---header_actions--2eb805783377---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=---header_actions--2eb805783377---------------------post_audio_button-----------)

Technology makes the world move faster. We are seeing this (yet again) today with AI. Using tools like Cursor, **developers can build 5–10X faster than before**. I personally experienced this recently when building my first-ever web application. In this post, I’ll walk through this experience and the tools to deploy this app in just 4 days.

![Image 4: a rocket is flying through the clouds](https://miro.medium.com/v2/resize:fit:700/1*AQxpS8eSQzM5S0swo0i-aw.png)

Image from Canva.

Although most data scientists use Python to process data and train models, **creating consumer software is a different ballgame**. This is a problem for me because, as a solo entrepreneur, I don’t have a team (or capital) to compensate for my inability.

With my savings on track to hit $0 this quarter, I was more motivated than ever to learn this skill set. To do this, I set the goal of launching 1 product every month this quarter.

The first such product is a tool to convert YouTube videos into blog posts (called y2b). **I launched the initial prototype for this app in 4 days**, and here, I will share exactly how I…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377%3Fsource%3D-----2eb805783377---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----2eb805783377---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377%3Fsource%3D-----2eb805783377---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----2eb805783377---------------------post_regwall-----------)

Sign up with email

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=-----2eb805783377---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fthe-data-entrepreneurs%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=---footer_actions--2eb805783377---------------------clap_footer-----------)

807

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fthe-data-entrepreneurs%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=---footer_actions--2eb805783377---------------------clap_footer-----------)

807

24

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=---footer_actions--2eb805783377---------------------bookmark_footer-----------)

[![Image 5: Shaw Talebi](https://miro.medium.com/v2/resize:fill:144:144/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=post_page---post_author_info--2eb805783377--------------------------------)

[![Image 6: The Data Entrepreneurs](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*pT7NF0Az25U4oiAEoUJzww.gif)](https://medium.com/the-data-entrepreneurs?source=post_page---post_author_info--2eb805783377--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F3ec6dd6333f3&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&newsletterV3=f3998e1cd186&newsletterV3Id=3ec6dd6333f3&user=Shaw+Talebi&userId=f3998e1cd186&source=---post_author_info--2eb805783377---------------------subscribe_user-----------)

·Editor for

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=post_page---post_author_info--2eb805783377--------------------------------)

Data Scientist | PhD, Physics

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F3ec6dd6333f3&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&newsletterV3=f3998e1cd186&newsletterV3Id=3ec6dd6333f3&user=Shaw+Talebi&userId=f3998e1cd186&source=---post_author_info--2eb805783377---------------------subscribe_user-----------)

More from Shaw Talebi and The Data Entrepreneurs
------------------------------------------------

![Image 7: 5 AI Projects You Can Build This Weekend (with Python)](https://miro.medium.com/v2/resize:fit:679/1*YMwyctXXY6dsjyW_CVv0lQ.png)

[![Image 8: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Towards Data Science](https://medium.com/towards-data-science?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[5 AI Projects You Can Build This Weekend (with Python) ------------------------------------------------------ ### From beginner-friendly to advanced](https://medium.com/towards-data-science/5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[3.7K 59](https://medium.com/towards-data-science/5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc57724e9c461&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461&source=-----2eb805783377----0-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

![Image 9: How to Freelance as a Data Scientist](https://miro.medium.com/v2/resize:fit:679/0*Ddrvuuhdcp8vQ44S)

[![Image 10: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[How to Freelance as a Data Scientist ------------------------------------ ### Asking successful freelancers how they do it](https://medium.com/the-data-entrepreneurs/how-to-freelance-as-a-data-scientist-ca9182999595?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[608 21](https://medium.com/the-data-entrepreneurs/how-to-freelance-as-a-data-scientist-ca9182999595?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fca9182999595&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fhow-to-freelance-as-a-data-scientist-ca9182999595&source=-----2eb805783377----1-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

![Image 11: I Spent $2,995 on Nassim Taleb’s Risk Taking Course — Here’s what I learned](https://miro.medium.com/v2/resize:fit:679/0*mMWok0ckH57WJibM)

[![Image 12: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[I Spent $2,995 on Nassim Taleb’s Risk Taking Course — Here’s what I learned --------------------------------------------------------------------------- ### Lessons and reflections from RWRI #19](https://medium.com/the-data-entrepreneurs/i-spent-2-995-on-nassim-talebs-risk-taking-course-here-s-what-i-learned-c442a55a2c64?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

Aug 23

[2.5K 44](https://medium.com/the-data-entrepreneurs/i-spent-2-995-on-nassim-talebs-risk-taking-course-here-s-what-i-learned-c442a55a2c64?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc442a55a2c64&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-spent-2-995-on-nassim-talebs-risk-taking-course-here-s-what-i-learned-c442a55a2c64&source=-----2eb805783377----2-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

![Image 13: Fine-Tuning BERT for Text Classification](https://miro.medium.com/v2/resize:fit:679/1*S-5K3D3dt8EH_S2eLE8aSQ.png)

[![Image 14: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Towards Data Science](https://medium.com/towards-data-science?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Fine-Tuning BERT for Text Classification ---------------------------------------- ### A hackable example with Python code](https://medium.com/towards-data-science/fine-tuning-bert-for-text-classification-a01f89b179fc?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[390 3](https://medium.com/towards-data-science/fine-tuning-bert-for-text-classification-a01f89b179fc?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa01f89b179fc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ffine-tuning-bert-for-text-classification-a01f89b179fc&source=-----2eb805783377----3-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[See all from Shaw Talebi](https://medium.com/@shawhin?source=post_page-----2eb805783377--------------------------------)

[See all from The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=post_page-----2eb805783377--------------------------------)

[![Image 16: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Stackademic](https://medium.com/stackademic?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[4.1K 22](https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[![Image 18: Richardson Gunde](https://miro.medium.com/v2/resize:fill:20:20/1*tp2uj3tur89cbR2GW0SrDQ.png)](https://medium.com/@honeyricky1m3?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Richardson Gunde](https://medium.com/@honeyricky1m3?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[AI Advances](https://medium.com/ai-advances?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[847 11](https://medium.com/ai-advances/the-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe57882dee7f8&operation=register&redirect=https%3A%2F%2Fai.gopubby.com%2Fthe-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8&source=-----2eb805783377----1-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[![Image 32: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

![Image 33: Claude 3.5 — The King of Document Intelligence](https://miro.medium.com/v2/resize:fit:679/1*n2XchxiV7CA0vkMETuBEHg.jpeg)

[![Image 34: Júlio Almeida](https://miro.medium.com/v2/resize:fill:20:20/1*8FTxz2UIRWokTjxMNci4ZQ.jpeg)](https://medium.com/@enoch3712?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Júlio Almeida](https://medium.com/@enoch3712?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Level Up Coding](https://medium.com/gitconnected?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Claude 3.5 — The King of Document Intelligence ---------------------------------------------- ### Achieving Near-Perfect Document Intelligence with Claude 3.5 Sonnet and Haiku. Classification, Splitting, and Extraction](https://medium.com/gitconnected/claude-3-5-the-king-of-document-intelligence-f57bea1d209d?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[760 10](https://medium.com/gitconnected/claude-3-5-the-king-of-document-intelligence-f57bea1d209d?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff57bea1d209d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-3-5-the-king-of-document-intelligence-f57bea1d209d&source=-----2eb805783377----1-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

![Image 35: Microsoft launches a new generative AI script: GenAIScript!](https://miro.medium.com/v2/resize:fit:679/0*KmoPYnUmJHXMRfP4)

[![Image 36: Xiuer Old](https://miro.medium.com/v2/resize:fill:20:20/1*cNgqwnMvbWQEhvuAhKkb9Q.png)](https://medium.com/@xiuerold?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Xiuer Old](https://medium.com/@xiuerold?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[JavaScript in Plain English](https://medium.com/javascript-in-plain-english?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Microsoft launches a new generative AI script: GenAIScript! ----------------------------------------------------------- ### Microsoft recently announced the launch of a new generative AI script: GenAIScript!](https://medium.com/javascript-in-plain-english/microsoft-launches-a-new-generative-ai-script-genaiscript-bc6dbe31bfee?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[238 3](https://medium.com/javascript-in-plain-english/microsoft-launches-a-new-generative-ai-script-genaiscript-bc6dbe31bfee?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbc6dbe31bfee&operation=register&redirect=https%3A%2F%2Fjavascript.plainenglish.io%2Fmicrosoft-launches-a-new-generative-ai-script-genaiscript-bc6dbe31bfee&source=-----2eb805783377----2-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

![Image 37: The HuggingFace dataset card showing an example RAG evaluation dataset that we generated.](https://miro.medium.com/v2/resize:fit:679/1*aYb8AgzctiTtUYofqQq9ug.png)

[![Image 38: Dr. Leon Eversberg](https://miro.medium.com/v2/resize:fill:20:20/1*s0Z_EQ6__8CxvIXDd2tYGg.png)](https://medium.com/@leoneversberg?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Dr. Leon Eversberg](https://medium.com/@leoneversberg?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Towards Data Science](https://medium.com/towards-data-science?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[How to Create a RAG Evaluation Dataset From Documents ----------------------------------------------------- ### Automatically create domain-specific datasets in any language using LLMs](https://medium.com/towards-data-science/how-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[485 2](https://medium.com/towards-data-science/how-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F140daa3cbe71&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71&source=-----2eb805783377----3-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

## Visual Content Analysis

### Image Analysis
Title: I Built an AI App in 4 Days — here’s how I did it | by Shaw Talebi | The Data Entrepreneurs

URL Source: https://medium.com/the-data-entrepreneurs/i-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377

Published Time: 2024-10-30T18:08:44.118Z

Markdown Content:
I Built an AI App in 4 Days — here’s how I did it | by Shaw Talebi | The Data Entrepreneurs
===============
 

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

**I Built an AI App in 4 Days** — H**ere’s How I Did It.**
==========================================================

(as a data scientist with no web dev experience)
------------------------------------------------

[![Image 2: Shaw Talebi](https://miro.medium.com/v2/resize:fill:88:88/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=post_page---byline--2eb805783377--------------------------------)

[![Image 3: The Data Entrepreneurs](https://miro.medium.com/v2/da:true/resize:fill:48:48/1*pT7NF0Az25U4oiAEoUJzww.gif)](https://medium.com/the-data-entrepreneurs?source=post_page---byline--2eb805783377--------------------------------)

[Shaw Talebi](https://medium.com/@shawhin?source=post_page---byline--2eb805783377--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff3998e1cd186&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=post_page-f3998e1cd186--byline--2eb805783377---------------------post_header-----------)

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=post_page---byline--2eb805783377--------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fthe-data-entrepreneurs%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=---header_actions--2eb805783377---------------------clap_footer-----------)

807

24

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=---header_actions--2eb805783377---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=---header_actions--2eb805783377---------------------post_audio_button-----------)

Technology makes the world move faster. We are seeing this (yet again) today with AI. Using tools like Cursor, **developers can build 5–10X faster than before**. I personally experienced this recently when building my first-ever web application. In this post, I’ll walk through this experience and the tools to deploy this app in just 4 days.

![Image 4: a rocket is flying through the clouds](https://miro.medium.com/v2/resize:fit:700/1*AQxpS8eSQzM5S0swo0i-aw.png)

Image from Canva.

Although most data scientists use Python to process data and train models, **creating consumer software is a different ballgame**. This is a problem for me because, as a solo entrepreneur, I don’t have a team (or capital) to compensate for my inability.

With my savings on track to hit $0 this quarter, I was more motivated than ever to learn this skill set. To do this, I set the goal of launching 1 product every month this quarter.

The first such product is a tool to convert YouTube videos into blog posts (called y2b). **I launched the initial prototype for this app in 4 days**, and here, I will share exactly how I…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377%3Fsource%3D-----2eb805783377---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----2eb805783377---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377%3Fsource%3D-----2eb805783377---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----2eb805783377---------------------post_regwall-----------)

Sign up with email

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=-----2eb805783377---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fthe-data-entrepreneurs%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=---footer_actions--2eb805783377---------------------clap_footer-----------)

807

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fthe-data-entrepreneurs%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&user=Shaw+Talebi&userId=f3998e1cd186&source=---footer_actions--2eb805783377---------------------clap_footer-----------)

807

24

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2eb805783377&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&source=---footer_actions--2eb805783377---------------------bookmark_footer-----------)

[![Image 5: Shaw Talebi](https://miro.medium.com/v2/resize:fill:144:144/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=post_page---post_author_info--2eb805783377--------------------------------)

[![Image 6: The Data Entrepreneurs](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*pT7NF0Az25U4oiAEoUJzww.gif)](https://medium.com/the-data-entrepreneurs?source=post_page---post_author_info--2eb805783377--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F3ec6dd6333f3&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&newsletterV3=f3998e1cd186&newsletterV3Id=3ec6dd6333f3&user=Shaw+Talebi&userId=f3998e1cd186&source=---post_author_info--2eb805783377---------------------subscribe_user-----------)

·Editor for

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=post_page---post_author_info--2eb805783377--------------------------------)

Data Scientist | PhD, Physics

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F3ec6dd6333f3&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-built-an-ai-app-in-4-days-heres-how-i-did-it-2eb805783377&newsletterV3=f3998e1cd186&newsletterV3Id=3ec6dd6333f3&user=Shaw+Talebi&userId=f3998e1cd186&source=---post_author_info--2eb805783377---------------------subscribe_user-----------)

More from Shaw Talebi and The Data Entrepreneurs
------------------------------------------------

![Image 7: 5 AI Projects You Can Build This Weekend (with Python)](https://miro.medium.com/v2/resize:fit:679/1*YMwyctXXY6dsjyW_CVv0lQ.png)

[![Image 8: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Towards Data Science](https://medium.com/towards-data-science?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[5 AI Projects You Can Build This Weekend (with Python) ------------------------------------------------------ ### From beginner-friendly to advanced](https://medium.com/towards-data-science/5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[3.7K 59](https://medium.com/towards-data-science/5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461?source=author_recirc-----2eb805783377----0---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc57724e9c461&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F5-ai-projects-you-can-build-this-weekend-with-python-c57724e9c461&source=-----2eb805783377----0-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

![Image 9: How to Freelance as a Data Scientist](https://miro.medium.com/v2/resize:fit:679/0*Ddrvuuhdcp8vQ44S)

[![Image 10: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[How to Freelance as a Data Scientist ------------------------------------ ### Asking successful freelancers how they do it](https://medium.com/the-data-entrepreneurs/how-to-freelance-as-a-data-scientist-ca9182999595?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[608 21](https://medium.com/the-data-entrepreneurs/how-to-freelance-as-a-data-scientist-ca9182999595?source=author_recirc-----2eb805783377----1---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fca9182999595&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fhow-to-freelance-as-a-data-scientist-ca9182999595&source=-----2eb805783377----1-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

![Image 11: I Spent $2,995 on Nassim Taleb’s Risk Taking Course — Here’s what I learned](https://miro.medium.com/v2/resize:fit:679/0*mMWok0ckH57WJibM)

[![Image 12: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[I Spent $2,995 on Nassim Taleb’s Risk Taking Course — Here’s what I learned --------------------------------------------------------------------------- ### Lessons and reflections from RWRI #19](https://medium.com/the-data-entrepreneurs/i-spent-2-995-on-nassim-talebs-risk-taking-course-here-s-what-i-learned-c442a55a2c64?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

Aug 23

[2.5K 44](https://medium.com/the-data-entrepreneurs/i-spent-2-995-on-nassim-talebs-risk-taking-course-here-s-what-i-learned-c442a55a2c64?source=author_recirc-----2eb805783377----2---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc442a55a2c64&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fthe-data-entrepreneurs%2Fi-spent-2-995-on-nassim-talebs-risk-taking-course-here-s-what-i-learned-c442a55a2c64&source=-----2eb805783377----2-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

![Image 13: Fine-Tuning BERT for Text Classification](https://miro.medium.com/v2/resize:fit:679/1*S-5K3D3dt8EH_S2eLE8aSQ.png)

[![Image 14: Shaw Talebi](https://miro.medium.com/v2/resize:fill:20:20/1*mhVX2L2LGQM4XZNwvU7H5A.jpeg)](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Shaw Talebi](https://medium.com/@shawhin?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Towards Data Science](https://medium.com/towards-data-science?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[Fine-Tuning BERT for Text Classification ---------------------------------------- ### A hackable example with Python code](https://medium.com/towards-data-science/fine-tuning-bert-for-text-classification-a01f89b179fc?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[390 3](https://medium.com/towards-data-science/fine-tuning-bert-for-text-classification-a01f89b179fc?source=author_recirc-----2eb805783377----3---------------------b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa01f89b179fc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ffine-tuning-bert-for-text-classification-a01f89b179fc&source=-----2eb805783377----3-----------------bookmark_preview----b8b250e7_d6e8_4dce_9413_083fe1b5a95d-------)

[See all from Shaw Talebi](https://medium.com/@shawhin?source=post_page-----2eb805783377--------------------------------)

[See all from The Data Entrepreneurs](https://medium.com/the-data-entrepreneurs?source=post_page-----2eb805783377--------------------------------)

[![Image 16: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Stackademic](https://medium.com/stackademic?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Python is No More The King of Data Science ------------------------------------------ ### 5 Reasons Why Python is Losing Its Crown](https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[4.1K 22](https://medium.com/stackademic/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[![Image 18: Richardson Gunde](https://miro.medium.com/v2/resize:fill:20:20/1*tp2uj3tur89cbR2GW0SrDQ.png)](https://medium.com/@honeyricky1m3?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Richardson Gunde](https://medium.com/@honeyricky1m3?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[AI Advances](https://medium.com/ai-advances?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[847 11](https://medium.com/ai-advances/the-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fe57882dee7f8&operation=register&redirect=https%3A%2F%2Fai.gopubby.com%2Fthe-pdf-extraction-revolution-why-pymupdf4llm-is-your-new-best-friend-and-llamaparse-is-crying-e57882dee7f8&source=-----2eb805783377----1-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[![Image 32: Harendra](https://miro.medium.com/v2/resize:fill:20:20/1*uTEzlRvlNBr3ralJoTQkmg.jpeg)](https://medium.com/@harendra21?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Harendra](https://medium.com/@harendra21?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[3.3K 36](https://medium.com/@harendra21/how-i-am-using-a-lifetime-100-free-server-bd241e3a347a?source=read_next_recirc-----2eb805783377----0---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

![Image 33: Claude 3.5 — The King of Document Intelligence](https://miro.medium.com/v2/resize:fit:679/1*n2XchxiV7CA0vkMETuBEHg.jpeg)

[![Image 34: Júlio Almeida](https://miro.medium.com/v2/resize:fill:20:20/1*8FTxz2UIRWokTjxMNci4ZQ.jpeg)](https://medium.com/@enoch3712?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Júlio Almeida](https://medium.com/@enoch3712?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Level Up Coding](https://medium.com/gitconnected?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Claude 3.5 — The King of Document Intelligence ---------------------------------------------- ### Achieving Near-Perfect Document Intelligence with Claude 3.5 Sonnet and Haiku. Classification, Splitting, and Extraction](https://medium.com/gitconnected/claude-3-5-the-king-of-document-intelligence-f57bea1d209d?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[760 10](https://medium.com/gitconnected/claude-3-5-the-king-of-document-intelligence-f57bea1d209d?source=read_next_recirc-----2eb805783377----1---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff57bea1d209d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-3-5-the-king-of-document-intelligence-f57bea1d209d&source=-----2eb805783377----1-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

![Image 35: Microsoft launches a new generative AI script: GenAIScript!](https://miro.medium.com/v2/resize:fit:679/0*KmoPYnUmJHXMRfP4)

[![Image 36: Xiuer Old](https://miro.medium.com/v2/resize:fill:20:20/1*cNgqwnMvbWQEhvuAhKkb9Q.png)](https://medium.com/@xiuerold?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Xiuer Old](https://medium.com/@xiuerold?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[JavaScript in Plain English](https://medium.com/javascript-in-plain-english?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Microsoft launches a new generative AI script: GenAIScript! ----------------------------------------------------------- ### Microsoft recently announced the launch of a new generative AI script: GenAIScript!](https://medium.com/javascript-in-plain-english/microsoft-launches-a-new-generative-ai-script-genaiscript-bc6dbe31bfee?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[238 3](https://medium.com/javascript-in-plain-english/microsoft-launches-a-new-generative-ai-script-genaiscript-bc6dbe31bfee?source=read_next_recirc-----2eb805783377----2---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbc6dbe31bfee&operation=register&redirect=https%3A%2F%2Fjavascript.plainenglish.io%2Fmicrosoft-launches-a-new-generative-ai-script-genaiscript-bc6dbe31bfee&source=-----2eb805783377----2-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

![Image 37: The HuggingFace dataset card showing an example RAG evaluation dataset that we generated.](https://miro.medium.com/v2/resize:fit:679/1*aYb8AgzctiTtUYofqQq9ug.png)

[![Image 38: Dr. Leon Eversberg](https://miro.medium.com/v2/resize:fill:20:20/1*s0Z_EQ6__8CxvIXDd2tYGg.png)](https://medium.com/@leoneversberg?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Dr. Leon Eversberg](https://medium.com/@leoneversberg?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[Towards Data Science](https://medium.com/towards-data-science?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[How to Create a RAG Evaluation Dataset From Documents ----------------------------------------------------- ### Automatically create domain-specific datasets in any language using LLMs](https://medium.com/towards-data-science/how-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[485 2](https://medium.com/towards-data-science/how-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71?source=read_next_recirc-----2eb805783377----3---------------------b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F140daa3cbe71&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71&source=-----2eb805783377----3-----------------bookmark_preview----b07e57e9_00a4_4bbe_93df_3405be1fea5a-------)


---



# Bundle: finance_articles

# Finance Articles Collection

## Table of Contents

### General
- [Towards Data Science](#towards-data-science)
- [Towards Data Science](#towards-data-science)

---

# General

## Towards Data Science

Source: https://medium.com/towards-data-science/top-data-science-career-questions-answered-abd3e3c085cc
Date fetched: 2024-11-10T01:52:10.233049

---

Title: Top Data Science Career Questions, Answered - Towards Data Science

URL Source: https://medium.com/towards-data-science/top-data-science-career-questions-answered-abd3e3c085cc

Markdown Content:
Top Data Science Career Questions, Answered | by Haden Pelletier | Nov, 2024 | Towards Data Science
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Top Data Science Career Questions, Answered
===========================================

I’ve been a data scientist for over 3 years. This is what most people want to know about the field.
---------------------------------------------------------------------------------------------------

[![Image 2: Haden Pelletier](https://miro.medium.com/v2/resize:fill:88:88/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=post_page---byline--abd3e3c085cc--------------------------------)

[Haden Pelletier](https://medium.com/@pelletierhaden?source=post_page---byline--abd3e3c085cc--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb14d1de976eb&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=post_page-b14d1de976eb--byline--abd3e3c085cc---------------------post_header-----------)

17 hours ago

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Fabd3e3c085cc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=---header_actions--abd3e3c085cc---------------------clap_footer-----------)

31

![Image 4: a computer monitor with a map on it](https://miro.medium.com/v2/resize:fit:700/1*VctqAv-l_o4Gr9IEbNO2YA@2x.jpeg)

Photo by [Clay Banks](http://claybanks.info/) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

What does a data scientist do?
==============================

Most people are both impressed and confused when I tell them I’m a data scientist.

Impressed because it’s considered such a fancy and prestigious title nowadays (though some will still call us statisticians who can code).

Confused because … what does data science mean, really? And what do we do?

Well, it depends.

**On the domain, the company, and the team itself.**

But in general, data science encompasses the following categories of work:

*   **Databases and data engineering** — Many data scientists work closely with databases, whether that’s loading and querying large amounts of data, building data pipelines, or cleaning and preparing data for analysis. At my last company, I used SQL regularly to access our database in order to query data needed to build ML models. I also found myself creating and altering tables in order to store results from models and other analyses.
*   **Data analytics and visualization** — Data visualization involves not only analyzing the data but…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc%3Fsource%3D-----abd3e3c085cc---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----abd3e3c085cc---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc%3Fsource%3D-----abd3e3c085cc---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----abd3e3c085cc---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=-----abd3e3c085cc---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Fabd3e3c085cc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=---footer_actions--abd3e3c085cc---------------------clap_footer-----------)

31

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Fabd3e3c085cc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=---footer_actions--abd3e3c085cc---------------------clap_footer-----------)

31

[![Image 5: Haden Pelletier](https://miro.medium.com/v2/resize:fill:144:144/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=post_page---post_author_info--abd3e3c085cc--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb14d1de976eb&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=post_page-b14d1de976eb--post_author_info--abd3e3c085cc---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fdf8b14e59fe5&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&newsletterV3=b14d1de976eb&newsletterV3Id=df8b14e59fe5&user=Haden+Pelletier&userId=b14d1de976eb&source=---post_author_info--abd3e3c085cc---------------------subscribe_user-----------)

Data scientist, traveler, & writer.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb14d1de976eb&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=post_page-b14d1de976eb--post_author_info--abd3e3c085cc---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fdf8b14e59fe5&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&newsletterV3=b14d1de976eb&newsletterV3Id=df8b14e59fe5&user=Haden+Pelletier&userId=b14d1de976eb&source=---post_author_info--abd3e3c085cc---------------------subscribe_user-----------)

![Image 7: How to Negotiate Your Salary as a Data Scientist](https://miro.medium.com/v2/resize:fit:679/0*fRwCyanMJ6Oax2y5)

[![Image 8: Haden Pelletier](https://miro.medium.com/v2/resize:fill:20:20/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Haden Pelletier](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[How to Negotiate Your Salary as a Data Scientist ------------------------------------------------ ### And how much I made my first year](https://medium.com/how-to-negotiate-your-salary-as-a-data-scientist-4c6ce176b2a5?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[187 4](https://medium.com/how-to-negotiate-your-salary-as-a-data-scientist-4c6ce176b2a5?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6ce176b2a5&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-negotiate-your-salary-as-a-data-scientist-4c6ce176b2a5&source=-----abd3e3c085cc----0-----------------bookmark_preview----905af031_0fe3_477d_a960_25f39c760700-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----abd3e3c085cc----1---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----abd3e3c085cc----1---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----abd3e3c085cc----1---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----abd3e3c085cc----1-----------------bookmark_preview----905af031_0fe3_477d_a960_25f39c760700-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----abd3e3c085cc----2---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----abd3e3c085cc----2---------------------905af031_0fe3_477d_a960_25f39c760700-------)

![Image 13: How to Network as a Data Scientist](https://miro.medium.com/v2/resize:fit:679/1*WTuPGF-Nh3VMmZlfQSQeLw@2x.jpeg)

[![Image 14: Haden Pelletier](https://miro.medium.com/v2/resize:fill:20:20/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Haden Pelletier](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[How to Network as a Data Scientist ---------------------------------- ### Times are changing — if you want to get into data science, you have to network like you mean it.](https://medium.com/how-to-network-as-a-data-scientist-12fd3ed8d176?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[478 6](https://medium.com/how-to-network-as-a-data-scientist-12fd3ed8d176?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F12fd3ed8d176&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-network-as-a-data-scientist-12fd3ed8d176&source=-----abd3e3c085cc----3-----------------bookmark_preview----905af031_0fe3_477d_a960_25f39c760700-------)

[![Image 16: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:20:20/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Saankhya Mondal](https://saankhya.medium.com/?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[300 10](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----abd3e3c085cc----0-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

![Image 17: Best Data Science Certifications In 2025 To Start Your Career](https://miro.medium.com/v2/resize:fit:679/1*NAz1NLTBwnjQGgHWv6mp-Q.png)

[![Image 18: Divyanshi kulkarni](https://miro.medium.com/v2/resize:fill:20:20/0*dg-3hj8dvaBaN44S)](https://medium.com/@divyanshikulkarni11?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Divyanshi kulkarni](https://medium.com/@divyanshikulkarni11?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Best Data Science Certifications In 2025 To Start Your Career ------------------------------------------------------------- ### With a data science certification, individuals can learn industry-relevant skills and validate their skills and knowledge. Data science…](https://medium.com/@divyanshikulkarni11/best-data-science-certifications-in-2025-to-start-your-career-b06b548e5e54?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[26 1](https://medium.com/@divyanshikulkarni11/best-data-science-certifications-in-2025-to-start-your-career-b06b548e5e54?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fb06b548e5e54&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40divyanshikulkarni11%2Fbest-data-science-certifications-in-2025-to-start-your-career-b06b548e5e54&source=-----abd3e3c085cc----1-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

![Image 31: 3 Probability Questions I was asked in Walmart Data Scientist Interview](https://miro.medium.com/v2/resize:fit:679/1*5f1WO-mbx8fwBTQSs6F3zg.png)

[![Image 32: Lucas Samba](https://miro.medium.com/v2/resize:fill:20:20/1*R0PCZj_QUhumxixbZeUNAw.jpeg)](https://medium.com/@lucassamba?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Lucas Samba](https://medium.com/@lucassamba?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[3 Probability Questions I was asked in Walmart Data Scientist Interview ----------------------------------------------------------------------- ### Recently I got an opportunity to interview at Walmart for Data Scientist — 3 position. All thanks to a referral by my friend working at…](https://medium.com/@lucassamba/3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[461 12](https://medium.com/@lucassamba/3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff3cddba746d1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40lucassamba%2F3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1&source=-----abd3e3c085cc----0-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

[![Image 34: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----abd3e3c085cc----1-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

![Image 35: Top 5 Statistical Tests Every Data Scientist Should Know](https://miro.medium.com/v2/resize:fit:679/1*ZEaCasuiJry_OWfOZYbsMQ.png)

[![Image 36: Niveatha Manickavasagam](https://miro.medium.com/v2/resize:fill:20:20/1*54gUVuwoy6rAAtar36raXQ.jpeg)](https://medium.com/@niveathadmv?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Niveatha Manickavasagam](https://medium.com/@niveathadmv?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Code Like A Girl](https://code.likeagirl.io/?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Top 5 Statistical Tests Every Data Scientist Should Know -------------------------------------------------------- ### A Comprehensive Overview of Must-Know Statistical Methods](https://code.likeagirl.io/top-5-statistical-tests-every-data-scientist-should-know-11f205b230c2?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[195 4](https://code.likeagirl.io/top-5-statistical-tests-every-data-scientist-should-know-11f205b230c2?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F11f205b230c2&operation=register&redirect=https%3A%2F%2Fcode.likeagirl.io%2Ftop-5-statistical-tests-every-data-scientist-should-know-11f205b230c2&source=-----abd3e3c085cc----2-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

[![Image 38: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

## Visual Content Analysis

### Image Analysis
Title: Top Data Science Career Questions, Answered - Towards Data Science

URL Source: https://medium.com/towards-data-science/top-data-science-career-questions-answered-abd3e3c085cc

Markdown Content:
Top Data Science Career Questions, Answered | by Haden Pelletier | Nov, 2024 | Towards Data Science
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Top Data Science Career Questions, Answered
===========================================

I’ve been a data scientist for over 3 years. This is what most people want to know about the field.
---------------------------------------------------------------------------------------------------

[![Image 2: Haden Pelletier](https://miro.medium.com/v2/resize:fill:88:88/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=post_page---byline--abd3e3c085cc--------------------------------)

[Haden Pelletier](https://medium.com/@pelletierhaden?source=post_page---byline--abd3e3c085cc--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb14d1de976eb&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=post_page-b14d1de976eb--byline--abd3e3c085cc---------------------post_header-----------)

17 hours ago

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Fabd3e3c085cc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=---header_actions--abd3e3c085cc---------------------clap_footer-----------)

31

![Image 4: a computer monitor with a map on it](https://miro.medium.com/v2/resize:fit:700/1*VctqAv-l_o4Gr9IEbNO2YA@2x.jpeg)

Photo by [Clay Banks](http://claybanks.info/) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

What does a data scientist do?
==============================

Most people are both impressed and confused when I tell them I’m a data scientist.

Impressed because it’s considered such a fancy and prestigious title nowadays (though some will still call us statisticians who can code).

Confused because … what does data science mean, really? And what do we do?

Well, it depends.

**On the domain, the company, and the team itself.**

But in general, data science encompasses the following categories of work:

*   **Databases and data engineering** — Many data scientists work closely with databases, whether that’s loading and querying large amounts of data, building data pipelines, or cleaning and preparing data for analysis. At my last company, I used SQL regularly to access our database in order to query data needed to build ML models. I also found myself creating and altering tables in order to store results from models and other analyses.
*   **Data analytics and visualization** — Data visualization involves not only analyzing the data but…

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc%3Fsource%3D-----abd3e3c085cc---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----abd3e3c085cc---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc%3Fsource%3D-----abd3e3c085cc---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----abd3e3c085cc---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&source=-----abd3e3c085cc---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Fabd3e3c085cc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=---footer_actions--abd3e3c085cc---------------------clap_footer-----------)

31

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Fabd3e3c085cc&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=---footer_actions--abd3e3c085cc---------------------clap_footer-----------)

31

[![Image 5: Haden Pelletier](https://miro.medium.com/v2/resize:fill:144:144/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=post_page---post_author_info--abd3e3c085cc--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb14d1de976eb&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=post_page-b14d1de976eb--post_author_info--abd3e3c085cc---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fdf8b14e59fe5&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&newsletterV3=b14d1de976eb&newsletterV3Id=df8b14e59fe5&user=Haden+Pelletier&userId=b14d1de976eb&source=---post_author_info--abd3e3c085cc---------------------subscribe_user-----------)

Data scientist, traveler, & writer.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fb14d1de976eb&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&user=Haden+Pelletier&userId=b14d1de976eb&source=post_page-b14d1de976eb--post_author_info--abd3e3c085cc---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fdf8b14e59fe5&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ftop-data-science-career-questions-answered-abd3e3c085cc&newsletterV3=b14d1de976eb&newsletterV3Id=df8b14e59fe5&user=Haden+Pelletier&userId=b14d1de976eb&source=---post_author_info--abd3e3c085cc---------------------subscribe_user-----------)

![Image 7: How to Negotiate Your Salary as a Data Scientist](https://miro.medium.com/v2/resize:fit:679/0*fRwCyanMJ6Oax2y5)

[![Image 8: Haden Pelletier](https://miro.medium.com/v2/resize:fill:20:20/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Haden Pelletier](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[How to Negotiate Your Salary as a Data Scientist ------------------------------------------------ ### And how much I made my first year](https://medium.com/how-to-negotiate-your-salary-as-a-data-scientist-4c6ce176b2a5?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[187 4](https://medium.com/how-to-negotiate-your-salary-as-a-data-scientist-4c6ce176b2a5?source=author_recirc-----abd3e3c085cc----0---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c6ce176b2a5&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-negotiate-your-salary-as-a-data-scientist-4c6ce176b2a5&source=-----abd3e3c085cc----0-----------------bookmark_preview----905af031_0fe3_477d_a960_25f39c760700-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----abd3e3c085cc----1---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----abd3e3c085cc----1---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----abd3e3c085cc----1---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd299b638773b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b&source=-----abd3e3c085cc----1-----------------bookmark_preview----905af031_0fe3_477d_a960_25f39c760700-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----abd3e3c085cc----2---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----abd3e3c085cc----2---------------------905af031_0fe3_477d_a960_25f39c760700-------)

![Image 13: How to Network as a Data Scientist](https://miro.medium.com/v2/resize:fit:679/1*WTuPGF-Nh3VMmZlfQSQeLw@2x.jpeg)

[![Image 14: Haden Pelletier](https://miro.medium.com/v2/resize:fill:20:20/1*a0nmhdOP6fSXKTkniLMsNw@2x.jpeg)](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[Haden Pelletier](https://medium.com/@pelletierhaden?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[How to Network as a Data Scientist ---------------------------------- ### Times are changing — if you want to get into data science, you have to network like you mean it.](https://medium.com/how-to-network-as-a-data-scientist-12fd3ed8d176?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[478 6](https://medium.com/how-to-network-as-a-data-scientist-12fd3ed8d176?source=author_recirc-----abd3e3c085cc----3---------------------905af031_0fe3_477d_a960_25f39c760700-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F12fd3ed8d176&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-network-as-a-data-scientist-12fd3ed8d176&source=-----abd3e3c085cc----3-----------------bookmark_preview----905af031_0fe3_477d_a960_25f39c760700-------)

[![Image 16: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:20:20/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Saankhya Mondal](https://saankhya.medium.com/?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Towards Data Science](https://towardsdatascience.com/?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[300 10](https://medium.com/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----abd3e3c085cc----0-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

![Image 17: Best Data Science Certifications In 2025 To Start Your Career](https://miro.medium.com/v2/resize:fit:679/1*NAz1NLTBwnjQGgHWv6mp-Q.png)

[![Image 18: Divyanshi kulkarni](https://miro.medium.com/v2/resize:fill:20:20/0*dg-3hj8dvaBaN44S)](https://medium.com/@divyanshikulkarni11?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Divyanshi kulkarni](https://medium.com/@divyanshikulkarni11?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Best Data Science Certifications In 2025 To Start Your Career ------------------------------------------------------------- ### With a data science certification, individuals can learn industry-relevant skills and validate their skills and knowledge. Data science…](https://medium.com/@divyanshikulkarni11/best-data-science-certifications-in-2025-to-start-your-career-b06b548e5e54?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[26 1](https://medium.com/@divyanshikulkarni11/best-data-science-certifications-in-2025-to-start-your-career-b06b548e5e54?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fb06b548e5e54&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40divyanshikulkarni11%2Fbest-data-science-certifications-in-2025-to-start-your-career-b06b548e5e54&source=-----abd3e3c085cc----1-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

![Image 31: 3 Probability Questions I was asked in Walmart Data Scientist Interview](https://miro.medium.com/v2/resize:fit:679/1*5f1WO-mbx8fwBTQSs6F3zg.png)

[![Image 32: Lucas Samba](https://miro.medium.com/v2/resize:fill:20:20/1*R0PCZj_QUhumxixbZeUNAw.jpeg)](https://medium.com/@lucassamba?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Lucas Samba](https://medium.com/@lucassamba?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[3 Probability Questions I was asked in Walmart Data Scientist Interview ----------------------------------------------------------------------- ### Recently I got an opportunity to interview at Walmart for Data Scientist — 3 position. All thanks to a referral by my friend working at…](https://medium.com/@lucassamba/3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[461 12](https://medium.com/@lucassamba/3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1?source=read_next_recirc-----abd3e3c085cc----0---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff3cddba746d1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40lucassamba%2F3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1&source=-----abd3e3c085cc----0-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

[![Image 34: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----abd3e3c085cc----1---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F476f1e3191b3&operation=register&redirect=https%3A%2F%2Fblog.stackademic.com%2Fis-python-still-the-king-of-data-science-476f1e3191b3&source=-----abd3e3c085cc----1-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

![Image 35: Top 5 Statistical Tests Every Data Scientist Should Know](https://miro.medium.com/v2/resize:fit:679/1*ZEaCasuiJry_OWfOZYbsMQ.png)

[![Image 36: Niveatha Manickavasagam](https://miro.medium.com/v2/resize:fill:20:20/1*54gUVuwoy6rAAtar36raXQ.jpeg)](https://medium.com/@niveathadmv?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Niveatha Manickavasagam](https://medium.com/@niveathadmv?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Code Like A Girl](https://code.likeagirl.io/?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Top 5 Statistical Tests Every Data Scientist Should Know -------------------------------------------------------- ### A Comprehensive Overview of Must-Know Statistical Methods](https://code.likeagirl.io/top-5-statistical-tests-every-data-scientist-should-know-11f205b230c2?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[195 4](https://code.likeagirl.io/top-5-statistical-tests-every-data-scientist-should-know-11f205b230c2?source=read_next_recirc-----abd3e3c085cc----2---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F11f205b230c2&operation=register&redirect=https%3A%2F%2Fcode.likeagirl.io%2Ftop-5-statistical-tests-every-data-scientist-should-know-11f205b230c2&source=-----abd3e3c085cc----2-----------------bookmark_preview----7b22311a_610c_4919_9724_1aa1b3db0654-------)

[![Image 38: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----abd3e3c085cc----3---------------------7b22311a_610c_4919_9724_1aa1b3db0654-------)


---

## Towards Data Science

Source: https://medium.com/towards-data-science/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a
Date fetched: 2024-11-10T01:53:20.385105

---

Title: Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists

URL Source: https://medium.com/towards-data-science/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a

Published Time: 2024-11-06T18:16:48.468Z

Markdown Content:
Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists | by Saankhya Mondal | Nov, 2024 | Towards Data Science
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists
==========================================================================

Key Technical Skills You Need to Kick-start Your Career in Data Science
-----------------------------------------------------------------------

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--byline--96e5072bd19a---------------------post_header-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---header_actions--96e5072bd19a---------------------clap_footer-----------)

300

10

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=---header_actions--96e5072bd19a---------------------post_audio_button-----------)

Are you curious about data science? Does math and artificial intelligence excite you? Do you want to explore data science and plan to pursue a data science career? Whether you’re unsure where to begin or just taking your first steps into data science, you’ve come to the right place. Trust me, this guide will help you take your first steps with confidence!

Non-members can click [here](https://medium.com/towards-data-science/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?sk=fc5e1cd546b7b858925252b2f09214a8) to read the full article.

Data science is one of the most exciting fields in which to work. It’s a multidisciplinary field that combines various techniques and tools to analyze complex datasets, build predictive models, and guide decision-making in businesses, research, and technology.

Data science is applied in various industries such as finance, healthcare, social media, travel, e-commerce, robotics, military, and espionage.

![Image 4: data science concept with various graphs and data](https://miro.medium.com/v2/resize:fit:700/1*o06jXpJ_dMBlIwnR1P7XwQ.png)

Image generated using GPT 4o

Myths and Truths about Data Science
===================================

The Internet has abundant information about how to start with data science, leading to myths and misconceptions about data science. The two most important misconceptions are —

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a%3Fsource%3D-----96e5072bd19a---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----96e5072bd19a---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a%3Fsource%3D-----96e5072bd19a---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----96e5072bd19a---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a%3Fsource%3D-----96e5072bd19a---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----96e5072bd19a---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----96e5072bd19a---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--96e5072bd19a---------------------clap_footer-----------)

300

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--96e5072bd19a---------------------clap_footer-----------)

300

10

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--96e5072bd19a---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F2189c683abab&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&newsletterV3=59f51d8e0df4&newsletterV3Id=2189c683abab&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---post_author_info--96e5072bd19a---------------------subscribe_user-----------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--96e5072bd19a---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F2189c683abab&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&newsletterV3=59f51d8e0df4&newsletterV3Id=2189c683abab&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---post_author_info--96e5072bd19a---------------------subscribe_user-----------)

[![Image 8: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:20:20/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----0---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----0---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----0---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

![Image 13: Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric](https://miro.medium.com/v2/resize:fit:679/0*U7MA1X95LAKAdchq)

[![Image 14: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:20:20/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric -------------------------------------------------------------------------- ### NDCG — The Rank-Aware Metric for Evaluating Recommendation Systems](https://medium.com/normalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[305 6](https://medium.com/normalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=-----96e5072bd19a----3-----------------bookmark_preview----9041e16a_ada4_44dc_8f90_40456674cd68-------)

[![Image 16: Dr. Leon Eversberg](https://miro.medium.com/v2/resize:fill:20:20/1*s0Z_EQ6__8CxvIXDd2tYGg.png)](https://medium.com/@leoneversberg?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Dr. Leon Eversberg](https://medium.com/@leoneversberg?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[485 2](https://medium.com/how-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F140daa3cbe71&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71&source=-----96e5072bd19a----0-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

![Image 17: An Introduction to Transformers in Machine Learning](https://miro.medium.com/v2/resize:fit:679/1*9X-RUNw78A25Vg5h8pjAVA.jpeg)

[![Image 18: Francesco Franco](https://miro.medium.com/v2/resize:fill:20:20/1*tv95qIzwoUpCIPRHa38M9w.jpeg)](https://medium.com/@francescofranco_39234?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Francesco Franco](https://medium.com/@francescofranco_39234?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[T3CH](https://medium.com/h7w?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[An Introduction to Transformers in Machine Learning --------------------------------------------------- ### When you read about Machine Learning in Natural Language Processing these days, all you hear is one thing — Transformers. Models based on…](https://medium.com/h7w/an-introduction-to-transformers-in-machine-learning-50c8a53af576?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[278 1](https://medium.com/h7w/an-introduction-to-transformers-in-machine-learning-50c8a53af576?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F50c8a53af576&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fh7w%2Fan-introduction-to-transformers-in-machine-learning-50c8a53af576&source=-----96e5072bd19a----1-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 34: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----96e5072bd19a----1-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 36: Lucas Samba](https://miro.medium.com/v2/resize:fill:20:20/1*R0PCZj_QUhumxixbZeUNAw.jpeg)](https://medium.com/@lucassamba?source=read_next_recirc-----96e5072bd19a----2---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Lucas Samba](https://medium.com/@lucassamba?source=read_next_recirc-----96e5072bd19a----2---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[461 12](https://medium.com/@lucassamba/3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1?source=read_next_recirc-----96e5072bd19a----2---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff3cddba746d1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40lucassamba%2F3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1&source=-----96e5072bd19a----2-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 38: Shenggang Li](https://miro.medium.com/v2/resize:fill:20:20/1*knqQWkDF7J-gf_A5p7ew5g.png)](https://medium.com/@datalev?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Shenggang Li](https://medium.com/@datalev?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Towards AI](https://pub.towardsai.net/?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[157 2](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa301f6028c73&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fexploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73&source=-----96e5072bd19a----3-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

## Visual Content Analysis

### Image Analysis
Title: Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists

URL Source: https://medium.com/towards-data-science/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a

Published Time: 2024-11-06T18:16:48.468Z

Markdown Content:
Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists | by Saankhya Mondal | Nov, 2024 | Towards Data Science
===============
 

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

Kickstart Your Data Science Journey — A Guide for Aspiring Data Scientists
==========================================================================

Key Technical Skills You Need to Kick-start Your Career in Data Science
-----------------------------------------------------------------------

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--byline--96e5072bd19a---------------------post_header-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---header_actions--96e5072bd19a---------------------clap_footer-----------)

300

10

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=---header_actions--96e5072bd19a---------------------post_audio_button-----------)

Are you curious about data science? Does math and artificial intelligence excite you? Do you want to explore data science and plan to pursue a data science career? Whether you’re unsure where to begin or just taking your first steps into data science, you’ve come to the right place. Trust me, this guide will help you take your first steps with confidence!

Non-members can click [here](https://medium.com/towards-data-science/kickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a?sk=fc5e1cd546b7b858925252b2f09214a8) to read the full article.

Data science is one of the most exciting fields in which to work. It’s a multidisciplinary field that combines various techniques and tools to analyze complex datasets, build predictive models, and guide decision-making in businesses, research, and technology.

Data science is applied in various industries such as finance, healthcare, social media, travel, e-commerce, robotics, military, and espionage.

![Image 4: data science concept with various graphs and data](https://miro.medium.com/v2/resize:fit:700/1*o06jXpJ_dMBlIwnR1P7XwQ.png)

Image generated using GPT 4o

Myths and Truths about Data Science
===================================

The Internet has abundant information about how to start with data science, leading to myths and misconceptions about data science. The two most important misconceptions are —

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a%3Fsource%3D-----96e5072bd19a---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----96e5072bd19a---------------------post_regwall-----------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a%3Fsource%3D-----96e5072bd19a---------------------post_regwall-----------%26skipOnboarding%3D1%7Cregister&source=-----96e5072bd19a---------------------post_regwall-----------)

[Sign up with email](https://medium.com/m/signin?redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a%3Fsource%3D-----96e5072bd19a---------------------post_regwall-----------%26skipOnboarding%3D1&operation=register&stepOverride=ENTER_EMAIL&source=-----96e5072bd19a---------------------post_regwall-----------)

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&source=-----96e5072bd19a---------------------post_regwall-----------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--96e5072bd19a---------------------clap_footer-----------)

300

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F96e5072bd19a&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---footer_actions--96e5072bd19a---------------------clap_footer-----------)

300

10

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--96e5072bd19a---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F2189c683abab&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&newsletterV3=59f51d8e0df4&newsletterV3Id=2189c683abab&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---post_author_info--96e5072bd19a---------------------subscribe_user-----------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F59f51d8e0df4&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&user=Saankhya+Mondal&userId=59f51d8e0df4&source=post_page-59f51d8e0df4--post_author_info--96e5072bd19a---------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F2189c683abab&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fkickstart-your-data-science-journey-a-guide-for-aspiring-data-scientists-96e5072bd19a&newsletterV3=59f51d8e0df4&newsletterV3Id=2189c683abab&user=Saankhya+Mondal&userId=59f51d8e0df4&source=---post_author_info--96e5072bd19a---------------------subscribe_user-----------)

[![Image 8: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:20:20/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----0---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----0---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----0---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[![Image 10: Satwiki De](https://miro.medium.com/v2/resize:fill:20:20/1*DUP9k15e2-cZj27IJxFCpQ.jpeg)](https://medium.com/@cleancoder?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Satwiki De](https://medium.com/@cleancoder?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[90 1](https://medium.com/what-did-i-learn-from-building-llm-applications-in-2024-part-1-d299b638773b?source=author_recirc-----96e5072bd19a----1---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[![Image 12: Aris Tsakpinis](https://miro.medium.com/v2/resize:fill:20:20/1*HiuDPBJ3_XhJLRi40lBb7Q.jpeg)](https://medium.com/@aris.tsakpinis?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Aris Tsakpinis](https://medium.com/@aris.tsakpinis?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Preference Alignment for Everyone! ---------------------------------- ### Frugal RLHF with multi-adapter PPO on Amazon SageMaker](https://medium.com/preference-alignment-for-everyone-2563cec4d10e?source=author_recirc-----96e5072bd19a----2---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

![Image 13: Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric](https://miro.medium.com/v2/resize:fit:679/0*U7MA1X95LAKAdchq)

[![Image 14: Saankhya Mondal](https://miro.medium.com/v2/resize:fill:20:20/1*TADxXNj_Fq5BqXipXvp1QQ.jpeg)](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Saankhya Mondal](https://saankhya.medium.com/?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Towards Data Science](https://towardsdatascience.com/?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[Normalized Discounted Cumulative Gain (NDCG) — The Ultimate Ranking Metric -------------------------------------------------------------------------- ### NDCG — The Rank-Aware Metric for Evaluating Recommendation Systems](https://medium.com/normalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[305 6](https://medium.com/normalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75?source=author_recirc-----96e5072bd19a----3---------------------9041e16a_ada4_44dc_8f90_40456674cd68-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F437b03529f75&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fnormalized-discounted-cumulative-gain-ndcg-the-ultimate-ranking-metric-437b03529f75&source=-----96e5072bd19a----3-----------------bookmark_preview----9041e16a_ada4_44dc_8f90_40456674cd68-------)

[![Image 16: Dr. Leon Eversberg](https://miro.medium.com/v2/resize:fill:20:20/1*s0Z_EQ6__8CxvIXDd2tYGg.png)](https://medium.com/@leoneversberg?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Dr. Leon Eversberg](https://medium.com/@leoneversberg?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[485 2](https://medium.com/how-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F140daa3cbe71&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-create-a-rag-evaluation-dataset-from-documents-140daa3cbe71&source=-----96e5072bd19a----0-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

![Image 17: An Introduction to Transformers in Machine Learning](https://miro.medium.com/v2/resize:fit:679/1*9X-RUNw78A25Vg5h8pjAVA.jpeg)

[![Image 18: Francesco Franco](https://miro.medium.com/v2/resize:fill:20:20/1*tv95qIzwoUpCIPRHa38M9w.jpeg)](https://medium.com/@francescofranco_39234?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Francesco Franco](https://medium.com/@francescofranco_39234?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[T3CH](https://medium.com/h7w?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[An Introduction to Transformers in Machine Learning --------------------------------------------------- ### When you read about Machine Learning in Natural Language Processing these days, all you hear is one thing — Transformers. Models based on…](https://medium.com/h7w/an-introduction-to-transformers-in-machine-learning-50c8a53af576?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[278 1](https://medium.com/h7w/an-introduction-to-transformers-in-machine-learning-50c8a53af576?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F50c8a53af576&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fh7w%2Fan-introduction-to-transformers-in-machine-learning-50c8a53af576&source=-----96e5072bd19a----1-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 32: Abdur Rahman](https://miro.medium.com/v2/resize:fill:20:20/1*dl3HiS_DMv2laLpaKyTBFg.jpeg)](https://medium.com/@abdur-rahman?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Abdur Rahman](https://medium.com/@abdur-rahman?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Stackademic](https://blog.stackademic.com/?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[4.1K 22](https://blog.stackademic.com/is-python-still-the-king-of-data-science-476f1e3191b3?source=read_next_recirc-----96e5072bd19a----0---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 34: Liu Zuo Lin](https://miro.medium.com/v2/resize:fill:20:20/1*Z5dMY4-vS6G69lMMdn3xIQ.jpeg)](https://zlliu.medium.com/?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Liu Zuo Lin](https://zlliu.medium.com/?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Level Up Coding](https://levelup.gitconnected.com/?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[1.7K 17](https://levelup.gitconnected.com/12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d?source=read_next_recirc-----96e5072bd19a----1---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fad32d8ae630d&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2F12-production-grade-python-code-styles-ive-picked-up-from-work-ad32d8ae630d&source=-----96e5072bd19a----1-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 36: Lucas Samba](https://miro.medium.com/v2/resize:fill:20:20/1*R0PCZj_QUhumxixbZeUNAw.jpeg)](https://medium.com/@lucassamba?source=read_next_recirc-----96e5072bd19a----2---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Lucas Samba](https://medium.com/@lucassamba?source=read_next_recirc-----96e5072bd19a----2---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[461 12](https://medium.com/@lucassamba/3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1?source=read_next_recirc-----96e5072bd19a----2---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff3cddba746d1&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40lucassamba%2F3-probability-questions-i-was-asked-in-walmart-data-scientist-interview-f3cddba746d1&source=-----96e5072bd19a----2-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[![Image 38: Shenggang Li](https://miro.medium.com/v2/resize:fill:20:20/1*knqQWkDF7J-gf_A5p7ew5g.png)](https://medium.com/@datalev?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Shenggang Li](https://medium.com/@datalev?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[Towards AI](https://pub.towardsai.net/?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[157 2](https://pub.towardsai.net/exploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73?source=read_next_recirc-----96e5072bd19a----3---------------------d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa301f6028c73&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fexploring-causal-decision-theory-approach-with-quantile-regression-a301f6028c73&source=-----96e5072bd19a----3-----------------bookmark_preview----d616f821_3ebc_4ccd_9ec9_a9b1adf6a4b4-------)


---

