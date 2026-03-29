"""Manus AI完全ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Manus AI完全ガイド"
BLOG_DESCRIPTION = "Meta発の汎用AIエージェントManus AIの使い方・最新情報・活用術を毎日更新。PCを自律操作するAIエージェントの最前線を解説。"
BLOG_URL = "https://musclelove-777.github.io/manus-ai-guide"
BLOG_TAGLINE = "AIがPCを操る時代 — Manus AI完全ガイド"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/manus-ai-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Manus AI 使い方",
    "Manus AI 料金・プラン",
    "Manus AI vs Devin",
    "Manus AI 最新ニュース",
    "AIエージェント活用",
    "Manus AI 開発者向け",
    "AIエージェント比較",
    "Manus AI 事例",
]

THEME = {
    "primary": "#0668E1",
    "accent": "#00C2FF",
    "gradient_start": "#0668E1",
    "gradient_end": "#00C2FF",
    "dark_bg": "#0a0f1e",
    "dark_surface": "#141c30",
    "light_bg": "#f0f7ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "AIツール": [
        {"service": "Manus AI", "url": "https://manus.im", "description": "Manus AIを試す"},
    ],
    "クラウドサービス": [
        {"service": "Meta AI", "url": "https://ai.meta.com", "description": "Meta AI公式サイト"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAIエージェント講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAIエージェント関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAIエージェント関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8093
