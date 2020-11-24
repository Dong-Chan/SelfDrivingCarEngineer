# The Need for Machine Learning Design Patterns

Design patterns are a way to codify the knowledge and experience of expects into advice that all practitioners can follow. The common challenges in machine learning tend to revolve around data quality, reproducibility, data drift, scale, and having to satisfy multiple objectives.



**Table of contents**

1. [Data Quality](#data-quality)
2. [Reproducibility](#reproducibility)
3. [Data drift](#data-drift)
4. [Scale](#scale)
5. [Multiple Objectives](#multiple-objectives)



### Data Quality

Data accuracy refers to both your training data's features and the ground truth labels corresponding with those features.



### Reproducibility

When training, ML model weights are initialized with random values. These weights then converge during training as the model iterates and learns from the data. Because of this, the same mmodel code given the same training data will produce slightly different results across training runs. This introduces a challenge of reproducibility. If you train a model to 98.1% accuracy, a repeated training run is not guaranteed to reach the same result.



### Data drift

While machine learning models typically represent a static relationship between inputs and outputs, data can change significantly over time. Data drift refers to the challenge of ensuring your machine learning models stay relevant, and that model predictions are an accurate reflection of the environment in which they're. being used.



### Scale

The challenge of scaling is present throughout many stages of a typical machine learning workflow. You'll likely encounter scaling challenges in data collection and preprocessing, training, and serving. When ingesting and preparing data for a machine learning model, the size of the dataset will dictate the tooling required for your solution. It is often the job of data engineers to build our data pipelines that can scale to handle dataset with millions of rows.



### Multiple Objectives

Though there is often a single team responsible for building a machine learning model, many teams across an organization will make use of the model in some way. Inevitably, these teams may have different ideas of what defines a successful model.