# 🎀 패키지 구조
<details>
  <summary><b>패키지 트리 구조</b></summary>
  <div markdown="1">

```
C:.
│  calculator.sqlite3
│  calculator_crud.py
│  database.py
│  main.py
│  models.py
│  schemas.py
│
\---template
    │  base.html
    │  index.html
    │
    └─static
           calculator.JPEG
```

  </div>
</details>
유지보수/테스트 용이성, 재사용성을 높이기 위해 패키지 구분.<br>
프론트엔드를 구성하는 html 파일은 template 폴더에 따로 저장, 이미지 폴더도 구분을 위해 static 폴더에 저장.<br>
기능은 모델, CRUD 함수들을 모아놓은 파일, 스키마, DB, main으로 구분하여 저장

# 🎀 추가기능
1. 나머지 연산 (%)
2. 루트 (√)
