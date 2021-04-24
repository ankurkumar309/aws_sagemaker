# Sagemaker-practice
Repository containing all the sagemaker assigments

Assignment 1: 
Create a flask app that get the folder name and lists the filename present in the corresponding folder. (Use Boto3 for reading the contents of the folder)
Deploy the same in EC2 free tier instance and allow incoming traffic on 8085 port

Solution steps:
1. Created S3 bucket empid-bucketname.
2. Created three folders inside bucket (A,B,C).
3. Putted files inside each of the folders.
4. Run the app using url :  http://52.66.211.30:8085/
We will reach to home page where you can select A OR B OR C folder and see the content inside it in the next page automatically after submiting the folder name.
Screenshot are provided below:




![home_ph](https://user-images.githubusercontent.com/60085341/115950807-11f5cc80-a4fb-11eb-9072-d5804edcb6e3.jpeg)






![foders_page](https://user-images.githubusercontent.com/60085341/115950823-32be2200-a4fb-11eb-8d9e-f94b67b6a3a5.jpg)



5. Budget set for the project:

![budget_set](https://user-images.githubusercontent.com/60085341/115951139-be847e00-a4fc-11eb-8343-359ac48c6920.PNG)

6.Billing information post completion:

![Billing](https://user-images.githubusercontent.com/60085341/115951155-da881f80-a4fc-11eb-87c6-90b5cb4295a5.PNG)





![Capture](https://user-images.githubusercontent.com/60085341/115951242-4f5b5980-a4fd-11eb-8b17-5ebb919baf5e.PNG)












Assignments 2: 
