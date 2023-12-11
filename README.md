# DOSnet
https://www.nature.com/articles/s41467-020-20342-6#additional-information

# data
https://figshare.com/articles/dataset/DOSnet_data/14511978

**Usage:**

1. Install prerequisites listed in requirements.txt. You will need: \
Keras==2.2.2 \
numpy==1.14.3 \
scikit_learn==0.23.2

2. To run the code on existing examples provided here, first unpack the data file containing the DOS and energies: \
`tar -xvf "your_file_here.tar.gz"` \
or for the combined data: \
`cat Combined_data.tar.gz.split* > Combined_data.tar.gz` \
`tar -xvf Combined_data.tar.gz`

3. Run DOSnet: \
`python Main.py` \
Example: \
`python Main.py --multi_adsorbate=1 --data_dir='Combined_data' --save_model=1 --batch_size=128`

Output will be written to txt files as "predict_test.txt" or "predict_train.txt" or "CV_predict.txt" for a cross-validation run.


5. file\
- change_dropout.py\
dropoutを変更して実行。各dropoutは別seedで10回ずつ\
- change_epoch.py\
epochを変更して実行。各epochは別seedで10回ずつ\





