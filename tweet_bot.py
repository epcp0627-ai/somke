import tweepy
import os
from datetime import date

# --- 트위터 API 키 불러오기 ---
api_key = os.environ["TWITTER_API_KEY"]
api_key_secret = os.environ["TWITTER_API_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# --- Tweepy 클라이언트 생성 ---
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# --- 금연 시작일 ---
quit_date = date(2025, 8, 22)  # ✅ 금연 시작일
today = date.today()
days = (today - quit_date).days + 1  # n일째 계산

# --- 트윗 내용 생성 ---
tweet_text = f"금연 {days}일차"

# --- 마지막 트윗 ID 파일 경로 ---
LAST_TWEET_FILE = "last_tweet_id.txt"

# --- 마지막 트윗 ID 불러오기 ---
last_tweet_id = None
if os.path.exists(LAST_TWEET_FILE):
    with open(LAST_TWEET_FILE, "r") as f:
        last_tweet_id = f.read().strip() or None

# --- 트윗 작성 ---
try:
    if last_tweet_id:
        response = client.create_tweet(text=tweet_text, in_reply_to_tweet_id=last_tweet_id)
        print(f"Replied to tweet ID {last_tweet_id}")
    else:
        response = client.create_tweet(text=tweet_text)
        print("Posted new main tweet")

    # --- 새 트윗 ID 저장 ---
    new_tweet_id = response.data["id"]
    with open(LAST_TWEET_FILE, "w") as f:
        f.write(str(new_tweet_id))

    print(f"Saved new tweet ID: {new_tweet_id}")
    print(f"✅ Successfully tweeted: {tweet_text}")

except Exception as e:
    print("❌ Error posting tweet:", e)
