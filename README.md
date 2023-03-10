# electric-car-charging-service

## 목차
<br>

1. [Summary](#-summary)
2. [사용 기술](#-사용-기술)
3. [ERD](#-erd)
4. [Task 관리](#-task-관리)
5. [API 명세서](#-api-명세서)
6. [브랜치 전략](#-브랜치-전략)
8. [컨벤션](#-코드-컨벤션)
9. [API 호출 테스트](#-api-호출-테스트)


<br>

## ✅ Summary
<br>

- 전기차 운전자들을 위한 충전소를 안내해주고 충전을 할 수 있는 서비스입니다.

<br>

- 사용자는 등록한 결제 수단으로 선불 충전과 후불 결제가 가능합니다.
- 사용자는 쿠폰을 지급받아 등록 할 수 있고, 결제시 사용 할 수 있습니다.
- 사용자는 충전소와 충전소의 충전기의 이용가능 여부를 쉽게 확인 할 수 있습니다.

<br>

#### User
- 인증은 JWT 토큰으로 이루어집니다.
- 회원가입, 로그인, 로그아웃, 토큰 재발급 기능을 제공합니다.
- 로그아웃시 기존에 발급받은 refresh token을 blacklist에 담아 사용을 제한합니다.

<br>

#### Coupon
- 관리자는 쿠폰을 생성, 조회, 수정, 삭제 할 수 있습니다.
- 인증된 사용자는 유효한 쿠폰을 등록할 수 있습니다.

<br>

#### Charging
- 관리자는 충전소를 생성, 수정, 삭제 할 수 있습니다.
- 관리자는 충전소의 충전기들을 생성, 수정, 삭제 할 수 있습니다.
- 인증된 사용자는 충전소들의 목록과 충전소의 충전기 목록을 조회 할 수 있습니다.
- 인증된 사용자는 충전 가능한 충전소 / 충전기의 목록을 조회 할 수 있습니다.

<br>

#### Payment
- 인증된 사용자는 결제수단을 생성, 조회, 수정, 삭제 할 수 있습니다.

<br>

## 🛠 사용 기술

<div align="center">
<br>

<img src="https://img.shields.io/badge/Python-blue?style=plastic&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django Rest Framework-EE350F?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-00979D?style=plastic&logo=MySQL&logoColor=white"/>

<br>
<br>

<img src="https://img.shields.io/badge/Github Actions-2088FF?style=plastic&logo=github actions&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-F05032?style=plastic&logo=Git&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub-grey?style=plastic&logo=github&logoColor=181717"/>

</div>
<br>

<br>

## 💡 ERD

<img width="1252" alt="충전 erd" src="https://user-images.githubusercontent.com/83942213/224421673-c5e9dc95-bbe5-4921-98f5-2572bdf134cb.png">


<br>

## 📜 API 명세서

<img width="1029" alt="스크린샷 2023-03-11 오전 5 27 20" src="https://user-images.githubusercontent.com/83942213/224421993-e83e89e7-4ce9-4809-8d52-f64b661f17de.png">

<br>

## 🔗 Task 관리

<img width="1079" alt="스크린샷 2023-03-11 오전 5 28 17" src="https://user-images.githubusercontent.com/83942213/224422137-f5086c3c-cc0d-40bc-8d57-565be5b6b9af.png">


- Github의 <a href="https://github.com/sxxk2/electric-car-charging-service/issues?q=is%3Aissue+is%3Aclosed" target="_blank">Issue</a> 와 
<a href="https://github.com/users/sxxk2/projects/7/views/1" target="_blank">Projects</a>를 사용합니다.
- issue 생성으로부터 개발을 시작하며 해당 기능을 개발 후 commit시 issue번호를 commit에 남깁니다.
- 명확한 라벨을 사용해 다른 작업자들도 한 눈에 보기 쉽게 구성했습니다.
 
<br>

## 🌱 브랜치 전략

- Github-flow를 사용합니다.
- main에서 파생된 feature 브랜치를 생성해 작업합니다.
- pull request를 통해 main에 병합합니다.
- pull reqeust template를 사용해 작업내용을 공유하고 호출테스트 사진을 첨부합니다.


<br>

## ✨🍰✨ 코드 컨벤션

- pre-commit
- github actions
- Formatter
  - isort
  - black
- Lint
  - flack8

<br>

### 💻 Local
<img width="662" alt="스크린샷 2022-08-19 오후 6 55 20" src="https://user-images.githubusercontent.com/83942213/185594792-dab3b933-9885-423a-a1b7-6f2c36d7af69.png">

- pre-commit 라이브러리를 통해 commit 시 자동으로 스테이징되어있는 코드에 대해 Formatter와 Linter를 실행합니다.
- 통과가 되지않는다면 커밋은 발생하지 않습니다.

<br>

### 🗄 Repository

<img width="1292" alt="스크린샷 2023-03-11 오전 5 33 08" src="https://user-images.githubusercontent.com/83942213/224422899-0dd5b2d5-56c3-41d3-ad96-fd0eae0ca264.png">

- push시 트리거가 되어 gitahub actions를 통해 코드 스타일을 체크합니다.
- pull reqeust상태에서 통과가 되지 않는다면 작업자들에게 알람을 줍니다.

<br>

## 💾 Pull reuqest 컨벤션

<img width="905" alt="스크린샷 2023-03-11 오전 5 32 00" src="https://user-images.githubusercontent.com/83942213/224423042-1b6b50b0-3ca6-4697-b657-b97ffd494a31.png">


- pull reuqest template를 설정해두어, PR 생성시 자동으로 불러와집니다.
- 해당 PR에 대한 배경지식이 없거나 적은 동료 리뷰어에게 리뷰를 받는다는 전제로 객관적으로 항목들을 작성합니다.
- 작성한 API의 호출 테스트를 사진과 함께 첨부합니다.

<br>

## 👌🏻 API 호출 테스트

### User

<br>

#### 회원가입 성공 (201)
<img width="1341" alt="체인 회원가입 성공" src="https://user-images.githubusercontent.com/83942213/224423371-10047cff-e3f2-4340-8b41-aff114e5f59a.png">


<br>

#### 회원가입 실패 (400)
<img width="1334" alt="체인 회원가입 실패 (닉네임, 이메일 중복)" src="https://user-images.githubusercontent.com/83942213/224423578-0df669da-188b-4245-9f72-67a27c265eb0.png">

- 이미 가입되어있는 이메일 or 닉네임

<br>

#### 회원가입 실패 (400)
<img width="1343" alt="체인 회원가입 실패(비밀번호 유효성검사)" src="https://user-images.githubusercontent.com/83942213/224423637-0b5547ff-c4da-40b0-bb4d-2ca311e68667.png">

- 비밀번호 유효성검사 통과 X (8~20자, 문자, 숫자, 기호의 조합)

<br>

#### 로그인 성공 (200)
<img width="1339" alt="체인 로그인 성공" src="https://user-images.githubusercontent.com/83942213/224423658-8d1bcb4d-a8bb-4b42-af4d-8b1cf3d509ea.png">

- aceess token과 refresh token 발급 후 리턴

<br>

#### 로그아웃 성공 (200)
<img width="1337" alt="체인 로그아웃 성공" src="https://user-images.githubusercontent.com/83942213/224423959-59ade088-229b-4832-991a-78554e9321bb.png">

- 로그인시 발급받았던 refresh token을 blacklisted 

<br>

#### access token 재발급 성공 (200)
<img width="1332" alt="체인 엑세스토큰 재발급 성공" src="https://user-images.githubusercontent.com/83942213/224424153-f122325d-bdf9-4f0b-95e8-0e369b663c7f.png">

- 로그인시 발급받았던 refresh token으로부터 access token 재발급

<br>

---

<br>

### Coupon

<br>

#### 쿠폰 생성 성공 (201)
<img width="1335" alt="체인 쿠폰 생성 성공 (201)" src="https://user-images.githubusercontent.com/83942213/224424283-aee19eaa-4e95-4f40-aa5d-9a19414462d9.png">

- 관리자 권한의 유저만 사용 가능

<br>

#### 쿠폰 목록 조회 성공 (200)
<img width="1339" alt="체인 쿠포 목록조회 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224424380-7647010b-b836-4584-bf96-add4f0de42a9.png">

- 관리자 권한의 유저만 사용 가능

<br>

#### 쿠폰 단건 상세조회 성공 (200)
<img width="1336" alt="체인 쿠폰 상세조회 성공(200)" src="https://user-images.githubusercontent.com/83942213/224424578-e9d14152-9da2-4151-91f8-43e76502f8bb.png">

- 관리자 권한의 유저만 사용 가능

<br>

#### 쿠폰 수정 성공 (200)
<img width="1334" alt="체인 쿠폰 수정 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224424664-817b73e8-a2f9-452f-8a7b-15b46710b8ee.png">

- 관리자 권한의 유저만 사용 가능
- 입력받은 데이터들과 함께 updated_at 컬럼 업데이트

<br>

#### 쿠폰 삭제 성공 (204)
<img width="1331" alt="체인 쿠폰 삭제 성공 (204)" src="https://user-images.githubusercontent.com/83942213/224424752-a8343fb6-1e94-4939-bf11-0ae282969455.png">

- 관리자 권한의 유저만 사용 가능

<br>

#### 쿠폰 등록 성공 (200)
<img width="1334" alt="체인 쿠폰 등록 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224424873-4b7428e2-bdc4-457e-b383-d3d87d88e3bc.png">

- coupon의 used_by, used_at 컬럼 업데이트

<br>

#### 쿠폰 등록 실패 (400)
<img width="1338" alt="체인 쿠폰 등록 실패 (400)" src="https://user-images.githubusercontent.com/83942213/224425070-1a9b27b1-8641-4735-aaa8-958d457c10d1.png">

- 유효하지 않은 쿠폰

<br>

---

<br>

### Charging

<br>

#### 충전소 생성 성공 (201)
<img width="1336" alt="체인 충전소 등록 성공 (201)" src="https://user-images.githubusercontent.com/83942213/224425360-bdf19719-7385-444f-a4f6-8efb23edf566.png">

- 관리자 권한의 유저만 사용 가능

<br>

#### 충전소 목록 조회 성공 (200)
<img width="1338" alt="체인 충전소 목록조회  쿼리스트링 포함 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224425423-661d4dd6-e4aa-4050-8edb-ce33a1d628b4.png">

- 쿼리파라미터로 is_available을 받아 사용 가능 여부를 필터링 할 수 있음

<br>

#### 충전기 생성 성공 (201)
<img width="1335" alt="체인 충전기 등록 성공 (201)" src="https://user-images.githubusercontent.com/83942213/224425657-65f54ad1-bf76-4803-aab0-4da86bced2e2.png">

- 관리자 권한의 유저만 사용 가능

<br>

#### 충전기 목록 조회 성공 (200)
<img width="1333" alt="체인 충전기 목록조회 필터 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224425735-f4e63179-45c7-438f-9f73-9d79492eef3d.png">

- 쿼리파라미터로 is_available과 type 을 받아 사용 가능 여부와 충전기의 타입을 필터링 할 수 있음

<br>

#### 충전기 단건 상세 조회 성공 (200)
<img width="1338" alt="체인 충전기 상세 조회 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224425950-d3cd3926-4c11-4226-83f1-166e9c10ec1a.png">

<br>

#### 충전기 수정 성공 (200)
<img width="1332" alt="체인 충전기 수정 성공 (204)" src="https://user-images.githubusercontent.com/83942213/224426019-46dccb96-69ce-427f-b2c2-e918b54c1c5c.png">

- 관리자 권한의 유저만 사용 가능

<br>

#### 충전기 삭제 성공 (204)
<img width="1338" alt="체인 충전기 삭제 성공 (204)" src="https://user-images.githubusercontent.com/83942213/224426102-48f6de9e-0a26-45fe-9fd0-98ae97cf692b.png">

- 관리자 권한의 유저만 사용 가능

<br>

---

<br>

### Payment

<br>

#### 결제 수단 생성 성공 (201)
<img width="1332" alt="체인 결제수단 등록 성공 (201)" src="https://user-images.githubusercontent.com/83942213/224426282-8f91c555-9b09-4346-86f0-7204c6014263.png">

<br>

#### 결제 수단 목록 조회 성공 (200)
<img width="1337" alt="체인 결제수단 목록조회 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224426356-613d9f24-3609-4483-9107-363b30976fdf.png">

<br>

#### 결제 수단 단건 상세조회 성공 (200)
<img width="1335" alt="체인 결제수단 상세조회 성공 (200)" src="https://user-images.githubusercontent.com/83942213/224426421-b9458b9c-3e7a-4d69-b4f2-d017da8cbedc.png">

<br>

#### 결제 수단 수정 성공 (200)
<img width="1336" alt="체인 결제수단 상세조회 수정 (200)" src="https://user-images.githubusercontent.com/83942213/224426474-420ce9fe-ca76-4497-8705-ee875f500f65.png">

<br>

#### 결제 수단 삭제 성공 (204)
<img width="1333" alt="체인 결제수단 삭제 성공 (204)" src="https://user-images.githubusercontent.com/83942213/224426521-94eaf409-3807-4b45-a543-b14c4102a180.png">

<br>



