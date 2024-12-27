## ✨ Admin 페이지 프론트단 제작 프로젝트

### 기본 요구사항
>  - 카테고리를 클릭하면 상의, 하의, 신발, 패션잡화 메뉴가 나오게 코드 작성
>  - 입력 버튼 안에 “제품명을 입력해주세요”가 나오게 코드 작성
>  - 조회 버튼이 입력창 옆에 붙어 있도록 코드 작성
>  - 테이블을 이용해 최 상단에는 속성 값을 넣고 하단에는 데이터가 입력되도록 코드 작성
>  - 최 하단에는 페이지 네이션 기능이 나타나도록 코드 작성

## 🧑‍💻 제작과정
---

#### 1. 카테고리 선택 메뉴 
카테고리를 클릭하면 상의, 하의, 신발, 패션잡화 메뉴가 나오게 합니다. 사용자에게 카테고리를 선택할 수 있는 옵션을 명확히 보여주며, 드롭다운을 사용하여 공간을 절약합니다.
```html
<!-- form 안에 작성 -->
      <div class="col-12">
        <select class="form-select" id="inlineFormSelectPref" name="category_data_table">
          <option value="" selected>카테고리를 선택하세요</option>
          <option value="상의">상의</option>
          <option value="하의">하의</option>
          <option value="신발">신발</option>
          <option value="패션잡화">패션잡화</option>
        </select>
      </div>
```
#### 2. 입력 버튼에 안내 문구
사용자가 제품명을 입력할 때 바로 안내 문구가 보이도록 placeholder 속성을 추가하여 UX를 개선합니다.
```html
<!-- form 안에 작성 -->
       <div class="col-3">
        <input type="text" class="form-control" placeholder="제품명을 입력해주세요">
      </div>
```
#### 3. 조회 버튼 위치 조정
조회 버튼은 입력창 바로 옆에 위치해 사용자가 쉽게 조회할 수 있도록 합니다. 이를 위해 col-auto 클래스를 사용하여 버튼과 입력창의 위치를 가깝게 만듭니다.
```html
<!-- form 안에 작성 -->
<div class="col-auto">
        <button type="button" class="btn btn-primary">조회</button>
</div>
```
#### 4. 페이지 네이션
테이블에 페이지 네이션 기능을 추가하여 많은 데이터가 있을 때 사용자가 쉽게 페이지를 넘길 수 있도록 합니다. UX를 고려하여 버튼들을 중앙 정렬하고, "이전"과 "다음" 버튼을 추가하여 탐색을 용이하게 만듭니다.
```html
    <!-- 페이지 네이션 -->
    <nav>
      <ul class="pagination justify-content-center">
        <li class="page-item"><a class="page-link" href="#">이전</a></li>
        <li class="page-item"><a class="page-link" href="#">1</a></li>
        <li class="page-item"><a class="page-link" href="#">2</a></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item"><a class="page-link" href="#">다음</a></li>
      </ul>
    </nav>
  </div>
```




## 챌린지 기능 구현
>  - 오늘 날짜와 현재 시간을 볼 수 있도록 기능을 구현해주세요
>  - 다크모드 기능을 만들어주세요
>  - 성별을 선택할 수 있는 셀렉터를 추가해주세요
>  - 회원 가입 버튼을 만들고 회원가입 버튼을 누르면 회원 가입 폼이 나오도록 기능을 만들어주세요


### 🧑‍💻 제작과정
---

#### 1. 현재 날짜와 시간 표시
페이지 상단에 현재 날짜와 시간을 실시간으로 업데이트하여 사용자에게 유용한 정보를 제공합니다.
```html
<!-- body에 작성 -->
<div class="mb-3">
      <span id="currentDateTime"></span>
</div>

<!-- script 에 표시 -->
<script>
    function updateDateTime() {
      const now = new Date();
      document.getElementById('currentDateTime').textContent = now.toLocaleString('ko-KR');
    }
    setInterval(updateDateTime, 1000);
    updateDateTime();
</script>
```
#### 2. 다크모드 기능
다크모드를 제공하여 사용자에게 더 편안한 환경을 제공합니다. 다크모드를 켜거나 끄는 기능은 버튼으로 제공되며, input 요소에 form-check-input 클래스를 사용하여 스타일을 일관되게 유지합니다.
```html
<!-- head -->
  <style>
    body.dark-mode {
      background-color: #121212;
      color: #ffffff;
    }
    .dark-mode .table {
      color: #ffffff;
    }
  </style>
<!-- body -->
<!-- 다크모드 스위치 -->
    <div class="form-check form-switch mb-3">
      <input class="form-check-input" type="checkbox" id="darkModeSwitch">
      <label class="form-check-label" for="darkModeSwitch">다크 모드</label>
    </div>

<!-- script 에 표시 -->
<script>
    // 다크모드 기능
    document.getElementById('darkModeSwitch').addEventListener('change', function () {
      document.body.classList.toggle('dark-mode', this.checked);
    });
</script>
```
#### 3. 성별 셀렉터 추가
성별을 선택할 수 있는 셀렉터를 추가하여 사용자가 성별에 맞는 필터링을 쉽게 할 수 있도록 합니다. 이로써 성별에 따른 데이터 조회가 가능해집니다.

```html
    <div class="mt-3">
      <label for="genderSelect" class="form-label">성별</label>
      <select class="form-select" id="genderSelect">
        <option value="전체" selected>전체</option>
        <option value="남성">남성</option>
        <option value="여성">여성</option>
      </select>
    </div>
```
#### 4. 회원 가입 버튼
회원 가입 버튼을 클릭하면 회원 가입 폼이 나타나도록 구현하여 사용자가 회원 가입을 원활하게 진행할 수 있도록 합니다. 폼은 사용자가 제출할 수 있는 텍스트 필드를 포함하고 있습니다.
``` html
<!-- body -->
    <div class="mt-3">
      <button id="signupButton" class="btn btn-success">회원 가입</button>
    </div>
    <div id="signupForm" class="mt-3" style="display: none;">
      <h5>회원 가입</h5>
      <form>
        <div class="mb-3">
          <label for="username" class="form-label">이름</label>
          <input type="text" class="form-control" id="username">
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">이메일</label>
          <input type="email" class="form-control" id="email">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">비밀번호</label>
          <input type="password" class="form-control" id="password">
        </div>
        <button type="submit" class="btn btn-primary">제출</button>
      </form>
    </div>

<!-- script 에 표시 -->
<script>
    document.getElementById('signupButton').addEventListener('click', function () {
      const form = document.getElementById('signupForm');
      form.style.display = form.style.display === 'none' ? 'block' : 'none';
    });
</script>
```

# ✨ 회원가입 양식 구현

이 프로젝트는 사용자 회원가입 양식을 구현한 예제입니다. 사용자가 회원가입 양식을 작성하고 제출할 수 있으며, 제출 후 입력한 정보를 확인할 수 있습니다. 또한, 다크모드 기능과 간단한 유효성 검사를 포함하고 있습니다.

## 기능

### 1. **회원가입 폼**

- 사용자로부터 다음 정보를 입력받습니다:
  - 아이디
  - 비밀번호
  - 비밀번호 확인
  - 이름
  - 전화번호
  - 성별
  - 이메일

### 2. **아이디와 비밀번호 유효성 검사**
- 아이디는 **6자 이상**이어야 합니다.
- 비밀번호는 **비밀번호 확인**란과 일치해야 합니다.

### 3. **다크모드**
- 사용자가 다크모드를 활성화하거나 비활성화할 수 있습니다.
- 다크모드가 활성화되면 페이지 배경과 버튼 색상이 어두운 테마로 변경됩니다.

### 4. **회원가입 완료 후 알림창 표시**
- 회원가입을 완료하면 **알림창**을 통해 사용자가 입력한 정보를 확인할 수 있습니다.
- 회원가입 완료 후 페이지로 리다이렉션됩니다.

## 코드 설명

### 🧑‍💻 HTML 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회원가입 양식</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* 기본 스타일 */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }

        /* 다크모드 스타일 */
        body.dark-mode {
            background-color: #121212;
            color: white;
        }

        .container {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        body.dark-mode .container {
            background-color: #1e1e1e;
            color: white;
        }

        form h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        /* 버튼에 대한 다크모드 스타일 */
        body.dark-mode button {
            background-color: #444;
            color: white;
        }

        /* 버튼 hover */
        body.dark-mode button:hover {
            background-color: #555;
        }

        button {
            width: 100px;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <div id="container" class="container mt-5">
        <form id="form">
            <h2>회원가입 양식</h2>
            <div class="mb-3">
                <label for="id" class="form-label">아이디</label>
                <input type="text" id="id" name="id" class="form-control" placeholder="아이디" required>
            </div>
            <div class="mb-3">
                <label for="pw1" class="form-label">비밀번호</label>
                <input type="password" id="pw1" name="pw1" class="form-control" placeholder="비밀번호" required>
            </div>
            <div class="mb-3">
                <label for="pw2" class="form-label">비밀번호 확인</label>
                <input type="password" id="pw2" name="pw2" class="form-control" placeholder="비밀번호 확인" required>
            </div>
            <div class="mb-3">
                <label for="name" class="form-label">이름</label>
                <input type="text" id="name" name="name" class="form-control" placeholder="사용자 이름" required>
            </div>
            <div class="mb-3">
                <label for="phone" class="form-label">전화번호</label>
                <input type="text" id="phone" name="phone" class="form-control" placeholder="휴대전화 번호">
            </div>
            <div class="mb-3">
                <label class="form-label">성별</label>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="gender" value="male" checked>
                    <label class="form-check-label">남자</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="gender" value="female">
                    <label class="form-check-label">여자</label>
                </div>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">이메일</label>
                <input type="email" id="email" name="email" class="form-control" title="정확한 메일 주소를 작성해주세요">
            </div>
            <div class="mb-3">
                <button type="submit" class="btn btn-primary">가입</button>
                <button type="reset" class="btn btn-secondary">리셋</button>
            </div>
        </form>
    </div>

    <!-- 다크모드 전환 버튼 -->
    <div class="position-fixed bottom-0 end-0 p-3">
        <button id="dark-mode-toggle" class="btn btn-dark">다크모드</button>
    </div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // 다크모드 토글 기능
        const darkModeToggle = document.getElementById("dark-mode-toggle");
        darkModeToggle.addEventListener("click", function() {
            document.body.classList.toggle("dark-mode");
        });

        // 회원가입 폼 제출 이벤트 핸들링
        const form = document.getElementById("form");
        form.addEventListener("submit", function(event) {
            event.preventDefault();

            // 폼 데이터 수집
            let userId = event.target.id.value;
            let userPw1 = event.target.pw1.value;
            let userPw2 = event.target.pw2.value;
            let userName = event.target.name.value;
            let userPhone = event.target.phone.value;
            let userGender = event.target.gender.value;
            let userEmail = event.target.email.value;

            // 아이디 유효성 검사
            if (userId.length < 6) {
                alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.");
                return;
            }

            // 비밀번호 일치 여부 검사
            if (userPw1 !== userPw2) {
                alert("비밀번호가 일치하지 않습니다.");
                return;
            }

            // 가입 완료 후 알림창 표시
            alert(`회원가입이 완료되었습니다!\n\n아이디: ${userId}\n이름: ${userName}\n전화번호: ${userPhone}\n성별: ${userGender}\n이메일: ${userEmail}`);

            // 페이지 전환 (리다이렉션)
            window.location.href = "success.html";
        });
    </script>
</body>
</html>
