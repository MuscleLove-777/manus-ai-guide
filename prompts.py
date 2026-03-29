"""Manus AI完全ガイド - プロンプト定義

Manus AI特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはAIエージェント技術の日本語エキスパートです。"
    "Meta発の汎用AIエージェントManus AIに精通し、"
    "デスクトップ操作の自動化・ファイル編集・アプリ連携などの実践的な情報を届けるプロのテックライターです。"
    "Manus AIの最新アップデートを常にキャッチアップし、"
    "他のAIエージェント（Devin、Claude Computer Use、AutoGPT等）との比較も客観的に行えます。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・解説。スクリーンショットの代わりに操作手順を箇条書きで明示）

## AIエージェント活用テクニック
（PC操作自動化 / ファイル編集 / ブラウザ操作 / アプリ連携の方法）

## 他のAIエージェントとの比較
（Devin / Claude Computer Use / AutoGPT / Copilot との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "Manus AI 使い方": "Manus AI 使い方、Manus AI 始め方、Manus AI とは、Manus AI 初心者、AIエージェント 使い方",
    "Manus AI 料金・プラン": "Manus AI 料金、Manus AI 無料、Manus AI 有料 違い、Manus AI プラン、AIエージェント 月額",
    "Manus AI vs Devin": "Manus AI Devin 比較、Manus AI Devin 違い、AIエージェント 比較 2026、どっちがいい",
    "Manus AI 最新ニュース": "Manus AI アップデート、Manus AI 新機能、Meta AI 最新、Meet My Computer、Meta 買収",
    "AIエージェント活用": "AIエージェント 活用、PC操作 自動化、ファイル編集 自動化、AIエージェント 業務効率化",
    "Manus AI 開発者向け": "Manus AI API、Manus AI SDK、Manus AI 開発、AIエージェント API 連携",
    "AIエージェント比較": "AIエージェント 比較 2026、Manus AI Claude 比較、AIエージェント おすすめ、自律AI 比較",
    "Manus AI 事例": "Manus AI ビジネス活用、Manus AI 事例、AIエージェント 導入事例、AI 業務自動化",
}

# ニュースソース
NEWS_SOURCES = [
    "Manus AI公式 (https://manus.im)",
    "Meta AI Blog (https://ai.meta.com/blog/)",
    "TechCrunch (https://techcrunch.com/tag/ai-agents/)",
    "The Verge (https://www.theverge.com/ai-artificial-intelligence)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "Manus AI（Meta発の汎用AIエージェント）に関するキーワードを選んでください。\n"
    "日本のユーザーが検索しそうな実用的なキーワードを意識してください。\n"
    "「Manus AI 使い方」「Manus AI 料金」「Manus AI vs Devin」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "Manus AI完全ガイドブログ用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Manus AI特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、Manus AI（Meta発AIエージェント）の専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的な操作手順や設定方法を含める
- PC操作自動化（ファイル編集・ブラウザ操作・アプリ連携等）の活用テクニックを含める
- 他のAIエージェントとの客観的な比較を含める
- 初心者にもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""
