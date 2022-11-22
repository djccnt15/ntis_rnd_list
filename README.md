# 국가 R&D 리스트 OpenAPI 활용 프로젝트

[국가과학기술지식정보서비스](https://www.ntis.go.kr/)의 [국가R&D통합공고](https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do) 공지 스크래핑, 데이터 전처리, 분석 및 시각화 프로젝트  

## 시도한 방법들

0. openAPI를 통한 데이터 수집
  - API 데이터가 공고에 대한 데이터가 아닌 과제 메타 정보 검색용이라 취소
0. RSS Feed를 통한 데이터 수집
  - 데이터가 대체로 일치하지만 완벽히 일치하지 않아 취소
0. Selenium, requests, Beautifulsoup를 이용한 직접 스크래핑(현재)