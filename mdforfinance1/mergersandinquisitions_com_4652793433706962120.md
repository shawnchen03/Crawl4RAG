---
url: https://mergersandinquisitions.com/enterprise-value/
fetch_date: 2024-11-08T21:15:31.961359
length: 57999
token_count: 12669
category: General
has_images: True
image_count: 1
---

# Original Content

Title: Enterprise Value vs Equity Value: Complete Guide and Excel Examples

URL Source: https://mergersandinquisitions.com/enterprise-value/

Published Time: 2020-05-27T14:25:00-04:00

Markdown Content:
![Image 1: Enterprise Value vs Equity Value](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070737/enterprise-value-vs-equity-value.jpg)

Yes, you read the title of this article correctly: we’re covering **Enterprise Value vs Equity Value** _yet again_.

I wrote a tutorial on them a few years ago, but I’m publishing an updated version today for a few reasons:

1.  **I didn’t get everything exactly right last time** – The basics were fine, but from answering student questions over the years, I realized that there was still some confusion about certain points.
2.  **Accounting rules have changed** – Companies [started reporting Operating Leases on their Balance Sheets in 2019](https://www.youtube.com/watch?v=MRHXaUOW3cU), which has created complications for the Enterprise Value calculation and metrics such as EBIT and EBITDA.

So, let’s get started and address every outstanding question, comment, and point of confusion:

Table Of Contents

1.  [Enterprise Value vs Equity Value: Defined](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-defined)
2.  [Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-arent-these-definitions-arbitrary-explain)
3.  [How to Calculate Equity Value and Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#how-to-calculate-equity-value-and-enterprise-value)
4.  [Key Points to Remember About Enterprise Value vs Equity Value](https://mergersandinquisitions.com/enterprise-value/#key-points-to-remember-about-enterprise-value-vs-equity-value)
    *   [Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-1-in-theory-financing-events-do-not-affect-enterprise-value-only-changes-to-the-companys-core-business-ie-net-operating-assets-affect-enterprise-value)
    
    *   [Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-2-metrics-that-represent-only-equity-investors-pair-with-equity-value-and-metrics-that-represent-all-investors-pair-with-enterprise-value)
    
    *   [Key Point #3: Could Equity Value and Enterprise Value Be Negative?](https://mergersandinquisitions.com/enterprise-value/#key-point-3-could-equity-value-and-enterprise-value-be-negative)
    
    *   [Key Point #4: Why the Theory of Enterprise Value Breaks Down](https://mergersandinquisitions.com/enterprise-value/#key-point-4-why-the-theory-of-enterprise-value-breaks-down)
5.  [Enterprise Value vs Equity Value: How to Answer Interview Questions](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-how-to-answer-interview-questions)
6.  [Operating Leases in Enterprise Value: What to Do?](https://mergersandinquisitions.com/enterprise-value/#operating-leases-in-enterprise-value-what-to-do)
7.  [For Further Reading](https://mergersandinquisitions.com/enterprise-value/#for-further-reading)
    *   [Comment Policy](https://mergersandinquisitions.com/enterprise-value/#comment-policy)

These concepts both go back to the formula that you can use to value any stabilized asset or company:

**Company Value** = Cash Flow / (Discount Rate – Cash Flow Growth Rate), where Cash Flow Growth Rate < Discount Rate.

The problem is that each term in this formula is vague: What does “Cash Flow” mean, exactly? Which type of Cash Flow is it? How do you calculate the Discount Rate? And what does “Company Value” mean?

We’re going to focus on the **Company Value** part here because other tutorials deal with concepts such as [how to calculate the Discount Rate](https://breakingintowallstreet.com/how-to-calculate-discount-rate/).

“Company Value” is tricky to define because there are different ways to view it:

*   **“Current Value” or “Market Value”****:** What is the company worth right now according to the stock market, its current owners, or its current investors?
*   **“Implied” or “Intrinsic” Value****:** What should the company be worth according to your analysis and views?

There’s also the question of **investor groups**. Most companies raise funding from different sources, such as Equity Investors (common shareholders), Debt Investors (lenders), and Preferred Stock Investors.

And a single company could be worth one amount to Equity Investors, but a different amount to _All Investors_.

This difference creates the need for **Equity Value** and **Enterprise Value**:

*   **Equity Value Definition:** The value of **EVERYTHING** a company has (Net Assets, or Total Assets – Total Liabilities), but only to **EQUITY INVESTORS** (common shareholders).
*   **Enterprise Value Definition:** The value of the company’s **CORE BUSINESS OPERATIONS** (Net Operating Assets, or Operating Assets – Operating Liabilities), but to **ALL INVESTORS** (Equity, Debt, Preferred, and possibly others).

In these definitions:

*   Replace “Value” with “Market Value” if you’re calculating what the company’s currently worth based on its current share price.
*   Replace “Value” with “Implied Value” if you’re calculating these numbers based on your views and analysis.

For example, Implied Enterprise Value is what _you believe_ the company’s Net Operating Assets _should be worth_ to all investors.

On the other hand, Current Equity Value represents the _market value_ of the company’s Net Assets to common shareholders _right now_, according to the stock market.

**Current Equity Value** is known colloquially as “Market Capitalization” or “Market Cap,” and for public companies, it’s equal to Current Share Price \* Shares Outstanding.

People often use Equity Value or Market Cap when discussing company valuations, and journalists write about it because it’s simple and easy to calculate.

But there is a big problem with it: if a company’s _capital structure_ (the percentage of Equity vs. Debt) changes, Equity Value will also change!

On the other hand, Enterprise Value will _not_ change – or at least, not change _as much_ – even if the company’s capital structure changes.

Here’s how it works for a company with three possible capital structures:

![Image 2: Enterprise Value vs Equity Value and Capital Structure](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070736/Enterprise-Value-vs-Equity-Value-Capital-Structure.jpg)

So, we often use Enterprise Value when analyzing companies because it lets us reach conclusions without having to forecast companies’ capital structures.

Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!
------------------------------------------------------------------------------

One common question we get goes like this:

_“_**_Why_** _do you pair Total Assets – Total Liabilities with Common Shareholders (Equity Value), but Operating Assets – Operating Liabilities with All Investors (Enterprise Value)? Isn’t this pairing arbitrary? If so, couldn’t you create other pairings?”_

No, it’s not arbitrary. You can understand the pairing with the following logic:

1.  A company can generate Equity **internally** from its Net Income (to Common) since it flows into Common Shareholders’ Equity, but it can also _raise_ Equity from outside investors by issuing stock, as in an [IPO or follow-on offering](https://mergersandinquisitions.com/equity-capital-markets/).
2.  On the other hand, a company **cannot** generate Debt, Preferred Stock, and other funding sources internally – it _must_ ask outside investors for these funds.
3.  A company is **unlikely** to raise capital from outside investors to acquire _Non-Core_ or _Non-Operating Assets_, such as a side business selling ice cream if it’s a software company.
4.  However, since Equity may be _generated internally_ or _raised externally_, the company could potentially use it for **both** Operating Assets and Non-Operating Assets.

So, we pair Enterprise Value with Net Operating Assets and Equity Value with Net Assets.

This logic does not hold up 100% in real life (think about [Debt-funded stock buybacks](https://www.youtube.com/watch?v=rplYw_7M9mA)), but this is the basic idea.

We need **both** Equity Value and Enterprise Value when analyzing companies because:

1.  One analysis might produce the Implied Equity Value, while another might produce the Implied Enterprise Value. But if we mostly care about one or the other, we need to move between them with a “bridge.”
2.  No single investor group is an island – actions taken by one group affect everyone else! For example, if a company raises Debt, that affects the risk and potential returns for common shareholders as well.

How to Calculate Equity Value and Enterprise Value
--------------------------------------------------

You usually **start** by calculating a company’s Current Equity Value.

In theory, you could use Market Value of Assets – Market Value of Liabilities, but in practice, that would take an exceptional amount of time and effort.

So, for public companies, you use Shares Outstanding \* Current Share Price to calculate Equity Value:

![Image 3: Equity Value Calculation](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Equity-Value-Calculation.jpg)

Private companies _do_ have share prices and share counts – it’s just that you cannot easily determine them.

So, you usually estimate Current Equity Value based on a private company’s valuation in its last round of funding or its valuation in an outside appraisal.

But you often **skip** this step for private companies and focus on Implied Equity Value and Implied Enterprise Value instead (see: our full tutorial on [private company valuation](https://mergersandinquisitions.com/private-company-valuation/)).

To move from Current Equity Value to Current Enterprise Value, start by rewriting the formula:

*   **Current Enterprise Value** = Market Value of Operating Assets – Market Value of Operating Liabilities

Operating Assets = Total Assets – Non-Operating Assets, so:

*   **Current Enterprise Value** = (Market Value of Assets – Non-Operating Assets) – (Market Value of Liabilities – Liability and Equity Items That Represent Other Investor Groups)

“Other Investor Groups” means “groups _besides_ the common shareholders.”

Then, you can remove the parentheses and rearrange the terms as follows:

*   **Current Enterprise Value** = Market Value of Assets – Market Value of Liabilities – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

At this point, recall that:

*   **Current Equity Value** **=** Market Value of Assets – Market Value of Liabilities

So, you can substitute this term into the Enterprise Value formula above:

*   **Current Enterprise Value** = Current Equity Value – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

You start with Current Equity Value and then subtract Non-Operating Assets and add Liability & Equity Items That Represent Other Investor Groups to make this move:

![Image 4: Enterprise Value Bridge](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Enterprise-Value-Bridge.jpg)

An Asset is “Non-Core” or “Non-Operating” if the company does not need that Asset to sell products/services and deliver them to customers.

**Examples** include Cash, Financial Investments, Side Businesses, Rental Properties (for non-real-estate companies), Assets Held for Sale, Assets of Discontinued Operation, Equity Investments or Associate Companies, and [Net Operating Losses](https://breakingintowallstreet.com/kb/accounting/net-operating-losses/) (NOLs).

(For more on a few of these items, please see our tutorials on the [equity method of accounting](https://mergersandinquisitions.com/equity-method-of-accounting/), [noncontrolling interests](https://mergersandinquisitions.com/noncontrolling-interests/), and [Section 382 limitations on NOLs in M&A deals](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/).

Yes, technically all companies need some minimum amount of Cash for operational purposes, but as a simplification, we assume that all Cash is Non-Operating.

“Liability & Equity Line Items That Represent Other Investor Groups” are harder to define precisely, but examples include Debt, Preferred Stock, Capital/Finance Leases, Noncontrolling Interests, Unfunded Pensions, and, potentially, Operating Leases (see below).

Ideally, you should use the **market values** of all these items when moving from Equity Value to Enterprise Value, but in reality, it doesn’t make a huge difference in most cases.

You need the market value for the company’s Current Share Price and Equity Value, but beyond that, market values and book values are often similar for the rest.

Key Points to Remember About Enterprise Value vs Equity Value
-------------------------------------------------------------

We’ve used a lot of definitions, words, and formulas above.

But what do they all mean _intuitively_? Here are the main points to remember:

### Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value

If a company issues $100 of Common Stock, what happens to Equity Value and Enterprise Value?

Common Shareholders’ Equity increases by $100, so **Equity Value increases by $100** (assuming no change in the share price, which is fine for interview questions).

Without even making any calculations, you can tell that **Enterprise Value stays the same because the company’s Net Operating Assets do not change**.

Cash is Non-Operating, and so is Common Shareholders’ Equity.

According to the theory (the [Modigliani–Miller theorem](https://en.wikipedia.org/wiki/Modigliani%E2%80%93Miller_theorem)), **financing events do NOT affect Enterprise Value**.

So, issuing Debt, Common Stock, Preferred Stock, and repaying Debt and Preferred Stock and repurchasing Common Shares all make no impact on Enterprise Value… in theory.

Enterprise Value changes only if Operating Assets or Liabilities, such as Net PP&E, Inventory, Accounts Receivable, or Deferred Revenue change.

### Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value

On their own, Equity Value and Enterprise Value are “useful, but incomplete.”

The issue is that if two companies are different sizes (e.g., one has $100 million in revenue, and the other has $500 million), then you can’t compare their metrics directly.

It would be like comparing the price of a house with 10,000 square feet to the price of a home with 2,000 square feet.

To make a proper comparison, you need to **normalize** and look at the numbers on a **per-square-foot** basis.

With companies, you do that via **valuation multiples**: take Enterprise Value and divide it by Revenue, EBIT, or EBITDA, for example.

Enterprise Value acts as the “price,” and Revenue acts as the “square foot” value.

You can use three simple rules to decide on the proper pairings:

1.  **Rule #1:** If a metric **deducts Net Interest Expense** (and Preferred Dividends, if applicable), use **Equity Value** in the numerator of any multiple with this metric in the denominator.
2.  **Rule #2:** If the denominator of an Enterprise Value-based multiple **does not deduct an Income Statement expense**, then the numerator should **add its corresponding Balance Sheet line item** (and vice versa).
3.  **Rule #3:** Stick to Equity Value, Enterprise Value Including Operating Leases, and Enterprise Value Excluding Operating Leases, and avoid “half-pregnant” metrics and multiples.

These rules explain why [Net Income](https://breakingintowallstreet.com/kb/accounting/net-income/) pairs with Equity Value: it deducts Net Interest Expense, so the money is no longer available to Debt Investors.

These rules also explain why metrics such as EBIT and [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/) pair with Enterprise Value: they do **not** deduct Net Interest Expense (or Preferred Dividends), so the money is still available to All Investors (both Debt and Equity).

For more on this one, see our full tutorial to [EBIT vs. EBITDA vs. Net Income](https://breakingintowallstreet.com/kb/valuation/ebit-vs-ebitda/).

You can think of this concept using the funnel structure below:

![Image 5: Enterprise Value Funnel](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Funnel.jpg)

If a metric does _not_ deduct Net Interest Expense or Preferred Dividends, then you pair it with Enterprise Value.

If a metric _does_ deduct Net Interest Expense and Preferred Dividends, then you pair it with Equity Value.

After both of those have been subtracted, the remaining cash flow is available only to the Equity Investors, which is why metrics in this category pair with Equity Value.

### Key Point #3: Could Equity Value and Enterprise Value Be Negative?

The answer is “sort of, but not in a meaningful way.”

Current Equity Value for a public company **cannot** be negative because neither its Current Share Price nor its Common Share Count can be negative.

However, Current Enterprise Value could be negative if, for example, the company’s Current Equity Value is $100 million, and it has $200 million in Cash and no Debt.

This scenario is rare; it’s most common for pre-bankruptcy companies that are burning through Cash at high rates and that are likely to die soon (see: [more on Negative Enterprise Value](https://www.youtube.com/watch?v=HxavTgTP070)).

Since Implied Equity Value and Enterprise Value are based on your views, both of them could be negative as well.

Once again, however, it’s rare unless you’re analyzing a distressed or highly speculative company – and even if it happens, you often just set the Implied Share Price to $0.00.

### Key Point #4: Why the Theory of Enterprise Value Breaks Down

Everything above represents a theoretical view of Enterprise Value: that it’s “capital structure-neutral,” and that only changes to a company’s core business affect it.

This graph represents that same theoretical view:

![Image 6: Enterprise Value in Theory](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Theory.jpg)

This view breaks down in real life because a company’s capital structure _does_ affect the value of its core business due to taxes, bankruptcy risk, agency costs, and market inefficiencies.

For example, at first, additional Debt may help [because Debt is cheaper than Equity and Preferred Stock](https://mergersandinquisitions.com/wacc-formula/).

But Debt starts reducing the company’s Implied Value past a certain point because the bankruptcy risk climbs to a much higher level, and there’s a higher chance of conflict between the different investor groups (“agency costs”).

So, this graph is a more accurate depiction of a company’s Enterprise Value as its capital structure changes:

![Image 7: Enterprise Value in Reality](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070733/Enterprise-Value-Reality.jpg)

This concept applies more to _Implied_ Enterprise Value than _Current_ Enterprise Value.

If a company raises more Debt, its Current Enterprise Value will probably **not** change overnight.

But if it is expected to have more Debt permanently, its Current Enterprise Value will start to change.

The bottom line is that Enterprise Value is **not** truly “capital structure-neutral,” as some sources claim.

It’s better to think about it like this: “Changes to a company’s capital structure tend to affect the company’s Equity Value by _more_ than they affect its Enterprise Value.”

Enterprise Value vs Equity Value: How to Answer Interview Questions
-------------------------------------------------------------------

[Investment banking interview questions](https://mergersandinquisitions.com/investment-banking-interview-questions-and-answers/) on these topics span a wide range, including everything from their meanings to the calculations for diluted shares.

However, there’s one specific category that often trips up interviewees: “How does Change X on the financial statements affect Equity Value and Enterprise Value?”

These questions are simple to answer if you remember the two key rules:

**1) Does Common Shareholders’ Equity (CSE) change?**

If so, then Equity Value changes by the amount that CSE changes. If not, then Equity Value does not change.

The main items that affect CSE include Net Income, Dividends, Stock Issuances, and Stock Repurchases.

**2) Do Net Operating Assets (NOA) change?**

If so, then Enterprise Value will change by the amount that NOA changes. It doesn’t matter which investor group was responsible because Enterprise Value reflects all investors.

**To be clear: we are NOT saying that Common Shareholders’ Equity and Equity Value are “the same” – they are very different because one is the book value, and one is the market value.**

**For purposes of interview questions, however, you can assume that a CHANGE to Common Shareholders’ Equity also makes the same impact on Equity Value.**

Also, for interview purposes, you can assume they’re asking about _Current_ Equity Value and _Current_ Enterprise Value.

Here are a few examples of these questions:

**_Q: A company issues $100 in Preferred Stock to purchase $50 of PP&E. How do Equity Value and Enterprise Value change?_**

**A:** CSE does not change because Preferred Stock issuances flow into Preferred Stock within Equity, not Common Shareholders’ Equity. Therefore, Equity Value stays the same.

Net Operating Assets increases by $50 because the PP&E is an Operating Asset, and no Operating Liabilities change, so Enterprise Value increases by $50.

**_Q: A company raises $200 in Debt to pay for issuances of $100 in Common Dividends and $100 in Preferred Dividends. How do Equity Value and Enterprise Value change \*immediately after\* these events?_**

**A:** Both Common Dividends and Preferred Dividends reduce Common Shareholders’ Equity, so it falls by $200, which means that Equity Value decreases by $200 as well.

Net Operating Assets stays the same because Cash, Debt, and CSE are all Non-Operating, so Enterprise Value stays the same.

**_Q: Deferred Revenue increase by $100, and then it decreases by $100 as the company delivers the product/service and recognizes it as Revenue._**

**_Explain how Equity Value and Enterprise Value change in the first step and at the end of both steps. Assume no additional expenses for simplicity._**

**A:** In the first step, Cash on the Assets side increases, and Deferred Revenue on the L&E side increases. Common Shareholders’ Equity does not change, so Equity Value stays the same.

Cash is a Non-Operating Asset, but Deferred Revenue is an Operating Liability, so Net Operating Assets decrease by $100, meaning that Enterprise Value initially decreases by $100.

In the second step, Revenue increases by $100 on the Income Statement, and Net Income goes up by $75, assuming a 25% tax rate.

On the CFS, Net Income is up by $75, and the previous increase in Deferred Revenue reverses, so Cash at the bottom is up by $75.

On the BS, Cash is up by $75 on the Assets side, and CSE is up by $75 on the L&E side due to the Net Income increase.

Therefore, Equity Value increases by $75 from beginning to end, and Enterprise Value stays the same (it went down in Step 1 and then up in Step 2).

**Operating Leases in Enterprise Value: What to Do?**
-----------------------------------------------------

In 2019, a major accounting rule under IFRS and U.S. GAAP changed, and companies **began to record Operating Leases on their Balance Sheets**.

We cover [these on-Balance Sheet Operating Leases in a tutorial here](https://www.youtube.com/watch?v=MRHXaUOW3cU); you can also get our full tutorial to [lease accounting](https://mergersandinquisitions.com/lease-accounting/).

This seemingly simple change has created many issues:

1.  Do you count Operating Leases as “another investor group” in the Enterprise Value calculation?
2.  The Lease Expense is presented differently under U.S. GAAP and IFRS. Under U.S. GAAP, it’s still a Rent or Lease Expense on the Income Statement, but under IFRS, it’s split into Depreciation and Interest elements – _even though the Cash paid for the lease is the same_. In other words, the “Depreciation element” is not a true non-cash expense!

**If you’re working with companies that follow U.S. GAAP, it’s easier and more efficient to _ignore_ Operating Leases in the Enterprise Value calculation**.

If you add them, then you also need to add back the Rent/Lease Expense on the Income Statement in metrics such as EBIT and EBITDA, which means that you now have to use EBITDAR and EBITR (???) instead.

It’s easier to stick with the old treatment and count Operating Leases (and the accompanying Right-of-Use Assets) as Operational items.

**Under IFRS, the problem is that companies may not split out the Lease Depreciation and Lease Interest separately from normal Depreciation and Interest.**

So, a metric such as EBITDA _already_ adds back these items – which means you need to pair it with (Enterprise Value + Operating Leases).

As a result, you tend to use (Enterprise Value + Operating Leases) under IFRS and also when comparing companies that use different accounting systems.

Even if a company does split out its Lease Depreciation and Lease Interest, adjusting for those items could create issues because you’ll end up with non-standard financial metrics.

In a [DCF model](https://mergersandinquisitions.com/dcf-model/) for an IFRS-based company, on the other hand, it’s a better idea to deduct the Lease Interest and Depreciation elements when calculating [NOPAT](https://breakingintowallstreet.com/kb/valuation/nopat/).

That way, you get [Unlevered FCF](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/) figures that are comparable to those for U.S.-based companies, and you can ignore Operating Leases in the bridge at the end.

**For Further Reading**
-----------------------

Our [Core Financial Modeling course](https://breakingintowallstreet.com/core-financial-modeling/) has the full coverage of Equity Value and Enterprise Value, and if you prefer to read instead of watch, the [IB Interview Guide](https://breakingintowallstreet.com/investment-banking-interview-guide/) has a good summary. Here are a few samples:

*   [Equity Value, Enterprise Value, and Valuation Multiples – Written Guide (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/IBIG-04-04-Equity-Value-Enterprise-Value-Metrics-Multiples.pdf)
*   [Excel Examples for Equity Value and Enterprise Value](https://breakingintowallstreet.com/kb/equity-value-enterprise-value/enterprise-value-vs-equity-value/)
*   [Private Company Valuation, Part 1: Are You in the Meth Business or the Money Business?](https://mergersandinquisitions.com/private-company-valuation/)
*   [Private Company Valuation, Part 2: Could You Be in the Meth Business \*and\* the Empire Business?](https://mergersandinquisitions.com/public-vs-private-companies-valuation-differences/)

### **Comment Policy**

Finally, I’m taking the rare step of closing comments on this post.

This is the most in-depth coverage of these concepts that you’ll find for free – anywhere.

If you have additional technical questions, please ask through one of our courses.

Otherwise, consult everything above, and you should be able to answer ~99% of interview questions on these topics.

Last but not least, if you want to have a team of coaches help you with your technical interview preparation, our friends at [Wall Street Mastermind](https://mergersandinquisitions.com/wall-street-mastermind-review/) might be able to help you out.

Their students have gotten offers from every bulge bracket and elite boutique bank on Wall Street, and their team of coaches includes a former Global Head of Recruiting at three different large banks, so you’ll know _exactly_ what banks are looking for in candidates.

They provide personalized, hands-on guidance through the entire networking and interview process, and they have a great track record of results for their clients.

[You can book a free consultation with them to learn more](https://fast.wallstmastermind.com/mandiwsmm1).


## Visual Content Analysis

### Image Analysis
Title: Enterprise Value vs Equity Value: Complete Guide and Excel Examples

URL Source: https://mergersandinquisitions.com/enterprise-value/

Published Time: 2020-05-27T14:25:00-04:00

Markdown Content:
![Image 1: Enterprise Value vs Equity Value](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070737/enterprise-value-vs-equity-value.jpg)

Yes, you read the title of this article correctly: we’re covering **Enterprise Value vs Equity Value** _yet again_.

I wrote a tutorial on them a few years ago, but I’m publishing an updated version today for a few reasons:

1.  **I didn’t get everything exactly right last time** – The basics were fine, but from answering student questions over the years, I realized that there was still some confusion about certain points.
2.  **Accounting rules have changed** – Companies [started reporting Operating Leases on their Balance Sheets in 2019](https://www.youtube.com/watch?v=MRHXaUOW3cU), which has created complications for the Enterprise Value calculation and metrics such as EBIT and EBITDA.

So, let’s get started and address every outstanding question, comment, and point of confusion:

Table Of Contents

1.  [Enterprise Value vs Equity Value: Defined](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-defined)
2.  [Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-arent-these-definitions-arbitrary-explain)
3.  [How to Calculate Equity Value and Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#how-to-calculate-equity-value-and-enterprise-value)
4.  [Key Points to Remember About Enterprise Value vs Equity Value](https://mergersandinquisitions.com/enterprise-value/#key-points-to-remember-about-enterprise-value-vs-equity-value)
    *   [Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-1-in-theory-financing-events-do-not-affect-enterprise-value-only-changes-to-the-companys-core-business-ie-net-operating-assets-affect-enterprise-value)
    
    *   [Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-2-metrics-that-represent-only-equity-investors-pair-with-equity-value-and-metrics-that-represent-all-investors-pair-with-enterprise-value)
    
    *   [Key Point #3: Could Equity Value and Enterprise Value Be Negative?](https://mergersandinquisitions.com/enterprise-value/#key-point-3-could-equity-value-and-enterprise-value-be-negative)
    
    *   [Key Point #4: Why the Theory of Enterprise Value Breaks Down](https://mergersandinquisitions.com/enterprise-value/#key-point-4-why-the-theory-of-enterprise-value-breaks-down)
5.  [Enterprise Value vs Equity Value: How to Answer Interview Questions](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-how-to-answer-interview-questions)
6.  [Operating Leases in Enterprise Value: What to Do?](https://mergersandinquisitions.com/enterprise-value/#operating-leases-in-enterprise-value-what-to-do)
7.  [For Further Reading](https://mergersandinquisitions.com/enterprise-value/#for-further-reading)
    *   [Comment Policy](https://mergersandinquisitions.com/enterprise-value/#comment-policy)

These concepts both go back to the formula that you can use to value any stabilized asset or company:

**Company Value** = Cash Flow / (Discount Rate – Cash Flow Growth Rate), where Cash Flow Growth Rate < Discount Rate.

The problem is that each term in this formula is vague: What does “Cash Flow” mean, exactly? Which type of Cash Flow is it? How do you calculate the Discount Rate? And what does “Company Value” mean?

We’re going to focus on the **Company Value** part here because other tutorials deal with concepts such as [how to calculate the Discount Rate](https://breakingintowallstreet.com/how-to-calculate-discount-rate/).

“Company Value” is tricky to define because there are different ways to view it:

*   **“Current Value” or “Market Value”****:** What is the company worth right now according to the stock market, its current owners, or its current investors?
*   **“Implied” or “Intrinsic” Value****:** What should the company be worth according to your analysis and views?

There’s also the question of **investor groups**. Most companies raise funding from different sources, such as Equity Investors (common shareholders), Debt Investors (lenders), and Preferred Stock Investors.

And a single company could be worth one amount to Equity Investors, but a different amount to _All Investors_.

This difference creates the need for **Equity Value** and **Enterprise Value**:

*   **Equity Value Definition:** The value of **EVERYTHING** a company has (Net Assets, or Total Assets – Total Liabilities), but only to **EQUITY INVESTORS** (common shareholders).
*   **Enterprise Value Definition:** The value of the company’s **CORE BUSINESS OPERATIONS** (Net Operating Assets, or Operating Assets – Operating Liabilities), but to **ALL INVESTORS** (Equity, Debt, Preferred, and possibly others).

In these definitions:

*   Replace “Value” with “Market Value” if you’re calculating what the company’s currently worth based on its current share price.
*   Replace “Value” with “Implied Value” if you’re calculating these numbers based on your views and analysis.

For example, Implied Enterprise Value is what _you believe_ the company’s Net Operating Assets _should be worth_ to all investors.

On the other hand, Current Equity Value represents the _market value_ of the company’s Net Assets to common shareholders _right now_, according to the stock market.

**Current Equity Value** is known colloquially as “Market Capitalization” or “Market Cap,” and for public companies, it’s equal to Current Share Price \* Shares Outstanding.

People often use Equity Value or Market Cap when discussing company valuations, and journalists write about it because it’s simple and easy to calculate.

But there is a big problem with it: if a company’s _capital structure_ (the percentage of Equity vs. Debt) changes, Equity Value will also change!

On the other hand, Enterprise Value will _not_ change – or at least, not change _as much_ – even if the company’s capital structure changes.

Here’s how it works for a company with three possible capital structures:

![Image 2: Enterprise Value vs Equity Value and Capital Structure](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070736/Enterprise-Value-vs-Equity-Value-Capital-Structure.jpg)

So, we often use Enterprise Value when analyzing companies because it lets us reach conclusions without having to forecast companies’ capital structures.

Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!
------------------------------------------------------------------------------

One common question we get goes like this:

_“_**_Why_** _do you pair Total Assets – Total Liabilities with Common Shareholders (Equity Value), but Operating Assets – Operating Liabilities with All Investors (Enterprise Value)? Isn’t this pairing arbitrary? If so, couldn’t you create other pairings?”_

No, it’s not arbitrary. You can understand the pairing with the following logic:

1.  A company can generate Equity **internally** from its Net Income (to Common) since it flows into Common Shareholders’ Equity, but it can also _raise_ Equity from outside investors by issuing stock, as in an [IPO or follow-on offering](https://mergersandinquisitions.com/equity-capital-markets/).
2.  On the other hand, a company **cannot** generate Debt, Preferred Stock, and other funding sources internally – it _must_ ask outside investors for these funds.
3.  A company is **unlikely** to raise capital from outside investors to acquire _Non-Core_ or _Non-Operating Assets_, such as a side business selling ice cream if it’s a software company.
4.  However, since Equity may be _generated internally_ or _raised externally_, the company could potentially use it for **both** Operating Assets and Non-Operating Assets.

So, we pair Enterprise Value with Net Operating Assets and Equity Value with Net Assets.

This logic does not hold up 100% in real life (think about [Debt-funded stock buybacks](https://www.youtube.com/watch?v=rplYw_7M9mA)), but this is the basic idea.

We need **both** Equity Value and Enterprise Value when analyzing companies because:

1.  One analysis might produce the Implied Equity Value, while another might produce the Implied Enterprise Value. But if we mostly care about one or the other, we need to move between them with a “bridge.”
2.  No single investor group is an island – actions taken by one group affect everyone else! For example, if a company raises Debt, that affects the risk and potential returns for common shareholders as well.

How to Calculate Equity Value and Enterprise Value
--------------------------------------------------

You usually **start** by calculating a company’s Current Equity Value.

In theory, you could use Market Value of Assets – Market Value of Liabilities, but in practice, that would take an exceptional amount of time and effort.

So, for public companies, you use Shares Outstanding \* Current Share Price to calculate Equity Value:

![Image 3: Equity Value Calculation](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Equity-Value-Calculation.jpg)

Private companies _do_ have share prices and share counts – it’s just that you cannot easily determine them.

So, you usually estimate Current Equity Value based on a private company’s valuation in its last round of funding or its valuation in an outside appraisal.

But you often **skip** this step for private companies and focus on Implied Equity Value and Implied Enterprise Value instead (see: our full tutorial on [private company valuation](https://mergersandinquisitions.com/private-company-valuation/)).

To move from Current Equity Value to Current Enterprise Value, start by rewriting the formula:

*   **Current Enterprise Value** = Market Value of Operating Assets – Market Value of Operating Liabilities

Operating Assets = Total Assets – Non-Operating Assets, so:

*   **Current Enterprise Value** = (Market Value of Assets – Non-Operating Assets) – (Market Value of Liabilities – Liability and Equity Items That Represent Other Investor Groups)

“Other Investor Groups” means “groups _besides_ the common shareholders.”

Then, you can remove the parentheses and rearrange the terms as follows:

*   **Current Enterprise Value** = Market Value of Assets – Market Value of Liabilities – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

At this point, recall that:

*   **Current Equity Value** **=** Market Value of Assets – Market Value of Liabilities

So, you can substitute this term into the Enterprise Value formula above:

*   **Current Enterprise Value** = Current Equity Value – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

You start with Current Equity Value and then subtract Non-Operating Assets and add Liability & Equity Items That Represent Other Investor Groups to make this move:

![Image 4: Enterprise Value Bridge](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Enterprise-Value-Bridge.jpg)

An Asset is “Non-Core” or “Non-Operating” if the company does not need that Asset to sell products/services and deliver them to customers.

**Examples** include Cash, Financial Investments, Side Businesses, Rental Properties (for non-real-estate companies), Assets Held for Sale, Assets of Discontinued Operation, Equity Investments or Associate Companies, and [Net Operating Losses](https://breakingintowallstreet.com/kb/accounting/net-operating-losses/) (NOLs).

(For more on a few of these items, please see our tutorials on the [equity method of accounting](https://mergersandinquisitions.com/equity-method-of-accounting/), [noncontrolling interests](https://mergersandinquisitions.com/noncontrolling-interests/), and [Section 382 limitations on NOLs in M&A deals](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/).

Yes, technically all companies need some minimum amount of Cash for operational purposes, but as a simplification, we assume that all Cash is Non-Operating.

“Liability & Equity Line Items That Represent Other Investor Groups” are harder to define precisely, but examples include Debt, Preferred Stock, Capital/Finance Leases, Noncontrolling Interests, Unfunded Pensions, and, potentially, Operating Leases (see below).

Ideally, you should use the **market values** of all these items when moving from Equity Value to Enterprise Value, but in reality, it doesn’t make a huge difference in most cases.

You need the market value for the company’s Current Share Price and Equity Value, but beyond that, market values and book values are often similar for the rest.

Key Points to Remember About Enterprise Value vs Equity Value
-------------------------------------------------------------

We’ve used a lot of definitions, words, and formulas above.

But what do they all mean _intuitively_? Here are the main points to remember:

### Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value

If a company issues $100 of Common Stock, what happens to Equity Value and Enterprise Value?

Common Shareholders’ Equity increases by $100, so **Equity Value increases by $100** (assuming no change in the share price, which is fine for interview questions).

Without even making any calculations, you can tell that **Enterprise Value stays the same because the company’s Net Operating Assets do not change**.

Cash is Non-Operating, and so is Common Shareholders’ Equity.

According to the theory (the [Modigliani–Miller theorem](https://en.wikipedia.org/wiki/Modigliani%E2%80%93Miller_theorem)), **financing events do NOT affect Enterprise Value**.

So, issuing Debt, Common Stock, Preferred Stock, and repaying Debt and Preferred Stock and repurchasing Common Shares all make no impact on Enterprise Value… in theory.

Enterprise Value changes only if Operating Assets or Liabilities, such as Net PP&E, Inventory, Accounts Receivable, or Deferred Revenue change.

### Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value

On their own, Equity Value and Enterprise Value are “useful, but incomplete.”

The issue is that if two companies are different sizes (e.g., one has $100 million in revenue, and the other has $500 million), then you can’t compare their metrics directly.

It would be like comparing the price of a house with 10,000 square feet to the price of a home with 2,000 square feet.

To make a proper comparison, you need to **normalize** and look at the numbers on a **per-square-foot** basis.

With companies, you do that via **valuation multiples**: take Enterprise Value and divide it by Revenue, EBIT, or EBITDA, for example.

Enterprise Value acts as the “price,” and Revenue acts as the “square foot” value.

You can use three simple rules to decide on the proper pairings:

1.  **Rule #1:** If a metric **deducts Net Interest Expense** (and Preferred Dividends, if applicable), use **Equity Value** in the numerator of any multiple with this metric in the denominator.
2.  **Rule #2:** If the denominator of an Enterprise Value-based multiple **does not deduct an Income Statement expense**, then the numerator should **add its corresponding Balance Sheet line item** (and vice versa).
3.  **Rule #3:** Stick to Equity Value, Enterprise Value Including Operating Leases, and Enterprise Value Excluding Operating Leases, and avoid “half-pregnant” metrics and multiples.

These rules explain why [Net Income](https://breakingintowallstreet.com/kb/accounting/net-income/) pairs with Equity Value: it deducts Net Interest Expense, so the money is no longer available to Debt Investors.

These rules also explain why metrics such as EBIT and [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/) pair with Enterprise Value: they do **not** deduct Net Interest Expense (or Preferred Dividends), so the money is still available to All Investors (both Debt and Equity).

For more on this one, see our full tutorial to [EBIT vs. EBITDA vs. Net Income](https://breakingintowallstreet.com/kb/valuation/ebit-vs-ebitda/).

You can think of this concept using the funnel structure below:

![Image 5: Enterprise Value Funnel](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Funnel.jpg)

If a metric does _not_ deduct Net Interest Expense or Preferred Dividends, then you pair it with Enterprise Value.

If a metric _does_ deduct Net Interest Expense and Preferred Dividends, then you pair it with Equity Value.

After both of those have been subtracted, the remaining cash flow is available only to the Equity Investors, which is why metrics in this category pair with Equity Value.

### Key Point #3: Could Equity Value and Enterprise Value Be Negative?

The answer is “sort of, but not in a meaningful way.”

Current Equity Value for a public company **cannot** be negative because neither its Current Share Price nor its Common Share Count can be negative.

However, Current Enterprise Value could be negative if, for example, the company’s Current Equity Value is $100 million, and it has $200 million in Cash and no Debt.

This scenario is rare; it’s most common for pre-bankruptcy companies that are burning through Cash at high rates and that are likely to die soon (see: [more on Negative Enterprise Value](https://www.youtube.com/watch?v=HxavTgTP070)).

Since Implied Equity Value and Enterprise Value are based on your views, both of them could be negative as well.

Once again, however, it’s rare unless you’re analyzing a distressed or highly speculative company – and even if it happens, you often just set the Implied Share Price to $0.00.

### Key Point #4: Why the Theory of Enterprise Value Breaks Down

Everything above represents a theoretical view of Enterprise Value: that it’s “capital structure-neutral,” and that only changes to a company’s core business affect it.

This graph represents that same theoretical view:

![Image 6: Enterprise Value in Theory](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Theory.jpg)

This view breaks down in real life because a company’s capital structure _does_ affect the value of its core business due to taxes, bankruptcy risk, agency costs, and market inefficiencies.

For example, at first, additional Debt may help [because Debt is cheaper than Equity and Preferred Stock](https://mergersandinquisitions.com/wacc-formula/).

But Debt starts reducing the company’s Implied Value past a certain point because the bankruptcy risk climbs to a much higher level, and there’s a higher chance of conflict between the different investor groups (“agency costs”).

So, this graph is a more accurate depiction of a company’s Enterprise Value as its capital structure changes:

![Image 7: Enterprise Value in Reality](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070733/Enterprise-Value-Reality.jpg)

This concept applies more to _Implied_ Enterprise Value than _Current_ Enterprise Value.

If a company raises more Debt, its Current Enterprise Value will probably **not** change overnight.

But if it is expected to have more Debt permanently, its Current Enterprise Value will start to change.

The bottom line is that Enterprise Value is **not** truly “capital structure-neutral,” as some sources claim.

It’s better to think about it like this: “Changes to a company’s capital structure tend to affect the company’s Equity Value by _more_ than they affect its Enterprise Value.”

Enterprise Value vs Equity Value: How to Answer Interview Questions
-------------------------------------------------------------------

[Investment banking interview questions](https://mergersandinquisitions.com/investment-banking-interview-questions-and-answers/) on these topics span a wide range, including everything from their meanings to the calculations for diluted shares.

However, there’s one specific category that often trips up interviewees: “How does Change X on the financial statements affect Equity Value and Enterprise Value?”

These questions are simple to answer if you remember the two key rules:

**1) Does Common Shareholders’ Equity (CSE) change?**

If so, then Equity Value changes by the amount that CSE changes. If not, then Equity Value does not change.

The main items that affect CSE include Net Income, Dividends, Stock Issuances, and Stock Repurchases.

**2) Do Net Operating Assets (NOA) change?**

If so, then Enterprise Value will change by the amount that NOA changes. It doesn’t matter which investor group was responsible because Enterprise Value reflects all investors.

**To be clear: we are NOT saying that Common Shareholders’ Equity and Equity Value are “the same” – they are very different because one is the book value, and one is the market value.**

**For purposes of interview questions, however, you can assume that a CHANGE to Common Shareholders’ Equity also makes the same impact on Equity Value.**

Also, for interview purposes, you can assume they’re asking about _Current_ Equity Value and _Current_ Enterprise Value.

Here are a few examples of these questions:

**_Q: A company issues $100 in Preferred Stock to purchase $50 of PP&E. How do Equity Value and Enterprise Value change?_**

**A:** CSE does not change because Preferred Stock issuances flow into Preferred Stock within Equity, not Common Shareholders’ Equity. Therefore, Equity Value stays the same.

Net Operating Assets increases by $50 because the PP&E is an Operating Asset, and no Operating Liabilities change, so Enterprise Value increases by $50.

**_Q: A company raises $200 in Debt to pay for issuances of $100 in Common Dividends and $100 in Preferred Dividends. How do Equity Value and Enterprise Value change \*immediately after\* these events?_**

**A:** Both Common Dividends and Preferred Dividends reduce Common Shareholders’ Equity, so it falls by $200, which means that Equity Value decreases by $200 as well.

Net Operating Assets stays the same because Cash, Debt, and CSE are all Non-Operating, so Enterprise Value stays the same.

**_Q: Deferred Revenue increase by $100, and then it decreases by $100 as the company delivers the product/service and recognizes it as Revenue._**

**_Explain how Equity Value and Enterprise Value change in the first step and at the end of both steps. Assume no additional expenses for simplicity._**

**A:** In the first step, Cash on the Assets side increases, and Deferred Revenue on the L&E side increases. Common Shareholders’ Equity does not change, so Equity Value stays the same.

Cash is a Non-Operating Asset, but Deferred Revenue is an Operating Liability, so Net Operating Assets decrease by $100, meaning that Enterprise Value initially decreases by $100.

In the second step, Revenue increases by $100 on the Income Statement, and Net Income goes up by $75, assuming a 25% tax rate.

On the CFS, Net Income is up by $75, and the previous increase in Deferred Revenue reverses, so Cash at the bottom is up by $75.

On the BS, Cash is up by $75 on the Assets side, and CSE is up by $75 on the L&E side due to the Net Income increase.

Therefore, Equity Value increases by $75 from beginning to end, and Enterprise Value stays the same (it went down in Step 1 and then up in Step 2).

**Operating Leases in Enterprise Value: What to Do?**
-----------------------------------------------------

In 2019, a major accounting rule under IFRS and U.S. GAAP changed, and companies **began to record Operating Leases on their Balance Sheets**.

We cover [these on-Balance Sheet Operating Leases in a tutorial here](https://www.youtube.com/watch?v=MRHXaUOW3cU); you can also get our full tutorial to [lease accounting](https://mergersandinquisitions.com/lease-accounting/).

This seemingly simple change has created many issues:

1.  Do you count Operating Leases as “another investor group” in the Enterprise Value calculation?
2.  The Lease Expense is presented differently under U.S. GAAP and IFRS. Under U.S. GAAP, it’s still a Rent or Lease Expense on the Income Statement, but under IFRS, it’s split into Depreciation and Interest elements – _even though the Cash paid for the lease is the same_. In other words, the “Depreciation element” is not a true non-cash expense!

**If you’re working with companies that follow U.S. GAAP, it’s easier and more efficient to _ignore_ Operating Leases in the Enterprise Value calculation**.

If you add them, then you also need to add back the Rent/Lease Expense on the Income Statement in metrics such as EBIT and EBITDA, which means that you now have to use EBITDAR and EBITR (???) instead.

It’s easier to stick with the old treatment and count Operating Leases (and the accompanying Right-of-Use Assets) as Operational items.

**Under IFRS, the problem is that companies may not split out the Lease Depreciation and Lease Interest separately from normal Depreciation and Interest.**

So, a metric such as EBITDA _already_ adds back these items – which means you need to pair it with (Enterprise Value + Operating Leases).

As a result, you tend to use (Enterprise Value + Operating Leases) under IFRS and also when comparing companies that use different accounting systems.

Even if a company does split out its Lease Depreciation and Lease Interest, adjusting for those items could create issues because you’ll end up with non-standard financial metrics.

In a [DCF model](https://mergersandinquisitions.com/dcf-model/) for an IFRS-based company, on the other hand, it’s a better idea to deduct the Lease Interest and Depreciation elements when calculating [NOPAT](https://breakingintowallstreet.com/kb/valuation/nopat/).

That way, you get [Unlevered FCF](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/) figures that are comparable to those for U.S.-based companies, and you can ignore Operating Leases in the bridge at the end.

**For Further Reading**
-----------------------

Our [Core Financial Modeling course](https://breakingintowallstreet.com/core-financial-modeling/) has the full coverage of Equity Value and Enterprise Value, and if you prefer to read instead of watch, the [IB Interview Guide](https://breakingintowallstreet.com/investment-banking-interview-guide/) has a good summary. Here are a few samples:

*   [Equity Value, Enterprise Value, and Valuation Multiples – Written Guide (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/IBIG-04-04-Equity-Value-Enterprise-Value-Metrics-Multiples.pdf)
*   [Excel Examples for Equity Value and Enterprise Value](https://breakingintowallstreet.com/kb/equity-value-enterprise-value/enterprise-value-vs-equity-value/)
*   [Private Company Valuation, Part 1: Are You in the Meth Business or the Money Business?](https://mergersandinquisitions.com/private-company-valuation/)
*   [Private Company Valuation, Part 2: Could You Be in the Meth Business \*and\* the Empire Business?](https://mergersandinquisitions.com/public-vs-private-companies-valuation-differences/)

### **Comment Policy**

Finally, I’m taking the rare step of closing comments on this post.

This is the most in-depth coverage of these concepts that you’ll find for free – anywhere.

If you have additional technical questions, please ask through one of our courses.

Otherwise, consult everything above, and you should be able to answer ~99% of interview questions on these topics.

Last but not least, if you want to have a team of coaches help you with your technical interview preparation, our friends at [Wall Street Mastermind](https://mergersandinquisitions.com/wall-street-mastermind-review/) might be able to help you out.

Their students have gotten offers from every bulge bracket and elite boutique bank on Wall Street, and their team of coaches includes a former Global Head of Recruiting at three different large banks, so you’ll know _exactly_ what banks are looking for in candidates.

They provide personalized, hands-on guidance through the entire networking and interview process, and they have a great track record of results for their clients.

[You can book a free consultation with them to learn more](https://fast.wallstmastermind.com/mandiwsmm1).


# Chunked Content


## Chunk 0 (Tokens: 512)

Title: Enterprise Value vs Equity Value: Complete Guide and Excel Examples

URL Source: https://mergersandinquisitions.com/enterprise-value/

Published Time: 2020-05-27T14:25:00-04:00

Markdown Content:
![Image 1: Enterprise Value vs Equity Value](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070737/enterprise-value-vs-equity-value.jpg)

Yes, you read the title of this article correctly: we’re covering **Enterprise Value vs Equity Value** _yet again_.

I wrote a tutorial on them a few years ago, but I’m publishing an updated version today for a few reasons:

1.  **I didn’t get everything exactly right last time** – The basics were fine, but from answering student questions over the years, I realized that there was still some confusion about certain points.
2.  **Accounting rules have changed** – Companies [started reporting Operating Leases on their Balance Sheets in 2019](https://www.youtube.com/watch?v=MRHXaUOW3cU), which has created complications for the Enterprise Value calculation and metrics such as EBIT and EBITDA.

So, let’s get started and address every outstanding question, comment, and point of confusion:

Table Of Contents

1.  [Enterprise Value vs Equity Value: Defined](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-defined)
2.  [Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-arent-these-definitions-arbitrary-explain)
3.  [How to Calculate Equity Value and Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#how-to-calculate-equity-value-and-enterprise-value)
4.  [Key Points to Remember About Enterprise Value vs Equity Value](https://mergersandinquisitions.com/enterprise-value/#key-points-to-remember-about-enterprise-value-vs-equity-value)
    *   [Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-1-in-theory-financing-events-do-not-affect-enterprise-value-only-changes-to-the-companys-core-business-ie-net-operating-assets-a

## Chunk 1 (Tokens: 512)

) Affect Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-1-in-theory-financing-events-do-not-affect-enterprise-value-only-changes-to-the-companys-core-business-ie-net-operating-assets-affect-enterprise-value)
    
    *   [Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-2-metrics-that-represent-only-equity-investors-pair-with-equity-value-and-metrics-that-represent-all-investors-pair-with-enterprise-value)
    
    *   [Key Point #3: Could Equity Value and Enterprise Value Be Negative?](https://mergersandinquisitions.com/enterprise-value/#key-point-3-could-equity-value-and-enterprise-value-be-negative)
    
    *   [Key Point #4: Why the Theory of Enterprise Value Breaks Down](https://mergersandinquisitions.com/enterprise-value/#key-point-4-why-the-theory-of-enterprise-value-breaks-down)
5.  [Enterprise Value vs Equity Value: How to Answer Interview Questions](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-how-to-answer-interview-questions)
6.  [Operating Leases in Enterprise Value: What to Do?](https://mergersandinquisitions.com/enterprise-value/#operating-leases-in-enterprise-value-what-to-do)
7.  [For Further Reading](https://mergersandinquisitions.com/enterprise-value/#for-further-reading)
    *   [Comment Policy](https://mergersandinquisitions.com/enterprise-value/#comment-policy)

These concepts both go back to the formula that you can use to value any stabilized asset or company:

**Company Value** = Cash Flow / (Discount Rate – Cash Flow Growth Rate), where Cash Flow Growth Rate < Discount Rate.

The problem is that each term in this formula is vague: What does “Cash Flow” mean, exactly? Which type of Cash Flow is it? How do you calculate the Discount Rate? And what does “Company Value” mean?

We’re going to focus on the **Company Value** part here because other tutorials deal with concepts such as [how to calculate the Discount Rate](https://breakingintowallstreet.com/how-to-calculate-discount-rate/).

“Company Value” is tricky to define because there are different ways to view

## Chunk 2 (Tokens: 512)

 part here because other tutorials deal with concepts such as [how to calculate the Discount Rate](https://breakingintowallstreet.com/how-to-calculate-discount-rate/).

“Company Value” is tricky to define because there are different ways to view it:

*   **“Current Value” or “Market Value”****:** What is the company worth right now according to the stock market, its current owners, or its current investors?
*   **“Implied” or “Intrinsic” Value****:** What should the company be worth according to your analysis and views?

There’s also the question of **investor groups**. Most companies raise funding from different sources, such as Equity Investors (common shareholders), Debt Investors (lenders), and Preferred Stock Investors.

And a single company could be worth one amount to Equity Investors, but a different amount to _All Investors_.

This difference creates the need for **Equity Value** and **Enterprise Value**:

*   **Equity Value Definition:** The value of **EVERYTHING** a company has (Net Assets, or Total Assets – Total Liabilities), but only to **EQUITY INVESTORS** (common shareholders).
*   **Enterprise Value Definition:** The value of the company’s **CORE BUSINESS OPERATIONS** (Net Operating Assets, or Operating Assets – Operating Liabilities), but to **ALL INVESTORS** (Equity, Debt, Preferred, and possibly others).

In these definitions:

*   Replace “Value” with “Market Value” if you’re calculating what the company’s currently worth based on its current share price.
*   Replace “Value” with “Implied Value” if you’re calculating these numbers based on your views and analysis.

For example, Implied Enterprise Value is what _you believe_ the company’s Net Operating Assets _should be worth_ to all investors.

On the other hand, Current Equity Value represents the _market value_ of the company’s Net Assets to common shareholders _right now_, according to the stock market.

**Current Equity Value** is known colloquially as “Market Capitalization” or “Market Cap,” and for public companies, it’s equal to Current Share Price \* Shares Outstanding.

People often use Equity Value or Market Cap when discussing company valuations, and journalists write about it because it’s simple and easy to calculate.

But there is a big problem with it: if a company’s _capital structure_ (the percentage of Equity vs. Debt) changes, Equity Value will also change!

On

## Chunk 3 (Tokens: 512)

, and journalists write about it because it’s simple and easy to calculate.

But there is a big problem with it: if a company’s _capital structure_ (the percentage of Equity vs. Debt) changes, Equity Value will also change!

On the other hand, Enterprise Value will _not_ change – or at least, not change _as much_ – even if the company’s capital structure changes.

Here’s how it works for a company with three possible capital structures:

![Image 2: Enterprise Value vs Equity Value and Capital Structure](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070736/Enterprise-Value-vs-Equity-Value-Capital-Structure.jpg)

So, we often use Enterprise Value when analyzing companies because it lets us reach conclusions without having to forecast companies’ capital structures.

Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!
------------------------------------------------------------------------------

One common question we get goes like this:

_“_**_Why_** _do you pair Total Assets – Total Liabilities with Common Shareholders (Equity Value), but Operating Assets – Operating Liabilities with All Investors (Enterprise Value)? Isn’t this pairing arbitrary? If so, couldn’t you create other pairings?”_

No, it’s not arbitrary. You can understand the pairing with the following logic:

1.  A company can generate Equity **internally** from its Net Income (to Common) since it flows into Common Shareholders’ Equity, but it can also _raise_ Equity from outside investors by issuing stock, as in an [IPO or follow-on offering](https://mergersandinquisitions.com/equity-capital-markets/).
2.  On the other hand, a company **cannot** generate Debt, Preferred Stock, and other funding sources internally – it _must_ ask outside investors for these funds.
3.  A company is **unlikely** to raise capital from outside investors to acquire _Non-Core_ or _Non-Operating Assets_, such as a side business selling ice cream if it’s a software company.
4.  However, since Equity may be _generated internally_ or _raised externally_, the company could potentially use it for **both** Operating Assets and Non-Operating Assets.

So, we pair Enterprise Value with Net Operating Assets and Equity Value with Net Assets.

This logic does not hold up 100% in real life (think about [Debt-funded stock buybacks](https://www.youtube.com/watch?v=rplYw

## Chunk 4 (Tokens: 512)

, we pair Enterprise Value with Net Operating Assets and Equity Value with Net Assets.

This logic does not hold up 100% in real life (think about [Debt-funded stock buybacks](https://www.youtube.com/watch?v=rplYw_7M9mA)), but this is the basic idea.

We need **both** Equity Value and Enterprise Value when analyzing companies because:

1.  One analysis might produce the Implied Equity Value, while another might produce the Implied Enterprise Value. But if we mostly care about one or the other, we need to move between them with a “bridge.”
2.  No single investor group is an island – actions taken by one group affect everyone else! For example, if a company raises Debt, that affects the risk and potential returns for common shareholders as well.

How to Calculate Equity Value and Enterprise Value
--------------------------------------------------

You usually **start** by calculating a company’s Current Equity Value.

In theory, you could use Market Value of Assets – Market Value of Liabilities, but in practice, that would take an exceptional amount of time and effort.

So, for public companies, you use Shares Outstanding \* Current Share Price to calculate Equity Value:

![Image 3: Equity Value Calculation](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Equity-Value-Calculation.jpg)

Private companies _do_ have share prices and share counts – it’s just that you cannot easily determine them.

So, you usually estimate Current Equity Value based on a private company’s valuation in its last round of funding or its valuation in an outside appraisal.

But you often **skip** this step for private companies and focus on Implied Equity Value and Implied Enterprise Value instead (see: our full tutorial on [private company valuation](https://mergersandinquisitions.com/private-company-valuation/)).

To move from Current Equity Value to Current Enterprise Value, start by rewriting the formula:

*   **Current Enterprise Value** = Market Value of Operating Assets – Market Value of Operating Liabilities

Operating Assets = Total Assets – Non-Operating Assets, so:

*   **Current Enterprise Value** = (Market Value of Assets – Non-Operating Assets) – (Market Value of Liabilities – Liability and Equity Items That Represent Other Investor Groups)

“Other Investor Groups” means “groups _besides_ the common shareholders.”

Then, you can remove the parentheses and rearrange the terms as follows:

*   **Current Enterprise Value** = Market

## Chunk 5 (Tokens: 512)

 Liability and Equity Items That Represent Other Investor Groups)

“Other Investor Groups” means “groups _besides_ the common shareholders.”

Then, you can remove the parentheses and rearrange the terms as follows:

*   **Current Enterprise Value** = Market Value of Assets – Market Value of Liabilities – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

At this point, recall that:

*   **Current Equity Value** **=** Market Value of Assets – Market Value of Liabilities

So, you can substitute this term into the Enterprise Value formula above:

*   **Current Enterprise Value** = Current Equity Value – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

You start with Current Equity Value and then subtract Non-Operating Assets and add Liability & Equity Items That Represent Other Investor Groups to make this move:

![Image 4: Enterprise Value Bridge](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Enterprise-Value-Bridge.jpg)

An Asset is “Non-Core” or “Non-Operating” if the company does not need that Asset to sell products/services and deliver them to customers.

**Examples** include Cash, Financial Investments, Side Businesses, Rental Properties (for non-real-estate companies), Assets Held for Sale, Assets of Discontinued Operation, Equity Investments or Associate Companies, and [Net Operating Losses](https://breakingintowallstreet.com/kb/accounting/net-operating-losses/) (NOLs).

(For more on a few of these items, please see our tutorials on the [equity method of accounting](https://mergersandinquisitions.com/equity-method-of-accounting/), [noncontrolling interests](https://mergersandinquisitions.com/noncontrolling-interests/), and [Section 382 limitations on NOLs in M&A deals](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/).

Yes, technically all companies need some minimum amount of Cash for operational purposes, but as a simplification, we assume that all Cash is Non-Operating.

“Liability & Equity Line Items That Represent Other Investor Groups” are harder to define precisely, but examples include Debt, Preferred Stock, Capital/Finance Leases, Noncontrolling Interests, Unfunded Pensions, and, potentially, Operating Leases (see below).

Ideally, you should use the **market values** of all these items

## Chunk 6 (Tokens: 512)

 include Debt, Preferred Stock, Capital/Finance Leases, Noncontrolling Interests, Unfunded Pensions, and, potentially, Operating Leases (see below).

Ideally, you should use the **market values** of all these items when moving from Equity Value to Enterprise Value, but in reality, it doesn’t make a huge difference in most cases.

You need the market value for the company’s Current Share Price and Equity Value, but beyond that, market values and book values are often similar for the rest.

Key Points to Remember About Enterprise Value vs Equity Value
-------------------------------------------------------------

We’ve used a lot of definitions, words, and formulas above.

But what do they all mean _intuitively_? Here are the main points to remember:

### Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value

If a company issues $100 of Common Stock, what happens to Equity Value and Enterprise Value?

Common Shareholders’ Equity increases by $100, so **Equity Value increases by $100** (assuming no change in the share price, which is fine for interview questions).

Without even making any calculations, you can tell that **Enterprise Value stays the same because the company’s Net Operating Assets do not change**.

Cash is Non-Operating, and so is Common Shareholders’ Equity.

According to the theory (the [Modigliani–Miller theorem](https://en.wikipedia.org/wiki/Modigliani%E2%80%93Miller_theorem)), **financing events do NOT affect Enterprise Value**.

So, issuing Debt, Common Stock, Preferred Stock, and repaying Debt and Preferred Stock and repurchasing Common Shares all make no impact on Enterprise Value… in theory.

Enterprise Value changes only if Operating Assets or Liabilities, such as Net PP&E, Inventory, Accounts Receivable, or Deferred Revenue change.

### Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value

On their own, Equity Value and Enterprise Value are “useful, but incomplete.”

The issue is that if two companies are different sizes (e.g., one has $100 million in revenue, and the other has $500 million), then you can’t compare their metrics directly.

It would be like comparing the price of a house with 10,000 square feet to the price of a home with 2,000 square

## Chunk 7 (Tokens: 512)

 million in revenue, and the other has $500 million), then you can’t compare their metrics directly.

It would be like comparing the price of a house with 10,000 square feet to the price of a home with 2,000 square feet.

To make a proper comparison, you need to **normalize** and look at the numbers on a **per-square-foot** basis.

With companies, you do that via **valuation multiples**: take Enterprise Value and divide it by Revenue, EBIT, or EBITDA, for example.

Enterprise Value acts as the “price,” and Revenue acts as the “square foot” value.

You can use three simple rules to decide on the proper pairings:

1.  **Rule #1:** If a metric **deducts Net Interest Expense** (and Preferred Dividends, if applicable), use **Equity Value** in the numerator of any multiple with this metric in the denominator.
2.  **Rule #2:** If the denominator of an Enterprise Value-based multiple **does not deduct an Income Statement expense**, then the numerator should **add its corresponding Balance Sheet line item** (and vice versa).
3.  **Rule #3:** Stick to Equity Value, Enterprise Value Including Operating Leases, and Enterprise Value Excluding Operating Leases, and avoid “half-pregnant” metrics and multiples.

These rules explain why [Net Income](https://breakingintowallstreet.com/kb/accounting/net-income/) pairs with Equity Value: it deducts Net Interest Expense, so the money is no longer available to Debt Investors.

These rules also explain why metrics such as EBIT and [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/) pair with Enterprise Value: they do **not** deduct Net Interest Expense (or Preferred Dividends), so the money is still available to All Investors (both Debt and Equity).

For more on this one, see our full tutorial to [EBIT vs. EBITDA vs. Net Income](https://breakingintowallstreet.com/kb/valuation/ebit-vs-ebitda/).

You can think of this concept using the funnel structure below:

![Image 5: Enterprise Value Funnel](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Funnel.jpg)

If a metric does _not_ deduct Net Interest Expense or Preferred Dividends, then you pair it with Enterprise Value

## Chunk 8 (Tokens: 512)

loads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Funnel.jpg)

If a metric does _not_ deduct Net Interest Expense or Preferred Dividends, then you pair it with Enterprise Value.

If a metric _does_ deduct Net Interest Expense and Preferred Dividends, then you pair it with Equity Value.

After both of those have been subtracted, the remaining cash flow is available only to the Equity Investors, which is why metrics in this category pair with Equity Value.

### Key Point #3: Could Equity Value and Enterprise Value Be Negative?

The answer is “sort of, but not in a meaningful way.”

Current Equity Value for a public company **cannot** be negative because neither its Current Share Price nor its Common Share Count can be negative.

However, Current Enterprise Value could be negative if, for example, the company’s Current Equity Value is $100 million, and it has $200 million in Cash and no Debt.

This scenario is rare; it’s most common for pre-bankruptcy companies that are burning through Cash at high rates and that are likely to die soon (see: [more on Negative Enterprise Value](https://www.youtube.com/watch?v=HxavTgTP070)).

Since Implied Equity Value and Enterprise Value are based on your views, both of them could be negative as well.

Once again, however, it’s rare unless you’re analyzing a distressed or highly speculative company – and even if it happens, you often just set the Implied Share Price to $0.00.

### Key Point #4: Why the Theory of Enterprise Value Breaks Down

Everything above represents a theoretical view of Enterprise Value: that it’s “capital structure-neutral,” and that only changes to a company’s core business affect it.

This graph represents that same theoretical view:

![Image 6: Enterprise Value in Theory](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Theory.jpg)

This view breaks down in real life because a company’s capital structure _does_ affect the value of its core business due to taxes, bankruptcy risk, agency costs, and market inefficiencies.

For example, at first, additional Debt may help [because Debt is cheaper than Equity and Preferred Stock](https://mergersandinquisitions.com/wacc-formula/).

But Debt starts reducing the company’s Implied Value past a certain point because the bankruptcy risk climbs to a much higher level,

## Chunk 9 (Tokens: 512)

 help [because Debt is cheaper than Equity and Preferred Stock](https://mergersandinquisitions.com/wacc-formula/).

But Debt starts reducing the company’s Implied Value past a certain point because the bankruptcy risk climbs to a much higher level, and there’s a higher chance of conflict between the different investor groups (“agency costs”).

So, this graph is a more accurate depiction of a company’s Enterprise Value as its capital structure changes:

![Image 7: Enterprise Value in Reality](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070733/Enterprise-Value-Reality.jpg)

This concept applies more to _Implied_ Enterprise Value than _Current_ Enterprise Value.

If a company raises more Debt, its Current Enterprise Value will probably **not** change overnight.

But if it is expected to have more Debt permanently, its Current Enterprise Value will start to change.

The bottom line is that Enterprise Value is **not** truly “capital structure-neutral,” as some sources claim.

It’s better to think about it like this: “Changes to a company’s capital structure tend to affect the company’s Equity Value by _more_ than they affect its Enterprise Value.”

Enterprise Value vs Equity Value: How to Answer Interview Questions
-------------------------------------------------------------------

[Investment banking interview questions](https://mergersandinquisitions.com/investment-banking-interview-questions-and-answers/) on these topics span a wide range, including everything from their meanings to the calculations for diluted shares.

However, there’s one specific category that often trips up interviewees: “How does Change X on the financial statements affect Equity Value and Enterprise Value?”

These questions are simple to answer if you remember the two key rules:

**1) Does Common Shareholders’ Equity (CSE) change?**

If so, then Equity Value changes by the amount that CSE changes. If not, then Equity Value does not change.

The main items that affect CSE include Net Income, Dividends, Stock Issuances, and Stock Repurchases.

**2) Do Net Operating Assets (NOA) change?**

If so, then Enterprise Value will change by the amount that NOA changes. It doesn’t matter which investor group was responsible because Enterprise Value reflects all investors.

**To be clear: we are NOT saying that Common Shareholders’ Equity and Equity Value are “the same” – they are very different because one is the book value, and one is the market value.**

**For purposes of interview questions, however

## Chunk 10 (Tokens: 512)

To be clear: we are NOT saying that Common Shareholders’ Equity and Equity Value are “the same” – they are very different because one is the book value, and one is the market value.**

**For purposes of interview questions, however, you can assume that a CHANGE to Common Shareholders’ Equity also makes the same impact on Equity Value.**

Also, for interview purposes, you can assume they’re asking about _Current_ Equity Value and _Current_ Enterprise Value.

Here are a few examples of these questions:

**_Q: A company issues $100 in Preferred Stock to purchase $50 of PP&E. How do Equity Value and Enterprise Value change?_**

**A:** CSE does not change because Preferred Stock issuances flow into Preferred Stock within Equity, not Common Shareholders’ Equity. Therefore, Equity Value stays the same.

Net Operating Assets increases by $50 because the PP&E is an Operating Asset, and no Operating Liabilities change, so Enterprise Value increases by $50.

**_Q: A company raises $200 in Debt to pay for issuances of $100 in Common Dividends and $100 in Preferred Dividends. How do Equity Value and Enterprise Value change \*immediately after\* these events?_**

**A:** Both Common Dividends and Preferred Dividends reduce Common Shareholders’ Equity, so it falls by $200, which means that Equity Value decreases by $200 as well.

Net Operating Assets stays the same because Cash, Debt, and CSE are all Non-Operating, so Enterprise Value stays the same.

**_Q: Deferred Revenue increase by $100, and then it decreases by $100 as the company delivers the product/service and recognizes it as Revenue._**

**_Explain how Equity Value and Enterprise Value change in the first step and at the end of both steps. Assume no additional expenses for simplicity._**

**A:** In the first step, Cash on the Assets side increases, and Deferred Revenue on the L&E side increases. Common Shareholders’ Equity does not change, so Equity Value stays the same.

Cash is a Non-Operating Asset, but Deferred Revenue is an Operating Liability, so Net Operating Assets decrease by $100, meaning that Enterprise Value initially decreases by $100.

In the second step, Revenue increases by $100 on the Income Statement, and Net Income goes up by $75, assuming a 25% tax rate.

On the CFS, Net Income is up by $75, and the previous increase in

## Chunk 11 (Tokens: 512)

In the second step, Revenue increases by $100 on the Income Statement, and Net Income goes up by $75, assuming a 25% tax rate.

On the CFS, Net Income is up by $75, and the previous increase in Deferred Revenue reverses, so Cash at the bottom is up by $75.

On the BS, Cash is up by $75 on the Assets side, and CSE is up by $75 on the L&E side due to the Net Income increase.

Therefore, Equity Value increases by $75 from beginning to end, and Enterprise Value stays the same (it went down in Step 1 and then up in Step 2).

**Operating Leases in Enterprise Value: What to Do?**
-----------------------------------------------------

In 2019, a major accounting rule under IFRS and U.S. GAAP changed, and companies **began to record Operating Leases on their Balance Sheets**.

We cover [these on-Balance Sheet Operating Leases in a tutorial here](https://www.youtube.com/watch?v=MRHXaUOW3cU); you can also get our full tutorial to [lease accounting](https://mergersandinquisitions.com/lease-accounting/).

This seemingly simple change has created many issues:

1.  Do you count Operating Leases as “another investor group” in the Enterprise Value calculation?
2.  The Lease Expense is presented differently under U.S. GAAP and IFRS. Under U.S. GAAP, it’s still a Rent or Lease Expense on the Income Statement, but under IFRS, it’s split into Depreciation and Interest elements – _even though the Cash paid for the lease is the same_. In other words, the “Depreciation element” is not a true non-cash expense!

**If you’re working with companies that follow U.S. GAAP, it’s easier and more efficient to _ignore_ Operating Leases in the Enterprise Value calculation**.

If you add them, then you also need to add back the Rent/Lease Expense on the Income Statement in metrics such as EBIT and EBITDA, which means that you now have to use EBITDAR and EBITR (???) instead.

It’s easier to stick with the old treatment and count Operating Leases (and the accompanying Right-of-Use Assets) as Operational items.

**Under IFRS, the problem is that companies may not split out the Lease Depreciation and Lease Interest separately from normal Depreciation

## Chunk 12 (Tokens: 512)

 old treatment and count Operating Leases (and the accompanying Right-of-Use Assets) as Operational items.

**Under IFRS, the problem is that companies may not split out the Lease Depreciation and Lease Interest separately from normal Depreciation and Interest.**

So, a metric such as EBITDA _already_ adds back these items – which means you need to pair it with (Enterprise Value + Operating Leases).

As a result, you tend to use (Enterprise Value + Operating Leases) under IFRS and also when comparing companies that use different accounting systems.

Even if a company does split out its Lease Depreciation and Lease Interest, adjusting for those items could create issues because you’ll end up with non-standard financial metrics.

In a [DCF model](https://mergersandinquisitions.com/dcf-model/) for an IFRS-based company, on the other hand, it’s a better idea to deduct the Lease Interest and Depreciation elements when calculating [NOPAT](https://breakingintowallstreet.com/kb/valuation/nopat/).

That way, you get [Unlevered FCF](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/) figures that are comparable to those for U.S.-based companies, and you can ignore Operating Leases in the bridge at the end.

**For Further Reading**
-----------------------

Our [Core Financial Modeling course](https://breakingintowallstreet.com/core-financial-modeling/) has the full coverage of Equity Value and Enterprise Value, and if you prefer to read instead of watch, the [IB Interview Guide](https://breakingintowallstreet.com/investment-banking-interview-guide/) has a good summary. Here are a few samples:

*   [Equity Value, Enterprise Value, and Valuation Multiples – Written Guide (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/IBIG-04-04-Equity-Value-Enterprise-Value-Metrics-Multiples.pdf)
*   [Excel Examples for Equity Value and Enterprise Value](https://breakingintowallstreet.com/kb/equity-value-enterprise-value/enterprise-value-vs-equity-value/)
*   [Private Company Valuation, Part 1: Are You in the Meth Business or the Money Business?](https://mergersandinquisitions.com/private-company-valuation/)
*   [Private Company Valuation, Part 2: Could

## Chunk 13 (Tokens: 512)

/)
*   [Private Company Valuation, Part 1: Are You in the Meth Business or the Money Business?](https://mergersandinquisitions.com/private-company-valuation/)
*   [Private Company Valuation, Part 2: Could You Be in the Meth Business \*and\* the Empire Business?](https://mergersandinquisitions.com/public-vs-private-companies-valuation-differences/)

### **Comment Policy**

Finally, I’m taking the rare step of closing comments on this post.

This is the most in-depth coverage of these concepts that you’ll find for free – anywhere.

If you have additional technical questions, please ask through one of our courses.

Otherwise, consult everything above, and you should be able to answer ~99% of interview questions on these topics.

Last but not least, if you want to have a team of coaches help you with your technical interview preparation, our friends at [Wall Street Mastermind](https://mergersandinquisitions.com/wall-street-mastermind-review/) might be able to help you out.

Their students have gotten offers from every bulge bracket and elite boutique bank on Wall Street, and their team of coaches includes a former Global Head of Recruiting at three different large banks, so you’ll know _exactly_ what banks are looking for in candidates.

They provide personalized, hands-on guidance through the entire networking and interview process, and they have a great track record of results for their clients.

[You can book a free consultation with them to learn more](https://fast.wallstmastermind.com/mandiwsmm1).


## Visual Content Analysis

### Image Analysis
Title: Enterprise Value vs Equity Value: Complete Guide and Excel Examples

URL Source: https://mergersandinquisitions.com/enterprise-value/

Published Time: 2020-05-27T14:25:00-04:00

Markdown Content:
![Image 1: Enterprise Value vs Equity Value](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070737/enterprise-value-vs-equity-value.jpg)

Yes, you read the title of this article correctly: we’re covering **Enterprise Value vs Equity Value** _yet again_.

I wrote a tutorial on them a few years ago, but I’m publishing an updated version today for a few reasons:

1.  **I didn’t get everything exactly right last time** – The basics were fine, but from answering student questions over the years, I realized that there was still

## Chunk 14 (Tokens: 512)

 ago, but I’m publishing an updated version today for a few reasons:

1.  **I didn’t get everything exactly right last time** – The basics were fine, but from answering student questions over the years, I realized that there was still some confusion about certain points.
2.  **Accounting rules have changed** – Companies [started reporting Operating Leases on their Balance Sheets in 2019](https://www.youtube.com/watch?v=MRHXaUOW3cU), which has created complications for the Enterprise Value calculation and metrics such as EBIT and EBITDA.

So, let’s get started and address every outstanding question, comment, and point of confusion:

Table Of Contents

1.  [Enterprise Value vs Equity Value: Defined](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-defined)
2.  [Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-arent-these-definitions-arbitrary-explain)
3.  [How to Calculate Equity Value and Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#how-to-calculate-equity-value-and-enterprise-value)
4.  [Key Points to Remember About Enterprise Value vs Equity Value](https://mergersandinquisitions.com/enterprise-value/#key-points-to-remember-about-enterprise-value-vs-equity-value)
    *   [Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-1-in-theory-financing-events-do-not-affect-enterprise-value-only-changes-to-the-companys-core-business-ie-net-operating-assets-affect-enterprise-value)
    
    *   [Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value](https://mergersandinquisitions.com/enterprise-value/#key-point-2-metrics-that-represent-only-equity-investors-pair-with-equity-value-and-metrics-that-represent-all-investors-pair-with-enterprise-value)
    
    *   [Key Point #3: Could Equity Value and Enterprise Value Be Negative?](https://mergersandinquisitions.com/enterprise-value/#key-point-3-could-equity-value-and-enterprise

## Chunk 15 (Tokens: 512)

-pair-with-enterprise-value)
    
    *   [Key Point #3: Could Equity Value and Enterprise Value Be Negative?](https://mergersandinquisitions.com/enterprise-value/#key-point-3-could-equity-value-and-enterprise-value-be-negative)
    
    *   [Key Point #4: Why the Theory of Enterprise Value Breaks Down](https://mergersandinquisitions.com/enterprise-value/#key-point-4-why-the-theory-of-enterprise-value-breaks-down)
5.  [Enterprise Value vs Equity Value: How to Answer Interview Questions](https://mergersandinquisitions.com/enterprise-value/#enterprise-value-vs-equity-value-how-to-answer-interview-questions)
6.  [Operating Leases in Enterprise Value: What to Do?](https://mergersandinquisitions.com/enterprise-value/#operating-leases-in-enterprise-value-what-to-do)
7.  [For Further Reading](https://mergersandinquisitions.com/enterprise-value/#for-further-reading)
    *   [Comment Policy](https://mergersandinquisitions.com/enterprise-value/#comment-policy)

These concepts both go back to the formula that you can use to value any stabilized asset or company:

**Company Value** = Cash Flow / (Discount Rate – Cash Flow Growth Rate), where Cash Flow Growth Rate < Discount Rate.

The problem is that each term in this formula is vague: What does “Cash Flow” mean, exactly? Which type of Cash Flow is it? How do you calculate the Discount Rate? And what does “Company Value” mean?

We’re going to focus on the **Company Value** part here because other tutorials deal with concepts such as [how to calculate the Discount Rate](https://breakingintowallstreet.com/how-to-calculate-discount-rate/).

“Company Value” is tricky to define because there are different ways to view it:

*   **“Current Value” or “Market Value”****:** What is the company worth right now according to the stock market, its current owners, or its current investors?
*   **“Implied” or “Intrinsic” Value****:** What should the company be worth according to your analysis and views?

There’s also the question of **investor groups**. Most companies raise funding from different sources, such as Equity Investors (common shareholders), Debt Investors (lenders), and Preferred Stock Investors.

And a single company could be worth one amount to Equity Investors, but a different amount to _All Investors_.

This

## Chunk 16 (Tokens: 512)

 companies raise funding from different sources, such as Equity Investors (common shareholders), Debt Investors (lenders), and Preferred Stock Investors.

And a single company could be worth one amount to Equity Investors, but a different amount to _All Investors_.

This difference creates the need for **Equity Value** and **Enterprise Value**:

*   **Equity Value Definition:** The value of **EVERYTHING** a company has (Net Assets, or Total Assets – Total Liabilities), but only to **EQUITY INVESTORS** (common shareholders).
*   **Enterprise Value Definition:** The value of the company’s **CORE BUSINESS OPERATIONS** (Net Operating Assets, or Operating Assets – Operating Liabilities), but to **ALL INVESTORS** (Equity, Debt, Preferred, and possibly others).

In these definitions:

*   Replace “Value” with “Market Value” if you’re calculating what the company’s currently worth based on its current share price.
*   Replace “Value” with “Implied Value” if you’re calculating these numbers based on your views and analysis.

For example, Implied Enterprise Value is what _you believe_ the company’s Net Operating Assets _should be worth_ to all investors.

On the other hand, Current Equity Value represents the _market value_ of the company’s Net Assets to common shareholders _right now_, according to the stock market.

**Current Equity Value** is known colloquially as “Market Capitalization” or “Market Cap,” and for public companies, it’s equal to Current Share Price \* Shares Outstanding.

People often use Equity Value or Market Cap when discussing company valuations, and journalists write about it because it’s simple and easy to calculate.

But there is a big problem with it: if a company’s _capital structure_ (the percentage of Equity vs. Debt) changes, Equity Value will also change!

On the other hand, Enterprise Value will _not_ change – or at least, not change _as much_ – even if the company’s capital structure changes.

Here’s how it works for a company with three possible capital structures:

![Image 2: Enterprise Value vs Equity Value and Capital Structure](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070736/Enterprise-Value-vs-Equity-Value-Capital-Structure.jpg)

So, we often use Enterprise Value when analyzing companies because it lets us reach conclusions without having to forecast companies’ capital structures.

Enterprise Value vs Equity Value

## Chunk 17 (Tokens: 512)

22070736/Enterprise-Value-vs-Equity-Value-Capital-Structure.jpg)

So, we often use Enterprise Value when analyzing companies because it lets us reach conclusions without having to forecast companies’ capital structures.

Enterprise Value vs Equity Value: Aren’t These Definitions Arbitrary? Explain!
------------------------------------------------------------------------------

One common question we get goes like this:

_“_**_Why_** _do you pair Total Assets – Total Liabilities with Common Shareholders (Equity Value), but Operating Assets – Operating Liabilities with All Investors (Enterprise Value)? Isn’t this pairing arbitrary? If so, couldn’t you create other pairings?”_

No, it’s not arbitrary. You can understand the pairing with the following logic:

1.  A company can generate Equity **internally** from its Net Income (to Common) since it flows into Common Shareholders’ Equity, but it can also _raise_ Equity from outside investors by issuing stock, as in an [IPO or follow-on offering](https://mergersandinquisitions.com/equity-capital-markets/).
2.  On the other hand, a company **cannot** generate Debt, Preferred Stock, and other funding sources internally – it _must_ ask outside investors for these funds.
3.  A company is **unlikely** to raise capital from outside investors to acquire _Non-Core_ or _Non-Operating Assets_, such as a side business selling ice cream if it’s a software company.
4.  However, since Equity may be _generated internally_ or _raised externally_, the company could potentially use it for **both** Operating Assets and Non-Operating Assets.

So, we pair Enterprise Value with Net Operating Assets and Equity Value with Net Assets.

This logic does not hold up 100% in real life (think about [Debt-funded stock buybacks](https://www.youtube.com/watch?v=rplYw_7M9mA)), but this is the basic idea.

We need **both** Equity Value and Enterprise Value when analyzing companies because:

1.  One analysis might produce the Implied Equity Value, while another might produce the Implied Enterprise Value. But if we mostly care about one or the other, we need to move between them with a “bridge.”
2.  No single investor group is an island – actions taken by one group affect everyone else! For example, if a company raises Debt, that affects the risk and potential returns for common shareholders as well.

How to Calculate Equity Value and Enterprise Value
--------------------------------------------------

You usually **

## Chunk 18 (Tokens: 512)

 group is an island – actions taken by one group affect everyone else! For example, if a company raises Debt, that affects the risk and potential returns for common shareholders as well.

How to Calculate Equity Value and Enterprise Value
--------------------------------------------------

You usually **start** by calculating a company’s Current Equity Value.

In theory, you could use Market Value of Assets – Market Value of Liabilities, but in practice, that would take an exceptional amount of time and effort.

So, for public companies, you use Shares Outstanding \* Current Share Price to calculate Equity Value:

![Image 3: Equity Value Calculation](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Equity-Value-Calculation.jpg)

Private companies _do_ have share prices and share counts – it’s just that you cannot easily determine them.

So, you usually estimate Current Equity Value based on a private company’s valuation in its last round of funding or its valuation in an outside appraisal.

But you often **skip** this step for private companies and focus on Implied Equity Value and Implied Enterprise Value instead (see: our full tutorial on [private company valuation](https://mergersandinquisitions.com/private-company-valuation/)).

To move from Current Equity Value to Current Enterprise Value, start by rewriting the formula:

*   **Current Enterprise Value** = Market Value of Operating Assets – Market Value of Operating Liabilities

Operating Assets = Total Assets – Non-Operating Assets, so:

*   **Current Enterprise Value** = (Market Value of Assets – Non-Operating Assets) – (Market Value of Liabilities – Liability and Equity Items That Represent Other Investor Groups)

“Other Investor Groups” means “groups _besides_ the common shareholders.”

Then, you can remove the parentheses and rearrange the terms as follows:

*   **Current Enterprise Value** = Market Value of Assets – Market Value of Liabilities – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

At this point, recall that:

*   **Current Equity Value** **=** Market Value of Assets – Market Value of Liabilities

So, you can substitute this term into the Enterprise Value formula above:

*   **Current Enterprise Value** = Current Equity Value – Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

You start with Current Equity Value and then subtract Non-Operating Assets and add Liability & Equity Items That Represent Other Investor Groups to make this move:

![Image 4: Enterprise

## Chunk 19 (Tokens: 512)

 Non-Operating Assets + Liability and Equity Items That Represent Other Investor Groups

You start with Current Equity Value and then subtract Non-Operating Assets and add Liability & Equity Items That Represent Other Investor Groups to make this move:

![Image 4: Enterprise Value Bridge](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070735/Enterprise-Value-Bridge.jpg)

An Asset is “Non-Core” or “Non-Operating” if the company does not need that Asset to sell products/services and deliver them to customers.

**Examples** include Cash, Financial Investments, Side Businesses, Rental Properties (for non-real-estate companies), Assets Held for Sale, Assets of Discontinued Operation, Equity Investments or Associate Companies, and [Net Operating Losses](https://breakingintowallstreet.com/kb/accounting/net-operating-losses/) (NOLs).

(For more on a few of these items, please see our tutorials on the [equity method of accounting](https://mergersandinquisitions.com/equity-method-of-accounting/), [noncontrolling interests](https://mergersandinquisitions.com/noncontrolling-interests/), and [Section 382 limitations on NOLs in M&A deals](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/).

Yes, technically all companies need some minimum amount of Cash for operational purposes, but as a simplification, we assume that all Cash is Non-Operating.

“Liability & Equity Line Items That Represent Other Investor Groups” are harder to define precisely, but examples include Debt, Preferred Stock, Capital/Finance Leases, Noncontrolling Interests, Unfunded Pensions, and, potentially, Operating Leases (see below).

Ideally, you should use the **market values** of all these items when moving from Equity Value to Enterprise Value, but in reality, it doesn’t make a huge difference in most cases.

You need the market value for the company’s Current Share Price and Equity Value, but beyond that, market values and book values are often similar for the rest.

Key Points to Remember About Enterprise Value vs Equity Value
-------------------------------------------------------------

We’ve used a lot of definitions, words, and formulas above.

But what do they all mean _intuitively_? Here are the main points to remember:

### Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core

## Chunk 20 (Tokens: 512)

, and formulas above.

But what do they all mean _intuitively_? Here are the main points to remember:

### Key Point #1: IN THEORY, Financing Events Do Not Affect Enterprise Value; Only Changes to the Company’s Core Business (i.e., Net Operating Assets) Affect Enterprise Value

If a company issues $100 of Common Stock, what happens to Equity Value and Enterprise Value?

Common Shareholders’ Equity increases by $100, so **Equity Value increases by $100** (assuming no change in the share price, which is fine for interview questions).

Without even making any calculations, you can tell that **Enterprise Value stays the same because the company’s Net Operating Assets do not change**.

Cash is Non-Operating, and so is Common Shareholders’ Equity.

According to the theory (the [Modigliani–Miller theorem](https://en.wikipedia.org/wiki/Modigliani%E2%80%93Miller_theorem)), **financing events do NOT affect Enterprise Value**.

So, issuing Debt, Common Stock, Preferred Stock, and repaying Debt and Preferred Stock and repurchasing Common Shares all make no impact on Enterprise Value… in theory.

Enterprise Value changes only if Operating Assets or Liabilities, such as Net PP&E, Inventory, Accounts Receivable, or Deferred Revenue change.

### Key Point #2: Metrics That Represent ONLY Equity Investors Pair with Equity Value, and Metrics That Represent ALL Investors Pair with Enterprise Value

On their own, Equity Value and Enterprise Value are “useful, but incomplete.”

The issue is that if two companies are different sizes (e.g., one has $100 million in revenue, and the other has $500 million), then you can’t compare their metrics directly.

It would be like comparing the price of a house with 10,000 square feet to the price of a home with 2,000 square feet.

To make a proper comparison, you need to **normalize** and look at the numbers on a **per-square-foot** basis.

With companies, you do that via **valuation multiples**: take Enterprise Value and divide it by Revenue, EBIT, or EBITDA, for example.

Enterprise Value acts as the “price,” and Revenue acts as the “square foot” value.

You can use three simple rules to decide on the proper pairings:

1.  **Rule #1:** If a metric **deducts Net Interest Expense** (and Preferred Dividends, if applicable), use **Equity Value** in the

## Chunk 21 (Tokens: 512)

 can use three simple rules to decide on the proper pairings:

1.  **Rule #1:** If a metric **deducts Net Interest Expense** (and Preferred Dividends, if applicable), use **Equity Value** in the numerator of any multiple with this metric in the denominator.
2.  **Rule #2:** If the denominator of an Enterprise Value-based multiple **does not deduct an Income Statement expense**, then the numerator should **add its corresponding Balance Sheet line item** (and vice versa).
3.  **Rule #3:** Stick to Equity Value, Enterprise Value Including Operating Leases, and Enterprise Value Excluding Operating Leases, and avoid “half-pregnant” metrics and multiples.

These rules explain why [Net Income](https://breakingintowallstreet.com/kb/accounting/net-income/) pairs with Equity Value: it deducts Net Interest Expense, so the money is no longer available to Debt Investors.

These rules also explain why metrics such as EBIT and [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/) pair with Enterprise Value: they do **not** deduct Net Interest Expense (or Preferred Dividends), so the money is still available to All Investors (both Debt and Equity).

For more on this one, see our full tutorial to [EBIT vs. EBITDA vs. Net Income](https://breakingintowallstreet.com/kb/valuation/ebit-vs-ebitda/).

You can think of this concept using the funnel structure below:

![Image 5: Enterprise Value Funnel](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Funnel.jpg)

If a metric does _not_ deduct Net Interest Expense or Preferred Dividends, then you pair it with Enterprise Value.

If a metric _does_ deduct Net Interest Expense and Preferred Dividends, then you pair it with Equity Value.

After both of those have been subtracted, the remaining cash flow is available only to the Equity Investors, which is why metrics in this category pair with Equity Value.

### Key Point #3: Could Equity Value and Enterprise Value Be Negative?

The answer is “sort of, but not in a meaningful way.”

Current Equity Value for a public company **cannot** be negative because neither its Current Share Price nor its Common Share Count can be negative.

However, Current Enterprise Value could be negative if, for example, the company

## Chunk 22 (Tokens: 512)

, but not in a meaningful way.”

Current Equity Value for a public company **cannot** be negative because neither its Current Share Price nor its Common Share Count can be negative.

However, Current Enterprise Value could be negative if, for example, the company’s Current Equity Value is $100 million, and it has $200 million in Cash and no Debt.

This scenario is rare; it’s most common for pre-bankruptcy companies that are burning through Cash at high rates and that are likely to die soon (see: [more on Negative Enterprise Value](https://www.youtube.com/watch?v=HxavTgTP070)).

Since Implied Equity Value and Enterprise Value are based on your views, both of them could be negative as well.

Once again, however, it’s rare unless you’re analyzing a distressed or highly speculative company – and even if it happens, you often just set the Implied Share Price to $0.00.

### Key Point #4: Why the Theory of Enterprise Value Breaks Down

Everything above represents a theoretical view of Enterprise Value: that it’s “capital structure-neutral,” and that only changes to a company’s core business affect it.

This graph represents that same theoretical view:

![Image 6: Enterprise Value in Theory](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070734/Enterprise-Value-Theory.jpg)

This view breaks down in real life because a company’s capital structure _does_ affect the value of its core business due to taxes, bankruptcy risk, agency costs, and market inefficiencies.

For example, at first, additional Debt may help [because Debt is cheaper than Equity and Preferred Stock](https://mergersandinquisitions.com/wacc-formula/).

But Debt starts reducing the company’s Implied Value past a certain point because the bankruptcy risk climbs to a much higher level, and there’s a higher chance of conflict between the different investor groups (“agency costs”).

So, this graph is a more accurate depiction of a company’s Enterprise Value as its capital structure changes:

![Image 7: Enterprise Value in Reality](https://mi-uploads-live.s3.amazonaws.com/wp-content/uploads/2017/06/22070733/Enterprise-Value-Reality.jpg)

This concept applies more to _Implied_ Enterprise Value than _Current_ Enterprise Value.

If a company raises more Debt, its Current Enterprise Value will probably **not** change overnight.

But if it is expected to have more Debt permanently, its Current

## Chunk 23 (Tokens: 512)

This concept applies more to _Implied_ Enterprise Value than _Current_ Enterprise Value.

If a company raises more Debt, its Current Enterprise Value will probably **not** change overnight.

But if it is expected to have more Debt permanently, its Current Enterprise Value will start to change.

The bottom line is that Enterprise Value is **not** truly “capital structure-neutral,” as some sources claim.

It’s better to think about it like this: “Changes to a company’s capital structure tend to affect the company’s Equity Value by _more_ than they affect its Enterprise Value.”

Enterprise Value vs Equity Value: How to Answer Interview Questions
-------------------------------------------------------------------

[Investment banking interview questions](https://mergersandinquisitions.com/investment-banking-interview-questions-and-answers/) on these topics span a wide range, including everything from their meanings to the calculations for diluted shares.

However, there’s one specific category that often trips up interviewees: “How does Change X on the financial statements affect Equity Value and Enterprise Value?”

These questions are simple to answer if you remember the two key rules:

**1) Does Common Shareholders’ Equity (CSE) change?**

If so, then Equity Value changes by the amount that CSE changes. If not, then Equity Value does not change.

The main items that affect CSE include Net Income, Dividends, Stock Issuances, and Stock Repurchases.

**2) Do Net Operating Assets (NOA) change?**

If so, then Enterprise Value will change by the amount that NOA changes. It doesn’t matter which investor group was responsible because Enterprise Value reflects all investors.

**To be clear: we are NOT saying that Common Shareholders’ Equity and Equity Value are “the same” – they are very different because one is the book value, and one is the market value.**

**For purposes of interview questions, however, you can assume that a CHANGE to Common Shareholders’ Equity also makes the same impact on Equity Value.**

Also, for interview purposes, you can assume they’re asking about _Current_ Equity Value and _Current_ Enterprise Value.

Here are a few examples of these questions:

**_Q: A company issues $100 in Preferred Stock to purchase $50 of PP&E. How do Equity Value and Enterprise Value change?_**

**A:** CSE does not change because Preferred Stock issuances flow into Preferred Stock within Equity, not Common Shareholders’ Equity. Therefore, Equity Value stays the same.

Net Operating Assets increases by $

## Chunk 24 (Tokens: 512)

 Equity Value and Enterprise Value change?_**

**A:** CSE does not change because Preferred Stock issuances flow into Preferred Stock within Equity, not Common Shareholders’ Equity. Therefore, Equity Value stays the same.

Net Operating Assets increases by $50 because the PP&E is an Operating Asset, and no Operating Liabilities change, so Enterprise Value increases by $50.

**_Q: A company raises $200 in Debt to pay for issuances of $100 in Common Dividends and $100 in Preferred Dividends. How do Equity Value and Enterprise Value change \*immediately after\* these events?_**

**A:** Both Common Dividends and Preferred Dividends reduce Common Shareholders’ Equity, so it falls by $200, which means that Equity Value decreases by $200 as well.

Net Operating Assets stays the same because Cash, Debt, and CSE are all Non-Operating, so Enterprise Value stays the same.

**_Q: Deferred Revenue increase by $100, and then it decreases by $100 as the company delivers the product/service and recognizes it as Revenue._**

**_Explain how Equity Value and Enterprise Value change in the first step and at the end of both steps. Assume no additional expenses for simplicity._**

**A:** In the first step, Cash on the Assets side increases, and Deferred Revenue on the L&E side increases. Common Shareholders’ Equity does not change, so Equity Value stays the same.

Cash is a Non-Operating Asset, but Deferred Revenue is an Operating Liability, so Net Operating Assets decrease by $100, meaning that Enterprise Value initially decreases by $100.

In the second step, Revenue increases by $100 on the Income Statement, and Net Income goes up by $75, assuming a 25% tax rate.

On the CFS, Net Income is up by $75, and the previous increase in Deferred Revenue reverses, so Cash at the bottom is up by $75.

On the BS, Cash is up by $75 on the Assets side, and CSE is up by $75 on the L&E side due to the Net Income increase.

Therefore, Equity Value increases by $75 from beginning to end, and Enterprise Value stays the same (it went down in Step 1 and then up in Step 2).

**Operating Leases in Enterprise Value: What to Do?**
-----------------------------------------------------

In 2019, a major accounting rule under IFRS and U.S. GAAP changed, and companies **began to record

## Chunk 25 (Tokens: 512)

 then up in Step 2).

**Operating Leases in Enterprise Value: What to Do?**
-----------------------------------------------------

In 2019, a major accounting rule under IFRS and U.S. GAAP changed, and companies **began to record Operating Leases on their Balance Sheets**.

We cover [these on-Balance Sheet Operating Leases in a tutorial here](https://www.youtube.com/watch?v=MRHXaUOW3cU); you can also get our full tutorial to [lease accounting](https://mergersandinquisitions.com/lease-accounting/).

This seemingly simple change has created many issues:

1.  Do you count Operating Leases as “another investor group” in the Enterprise Value calculation?
2.  The Lease Expense is presented differently under U.S. GAAP and IFRS. Under U.S. GAAP, it’s still a Rent or Lease Expense on the Income Statement, but under IFRS, it’s split into Depreciation and Interest elements – _even though the Cash paid for the lease is the same_. In other words, the “Depreciation element” is not a true non-cash expense!

**If you’re working with companies that follow U.S. GAAP, it’s easier and more efficient to _ignore_ Operating Leases in the Enterprise Value calculation**.

If you add them, then you also need to add back the Rent/Lease Expense on the Income Statement in metrics such as EBIT and EBITDA, which means that you now have to use EBITDAR and EBITR (???) instead.

It’s easier to stick with the old treatment and count Operating Leases (and the accompanying Right-of-Use Assets) as Operational items.

**Under IFRS, the problem is that companies may not split out the Lease Depreciation and Lease Interest separately from normal Depreciation and Interest.**

So, a metric such as EBITDA _already_ adds back these items – which means you need to pair it with (Enterprise Value + Operating Leases).

As a result, you tend to use (Enterprise Value + Operating Leases) under IFRS and also when comparing companies that use different accounting systems.

Even if a company does split out its Lease Depreciation and Lease Interest, adjusting for those items could create issues because you’ll end up with non-standard financial metrics.

In a [DCF model](https://mergersandinquisitions.com/dcf-model/) for an IFRS-based company, on the

## Chunk 26 (Tokens: 512)

iation and Lease Interest, adjusting for those items could create issues because you’ll end up with non-standard financial metrics.

In a [DCF model](https://mergersandinquisitions.com/dcf-model/) for an IFRS-based company, on the other hand, it’s a better idea to deduct the Lease Interest and Depreciation elements when calculating [NOPAT](https://breakingintowallstreet.com/kb/valuation/nopat/).

That way, you get [Unlevered FCF](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/) figures that are comparable to those for U.S.-based companies, and you can ignore Operating Leases in the bridge at the end.

**For Further Reading**
-----------------------

Our [Core Financial Modeling course](https://breakingintowallstreet.com/core-financial-modeling/) has the full coverage of Equity Value and Enterprise Value, and if you prefer to read instead of watch, the [IB Interview Guide](https://breakingintowallstreet.com/investment-banking-interview-guide/) has a good summary. Here are a few samples:

*   [Equity Value, Enterprise Value, and Valuation Multiples – Written Guide (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/IBIG-04-04-Equity-Value-Enterprise-Value-Metrics-Multiples.pdf)
*   [Excel Examples for Equity Value and Enterprise Value](https://breakingintowallstreet.com/kb/equity-value-enterprise-value/enterprise-value-vs-equity-value/)
*   [Private Company Valuation, Part 1: Are You in the Meth Business or the Money Business?](https://mergersandinquisitions.com/private-company-valuation/)
*   [Private Company Valuation, Part 2: Could You Be in the Meth Business \*and\* the Empire Business?](https://mergersandinquisitions.com/public-vs-private-companies-valuation-differences/)

### **Comment Policy**

Finally, I’m taking the rare step of closing comments on this post.

This is the most in-depth coverage of these concepts that you’ll find for free – anywhere.

If you have additional technical questions, please ask through one of our courses.

Otherwise, consult everything above, and you should be able to answer ~99% of interview questions on these topics.

Last but not least, if you want to have a team of coaches help you with your

## Chunk 27 (Tokens: 195)

, please ask through one of our courses.

Otherwise, consult everything above, and you should be able to answer ~99% of interview questions on these topics.

Last but not least, if you want to have a team of coaches help you with your technical interview preparation, our friends at [Wall Street Mastermind](https://mergersandinquisitions.com/wall-street-mastermind-review/) might be able to help you out.

Their students have gotten offers from every bulge bracket and elite boutique bank on Wall Street, and their team of coaches includes a former Global Head of Recruiting at three different large banks, so you’ll know _exactly_ what banks are looking for in candidates.

They provide personalized, hands-on guidance through the entire networking and interview process, and they have a great track record of results for their clients.

[You can book a free consultation with them to learn more](https://fast.wallstmastermind.com/mandiwsmm1).

