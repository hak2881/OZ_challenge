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
