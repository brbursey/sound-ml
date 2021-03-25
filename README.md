# sound-ml
This will be a personal project for machine learning audio classification.

Still working on what to classify. Most likely will be classifying voice types into: 
- Bass
- Baritone
- Tenor
- Alto
- Mezzo-Soprano
- Soprano

More importantly, I want to focus on differnt architecture patterns for building machine learning products. This will start with:
- classifier service (Python)
- API wrapper (.NET)
- store models in AWS
- Amazon SQS to send requests to AWS
- docker
  

# Kickstarting Project in 2021

Need to deploy a project so that I can get some experience creating a Machine Learning project from model creating to a working endpoint that can be hit. To do so, I am going to split this project up into three phases.

## Phase 1: Core functionality
- [ ] Create model
- [ ] Create dockerfile to run project

**Acceptance Criteria:**
- **Can input a soundbite of a cat/dog and receive a prediction  all while running in docker.**

After phase 1, I should be able to use the model. Thats a great first step. After that it would be nice to tweak some things and update our system. Thats what will happen in phase 2.

## Phase 2: Updates and Start MLOps
- [ ] Refactor model and project. Keeping things SOLID
  - Use Tensorflow to read the files.
  - Look back at older TF courses on how to do that.
- [ ] Deploy app to AWS, GCP, Azure, whatever. GET IT IN THE CLOUD!
  - good link for deploying model: https://www.youtube.com/watch?v=fw6NMQrYc6w&t=3s&ab_channel=DanielBourke
- [ ] Setup cloud environment
  - Create bucket for data to live
  - Route bucket data to model
  - **Stretch:** Setup experiments pipeline

**Acceptance Critera:**
- **Model is deployed in cloud provider**
- **Code is cleaned up. Older unused files are gone.**
- **Data is living in the cloud and not in folders where the project lives**

After phase 2, the same model (with some slight enhancements) should be up in the cloud of choice! If stretch goal is reached, will then be able to create other models and then choose the best one to deploy. At this point, we have **OFFICIALLY** deployed our model, so thats the big goal! Phase 3 is where we can finally make adjustments to the model itself. 

***Note: This is the step we want to reach. This is where the fun begins, but all the work that is really valuable is done in Phase 1 and 2.***

