Steps:

1.Create the VM instance on GCP by following the below link:
https://towardsdatascience.com/running-jupyter-notebook-in-google-cloud-platform-in-15-min-61e16da34d52

2.Prepare the dataset for training by running the command on Anaconda prompt of your local machine:
python dataset_tool.py directory_of_dataset"dataset_name ~/downloads_directory/folder_name.
tf records will be generated which contains images with *.tfrecords file for each resolution

3.Upload the zip file of generated tf records on GCP through SSH shell and unzip it

4.upload the code on GCP through SSH shell and unzip it using unzip (filename)

4.Go to the code directory on shell and run the train.py file

6.The generted images are downloaded in your directory

6.Train for 12-13 hours for the data to converge into proper image