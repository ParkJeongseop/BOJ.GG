# BOJ.GG
Beakjoon Online Judge 전적검색 및 통계 프로그램


20181617 박정현

20181616 박정섭

# 개발문서

## 요구사항 명세서 (SRS) Software Requirement Specification

1.기능적 요구사항
 * 1-1. Beakjoon Online Judge(이하 BOJ)의 user페이지를 파싱하여 데이터를 불러온다.
 * 1-2. BOJ의 user정보가 올바른지 확인한다.
 * 1-3. 사용자 채점 현황을 불러온다.
 * 1-4. 사용자 채점 현황 중 맞은 문제를 불러와 통계를 내어 그래프로 표시해 준다.

2.사용자 인터페이스 요구사항
 * 2-1. userID를 입력받는 window
   + 2-1-1. 프로그램 이름 label
 * 2-2. 전적 및 통계 표시 window
   + 2-2-1. 사용자 정보 표시 QTableWidget
   + 2-2-2. 사용자 채점 현황 QTableWidget
   + 2-2-3. 사용자 통계 그래프

3.비기능적 요구사항
 * 3-1. 이 소프트웨어의 구현에는 Python, PyQt5, BeautifulSoup을 이용한다.
 
 
 
## 구조설계서 (ADS) Architecture Design
| 모듈 | 클래스 | 역할 |
| ------------ | ------------- | ------------- |
| main.py | MainWindow | 사용자ID 입력받는 window |
|  | UserInfoWindow | 검색 내용 출력 window |
|  | Window |  |
| boj.py |  | SW의 핵심 로직 구현 |

## 상세설계서 (DDS)
main.py

| 클래스 | 메서드 | 입력인자 | 출력인자 | 기능 |
| ------------ | ------------- | ------------- | ------------- | ------------- |
| MainWindow | setupUI | | | 기본 UI 구성 |
|  | retranslateUI | | | 사용자ID 입력받는 window 구성
| UserInfoWindow | setupUI | | | 검색 내용 출력 window UI 구성|
| | setupUserInfo | | | 사용자정보 구성 |
| | setupStatus | | | 상태 구성 |
| | setupGraph | | | 그래프 구성 |
| Window | startMainWindow | | | |
| | startUserInfoWindow | userID | | |

boj모듈

| 함수 | 입력인자 | 출력인자 | 기능 |
| ------------ | ------------- | ------------- | ------------- |
| isBOJUser | userID | Boolean | 올바른 userID인지 boolean으로 출력 |
| getUserInfo | userID | list | User의 정보를 불러와리스트로 출력 |
| getStatus | userID | list | User의 채점현황을 불러와 리스트로 출력 |
| getAcceptedData | userID | list | User의 채점현황중 맞은 문제를 불러와 리스트로 출력 |


## 단위 테스트 보고서 (UTR)

## 소프트웨어 패키지

## 통합 테스트 보고서 (ITR)
