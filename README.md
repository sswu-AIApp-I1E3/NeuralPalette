# NeuralPalette🎨
성신여자대학교 2025-1 인공지능 응용 팀프로젝트
<br/><br/>

## 프로젝트 주제
> 논문 [Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization](https://arxiv.org/abs/1703.06868) 구현 및 개선

```
@inproceedings{huang2017adain,
  title={Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization},
  author={Huang, Xun and Belongie, Serge},
  booktitle={ICCV},
  year={2017}
}
```

<br/>

## 'I1E3' 팀 소개
|이름|역할|
|---------|-------------|
|김희주(팀장)|발표, decoder 구현 및 최적화|
|이나경(팀원)|논문 review 및 discussion, encoder 구현 및 최적화|
|채서연(팀원)|데이터 수집 및 전처리, encoder 구현 및 최적화|
|강민정(팀원)|article 정리, decoder 구현 및 최적화|

<br/>

## 주차별 계획
|주차|기간|내용|
|-----|:----:|----------|
|6주차|4/10 ~ 4/16|프로젝트 방향성 및 주제 선정|
|7주차|4/17 ~ 4/23|논문 읽기 및 이미지 처리 공부|
|8주차|4/24 ~ 4/30|논문 review 및 discussion, 중간 발표 준비|
|9주차|5/1 ~ 5/7|감정 분류 모델 데이터 수집 및 전처리|
|10주차|5/8 ~ 5/15|감정 분류 모델 구현|
|11주차|5/16 ~ 5/21|AdaIN 데이터 수집 및 전처리|
|12주차|5/22 ~ 5/28|AdaIN 모델 구성|
|13주차|5/29 ~ 6/4|최종 평가 및 검증|
|14주차|6/5 ~ 6/11|article 정리 및 발표 준비|

<br/>

## 주차별 팀원 기여도
|이름|6주차|7주차|8주차|9주차|10주차|11주차|12주차|13주차|14주차|
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|김희주|25%|25%|25%|25%|25%|25%|25%|
|이나경|25%|25%|25%|25%|25%|25%|25%|
|채서연|25%|25%|25%|25%|25%|25%|25%|
|강민정|25%|25%|25%|25%|25%|25%|25%|

<br/><br/>

## 회의록
### 6주차
> 프로젝트 방향성 및 주제 선정
* 일시 및 장소: 2025/04/13 일요일 오후 10시 Google Meet
* 참석 인원: 김희주, 이나경, 채서연, 강민정
* 회의 내용
  - 논문 학습 및 구현으로 프로젝트 방향성 결정
  - 각자 논문과 해당 소스코드 찾아와서 공유
  - 논문 선정
  - 팀명 및 프로젝트명 논의, 주차별 활동 계획 수립, 역할 분담(임시)
* 회의 사진
  <br/>
  <img width="600" alt="Image" src="https://github.com/user-attachments/assets/e5b8a51e-7324-4ef9-968b-d762f0e40e1d" />

<br/>

### 7주차
> 논문 읽기 및 이미지 처리 공부
* 일시 및 장소: 2025/04/20 일요일 오후 10시 Google Meet
* 참석 인원: 김희주, 이나경, 채서연, 강민정
* 회의 내용
  - 논문 주요 내용 요약
  - 다음주 논문 review 및 discussion 준비
  - 중간 발표 준비 역할 분담: 자료 조사 - 나경 & 민정, 발표 자료 제작 - 희주 & 서연
* 논문 주요 내용 요약 <br/>   
  3. Background <br/>
  <blockquote>
  BN layer에서는 input batch가 주어졌을 때 각각의 feature 채널에 대해서 평균과 표준편차를 normalize한다. BN layer보다 성능이 좋은 IN layer에서는 각각의 채널과 샘플에 대해 독립적인 공간 차원에서 평균과 표준편차가 계산된다. 이후 각 스타일마다 다른 파라미터를 학습하는 CIN layer가 제안됐는데, 네트워크에서 같은 convolutional parameter가 사용되기 때문에 완전 다른 스타일도 생성하는 것이 가능해졌다.<br/>
  하지만 nomalization layer가 없는 네트워크와 달리, CIN layer가 있는 네트워크는 추가적으로 2FS개(F는 feature map 개수, S는 스타일 개수)의 파라미터를 요구하기 때문에 스타일 수가 많을 때는 확장이 어렵다. 또한 새로운 스타일에 대해서는 재학습이 필요하다는 단점이 있다.
  </blockquote>
  <br/>
  4. Interpreting Instance Normalization<br/>
  <blockquote>
  IN은 content image의 contrast에 영향을 받지 않고, affine parameters가 출력 이미지의 스타일을 완전히 변경할 수 있다는 특징이 있다. 또한, 개별 이미지의 스타일을 target style로 정규화 하여 content manipulation에 집중할 수 있으므로 학습에 용이하다. 실험에 따르면, IN이 BN보다 빠르게 수렴하며 정규화 된 이미지에 대해서도 효과적인 성능을 보인다.<br/>
  <img width="452" alt="Image" src="https://github.com/user-attachments/assets/5bdf480d-71e0-453c-9233-0cc308ce4fff" />
  </blockquote>
  <br/>
  5. Adaptive Instance Normalization <br/>
  <blockquote>
    <img width="452" alt="Image" src="https://github.com/user-attachments/assets/fc333bd2-9c41-455d-8d5b-fb4a4a6a3de3" /><br/>
  AdaIN은 content 입력 x 와 style 입력 y를 받아, x의 평균과 분산을 y의 통계값에 맞춰 정규화한다. 입력을 정규화한 뒤, y의 표준편차로 스케일링하고 평균을 더하는 방식이라 할 수 있다. BN, IN, CIN과는 달리 학습 가능한 affine 파라미터 없이 스타일 입력에서 통계값을 직접 계산한다. 이러한 통계값은 채널별로, 공간 전체를 기준으로 계산되며 스타일 특유의 질감을 효과적으로 전달할 수 있다는 장점이 있다.
  </blockquote>
  <br/>
  6. Experimental Setup<br/>
  <blockquote>
  이 논문의 실험 설정은 contents/style 이미지를 입력받는 스타일 전송 네트워크를 기반으로 한다. 아키텍처는 세 부분으로 구성된다: 1) 사전 훈련된 VGG-19의 초기 층(relu4_1까지)을 인코더로 고정 사용, 2) 콘텐츠 특징의 평균과 분산을 스타일 특징에 맞게 조정하는 AdaIN 레이어, 3) AdaIN 출력을 이미지 공간으로 변환하는 디코더(pulling 대신 up-sampling 사용, 테두리 artifacts 방지를 위한 반사 패딩 적용, 정규화 레이어 미사용)이다. 학습에는 MS-COCO와 WikiArt 데이터셋(각 80,000개 이미지)을 사용했고, 손실 함수는 AdaIN 출력과 생성된 이미지의 특징 간 콘텐츠 손실(AdaIN 출력과 생성된 이미지 특징 간 유클리드 거리) 및 VGG 레이어에서 계산된 스타일 손실(생성된 이미지와 스타일 이미지 간 IN 통계 매칭)의 조합으로 구성된다.
  </blockquote>

<br/>

* 회의 사진
  <br/>
  <img width="600" alt="Image" src="https://github.com/user-attachments/assets/c798ac32-a704-42b0-b829-201733d09636" />

<br/>

### 8주차
> 논문 review 및 discussion, 중간 발표 준비
* 일시 및 장소: 2025/04/26 토요일 오후 4시 30분 Google Meet
* 참석 인원: 김희주, 이나경, 채서연, 강민정
* 회의 내용
  - 논문 요약, 강/약점, 코멘트 공유
  - 구체적인 모델 개선 방향성 discussion
  - 중간 발표 준비
* 회의 사진
  <br/>
  <img width="600" alt="Image" src="https://github.com/user-attachments/assets/54f6f6f5-afdb-4b1e-b89c-81215abc3e70" />

<br/>

### 9주차
> 데이터 수집 및 전처리
* 일시 및 장소: 2025/05/05 월요일 오후 5시 Google Meet
* 참석 인원: 김희주, 이나경, 채서연, 강민정
* 회의 내용
  - 중간 발표 피드백
  - 데이터셋 구조 결정: 각 클래스별 6000장(총 24,000장)
    ```
    dataset/
    ├── images/
    │   ├── anger/
    │   │   ├── anger_0000.jpg
    │   │   ├── anger_….jpg
    │   │   ├── anger_6000.jpg
    │   ├── fear/
    │   │   ├── fear_0000.jpg
    │   │   ├── fear_….jpg
    │   │   ├── fear_6000.jpg
    │   ├── happy/
    │   │   ├── happy_0000.jpg
    │   │   ├── happy_….jpg
    │   │   ├── happy_6000.jpg
    │   ├── sadness/
    │   │   ├── sadness_0000.jpg
    │   │   ├── sadness_….jpg
    │   │   ├── sadness_6000.jpg
    └── labels.csv
    ```
  - 라벨 데이터 형태 결정
    ```
    <labels.csv>
    filename,emotion
    anger_0000.jpg,anger
    anger_0001.jpg,anger
    …
    sadness_4999,sadness
    sadness_6000,sadness
    ```
  - 이미지 수집 및 라벨링 역할 분담: [공개된 감정 데이터셋](https://qzyou.github.io/projects/sa-ds/) + 직접 이미지 수집 후 라벨링 진행
  - 감정 분류 모델 데이터셋 구축
* 회의 사진
  <br/>
  <img width="600" alt="Image" src="https://github.com/user-attachments/assets/bee27767-b3b0-4cbc-a2b6-df76608ff390" />

<br/>

### 10주차
> 감정 분류 모델 구현
* 일시 및 장소: 2025/05/08 목요일 오후 2시 30분 성신여자대학교 학생회관 스터디룸
* 참석 인원: 김희주, 이나경, 채서연, 강민정
* 회의 내용
  - 감정 데이터셋(24,000장) 공유 및 구현 역할 분담
  - 나경 & 서연: 감정 데이터셋 이용해 감정 분류 CNN 모델 구현
  - 민정 & 희주: 콘텐츠 이미지, 스타일 이미지 수집하고 인코딩으로 특징 추출, 감정 가중치 업데이트
  - 콘텐츠 이미지: 수집 예정(24,000장)
  - 스타일 이미지: WikiArt 데이터셋(24,000장)
* 회의 사진
  <br/>
  <img width="600" alt="Image" src="https://github.com/user-attachments/assets/4284a744-499f-43d4-9ac7-62c8455ab644" />

<br/>

### 11주차
> 감정 분류 모델 구현 - 회의록 폴더에 업로드
