# predicting_demographics
Are BLS job descriptions predictive of workforce demographics?

This project will use text, numeric and image data from the **Bureau of Labor Statistics (BLS)** to predict the key demographics of a workforce (i.e. sex, race, age) based on ground truth labels obtained from the Labor Force Statistics from the **Current Population Survey** which is a monthly survey of households conducted for the BLS by the Bureau of Census.  We will use a detailed main dataset called the **Occupational Outlook Handbook (OOH)** and a supplementary data set called **Data for Occupations Not Covered in Detail** which does not include any text or image data. From this supplementary data set we will extract only the median annual wage and typical entry-level education.

As a concrete example of the text data that we will be using, this is an excerpt from the OOH job description for **Home Health and Personal Care Aides**:

“_Detail oriented. Home health and personal care aides must adhere to specific rules and protocols to help care for clients. They must carefully follow instructions, such as how to care for wounds, that they receive from other healthcare workers._”

This is a **supervised learning** task but as the occupational handbook is grouped by BLS into 25 major headings such as Architecture and Engineering, Arts and Design, and Computer and Information Technology, we will also perform **unsupervised learning** as a separate task to see if we can achieve similar groupings using cluster analysis.

To predict the age, sex and racial compostion of an occupation, since we are dealing with text, image and numeric data, we intend to use a neural network and compare the performance of two models.

1. The first model will use only text and image data 
2. The second model will use income and educational data in addition to text and image data 

The project goal is to determine if there is any bias in the BLS job descriptions have that may have a direct or indirect causal impact on the demographic diversity (or lack thereof) of an occupation through the unintentional messages that these job descriptions convey to employers and applicants about the type of people who are suitable/desirable for the job.

In an ideal world, after controlling for income and education, there should not be any statistically significant difference in the demographic composition of an occupation as compared to the general population from which it is drawn. If the model based solely on text and images outperforms the other model, this would suggest that the job descriptions have a bias which we can report to the BLS as a possible source of discouragement that may prevent certain groups of people from pursuing a particular occupation, which is **commercially** undesirable with respect to the supply of labor and **socially** undesirable with respect to ensuring equal opportunity.
