# 🚭 No Smoking Tweet Bot (GitHub Actions + Twitter API v2)

매일 자동으로 “금연 n일째” 트윗을 이어붙여주는 스레드 봇입니다.
깃허브 액션으로 동작하며, Python + Tweepy + Twitter API v2를 사용합니다.

---

## 📅 동작 예시

- 첫 실행 → `🚭 금연 1일째! 오늘도 참고 있다.`  
- 다음날 → `🚭 금연 2일째! 오늘도 참고 있다.`  
- 이렇게 트윗이 **자동으로 스레드(연속 트윗)** 형태로 이어집니다.

---

## ⚙️ 설정 방법

### 1️⃣ 트위터 API 키 발급

Twitter Developer 계정에서 API Key/Secret, Access Token/Secret 4개를 발급받습니다.

### 2️⃣ 깃허브 Secrets 등록

GitHub 레포 → **Settings → Secrets → Actions → New repository secret**

| 이름 | 설명 |
|------|------|
| `TWITTER_API_KEY` | Twitter API Key |
| `TWITTER_API_KEY_SECRET` | Twitter API Secret |
| `TWITTER_ACCESS_TOKEN` | Access Token |
| `TWITTER_ACCESS_TOKEN_SECRET` | Access Token Secret |

### 3️⃣ 코드 업로드

이 폴더 구조 그대로 깃허브에 push 합니다.

---

## 🕒 자동 실행

- 매일 **00:00 UTC (한국시간 오전 9시)** 자동 트윗  
- 수동 실행도 가능 (Actions 탭 → Run workflow)

---

## ✅ 파일 설명

| 파일 | 설명 |
|------|------|
| `tweet_bot.py` | 트윗 작성 로직 (스레드 이어붙이기 포함) |
| `tweet_id.txt` | 마지막 트윗 ID 기록용 파일 |
| `.github/workflows/tweet.yml` | GitHub Actions 자동 실행 설정 |
| `README.md` | 설명서 |

---

## 🧩 커스터마이징

- `tweet_bot.py` 안의 `start_date` 수정하면 시작일 바꿀 수 있음  
  ```python
  start_date = date(2025, 8, 22)  # 금연 시작일
  ```
- `tweet_text` 부분을 바꿔서 다른 형태의 일기나 챌린지로도 활용 가능
- GitHub Actions `cron` 주기 변경 가능 (`tweet.yml` 안에서)

---

## 💬 문의 / 아이디어
- 금연 외에도 다이어트, 공부, 운동, 습관 기록 등으로 확장 가능  
- 트위터 스레드 자동 관리용 베이스 코드로 활용 가능
