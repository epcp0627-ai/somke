import os
import tweepy
from datetime import date

# --- 환경 변수로부터 인증 정보 불러오기 ---
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# --- Tweepy 클라이언트 (API v2) 초기화 ---
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

# --- 이전 트윗 ID 불러오기 ---
TWEET_ID_FILE = "tweet_id.txt"
previous_tweet_id = None
if os.path.exists(TWEET_ID_FILE):
    with open(TWEET_ID_FILE, "r") as f:
        previous_tweet_id = f.read().strip() or None

# --- 금연 시작일 / 오늘 날짜 계산 ---
start_date = date(2025, 8, 22)  # ✅ 금연 시작일
today = date.today()
days = (today - start_date).days + 1

# --- 트윗 내용 ---
tweet_text = f"🚭 금연 {days}일째! 오늘도 참고 있다."

# --- 트윗 작성 (스레드로 이어붙이기) ---
if previous_tweet_id:
    response = client.create_tweet(
        text=tweet_text,
        in_reply_to_tweet_id=previous_tweet_id
    )
else:
    response = client.create_tweet(text=tweet_text)

# --- 새 트윗 ID 저장 ---
new_tweet_id = response.data["id"]
with open(TWEET_ID_FILE, "w") as f:
    f.write(str(new_tweet_id))

print(f"✅ 트윗 완료: {tweet_text} (id={new_tweet_id})")
