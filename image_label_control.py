import os
import random
import shutil

# 데이터셋 경로 (사용자 경로에 맞게 수정)
base_path = "Link"  # train, valid, test가 포함된 최상위 디렉토리
output_path = "바탕 화면"  # 샘플링된 데이터셋 저장 경로
os.makedirs(output_path, exist_ok=True)

# 각 세트의 디렉토리
datasets = ['train', 'valid', 'test']

# 전체 샘플 수 설정
total_target_size = 1000

# 샘플링 및 파일 복사 함수
def sample_and_copy(source_images_dir, source_labels_dir, target_images_dir, target_labels_dir, sample_size):
    os.makedirs(target_images_dir, exist_ok=True)
    os.makedirs(target_labels_dir, exist_ok=True)

    # 이미지 및 라벨 파일 로드
    images = [f for f in os.listdir(source_images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
    sampled_images = random.sample(images, min(len(images), sample_size))

    # 파일 복사
    for img_file in sampled_images:
        # 이미지 복사
        shutil.copy(os.path.join(source_images_dir, img_file), os.path.join(target_images_dir, img_file))

        # 라벨 파일 복사 (이미지 이름에서 확장자만 .txt로 교체)
        label_file = os.path.splitext(img_file)[0] + ".txt"
        shutil.copy(os.path.join(source_labels_dir, label_file), os.path.join(target_labels_dir, label_file))

# 데이터셋 처리
total_images = sum(len(os.listdir(os.path.join(base_path, ds, 'images'))) for ds in datasets)

for ds in datasets:
    source_images_dir = os.path.join(base_path, ds, 'images')
    source_labels_dir = os.path.join(base_path, ds, 'labels')

    target_images_dir = os.path.join(output_path, ds, 'images')
    target_labels_dir = os.path.join(output_path, ds, 'labels')

    # 각 데이터셋의 샘플 수 계산
    dataset_size = len(os.listdir(source_images_dir))
    sample_size = int((dataset_size / total_images) * total_target_size)

    # 샘플링 및 복사
    sample_and_copy(source_images_dir, source_labels_dir, target_images_dir, target_labels_dir, sample_size)

print(f"샘플링 완료: {output_path}에 저장되었습니다.")
