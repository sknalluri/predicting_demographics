# predicting_demographics
Do BLS job descriptions condtain unintended bias?

There are many historical, socioeconomic and cultural reasons why particular occupations skew male or female, black or white, and old or young, not all of which are good ones. Demographic disparity of worker pay and opportunity is a big problem that many are working hard to correct, including the US government through public policy, funding, and its own hiring practices. 

To assist the government in this worthy endeavor, this project will use text, numeric and image data from the Bureau of Labor Statistics (BLS) in a supervised learning task to predict the key demographics of a workforce (i.e. sex, race, age) based on ground truth labels obtained from the [Labor Force Statistics from the Current Population Survey](https://www.bls.gov/cps/tables.htm) which is a monthly survey of households conducted for the BLS by the Bureau of Census.  We will use a detailed main dataset called the [Occupational Outlook Handbook](https://www.bls.gov/ooh/)(OOH) and a supplementary data set called **Data for Occupations Not Covered in Detail** which does not include any text or image data. From this supplementary data set we will extract only the median annual wage and typical entry-level education.

As a concrete example of the text and image data that we will be using, the following is an excerpt of an image and captioned photo from the OOH job description for **Home Health and Personal Care Aides**:

“_Detail oriented. Home health and personal care aides must adhere to specific rules and protocols to help care for clients. They must carefully follow instructions, such as how to care for wounds, that they receive from other healthcare workers._”

To predict the age, sex and racial compostion of an occupation, since we are dealing with text, image and numeric data, we intend to use a neural network and compare the performance of several models:

1. Image only: Image objects will be detected and converted to a Bag of Words (BOW) that will be used as input to a Multi-Layer Perceptron (MLP) to predict demographic targets 
2. Text only: Long Short-Term Memory (LSTM) model
3. Numeric only: Multi-Layer Perceptron
4. Text, Numeric:	LSTM + MLP
5. Text, Numeric, Image: LSTM + MLP + MLP

If we are able to predict the demographics of an occupation based soley on the words, numbers and images used to describe that occupation, this implies that the descriptions contain biases that could uncover the source of demographic imbalance that may be reinforcing stereotypes and unintentionally influencing labor market supply (i.e. employers) and demand (i.e. job seekers). 

Intentional or not, the words, numbers and images used to describe an occupation communicate the prevalent attributes associated with that occupation. If we are able to successfully predict the demographic composition of an occupation based on these associations, then we can help employers and workers to identify and address the underlying factors that explain the demographic dominance and deficiencies of a given workforce, and ultimately advance the cause of equal pay and opportunity. 
