# 🌱 Gardening Mate(진행중, 2025.07~현재)
<br>
실시간으로 작물의 환경을 모니터링하는 시스템입니다.(ex. 토양의 수분율 등)
<br>
<br>

## 프로젝트 소개
- 토양의 수분, 온도, 습도 등의 환경 정보를 주기적으로 수집하고 이를 클라우드에 저장해 개인 디바이스에서 확인할 수 있는 스마트 파밍 시스템입니다.
- 센서를 통해 라즈베리파이로 데이터를 수집한 뒤 AWS S3, Lambda, RDS 등 클라우드 서비스를 활용하여 데이터를 관리하고 디바이스를 통해 사용자에게 제공하는 것을 목표로 합니다.
- 직접 밭을 가꾸면서 식물의 환경을 눈으로만 인지하는 것에는 한계가 있어 시작하게 된 프로젝트입니다.
  <p align="center">
    <img width="500" src="https://github.com/user-attachments/assets/a55284e9-9481-4f2d-92ca-967ab41882f9" />
  </p>
<br>

## 프로젝트 구성도
<p align="center">
  <img width="900" alt="스크린샷 2025-07-21 오전 1 39 56" src="https://github.com/user-attachments/assets/affbcb6e-5aac-42c9-aed5-e46ecc46a200" />
</p>
<br>

## 토양 수분 측정 센서 - 라즈베리파이 연결 회로도
<p align="center">
  <img width="900" alt="스크린샷 2025-07-20 오후 7 50 45" src="https://github.com/user-attachments/assets/989ea873-bdbe-4cf6-86c6-53fd3b575e00" />
</p>
<br>

## 파일 별 설명
read_and_save_rate.py : 토양 수분 센서로부터 아날로그 데이터를 읽어와 CSV 파일로 저장한다.<br>
upload_s3.py : CSV파일을 AWS S3에 업로드한다.<br>
data_to_graph.py : CSV파일 기반으로 Streamlit을 활용하여 시간별 수분율을 그래프로 시각화한다.<br>
