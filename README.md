# DOSnet


**Usage:**

1. Install prerequisites listed in requirements.txt. You will need: \
Keras==2.2.2 \
numpy==1.14.3 \
scikit_learn==0.23.2

2. To run the code on existing examples provided here, first unpack the data file containing the DOS and energies: \
tar -xvf "your_file_here.tar.gz" \
or for the combined data: \
cat Combined_data.tar.gz.split* > Combined_data.tar.gz \
tar -xvf Combined_data.tar.gz

3. Run DOSnet: \
python Main.py \
Example: \
python Main.py --multi_adsorbate=1 --data_dir='Combined_data' --save_model=1 --batch_size=128

Output will be written to txt files as "predict_test.txt" or "predict_train.txt" or "CV_predict.txt" for a cross-validation run.

4. plot.py

python3 plot.py --dataname="CH_data" --data="test"


5. option

- ドロップアウトの値を変えてまとめて実行\
python3 chanege_dropout.py\
実行して作成したデータをグラフに
python3 plot_errerbar_dropout.py


