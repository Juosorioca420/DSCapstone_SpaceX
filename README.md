<h1>SpaceX  Falcon 9 first stage Landing Prediction</h1>

At this project, it is intended to explore the SpaceX records to determine how the payload mass, the orbit and even the launch area, among other various factors, can affect the success of the subsequent recovery of the first stage of a Falcon 9 rocket. In this order of ideas, it will be possible to parameterize and develop certain machine learning models, and once the model that best fits the data under study has been determined, to predict whether a recovery mission for a Falcon 9 will be successful.


<h3>Conclusions</h3>

- The best performing model was the Decision Tree, with a F1 - Score
of 0.943; expressing the ability of the model to correctly classify both
positive and negative outcomes.

- No clear causality was established between the success of a mission
and its original launch site, rather, an increase in the success rate is
observed over time, possibly due to technological improvements and
experience.

- As the payload mass of a mission increases, and proportionally with
it, the investment and resources involved in such mission increase,
the success rate of the mission increases too.

- Even when the data obtained is of high quality, displaying a
wealth of valuable information, the studied data set had relatively
few records. For the development of more reliable models it
would be necessary to extract a more significant volume of data.

- Since the function of the dependent variable had many
independent variables associated with it, it is pertinent to refine
the analysis, where the variation in the data can be described with
fewer dimensions than the initial data applying a Principal
Component Analysis.

- Starting from the best model obtained for this data set, it is
possible to refine the model further, applying a Random Forest
modeling using decision trees to average the votes of each tree or
applying an XGBoost or LightGBM modeling based on 'weak'
decision trees to generate a stronger model altogether.