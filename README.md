# predicting_demographics
**Do BLS job descriptions condtain unintended bias?**

There are many historical, socioeconomic and cultural reasons why particular occupations skew male or female, black or white, and old or young, not all of which are good ones. Demographic disparity of worker pay and opportunity is a big problem that many are working hard to correct, including the US government through public policy, funding, and its own hiring practices. 

To assist the government in this worthy endeavor, this project will use text, numeric and image data from the Bureau of Labor Statistics (BLS) in a supervised learning task to predict the key demographics of a workforce (i.e. sex, race, age) based on ground truth labels obtained from the [Labor Force Statistics from the Current Population Survey](https://www.bls.gov/cps/tables.htm) which is a monthly survey of households conducted for the BLS by the Bureau of Census.  We will use a detailed main dataset called the [Occupational Outlook Handbook](https://www.bls.gov/ooh/)(OOH) and a supplementary data set called [Data for Occupations Not Covered in Detail](https://www.bls.gov/ooh/about/data-for-occupations-not-covered-in-detail.htm) which does not include any text or image data. From this supplementary data set we will extract only the median annual wage and typical entry-level education.

As a concrete example of the text, numeric and image data that we will be using, below are a captioned image, summary statistics, and an excerpt from an OOH job description for [Home Health and Personal Care Aides](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm):

<img width="1009" alt="Screen Shot 2021-08-23 at 6 37 18 PM" src="https://user-images.githubusercontent.com/75413805/130541587-4944faed-d62f-4501-93cc-94a250734b34.png">

<img width="945" alt="Screen Shot 2021-08-23 at 6 40 08 PM" src="https://user-images.githubusercontent.com/75413805/130541825-ce78cc72-826e-4ac1-abd0-c555668f6c91.png">

To predict the age, sex and racial compostion of an occupation, since we are dealing with text, image and numeric data, we intend to use a neural network and compare the performance of several models:

1. Image only: Image objects will be detected and converted to a Bag of Words (BOW) that will be used as input to a Multi-Layer Perceptron (MLP) to predict demographic targets 
2. Text only: Long Short-Term Memory (LSTM) model
3. Numeric only: Multi-Layer Perceptron
4. Text, Numeric:	LSTM + MLP
5. Text, Numeric, Image: LSTM + MLP + MLP

If we are able to predict the demographics of an occupation based soley on the words, numbers and images used to describe that occupation, this implies that the descriptions contain biases that could uncover the source of demographic imbalance that may be reinforcing stereotypes and unintentionally influencing labor market supply (i.e. employers) and demand (i.e. job seekers). 

Intentional or not, the words, numbers and images used to describe an occupation communicate the prevalent attributes associated with that occupation. If we are able to successfully predict the demographic composition of an occupation based on these associations, then we can help employers and workers to identify and address the underlying factors that explain the demographic dominance and deficiencies of a given workforce, and ultimately advance the cause of equal pay and opportunity. 
