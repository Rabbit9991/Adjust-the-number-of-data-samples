# Adjust-the-number-of-data-samples
Adjust the number of data samples
Code that divides each data set into test train values for training

각각의 데이터 셋을 test train valid로 나누어 학습시키기 위해 분할 하는 코드


기본 경로 설정: base_path를 원본 데이터셋이 있는 최상위 디렉토리 설정  
출력 경로 설정: output_path를 샘플링된 데이터셋이 저장 위치 설정  
스크립트 실행: Python 환경에서 실행하면 train, valid, test 데이터셋에서 샘플을 추출하여 새로운 디렉토리 저장  

### 실행 예시  
python dataset_sampling.py
