## ✨ Admin 페이지 프론트단 제작 프로젝트

### 기본 요구사항
>  - 카테고리를 클릭하면 상의, 하의, 신발, 패션잡화 메뉴가 나오게 코드 작성
>  - 입력 버튼 안에 “제품명을 입력해주세요”가 나오게 코드 작성
>  - 조회 버튼이 입력창 옆에 붙어 있도록 코드 작성
>  - 테이블을 이용해 최 상단에는 속성 값을 넣고 하단에는 데이터가 입력되도록 코드 작성
>  - 최 하단에는 페이지 네이션 기능이 나타나도록 코드 작성

## 🧑‍💻 제작과정
---

* 카테고리를 클릭하면 상의, 하의, 신발, 패션잡화 메뉴가 나오게 코드 작성
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
* 입력 버튼 안에 “제품명을 입력해주세요”가 나오게 코드 작성
```html
<!-- form 안에 작성 -->
       <div class="col-3">
        <input type="text" class="form-control" placeholder="제품명을 입력해주세요">
      </div>
```
* 조회 버튼이 입력창 옆에 붙어 있도록 코드 작성
```html
<!-- form 안에 작성 -->
<div class="col-auto">
        <button type="button" class="btn btn-primary">조회</button>
</div>
```
* 최 하단에는 페이지 네이션 기능이 나타나도록 코드 작성
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




### 챌린지 기능 구현
>  - 오늘 날짜와 현재 시간을 볼 수 있도록 기능을 구현해주세요
>  - 다크모드 기능을 만들어주세요
>  - 성별을 선택할 수 있는 셀렉터를 추가해주세요
>  - 회원 가입 버튼을 만들고 회원가입 버튼을 누르면 회원 가입 폼이 나오도록 기능을 만들어주세요


## 🧑‍💻 제작과정
---

* 오늘 날짜와 현재 시간을 볼 수 있도록 기능을 구현해주세요
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
* 다크모드 기능을 만들어주세요
```html
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
* 성별을 선택할 수 있는 셀렉터를 추가해주세요

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
* 회원 가입 버튼을 만들고 회원가입 버튼을 누르면 회원 가입 폼이 나오도록 기능을 만들어주세요
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
