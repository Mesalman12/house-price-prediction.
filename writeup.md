# Housing Price Regression — Write-up

## Dataset
Used the California Housing dataset structure (median household
income, rooms, bedrooms, house age, population) to predict median
house value.

## Features selected (5)
- **MedInc** — median household income
- **AveRooms** — average rooms per household
- **AveBedrms** — average bedrooms per household
- **HouseAge** — median age of the house
- **Population** — population of the area

These were chosen because income, size, layout, age, and area density
are typically the strongest drivers of house price.

## Model
Trained a Linear Regression model using scikit-learn on the selected
features.

## Evaluation
- **RMSE ≈ $44,900** — the model's predictions are off by about $45K on average.
- **R² ≈ 0.69** — the model explains about 69% of the variation in house prices.

## Scatter plot
`predicted_vs_actual.png` — predicted price plotted against actual
price for the test set, with a red diagonal line showing what a
perfect prediction would look like.

## Plain-English explanation of R² score
R² is like a report card for how well the model understands what
drives house prices. An R² of 0.69 means about 69% of the ups and
downs in house prices can be explained by the features we used —
income, size, age, and area. The remaining 31% comes from things we
didn't measure, like exact location, school districts, or
renovations. In simple terms, this model gives a genuinely useful
first estimate, but it isn't a crystal ball — a real appraiser or a
more detailed model would still do better.
