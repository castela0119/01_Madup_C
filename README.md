# Madup

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-%20v3.8%20-blue.svg?&style=flat&logo=Python&logoColor=white&labelColor=abcdef&cacheSeconds=3600$logoWidth=60)
  ![Miniconda](https://img.shields.io/badge/Conda-%20miniconda%20-lightgreen.svg?&style=flat&logo=Anaconda&logoColor=white&labelColor=44A833&cacheSeconds=3600$logoWidth=60)
  ![MySQL](https://img.shields.io/badge/MySQL-%20v8.0%20-4479A1.svg?&style=flat&logo=MySQL&labelColor=ffffff&cacheSeconds=3600$logoWidth=80)
</div>

[//]: <app 추가되면 수정>

```bash
# tree -L 2 -d
.
├── advertisers
│   └── migrations
│   └── tests
├── config
├── products
│   ├── migrations
│   └── tests
├── scripts
└── src
    ├── images
    └── reports

11 directories
```

## [Project Progress](https://github.com/orgs/PreOnboarding-Team-C/projects/1/views/2) [^kanban]

본 프로젝트에서는 None, Todo, In Progress, Done으로 나누어 공유가 가능하도록 합니다. 중요도는 상황에 따라 상대적으로 부여될 수 있기에, 담당자의 판단 하에 priorities를 설정해주시길 바랍니다.

## Contexts
* [Tasks](#tasks)
* [Rules](#rules)
* [Roles](#roles)

---
### Tasks
#### Infos
* Terms 
  * CTR(Click-Through Rate): 광고 노출 대비 클릭률 = click * 100 / impression 
  * ROAS(Return On Advertising Spend): 광고비 대비 매출액 = cv [^1] * 100 / cost
  * CPC(Cost Per Click): 클릭 당 광고비 = cost / click
  * CVR(Conversion Rate): 클릭 대비 전환율 = conversion * 100 / click
  * CPA(Cost Per Action): 전환 당 광고비 = cost / conversion

* DATASET
  | advertiser | uid | media | date | cost | impression | click | conversion | cv |
  |------------|-----|-------|------|------|------------|-------|-----------|----|

  주어진 데이터 셋의 칼럼명은 위와 같다.

  [simple analytics report](./src/reports/analytics_day1.md)를 참고하면, load 기준으로 부여된 index [78, 840, 940, 942, 24, 25, 891, 149, 191, 68840]가 중복됨을 확인할 수 있다. 이는 migration을 할 때 염두해야 할 내용이다.
  
* ERD
  ![Alt test](./src/images/erd_v3.png "erd sketch - version 2")

* Output
  ```shell
  1{
  2 "naver": {
  3 "ctr": 0.51,
  4 "cpc": 990.55,
  5 "roas": 265.38,
  6 "cvr": 8.33,
  7 "cpa": 881.01
  8 },
  9 "facebook": {
  10 "ctr": 0.51,
  11 "cpc": 990.55,
  12 "roas": 265.38,
  13 "cvr": 8.33,
  14 "cpa": 881.01
  15 },
  ```

---
### Rules

  
* Code Conventions
  * class: Upper Camel Case ex) UserSerializer
  * function: snake_case ex) get_user_information()
  * DB table, columns: snake_case ex) advertiser_reports
  * 必) DB index 설정
  * 클래스 작성 및 수정 시, 클래스명 바로 하단에 여러 줄의 주석을 활용해, assignee, reviewer 정보 기입

---
### Roles
* 개발 환경 구축, 광고주 CRUD (assignee: [@Bruno-Jang](https://github.com/Bruno-Jang))
* 모델링, 조회(assignee: [@do-not-do-that](https://github.com/do-not-do-that))
* Migration, REST API 설계(assignee: [@castela0119](https://github.com/castela0119))
* 테스트 코드, 케이스 작성(assignee: [@AshbeeKim](https://github.com/AshbeeKim))

---

[//]: <가산점은 현재 고려사항이 아니기에 pass>

---
### Comments
[^kanban]: 통상적으로 backlog, in-progress, peer-review, in-test, done, blocked 로 구분해서 업무를 처리 과정에 따라 확인할 수 있는 보드를 칸반 보드라고 함. 간단하게 협업의 감을 익히기 위해 사용함.ref) [WIKIPEDIA | Kanban Board](https://en.wikipedia.org/wiki/Kanban_board) 
[^1]: cv([Conversion Value](https://www.investopedia.com/terms/c/conversion-value.asp))
[^2]: 용어로 설명된 내용은 광고 채널(매체) 별 광고 효용에 대한 지표를 얻을 수 있는 일종의 보고서와 같다. 출력 형태는 소숫점 둘째자리까지 출력(이하 버림)하도록 하고, Output을 참고하면 됨.
