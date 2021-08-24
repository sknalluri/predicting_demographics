# predicting_demographics
**Do BLS job descriptions condtain unintended bias?**

There are many historical, socioeconomic and cultural reasons why particular occupations skew male or female, black or white, and old or young, not all of which are good ones. Demographic disparity of worker pay and opportunity is a big problem that many are working hard to correct, including the US government through public policy, funding, and its own hiring practices. 

To assist the government in this worthy endeavor, this project we will built a multi-output regresson model using multiple input data types (i.e. **Text**, **Numeric**, **Image**) taken from the [Bureau of Labor Statistics](https://www.bls.gov/) (BLS) in a musupervised learning task to predict key demographics of a workforce (i.e. **Sex, Race, Age**) based on ground truth labels obtained from the [Labor Force Statistics from the Current Population Survey](https://www.bls.gov/cps/tables.html), a monthly survey of households conducted for the BLS by the Bureau of Census.  We will use a detailed main dataset called the [Occupational Outlook Handbook](https://www.bls.gov/ooh/) (OOH) and a supplementary data set called [Data for Occupations Not Covered in Detail](https://www.bls.gov/ooh/about/data-for-occupations-not-covered-in-detail.htm) which does not include any text or image data. From this supplementary data set we will extract only the median annual wage and typical entry-level education.

As a concrete example of the text, numeric and image data that we will be using, below are captioned images, summary statistics, and an excerpt from the job description for [Home Health and Personal Care Aides](https://www.bls.gov/ooh/healthcare/home-health-aides-and-personal-care-aides.htm):

<img width="1009" alt="Screen Shot 2021-08-23 at 6 37 18 PM" src="https://user-images.githubusercontent.com/75413805/130541587-4944faed-d62f-4501-93cc-94a250734b34.png">

<img width="945" alt="Screen Shot 2021-08-23 at 6 40 08 PM" src="https://user-images.githubusercontent.com/75413805/130541825-ce78cc72-826e-4ac1-abd0-c555668f6c91.png">

We will build, optimize and compare the performance of individual models using each of the three data types as inputs and combinations of these models as follows:

1. Image only: Image objects will be detected and converted to a Bag of Words (BOW) using a [TensorFlow Hub Object Detection Module on Google Colab](https://www.tensorflow.org/hub/tutorials/object_detection) that will be used as input to a **Multi-Layer Perceptron **(MLP) to predict demographic targets 
2. Text only: **Long Short-Term Memory (LSTM)** model
3. Numeric only: **MLP**
4. Text, Numeric:	**LSTM + MLP**
5. Text, Numeric, Image: **LSTM + MLP + MLP**

Our models will be predicting the following twelve demographics: _Women, White,	Black or African American, Asian, Hispanic or Latino,	16-19, 20-24, 25-34, 35-44, 45-54, 55-64,	65+_

While we hope to build a high performaing model, it is as or more important for us to be able interpret these results and their implications for the real-life problem we want to address. As such, we intend to use the [Local Interpretable Model-Agnostic Explanations](https://lime-ml.readthedocs.io/en/latest/)(LIME) package to assist us in this effort.

Intentional or not, the words, numbers and images used to describe an occupation communicate the prevalent attributes associated with that occupation. If we are able to successfully predict the demographic composition of an occupation based on these associations, then we can help employers and workers to identify and address the underlying factors that explain the demographic dominance and deficiencies of a given workforce, and ultimately advance the cause of equal pay and opportunity. 
